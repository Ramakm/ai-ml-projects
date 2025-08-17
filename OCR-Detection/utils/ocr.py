import easyocr
import cv2

reader = easyocr.Reader(["en"])  # You can add ["en", "tr"] if Turkish plates

def extract_text(image):
    if image is None:
        return ""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = reader.readtext(gray)
    text = " ".join([res[1] for res in result])
    return text
