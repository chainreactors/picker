---
title: 内存取证练习7
url: https://mp.weixin.qq.com/s/zvVbpuoUbsib7NBf_FQhxQ
source: Doonsec's feed
date: 2026-10-11
fetch_date: 2026-10-12T08:12:55.120645
---

# 内存取证练习7

# 内存取证练习7

原创

内存余响
内存余响

内存余响

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#

挑战描述 我们公司的一个客户由于未知错误而失去了对其系统的访问权限。据说他是一位非常受欢迎的“环保”活动家。作为调查的一部分，他告诉我们，他常用的应用程序是浏览器、密码管理器等。我们希望你能深入挖掘这个记忆转储，找到他的重要东西并还给我们。 注意：此挑战由 3 个flag组成。

题目附件在上一个内存取证练习6

首先我们看这个题目，“环保”可能和环境有关，浏览器历史记录和密码应该关注一下

# flag1

首先看一下操作系统信息

vol.py -f MemoryDump\_Lab2.raw imageinfo

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib98W9JmJPbkcZR9wD4fJYuTVkicr9GXyDHlLibibymIbuf8kPyfUStgpJcViaPcOa2B3yA5NkPM7KNOqOw5AxnWmpymARMias2DZDEc/640?wx_fmt=png)

查看环境变量

vol.py -f MemoryDump\_Lab2.raw --profile=Win7SP1x64 envars

一开始没有看见，感觉眼睛要看瞎了，还好后面看见了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib98XsG1picvm9QWtENfLLo4CFzjEdnWFqVka2HKnzeibUNExBcLPSEgoYyUV67ibsmkzE7exy2ibYcrjxvXDftibg6zKkSEcs5icLLQo/640?wx_fmt=png)

解码base64

echo "ZmxhZ3t3M2xjMG0zX1QwXyRUNGczXyFfT2ZfTDRCXzJ9" |base64 -d

得到第一个flag

# flag2

查看浏览器历史记录

vol.py -f MemoryDump\_Lab2.raw --profile=Win7SP1x64 iehistory

发现一些要值得注意的，有一个Important.rar，SW1wb3J0YW50.rar，stAg3\_5.txt，Password.png，Hidden.kdbx

文件查找一下看看在哪里

vol.py -f MemoryDump\_Lab2.raw --profile=Win7SP1x64 filescan |grep -iE "Password.png"

找到了这个图片，其没有

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibibWzSNJiccPflKgSfUVl4u9QVUx0YYPQpjCPjHK3WQrkzuPIM2Y1k2ZEfnpX0cey3xrC81lPOW570bRrreBVqAsVxuORrRaicwWA/640?wx_fmt=png)

把这个图片下载下来

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibibcHcymeosyvm6UddAia6FeyHlIpicqHwAeImMjYAgL9eqXSkiaFLGpwKxoRJ1UnsPhcbamsxNyPicsxpmguI3Qw0BLyyrm0cic3eyw/640?wx_fmt=png)

发现密码P4SSw0rd\_123

还有Hidden.kdbx这个也下载下来看看，但是这个后缀我还没有见过，我还不知道这是什么东西

查阅资料之后知道这个是一个由 KeePass 密码管理器创建的加密数据库文件，需要密码才可以打开，之前我们已经得到密码了

这里我们需要在kali下载keepassxc这个工具，安装好了之后打开Hidden.kdbx这个数据库输入我们刚刚得到的密码就可以（要先把dumpfiles之后得到的文件重命名）

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib8WmvYicW6gcasOoeTpwBgZ6qiaBcbG0O2bL5ibs15XyU2yvb29qQ1wiaYdW873xdLvLW6yfUKWcTrG0ahBAKPcwLQnbB7DDOIfU4Q/640?wx_fmt=png)

flag{w0w\_th1s\_1s\_Th3\_SeC0nD\_ST4g3\_!!}

# flag3

查看历史命令，发现除了ie浏览器还用过chrome浏览器

同样的查看chrome浏览器历史，这里需要自己插入插件

vol.py -f MemoryDump\_Lab2.raw --profile=Win7SP1x64 chromehistory

找到一个网盘地址

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibickABRibMmCeX5LPNDvFhfZibSFsorbS3HRmFR4vk5fWFrtic19pqhwVFwTOcQorbZ4CUylgBs9OlI7FZMibO4GJKlfnGJtqvkk5ac/640?wx_fmt=png)

打开发现了Important.rar，需要密码，提示memlabs第三部分flag的hash值且为小写

Lab-1第三阶段Flag为：flag{w3ll\_3rd\_stage\_was\_easy}，对其加密为SHA1，密码为：6045dd90029719a039fd2d2ebcca718439dd100a

打开得到flag3

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib9K1e8sER4Sib2PbrPK5OWThPZQPR8UjBdrW6XeJOb4SXDmK3AtxhzHMoS4Oms0tQBvw3E2tmD6vtOJ2wicEJavy6PyBcibvdYrIc/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic4YfldibtqMVhOo0ez7bhNzzvcKGfFIlhFKFvlSN3VmFvNUVyibvMYJP3SR60w6t9GFkzGY4yrGNrvk2DZYQ5lbJQppuHpG1VfI/0?wx_fmt=png)

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