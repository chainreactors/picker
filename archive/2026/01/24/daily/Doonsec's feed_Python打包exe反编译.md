---
title: Python打包exe反编译
url: https://mp.weixin.qq.com/s/dYq6ppSQOkwxu1SwLMycwg
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:54:29.037534
---

# Python打包exe反编译

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLlmbfB7Z9UvjC5IyWwf2fSF3BcbAZLnV7rrFpibt69rTOsvWIKtoHYCA/0?wx_fmt=jpeg)

# Python打包exe反编译

原创

secureyang
secureyang

secureyang

![]()

在小说阅读器中沉浸阅读

Python打包exe反编译

# Python打包exe反编译

pyinstxtractor 是一个用于解包 使用了 pyinstaller 打包的 python 可执行程序的工具。

指令如下：

```
 python pyintxtractor.py xxx.exe
```

这个库文件下载地址如下：GitHub - extremecoders-re/pyinstxtractor: PyInstaller Extractor

使用图片如下：

![image-20260122205339801](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLJJ102kvaJOoEI8yvdMHHG4NYoIkrbRTFmOPPsVnYsdTVJrmHgI5LoA/640?wx_fmt=png&from=appmsg)

.pyc 是 python 的字节码文件

这个时候我们需要使用 uncompyle6 这个库，或者类似的工具将 .pyc 这样的文件反编译位可读的 python 源码

```
 pip install uncompyle6
```

![image-20260122205636148](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtL5icXnAsLUwIKSrl7Xsu7TJH4rmqdDXTtxJ3312tN9BmgebBhgb0YicDg/640?wx_fmt=png&from=appmsg)

使用方法

```
 uncompyle6 xxx.pyc > xxx.py
```

![image-20260122205934560](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLauUAz76vibwo19k1oyRx2IQpwWOPgdCDZpyWwibkAgFibwlSibLCicIVFyQ/640?wx_fmt=png&from=appmsg)

![image-20260122210436809](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLqPqfI4c6lzSX9GUrQshwa2zup2Sp9N1rnD7ArHsDuwAb2icnDibNgNXA/640?wx_fmt=png&from=appmsg)

我们可以看到，cmd里面说了 Can't uncompile shellcode\_64.pyc

这个原因是 uncompyle6 现在属于半停更状态，只支持到 python  3.8  的状态

注意：python 3.8 版本及以下开发的 exe，就可以使用上述办法。

对于我们这种高版本的怎么办呢？我们需要更换更好、更新、更适配的工具，如下：pycdc

在线Python pyc文件编译与反编译

不用自己下了，在线即可使用，而且这个在线还支持 uncompyle6 的库使用，很方便。

![image-20260123135416591](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLtZpM1JvjKGw9vOYf7dtyg1unKQzyxILbVqzz1EpQU2U4uhEIVaibuXw/640?wx_fmt=png&from=appmsg)

直接把文件拖进去就好。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoQW0gRe2T7PcibUQdxRXlZ9gUmhnDnCnZH1QV9ickJOicpYfupCNqRefT4xquSPPTcAIhDibeicp4aL8ZQ/0?wx_fmt=png)

secureyang

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoQW0gRe2T7PcibUQdxRXlZ9gUmhnDnCnZH1QV9ickJOicpYfupCNqRefT4xquSPPTcAIhDibeicp4aL8ZQ/0?wx_fmt=png)

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