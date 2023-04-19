# Main file

import cv2
import pytesseract
import numpy as np
import PIL


if __name__ == "__main__":
    # specify which command can be used for tesseract
    pytesseract.pytesseract.tesseract_cmd = "tesseract"

    # use pytesseract to get text from image
    text = pytesseract.image_to_string(np.array(PIL.Image.open("testimage1.png")))
    print("Text: \n" + text)
