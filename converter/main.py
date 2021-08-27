import bt
import convert
import cv2
import os


try:
    path = input("Please enter the path of the file : ")
    image_name = input("Please enter the image name (imagename.jpg) : ")
    pdf_path = path + "/pdfs"
    image_path = path + "/images"
except:
    print("There is no such path or image. Check and try again")


try:
    image_name = '/' + image_name
    image = cv2.imread(image_path + image_name)
    image_thresh = bt.blurNthresh(image)
    cv2.imwrite(path + "/images/jpgimage.jpg", image_thresh)
    convert.jpgToPdf(image_path, pdf_path)
    print(image_name[1:30] + " has successfully converted to pdf at : " + pdf_path)
    try:
        os.remove(image_path + "/jpgimage.jpg")
    except : pass
except:
    print("An error has been accured. try again")






