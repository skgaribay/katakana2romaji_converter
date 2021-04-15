# katakana2romaji_converter
 takes images of katakana words and attaches a romaji translation
 
# Requirements:
# -Python 2.7.15
#	Python Libraries: (you can download manually and copy to ~\Python27\lib\site-packages
#			   or you can use 'pip install <package>' i.e. 'pip install numpy' *this is done on the terminal/cmd and not within the python environment)	*pip should be available in ~\Python27\Scripts when you have Python installed
#	-numpy 1.15.4
#	-cv2 4.0.0-alpha (python OpenCV library)
#	-Pillow 5.3.0 *(it's supposed to be a requirement for pytesseract but I did not import it in the code)
#	-pytesseract 0.2.5 (requires Tesseract OCR program)
# -Tesseract OCR 3.05.02
#	-available at https://github.com/UB-Mannheim/tesseract/wiki
#	-download the latest .exe (should be tesseract-ocr-setup-3.05.02-20180621.exe as of 12/16/18) and run.
#	-we have provided the necessary training data file 'jpn.traineddata'. Just copy to ~\Tesseract-OCR\tessdata

# Instructions:
# -within the terminal/cmd, 'python katakana2romaji.py'
# -This version of the code will run indefinitely as to accept continuous inputs. Just click 'No' at the prompt after each translation if you want to exit.
# -The chosen input image will pop up in a window. Click that window and press any key to continue. DO NOT EXIT THE WINDOW USING THE 'X' BUTTON.
# -The output image will pop up showing the image with the translation superimposed. Press 's' on the keyboard to save (you will have to input the file name and file type) or press any other key to ignore.

# -In windows, the program is typically run within the ~\Python27\ directory. If you want to run it in the same folder as the files, you need to add python to the windows PATH file.
# -To add python to the PATH file: https://superuser.com/questions/143119/how-do-i-add-python-to-the-windows-path
# -This way, the program may be run with a double-click. Just make sure to set python as the default program for .py files.

# please email Kris Garibay (sggaribay@up.edu.ph) for any questions.
