---
title: ScrapPY - A Python Utility For Scraping Manuals, Documents, And Other Sensitive PDFs To Generate Wordlists That Can Be Utilized By Offensive Security Tools
url: https://buaq.net/go-171195.html
source: unSafe.sh - 不安全
date: 2023-07-05
fetch_date: 2025-10-04T11:52:24.584071
---

# ScrapPY - A Python Utility For Scraping Manuals, Documents, And Other Sensitive PDFs To Generate Wordlists That Can Be Utilized By Offensive Security Tools

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

![](https://8aqnet.cdn.bcebos.com/baeb19ec43a35d5ce038f301c73ac5ba.jpg)

ScrapPY - A Python Utility For Scraping Manuals, Documents, And Other Sensitive PDFs To Generate Wordlists That Can Be Utilized By Offensive Security Tools

ScrapPY is a Python utility for scraping manuals, documents, and other sensitive PDFs to gen
*2023-7-4 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-171195.htm)
阅读量:21
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0WPDWA4xy3vRr-FR7VAoy_5LzwFfHR5KEvQwsV2XxhIYm4oXUtUI_U9RZ4U3h7KyeDWNrgeRHzkSueUe2BymxIgjaKl41n0MiKbFnHswHihduDRSPGcdXsf2In5Y9omQ8pA7w9Y3eIUpVRgeTXtGW_d7CV79qrulN3N-v1eMBfutmcpKAZgGWKMfrnvlX/w640-h640/ScrapPY.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0WPDWA4xy3vRr-FR7VAoy_5LzwFfHR5KEvQwsV2XxhIYm4oXUtUI_U9RZ4U3h7KyeDWNrgeRHzkSueUe2BymxIgjaKl41n0MiKbFnHswHihduDRSPGcdXsf2In5Y9omQ8pA7w9Y3eIUpVRgeTXtGW_d7CV79qrulN3N-v1eMBfutmcpKAZgGWKMfrnvlX/s1772/ScrapPY.png)

ScrapPY is a Python utility for scraping manuals, documents, and other sensitive PDFs to generate targeted wordlists that can be utilized by offensive security tools to perform brute force, forced browsing, and [dictionary](https://www.kitploit.com/search/label/Dictionary "dictionary") attacks. ScrapPY performs word frequency, entropy, and metadata analysis, and can run in full output modes to craft custom wordlists for targeted attacks. The tool dives deep to discover keywords and phrases leading to potential passwords or hidden directories, outputting to a text file that is readable by tools such as Hydra, Dirb, and Nmap. Expedite initial access, [vulnerability](https://www.kitploit.com/search/label/Vulnerability "vulnerability") discovery, and [lateral movement](https://www.kitploit.com/search/label/Lateral%20Movement "lateral movement") with ScrapPY!

Download Repository:

```
$ mkdir ScrapPY
```

Install Dependencies:

```
$ pip3 install -r requirements.txt
```

```
usage: ScrapPY.py [-h] [-f FILE] [-m {word-frequency,full,metadata,entropy}] [-o OUTPUT]
```

Output metadata of document:

```
$ python3 ScrapPY.py -f example.pdf -m metadata
```

Output top 100 frequently used keywords to a file name `Top_100_Keywords.txt`:

```
$ python3 ScrapPY.py -f example.pdf -m word-frequency -o Top_100_Keywords.txt
```

Output all keywords to default ScrapPY.txt file:

```
$ python3 ScrapPY.py -f example.pdf
```

Output top 100 keywords with highest entropy rating:

```
$ python3 ScrapPY.py -f example.pdf -m entropy
```

ScrapPY Output:

```
# ScrapPY outputs the ScrapPY.txt file or specified name file to the directory in which the tool was ran. To view the first fifty lines of the file, run this command:

$ head -50 ScrapPY.txt

# To see how many words were generated, run this command:

$ wc -l ScrapPY.txt
```

Easily integrate with tools such as Dirb to expedite the process of discovering hidden subdirectories:

```
[email protected]:~# dirb http://192.168.1.123/ /root/ScrapPY/ScrapPY.txt

-----------------
DIRB v2.21
By The Dark Raver
-----------------

START_TIME: Fri May 16 13:41:45 2014
URL_BASE: http://192.168.1.123/
WORDLIST_FILES: /root/ScrapPY/ScrapPY.txt

-----------------

GENERATED WORDS: 4592

---- Scanning URL: http://192.168.1.123/ ----
==> DIRECTORY: http://192.168.1.123/vi/
+ http://192.168.1.123/programming (CODE:200|SIZE:2726)
+ http://192.168.1.123/s7-logic/ (CODE:403|SIZE:1122)
==> DIRECTORY: http://192.168.1.123/config/
==> DIRECTORY: http://192.168.1.123/docs/
==> DIRECTORY: http://192.168.1.123/external/
```

Utilize ScrapPY with Hydra for advanced [brute force](https://www.kitploit.com/search/label/Brute%20Force "brute force") attacks:

```
[email protected]:~# hydra -l root -P /root/ScrapPY/ScrapPY.txt -t 6 ssh://192.168.1.123
Hydra v7.6 (c)2013 by van Hauser/THC & David Maciejak - for legal purposes only

Hydra (http://www.thc.org/thc-hydra) starting at 2014-05-19 07:53:33
[DATA] 6 tasks, 1 server, 1003 login tries (l:1/p:1003), ~167 tries per task
[DATA] attacking service ssh on port 22
```

Enhance Nmap scripts with ScrapPY wordlists:

```
nmap -p445 --script smb-brute.nse --script-args userdb=users.txt,passdb=ScrapPY.txt 192.168.1.123
```

## Future Development:

* Allow for custom output file naming and increased verbosity
* Integrate different modes of operation including word frequency analysis
* Allow for metadata analysis
* Search for high-entropy data
* Search for path-like data
* Implement image OCR to enumerate data from images in PDFs
* Allow for processing of multiple PDFs

ScrapPY - A Python Utility For Scraping Manuals, Documents, And Other Sensitive PDFs To Generate Wordlists That Can Be Utilized By Offensive Security Tools
![ScrapPY - A Python Utility For Scraping Manuals, Documents, And Other Sensitive PDFs To Generate Wordlists That Can Be Utilized By Offensive Security Tools](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0WPDWA4xy3vRr-FR7VAoy_5LzwFfHR5KEvQwsV2XxhIYm4oXUtUI_U9RZ4U3h7KyeDWNrgeRHzkSueUe2BymxIgjaKl41n0MiKbFnHswHihduDRSPGcdXsf2In5Y9omQ8pA7w9Y3eIUpVRgeTXtGW_d7CV79qrulN3N-v1eMBfutmcpKAZgGWKMfrnvlX/s72-w640-c-h640/ScrapPY.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/07/scrappy-python-utility-for-scraping.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)