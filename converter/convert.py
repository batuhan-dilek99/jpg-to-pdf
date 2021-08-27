from PIL import Image

def jpgToPdf(image_name) : 
    jpgImage = Image.open(r'C:/Users/Batuhan/Desktop/converter/jpgimage.jpg')
    pdfImage = jpgImage.convert('RGB')
    pdfImage.save(r'C:/Users/Batuhan/Desktop/converter/pdfImage.pdf')
