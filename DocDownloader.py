from tqdm import tqdm
from time import sleep
import requests


a=input("Enter the Magent link of Doc File: ")
url = a
r= requests.get(url, stream=True)
TotalByte= int(r.headers["content-length"])
for i in tqdm(range(0, TotalByte), desc ="File Downloaded : "):
	pass
fp=open("1mb_file.doc","wb")

fp.write(r.content)
fp.close()