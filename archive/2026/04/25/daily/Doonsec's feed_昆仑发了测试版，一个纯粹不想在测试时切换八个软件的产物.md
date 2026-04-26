---
title: 昆仑发了测试版，一个纯粹不想在测试时切换八个软件的产物
url: https://mp.weixin.qq.com/s/zaTqEQulTFojjmWoTzhW8Q
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:59:00.145941
---

# 昆仑发了测试版，一个纯粹不想在测试时切换八个软件的产物

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3oR6eMARh6z3MjUMI3BP5XbXnW3OPvibHrD7mibX1QdqHBSdrcnKKZcx7okMNAKWgmRPEPO1FbmIsnoWkgPls2NjhKVSyKOTmbCW6ibvVr5NBA/0?wx_fmt=jpeg)

# 昆仑发了测试版，一个纯粹不想在测试时切换八个软件的产物

原创

昆仑AI安全实验室
昆仑AI安全实验室

昆仑AI安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

昆仑这名字听着挺唬人的，其实就是一个渗透测试工具。今年我开始做这个的时候，纯粹是因为每次做红队项目都得同时开四五个工具，任务栏塞得满满当当，切来切去烦得要死。于是就想，能不能把这些活儿归到一个软件里，让它从外网打点一直干到内网横移，中间不用跳出去开别的。

几个月过去了，这东西终于能勉强见人了。今天发测试版，先说好，bug肯定是有的，功能也还差不少，但核心的攻击链路算是跑通了。放出来主要是想听听大家的骂声，好知道接下来该往哪儿改。

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6xQxBxiabQR2aXpkVoC6qbq8ZSFx2VibVUx18TBDXmQ31Oo7eFKSkibJJAicVx3FibmrKjLIdiaSIMH5Pic33EJeIboJLPQhsaxRH7oWs/640?wx_fmt=png&from=appmsg)

**一、它能干点啥**

简单讲，我把平时挖洞用到的那些功能尽量往里面塞了。

**找资产**

对标Goby做的，基础的端口扫描、Banner抓取、JA3指纹、favicon哈希这些肯定有。花了最多时间的是一个叫FID的东西——当碰到一个网站，域名没有、证书没有、logo也看不出来是什么的时候，FID会自动去提取网页结构、响应头顺序、静态资源这些特征，把它跟已知的资产归到一类。有次护网靠这个找出来三十几个没在资产管理表里的边缘系统，里面藏着三个高危。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6y00oa9L5ME8kVJ4U4TibEiaoTZRZ1ibqzQclxydicMl8KgrrXZ8E5HbCARUdCcvb19DT1Y5at1LLIDibGAayZSUBplBx6RpaSiberWw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6zR1ZichLpojjGx4iaRxEpuxMg8wUqiat6xxIeZEjHfbnTgsuricicdAzfnt8dd6tV70jUzycur65JQrqkrdGlFl5wNLFCNSxs2UwmU/640?wx_fmt=png&from=appmsg)

**抓包改包**

对标Yakit和Burp做的MITM代理。HTTP/HTTPS/WebSocket都能截，断点修改、自动替换规则这些该有的都有。另外做了个Fuzztag，在请求的任意位置打标签就能批量生成测试数据。有次测一个支付接口，几分钟跑了几百种参数组合，结果发现一个并发竞争漏洞，金额可以改。客户安全团队后来说他们用商业扫描器扫了好几天都没扫出来。

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6yPrwOtWzlN8xiaaOC0GCzalJBFvaJA2ia5dK95HZaLQFUmmsADIETcVFXU5bLJUbyF37Emod7qlToNgF389Q7zMKiapyPrbpwA6Y/640?wx_fmt=png&from=appmsg)

**漏洞验证**

PoC引擎支持沙箱执行，内置了DNSLog、HTTPLog、LDAPLog用来检测无回显的洞。PoC写完直接热加载，不用重启软件。目前内置PoC只有千把条，跟商业扫描器的几十万条没法比，但这块后续会慢慢补。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6xzoMhugkgKibrTpTHwoiaMkYr0YHBmK5dLxuvliaJ9BAs08NIBAINkICuwXd2wGFicrujgPt1PLs7mAMHXq2kZqbXX3dVFqfjkkew/640?wx_fmt=png&from=appmsg)

