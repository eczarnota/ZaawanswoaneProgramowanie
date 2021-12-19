import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def readTextFromImg(img: str):
    img = cv2.imread(img)
    img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print(pytesseract.image_to_string(img_convert))

#readTextFromImg('zdj1.jpg')
readTextFromImg('zdj2.jpg')