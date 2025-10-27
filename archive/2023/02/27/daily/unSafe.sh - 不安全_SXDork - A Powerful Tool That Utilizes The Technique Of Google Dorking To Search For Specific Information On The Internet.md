---
title: SXDork - A Powerful Tool That Utilizes The Technique Of Google Dorking To Search For Specific Information On The Internet
url: https://buaq.net/go-151047.html
source: unSafe.sh - 不安全
date: 2023-02-27
fetch_date: 2025-10-04T08:10:13.012092
---

# SXDork - A Powerful Tool That Utilizes The Technique Of Google Dorking To Search For Specific Information On The Internet

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

![](https://8aqnet.cdn.bcebos.com/6d1497bf3d30a6916b1e259dc8d58fef.jpg)

SXDork - A Powerful Tool That Utilizes The Technique Of Google Dorking To Search For Specific Information On The Internet

SXDork is a powerful tool that utilizes the technique of google dorking to search for specif
*2023-2-26 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-151047.htm)
阅读量:48
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEis1hpOEGZBnvC_H-a1f3EnLkA8LWGuR5YGf65VeiMtZU2z-hFP9-19-SQgBqfNw_YU_7Fw54l4E9Lgi2ai_8GgFDcNRJuGNUpzue1d_65gW1wUjrdN28SLvuOdpsdrnjSghhoapftNgiar0ErHJkj-43sO636ifuvqff-MCS9wjFU9eKxkxanTRE58aQ/w640-h360/SXDork_8_SXDork.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEis1hpOEGZBnvC_H-a1f3EnLkA8LWGuR5YGf65VeiMtZU2z-hFP9-19-SQgBqfNw_YU_7Fw54l4E9Lgi2ai_8GgFDcNRJuGNUpzue1d_65gW1wUjrdN28SLvuOdpsdrnjSghhoapftNgiar0ErHJkj-43sO636ifuvqff-MCS9wjFU9eKxkxanTRE58aQ/s1920/SXDork_8_SXDork.gif)

SXDork is a powerful tool that utilizes the technique of google [dorking](https://www.kitploit.com/search/label/Dorking "dorking") to search for specific information on the internet. Google dorking is a method of using advanced search operators and keywords to uncover [sensitive information](https://www.kitploit.com/search/label/Sensitive%20Information "sensitive information") that is publicly available on the internet. SXDork offers a wide range of options to search for different types of dorks, such as domain login dork, wpadmin dork, SQL dork, configuration file dorks, logfile dorks, [dashboard](https://www.kitploit.com/search/label/Dashboard "dashboard") dork, id\_rsa dorks, ftp dorks, backup file dorks, mail archive dorks, password dorks, DCIM photos dork, and CCTV dorks.

One of the key features of SXDork is its ability to search dorks using the -s flag. This function allows users to retrieve a significant amount of information related to search keywords. Users can specify specific keywords and the tool will search for all the related information available on the internet. Additionally, users can use the -r flag to set the number of results that will be displayed. The default setting is 10 results, however, users can increase or decrease the number of results as per their requirement. This feature is useful for users who are looking for specific information and want to filter through the results quickly.

SXDork also allows users to search wildcard domains and find a wide range of information. This feature is particularly useful for security researchers, penetration testers and other professionals who need to find sensitive information on the internet. With the ability to search for different types of dorks, wildcard domains and filter through results, SXDork is a powerful tool that can help users find information that is publicly available on the internet.

SXDork has the ability to search for information on multiple domains. By default, the tool searches for information on pastebin.com and controlc.com, but you can easily add more domains to search against. To do this, you can navigate to the src [directory](https://www.kitploit.com/search/label/Directory "directory") and edit the dorks.py file, where you will see an array called src that contains the default domains. Simply add more domains to this array, and the next time you run a search query, SXDork will check all the domains in the array for the keyword you are searching for. This allows you to easily find information across multiple domains.

## Installation

```
git clone https://github.com/samhaxr/SXDork.git
```

## Usage

```
usage: SXDork.py [-h] [-s SEARCH] [-r RESULT] [-dl DOMLOGIN] [-da DOMADMIN]
                 [-wp WPADMIN] [-lp LPANEL] [-sql SQLFILE] [-cnf CONFILE]
                 [-log LOGFILE] [-dash DASHBOARD] [-rsa IDRSA] [-ftp FTPFILE]
                 [-bck BACKUPFILE] [-ma MAILARCHIVE] [-pw PASSWORD]
                 [-pic PHOTOS] [-cam CCTVCAM]

Search keywords using google dork

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        Search keyword with dork
  -r RESULT, --result RESULT
                        Number of output result
  -dl DOMLOGIN, --domlogin DOMLOGIN
                        Search domain(s) for login pages
  -da DOMADMIN, --domadmin DOMADMIN
                        Search domain(s) for admin panels
  -wp WPADMIN, --wpadmin WPADMIN
                        Search domain(s) for wordpress admin
  -lp LPANEL, --lpanel LPANEL
                        Search domain(s) for login panels
  -sql SQLFILE, --sqlfile SQLFILE
                        Search domain(s) for sql database files
  -cnf CONFILE, --confile CONFILE
                        Search domain(s) for configuration files
  -log LOGFILE, --logfile LOGFILE
                        Search domain(s) for log files
  -dash DASHBOARD, --dashboard DASHBOARD
                        Search domain(s) for the dashboard
  -rsa IDRSA, --idrsa IDRSA
                        Search domain(s) for id_rsa pub keys
  -ftp FTPFILE, --ftpfile FTPFILE
                        Search domain(s) for FTP files
  -bck BACKUPFILE, --backupfile BACKUPFILE
                        Search domain(s) for backup files
  -ma MAILARCHIVE, --mailarchive MAILARCHIVE
                        Search domain(s) for ma   il archives
  -pw PASSWORD, --password PASSWORD
                        Search domain(s) for passwords
  -pic PHOTOS, --photos PHOTOS
                        Search domain(s) for DCIM/Photos
  -cam CCTVCAM, --cctvcam CCTVCAM
                        Search domain(s) for CCTV/CAMs
```

SXDork - A Powerful Tool That Utilizes The Technique Of Google Dorking To Search For Specific Information On The Internet
![SXDork - A Powerful Tool That Utilizes The Technique Of Google Dorking To Search For Specific Information On The Internet](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEis1hpOEGZBnvC_H-a1f3EnLkA8LWGuR5YGf65VeiMtZU2z-hFP9-19-SQgBqfNw_YU_7Fw54l4E9Lgi2ai_8GgFDcNRJuGNUpzue1d_65gW1wUjrdN28SLvuOdpsdrnjSghhoapftNgiar0ErHJkj-43sO636ifuvqff-MCS9wjFU9eKxkxanTRE58aQ/s72-w640-c-h360/SXDork_8_SXDork.gif)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/02/sxdork-powerful-tool-that-utilizes.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)