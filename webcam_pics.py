import cv2
import time
import boto3
from PIL import Image 

s3_client = boto3.client('s3')
# a=int(input('enter number of imgs u want to be clicked: '))
a=10	//u can change no. of clicks acc to ur requirement
camera = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
for i in range(a):
    return_value, image = camera.read()

    image_string = cv2.imencode('.jpg', image)[1].tobytes()

    s3_client.put_object(Bucket="abc12345", Key = 'img'+str(i)+'.png', Body=image_string, ContentType='png')   //create S3 bucket and replace name with ur S3 bucket name
    print(i)
    time.sleep(5)
del(camera)
cv2.destroyAllWindows()
