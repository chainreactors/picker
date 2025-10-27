---
title: OpenEMR 5.0.1.3 — (Authenticated) Arbitrary File Actions
url: https://buaq.net/go-151581.html
source: unSafe.sh - 不安全
date: 2023-03-02
fetch_date: 2025-10-04T08:25:25.140720
---

# OpenEMR 5.0.1.3 — (Authenticated) Arbitrary File Actions

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

OpenEMR 5.0.1.3 — (Authenticated) Arbitrary File Actions

Back in 2018, a group of security researchers and I decided to try our hands at OpenEMR and find sec
*2023-3-1 22:10:24
Author: [infosecwriteups.com(查看原文)](/jump-151581.htm)
阅读量:17
收藏*

---

Back in 2018, a group of security researchers and I decided to try our hands at OpenEMR and find security vulnerabilities.The full report can be found [here](https://www.open-emr.org/wiki/images/1/11/Openemr_insecurity.pdf).This a very good read and I recommend reading it in its entirety. However this blog post is just documenting my contribution to the project.The following are the three CVEs I received in the collaboration. These were all responsibly disclosed and patched so upgrading to the latest version would be well advised.

1.CVE-2018–15140-Authenicated Arbitrary Read

Vulnerable Code:

```
if ($_POST['mode'] == 'get'){
```

This is a vulnerability that allows an attacker to make a malicious request to /portal/import\_template.php on a unpatched instance of OpenEMR.The result of this request is an arbitrary file read of a local file located on the file system.This vulnerability was possible due to the application passing user input into file\_get\_contents() without any sanitization if the parameter mode is set with get as its value. This result of this input,which is the local file, was then echoed back in the html response.

2.CVE-2018–15142-Authenicated Arbitrary Write

Vulnerable Code:

```
} else if ($_POST['mode'] == 'save') {
    file_put_contents($_POST['docid'], $_POST['content']);
    exit(true);
}
```

This is an vulnerability in /portal/import\_template.php which allows an attacker to write php files to a local file system.This works if the parameter mode is set to save.If that is the case the post parameters docid and content are passed to file\_put\_contents() without any sanitization.The docid is the file name and the content includes the malicious php code. This by itself doesn’t have that much impact since you cannot execute the file, but when paired up with the previously found arbitrary file read, leads to remote code execution.

3.CVE-2018–15141- Authenticated Arbitrary File Delete

Vulnerable Code:

```
} else if ($_POST['mode'] == 'delete') {
     unlink($_POST['docid']);
     exit(true);
 }
```

This is an vulnerability also in /portal/import\_template.php which allows an attacker to delete any file in the system if the filename is known and the permissions to delete are allowed.This is possible when the post parameter mode is set to delete. The docid parameter which contains the file name specified by the attacker is then passed to unlink() without sanitization.

Thank you for reading and hope you enjoyed.You can find Pocs for any one of these on ExploitDB, [here](https://www.exploit-db.com/exploits/45202). You can also read CTF and bug bounty writeups on here or on my blog <https://jsecu.github.io>. If you have any questions, feel free to message me at @Pullerze on Twitter . More Bug Bounty and security writeups coming soon!

文章来源: https://infosecwriteups.com/openemr-5-0-1-3-authenticated-arbitrary-file-actions-f7006e636b8c?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)