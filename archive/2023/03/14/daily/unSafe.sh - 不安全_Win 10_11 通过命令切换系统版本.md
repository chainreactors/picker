---
title: Win 10/11 通过命令切换系统版本
url: https://buaq.net/go-153252.html
source: unSafe.sh - 不安全
date: 2023-03-14
fetch_date: 2025-10-04T09:27:58.331576
---

# Win 10/11 通过命令切换系统版本

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

Win 10/11 通过命令切换系统版本

点击win键，输入CMD，在最佳配置出现的命令提示符处右键，选择以管理员运行。在打开的窗口中输入命令 dism /online /get-Current
*2023-3-13 22:37:10
Author: [blog.upx8.com(查看原文)](/jump-153252.htm)
阅读量:77
收藏*

---

点击win键，输入CMD，在最佳配置出现的命令提示符处右键，选择以管理员运行。

在打开的窗口中输入命令 dism /online /get-CurrentEdition获取当前系统版本

再使用命令 dism /online /Get-TargetEditions显示可以将当前系统可以升级到的版本

```
Professional为专业版 VK7JG-NPHTM-C97JM-9MPGT-3V66T
ProfessionalEducation为专业教育版 8PTT6-RNW4C-6V7J2-C2D3X-MHBPB
ProfessionalWorkstation为专业工作站版 DXG7C-N36C4-C4HTG-X4T3X-2YV77
ProfessionalCountrySpecific为专业国家特定版本
ProfessionalSingleLanguage为专业单语言版
ServerRdsh为服务器Rdsh版，开启Rdsh后可接受无穷多的RDP远程用户，本地也可以开启一个用户。
IoTEnterprise为嵌入式版本，可以理解为物联网版。
Enterprise为企业版 XGVPP-NMH47-7TTHJ-W3FW7-8HV2C
Education为教育版 YNMGQ-8RYV3-4PGQ3-C8XTP-7CFBY
Home Edition为家庭版 YTMG3-N6DKC-DKB77-7M9GH-8HVX7
```

根据个人需求输入相应版本密钥,以教育版转专业工作站版为例 命令如下

```
changepk /productkey DXG7C-N36C4-C4HTG-X4T3X-2YV77
输入后回车，如需要升级文件，等待弹出升级界面并升级完成。若无文件升级，则等待片刻后可通过此电脑右键属性查看系统版本。
升级前务必通过命令dism /online /Get-TargetEditions查看确定可以升级到的版本，再用对应的key转换。
更换版本后很容易出现系统未激活的问题，请自行使用key或工具激活。
```

文章来源: https://blog.upx8.com/3265
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)