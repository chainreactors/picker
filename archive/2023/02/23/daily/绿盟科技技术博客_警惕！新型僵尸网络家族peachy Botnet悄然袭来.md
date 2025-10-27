---
title: 警惕！新型僵尸网络家族peachy Botnet悄然袭来
url: http://blog.nsfocus.net/peachy-botnet/
source: 绿盟科技技术博客
date: 2023-02-23
fetch_date: 2025-10-04T07:51:14.496963
---

# 警惕！新型僵尸网络家族peachy Botnet悄然袭来

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 警惕！新型僵尸网络家族peachy Botnet悄然袭来

### 警惕！新型僵尸网络家族peachy Botnet悄然袭来

[2023-02-22](https://blog.nsfocus.net/peachy-botnet/ "警惕！新型僵尸网络家族peachy Botnet悄然袭来")[伏影实验室](https://blog.nsfocus.net/author/fuying-lab/ "View all posts by 伏影实验室")

阅读： 1,542

## ****一、背景****

2023年2月初，绿盟科技伏影实验室全球威胁狩猎系统监测到一类可疑的elf样本正在大范围传播，这引起了我们的警惕，经过人工确认，发现这批elf样本隶属于新的僵尸网络家族，我们依据Bot作者在样本中留有的签名信息将该家族命名为peachy Botnet。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_7-4-300x154.png)

peachy Botnet最早于2021年8月份开始传播，在代码结构上有过多次微调，多次版本变化中较大的变动体现在对攻击方式修改，早期版本仅支持一种DDoS攻击方式，后面增加到了四种，这两个版本均出现于2021年8月第至2021年9月中旬期间，且在后期均有不同程度的传播。

## ![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_8-4-300x94.png)

### 2.1 传播

peachy Botnet通过Telnet爆破的方式传播，受影响平台涵盖了arm，spc，ppc,mips以及x86架构。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_9-4-300x79.png)

其爆破所使用的弱口令对在传统的Gafgyt和Mirai类僵尸网络家族中较为常见。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_10-4-198x300.png)

我们注意到peachy Botnet在telnet爆破过程中，会发送字符串“PEACH”，该特点可以很好地作为标记该家族的特征，能够有效地将它与传统类家族的telnet扫描流量区分开来。

### ![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_11-4-300x43.png)2.2 通信&&指令

peachy Botnet在与控制端建立连接的过程中会拼接命令行参数作为上线包，当无参数传入时拼接“unknown”字符串。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_12-3-300x137.png)

产生的流量如下：

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_13-3-300x57.png)

随后会依据控制端返回值的不同来执行不同的功能，首先判断receive返回值，当为0x104时执行下载更新功能。

![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_14-3-300x155.png)

另一种情况，则依据首字节的值的不同，执行扫描爆破以及发起DDoS攻击等功能，具体如下：

|  |  |
| --- | --- |
| 首字节的值 | 执行功能 |
| 1 | scanner\_kill |
| 2 | socks5\_kill |
| 4 | scanner\_init |
| 5 | socks5\_server\_init |
| 0xF | attack\_handler |

当首字节的值为0xF时发起DDoS攻击，最新版本支持tcp\_raw和udpplain在内四种常见的DDoS攻击方式。

## ![](https://blog.nsfocus.net/wp-content/uploads/2023/02/wps_doc_15-3-300x113.png)三、总结

从首次发现至今，peachy Botnet并未发起过较大破坏力的攻击活动，一直表现的很沉默，但在近期，却加强了传播力度。该家族功能相对比较简单，各版本文件大小仅维持在60k上下，但相较于每天大量出现的各类基于Mirai和Gafgyt变种，其所采用的架构却相对较新，并且在不断地更新版本，功能也在趋于完善，我们推断该家族在后期仍会活跃一段时间，伏影实验室将持续加强对peachy Botnet家族及其背后运营团伙的监测。

## IOC

4309050903bfd9e6079bfc5e9cb21e82ec4c8b13b29c0b8307da9c86aad7d9e0

cf015e8a179f72c8f2173e818767ed346ec28f6349b155f07e1f0208dee9b002

e87f5b59fab81a2ad003636fbe8347b46d32a9481d180c9f953cf3ea9dd4bbd3

c17a1ddc156733a04a1deb651ab5644b6ac75e3bc481e69a13ff3dcc4e0d720d

c7e9bc0403253991b8189d848a6d395f1f73ccd2da1af7f00938e230bddc5a76

6502092c4b73142f3e06e323add1da8b90adefe2c4545cdb24025097295d2e66

0454b55141cbb4c2a7a3dfd27c89e0831fe30c939ed3a630893978ad284a696f

323be16b1fc824f1c3fa1a80bf6e81e1997ba2ef61090a3b1aee706230c7a50a

90b0703ebbd096b757d5c19175459bfdb0f4003cfc46d306f0bcd251fb649457

6b4438ce21e4ebd9af45b48b2986d8ea3f8dc2281aa30470116e00b19b864735

3edbfab04f3c67e0a585dce03201196ed821fbbf80b23133fa56ca32b27de57c

2c9fab4101794f696d3cdfc259564cc4

778db5ee392be30ef8f0291533e123f6

37.0.11.160

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/ssh-server/)

[Next](https://blog.nsfocus.net/vmware-carbon-black-app-controlcve-2023-20858/)

### Meet The Author

伏影实验室

伏影实验室专注于安全威胁监测与对抗技术研究。
研究目标包括Botnet、APT高级威胁，DDoS对抗，WEB对抗，流行服务系统脆弱利用威胁、身份认证威胁，数字资产威胁，黑色产业威胁及新兴威胁。通过掌控现网威胁来识别风险，缓解威胁伤害，为威胁对抗提供决策支撑。

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)