from PIL import Image

def jpgToPdf(image_path, pdf_path) : 
    try:
        jpgImage = Image.open(image_path + '/jpgimage.jpg')
        pdfImage = jpgImage.convert('RGB')
        pdfImage.save(pdf_path + '/pdfImage.pdf')
    except:
        print("Could not load the image")
