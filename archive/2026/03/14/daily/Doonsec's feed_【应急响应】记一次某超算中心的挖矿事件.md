---
title: 【应急响应】记一次某超算中心的挖矿事件
url: https://mp.weixin.qq.com/s/umqb_9Z0wJe5PRfy3bVjFQ
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:30:59.037597
---

# 【应急响应】记一次某超算中心的挖矿事件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JRTVZz6AumPpu1Z98wgtKG684YhFMlJfo8SJqgR71CLgo1RwuppopaXIW2PQe63eW0m4Q3KbsEeWp0fUPiad81Vkh5W4Hdib5n5aSpNYd0GBs/0?wx_fmt=jpeg)

# 【应急响应】记一次某超算中心的挖矿事件

原创

十二主神
十二主神

十二主神

![]()

在小说阅读器中沉浸阅读

**前言**

点击下方 "**十二主神****"****公众号关注, 设为****星标**。有用的话请点赞、收藏备查。

# 01-事件背景

根据某省超算平台中心应急响应工作要求，针对超算中心提供的超算平台服务器（172.16.0.x）及相关服务器进行应急响应，发现此次挖矿事件中被黑客利用的漏洞和系统脆弱点，还原整个攻击过程，恢复服务器正常业务运转，并提供应急响应报告和系统整改意见。

# 02-技术方法

通过可控的应急响应技术对受影响的相关系统服务器和终端进行事件分析和风险排查，对被利用漏洞进行定位和验证，以及还原具体攻击路径。本次应急响应将采取以下技术方法：

|  |  |
| --- | --- |
| 日志分析 | 通过对应用日志、系统日志、中间件日志和安全设备日志等进行攻击痕迹和可疑访问行为等进行分析，发现服务器和终端存在的安全隐患和黑客的攻击路径。 |
| 攻击溯源 | 通过对攻击者在服务器和终端上留下的痕迹进行逐步分析，如系统日志等，从而逐步还原攻击者的攻击路径和利用的漏洞。 |
| 程序沙箱分析 | 通过对服务器和终端上发现的恶意程序进行沙箱分析，代码分析，从而识别恶意程序的逻辑，恢复服务器业务或系统正常，如分析病毒程序，破解病毒原理进行服务器恢复等。 |

# 03-应急工具

|  |  |
| --- | --- |
| 工具类型 | 应急工具名称 |
| 日志分析 | LogViewPro、Papertrail、elk等 |
| 后门与webshell扫描 | D盾、WebShellKiller等 |
| 攻击溯源 | Wireshark、Dsniffer、LogViewPro等 |
| 恶意程序分析 | IDA pro、winhex等 |
| 漏洞验证 | Metasploit、sqlmap、burpsuite、CVE利用脚本等 |

# 04-分析过程

2025年08月27日9：30到达客户现场，通过客户针对此次应急事件沟通，发现客户已采取措施：

* 中断服务器（172.16.0.167）连接互联网
* 通过出口山石防火墙对访问SSH端口进行限制
* 172.16.0.167服务器已经经过两轮的人工查杀

查看态势感知告警，在8月16日晚上19：45分出现frp代理工具事件告警

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumN8hdczjZMSoeH5WBvQicziaWEsm9EMFS4uhDyR8HqM5BLa1paby9NKEAyCiaZqdp7NZq9cEbndmxq47PHGniblMZfrPVl9MeceyJs/640?wx_fmt=png&from=appmsg)

攻击IP为45.79.108.110，位置归属在美国加利福尼亚，威胁情报也标记此IP为反向代理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumOwYGWFVahCmeTLWV4Dpgdc6zibU37ZiaoIrvm2ZntzvKcEqgmopk7BDYUKqKWCgMS05fNATPQVgFJjBrkFdvrU095TwSPCUxklc/640?wx_fmt=png&from=appmsg)

通过态势感知拉取8月16日的所有日志，发现在19点17分的时候，使用cip.cc域名对出口IP进行探测，此时攻击者获取了172.16.0.167服务器的权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumOV1pU6nmeQSea1OHl2268tq2gaGgGkuYYGwsBJ1pW3q8KblAUDjD9YSibd9vrY5vWhG5EtUUQQOkZNWXUdI7ns4fbflnwkxuDo/640?wx_fmt=png&from=appmsg)

其次在19点23分的时候，攻击者通过167服务器访问39.106.248.18，下载了两个tgz文件，文件名为l1.tgz和l.tgz

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumOE8H8GH8qicS972QlWQArFv6MsllDZvOCaU05js1TGagNNLSksREdpkkgCQw0rzTkTX3A6bkwm7JxFKd4Jz1McG5UfcoURCqxw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumNMv4ACSWaogAND5FtnAiamzJXphcZX26YibUSpau47oYQNFH4ibmPz1yYrXRrRSvzA640D4ncnnRqS1s5dfsdbiaRictWkI2fsIic0w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumOIQPL5FGTZDUrsUD0hkQiaCTibphicNAupIqicafWuEg9Q3eBib37oTsjYjT6icGSzhrCOGBNgY5Yia7DgaqE9vHwicJ93dG8vXDxjYX4/640?wx_fmt=png&from=appmsg)

