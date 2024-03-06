from qreader import QReader
import urllib.request
import cv2


# Create a QReader instance
qreader = QReader()

# Get the image that contains the QR code
image = cv2.cvtColor(cv2.imread("url.png"), cv2.COLOR_BGR2RGB)

# Use the detect_and_decode function to get the decoded QR data
URL = qreader.detect_and_decode(image=image)
print(URL)
