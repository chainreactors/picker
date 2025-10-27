---
title: 新型PyPI攻击技术可能导致超2.2万软件包被劫持
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546790&idx=3&sn=81e60ddbbf403f47437bf803cc835e72&chksm=fa938167cde4087139c1c5b9ca20adae3ad975a69d3fd28037c50169a135a6a1a1381a9f9280&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-09-07
fetch_date: 2025-10-06T18:29:12.863161
---

# 新型PyPI攻击技术可能导致超2.2万软件包被劫持

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lrHvS5NUY4Mj1UM7KETFlB7P5M0MBkfEutSX6HfePL5nNfsLmtYAqC2PpwZTNibKryCbZia05Y6fUA/0?wx_fmt=jpeg)

# 新型PyPI攻击技术可能导致超2.2万软件包被劫持

网络安全应急技术国家工程中心

一种针对 Python 软件包索引（PyPI）注册表的新型供应链攻击技术已在野外被利用，并且目前正试图渗透到下游组织中。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38NgF4pibf9fXY1fwksPYG9BfxjLBWNvMD0HddiblFvtE7gCGNI6GcicyoVF9MAibDQOJfjfAmnpCQWYA/640?wx_fmt=jpeg&from=appmsg&wxfrom=13&tp=wxpic)

软件供应链安全公司 JFrog 将其代号定为Revival Hijack，并称这种攻击方法可用于劫持 2.2万个现有 PyPI 软件包，并导致数十万次恶意软件包下载。这些易受攻击的软件包下载量已超过 10 万次，或已活跃超过 6 个月。

JFrog安全研究人员Andrey Polkovnychenko和Brian Moussalli在与《黑客新闻》分享的一份报告中说："这种攻击技术涉及劫持PyPI软件包，一旦这些软件包被原所有者从PyPI索引中删除，就操纵重新注册这些软件包的选项。

这种被称为“Revival Hijack”的技术利用了一项政策漏洞，允许攻击者在原始开发人员将软件包从PyPI中删除后重新注册并劫持软件包名称。

与传统的域名抢注攻击不同，Revival Hijack攻击利用的是用户拼写错误的软件包名称，而传统域名抢注攻击则利用了热门软件包的删除和重新注册。当开发人员从PyPI中删除他们的项目时，软件包名称就会可供其他任何人注册。然后，攻击者可以上传这些软件包的恶意版本，毫无戒心的用户可能会下载并安装这些软件包，并认为它们是合法的。

JFrog 分享的统计数据显示，平均每月约有 309 个软件包被删除。出现这些情况的原因有很多，比如：缺乏维护（即废弃软件）、软件包以不同的名称重新发布，或将相同的功能引入官方库或内置 API。

这也构成了一个有利可图的攻击面，它比错别字抢注更有效，攻击者可以利用自己的账户，以相同的名称和更高的版本发布恶意软件包，感染开发者环境。

虽然PyPI确实有防止冒充作者和抢注的措施，但JFrog的分析发现，运行 “pip list--outdated ”命令会将假冒软件包列为原始软件包的新版本，而前者对应的是来自完全不同作者的不同软件包。

更令人担忧的是，运行 “pip install -upgrade ”命令会将实际软件包替换为虚假软件包，而软件包的作者却没有任何警告，这可能会让不知情的开发者面临巨大的软件供应链风险。

JFrog 表示，它采取的措施是创建一个名为 “security\_holding ”的新 PyPI 用户账户，用来安全地劫持易受攻击的软件包，并用空的占位符取代它们，以防止恶意行为者利用被删除的软件包。

此外，每个软件包的版本号都被指定为 0.0.0.1，这与依赖关系混乱攻击的情况正好相反，以避免在运行 pip 升级命令时被开发人员调用。

更令人不安的是，Revival 劫持已经在野外被利用，一个名为 Jinnis 的未知威胁行为者于 2024 年 3 月 30 日引入了一个名为 “pingdomv3 ”的软件包的良性版本，而就在同一天，原所有者（cheneyyan）从 PyPI 中删除了该软件包。

2024 年 4 月 12 日，新的开发者发布了一个更新，其中包含一个 Base64 编码的有效载荷，该有效载荷会检查是否存在 “JENKINS\_URL ”环境变量，如果存在，则会执行从远程服务器获取的未知下一阶段模块。

JFrog认为攻击者可能推迟了攻击的发送时间，或者将其设计得更有针对性，将其限制在特定的IP范围内。

新的攻击行为表明，威胁行为者正盯上更大规模的供应链攻击，以删除的 PyPI 软件包为目标，从而扩大攻击范围。建议企业和开发人员检查他们的 DevOps 管道，以确保他们没有安装已经从版本库中删除的软件包。

JFrog安全研究团队负责人Moussalli表示：利用处理已删除软件包的漏洞行为，攻击者可以劫持现有软件包，从而在不改变用户工作流程的情况下将其安装到目标系统中。

PyPI 软件包的攻击面正在不断扩大。尽管在此进行了主动干预，但用户仍应始终保持警觉，并采取必要的预防措施来保护自己和 PyPI 社区免受这种劫持技术的侵害。

**参考链接：**

https://thehackernews.com/2024/09/hackers-hijack-22000-removed-pypi.html

原文来源：FreeBuf

“投稿联系方式：sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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