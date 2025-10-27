---
title: 实战 | 记一次SQL到接口的SSRF
url: https://buaq.net/go-153962.html
source: unSafe.sh - 不安全
date: 2023-03-18
fetch_date: 2025-10-04T09:56:26.763497
---

# 实战 | 记一次SQL到接口的SSRF

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/360adab68c9836ad3179cc2aca64fbd2.jpg)

实战 | 记一次SQL到接口的SSRF

再一次众测项目中挖掘到一个有意思的漏洞空白页面，先扫下端口和目录Wap目录有个登录页弱口令爆破下日了，有校验本来准备换站的，刷新了一下，突然进来了？玩的就是心跳和刺激是吧，主打的就是一个陪伴是吧功能少
*2023-3-17 23:7:56
Author: [mp.weixin.qq.com(查看原文)](/jump-153962.htm)
阅读量:39
收藏*

---

再一次众测项目中挖掘到一个有意思的漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedw4AqghIaH0LxFAJr4Fy2d5cac3icXyS55EyRyeiaVlX9F7BA4OSwDkgtA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedw2ltkmmGLUaXDbADiatqV1lzRMDkNLNsGOpBDRJ1sCkZTO4icX7rYghNw/640?wx_fmt=png)

Wap目录有个登录页

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwvXicrhmvlvZmbyf2dWsuAIh522E1pzPeMXJW7WYj8JXdN77aSooaWYQ/640?wx_fmt=png)弱口令爆破下

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwm5OyOCRSRhUdbPLcNKhhRcBP7vGyys17phNBAWzsEJwTDykHpXsmicQ/640?wx_fmt=png)日了，有校验

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwPF7Pb53SZnOiahYkiaTut2M7DBoH8UgyYfYPkwMJiaLT2GupY1dYCO8sA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwCzjznoYAmMM4PSt6ia1UrXX3dpILW7EToJKcwkBLRbpqzSxrEdf2EDw/640?wx_fmt=png)

本来准备换站的，刷新了一下，突然进来了？

玩的就是心跳和刺激是吧，主打的就是一个陪伴是吧

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwc151MBXxBH0cbBbLdTkGDLEZtvX8STc8HYgfcd2DugJ0DTr7icv1GBQ/640?wx_fmt=png)功能少的可怜，也不是管理员用户

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedw3SlyJH3cfQJ58TwVWfrSXpWZicwibUI8MHqMkMPlWib6LCliaI1ePJMbaQ/640?wx_fmt=png)

然后仔细分析了下加载的url找到一处sql

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwq4ibrXV844FTnzGLGdGJld0CF2DeIAZ3SnCVbozZzC4ibF39AUZ61t7A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwzkvSNrAsslWLsmibJ4hjs0knUxay1BIzPtRx7nibxabcT4cI2yUuzLGw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwCjxrXHhu4oibjnnvggT3pdJ98nSfQhh9HVcCqludlkiaTlWrEvsIOpNA/640?wx_fmt=png)直接sqlmap梭哈梭哈

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedw9WkJpLxFNU32QUtWvvUTO7yaIYVCdct2Pg88T866IZz9EXqBia1K3Mw/640?wx_fmt=png)问了下不能读用户表，所以就dump菜单表吧，也方便观看

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwmRxlNlxVibap8qhJ6ticdIQYJrVIA8t9WVv3jE3Me0O2kFTT6Yg4zukg/640?wx_fmt=png)

发现有个接口有意思

```
/wap/web/api/imgsrc=
```

看看能不能远程加载，试下百度，不回显

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwRdMiaRlHVUAn89MDjXv1hUibmle1UFmJJw1dNRZpxLbiaKz1AThu4zzkA/640?wx_fmt=png)

试下dnslog

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwj0iaUeJvP8icyJ8ZVLND4a0WNcrAI50gVPISodUAoAbV6TqZq4vSTJ0g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwq5KTtticIj3XNJjPg3Y3bW1WHpqHbl0k0RZrP0bMCgcNwQCHJftc6hg/640?wx_fmt=png)发现返回ip了

然后试着其他协议，什么file协议，一样不返回

