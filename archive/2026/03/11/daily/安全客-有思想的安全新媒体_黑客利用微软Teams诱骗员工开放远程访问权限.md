---
title: 黑客利用微软Teams诱骗员工开放远程访问权限
url: https://www.anquanke.com/post/id/315110
source: 安全客-有思想的安全新媒体
date: 2026-03-11
fetch_date: 2026-03-12T04:06:46.168122
---

# 黑客利用微软Teams诱骗员工开放远程访问权限

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 黑客利用微软Teams诱骗员工开放远程访问权限

阅读量**20430**

发布时间 : 2026-03-11 13:59:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Divya，文章来源：gbhackers

原文地址：<https://gbhackers.com/hackers-use-microsoft-teams-to-manipulate-employees-into-allowing-remote-access/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

安全研究人员近期发现一项新型恶意软件攻击活动，攻击者**伪装成企业内部 IT 支持人员**，针对金融与医疗行业员工实施定向入侵。

攻击者在取得初步访问后，会部署一款名为 **A0Backdoor** 的新型隐秘后门。

BlueVoyant 网络安全研究团队确认，该攻击由 **Blitz Brigantine（又称 Storm‑1811）** 组织实施，其通过**邮件炸弹轰炸**与**微软 Teams 聊天消息**组合诱骗受害者开放远程控制权限。

---

### 基于 Teams 与 Quick Assist 的完整攻击链

攻击以**大规模垃圾邮件轰炸**受害者邮箱为开端。

邮件轰炸开始后不久，黑客立即通过**微软 Teams** 联系受害者，**伪装成公司 IT 客服**，声称可协助解决当前的邮件异常问题。

攻击者诱导受害者打开 Windows 自带远程工具 **Quick Assist**，从而**瞬间获得设备完全控制权**。

在拿到远程访问权限后，攻击者随即下载恶意安装包，这些文件**高度伪装成微软 Teams 与 Phone Link 的合法更新程序**。

为让文件看起来完全可信，黑客将其托管在**个人微软云存储账号**中，并使用**数字证书**进行签名。

安装程序运行后，会将一个正常的微软程序，与名为 **hostfxr.dll** 的恶意伪造文件放在一起。

当正常程序启动时，会在无感知情况下加载恶意文件，这一隐秘攻击手法被称为 **DLL 侧加载**。

该伪造文件是一个**加壳强度极高的恶意加载器**，可阻止安全工具对其进行分析。

* 它通过**反沙箱技术**检查设备固件，识别 QEMU 等虚拟测试环境。
* 同时创建大量垃圾线程，专门用于**使调试软件崩溃**。

更特殊的是，该加载器使用**自定义时间算法**解锁真实载荷。

恶意代码**仅在特定 55 小时时间窗口内**才能成功解密。

此外，黑客会在命令行末尾插入一个**不可见空格字符**。

恶意软件必须匹配该隐藏字符，才能生成正确密钥，解锁最终病毒体。

这一设计让安全研究人员在事后**极难复现攻击与分析代码**。

---

### A0Backdoor 后门与 DNS 隐秘通信战术

在通过所有自检后，恶意软件会将 **A0Backdoor** 写入内存。该后门用于**窃取信息并维持长期控制**。

后门会立即采集设备信息，包括**用户名与系统硬件信息**，方便攻击者精准识别受害者。

为在不触发告警的情况下与攻击者通信，A0Backdoor 采用了 **DNS 隧道**这一隐蔽通信技术。

malware 不会直接连接可疑的黑客控制服务器，而是向可信公共 DNS 解析器发送请求，例如 `1.1.1.1` 或 `8.8.8.8`。

它将隐藏信息伪装成**邮件交换记录查询（MX 查询）**，这类请求通常用于服务器正常邮件路由。

攻击者将窃取的数据与恶意指令隐藏在**超长、复杂的子域名**中。

公共解析器会将请求转发至黑客隐藏服务器，并将加密响应返回给受感染设备。

由于流量全程经过可信公共服务器，且外观与**企业常规邮件路由**完全一致，可轻易混入正常流量中不被发现。

黑客还刻意使用**早年注册的旧域名**，而非全新注册域名，以此绕过安全设备对**新注册域名**的自动拦截规则。

---

此次攻击标志着 Blitz Brigantine 组织战术的重大转变，其已**放弃传统勒索软件模式**，转向**高度定制化的隐秘攻击**。

专家强烈建议企业：

* 加强员工培训，**严格核验所有来自 Teams 的 IT 支持请求**
* 监控并限制 Quick Assist 等远程工具的使用
* 拦截未授权的安装包，防范此类高危害入侵

本文翻译自gbhackers [原文链接](https://gbhackers.com/hackers-use-microsoft-teams-to-manipulate-employees-into-allowing-remote-access/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315110](/post/id/315110)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/hackers-use-microsoft-teams-to-manipulate-employees-into-allowing-remote-access/)

如若转载,请注明出处： <https://gbhackers.com/hackers-use-microsoft-teams-to-manipulate-employees-into-allowing-remote-access/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1080**

* 粉丝
* **6**

### TA的文章

* ##### [侧边栏里的间谍假冒AI浏览器插件窃取90万用户数据](/post/id/315092)

  2026-03-11 14:01:17
* ##### [Kubernetes安全预警Ingress-Nginx注入漏洞可致集群密钥全局泄露](/post/id/315095)

  2026-03-11 14:00:47
* ##### [Budibase存在高危漏洞 可导致生产环境密钥全面泄露](/post/id/315099)

  2026-03-11 14:00:25
* ##### [Radware推出Alteon Protect实现云级ADC应用安全防护](/post/id/315102)

  2026-03-11 14:00:03
* ##### [研究人员打造AI智能体 可全自动实施诈骗通话](/post/id/315106)

  2026-03-11 13:59:37

### 相关文章

* ##### [侧边栏里的间谍假冒AI浏览器插件窃取90万用户数据](/post/id/315092)

  2026-03-11 14:01:17
* ##### [Kubernetes安全预警Ingress-Nginx注入漏洞可致集群密钥全局泄露](/post/id/315095)

  2026-03-11 14:00:47
* ##### [Budibase存在高危漏洞 可导致生产环境密钥全面泄露](/post/id/315099)

  2026-03-11 14:00:25
* ##### [Radware推出Alteon Protect实现云级ADC应用安全防护](/post/id/315102)

  2026-03-11 14:00:03
* ##### [研究人员打造AI智能体 可全自动实施诈骗通话](/post/id/315106)

  2026-03-11 13:59:37
* ##### [微软推出365 E5升级套件与Agent 365 AI管控平台](/post/id/315113)

  2026-03-11 13:58:42
* ##### [GhostClaw伪装成OpenClaw窃取开发者设备数据](/post/id/315116)

  2026-03-11 13:58:16

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)