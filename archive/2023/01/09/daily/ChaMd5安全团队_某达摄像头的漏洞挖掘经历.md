---
title: 某达摄像头的漏洞挖掘经历
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247508121&idx=1&sn=e34f59e53a1394600c7e768fcbf237f9&chksm=e89d8841dfea0157a63c1a15213306739f936f3b63aa8e32ae6657a87934aec82d60bfe046b8&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2023-01-09
fetch_date: 2025-10-04T03:21:42.986337
---

# 某达摄像头的漏洞挖掘经历

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PUubqXlrzBSxh0gLKLFeREib4duudlNgEQltqza3GxoMTrHgDibgTfekYZIvnMtp7emCjkWGZW6GTqrkIHXQkKAw/0?wx_fmt=jpeg)

# 某达摄像头的漏洞挖掘经历

原创

狒猩橙

ChaMd5安全团队

### 前言

在看了一位师傅的关于摄像头的文章之后，我也心血来潮找了一款摄像头（某达最新款CP7）固件去挖一下练练手。

### 串口获取shell

拿到摄像头拆下来之后尝试了一波串口获取`shell`。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBSxh0gLKLFeREib4duudlNgEqaJd6BwNV6IcQws9G7fvlicePgJK0elOHodnn1tX6zTv3Da1IJ4ugbA/640?wx_fmt=png)

image-20230103171820881

但是连上之后发现这个摄像头貌似无法获得一个正常的`shell`，只能用来看回显信息。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBSxh0gLKLFeREib4duudlNgE1nrGCyBdMwyLLlawjkx8uiaml1iaz0z5ygvzLZA6w5ugouZzjUkbA5jQ/640?wx_fmt=png)

image-20230103171820881

### 分析

用`IDA`打开摄像头相关程序之后，可以发现和那位师傅分析的固件大同小异。那么，如果我们想要挖掘新的漏洞的话也只能从不同的角度去进行挖掘了。之前那个师傅找到的是某个类似于后门的命令执行漏洞。那么我们再去找看看能不能发现一些其他的漏洞点。

首先还是绑定并监听1300端口。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBSxh0gLKLFeREib4duudlNgEDskibHFvcRR267HibR2LQ0fJu49IGWf3C1iau7AoGK5Hic1tkADxyBDNbw/640?wx_fmt=png)

image-20230103171820881

然后等待用户连接1300端口。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBSxh0gLKLFeREib4duudlNgEZeEOj4o5sekPbfS8erEfx8OA1YUelCNHX0SOnawWBT2J57cNDn3seQ/640?wx_fmt=png)

image-20230103171820881

之后获取用户端传入的内容。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBSxh0gLKLFeREib4duudlNgEiaw0wGKlLWZtRCbwwlqCwDxyQicnle9lfO5faxxjZKiakFHoLpGJAH8UA/640?wx_fmt=png)

image-20230103171820881

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBSxh0gLKLFeREib4duudlNgEt2qAJpJ1pSOzPicBZKemBric7CNbUmjavLr4f0j5BYzM0giaagpHD8ibLQ/640?wx_fmt=png)

image-20230103171820881

接下来会对用户的输入进行判断，并进行相应的处理。偶然发现了一个和那位师傅提出的不一样的命令执行触发点。如果匹配到的是`SYSTEMEX`这个标签，那么会进入`sub_14404`函数。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBSxh0gLKLFeREib4duudlNgE2TYXaibxHJ2W3n1LicYJoYMMCgafV93egePJlWibLazoIEKStM9oyic0lQ/640?wx_fmt=png)

image-20230103171820881

这个函数中，会把所包含的字符串传入`sub_16E04`函数中进行操作，而这个函数里有关于`popen`的操作，因此可以达到一个命令执行。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBSxh0gLKLFeREib4duudlNgEQSeNmXgeSq64C8ZJEkhanVtQSU88l0MU7uy3PMlYTKgicEqN9ZibiaricQ/640?wx_fmt=png)

image-20230103171820881

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBSxh0gLKLFeREib4duudlNgEibLZOI2lXf1qPeOojTusFibSjd3O5dVclVZPGu7LzzcReiaZkKWL9G0ww/640?wx_fmt=png)

image-20230103171820881

`exp`这里就不贴了，感兴趣的师傅可以自行尝试。

### 总结

算是在大师傅后面捡了个漏，`IOT`的一些设备依旧不是很严谨，只要认真挖挖还是能找到一些漏洞的。

招新小广告

ChaMd5 Venom 招收大佬入圈

新成立组IOT+工控+样本分析 长期招新

欢迎联系admin@chamd5.org

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBR8nk7RR7HefBINILy4PClwoEMzGCJovye9KIsEjCKwxlqcSFsGJSv3OtYIjmKpXzVyfzlqSicWwxQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

ChaMd5安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBRyftF8Oqhh2V8ib6wEgOiaCMdKBLfkLlHAvKibMgjerLzeXXxRmyI9VpjX7e37vjeW2scODia9KHGoqQ/0?wx_fmt=png)

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