就一个dict协议返回内容

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwY7Iv3sG5VnNLYQ46m1Rn0cEofMmHqGsGkHbMhrTiciayjVyxMuFK73Gg/640?wx_fmt=png)想吧危害最大化咋搞呢，那直接从现有sql注入开始开始

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwGTm2ebXexkZbdpFuUHic4LAaRBEqvD8oeedXMQKvIrOdV3ABYSLAksA/640?wx_fmt=png)直接大力出奇迹

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwcdP6K7ApT5IPuN8EfzqAkjCiaTfWgdpcHnqj6yic59BR1Ifqov5xpuUQ/640?wx_fmt=png)解不开是吧，找朋友用他的hash池子试下

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwM5TbHzrUcIbkicxxUSZal6UTiaxw6qhr1bVlfAVsdrkd3VXSQ803w9AQ/640?wx_fmt=png)经过漫长的等待，报出了一个test的用户密码居然是abc8888

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwRSflJu2jr0C7DN0vkDhicJyQybmnnic9scT3b3d54zeZdicVxxgxp0Kgg/640?wx_fmt=png)

可惜权限太低,就到此为止吧，浪费感情

2023主打的就是一个难过，直接emo到

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibcUdGptOJPvP3KuYXneedwibVSzE2x0DbhMibYYLT7yWWIkQ9UrrAzIttbvQTwcIMc0ShOEV0zRwVg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/ndicuTO22p6ibN1yF91ZicoggaJJZX3vQ77Vhx81O5GRyfuQoBRjpaUyLOErsSo8PwNYlT1XzZ6fbwQuXBRKf4j3Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**推荐阅读：**

[**干货 | 实战渗透视频资源分享**](https://mp.weixin.qq.com/s?__biz=MzI5MDU1NDk2MA==&mid=2247511764&idx=1&sn=078a8b5ce7641a0b4641fae53fd1d111&chksm=ec1cfbebdb6b72fd6c09cc0bffd620d07f5c1ae301a4f4475378c6e5a469f7f921b2d070bc79&scene=21#wechat_redirect)

[**记一次赏金10000美金的漏洞挖掘(从.git泄露到RCE）**](https://mp.weixin.qq.com/s?__biz=MzI5MDU1NDk2MA==&mid=2247511554&idx=1&sn=47ba1e59f2e80b256a1808e12a59b4e5&chksm=ec1cfb3ddb6b722b406bf0bfd314d92aecec368d877da550ab385907ac9516ee93659dd65e37&scene=21#wechat_redirect)

[**实战 | 记一次针对非法网站的SSRF渗透**](https://mp.weixin.qq.com/s?__biz=MzI5MDU1NDk2MA==&mid=2247511509&idx=1&sn=73c16119dd7334591cfeb502a3523011&chksm=ec1cf8eadb6b71fc37282df87494e2b425068b73d157052c400a9a3d150ff526307c4c7b7d64&scene=21#wechat_redirect)

**[实战 ｜ 记一次从瑟瑟游戏的下载到某网盘网站的渗透测试](https://mp.weixin.qq.com/s?__biz=MzI5MDU1NDk2MA==&mid=2247511471&idx=1&sn=8fef4413352f6320b624e326249ad2a6&chksm=ec1cf890db6b718693793975f7561948921b9f80f789e20f6e4858a79789bebac0571c588403&scene=21#wechat_redirect)**

**[实战 | 记一次针对非法网站的SSRF渗透](https://mp.weixin.qq.com/s?__biz=MzI5MDU1NDk2MA==&mid=2247511509&idx=1&sn=73c16119dd7334591cfeb502a3523011&chksm=ec1cf8eadb6b71fc37282df87494e2b425068b73d157052c400a9a3d150ff526307c4c7b7d64&scene=21#wechat_redirect)**

**[2023年零基础+进阶系统化白帽黑客学习 | 2月份最新版](https://mp.weixin.qq.com/s?__biz=MzI5MDU1NDk2MA==&mid=2247511350&idx=1&sn=4164f4acdcc6216919ebe85b91cccd88&chksm=ec1cf809db6b711f9cc83d2c20f81e815b4bef5150d03c8afc688ca5083290e3507f34f621b5&scene=21#wechat_redirect)**

原创投稿作者：华强

![](https://mmbiz.qpic.cn/mmbiz_gif/Uq8QfeuvouibQiaEkicNSzLStibHWxDSDpKeBqxDe6QMdr7M5ld84NFX0Q5HoNEedaMZeibI6cKE55jiaLMf9APuY0pA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

文章来源: http://mp.weixin.qq.com/s?\_\_biz=MzI5MDU1NDk2MA==&mid=2247511792&idx=1&sn=befb4d4da9eb9e2585255e069a27c12d&chksm=ec1cfbcfdb6b72d96ea48f44e1fdcad0e061d19e595cee9ab9428083fd077ab7581123891aa0&mpshare=1&scene=1&srcid=0317amy0kilMOlZfAKh8b6CF&sharer\_sharetime=1679065665167&sharer\_shareid=205c037363a9188e37dfb6bb4436f95b#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)