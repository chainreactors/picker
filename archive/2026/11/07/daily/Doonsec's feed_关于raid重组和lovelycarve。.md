---
title: 关于raid重组和lovelycarve。
url: https://mp.weixin.qq.com/s/4vPArcSc-U3N6Hhrv0bD5w
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:08:34.060340
---

# 关于raid重组和lovelycarve。

# 关于raid重组和lovelycarve。

老皮的碎碎念念

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

起因是同事做了一套四川大数据的题，说看不太懂raid5重组，降级这个事，我说这个不简单吗，重组下然后挂载这种不是轻车熟路吗，然后就翻车，现在回顾一下翻车过程。

有佬已经写好了用lovelycarve的过程，我是懒得在这个电脑上再下载安装了，熟练打开火眼的raid重组工具。呃，没想到升级了。

![](https://mmbiz.qpic.cn/mmbiz_png/SVAhggk0wbyyZibK17w0L7kar4YupYwFAqxsPAUhtYnVPZ3JohUX4ibkRzq0R36EkdmQFbknERIibMpDKa7iaFB5XgtYcjnDzWReOe2uyzWCWH4/640?wx_fmt=png&from=appmsg)

查询 ，左同步，1024扇区，ok，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbyjM1kVTPPMDECxBBAe1Fzdz4z8TibziaHUjR0MGqrqrRTjOkic7FvUSV5G9K8DeGo4eB21ibum0MibduPEQeb21kYFiaZ8l1b3EVJOo/640?wx_fmt=png&from=appmsg)

重组，这里有个坑让我踩上了，所有后面一系列的事从这里开始了。

去仿真，发现，这里可以直接挂raid镜像。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbz6efL6upqRtQqficQ676FZDewcoJKyJk6j0p1m2iaicj70WKoU0oFUZTKbqrkAgibcqpkjZpictTqEa95dFCEpLdhHDwwlJNvgkcg8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbxm6ibeqSHjmt4Ee0hJgrYd5vfJuicLWKa9ED6wib714BZ3gXMnV7ibNNcILPoOJRAjFH8qHeKd9pibXQNRcvfyoZpQM8Pyds48mOws/640?wx_fmt=png&from=appmsg)

于是把三块盘挂上raid5，启动，进去挂载，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbxZRr9K9pWNWJ9DbFQ591x9WSUVFtRkQMAgncicDOiboSLsOQhx1PTjCLkf0icXaDfXrsiaMFd2pDIa7NrYlrNqazXdcJ8FsFTZdWI/640?wx_fmt=png&from=appmsg)

？？？？

把重组生成的文件做为从盘挂载，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbyWluNSiaPTHUW2b6Wib1tfhCB1JWYsj5KfZDKEMdTGZzrUkBkib634QpqTVeTicKm7mzLfeFsZMiaUvDDxJyAw37GBJS9gDP4MTozA/640?wx_fmt=png&from=appmsg)

依然如故。

