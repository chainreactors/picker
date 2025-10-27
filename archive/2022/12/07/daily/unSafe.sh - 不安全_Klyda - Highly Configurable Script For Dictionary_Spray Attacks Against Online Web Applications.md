---
title: Klyda - Highly Configurable Script For Dictionary/Spray Attacks Against Online Web Applications
url: https://buaq.net/go-138836.html
source: unSafe.sh - 不安全
date: 2022-12-07
fetch_date: 2025-10-04T00:38:44.074396
---

# Klyda - Highly Configurable Script For Dictionary/Spray Attacks Against Online Web Applications

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

![](https://8aqnet.cdn.bcebos.com/b974d981d22cfcbcabb0a522be94fbe4.jpg)

Klyda - Highly Configurable Script For Dictionary/Spray Attacks Against Online Web Applications

The Klyda project has been created to aid in quick credential based attacks against online
*2022-12-6 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-138836.htm)
阅读量:26
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh3qH_uSHEBDdaKHa2u9OrKTxobiij1SJUy23EDpdiUHL9__GQ409x14dCOXyG0XK_w0zrSheyLxvcE2T5o5NPz72juRYWHvdrsCYn5x--YTODZn_Q-3YnGB19TpU7IMMqQMykrxUOyKKX9OYr7PX06kjfzeo7Mb89ah6Qxc3q-I2vlT8elCB93tlFEBA=w400-h140)](https://blogger.googleusercontent.com/img/a/AVvXsEh3qH_uSHEBDdaKHa2u9OrKTxobiij1SJUy23EDpdiUHL9__GQ409x14dCOXyG0XK_w0zrSheyLxvcE2T5o5NPz72juRYWHvdrsCYn5x--YTODZn_Q-3YnGB19TpU7IMMqQMykrxUOyKKX9OYr7PX06kjfzeo7Mb89ah6Qxc3q-I2vlT8elCB93tlFEBA)

The Klyda project has been created to aid in quick credential based attacks against online web applications.

Klyda is a new project, and I am looking for any contributions. Any help is very appreciated.

Klyda offers simple, easy to remember usage; however, still offers configurability for your needs:

* Mulithreaded tasks
* Combine wordlists for larger scale attacks
* Blacklisting data to narrow down results
* Limit thread speed for sneaky purposes

[![](https://blogger.googleusercontent.com/img/a/AVvXsEifeCMtH_0bToV4FgI0gFFl_d2kho5pOqF2dKw75I9f8E2U0QIqwIPP_0ACEqiFoyRfq-22s2KHf_NcQraNP-lNGclJBkcJh8s9OTI1B1mso5k76ll9n0MzNDDDOeQ1HRO2qsV0_Hl2lvPp7mu1RqtFzRuJVw9SE0Wav5k9SMx-MSa4e8SSovszvjEAuA=w640-h332)](https://blogger.googleusercontent.com/img/a/AVvXsEifeCMtH_0bToV4FgI0gFFl_d2kho5pOqF2dKw75I9f8E2U0QIqwIPP_0ACEqiFoyRfq-22s2KHf_NcQraNP-lNGclJBkcJh8s9OTI1B1mso5k76ll9n0MzNDDDOeQ1HRO2qsV0_Hl2lvPp7mu1RqtFzRuJVw9SE0Wav5k9SMx-MSa4e8SSovszvjEAuA)

**1)** Clone the Git repo to your machine, `git clone https://github.com/Xeonrx/Klyda`
 **2)** Cd into the Klyda directory, `cd Klyda`
 **3)** Install the neccessary modules via Pip, `pip install requests [beautifulsoup4](https://www.kitploit.com/search/label/Beautifulsoup4 "beautifulsoup4") colorama numpy`
 **4)** Display the Klyda help prompt for usage, `python3 klyda.py -h`

> Klyda has been mainly designed for Linux, but should work on any machine capable of running Python.

What Klyda needs to work are only four simple dependencies: URL to attack, username(s), password(s), and formdata.

## The URL

You can parse the URL via the `--url` tag. It should look something like this, `--url http://127.0.0.1`
 Remember to **never** launch an attack on a webpage, that you don't have proper permission to do so.

## Usernames

Usernames are the main target to these dictionary attacks. It could be a whole range of usernames, a few in specific, or perhaps just one. That's all your decision when using the script. You can specify usernames in a few ways...

