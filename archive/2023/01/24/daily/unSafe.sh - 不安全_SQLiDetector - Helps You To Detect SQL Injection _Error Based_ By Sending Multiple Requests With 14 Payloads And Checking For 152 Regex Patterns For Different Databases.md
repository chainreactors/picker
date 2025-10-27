---
title: SQLiDetector - Helps You To Detect SQL Injection "Error Based" By Sending Multiple Requests With 14 Payloads And Checking For 152 Regex Patterns For Different Databases
url: https://buaq.net/go-146539.html
source: unSafe.sh - 不安全
date: 2023-01-24
fetch_date: 2025-10-04T04:37:01.178533
---

# SQLiDetector - Helps You To Detect SQL Injection "Error Based" By Sending Multiple Requests With 14 Payloads And Checking For 152 Regex Patterns For Different Databases

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

![](https://8aqnet.cdn.bcebos.com/394edb7fe9a040b33c921597e7ccc61e.jpg)

SQLiDetector - Helps You To Detect SQL Injection "Error Based" By Sending Multiple Requests With 14 Payloads And Checking For 152 Regex Patterns For Different Databases

Simple python script supported with BurpBouty profile that helps you to detect SQL injection
*2023-1-23 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-146539.htm)
阅读量:38
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgXWgMVyPOQMnB8xYQu9D3OwsksGjSzDfDdbM4krDBliNJFnHvfwHDoOAa6af1BY4BfqWxJSLnJTmV7tKYag0ziRQKqP3Nd4FlM4wICNO-fdBTpH0N367pe8jfoyY9IB6AVTxAhRleyq6m_33CYdWKkTeG6upEn2nytMWwRocp0z1eCXNJpfo7ClAsaHA=w640-h164)](https://blogger.googleusercontent.com/img/a/AVvXsEgXWgMVyPOQMnB8xYQu9D3OwsksGjSzDfDdbM4krDBliNJFnHvfwHDoOAa6af1BY4BfqWxJSLnJTmV7tKYag0ziRQKqP3Nd4FlM4wICNO-fdBTpH0N367pe8jfoyY9IB6AVTxAhRleyq6m_33CYdWKkTeG6upEn2nytMWwRocp0z1eCXNJpfo7ClAsaHA)

Simple python script supported with BurpBouty profile that helps you to detect SQL injection "Error based" by sending multiple requests with 14 payloads and checking for 152 regex patterns for different databases.

```
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
```

## Description

The main idea for the tool is scanning for Error Based SQL [Injection](https://www.kitploit.com/search/label/Injection "Injection") by using different payloads like

```
'123
''123
`123
")123
"))123
`)123
`))123
'))123
')123"123
[]123
""123
'"123
"'123
\123
```

And match for 152 error regex patterns for different databases.
 Source: [https://github.com/sqlmapproject/sqlmap/blob/master/data/xml/errors.xml](https://github.com/sqlmapproject/sqlmap/blob/master/data/xml/errors.xml "https://github.com/sqlmapproject/sqlmap/blob/master/data/xml/errors.xml")

## How does it work?

It's very simple, just organize your steps as follows

1. Use your subdomain grabber script or tools.
2. Pass all collected [subdomains](https://www.kitploit.com/search/label/Subdomains "subdomains") to httpx or httprobe to get only live subs.
3. Use your links and URLs tools to grab all [waybackurls](https://www.kitploit.com/search/label/Waybackurls "waybackurls") like waybackurls, gau, gauplus, etc.
4. Use URO tool to filter them and reduce the noise.
5. Grep to get all the links that contain parameters only. You can use Grep or GF tool.
6. Pass the final URLs file to the tool, and it will test them.

The final schema of URLs that you will pass to the tool must be like this one

```
https://aykalam.com?x=test&y=fortest
http://test.com?parameter=ayhaga
```

## Installation and Usage

Just run the following command to install the required libraries.

```
~/eslam3kl/SQLiDetector# pip3 install -r requirements.txt
```

To run the tool itself.

```
# cat urls.txt
http://testphp.vulnweb.com/artists.php?artist=1

