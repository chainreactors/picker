---
title: Slicer - Tool To Automate The Boring Process Of APK Recon
url: https://buaq.net/go-136274.html
source: unSafe.sh - 不安全
date: 2022-11-19
fetch_date: 2025-10-03T23:11:28.685851
---

# Slicer - Tool To Automate The Boring Process Of APK Recon

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

![](https://8aqnet.cdn.bcebos.com/6c98ca6a47cb2cf61e1557a5174d7cc3.jpg)

Slicer - Tool To Automate The Boring Process Of APK Recon

A tool to automate the recon process on an APK file. Slicer accepts a path to an extracted
*2022-11-18 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-136274.htm)
阅读量:33
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHVdiYcXmDVI4Q1KL2lXJL6WnWDmdmE1sZcdcblSe15ijAkYSJczx9wKVHSd7ingNF34azrx-xXOWrWXqdzsfSIsycJHBoolTc9rjceiR_88DqxVKmIZL8C74bdneUsRVtMhxWB0sBphCiD1snZMWfzZT64SHPDvwG9rbPC0PfqbbDKpo12lVQ9EMzRw/w640-h408/hack-apk.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHVdiYcXmDVI4Q1KL2lXJL6WnWDmdmE1sZcdcblSe15ijAkYSJczx9wKVHSd7ingNF34azrx-xXOWrWXqdzsfSIsycJHBoolTc9rjceiR_88DqxVKmIZL8C74bdneUsRVtMhxWB0sBphCiD1snZMWfzZT64SHPDvwG9rbPC0PfqbbDKpo12lVQ9EMzRw/s1002/hack-apk.png)

A tool to automate the recon process on an APK file.

Slicer accepts a path to an extracted APK file and then returns all the activities, receivers, and services which are exported and have `null` permissions and can be externally provoked.

**Note**: The APK has to be extracted via `jadx` or `apktool`.

**Why?**

I started bug bounty like 3 weeks ago(in June 2020) and I have been trying my best on android apps. But I noticed one thing that in all the apps there were certain things which I have to do before diving in deep. So I just thought it would be nice to automate that process with a simple tool.

**Why not drozer?**

Well, drozer is a different beast. Even though it does finds out all the accessible components but I was tired of running those commands again and again.

**Why not automate using drozer?**

I actually wrote a bash script for running certain drozer commands so I won't have to run them manually but there was still some boring stuff that had to be done. Like Checking the `strings.xml` for various API keys, testing if firebase DB was publically accessible or if those google API keys have setup any cap or anything on their usage and lot of other stuff.

**Why not search all the files?**

I think that a tool like grep or ripgrep would be much faster to search through all the files. So if there is something specific that you want to search it would be better to use those tools. But if you think that there is something which should be checked in all the android files then feel free to open an issue.

* Check if the APK has set the `android:allowbackup` to `true`
* Check if the APK has set the `android:debuggable` to `true`.
* Return all the activities, services and broadcast receivers which are exported and have null permission set. This is decided on the basis of two things:

  + `android:exporte=true` is present in any of the component and have no permission set.
  + If exported is not mention then slicer check if any `Intent-filters` are defined for that component, if yes that means that component is exported by default(This is the rule given in android documentation.)
* Check the [Firebase](https://www.kitploit.com/search/label/Firebase "Firebase") URL of the APK by testing it for `.json` trick.

  + If the firebase URL is `myapp.firebaseio.com` then it will check if `https://myapp.firebaseio.com/.json` returns something or gives permission denied.
  + If this thing is open then that can be reported as high severity.
* Check if the google API keys are publically accessible or not.

  + This can be reported on some bounty programs but have a low severity.
  + But most of the time [reporting](https://www.kitploit.com/search/label/Reporting "reporting") this kind of thing will bring out the pain of `Duplicate`.
  + Also sometimes the company can just close it as `not applicable` and will claim that the KEY has a `usage cap` - r/suspiciouslyspecific

    
* Return other API keys that are present in `strings.xml` and in `AndroidManifest.xml`
* List all the file names present in `/res/raw` and `res/xml` directory.
* Extracts all the URLs and paths.

  + These can be used with tool like [dirsearch](https://www.kitploit.com/search/label/dirsearch "dirsearch") or ffuf.

* Clone this repository

```
git clone https://github.com/mzfr/slicer
```

* `cd slicer`
* Now you can run it: `python3 slicer.py -h`

It's very simple to use. Following options are available:

```
Extract information from Manifest and strings of an APK

Usage:
        slicer [OPTION] [Extracted APK directory]

Options:

-d, --dir             path to jadx output directory
  -o, --output          Name of the output file(not implemented)
```

I have not implemented the `output` flag yet because I think if you can redirect slicer output to a yaml file it will a proper format.

* Extract information from the APK and display it on the screen.

```
python3 slicer.py -d path/to/extact/apk -c config.json
```

The [extractor](https://www.kitploit.com/search/label/Extractor "extractor") module used to extract URLs and paths is taken from [apkurlgrep](https://github.com/ndelphit "apkurlgrep") by @ndelphit

All the features implemented in this are things that I've learned in past few weeks, so if you think that there are various other things which should be checked in an APK then please open an issue for that feature and I'd be happy to implement that :)

If you'd like you can buy me some coffee:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiWxEbUy0AhAZAjp---ImuMGnw2du0WEqoJm16l05-sNNx8amFV9TwdbXjY3zmNB6_OztOGTIkDAe_mWLXdCyprBh3mRtOUGF7jGboVm9HPxd3kFks0QdF2A01EqQzJPDMrU8g6B9a655etEugDSXCRkFitqkkw2vYJ4YTx7tsdHAsDAe0ZcCzCCBv6_g=s320)](https://blogger.googleusercontent.com/img/a/AVvXsEiWxEbUy0AhAZAjp---ImuMGnw2du0WEqoJm16l05-sNNx8amFV9TwdbXjY3zmNB6_OztOGTIkDAe_mWLXdCyprBh3mRtOUGF7jGboVm9HPxd3kFks0QdF2A01EqQzJPDMrU8g6B9a655etEugDSXCRkFitqkkw2vYJ4YTx7tsdHAsDAe0ZcCzCCBv6_g)

Slicer - Tool To Automate The Boring Process Of APK Recon
![Slicer - Tool To Automate The Boring Process Of APK Recon](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHVdiYcXmDVI4Q1KL2lXJL6WnWDmdmE1sZcdcblSe15ijAkYSJczx9wKVHSd7ingNF34azrx-xXOWrWXqdzsfSIsycJHBoolTc9rjceiR_88DqxVKmIZL8C74bdneUsRVtMhxWB0sBphCiD1snZMWfzZT64SHPDvwG9rbPC0PfqbbDKpo12lVQ9EMzRw/s72-w640-c-h408/hack-apk.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/11/slicer-tool-to-automate-boring-process.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)