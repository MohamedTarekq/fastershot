from concurrent.futures import ThreadPoolExecutor
import requests
import urllib.parse
import sys,os
import argparse

parser = argparse.ArgumentParser(description='faster tool to take a screenshot to list of urls')
parser.add_argument("-l" , help="List of urls" ,type=str)
parser.add_argument("-n" , help="Number of requests per seconde default is 15" , default=15 , type=int)
args = parser.parse_args()

if not os.path.exists('result'):
    os.makedirs('result')
path = 'result/'

file = open(args.l,'r').readlines()
BASE = 'https://render-tron.appspot.com/screenshot/' 

def download(i): 
    s = i.strip()
    url = urllib.parse.quote_plus(s)
    response = requests.get(url=BASE + url,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125'} , proxies={'http':'http://127.0.0.1:8080'}, stream=True)  
    if response.status_code == 200:
     sys.stdout.write(s+'\x1b[32m'+" [OK]\x1b[39m\n")
     pic = s.replace("://", ".")
     with open(path+pic+'.jpg', 'wb') as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)
    else :
     sys.stdout.write(s+'\x1b[31m'+" [Failed]\x1b[39m\n")

if __name__ == "__main__":
  
    with ThreadPoolExecutor(max_workers=args.n) as pool:
        pool.map(download, file)