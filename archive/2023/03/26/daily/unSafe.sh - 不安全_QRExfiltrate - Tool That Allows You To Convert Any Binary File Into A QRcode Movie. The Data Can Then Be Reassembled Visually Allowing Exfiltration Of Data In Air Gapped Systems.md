---
title: QRExfiltrate - Tool That Allows You To Convert Any Binary File Into A QRcode Movie. The Data Can Then Be Reassembled Visually Allowing Exfiltration Of Data In Air Gapped Systems
url: https://buaq.net/go-155236.html
source: unSafe.sh - 不安全
date: 2023-03-26
fetch_date: 2025-10-04T10:42:21.230794
---

# QRExfiltrate - Tool That Allows You To Convert Any Binary File Into A QRcode Movie. The Data Can Then Be Reassembled Visually Allowing Exfiltration Of Data In Air Gapped Systems

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

![](https://8aqnet.cdn.bcebos.com/83c276020581e782bc122a7601858502.jpg)

QRExfiltrate - Tool That Allows You To Convert Any Binary File Into A QRcode Movie. The Data Can Then Be Reassembled Visually Allowing Exfiltration Of Data In Air Gapped Systems

This tool is a command line utility that allows you to convert any binary file into a QRcode
*2023-3-25 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-155236.htm)
阅读量:40
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgdlOiSoVpKzHp2ADAU1jUUM5dBjNVZTMFR24rypxQCLK1iDB7MVaFxM37QbEEJfjvtZkilLe8wC5PExw1NFdrhcAeZsDPVAjAKy_4TBOdY3j1b1gEuIOYRlelDBhNS7--kcqh2o7cvbuKgcyVltWmRP-FdITSV9fN7pIxV84PV3C5QvVQZXJl9K0zy2Q=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEgdlOiSoVpKzHp2ADAU1jUUM5dBjNVZTMFR24rypxQCLK1iDB7MVaFxM37QbEEJfjvtZkilLe8wC5PExw1NFdrhcAeZsDPVAjAKy_4TBOdY3j1b1gEuIOYRlelDBhNS7--kcqh2o7cvbuKgcyVltWmRP-FdITSV9fN7pIxV84PV3C5QvVQZXJl9K0zy2Q)

This tool is a [command line](https://www.kitploit.com/search/label/Command%20Line "command line") utility that allows you to convert any binary file into a QRcode GIF. The data can then be reassembled visually allowing [exfiltration](https://www.kitploit.com/search/label/Exfiltration "exfiltration") of data in air gapped systems. It was designed as a [proof of concept](https://www.kitploit.com/search/label/Proof%20Of%20Concept "proof of concept") to demonstrate weaknesses in DLP software; that is, the assumption that data will leave the system via email, USB sticks or other media.

The tool works by taking a binary file and converting it into a series of [QR codes](https://www.kitploit.com/search/label/QR%20codes "QR codes") images. These images are then combined into a GIF file that can be easily reassembled using any standard QR code reader. This allows data to be exfiltrated without detection from most DLP systems.

## How to Use

To use QRExfiltrate, open a command line and navigate to the [directory](https://www.kitploit.com/search/label/Directory "directory") containing the QRExfiltrate scripts.

Once you have done this, you can run the following command to convert your binary file into a QRcode GIF:

```
./encode.sh ./draft-taddei-ech4ent-introduction-00.txt output.gif
```

## Demo

`encode.sh <inputfile>`

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgdlOiSoVpKzHp2ADAU1jUUM5dBjNVZTMFR24rypxQCLK1iDB7MVaFxM37QbEEJfjvtZkilLe8wC5PExw1NFdrhcAeZsDPVAjAKy_4TBOdY3j1b1gEuIOYRlelDBhNS7--kcqh2o7cvbuKgcyVltWmRP-FdITSV9fN7pIxV84PV3C5QvVQZXJl9K0zy2Q=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEgdlOiSoVpKzHp2ADAU1jUUM5dBjNVZTMFR24rypxQCLK1iDB7MVaFxM37QbEEJfjvtZkilLe8wC5PExw1NFdrhcAeZsDPVAjAKy_4TBOdY3j1b1gEuIOYRlelDBhNS7--kcqh2o7cvbuKgcyVltWmRP-FdITSV9fN7pIxV84PV3C5QvVQZXJl9K0zy2Q)

Where `<inputfile>` is the path to the binary file you wish to convert, and `<outputfile>`, if no output is specified output.gif used is the path to the desired output GIF file.

Once the command completes, you will have a GIF file containing the data from your binary file.

You can then transfer this GIF file as you wish and reassemble the data using any standard QR code reader.

## Prerequisites

QRExfiltrate requires the following prerequisites:

* qrencode
* ffmpeg

## Limitations

QRExfiltrate is limited by the size of the source data, qrencoding per frame has been capped to 64 bytes to ensure the resulting image has a uniform size and shape. Additionally the conversion to QR code results in a lot of storage overhead, on average the resulting gif is 50x larger than the original. Finally, QRExfiltrate is limited by the capabilities of the QR code reader. If the reader is not able to detect the QR codes from the GIF, the data will not be able to be reassembled.

> The decoder script has been intentionally omitted

## Conclusion

QRExfiltrate is a powerful tool that can be used to bypass DLP systems and exfiltrate data in air gapped networks. However, it is important to note that QRExfiltrate should be used with caution and only in situations where the risk of detection is low.

QRExfiltrate - Tool That Allows You To Convert Any Binary File Into A QRcode Movie. The Data Can Then Be Reassembled Visually Allowing Exfiltration Of Data In Air Gapped Systems
![QRExfiltrate - Tool That Allows You To Convert Any Binary File Into A QRcode Movie. The Data Can Then Be Reassembled Visually Allowing Exfiltration Of Data In Air Gapped Systems](https://blogger.googleusercontent.com/img/a/AVvXsEgdlOiSoVpKzHp2ADAU1jUUM5dBjNVZTMFR24rypxQCLK1iDB7MVaFxM37QbEEJfjvtZkilLe8wC5PExw1NFdrhcAeZsDPVAjAKy_4TBOdY3j1b1gEuIOYRlelDBhNS7--kcqh2o7cvbuKgcyVltWmRP-FdITSV9fN7pIxV84PV3C5QvVQZXJl9K0zy2Q=s72-c)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/03/qrexfiltrate-tool-that-allows-you-to.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)