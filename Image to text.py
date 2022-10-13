# # #image download
# from bs4 import BeautifulSoup as BSHTML
# import urllib
# import requests


# # page = urllib.request.urlopen('https://mahasldc.in/wp-content/reports/sldc/mvrreport3.jpg')
# # soup = BSHTML(page)
# # print(soup)
# response = requests.get("https://mahasldc.in/wp-content/reports/sldc/mvrreport3.jpg")

# file = open("sample_image.png", "wb")
# file.write(response.content)
# file.close()


#text extraction
import matplotlib.pyplot as plt
import  cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize']=8,16
reader=easyocr.Reader(['en'])
output=reader.readtext('sample_image.png')
print(output)
