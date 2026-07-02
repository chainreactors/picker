---
title: 为什么虚拟机是每个黑客的必备？一文教会你安装虚拟机的详细步骤！
url: https://mp.weixin.qq.com/s/rFx44Qn7i9S5ZPc-j5AoJw
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:54:50.856992
---

# 为什么虚拟机是每个黑客的必备？一文教会你安装虚拟机的详细步骤！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kzUNKm24hOoEKqjzvB0xn7eMiaEUHMPiahzPTayHj6Jwcwx3RAfsnA56kU6feXMzoch4pe30fgTALxKv72AWKK99u7hu1oDSM3W2KCO31Tuo0/0?wx_fmt=jpeg)

# 为什么虚拟机是每个黑客的必备？一文教会你安装虚拟机的详细步骤！

沧海讲安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

你知道真正的网安从业者，电脑里其实藏着无数个‘平行宇宙’吗？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9RjqWGV5cjNicshsOXCG9PpPRdq73O7eyicCSgh6dwkLwbscFa3YN1DXe8msQHePzvWJsWfWVur4FZNEJx6BxgOt1vQRs9PouSV0/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

因为为了在绝对安全的前提下测试高危漏洞，他们会在现有系统中搭建出一个与外界完全隔离的独立虚拟环境，这里既能联网进行模拟演练，又具备极高的安全性——无论操作如何破坏，都能迅速恢复且绝不波及真实系统。

今天，我们就来聊聊这个网安神器：虚拟机，并带你从零开始，亲手搭建专属的安全“黑客实验室”。

---

那为什么必须用虚拟机呢？

你可以把虚拟机想象成一台“机器猫”，它能在你真实的电脑里“变出”好几台完全独立的“虚拟电脑”。在网络安全的学习中，它扮演着不可替代的角色：

* 规避测试风险： 网安学习难免会接触到恶意程序或进行破坏性实验。如果在真实电脑上操作，极易导致系统崩溃、数据丢失。而在虚拟机里，无论怎么“折腾”，都不会影响你真实的操作系统。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9RDVUKwebyCrfJ2MficILzZ0QVlib9MzdcIsLMZDy3WowkHZJDiabsKzKJtl1yicOoqjD2DonFSkPcDAbrBlr5FUNOaekR973Zu6mM/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

* 打造专属靶场： 网安讲究“先建后破”。你需要自己搭建带有漏洞的网站或系统来练习攻防。虚拟机允许你灵活部署各种操作系统，轻松构建复杂的实验场景。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9QjcrABJiby1IFNZ7LF7EfP6LGzrHRF5ut4gEnM8L4RUwdupnvxtnkA9jzzbgKFC0eic9Ik3CEMXf6IpKYJs504ZrBZAwjdmUA1U/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

* 法律与伦理安全： 网安技术是一把双刃剑。法律是绝对的红线，未经授权对任何非己所有的网络进行测试都是违法行为。虚拟机为你提供了一个100%由你控制的、完全合法的“沙盒”，让你能在安全合规的前提下磨练技术。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9QXP7aoTxIL08XRh3POoaibb36TNx5xYYVickwevsibfANibGBg8xeJtIgJbdVqux74pIaK7dI7KhQCkv6A1aQzR7rMQibRiafXsdeRI/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

---

环境搭建实战指南：

对于新手而言，最推荐的组合是“VMware Workstation Player + Kali Linux”。VMware对个人免费且极其稳定，而Kali Linux则是专为渗透测试设计的系统，预装了数百种安全工具，是网安人的首选。接下来，我们进入保姆级的安装步骤：

* 第一步：安装虚拟机软件

打开浏览器搜索“VMware Workstation Player download”，进入官网下载适合你系统的免费版本。下载完成后，双击安装包，像安装普通软件一样，一路点击“Next”即可完成安装。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9TRrZrhzjQFjZHwtRf2ILoqo6eBBaickk5Ejr4L5ZGJSGHTcA0aFCZ0dz6qZrMmiaIiajpFhW3RFwqvrywwpuOPwuAoGdibGIicibWXs/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

* 第二步：获取系统镜像（ISO文件）

我们需要一个操作系统的“安装盘”。访问Kali Linux官网，在下载页面选择“Virtual Machines”（虚拟机预装版）或“Installer Images”（安装镜像版）。

对于新手，推荐下载预装版，可以省去繁琐的系统安装步骤；若选择安装镜像版，请下载最新的64位ISO文件。

