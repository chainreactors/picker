---
title: 响尾蛇组织窃密木马通信分析
url: https://buaq.net/go-144135.html
source: unSafe.sh - 不安全
date: 2023-01-05
fetch_date: 2025-10-04T03:03:39.156616
---

# 响尾蛇组织窃密木马通信分析

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

![](https://8aqnet.cdn.bcebos.com/54dee9db8d5106df2efb9c66892ca0fc.jpg)

响尾蛇组织窃密木马通信分析

响尾蛇组织窃密木马通信分析 日期：2023年01月04日 阅：99 2022
*2023-1-4 17:21:12
Author: [www.aqniu.com(查看原文)](/jump-144135.htm)
阅读量:34
收藏*

---

响尾蛇组织窃密木马通信分析

日期：2023年01月04日
阅：99

2022年11月22日，响尾蛇组织对我国高校发起攻击活动，利用疫情相关信息包装钓鱼邮件，诱导受害者打开邮件附件，十分具有迷惑性。本次攻击活动仍然采用以往的攻击流程，利用LNK文件下载HTA文件，最终完成窃密行为或实现远程控制。观成科技安全研究团队对响尾蛇组织在类似攻击活动中常用的窃密木马家族进行逆向分析，搭建服务器模拟木马控制端，复现了其通信过程。

![](https://www.aqniu.com/wp-content/uploads/2023/01/1-4-1024x166.png)

该窃密木马执行后，通过HTTPS加密协议上传窃取的系统信息、文件列表，并从C2服务器获取控制指令然后执行。

## 2.1    上传窃密数据

该窃密木马会将收集到的信息存储到C:\Users\username\AppData\Roaming\SyncDat\目录下，系统信息和已安装程序列表存储到\*.sif文件中，文件列表信息存储到\*.flc文件，指定后缀文件信息存储到\*.fls文件中，错误日志存储到\*.err文件中。

该窃密木马创建了定时器来触发上传操作，通过向https://cdn-sop.net/202/F2cPn7PzyV2DdCL4nNCotIfPzcXCLM1YvyGlmyp6/-1/13897/37d4baca发送POST请求将SyncDat目录下的文件上传到C2服务器。

窃密木马生成的HTTP请求头中填充了上传的文件路径和文件类型，如下图所示，X-File-Path字段中填充了Base64编码的文件路径，X-File-Type字段中填充了文件类型“sysInfo”（系统信息）。上传的文件信息使用GZIP进行压缩。

![](https://www.aqniu.com/wp-content/uploads/2023/01/1-3.png)

图 2‑1 上传系统信息和已安装文件列表（HTTPS解密后）

![](https://www.aqniu.com/wp-content/uploads/2023/01/2-1.png)

图 2‑2上传系统信息和已安装文件列表（HTTPS）

## 2.2     下发控制指令

该窃密木马创建了定时器触发请求控制指令操作，通过向https://cdn-sop.net/202/F2cPn7PzyV2DdCL4nNCotIfPzcXCLM1YvyGlmyp6/-1/13897/37d4baca发送HTTP GET请求来获取控制指令。

![](https://www.aqniu.com/wp-content/uploads/2023/01/3-2.png)

图 2‑3 服务器下发控制指令（HTTPS）

该窃密木马使用了不同于其他木马的指令下发方式。C2服务器将控制指令隐藏在DLL的ToString方法中，通过下发DLL文件来传递控制指令。

![](https://www.aqniu.com/wp-content/uploads/2023/01/4-1.png)

图 2‑4 包含控制指令的DLL

服务器下发的DLL经过了XOR加密，加密数据结构如下。前0x20字节是服务器生成的XOR密钥，后面的数据是循环异或后的DLL数据。

![](https://www.aqniu.com/wp-content/uploads/2023/01/5-1.png)

图 2‑5 加密数据

模拟服务器下发加密后的DLL，如下图所示，窃密木马可以正常解析并执行控制指令。

![](https://www.aqniu.com/wp-content/uploads/2023/01/6.png)

图 2‑6 服务器下发控制指令（HTTPS解密后）

该窃密木马获取Base64编码字符串后解码，并使用第一个字节数据作为控制指令码，具体功能如下：

![](https://www.aqniu.com/wp-content/uploads/2023/01/2-2-1024x393.png)

观成瞰云（ENS）-加密威胁智能检测系统能够对响尾蛇APT组织的加密流量进行检测。

![](https://www.aqniu.com/wp-content/uploads/2023/01/7-1024x442.png)

图 3‑1 TLS协议加密流量检测鱼骨图

本次分析的响尾蛇组织窃密木马，通过HTTPS加密通信的方式实现隐蔽上传窃密数据和下发控制指令，其中，该木马控制指令下发的方式很有特点，控制端下发加密后的DLL文件，将控制命令隐藏在DLL文件中，当受控主机调用该DLL文件执行时即可获得指令。当前大多数APT组织都会使用加密通信的方式隐藏命令与控制信息，观成科技安全研究团队通过逆向分析技术对APT组织样本进行分析，研究其加密通信技术手法，并持续对APT组织的进行监测和跟踪。

![](https://www.aqniu.com/wp-content/uploads/avatars/12187/6073c4f71a1df-bpfull.png)

##### [观成科技](https://www.aqniu.com/vip-users/guanchengkeji "由观成科技发布")

观成科技成立于2018年8月，由国内一流安全团队创建，团队核心成员拥有十余年的攻防对抗、产品研发、安全分析、人工智能的实战经验。
       观成科技坚持“自主研发、持续创新”，公司将人工智能、攻防技术和密码技术相结合，在国内首家推出针对加密流量AI安全检测、防御的创新型产品，产品已申请加密流量检测相关国家发明专利20余篇，应用在军工、网信、部委、央企等重要客户，并被多个央企、龙头安全企业选为合作伙伴。
       公司2019年6月获得联想之星、基石基金的天使轮投资；2021年2月获得奇安投资、基石基金的Pre-A投资。

文章来源: https://www.aqniu.com/vendor/92752.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)