其中针对l.tgz进行解压，解压完之后是l.tar压缩包，对l.tar进行解压，解压完成之后得到lan文件夹，打开lan文件夹发现是内网代理frp工具，并且转发了SSH端口

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumPVFEyTf1zFiaKZia72Afn2Dy2lWToW7gOicp6kSAONZEfjeJ8JmyQiaxSibbWfeafqcGFjiaqmPe2CzScw55Z5VwibQvkKOLzniaNbdRc/640?wx_fmt=png&from=appmsg)

然后对l1.tgz进行解压，得到l1.tar压缩包，对l1.tar进行解压，解压完成之后得到Localroot-ALL-CVE文件夹，发现是Linux系统提权脚本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumPcFH76YoqRcBichsdv552HtZciaLXdgoHt5A5nszcSdcbIULOEBKILGEL9SABkcHTGIOJWHggibg54MfaB4icHjalFBTNZrFCcEjw/640?wx_fmt=png&from=appmsg)

从态势感知上分析19点23分之后，攻击者开始挂上frp内网代理软件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumMrbWvL5WKNqjZsMvBMzPicnjS2p9t7AjQ4pxicz5XzPOLjicSAg7oJOGh53PPkMLtdnHwfoxPy3jpjy5iaOEwYspJO9vuvlS9LKJk/640?wx_fmt=png&from=appmsg)

一直持续到20：02左右，攻击者下载了g.tgz和tunnel文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumNvRuJjkTqYys1vBgxzQcSiciaSqRRHI70EC349TW1LMsfR5P2GmENghMtbgRbVDl2mf7JvdhkS6rlSokxbezfsia8PT4hj8RoABE/640?wx_fmt=png&from=appmsg)

下载2个文件进行分析，在下载的过程中，杀毒软件直接报bitcoin挖矿病毒，并且查杀了

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumMJW6PQxPXpkVqxygvW6mXicDgRQziaKLOgsf5UP5icia1GnGTess9OtR4l2eYDpxV1pxah7ocJvS9fpeYkabBOAKicl7jWQOcqxAPE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumNtK4G1NVo9hpx7FjibJuVUiaZjL46rY9NUQIOcACw4KGXv6p5B7FsLGCaTeDlI8flVDWtz5Xicka031Eb3bGfMQDiaPLVkGQ1ZyeE/640?wx_fmt=png&from=appmsg)

找回文件进行解压得到两个文件go和mihner

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumMZAIZeVyJJ3IMWFCwhSt6U8psLOFzfbiaGLZXoeZfMlhNicOqX3iaHdhVZXqEOdFCXhibpibyLCQSJYIkkfjGdC5Jwab9AXic76kPbo/640?wx_fmt=png&from=appmsg)

通过沙箱分析证明minhner是挖矿病毒程序

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumPBQHiaibcDAWCEpqhdrRCl4q4wicpFWITMjyiaP3j6EmSGFUpomeVICpmWmkACfRk9httG52TsORQJXJp6U83ISdCibGsvB3wS1ftE/640?wx_fmt=png&from=appmsg)

go为后门植入恶意脚本，复制mihner挖矿病毒到系统随机名称文件，并且删除miher、go、g.tgz等原始恶意挖矿病毒。

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumOnu3WMpg7d7XBsN68BlTmTOAHZ6vbxFTlGLwA3tiawPDy024QVsZEAPyLKNhaia6bNKia5QrZ3gVgz4AGlt81s20CzmnpGDoCZt8/640?wx_fmt=png&from=appmsg)

针对tunnel文件进行下载分析，发现是红队gost代理工具

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumMznvzo42KMw2Ao84OE8vRImvXyhmjdCHc17tynPHsY7na8Z14IWUS0YiaLucvJM1Jict2wKwNzwaWicJ5VhIWicicVMicibibfZcDsbsU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumMH32gUdEB2gqkPOTeyxHdws247sQ8thOHF330VT1DmdsmzdPicGGhLxc2m9OvVODYDk9oYy6szCqGQ2LUSnz36Zc9yRFQUwic6c/640?wx_fmt=png&from=appmsg)