**反连平台**

做了多协议端口复用，单个端口同时监听DNS、HTTP、LDAP、RMI。有次测一个云服务商，外网打不进去，在一个API的User-Agent头里插了JNDI Payload指向我的反连平台，等了一会儿收到内网服务器的LDAP回连，直接拿到了反向Shell。这个漏洞如果没有反连平台，大概率被当成“无回显”略过。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6wbOKlsaIPYX2Arn12gALdx0qMollibb3rxIyjG8x3QicgUmIFcZh9zJODwvucnFMlZ0zsL14XvfyzZSH3tayxatZdFJMBOf1lJ8/640?wx_fmt=png&from=appmsg)

**C2和横向移动**

这块是全自研的，纯Python写的。Beacon支持HTTP/HTTPS/DNS/WebSocket几种协议，通信做了加密和流量混淆。横向移动功能包括哈希传递、票据传递、WMI、SMB、WinRM、计划任务持久化。

去年有一次攻防演练，从一台暴露在公网的交换机开始（admin/admin这种默认密码），一路横到域控。全程就在昆仑里操作，没切换任何外部工具。从发现那台交换机到导出域控的krbtgt哈希，一共花了十八个小时。

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6x8iaeUCJkupNO5rpu5d8VgvEyLLpUHEjOZcaHSsbGdMHribx0WG2nvkSC6K09poicR7L7KA2pYkjicFAiarm3eIAat48wibweDeGRbg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6yddIsklKSicqRWcFLJbJUibKibc61vIHgcKibgqPXqcsvZFte4yw539jQ5ZHId3HQ6Kus3PZvO43ia79LYiavj9REBBs2C8K98TcyKk/640?wx_fmt=png&from=appmsg)

**二、几个真实案例**

**交换机到域控**

上面提到那次演练，目标是一家制造企业。我先用FOFA搜到了他们一台暴露在公网的华三交换机，管理界面直接admin/admin登录。翻配置文件，在注释里发现了一个监控账号monitor的明文密码。

用这个账号进了同一网段一台Windows服务器，在LSASS内存里抓到了域账号的NTLM哈希。然后在昆仑里直接做哈希传递，横向到另一台成员服务器，那台机器上恰好有个域管理员账号在活动。注入他的会话，执行DCSync，导出krbtgt哈希。整条链走下来，从发现那台交换机到最后拿下域控，刚好十八个小时。

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6z2OuFQ0YUCFLOic8GVHyXMZEd09etXKsLYfty5HIIvaxibaShbJibScVg2X1m2yaAgVibLNdbzIKibxBLYicuk936IuIp92WKyrB38U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6zeRcG0A05QibIN3ra9xgjiaN4ejCf6GQW7ZLeU8Op3L1nhj6LsEgsCiaHUoax3zkq0DG1EwAsMuYTaG2eNiazw5cTeeuj4vwHnicNk/640?wx_fmt=png&from=appmsg)

**反连平台捡漏**

给一个云服务商做测试，外网扫了半天没找到能用的漏洞。随手在一个API的User-Agent头里塞了个JNDI Payload，指向昆仑反连平台的LDAP监听端口。

等了一段时间，反连平台收到内网某台服务器的LDAP回连请求。通过LDAP通道投递了一个恶意Java类，拿到了反向Shell。后来定位到这台服务器在第三层内网。如果没有反连平台，这个漏洞大概率被当成“无回显”直接忽略了。

**影子资产发现**

某互联网公司SRC，常规扫描只发现了十几个资产。我用FID对已知资产的Web页面做特征提取，然后对C段全扫。结果匹配出了二十多个没有在DNS里记录过的影子资产。其中一台是废弃的测试环境，上面跑着老版本GitLab，有已知的RCE漏洞。从发现这堆影子资产到进去，全过程不到一个小时。

**三、目前存在的问题**

