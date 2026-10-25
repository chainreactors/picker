---
title: 【安全圈】荷兰白帽暗推两百万补丁！终结废弃软件僵尸网络危机
url: https://mp.weixin.qq.com/s/rbRm4e3kkpS-4uWkhjL0sg
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:07:12.350475
---

# 【安全圈】荷兰白帽暗推两百万补丁！终结废弃软件僵尸网络危机

# 【安全圈】荷兰白帽暗推两百万补丁！终结废弃软件僵尸网络危机

安全圈
安全圈

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

**核心事实**：荷兰网络安全机构 Eye Security 正式披露代号为“IXIM 行动”的防御战役。研究人员在合法接管已废弃软件遗留的更新域名后，直接向全球超过 200 万台受影响计算机分发了一剂特殊“良性更新”，强行注销其后台危险更新组件，成功化解了一场足以颠覆全球互联网的数百万级僵尸网络隐患

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyEED50QqCHQaaO6WrdubiauL1AfCBicXxvL3eLiaSFSHFuicUaBtckGUmXmFETLic7l4R51piaRqAlWeYvnRBj9t4lms8WhyoMxia8L8A/640?wx_fmt=other&from=appmsg)

## 🔍 遗留后门潜伏十年：SYSTEM最高权限裸奔

事件源头指向十年前风靡一时的 BitTorrent 流媒体客户端衍生品 Time4Popcorn。虽然原版项目早已停更解散，但数百万台装有机型的电脑仍在日复一日开机运行。该软件附带的后台常驻模块 `Updater.exe` 自带毁灭级安全硬伤：

* **最高特权驻留**

  ：在 Windows 下直接以系统最高权限 `SYSTEM` 运行，在 macOS 环境下则以 `root` 权限常驻启动项
* **明文轮询无校验**

  ：定时通过未加密的 HTTP 协议向远程服务器请求新版本文件，且对下载的二进制载荷不做任何代码签名验证
* **域名失效沦为公共猎场**

  ：其预设的回连域名多年前已到期注销，处于任何人都可以花几十美元注册接管的失控状态

该漏洞被正式分配为 **CVE-2026-30612**，美国 CISA 漏洞数据库直接给出了 **9.8** 的近乎满分严重评级。黑客一旦抢注域名，就能在数小时内将勒索软件或挖矿木马以最高权限分发给数百万台设备

## 🌐 惊人的失控规模：从家庭电脑到政企内网

Eye Security 在例行威胁排查中发现了客户笔记本上的异常回连行为。为了防范恶意分子利用，他们抢先注册了该废弃域名并架设接收分析节点。一经上线，蜂拥而至的连接请求高达每秒 50 次

在随后数月的监测中，分析节点记录到了超过 380 万个不同的硬件指纹。经过数据清洗和去重，实际受波及终端保守估计包含 **250 万至 300 万台 Windows PC** 以及 **25 万至 35 万台 Mac 电脑**。IP 采样分析显示，除了遍布全球的普通个人终端外，还出现了来自多家大型跨国企业、政府部门乃至军方网络的内网设备

## ⚡ 用更新机制消灭更新：白帽反推疫苗

软件原作者失联且软件早已死亡，官方补丁绝无可能出现。眼看随时有被网络犯罪集团接管的灭顶风险，Eye Security 在咨询资深法律顾问后，作出了极为罕见的技术干预决断：利用该软件的更新通道自制补丁疫苗

他们精心编写了一个极简良性载荷。该补丁通过更新通道静默下发至终端后，仅执行单一任务：**彻底停止并注销 Updater.exe 系统服务**。补丁不触动用户的任何文件，不修改流媒体主程序，更不收集上传任何隐私数据

## 🎯 杀软误报博弈与最终战果

行动刚开始时遭遇了戏剧性波折：有人将这套补丁上传至 VirusTotal，多家主流杀毒引擎因其“静默关闭 Windows 服务”的动作直接将其标记为恶意软件并实施拦截。而杀毒软件的每一次查杀拦截，都会导致脆弱的更新服务继续裸奔

团队随后对二进制代码进行了多次针对性重构，消除了绝大部分启发式误报，最终实现了平稳推送。截至行动结束，他们已成功修复了超过 **200 万台终端**，将来自全球的恶意回连流量压降了 90% 以上，为僵尸网络风险彻底拆除了引信。

***END***

阅读推荐

[【安全圈】PHP2Shell 遭百万次攻击，竟无一得手](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079470&idx=1&sn=1f84c3759d5f7bf34fcbd56949ea72a3&scene=21#wechat_redirect)

[【安全圈】9.0 分 Linux 内核 RCE，被一封邮件捅穿](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079470&idx=2&sn=f760b577c0f307d90d16107d46ad7e9a&scene=21#wechat_redirect)

[【安全圈】1177 万条！卡普空确认账号库被偷](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079470&idx=3&sn=4ed4671e35da838dae890d616c227665&scene=21#wechat_redirect)

[【安全圈】老乡鸡小程序又崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079459&idx=1&sn=9bbd43e57a372693618b7ed16c3c2af4&scene=21#wechat_redirect)

[【安全圈】单连接打崩服务器！HTTP3曝4000倍内存放大漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079445&idx=1&sn=faa0a86fd9d2ee022af099b2286cf0d2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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