---
title: APT-C-36（盲眼鹰）近期伪造司法部门文件投DcRat后门事件分析
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247504326&idx=1&sn=4a308586420335a0a150768b2fe76d77&chksm=f9c1e2cfceb66bd91be1ec1d2aecc3afdd457db50ecb44ad0f4fd0182efac85a850bd3349bda&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-11-21
fetch_date: 2025-10-06T19:17:19.328165
---

# APT-C-36（盲眼鹰）近期伪造司法部门文件投DcRat后门事件分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRjFDdQx90982QViarTmW9EuWp5rDUMF0oOd99Kch7s24rJrgdwbXLiaB8g/0?wx_fmt=jpeg)

# APT-C-36（盲眼鹰）近期伪造司法部门文件投DcRat后门事件分析

高级威胁研究院

360威胁情报中心

**APT-C-36**

**盲眼鹰**

APT-C-36（盲眼鹰）是一个疑似来自南美洲的APT组织，主要目标位于哥伦比亚境内，以及南美的一些地区，如厄瓜多尔和巴拿马。该组织自2018年被发现以来，持续发起针对哥伦比亚国家的政府部门、金融、保险等行业以及大型公司的定向攻击。

监测发现，APT-C-36（盲眼鹰）近期使用UUE压缩包伪造司法部门文件向哥伦比亚地区人群或组织投放，最终释放DcRat后门于用户机器中运行。

## **一.攻击流程分析**

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PprmLyxft5DdejiasRRf8JPDUMxDrgxOvSaGB5zgh9E6OHia4tI6VWsNgoTzibT6YDdS87seKc3eAD1Q/640?wx_fmt=png&from=appmsg)

## **二.恶意载荷分析**

攻击者通过钓鱼邮件诱使用户从第三方云平台下载携带恶意文件的UUE/ZIP等压缩包，此次活动中攻击者在UUE压缩文件中内嵌一个自解压EXE文件，UUE压缩文件和自解压EXE文件使用西班牙语命名，伪造成司法部门文件向哥伦比亚地区人群和组织投递。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PprmLyxft5DdejiasRRf8JPDgVc6Z8KBAkmDic0vFv2FFG8AiapCx386IoeUAQPBWjpx6c5peEkKAY4w/640?wx_fmt=png&from=appmsg)

自解压EXE文件运行后会在%TEMP%目录下释放恶意脚本执行程序和恶意脚本文件。以WSF为后缀的恶意脚本文件经过众多特殊字符进行混淆，脚本执行后会现将特殊字符进行替换还原恶意代码后执行恶意命令。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRjpVcGfLaLBJSpo7lIJVah05070CVtRHbpIpMwp2pWJYkAiacM4YucBfg/640?wx_fmt=png&from=appmsg)

恶意脚本被执行后会在计算机中创建一个名为“google Update2024 Tas”的计划任务用于持久化且请求下一阶段的恶意脚本运行。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRjkJDDAYptF2L0624ibe4ia6PZ9HoFv7s9QDtzlOZ5EDWkiafCLzd5osZOw/640?wx_fmt=png&from=appmsg)

下一阶段的sostener.vbs恶意脚本沿用了APT-C-36（盲眼鹰）的一贯风格：在正常的代码中夹带混淆过的恶意代码。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRjHwvQLduKrK4bxBRGdJHLsxRclDgyicAciarLTianibSlMxzvq0f68RKasg/640?wx_fmt=png&from=appmsg)

混淆代码解混淆解base64编码后继续从第三方平台中下载载荷，进行base64解密后传入构造好的参数执行载荷指定类和函数。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRjwgDicBiaqklhc9E54bq6dyHhkHqSAicLOiazHcYCAP5dHR7TS1wh0rMtZQ/640?wx_fmt=png&from=appmsg)

## **三.攻击组件分析**

Dllskyfal.txt进行base64解码后是一个C#编译的dll文件，DLL文件内包含反虚拟机，持久化以及载荷加载等功能。

DLL文件运行后根据传入的参数以及计算机内的进程名进行判断机器是否处于虚拟机环境，如果处于虚拟机环境便退出。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRjyeIjPILor2XvzDT7H0DQd0zeKAoqw4LxReBP7HR6V3ZDqvmCqM0xvA/640?wx_fmt=png&from=appmsg)

对参数进行判断选择持久化方案，如果参数中包含“1”便在计算机内%temp%目录下创建一个名为xxx.ps1和xx2.vbs文件执行完成持久化。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRj8JWoNztTUibMJicfAb9Q9M28O0t69vngMbTPtK3Yia8kqVsicyGxmMXFVQ/640?wx_fmt=png&from=appmsg)

