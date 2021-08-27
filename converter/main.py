import bt
import convert
import cv2
path = input("Please enter the path of the image : ")
image_name = input("Please enter the image name (imagename.jpg) : ")
image_name = '/' + image_name
image = cv2.imread(path + image_name)
image_thresh = bt.blurNthresh(image)
cv2.imwrite(path + "/jpgimage.jpg", image_thresh)
convert.jpgToPdf(path + '/jpgimage.jpg')