**1)** Specify them manually, `-u Admin User123 Guest`
 **2)** Give a file to use, or a few to combine, `-U users.txt extra.txt`
 **3)** Give both a file & manual entry, `-U users.txt -u Johnson924`

## Passwords

Passwords are the hard part to these attacks. You don't know them, hence why dictionary & [brute force attacks](https://www.kitploit.com/search/label/Brute%20Force%20Attacks "brute force attacks") exists. Like the usernames, you can give from just one password, up to however many you want. You can specify passwords in a few ways...

**1)** Specify them manually, `-p password 1234 letmein`
 **2)** Give a file to use, or a few to combine, `-P passwords.txt extra.txt`
 **3)** Give both a file & manual entry, `-P passwords.txt -p redklyda24`

## FormData

FormData is how you form the request, so the target website can take it in, and process the given information. Usually you would need to specify a: username value, a password value, and sometimes an extra value. You can see the FormData your target uses by reviewing the network tab, of your browsers inspect element. For Klyda, you use the `-d` tag.

You need to use placeholders to Klyda knows where to inject in the username & password, when fowarding out its requests. It may look something like this... `-d username:xuser password:xpass Login:Login`

`xuser` is the placeholder to inject the usernames, & `xpass` is the placeholder to inject the passwords. Make sure you know these, or Klyda won't be able to work.

Format the FormData as `(key):(value)`

## Blacklists

In order to Klyda to know if it hit a successful strike or not, you need to give it data to dig through. Klyda takes use of given blacklists from failed login attempts, so it can tell the difference between a failed or complete request. You can blacklist three different types of data...

**1)** Strings, `--bstr "Login failed"`
 **2)** Status Codes, `--bcde 404`
 **3)** Content Length, `--blen 11`

You can specify as much data for each blacklist as needed. If any of the given data is not found from the response, Klyda gives it a "strike", saying it was a successful login attempt. Otherwise if data in the blacklists is found, Klyda marks it as an unsuccessful login attempt. Since you give the data for Klyda to evaluate, false positives are non-apparent.

> If you don't give any data to blacklist, then every request will be marked as a strike from Klyda!

## Rate limiting & Threads

By default, Klyda only uses a single thread to run; but, you can specify more, using the `-t` tag. This can be helpful for speeding up your work.

However, credential attacks can be **very** loud on a network; hence, are detected easily. A targeted account could simply just receieve a simple lock due to too many login attempts. This creates a DoS attack, but prevents you from gaining the users's credentials, which is the goal of Klyda.

So to make these attacks a little less loud, you can take use of the `--rate` tag. This allows you to limit your threads to a certain number of requests per minute.
 It will be formatted like this, `--rate (# of requests) (minutes)`

For example, `--rate 5 1` will only send out 5 requests for each minute. Remember, this is for each thread. If you had 2 threads, this would send 10 requests per minute.

## Example

Test Klyda out on the [Damn Vulnerable](https://www.kitploit.com/search/label/Damn%20Vulnerable "Damn Vulnerable") Web App (DVWA), or Mutillidae.

`python3 klyda.py --url http://127.0.0.1/dvwa/login.php -u user guest admin -p 1234 password admin -d username:xuser password:xpass Login:Login --bstr "Login failed"`

`python3 klyda.py --url http://127.0.0.1/mutillidae/index.php?page=login.php -u root -P passwords.txt -d username:xuser password:xpass login-php-submit-button:Login --bstr "Authentication Error"`

## The Future

Like mentioned earlier, Klyda is still a work in progress. For the future, I plan on adding more functionality and reformating code for a cleaner look.

My top piority is to add proxy functionality, and am currently working on it.

Klyda - Highly Configurable Script For Dictionary/Spray Attacks Against Online Web Applications
![Klyda - Highly Configurable Script For Dictionary/Spray Attacks Against Online Web Applications](https://blogger.googleusercontent.com/img/a/AVvXsEh3qH_uSHEBDdaKHa2u9OrKTxobiij1SJUy23EDpdiUHL9__GQ409x14dCOXyG0XK_w0zrSheyLxvcE2T5o5NPz72juRYWHvdrsCYn5x--YTODZn_Q-3YnGB19TpU7IMMqQMykrxUOyKKX9OYr7PX06kjfzeo7Mb89ah6Qxc3q-I2vlT8elCB93tlFEBA=s72-w400-c-h140)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/12/klyda-highly-configurable-script-for.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克...