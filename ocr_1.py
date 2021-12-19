import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def readTextFromImg(image: str):
    img = cv2.imread(image)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(pytesseract.image_to_string(img))

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    converted_img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    print(pytesseract.image_to_string(converted_img))

    cv2.imshow('image', converted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    converted_img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    print(pytesseract.image_to_string(converted_img))

    cv2.imshow('image', converted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    converted_img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    print(pytesseract.image_to_string(converted_img))

    cv2.imshow('image', converted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    converted_img = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    print(pytesseract.image_to_string(converted_img))

    cv2.imshow('image', converted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    converted_img = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    print(pytesseract.image_to_string(converted_img))

    cv2.imshow('image', converted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    converted_img = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    print(pytesseract.image_to_string(converted_img))

    cv2.imshow('image', converted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

readTextFromImg("captcha2.jpg")