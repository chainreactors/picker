---
title: 新型 PIXHELL 声音攻击能从 LCD 屏幕噪音中泄露信息
url: https://www.freebuf.com/news/410723.html
source: FreeBuf网络安全行业门户
date: 2024-09-12
fetch_date: 2025-10-06T18:28:23.612583
---

# 新型 PIXHELL 声音攻击能从 LCD 屏幕噪音中泄露信息

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

新型 PIXHELL 声音攻击能从 LCD 屏幕噪音中泄露信息

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型 PIXHELL 声音攻击能从 LCD 屏幕噪音中泄露信息

2024-09-11 11:44:10

所属地 上海

以色列内盖夫本古里安大学（Ben Gurion University of the Negev）的研究人员发现，一种被称为 “PIXHELL”的新型侧信道攻击可通过突破“音频间隙”攻击气隙系统（Air-gapped ）中的计算机，并利用屏幕上像素产生的噪声来窃取敏感信息。

所谓气隙系统是一种将电脑进行完全隔离（不与互联网以及任何其他联网设备连接）以保护数据安全的系统，通常是通过断开网线、禁用无线接口和 USB 连接来实现， 被认为是最难以渗透的、最安全的计算机。

## 攻击原理

该大学软件和信息系统工程系进攻性网络研究实验室（Offensive Cyber Research Lab）负责人Mordechai Guri （莫迪凯·古里）博士在新发表的论文中称，气隙和音频气隙计算机中的恶意软件会生成精心制作的像素图案，产生频率范围在0-22千赫的噪声，恶意代码利用线圈和电容器产生的声音来控制从屏幕发出的频率，声音信号可以编码和传输敏感信息。

值得注意的是，这种攻击不需要任何专门的音频硬件、扬声器或被攻击计算机的内部扬声器，而是依靠LCD屏幕产生声音信号。

古里博士表示，气隙系统御措施可能被恶意内部人员或其他社会工程学技术渗透，如恶意U盘的插入、点击恶意链接或下载受感染的文件，攻击者还可能利用软件供应链攻击，瞄准软件应用程序依赖关系或第三方库。 通过破坏这些依赖关系引入在开发和测试过程中可能被忽视的漏洞或恶意代码。

因此，PIXHELL攻击利用部署在被入侵主机上的恶意软件创建一个声音通道，从音频屏蔽系统中泄露信息。 这是因为LCD屏幕的内部组件和电源中包含电感器和电容器，当电流通过线圈时，这些电感器和电容器会以可听到的频率振动，产生高音噪音，这种现象被称为电感啸叫。 具体而言，耗电量的变化会引起电容器的机械振动或压电效应，从而产生可听到的噪音。 影响耗电模式的一个关键因素是点亮的像素数量及其在屏幕上的分布，因为白色像素比深色像素需要更多的电量来显示。

此外，当交流电（AC）通过屏幕电容器时会以特定频率振动， 声波由液晶屏的内部电气部分产生。 其特性受屏幕上投射的实际位图、图案和像素强度影响。

通过仔细控制屏幕上显示的像素图案，就可以从LCD屏幕上产生特定频率的声波，而攻击者可以利用这种技术，以声波信号的形式渗出数据，然后将这些信号调制并传输到附近的 Windows 或 Android 设备，然后解调数据包并提取信息。

![](https://image.3001.net/images/20240911/1726034647_66e132d7647ff1755c6cc.png!small)攻击场景：被入侵计算机（A）上的恶意软件会对信息进行编码，并使用精心制作的像素模式通过发射的声波信号将信息外泄。附近的笔记本电脑接收信号、解码并将其发送给攻击者

## 限制条件

尽管如此，这种攻击方式存在一些限制条件，包括发射的声音信号功率和质量需要取决于具体的屏幕结构、内部电源、线圈和电容器的位置等因素。 另一个更加限制的条件在于，PIXHELL 攻击默认情况下需要将显示屏幕调整为由黑白交替行组成的位图模式，因此了保持隐蔽性，攻击者可能会采用在目标用户不在时进行攻击，比如在非工作时间行所谓的'通宵攻击'，降低被揭露和暴露的风险。

但古里博士也指出了一种可在平时工作时间转变为隐蔽攻击的方法，即在传输之前将像素颜色降低到非常低的值，比如使用 (1,1,1)、(3,3,3)、(7,7,7) 和 (15,15,15) 的 RGB数值，从而给用户造成屏幕是完全黑色的假象。但同样，这一方法的副作用是大幅降低了声音的制作水平。此外，如果用户仔细观察屏幕，仍然可以发现异常之处。

![](https://image.3001.net/images/20240911/1726034854_66e133a698cbb3a270ff4.png!small)四种近似黑色的RGB数值显示效果

该研究这并不是第一次在实验装置中突破音频间隙限制。 古里博士在之前进行的研究中还采用了计算机风扇（Fansmitter）、硬盘驱动器（Diskfiltration）、CD/DVD 驱动器（CD-LEAK）、电源装置（POWER-SUPPLaY）和喷墨打印机（Inkfiltration）产生的声音。

作为应对措施，建议使用声音干扰器来中和传输，监控音频频谱是否有异常或不常见的信号，限制授权人员的物理访问，禁止使用智能手机，并使用外部摄像头来检测异常的屏幕调制模式。

**参考来源：**

> [New PIXHELL Attack Exploits Screen Noise to Exfiltrates Data from Air-Gapped Computers](https://thehackernews.com/2024/09/new-pixhell-attack-exploits-screen.html)

# 网络安全 # 数据安全

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

攻击原理

限制条件

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)