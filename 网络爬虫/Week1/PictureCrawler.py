import requests
import os

url = "http://img0.dili360.com/rw9/ga/M00/49/2D/wKgBzFoL9BKAaDXlAAJA4oYZYZA649.tub.jpg"
path = "D:/" + url.split('/')[-1]
r = requests.get(url)
print(r.status_code)
with open(path,'wb') as f:
    f.write(r.content)
    f.close()