![图片](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9TNhiczMEhndsFu2KdzHJ9icNebqpCr4jj9MnibJ2YJMiccpm0oaVAHA3L0MH8rQQNQ6KicpqZibV0GGmJdabFickMWZRUqJX4aIR3Nek/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

* 第三步：创建你的第一台虚拟机

1. 打开VMware，点击“创建新虚拟机”；

2. 选择“安装程序光盘映像文件”，浏览并选中你刚才下载的Kali镜像文件；

3. 给虚拟机起个名字（如My-Kali-Lab），切记将安装位置设置在非C盘，以免占用系统盘空间导致电脑卡顿；

4. 在磁盘设置上，建议分配40GB以上的空间；

5. 并选择“将虚拟磁盘拆分成多个文件”，方便后续管理。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9TQicXRPibuIv53wB8zlq7Tibt0fvfK8Du2nZTJ468VQD4icRIxAdcJrDv8lX0VBn5nkGrmsHKWuprEgl1UOXNxWNXjTzwPuDoAzko/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

* 第四步：优化硬件配置

在创建向导的最后一步或创建完成后，点击“自定义硬件”。

为了保证Kali运行流畅，建议将内存调至至少4GB（8GB更佳），处理器数量设为2。同时，移除不必要的“打印机”等硬件设备，确保网络适配器处于“NAT模式”（这样虚拟机就能共享你主机的网络上网了）。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9RUa26pJIoHdNknCUPKcXCuU0t4m9RGTEwtf9aYQNAz5YgVLQRleoAbvFpS2NABo93WiaTXwvQvEyX9RFQNcaGfFIBlqicUzURIw/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

* 第五步：启动与系统配置

点击“开启此虚拟机”。

如果你下载的是安装镜像，系统会进入图形化安装界面，按照提示选择中文语言、设置时区、创建用户名和密码即可（密码务必牢记！）。

如果你下载的是预装版，系统会自动解压并引导进入桌面。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9SuzN5GeMI2ZY2dOJicc0ZR1tCWkCA7SXiaMuA3u5sFlqgloAz4DtKv2tZn2wjU1libsSh7JnMgF9zx6iaCKiaUOR7PkKXnLQZpsa68/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

当Kali的桌面出现在你眼前时，恭喜你，你的专属“黑客实验室”已经搭建成功！允许你拍照发朋友圈，但这一步完成，真正的网安学习也才刚刚开始......

---

---

「最后」

如果你真的想学好一门本事，首先就要考虑自己对这门技术的兴趣，没有天赋还能靠时间和努力去弥补，但如果没有兴趣加持，就很难坚持到最后。

你要是正打算尝试网安或者想努力一次，我把这些年用过的视频教程和学习笔记都梳理出来了，现在都无偿分享给大家，需要的找我拿就行（文末自取）。

现在哪个行业都不好走，如果没有学历也没有天赋，那就只有努力和坚持了，请相信相信的力量，共勉！

**沧海专属黑客/网络攻防技术资料**

@沧海讲安全：在安全圈待了十多年，已经积累了很多的技术教程，在计算机这个行业，如果不会主动学习，手里没点学习资料，注定是走不远的。我整理的这些资料包含了市场上主流的攻防技术，不说让你成为黑客大佬，帮助你从0到进阶网络安全技术问题不大。

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

**部分技术资料预览**

**01**

***视频教程***

从0到进阶主流攻防技术视频教程（包含红蓝对抗、CTF、HW等技术点）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcYaRKqWc1cxP8sBrX6KZasFTJEVibWmdyoGAuRO4AbzaVjUJ8guoWAzQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcCP8oaOCQm8Cp2qhpCxWiaOjzYrOoA1iac5eSafBicPxSQcpYtchyfVvxA/640?wx_fmt=jpeg&from=appmsg)

**0****2**

***书籍Pdf***

入门必看攻防技术书籍pdf（书面上的技术书籍确实太多了，这些是我精选出来的）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcUumOTUmUznuo7MzKl1JiaEQIeSh4ibkO6jxY68zVZz7iayrwGRtGu2bHw/640?wx_fmt=jpeg&from=appmsg)

**0****3**

*安装包/源码*

主要攻防会涉及到的工具安装包和项目源码（防止你看到这连基础的工具都还没有）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcvsT9h4B1hS9VEPengMcOtNL24949kb4cibKLS9HkIb1k2htW8GYqzMQ/640?wx_fmt=jpeg&from=appmsg)

**0****4**

***面试试题/经验***

网络安全岗位面试经验总结（谁学技术不是为了赚$呢，找个好的岗位很重要）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6Kqcm6J0eAql29R6DIM8bJW4rweVBicM8ibGMOmLNFTpdcQ0gFvefMTOg9dA/640?wx_fmt=jpeg&from=appmsg)

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

@沧海讲安全：只要你是真心想学黑客/网络安全技术，我这份资料就可以无偿共享给你学习，但是想学技术去乱搞的人别来找我，目前全球网络环境日益紧张，我国在这方面的相关人才比较紧缺，网络安全行业确实也需要更多的有志之士加入进来，我也真心希望帮助大家学好这门技术，如果日后有啥学习上的问题，欢迎找我交流。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kWXbooRKsCUic8In0GE4Hd6nTM7iclEUG0UewS479kicpBqGcfpOAaTibhgwsEsblvqe0EsP95XKBe2E90T9g02cQg/0?wx_fmt=png)

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