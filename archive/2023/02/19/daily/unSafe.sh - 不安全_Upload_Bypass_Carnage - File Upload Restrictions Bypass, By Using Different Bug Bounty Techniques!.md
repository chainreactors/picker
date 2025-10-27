---
title: Upload_Bypass_Carnage - File Upload Restrictions Bypass, By Using Different Bug Bounty Techniques!
url: https://buaq.net/go-149997.html
source: unSafe.sh - 不安全
date: 2023-02-19
fetch_date: 2025-10-04T07:29:17.577661
---

# Upload_Bypass_Carnage - File Upload Restrictions Bypass, By Using Different Bug Bounty Techniques!

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

![](https://8aqnet.cdn.bcebos.com/86a39b805db318b8e21bfe11df24ba79.jpg)

Upload\_Bypass\_Carnage - File Upload Restrictions Bypass, By Using Different Bug Bounty Techniques!

File Upload Restrictions Bypass, By Using Different Bug Bounty Techniques!POC video: File u
*2023-2-18 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-149997.htm)
阅读量:80
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEKnaGI0gdG7nQyY-1Hyf98cLyY0tihjQY-__-RUt3M4UkUc4E_VU22PT1aiWKmF5UYG4FKzZk_6dElqe0mqGF4FM6A-yVBAOSCYjFbwj-mQuKimFOI4vv0H68n4cusILcjBpufykx4dpvGpRNyRJESXLa8XHWj_8Q_u9NqYBewfNN8Gpagjyikp6gKg/w640-h350/Upload_Bypass_Carnage.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEKnaGI0gdG7nQyY-1Hyf98cLyY0tihjQY-__-RUt3M4UkUc4E_VU22PT1aiWKmF5UYG4FKzZk_6dElqe0mqGF4FM6A-yVBAOSCYjFbwj-mQuKimFOI4vv0H68n4cusILcjBpufykx4dpvGpRNyRJESXLa8XHWj_8Q_u9NqYBewfNN8Gpagjyikp6gKg/s893/Upload_Bypass_Carnage.png)

File Upload Restrictions Bypass, By Using Different Bug Bounty Techniques!

POC video:

File upload [restrictions](https://www.kitploit.com/search/label/Restrictions "restrictions") bypass by using different bug bounty techniques! Tool must be running with all its assets!

Installation:

```
pip3 install -r requirements.txt
```

Usage: upload\_bypass.py [options]

Options: -h, --help

```
  show this help message and exit
```

-u URL, --url=URL

```
  Supply the login page, for example: -u http://192.168.98.200/login.php'
```

-s , --success

```
 Success message when upload an image, example: -s 'Image uploaded successfully.'
```

-e , --extension

```
 Provide server backend extension, for example: --extension php (Supported extensions: php,asp,jsp,perl,coldfusion)
```

-a , --allowed

```
 Provide allowed extensions to be uploaded, for example: php,asp,jsp,perl
```

-H , --header

```
 (Optional) - for example: '"X-Forwarded-For":"10.10.10.10"' - Use double quotes around the data and wrapp it all with single quotes. Use comma to separate multi headers.
```

-l , --location

```
 (Optional) - Supply a remote path where the webshell suppose to be. For exmaple: /uploads/
```

-S, --ssl

```
 (Optional) - No checks for TLS or SSL
```

-p, --proxy

```
 (Optional) - Channel the requests through proxy
```

-c, --continue

```
 (Optional) - If set, the brute force will continue even if one or more methods found!
```

-v, --verbose

```
 (Optional) - Printing the http response in terminal
```

-U , --username

```
 (Optional) - Username for authentication. For exmaple: --username admin
```

-P , --password

```
 (Optional) - - Password for authentication. For exmaple: --password 12345
```

Upload\_Bypass\_Carnage - File Upload Restrictions Bypass, By Using Different Bug Bounty Techniques!
![Upload_Bypass_Carnage - File Upload Restrictions Bypass, By Using Different Bug Bounty Techniques!](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEKnaGI0gdG7nQyY-1Hyf98cLyY0tihjQY-__-RUt3M4UkUc4E_VU22PT1aiWKmF5UYG4FKzZk_6dElqe0mqGF4FM6A-yVBAOSCYjFbwj-mQuKimFOI4vv0H68n4cusILcjBpufykx4dpvGpRNyRJESXLa8XHWj_8Q_u9NqYBewfNN8Gpagjyikp6gKg/s72-w640-c-h350/Upload_Bypass_Carnage.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/02/uploadbypasscarnage-file-upload.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)