# python3 sqlidetector.py -h
usage: sqlidetector.py [-h] -f FILE [-w WORKERS] [-p PROXY] [-t TIMEOUT] [-o OUTPUT]
A simple tool to detect SQL errors
optional arguments:
  -h, --help            show this help message and exit]
  -f FILE, --file FILE  [File of the urls]
  -w WORKERS, --workers [WORKERS Number of threads]
  -p PROXY, --proxy [PROXY Proxy host]
  -t TIMEOUT, --timeout [TIMEOUT Connection timeout]
  -o OUTPUT, --output [OUTPUT [Output file]

# python3 sqlidetector.py -f urls.txt -w 50 -o output.txt -t 10
```

## BurpBounty Module

I've created a burpbounty profile that uses the same payloads add injecting them at multiple positions like

* Parameter name
* Parameter value
* Headers
* Paths

I think it's more effective and will helpful for POST request that you can't test them using the Python script. [![](https://blogger.googleusercontent.com/img/a/AVvXsEgDC_vTjRS0rlmO6BkOiIkrerHtg8jlCP64gkGjLBQjOHIJ_DRJFknunCpKDiCUqhN5uFXa7xwLdYAzQkqEZX0c-r7WuhnIC5eRCyWT0t-NsiE76f8MNemKZHUqIq8byIbkmk_PUfV_rSocKFtQE_3Ou_mwfWLvdIcoHqSygKJXAYQwcpR7e345XnGEeQ=w640-h336)](https://blogger.googleusercontent.com/img/a/AVvXsEgDC_vTjRS0rlmO6BkOiIkrerHtg8jlCP64gkGjLBQjOHIJ_DRJFknunCpKDiCUqhN5uFXa7xwLdYAzQkqEZX0c-r7WuhnIC5eRCyWT0t-NsiE76f8MNemKZHUqIq8byIbkmk_PUfV_rSocKFtQE_3Ou_mwfWLvdIcoHqSygKJXAYQwcpR7e345XnGEeQ)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhYYsYXa4uAXopGl_ElKGo0jkOFT6lD2gPatGmAGFpt5DXuh3B_2ZEZyqwghrnawGdi0GblIcD4yLWt2rNQDXpYkpXW7LoLR1J-ornvzDwe9SISKsHQc0fje0J-FyF4VpWbAqYgRiSgDoIKluOhrlU9H-xD7A6S9XyEMY3tyO1BrZjPwHh_Qu5jSk-Rfg=w640-h356)](https://blogger.googleusercontent.com/img/a/AVvXsEhYYsYXa4uAXopGl_ElKGo0jkOFT6lD2gPatGmAGFpt5DXuh3B_2ZEZyqwghrnawGdi0GblIcD4yLWt2rNQDXpYkpXW7LoLR1J-ornvzDwe9SISKsHQc0fje0J-FyF4VpWbAqYgRiSgDoIKluOhrlU9H-xD7A6S9XyEMY3tyO1BrZjPwHh_Qu5jSk-Rfg)

## How does it test the parameter?

What's the difference between this tool and any other one? If we have a link like this one `https://example.com?file=aykalam&username=eslam3kl` so we have 2 parameters. It creates 2 possible [vulnerable](https://www.kitploit.com/search/label/Vulnerable "vulnerable") URLs.

1. It will work for every payload like the following

```
https://example.com?file=123'&username=eslam3kl
https://example.com?file=aykalam&username=123'
```

2. It will send a request for every link and check if one of the patterns is existing using regex.
3. For any vulnerable link, it will save it at a separate file for every process.

## Upcoming updates

* Output json option.
* Adding proxy option.
* Adding threads to increase the speed.
* Adding progress bar.
* Adding more payloads.
* Adding [BurpBounty](https://www.kitploit.com/search/label/BurpBounty "BurpBounty") Profile.
* Inject the payloads in the parameter name itself.

If you want to contribute, feel free to do that. You're welcome :)

## Thanks to

Thanks to Mohamed El-Khayat and Orwa for the amazing paylaods and ideas. Follow them and you will learn more

```
https://twitter.com/Mohamed87Khayat
https://twitter.com/GodfatherOrwa
```

## Stay in touch <3

[LinkedIn](https://www.linkedin.com/in/eslam3kl/ "LinkedIn") | [Blog](https://eslam3kl.medium.com/ "Blog") | [Twitter](https://twitter.com/eslam3kll "Twitter")

SQLiDetector - Helps You To Detect SQL Injection "Error Based" By Sending Multiple Requests With 14 Payloads And Checking For 152 Regex Patterns For Different Databases
![SQLiDetector - Helps You To Detect SQL Injection "Error Based" By Sending Multiple Requests With 14 Payloads And Checking For 152 Regex Patterns For Different Databases](https://blogger.googleusercontent.com/img/a/AVvXsEgXWgMVyPOQMnB8xYQu9D3OwsksGjSzDfDdbM4krDBliNJFnHvfwHDoOAa6af1BY4BfqWxJSLnJTmV7tKYag0ziRQKqP3Nd4FlM4wICNO-fdBTpH0N367pe8jfoyY9IB6AVTxAhRleyq6m_33CYdWKkTeG6upEn2nytMWwRocp0z1eCXNJpfo7ClAsaHA=s72-w640-c-h164)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/01/sqlidetector-helps-you-to-detect-sql.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)