---
title: Masjesu 僵尸网络隐蔽攻击物联网设备，专注持久化而非大规模感染
url: https://hackernews.cc/archives/64064
source: HackerNews
date: 2026-04-09
fetch_date: 2026-04-10T04:45:21.909626
---

# Masjesu 僵尸网络隐蔽攻击物联网设备，专注持久化而非大规模感染

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![hacker-2883630_可用](https://hackernews.cc/wp-content/uploads/2025/02/hacker-2883630_可用.jpg)

# Masjesu 僵尸网络隐蔽攻击物联网设备，专注持久化而非大规模感染

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-04-09](https://hackernews.cc/archives/64064 "12:13")
分类: [恶意软件](https://hackernews.cc/archives/category/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6),[网络犯罪](https://hackernews.cc/archives/category/%E7%BD%91%E7%BB%9C%E7%8A%AF%E7%BD%AA)
[暂无评论](https://hackernews.cc/archives/64064#respond)

* 浏览次数 159
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

Trellix深入分析了Masjesu僵尸网络的内部运作，**这是一个用于分布式拒绝服务（DDoS）攻击的僵尸网络，已感染多种物联网设备。**

Masjesu自2023年起活跃，其运营者主要在Telegram上宣传，**声称能够发动数百GB规模的DDoS攻击。**运营者的帖子同时针对中文和英文用户，”表明其服务继续瞄准中美客户”。目前该运营者的Telegram频道拥有超过400名订阅者，但僵尸网络用户群似乎更大，因最初推广该僵尸网络的频道已被平台以违反政策为由关闭。

攻击来源国家分析显示，**Masjesu感染的大多数设备位于越南，但巴西、印度、伊朗、肯尼亚和乌克兰也有大量设备被感染。**“数据强烈表明攻击来自多个自治系统，涉及各种网络，而非僵尸网络完全托管于单一虚拟专用服务器（VPS）提供商，”Trellix指出。

近期分析的Masjesu样本显示，其可针对多种架构，包括i386、MIPS、ARM、SPARC、PPC、68K（摩托罗拉68000）和AMD64。**该僵尸网络通过D-Link路由器、GPON路由器、华为家庭网关、MVPower DVR、Netgear路由器、UPnP服务及其他物联网设备的漏洞传播。**

在受感染设备上，恶意软件绑定硬编码TCP端口的套接字为运营者提供远程访问，并加固自身以实现持久化。恶意软件将敏感字符串（包括命令控制域名、端口、文件夹名和进程名）加密存储在查找表中，运行时解密。

为实现持久化，Masjesu首先分叉新进程，将原始可执行路径重命名为模拟合法Linux动态链接器的路径和功能。然后创建cron作业每15分钟运行重命名的可执行文件，将进程转为后台守护进程，并重命名以显示为合法系统组件。

恶意软件还终止常用进程（如wget和curl），锁定共享临时文件夹，可能为防止其他僵尸网络感染。为传播，它扫描互联网随机IP地址寻找可感染的脆弱设备。

Masjesu使用多个命令控制域名和备用IP，在套接字连接上配置60秒接收超时，客户端解密接收数据。根据服务器接收的数据，僵尸网络可发动多种DDoS攻击，包括UDP、TCP、VSE、GRE、RDP、OSPF、ICMP、IGMP、TCP\_SYN、TCP-ACK、TCP-ACKPSH和HTTP洪水攻击。

---

**消息来源：[securityweek.com](https://www.securityweek.com/evasive-masjesu-ddos-botnet-targets-iot-devices/)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[Masjesu](https://hackernews.cc/archives/tag/masjesu)[僵尸网络](https://hackernews.cc/archives/tag/%E5%83%B5%E5%B0%B8%E7%BD%91%E7%BB%9C)[恶意软件](https://hackernews.cc/archives/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用 网络安全](https://hackernews.cc/wp-content/uploads/2026/02/geralt-matrix-2503236_1920-210x140.jpg)](https://hackernews.cc/archives/64008 "新型 CrystalRAT 恶意软件集远控、窃取与恶搞功能于一身")

##### [新型 CrystalRAT 恶意软件集远控、窃取与恶搞功能于一身](https://hackernews.cc/archives/64008 "新型 CrystalRAT 恶意软件集远控、窃取与恶搞功能于一身")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-02

[![可用-scam-7503835_1280](https://hackernews.cc/wp-content/uploads/2025/02/可用-scam-7503835_1280-210x140.jpg)](https://hackernews.cc/archives/64006 "“卡斯巴内罗” 网络钓鱼利用动态 PDF 诱饵瞄准拉美和欧洲")

##### [“卡斯巴内罗” 网络钓鱼利用动态 PDF 诱饵瞄准拉美和欧洲](https://hackernews.cc/archives/64006 "“卡斯巴内罗” 网络钓鱼利用动态 PDF 诱饵瞄准拉美和欧洲")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-02

[![可用-ai-generated-8366100_1280](https://hackernews.cc/wp-content/uploads/2025/02/可用-ai-generated-8366100_1280-210x140.jpg)](https://hackernews.cc/archives/64005 "微软警告：WhatsApp 传播的 VBS 恶意软件通过绕过 UAC 劫持 Windows 系统")

##### [微软警告：WhatsApp 传播的 VBS 恶意软件通过绕过 UAC 劫持 Window...](https://hackernews.cc/archives/64005 "微软警告：WhatsApp 传播的 VBS 恶意软件通过绕过 UAC 劫持 Windows 系统")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-02

[![可用-黑客](https://hackernews.cc/wp-content/uploads/2025/08/ai-generated-8630602_640-210x140.png)](https://hackernews.cc/archives/64004 "乌克兰 CERT-UA 遭仿冒，AGEWHEEZE 恶意软件被群发至百万邮箱")

##### [乌克兰 CERT-UA 遭仿冒，AGEWHEEZE 恶意软件被群发至百万邮箱](https://hackernews.cc/archives/64004 "乌克兰 CERT-UA 遭仿冒，AGEWHEEZE 恶意软件被群发至百万邮箱")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-02

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team