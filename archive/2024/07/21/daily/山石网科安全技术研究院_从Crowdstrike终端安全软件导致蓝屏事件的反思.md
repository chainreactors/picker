---
title: 从Crowdstrike终端安全软件导致蓝屏事件的反思
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247507150&idx=1&sn=91eb6c465032efbcf0e738519c3228ba&chksm=fa520970cd258066e40e35b8927487652137d6d1960d6bd6765964260c11055768c99eba7168&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-07-21
fetch_date: 2025-10-06T17:41:15.283617
---

# 从Crowdstrike终端安全软件导致蓝屏事件的反思

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnR3uBVd4TmW1ibdf2jT8vH9BCg5ZibADicRvdHpY3zReCQFricYxCvToEIKO30hicGlStNvdGsTpJxH3BA/0?wx_fmt=jpeg)

# 从Crowdstrike终端安全软件导致蓝屏事件的反思

原创

4K457

山石网科安全技术研究院

## 关于CrowdStrike

CrowdStrike（NASDAQ：CRWD）成立于 2011 年，是一家全球知名的网络安全公司，CrowdStrike Falcon在终端安全领域市场份额高达17.7%，500强企业中有271家是其客户，根据 CrowdStrike公布的IDC 端点安全市场份额报告，它在 26 家供应商中排名第一。在2024 财年第四季度，他们的身份保护业务的年度经常性收入 (ARR) 已超过 3 亿美元，同比增长了一倍多。CrowdStrike 的集成 Falcon 平台是公司惊人增长的驱动力。

CrowdStrike 在其 Falcon 平台下提供 27 种不同的型号，允许客户选择自己喜欢的型号进行购买，其技术平台采用基于云的尖端基础设施，其 Falcon 平台专为一个控制台、一个具有多个模型的代理而构建。这些模型可以满足不同规模企业的端点、云、身份、SIEM 和数据保护需求。

## 事件背景

今天由于网络安全公司CrowdStrike Falcon Sensor的一项软件自动更新中的通道配置文件csagent.sys引发了Windows操作系统的“WIN32K\_POWER\_WATCHDOG\_TIMEOUT”错误，从而导致系统崩溃并出现蓝屏。初步估计，这次蓝屏可能影响了近千万台使用Windows的设备，目前也没有很好的恢复方法，只能一台台手动恢复，其中涉及大量关键基础设施，堪称一次核弹级的网络安全事件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnR3uBVd4TmW1ibdf2jT8vH9BlCadjser7A9HaMcrcI3IHVF6fWlNOaFh1GAFsjzvj78F5xkHj5YwlQ/640?wx_fmt=jpeg&from=appmsg)

此次蓝屏事件对于CrowdStrike影响非常明显，从多处机场航班地面停摆到银行服务、广播服务、医疗服务中断，再到电视节目停播，随着事件的持续发酵，CrowdStrike的股价应声下跌，开盘前跌幅超过20%，微软也受到了波及，股价下跌超过3%。这不仅是一次技术故障，更是对CrowdStrike的一次严峻考验，同类的厂商都应该吸取教训！

## 安全反思

1. 说到反思，首先想到的这件事是真不应该发生，作为一家历史悠久的安全大厂，只要正常进行过发布测试的软件都不会发生这么弱智的错误问题，除非是人为故意的，或者是被恶意黑客利用来进行供应链攻击，终端安全软件成了系统大杀器。

   ![](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnR3uBVd4TmW1ibdf2jT8vH9BiaJ9dAFBkUfGuiaKdQSw6y7TicrEWia36iaXSJNC737HzoOr9z6ZMohRmxQ/640?wx_fmt=jpeg&from=appmsg)
2. 通过这次事件，大家应该能感受到供应链攻击多么可怕，特别是像CrowdStrike这种自动更新的软件，没有经过用户确认，和一个木马后门无异，往大家的电脑里推送什么都可以！
3. 本次蓝屏可以通过恢复模式启动，或者多次异常重启进入安全模式重命名这个文件：**C:\Windows\System32\drivers\CrowdStrike\csagent.sys**，或者直接重命名整个文件夹**C:\Windows\System32\Drivers\Crowdstrike**。但如果连安全模式都进不去，只能使用WinPE解决，但又如果磁盘使用了bitlocker加密，就更加麻烦，需要在电脑之外有备份解密密钥，备份很重要！
4. 下面是 CrowdStrike 的官方解决方案，弱智的更新引发那么大的全球故障，发个公告都遮遮掩掩的，只有注册用户才能看，一点都不大气，也不是负责任的态度，大家是可以考虑更换供应商了。https://supportportal.crowdstrike.com/s/login/?ec=302&startURL=%2Fs%2Farticle%2FTech.Alert-Windows-crashes-related-to-Falcon-Sensor-2024-07-19

   ![](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnR3uBVd4TmW1ibdf2jT8vH9Bq1ZzRo1kBkrHfnV3HsUaAMq2leErwVVHTx0AianO9hESmuETBzxIsiag/640?wx_fmt=jpeg&from=appmsg)
5. 如果电脑终端数量非常庞大的企业是不是可以考虑分区域使用不同供应商的软件？甚至使用不同的操作系统，Windows、iOS、Linux等，避免像本次遇到供应链攻击或同类的故障时，所有终端一起全军覆没了，大家都可以摸鱼，唯有IT运维兄弟太苦了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZklJrRfHgD20mpib0des3hXE4j8wZVnQXn5007JuzcOjvaiaS9yVnx2RTYQCbTS7O3ogpmJ2PPiat6sa7KicT2ftw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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