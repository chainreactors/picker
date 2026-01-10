---
title: 某赛通Nday漏洞分析
url: https://mp.weixin.qq.com/s/CiMdkibcYiyYrQ5P_dCBPQ
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:21:46.288240
---

# 某赛通Nday漏洞分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQI08eGPd8SgicibvicicOCbcxbxM5NZsMMFX1t3tRpdkbJyKlSWV5UWO2AKQ/0?wx_fmt=jpeg)

# 某赛通Nday漏洞分析

原创

redcat

虹猫少侠的江湖路

![]()

在小说阅读器中沉浸阅读

免责声明

![图片](https://mmbiz.qpic.cn/mmbiz_gif/QtaE6uFmibPlPBODMGcLpNt9QBAWypThbpd3jzvdXXROdjXCddIaUR6icvQfhjUVDAXNPbM4SuibSU8GwCr9t5VvA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

由于传播、利用本公众号虹猫少侠的江湖路所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号虹猫少侠的江湖路及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，会立即删除并致歉。

最近没项目闲的有点蛋疼，看到某公众号发了关于某安全文档系统的前台任意文件上传漏洞，并且明确标注了受影响的版本号，该系统在攻防中内外网还是存在一定占比的，于是打算分析下exp备用。

直接下载对应的两个版本源码进行对比，整个过程比较简单：

过程：

下载Beyond Compare 对比工具进行差异对比：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQIo0Tw9G60jLmTgsLxr2kXEWIicibF5mTnDxWtxpElD1kHAFc4CSKsiaA1Q/640?wx_fmt=png&from=appmsg)

该工具默认不会反编译class文件的，需要下载对应的插件，直接询问ai：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQIiaU6XLjTODyF7AD48DxvvicG2yYjIUTSZHJ5tv8R6WkpSBfBgvcwSz2Q/640?wx_fmt=png&from=appmsg)

安装这个插件之后就可以正常查看class文件了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQIDrwCRbysiajO8jRyLOrj4RAl8rv6Ld4HTGUPLfS4PoTj2Rt3dxAXXZA/640?wx_fmt=png&from=appmsg)

看到某方法中增加了一个baseDir的代码，猜测大概率就是禁止往上跨目录的修复，并且这个方法后续还有文件操作，所以大概率就是这里了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQIUMibPld8gCrVxUZz1HZ185wkBgZWKjRa5ictseKrNbufibHNvLfH6coYw/640?wx_fmt=png&from=appmsg)

然后用idea看了下这个控制器的方法，这里就是存在跨目录的任意文件上传操作，后续就是过一些验证了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQITPmwBzFrn1r9XpdvZTsvS9PTl31d8PS5GVTvMl32EibTTJPGdRLgjzQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQIYEC2Qpg99s11vJphVIs9IwNugX3RNRnvxxLZSAUSibmEicicjtATAtRAw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQIicHEYicLTk5cQbpGtgXZic4rNFosZnsWAiaSvrBkbbKdG5CQG3V85Nl9sw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQICAibJjJ9H6yibNSFd83KbEkM0XmBaiaGykia2LYKBztzG4mgF9rdfiaYVrA/640?wx_fmt=png&from=appmsg)

本地没有下载链接sqlite数据库的工具，这里直接让ai搞：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQI4CrGHn2XUFBcWT80ib7ZANXXWicVWF53SxTGO2F7c0l4Pcp4RRVzorWw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQIczOhCicDL1DcmvwWMhjGhQoTUe2E9C33GgJaLdq3JictcicsPkiaGJ8jxw/640?wx_fmt=png&from=appmsg)

最后也是成功的复现了某通告中的内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdOhOibZl9YveMiaqyz987ibQIB0cYoabMbCb3xxSpcuVqymfQw0Wl5TRchr0EQCpfVf6iaxkv3IAibkIg/640?wx_fmt=png&from=appmsg)

提示：这漏洞不是默认的对外的web端口上的应用，同时这个数据库中的密码也是有一部分系统搭建之后改了的，所以影响一般，在内网遇到或许可以试试，漏洞的特征倒是不明显，没有../../ 这类敏感字符。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdwr9lsEibiaSjx6GEN71DGObNlYS0pAKWWWj7fxjhiaIdsUWL1X8n7ZNZibibguCGb0jdD8vAKjia6IpBg/0?wx_fmt=png)

虹猫少侠的江湖路

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/RzCEZQRRgcdwr9lsEibiaSjx6GEN71DGObNlYS0pAKWWWj7fxjhiaIdsUWL1X8n7ZNZibibguCGb0jdD8vAKjia6IpBg/0?wx_fmt=png)

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