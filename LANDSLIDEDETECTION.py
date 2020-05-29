import requests

url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'

data = {'file': open('D:/hhgtg/landslide5.jpg', 'rb'), 'modelId': ('', 'caf6a739-0653-4817-975e-85129afef139')}

response = requests.post(url, auth= requests.auth.HTTPBasicAuth('AOi5uQ1KPoiJ_sRyS03LNhOLM-hBzfSY', ''), files=data)

print(response.text)
