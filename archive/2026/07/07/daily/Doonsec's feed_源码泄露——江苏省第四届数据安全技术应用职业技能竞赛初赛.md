---
title: 源码泄露——江苏省第四届数据安全技术应用职业技能竞赛初赛
url: https://mp.weixin.qq.com/s/ZJxc9u4hoR13JhlN8sRAAw
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T04:59:37.217826
---

# 源码泄露——江苏省第四届数据安全技术应用职业技能竞赛初赛

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RJrNBTwulvcee2kjc4eWzVqrR9jHnT7ia8JGV0tLt6HkZxBzH90ze46libiadjHzh6j4vyf17icNhgic2Bl9CPeXHBoL5vYaENHMk3vgnEj0ib44o/0?wx_fmt=jpeg)

# 源码泄露——江苏省第四届数据安全技术应用职业技能竞赛初赛

原创

一只岸上的鱼
一只岸上的鱼

一只岸上的鱼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 源码泄露——江苏省第四届数据安全技术应用职业技能竞赛初赛

## 缘起

什么叫屡战屡败？ 就是这次又没进决赛……

什么叫屡败屡战？ 就是下次还参加……

只要每次能学点东西。

咱号称程序员，源码泄露题应该最简单吧，今天先来个简单的。

## 题干

见下图，一共三问，第二问最简单 还是先来第二问吧：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvfZgTN0Y60yyprBN2SYMaIlvRgOvAgwmia9D9bLO2uaBtMYefLLDj32vrkiceO10VpyD0yA2vULbTO2IyhicXMd6xibTqg85qTdrib4/640?wx_fmt=png&from=appmsg)

先来看看附件：

附件解压后是2个压缩文件，一个zip，一个gz，那还是放在kali里面处理好了:

全部解压成2个文件夹：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvdRVkNMQ11j97mv9N5LFyKEA3NYfbzmIu7mBC13DRgnI7JtkJCFxR56NXVlSzvpxDpV3IWiagaLL90f5eL1wNdaEwNdNxKuVEhA/640?wx_fmt=png&from=appmsg)

解压后看看文件：

```
bash

tar -xvf repo_server_snapshot.tar.gz -C repo
unzip leaked_repo_sample.zip

# 看看文件目录
tree -L 3
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvdDibRb9wyUsUyXuwdFVTvSb3Lnj5iaGE5jltvKyk8sDibWZGTDebHGibH7CznhWYMCErPcp69D4oxm4LmIQ5ugrIDXxibj0PQibWaibk/640?wx_fmt=png&from=appmsg)

有个git仓库，进去看看，居然发现日志只有5条，现在知道为什么说他最简单了吧？因为每题可以提交10次答案，直接提交，第三次就对了：

```
code

2561d4af185e4e4d1dc1af4f6deedece003ffa6e
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvcolUW5JA7yhPicqyWwYCbmgR3KVy4n1Jpb2eKZRdj8dl5Hc6icfWpxXFC33zUnI0DnXVIAFnQfPySRxkq5qgCPLCtQ62EVwWgm4/640?wx_fmt=png&from=appmsg)

当然，这是投机取巧的做法，实际并不会每次都这样，正统的解法是这样的：

leaked\_repo\_sample.zip 是源码文件，应该从git中回复每个日志版本，然后比对文件，一样的那个日志就是答案：

```
bash

mv citizen-service-api.git .git

git --work-tree=./ checkout -b r1 2561d4af185e4e4d1dc1af4f6deedece003ffa6e
```

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvfLCp9ZToGGBWUXxGSAbVxl0uqBwRtJ3xuoVf5EM1bM5LmqwFpdBsC51YWUkhmhkrVNsv1iaKYwYxuhSSUNvgVULrIrZItAfx9M/640?wx_fmt=png&from=appmsg)

## 第一问：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvf6utcMK11zXythNuwhQQXgR925cgLf21sTfqHQCkEJWBZyjHwqicxKPZFaF1FDcq1pk3mSfjyoEaVJCfWwvepzibg7e4o4lkezw/640?wx_fmt=png&from=appmsg)

什么叫异常？没说，那就是长的和别人不一样叫异常，看看log文件吧：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulveATR8Qic7oNCJvmLE2ibJicfbJsSkUT7wdUFZGzFibUeNP7gyuKbGc4SygiaticxOuddrs8BZsN2pp6cOClkm2TaTs1hGDk2rpgvfng/640?wx_fmt=png&from=appmsg)