在20：03执行了挖矿病毒程序，开始连接45.33.69.138、192.81.128.77矿池地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumMkdt09OZHzgVia8t4n8VFNQDbk5bzqSJpaEIwCB35b3O66jKiahaibYsibMJqUj8w0l7OTxhnCoggM8NMic1p1ibwWNhWXCGOfaZxeo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumPpDEb1JV6lTVQBtbBewKRJZ73BSicl9uVXp04icOhFHaGSNzNjE3XyPaq10sHcNW8fKqOBlqIPztw1OT2SqHFmk4bZYrMM01IK0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumN9zjy2rPyvNfaDWXX4thoeY1HsF7f7B30HW0yozSnoQnbZiau0vqOicicy3YI3uNmPOXibp0xllibvCo4oKdJvEmwyScXaFCiaggyy8/640?wx_fmt=png&from=appmsg)

通过态势感知上发现，在20：15分，攻击者通过167服务器访问97.107.137.164和39.106.248.18，下载了cart.tgz文件

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumMQynAwHW9bJia5IhtJOGtvhuMUaicTWdfW2zgONAQuNjZ73AFXVYBRyYDibJaSfaTNXWEEePorJDXaRO9viatSjhKy15ibonq5VKEM/640?wx_fmt=png&from=appmsg)

解压cart.tgz，得到了三个文件top、uptime、w，推测为命令替换+后门驻留

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumOk49P5uicdF1m9w91S2nqRUO1dNZRW4vCqia9qvKviaRkGWmkcibxuHpSax3Anw8gk0fsglZhb25QBMXCPsD22aexUfsYL6I3Ygxk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumN2sm8PLI9t4kgV1GHeGmvOtnvxJwQJgib3n6F8dJmuTKBYYGdCaZnjdYJeDxhgajX8kEVEPibAoeCbLLLpsdhwZYYjPQucn7Vns/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumNLdoC5bN5eCjpEpr7Ifa6hgKjwROWxvT45bh7TricqMZh0BvFfe0rS6aSY3x6xoH1TA59d88EeRwbScOficeuPicppDIvdVRMNQI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumNxqxjXLgdBPStFgn8GJpibsp2jjatJ9TiaOxdeGV6mERovv6Kb2YJiaPOT487v3SK3T6zicaS2wxfScKIrDbsyuQeAxeRPnRnmGn0/640?wx_fmt=png&from=appmsg)

通过态势感知分析在20：09分，攻击者通过167服务器访问39.106.248.18，下载了proxy2022.tgz文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumNSTvq5Pvwj4txFxPZicHvjzHZxRv6THXS2x1qL1qUfgoFn5Px2qUQibNDOC7nzZhPrPxdG3OVBGliac8zWajFYOlvntq4gpEVn64/640?wx_fmt=png&from=appmsg)

杀毒软件提示为bitcoin挖矿病毒

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumOiae5mmTL2Bo5u29ocHFMjiaDzTXv5ZkP0Pq9ILOgeRZvTMKWOneIUjBacjzpsLSEAGuRwiaQQVTIwic5XsvUvbFpNPRJyE3G86to/640?wx_fmt=png&from=appmsg)

分析为xmr门罗币的挖矿程序，钱包地址如下

"42tGCaozbTPj3rgikVBb8iEBem23cBnx6N1BhAcKZ2VLXMt5wAFSTKWTiL6dm356bnZxo2rwZcaGYYSoqURcZ1yU6vjKrsq",

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumPUVaZgYjj09C8T1g0pQ9Jpxd6icw3sLklkqevHt7lwNAw6QhXVy8WpX35s8W5QMCDhOUr4kiaezQFuN1IDN8ibwMrf7rtza96qf4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/JRTVZz6AumPMdbOsgzGpMTram6kiaQysDM3Zu1PuqR84nriaUQgwnyKCbWuFjsnVfOl5oHRF0jd7LZR6AANPticd9DSpPh3dFaL5qOSW2zbcBY/640?wx_fmt=png&from=appmsg)

同时在态势感知上也发现了存在挖矿的安全事件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumON51YJOSIpPiboExBQc9icm7WdrVPwPw24Judic1XoPEzVq14LyWmAKmv5sJ9jvlbaFH4uVibhSwJURsvoSYH8IiaFPjwcDRY5SnxE/640?wx_fmt=png&from=appmsg)

根据使用FRP代理工具的时间，去172.16.0.167服务器上查找相关的登录日志记录，发现在19:16:24时间发现了sc13003账号使用pwnkit提权工具进行提权的记录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JRTVZz6AumOGqHT3PibHhGqf6ZH7HnTHtiaxolvMMEEic54CzHSz48hrhvVvEbNMC7CkzykqB9NwN6Vj24H3JRJtPOiaqzF5eWgiaIAZcDxzl6ib8/640?wx_fmt=png&from=appmsg)

检索SC13003账号的所有登录日志，发现入侵时间在8月16日 19:15:40，随后在19：16分开始执行提权操作，入侵的IP为47.94.16.87，在19：27又重新登录sc13003账号，重新执行了提权的操作，19：27分获取到了ro...