随后DLL文件分别对AndeLoader载荷以及DcRat载荷进行下载，运行AndeLoader将DcRat注入到RegSvcs.exe进程中执行。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRjwGTCeBxlZHlNG7GkHo5JVPDiaL4TSrNWn9j67MsUwQZE0kIS5TUxuvg/640?wx_fmt=png&from=appmsg)

Dark Crystal RAT（简称DcRAT）是一种模块化的开源远控木马（RAT），首次在2018年被观察到，该木马采用了模块化的策略能够灵活的添加和部署想要实现的恶意功能，如：键盘窃取、截屏、剪切板复制、指令执行等。

|  |  |
| --- | --- |
| **字段** | **详情** |
| Por\_ts | 35650 |
| Hos\_ts | dcmxz.duckdns.org |
| Ver\_sion | 1.0.7 |
| In\_stall | FALSE |
| Install\_Folder | %AppData% |
| Key | BMaxyTI6PFcknz46fW6SoamkbMkpDOBY |
| MTX | DcRatMutex\_qwqdanchun |

使用WMI查询机器内是否存在杀毒引擎。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRjnkWQaQJRMrP7fDObCRlysnAqzExoMMGU0BGYoyrpryJX0GzuhAdYeQ/640?wx_fmt=png&from=appmsg)

根据系统位数选择不同的AMSI绕过策略进行反调试。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRjfpLKKEARnpTGZibkaYSicaicW8iat5iceNFrlibbNFBEF7dBiaK7CSqVqfbrw/640?wx_fmt=png&from=appmsg)

在用户机器内查找指定敏感进程名，如果存在就终止进程。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRj6iaboKx3HKee7nxnIe6GNZMdkjheBqBDIbrjuTRhozQ7qicicy0d8jkYw/640?wx_fmt=png&from=appmsg)

获取的受害用户机器敏感信息发送到攻击者服务器内。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PqiaMZBib6yeTHg0nSJQhpJRj28GviaM4qA0q4rao3FiaKqeIkKMRczknLQWGWFXHxdLicoQ7icNFQUe4CA/640?wx_fmt=png&from=appmsg)

## **四.归属研判**

1、此次攻击事件使用的诱饵文件贯彻APT-C-36（盲眼鹰）以往的习惯：使用西班牙语进行命名伪造司法部文件向受害用户投递；

2、以及使用的恶意代码混淆方式以及后续载荷都与APT-C-36以往活动中使用的都基本一致。

在我方视野中APT-C-36（盲眼鹰）持续活跃，针对哥伦比亚、墨西哥、厄瓜多尔、土耳其等地区使用西班牙语的人群以及团体进行木马投递。该组织在近期攻击活动不断开发新工具并完善攻击链，扩大攻击群体的同时也在尝试使用不同的攻击链发起攻击，可预见在未来或能观测到更多APT-C-36（盲眼鹰）组织活跃的痕迹。

#

**附录 IOC**

#

816999bfe363b545575d2aaca78a6fdd

cd4b908264f6711321d7cb9d62df89d2

ff30cc63bb8ba014ffe95ba9fa52eca4

31748fb41fa5212711aac8dbd62af0b6

ad25a95f049577f0372657779a58bf0c

5d40616dda7b012eb774c45806b7b42a

4927769fa3f3c5a80287ab3e335d8769

31748fb41fa5212711aac8dbd62af0b6

e078fa76a2ddd05106a6dddba78b4608

e8c4326e36be1949ce49150c9066f944

dcmxz.duckdns[.]org

https://www.informacionoportuna[.]com/wp-content/uploads/2024/09/dllskyfal.txt

http://keepz.duckdns[.]org/sostener.vbs

https://bitbucket[.]org/89999999999999/acaaaaaaaaa/downloads/dll.txt

http://pastebin[.]com/raw/V9y5Q5vv

https://bitbucket[.]org/556ghfhgfhgf/fdsfdsf/downloads/dllhope.txt

https://cdn.discordapp[.]com/attachments/1046967871470837855/1046969589982044230/dll.txt

http://91.202.233[.]169/Tak/Reg/Marz/DRG/RTC/F3dll.txt

https://textbin[.]net/raw/ezjmofz3s6

**团队介绍**

TEAM INTRODUCTION

**360****高级威胁研究院**

360高级威胁研究院是360政企安全集团的核心能力支持部门，由360资深安全专家组成，专注于高级威胁的发现、防御、处置和研究，曾在全球范围内率先捕获双杀、双星、噩梦公式等多起业界知名的0day在野攻击，独家披露多个国家级APT组织的高级行动，赢得业内外的广泛认可，为360保障国家网络安全提供有力支撑。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

360威胁情报中心

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4Pruscv37D0qgOMbfC4jVxUnso6yyhQC9OIyDNX6TYo5k8iafcfZMzT0ia5boCo69WZSicq7krbicKaHsw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过