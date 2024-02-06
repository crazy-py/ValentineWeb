
# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
s = " https://crazy-py.github.io/ValentineWeb/"
  
# Generate QR code 
url = pyqrcode.create(s) 
    
# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale = 6) 

print("QR Code Generated")