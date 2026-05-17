---
title: Pwn2Own Berlin 2026第三天：百万美元奖金池即将突破
url: https://mp.weixin.qq.com/s/qsa887R8D7ppJvKRzYI4JQ
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:43:20.865765
---

# Pwn2Own Berlin 2026第三天：百万美元奖金池即将突破

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibdAibXcRZH4yHLpSicZ2sLX0G2CapyEiam53ynO3kpvVjicuGBABuHuxAPhA7Re3gscMicRHhqwYrsEO9E4iaCD03YtNVonxsPlc6dPo/0?wx_fmt=jpeg)

# Pwn2Own Berlin 2026第三天：百万美元奖金池即将突破

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> Pwn2Own Berlin 2026最后一天比赛结束，三天累计颁发奖金$908,750，覆盖39个独特零日漏洞。Viettel、Ikotas Labs等战队继续扩大战果，但Summoning Team在VMware ESXi攻击中失利。百万美元大关近在咫尺。

## 最后一天开战：积分榜与目标

Pwn2Own Berlin 2026进入第三个比赛日，也是最后一天。前两天已经见证了相当激烈的攻防对抗，39个零日漏洞总共换来了$908,750的奖金。今天的目标清单上还有SharePoint和ESXi，突破百万美元几乎没什么悬念。这是今天的Master of Pwn积分榜：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibefbibfRDTFPFRE3lhNMJ2tdMFS3wsernIdMTGrQpdjtzPurvkZXvPGOfyAFs9zjj1Tuvfj6uxHyYudYodcibzZXgX8THTia1Yob0/640?wx_fmt=png&from=appmsg)

## 第三天战况一览

先看Red Hat Linux的挑战。Summoning Team的Sina Kheirkhah用了两个漏洞，但其中一个之前已经被报过了。这种碰撞情况按规定只能拿到部分奖金——$7,000和1.5个Master of Pwn积分。说实话有点可惜，如果两个都是新洞，回报会高不少。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibfsia7zQTwWrACNibibVicKz2qfMCyRbQvAeYeu2zjfxTJwibVYHSLnUibfG2KZBFv50ib5Wubuap6BLlWucvvV31UaGvFVWEUibHCUMTA/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeRDpGichMW0BHC47I6fQqOa3pry02d2CYuTfcoNIECg56vgYJSXUIIQ6DFp2uN6WGcnH9AR4rHfswcVQ6IAaUPSicAHGId0kExA/640?wx_fmt=webp&from=appmsg)

## Viettel与Ikotas的连胜

Viettel Cyber Security今天继续刷存在感。Le Tran Hai Tung、dungnm和hieuvd三人组合用一个整数溢出漏洞拿下了Windows 11的提权。这是他们第五轮成功利用了，又入账$7,500加3个积分。这队今年的状态确实稳。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibfREkgjWXYiaqE4KtHV5kiaMdibxtV8nic0m8xmL6cs4dia6zeg6ycfeGRBTicVzSvVEuf02BHR6fk3dJ9Lfxo4GiceeZ7xLViaqVeNSfA/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibc9OEIvnqlZDPBDXcgj3L7bcFqpyOLRykIHG9ictPOwCzLsBI5eB61Ms6Z5CAndWVicP0bguLtU8iapo1VEYRF7ZtEBHWNgZPibANA/640?wx_fmt=webp&from=appmsg)

另一边的AI攻击类别也有收获。Ikotas Labs的Satoki Tsuji利用外部控制漏洞搞定了OpenAI Codex，弹出了一堆计算器。这一下值$20,000和4个积分。AI类目标的奖金一向给得大方，Satoki这次选的目标也够刁钻。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibfpAPWia6mH6MubyfqHzgenM567wdnke4bibjibbhjH0d8ia0os1RCgNibIvcfjotp5xDT0z1PD0srWj6YEfM8ibJiaRHibo9xGKpfKwbY/640?wx_fmt=webp&from=appmsg)

## ESXi攻击失利

不过不是所有人都顺利收工。Summoning Team的Giuseppe Calì在VMware ESXi的攻击上没能在规定时间内完成利用，最终被判失败。ESXi一直是Pwn2Own的硬骨头，每年都有人栽在上面。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibdPf6PLlZhNXswnekZdN3bZZz0HgdAwkOmKiaJelYZ9uWAalvaEMvEF2mmAia2yEz23icqO6D8A7WoOpIW3ZRmKHWaTVhU6nvCicRk/640?wx_fmt=webp&from=appmsg)

## 一些看法

三天下来，39个零日漏洞被当场演示并提交，这数字放在任何一届Pwn2Own都算高的。Windows、Linux、ESXi、AI——覆盖面很广，攻击手法也从整数溢出到外部控制五花八门。百万美元的门槛大概率在SharePoint或ESXi环节就破了。Viettel今年势头很猛，五次成功利用不是白给的。而ESXi的这次失败也提醒大家，虚拟化平台的安全壁垒依然厚实，不是随便能撬动的。

---

### 参考资料

[1] https://www.zerodayinitiative.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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