![](https://mmbiz.qpic.cn/mmbiz_png/SVAhggk0wbz7q9DqWJP31IkgibvlNJCWZe6qXlnEb6c0icGxZ2y1sD6Wjqndw9Djic8TvyXXib3iaSHFPMMdlyk9CjIyyFhMQ4PnHJTW5EfiaQIVk/640?wx_fmt=png&from=appmsg)

改用ufs，一样

![](https://mmbiz.qpic.cn/mmbiz_png/SVAhggk0wby64t1w9orsAtT62JwdvK04NYT62yO8bia6YpawkO9r2OtdvXniaOysHwRju8N36NNicPCcgGI6DnCUtMFOuX9ibEICoYtBDBibDZYE/640?wx_fmt=png&from=appmsg)

改用rstudio ，一样

真是sun dog！

![](https://mmbiz.qpic.cn/mmbiz_png/SVAhggk0wbyvZ2UpdR58eMIqrZmLgLUgUcVWNzHdZouDF3qwLKJibOTGPDyJZxHoCdQPfLTKHv0tT9SfYwXv7sCR63C2CMq8tS2oiaxicK15KQ/640?wx_fmt=png&from=appmsg)

忘了说一句，以上产生的镜像，用xway和7z都是能正常打开看见文件的，火眼也能正常分析。

![](https://mmbiz.qpic.cn/mmbiz_png/SVAhggk0wbwlspRugR4B8MulbWQYiaTuvm3rMTjx6ibj0A98D2HicAJhJJ1WyJ3bMoSYkGWcanFyrOXYTEmDsXH6S7fxKLMDibb7xGuUSPKgw14/640?wx_fmt=png&from=appmsg)

没奈何，我老实下载了lovelycarve，导出镜像挂载，一次成功，

![](https://mmbiz.qpic.cn/mmbiz_png/SVAhggk0wbwHOJrzicVPftqDyIC0sMNU0SB2lFvuTdyyFia9oxc8FEut7LNyIE01maJRuv1jX5WV8ia8KJccU5rpgYjFLIJVp0BjPILiabtrXOA/640?wx_fmt=png&from=appmsg)

我不禁陷入了沉思。

根据早起王大佬的建议，我把几个镜像丢给trae分析。跑了20分钟后。

给出了如下结论：

## 三个镜像表现不同的原因

1. `.dd` （lovelycar生成）（唯一成功） ：无 MBR，ext4 超级块位于绝对偏移 1024，属于“整盘即文件系统”的布局，`mount -o loop` 直接按 ext4 识别；且文件长度与超级块声明的块数完全吻合，所有工具的大小/边界校验都能通过。

2. `5.dsk` （ufs8.7生成）：数据 100% 正确，但生成它的软件把阵列容量算小了——每块盘少算 512KB（3 块合计正好 1.5MB / 3,072 扇区 / 384 个 4K 块），而数据本身并没有跳过这段偏移。结果就是：ext4 说自己有 784,128 块，文件只提供了 783,744 块， 文件系统比“设备”大 。凡是校验设备大小的挂载器/虚拟机都会拒绝（提示容量不符、无法识别等）；即使挂上，末尾 384 块也落在文件之外（这部分恰好全为 0）。注意这也是它与其他两份的唯一实质差异，所以“5.dsk 挂不了”不是数据结构问题。

3. `virt-mdadm-localhost.vmdk` （rstudio生成）：R-Studio 输出时把整个阵列当成一个“分区卷”来处理，自动在 LBA0 写入合成 MBR，把阵列放在 1 号扇区： - 分区起点 LBA=1（不是 0/2048，属于非对齐起点），类型标成`0x07 = NTFS` ，而里面实际是 ext4；   - 于是整盘挂载时在 1024 处看到的不是 ext4 超级块（超级块被推到 1536），识别失败；   - 按分区挂载时，Windows/自动挂载器看到类型 07 会按 NTFS 去解析，也失败；Linux 需显式`mount -t ext4` 挂`/dev/xxx1` 。

？？？只有lovelycarve算对大小了？

那么，我深深信任的火眼又是咋回事呢，我又拿火眼的raid工具再次进行了一次操作，这时候，我发现了一个问题！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SVAhggk0wbz3yl5icyQKqnshB9Vvsx0CyGTiciaxsj0nqS2jh1O9nRqFuUDsX0ZLhcr1ev6v9yko5BKuPKoEbYciaNW0OaarvW7g0YyqBLn1GWU/640?wx_fmt=png&from=appmsg)

条带大小，不是查询出来的数值，也就是说拖入镜像后参数没有自动生成，而以前的版本是自动生成的！

重新按照查询的数据生成镜像后加载成功！

推荐完lovelycarve（工具库又多一个必备工具）后，照例PUA一下春哥，让他改！![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_05.png)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EsNNx0KLiawZLgs5PZVjW3EsyTjiafk5PickpBNicuMRqgDjnPdYNwfQ0duxXZJs9FNYeD4jX506YtCD09pBEoK9ibQ/0?wx_fmt=png)

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