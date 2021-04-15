import numpy as np 
import cv2
import pytesseract
import os
import easygui

os.system('cls')
    
while True:
    fname = easygui.fileopenbox()
    print 'Opened ' + fname
    img = cv2.imread(fname,0)

    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #preprocessing
    strel = np.ones((9,9),np.uint8)
    bw = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,2)# adaptive threshold plus complement
    bw = cv2.morphologyEx(bw, cv2.MORPH_OPEN, strel)#morph open

    strel = np.ones((5,5),np.uint8)
    bwD = cv2.dilate(bw,strel,iterations = 3)#morph dilation

    vProj = cv2.reduce(bwD, 0, cv2.REDUCE_SUM, dtype=cv2.CV_32S)#get vertical projection / sum of all rows reduced to one row
    vProj[vProj > 0] = 255#converts to pseudo 'logical'

    xline = np.nonzero(vProj)#indeces of all white
    canvas = bwD.copy()

    for i in xline[1]:
        canvas[:,i] = 255

    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(canvas, 8, cv2.CV_32S)#connected components

    c2 = centroids[2:nlabels,0] 
    c1 = centroids[1:nlabels-1,0]
    spaces =  c2-c1
    aveSpace =  np.mean(spaces)

    for i in range(0,len(spaces)):
        if spaces[i] < 0.8*aveSpace:
            for j in range(int(c1[i]),int(c2[i])):
                canvas[:,j] = 255

    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(canvas, 8, cv2.CV_32S)#connected components
    x = stats[0:,cv2.CC_STAT_LEFT]
    y = stats[0:,cv2.CC_STAT_TOP]
    w = stats[0:,cv2.CC_STAT_WIDTH]
    h = stats[0:,cv2.CC_STAT_HEIGHT]

    bboxes = np.empty([nlabels-1,1,4],dtype=int)#bounding box matrix

    for i in range(1,nlabels):
        holder = bwD[y[i]:y[i]+h[i],x[i]:x[i]+w[i]]
        arr = np.nonzero(holder)
        x1 = x[i]#leftmost pixel
        x2 = max(arr[1]) - min(arr[1])#width
        y1 = min(arr[0])#topmost pixel
        y2 = max(arr[0]) - min(arr[0])#height
        bboxes[i-1] = np.array([x1, x2, y1, y2])

    config = ("-l jpn --oem 3 --psm 10")
    result = ''

    for i in range(0,len(bboxes)):
        x1 = bboxes[i,0,0]
        x2 = bboxes[i,0,1]
        y1 = bboxes[i,0,2]
        y2 = bboxes[i,0,3]

        roi = img[y1:y1+y2,x1:x1+x2] #Region of image to feed to tessaract
        text = pytesseract.image_to_string(roi, config=config)
        result = result + text + ' '

    cv2.putText(img, result, (bboxes[0,0,0],max(bboxes[:,0,3])),
            cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)

    cv2.imshow('image',img)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.destroyAllWindows()
        sname = easygui.filesavebox()
        cv2.imwrite(sname,img)
        cv2.destroyAllWindows()
        print 'Image saved as ' + sname

    if not easygui.ynbox('Shall I continue?', 'Title', ('Yes', 'No')):
        break
