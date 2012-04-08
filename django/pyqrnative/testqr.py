from PyQRNative import QRCode, QRErrorCorrectLevel

try:
    qr = QRCode(4, QRErrorCorrectLevel.M)
    qr.addData("http://www.h3-art.heliohost.org/gift/b1ff2773e2aa9591")
    qr.make()
except ValueError, exc:
    print 'Error!'    
    print exc    
    #raise
except:
    print 'Unknown error'
    raise
else:
    im = qr.makeImage(boxsize = 8, offset = 4)
    im.show()