只有一条是“interactive\_fetch”，那就是他了，记住他的进程id：ssh\_pid=1217

再去auth.log看看：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulveATR8Qic7oNCJvmLE2ibJicfbJsSkUT7wdUFZGzFibUeNP7gyuKbGc4SygiaticxOuddrs8BZsN2pp6cOClkm2TaTs1hGDk2rpgvfng/640?wx_fmt=png&from=appmsg)

找到前缀：key\_fp\_prefix

那就再去ssh key文件里面看看，计算一下：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvdOkpRaIJIfPvAc3aXPYTKyPQvuB9Rn5aCnf0lC8amJyYVBFXYFLWAHXHu1Hny77ROoXSYD0ic2q7CUhS0K0ibRwQdYMFJFWg19o/640?wx_fmt=png&from=appmsg)

对比前缀，就找到答案了：

```
code

SHA256:s1BnYrBJr15crIh48E/6UHuJKM2ZEARymspEhTjaQhU
```

用到的命令：

```
bash

tail git-shell.log
cat auth.log

ssh-keygen -lf ./authorized_keys
```

## 第三问：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulveic6UEZeXUlEQzQDJz1ibSHIEeqNv4bWKsgdTQMZwA4wwr5jnoa5WLOh3seH7mlmBLqKLTNwYx2K3ncbW17mQULNINCXKWlVtlc/640?wx_fmt=png&from=appmsg)

这题很明显解出来了，但是答案一直不对，不知道怎么回事，记录一下解题过程：

这个文件是个块备份文件：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvf5Sr6YmrLMgmm1ia5Q0TWcFVQ8IqkyLJOGCtfb684O8N1UKIZPiaJbbxscSd1Vuj363ml9rclbXXuNHelabGEJrzibcpYmCNSnlU/640?wx_fmt=png&from=appmsg)

是可以直接用binwalk分离的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvfW9H0bXV2oocODDUfuljAssMqUMaWZyeKg2IQUrFQE4xdvYzohSVJoojXc3oZvAj6pOJcJnKlMpj8MnATFhJWCoSg5Ahfcv3E/640?wx_fmt=png&from=appmsg)

分离的文件也是正常的，可以解压：

![](https://mmbiz.qpic.cn/mmbiz_png/RJrNBTwulvc7FIQGpU1NF1RHOIcdOxoECqLicicVOAtwPfsUOb5kWrHliaxlzibZLAoBxFPPJCAoWibDUdgJbtAepA6gJ9Kvvt82rw5upNPJ8wTo/640?wx_fmt=png&from=appmsg)

一共就4个文件，都不用继续处理，都试一次好了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulvcEibhUvb5qYhJI13Yf3NHXKeKVwejIibztc4F8n2WjIZFoCgoXeG5ZIicwF9rUnI6n3rGtKIYaViahuu1R7Wcw5icG2qxzHj0Cj1aA/640?wx_fmt=png&from=appmsg)

都不对！奇了怪了！

用到的脚本：

```
bash

file deleted_blocks/block_0017.bin

binwalk deleted_blocks/block_0017.bin

binwalk -e block_0017.bin --run-as=root

sha256sum 4BC
```

但是发现分离的文件都一样大，偷偷问了AI，说是binwalk和dd都是默认的贪婪模式：保守提取至文件尾，因为gz有校验，解压至文件结尾结束，所以正常解压不会报错，想要精确的得到文件，可以使用dd分离，并且控制大小：

```
bash

dd if=./block_0017.bin of=gz_11.gz bs=1 skip=1212 count=$((3370-1212))
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RJrNBTwulveGBFe9DseyCamJpl3tdmrPKBokgWtjrtwnoJ5QPDQUKZ4cQiafI4m2C9JcdZA79Iia9RpDcdGEC1D7pW3tBDxdo4h34QfUB0D5Q/640?wx_fmt=png&from=appmsg)

就是使用count来控制大小，大小从binwalk读出的分离计算。

但是，没办法去验证是否正确了。

## 小结

这题算是对我来说，最简单的了，可惜，第三问还是没得分……

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ZG8Fru1tL1whh58JUwn0GLYzvqhGcECfmoW1O5J0JY0h7tksUWibmqwhwmEkL7kf1TTb37avJialEYsc7GfDhBCw/0?wx_fmt=png)

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