---
title: Python趣味题--求bytes的压缩显示
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247486571&idx=1&sn=7d293cb40dfe79269aa3551714b68917&chksm=fab2cf54cdc54642aefba21933c904e5a77be7f6b06208b04e5ce5d33f2b3e61eaafa21c8c4b&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2023-04-01
fetch_date: 2025-10-04T11:22:40.960578
---

# Python趣味题--求bytes的压缩显示

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPMCibu03NE4BEeGZgHXB633J0ZbSEiciag3Cg2D6Jl1tdtIcTTqLiaPX2YibTNHHrhSMRDo3ibRQR8gYyIg/0?wx_fmt=jpeg)

# Python趣味题--求bytes的压缩显示

原创

沈沉舟

青衣十三楼飞花堂

```
https://scz.617.cn/python/202303311632.txt
```

出个Python小题，有兴趣的可以做一下，没啥技术难度，但坑点不少，心得比较细。

```
import hexdump
tmp=b'PK\3\4'+b'\0'*26+b'+(\xca\xcc+\xd1P\xf7H\xcd'+b'\xc9'*2+b'W\b\xcf/\xcaIQT\xd7\4\0PK\1\2'+b'\0'*6+b'\1'+b'\0'*9+b'\x17'+b'\0'*7+b'\v'+b'\0'*17+b'_'*2+b'main'+b'_'*2+b'.pyPK\5\6'+b'\0'*8+b'9'+b'\0'*3+b'5'+b'\0'*3
hexdump.hexdump(tmp)

00000000: 50 4B 03 04 00 00 00 00  00 00 00 00 00 00 00 00  PK..............
00000010: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 2B 28  ..............+(
00000020: CA CC 2B D1 50 F7 48 CD  C9 C9 57 08 CF 2F CA 49  ..+.P.H...W../.I
00000030: 51 54 D7 04 00 50 4B 01  02 00 00 00 00 00 00 01  QT...PK.........
00000040: 00 00 00 00 00 00 00 00  00 17 00 00 00 00 00 00  ................
00000050: 00 0B 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
00000060: 00 00 00 5F 5F 6D 61 69  6E 5F 5F 2E 70 79 50 4B  ...__main__.pyPK
00000070: 05 06 00 00 00 00 00 00  00 00 39 00 00 00 35 00  ..........9...5.
00000080: 00 00                                             ..
```

tmp数据如上，print(repr(tmp))看到的内容太占地方，请实现一个repr\_ex()，使得print(repr\_ex(tmp))看到的显示同tmp变量表达式。

```
>>> print(repr(tmp))
b'PK\x03\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00+(\xca\xcc+\xd1P\xf7H\xcd\xc9\xc9W\x08\xcf/\xcaIQT\xd7\x04\x00PK\x01\x02\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00__main__.pyPK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x009\x00\x00\x005\x00\x00\x00'

>>> print(repr_ex(tmp))
b'PK\3\4'+b'\0'*26+b'+(\xca\xcc+\xd1P\xf7H\xcd'+b'\xc9'*2+b'W\b\xcf/\xcaIQT\xd7\4\0PK\1\2'+b'\0'*6+b'\1'+b'\0'*9+b'\x17'+b'\0'*7+b'\v'+b'\0'*17+b'_'*2+b'main'+b'_'*2+b'.pyPK\5\6'+b'\0'*8+b'9'+b'\0'*3+b'5'+b'\0'*3

>>> hexdump.hexdump(eval(repr_ex(tmp)))
00000000: 50 4B 03 04 00 00 00 00  00 00 00 00 00 00 00 00  PK..............
00000010: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 2B 28  ..............+(
00000020: CA CC 2B D1 50 F7 48 CD  C9 C9 57 08 CF 2F CA 49  ..+.P.H...W../.I
00000030: 51 54 D7 04 00 50 4B 01  02 00 00 00 00 00 00 01  QT...PK.........
00000040: 00 00 00 00 00 00 00 00  00 17 00 00 00 00 00 00  ................
00000050: 00 0B 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
00000060: 00 00 00 5F 5F 6D 61 69  6E 5F 5F 2E 70 79 50 4B  ...__main__.pyPK
00000070: 05 06 00 00 00 00 00 00  00 00 39 00 00 00 35 00  ..........9...5.
00000080: 00 00                                             ..
```

之前懒得自实现repr\_ex()，想让ChatGPT帮写一个，未如愿。或许谁运气好，能让ChatGPT实现此需求，自实现亦可。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

青衣十三楼飞花堂

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

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