老实说，这个东西现在还比较粗糙。

第一，HTTP/2代理还没写完，QUIC更是在排队，WebSocket也只能看不能单帧修改。第二，PoC库目前只有千把条，跟那些商业扫描器动辄几十万条规则比起来确实寒酸。第三，插件市场现在只有我在上传，生态还谈不上。第四，功能稳定性还需要打磨，复杂的生产环境可能会遇到一些意料之外的问题。

但核心的链路是通的，我自己在多次攻防演练里验证过，拿了几个省级优秀攻击手。如果你也是干这行的，应该能理解这个东西的价值在哪里。

**四、怎么搞到手**

昆仑走闭源发布，源码不公开。用户能在GitHub公开仓库直接下载打包好的exe文件。

下载地址：https://github.com/xyz-1008/Kunlun-Penetration-Testing-Platform

以下是部分功能图片

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6wN63jBYyPicd3Huvvm0VnbWod5alPIQfSJ1tr1TyicOsojJ7ia8NSpzHEp9VFaGBgIgNkzZZ0libbn197G7cN4qq7qjouDpLDoibFA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6y7YlfCstxs5Tnm09VScRPFDuoKxW2BNXS3JoNibGzTwkbnUFWzAfkxslhItDoJaGoMR36laHZ5Zl984FeBvoSPc83VIibyuibXcU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6wa2RqYOia1FEkrV8r3VZkG3ic1LHyaxmUicRX1bRbSXQDLW45KWwfzEDkJibOm9Qxt4KWVO75iaQaWfTO25NdqtLCcHX0uFI8Gibm8M/640?wx_fmt=png&from=appmsg)

安装简单：

1. 下载exe，双击打开
2. 首次启动有个向导，会引导你初始化数据库和生成根证书
3. 完了就能用了

文档还在写，目前有基本的功能说明和插件开发指南。碰到问题去GitHub提Issue，我看到就修。

**五、最后唠几句**

做了几个月，中间推倒重来了好几次。有时候一个模块写了好长时间发现架构不对，全删了重写。最崩溃的一次是PyInstaller打包完各种闪退，查了很久才发现是某个依赖的版本有问题。

市面上不缺好用的工具，Burp好用，Goby好用，Yakit也好用。我做这个纯粹是因为没有一款工具能让我一个人从头打到尾中间不切换软件。

昆仑就是给“一个人的红队”准备的。它不完美，但能用。如果你也受够了在好几个工具之间来回切换的折腾，不妨试试。

发现问题随时反馈，我尽量第一时间修。昆仑可能还有很多不够完善的地方，希望各位同行多担待，有什么建议直接提，咱们一起把它改得更好用。均为测试版正式版截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6w66hLOgpngP8KiapR1rrlN7suEhRicFUXd6McpEZmvRulHk8TtkeSxcMLGsngVVoYp0wsHF50mmDlKz12n2e5mgYtibdkUUJKq2c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6wdURquYcV1JDOHj1tZumZAQYZ14AS4hoORF5sLk8tYe5BVaIAXQom9T47VOPO7jENuClUEYL3u6OFyVswuhWZcGhMAjdMFhgM/640?wx_fmt=png&from=appmsg)

//昆仑AI安全实验室|创始人兼安全工程师专注AI接口安全与企业级网络安全服务AIToken中转分发/红队渗透测试/企业级安全加固/定制化AI应用开发/软件开发为个人、商家、电商及短视频平台提供稳定、合规、高可用的技术解决方案 合作方式在公众号

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zxPsSBiaTT0QiaBjibScxViciathof2tlahJCticqia6DncZNe4Fiatd1zWxPQKdTAqnyRPFWmxviaJJm5R8JLbEAURJnZRMiaKa1quLS8k/0?wx_fmt=png)

昆仑AI安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zxPsSBiaTT0QiaBjibScxViciathof2tlahJCticqia6DncZNe4Fiatd1zWxPQKdTAqnyRPFWmxviaJJm5R8JLbEAURJnZRMiaKa1quLS8k/0?wx_fmt=png)

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