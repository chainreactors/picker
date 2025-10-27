---
title: 突发：CrowdStrike软件更新导致全球各地Windows计算机瘫痪（附修复措施）
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501756&idx=3&sn=0cd0ef95b61d5a80ae261b8ca7424bd4&chksm=fe79e324c90e6a3292cd35e20393db55be15df9b3461cc2d6c65b727546a1a4754a170a90ba6&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-07-20
fetch_date: 2025-10-06T17:43:08.259859
---

# 突发：CrowdStrike软件更新导致全球各地Windows计算机瘫痪（附修复措施）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs495dPll9Zecl6bMiaoo4JGnFZh6Q19BQunzaERBaIWWibOwAGCLfggOjSRek6Aicz7rKd6pW4IMZx4icA/0?wx_fmt=jpeg)

# 突发：CrowdStrike软件更新导致全球各地Windows计算机瘫痪（附修复措施）

奇安信 CERT

**一、事件过程**

北京时间2024年7月19日下午，全球大量Windows用户在社交媒体上晒出电脑蓝屏画面，出现了大量 Windows 10电脑崩溃、显示蓝屏死机、无法重新启动的案例。在国内“微软蓝屏”迅速登顶微博热搜，成为热议话题。随后。蓝屏问题被确认与CrowdStrike的软件更新有关，导致Windows用户出现了蓝屏现象。

![](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs495dPll9Zecl6bMiaoo4JGnFiaE7ygJ9QIiclUicQ8ZDgKvPqQZZNkGusSdMxHKnicic26L5VzEMccSKWDA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs495dPll9Zecl6bMiaoo4JGnFVAsO9nibdY7KSkZSA7sV2eDG4J7I5QECA55r7kFcyjVTCI5Efld9Nsw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs495dPll9Zecl6bMiaoo4JGnF0AmzaHabjannibGT0gxy6kzqFbLcwsR6JFhzfRf3icaQa7hneaoEOHmQ/640?wx_fmt=png&from=appmsg)

CrowdStrike于7月19日下午发布相关通知承认了这一问题，并表示其工程团队正在积极解决此问题。

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs495dPll9Zecl6bMiaoo4JGnFhynHJUlLxP6z5S5sLY1FaztuDLztmF17ztDjWshaXdaHuHqHmyM3Qw/640?wx_fmt=png&from=appmsg)

**二、事件影响**

CrowdStrike软件更新导致全球计算机瘫痪事件造成了严重的影响，福布斯新闻、彭博社、卫报等主流媒体均对此事进行了相关报道，报道称美国和澳大利亚有多家航空公司停飞航班，其中墨尔本机场发生了停电，导致大规模航班延误。此外，报道称网上银行服务也受到了影响，导致客户无法登录或交易，广播公司也遭到被迫停播。

![](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs495dPll9Zecl6bMiaoo4JGnF0hBFLBxvoicTEDgGiaztlzwAmicrO2VX0eKs91hhGicPia3NZzYekhibTqkA/640?wx_fmt=jpeg&from=appmsg)

**三、修复措施**

对于遇到此问题的用户，可以尝试以下措施来修复：

1. 使用安全模式或恢复模式进入操作系统。

2. 进入 C:\Windows\System32\drivers\CrowdStrike 目录。

3. 找到所有匹配“C-00000291\*.sys”的文件，并将其删除。

4. 正常启动主机。

或者直接重命名以下文件夹：

“C:\Windows\system32\drivers\CrowdStrike

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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