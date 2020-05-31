import requests
import cv2
import json
import os
import sys
from PIL import Image,ImageDraw,ImageFont


######api cred###########

#########pil#####
font = ImageFont.truetype(font='simple.ttf',size=18)
##font=ImageFont.load_default()
paths=os.listdir('./test_set2/')
##path='./landslide_test/1.jpg'

for it in paths:
    
    path='./test_set2/' + it
    print(path)
  

    url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'
    data = {'file': open(path,'rb'), 'modelId': ('', '90017ee6-3193-4206-b8bd-7bdafcc551d0')}
    response = requests.post(url, auth= requests.auth.HTTPBasicAuth('6JhbrEtb_7ITORrOITZ8beDa5ubgnkJ6', ''), files=data)

    ##    print(response.text)
##    string='{"message":"Success","result":[{"message":"Success","prediction":[{"label":"landslide_detected","probability":0.999361},{"label":"landslide_not_detected","probability":0.00063905714}],"file":"test7.jfif"}]}'

    js=json.loads(response.text)
##    js=json.loads(string)
    res=js['result'][0]['prediction']

    ##print 0th index label and value
    image = Image.open(path)
    image=image.resize((500,500),Image.BILINEAR)
    
    draw=ImageDraw.Draw(image)

    if(res[0]['label']=="landslide_detected"):
        color='rgb(0,250,0)'
    else:
        color='rgb(250,0,0)'

    (x, y) = (20, 20)
    draw.text((x,y),res[0]['label'],fill=color,font=font)
    (x, y) = (20, 50)
    draw.text((x,y),str(res[0]['probability']),fill=color,font=font)

    if(res[1]['label']=="landslide_detected"):
        color='rgb(0,250,0)'
    else:
        color='rgb(250,0,0)'
    (x, y) = (260, 20)
    draw.text((x,y),res[1]['label'],fill=color,font=font)
    (x, y) = (260, 50)
    draw.text((x,y),str(res[1]['probability']),fill=color,font=font)

##    image.show()

    image.save('./output_test_set2/'+it)


print('done')
