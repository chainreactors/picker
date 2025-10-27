---
title: 数万台设备已被影响！疑似DDOS团伙Blackmoon再现江湖
url: https://www.secpulse.com/archives/196115.html
source: 安全脉搏
date: 2023-02-21
fetch_date: 2025-10-04T07:35:32.155003
---

# 数万台设备已被影响！疑似DDOS团伙Blackmoon再现江湖

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 数万台设备已被影响！疑似DDOS团伙Blackmoon再现江湖

[漏洞](https://www.secpulse.com/archives/category/vul)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-20

12,520

**恶意家族名称：**

BlackMoon

**威胁类型：**

僵尸网络

**简单描述：**

BlackMoon 是一款僵尸网络，曾于 2022 年 1 月至 3 月大规模爆发。该僵尸网络能够与 C2 服务器连接，并通过C2服务器下达的指令对指定目标实行不同类型的 DDOS 攻击，导致目标可能遭受服务器瘫痪、核心数据被窃等损失。

**恶意文件分析**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871351.gif)

**1.恶意文件描述**

近期，深信服深盾终端实验室在运营工作中发现了一款僵尸网络病毒，通过跟踪监测发现，该病毒近期肉鸡控制规模已达 6 万以上。

经分析，该病毒所使用的网络资产与 DDOS 团伙 BlackMoon 的网络资产存在重叠。该病毒已产生一次变种，但功能基本一致，均由对应 C2 下达指令对目标 IP发起 DDOS 攻击。**该攻击占用宿主机大量资源，同时被攻击目标也将遭受网站堵塞、服务器瘫痪等巨大威胁。**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-16768713511.gif)

**2.恶意文件分析**

该僵尸网络病毒样本由 go 语言编写。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871352.png)

在初次运行时，该样本会通过查询注册表键值以获取当前宿主机名称等信息，并将在后续功能中使用到该类信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-16768713521.png)

随后程序通过 TCP 协议与 C2 服务器进行远程通信。程序会将硬编码在样本中的域名作为 C2 地址。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871353.png)

与 C2 服务器建立连接之后，程序首先向 C2 服务器发送一个 “ok” 字符串，并进入预定时长等待。

若 C2 服务器接收到该请求，将会回复字符串 “1337”。该阶段表示样本成功上线，随后病毒进入第一次循环监听状态，等待接受 C2 服务器下达的指令。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871354.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871356.png)

当 C2 发送第一轮指令时，病毒对接受的指令进行判断，并进入对应的 DDOS 攻击类型分支，如 post、http 等。

随后病毒创建一个周期性计时器，在有效时间内进入第二次监听状态，等待 C2 服务器下发第二轮指令，包括但不限于需要攻击的 IP 或域名。

病毒还会根据之前获得的宿主机信息，判断操作系统是 Windows 还是 Android、IOS，将取得的结果进行比对后，不同的操作系统执行 DDOS 攻击时会采用不同的UA，不同的攻击类型也会拥有不同的请求头。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871357.png)

C2 指令形式大致如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871360.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871362.gif)

**情报关联分析**

本次样本于 2023 年 2 月 2 日发现，为变种样本，活动最早可追溯至 2022 年 7 月。

在情报识别中，样本下载链接与 DDOS 团伙 BlackMoon 团队曾使用的网络资产重叠，故初步判断此次僵尸网络事件所属团伙可能为 BlackMoon。

以下是情报的具体流程图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871362.png)

原始样本与变种样本功能相似，不同点在于通信协议较多，且不判断系统，下图是原始样本功能场景：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871364.png)

**IOCs**

B34D7ED024EC71421EAA857E98E5B2E2

57ACC280049394A4FE8581D7A29D1F6B

83DD26840EE3606A406553F82DDB66B9

4AE2CDF1BB4E2A53B40FBA1024911E10

3FF63F13497A2F8271634166B585CB7C

ddc.wuxianlequ.com

yyy.wuxianlequ.com

8.219.160.241

8.218.16.68

8.219.214.251

**解决方案**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196115-1676871365.gif)

**处置建议**

1. 避免将重要服务在外网开放，若一定要开放，需增加口令复杂度，避免使用弱口令。

2. 避免打开可疑或来历不明的邮件，尤其是其中的链接和附件等，如一定要打开未知文件，请先使用杀毒软件进行扫描。

3. 安装信誉良好的防病毒/反间谍软件，定期进行系统全盘扫描，并删除检测到的威胁，按时升级打补丁。

4. 使用官方和经过验证的下载渠道，使用正版开发人员提供的工具/功能激活和更新产品，不建议使用非法激活工具和第三方下载器，因为它们通常用于分发恶意内容。

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/196115.html**](https://www.secpulse.com/archives/196115.html)

Tags: [BlackMoon](https://www.secpulse.com/archives/tag/blackmoon)、[C2](https://www.secpulse.com/archives/tag/c2)、[ddos](https://www.secpulse.com/archives/tag/ddos)、[HTTP](https://www.secpulse.com/archives/tag/http)、[POST](https://www.secpulse.com/archives/tag/POST)、[TCP 协议](https://www.secpulse.com/archives/tag/tcp-%E5%8D%8F%E8%AE%AE)、[僵尸网络](https://www.secpulse.com/archives/tag/%E5%83%B5%E5%B0%B8%E7%BD%91%E7%BB%9C)

点赞：
6
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![5月恶意软件态势研判分析报告](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201650-1686287775-300x166.png)

  5月恶意软件态势研判分析报告](https://www.secpulse.com/archives/201650.html "详细阅读 5月恶意软件态势研判分析报告")
* [![API安全基础理论](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image10-300x192.png)

  API安全基础理论](https://www.secpulse.com/archives/200281.html "详细阅读 API安全基础理论")
* [![bypass！一个简单shellcode注入器](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1683770184567-300x202.png)

  bypass！一个简单shellcode…](https://www.secpulse.com/archives/200219.html "详细阅读 bypass！一个简单shellcode注入器")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/08/16/9f4b1a0a8978eebf651bfe827b4d307a-300x255.jpeg)](https://www.secpulse.com/newpage/author?author_id=9241aaa) | [Further\_eye ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=9241) | |
| 文章数：319 | 积分： 2105 |
| 深信服科技旗下安全实验室，致力于网络安全攻防技术的研究和积累，深度洞察未知网络安全威胁，解读前沿安全技术。 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newp...