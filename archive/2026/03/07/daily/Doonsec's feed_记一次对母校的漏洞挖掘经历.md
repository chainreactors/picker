---
title: 记一次对母校的漏洞挖掘经历
url: https://mp.weixin.qq.com/s/VzwjCfbHGESk7RwUMQ44cA
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:05:46.959205
---

# 记一次对母校的漏洞挖掘经历

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PZ1gNjiabODL3aORXhTzibaC3kZ5e0DrcEhhP3UlsugvO056O5BiblshZPYTqsAftibO3pFoqHQWpd1JF1VVU5Ted4JeTPbIY4icwU/0?wx_fmt=jpeg)

# 记一次对母校的漏洞挖掘经历

黑白之道

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif)

# 声明

本文仅供学习和研究网络安全技术。反对一切危害网络安全的行为。造成法律后果自行负责

注：本文漏洞均在取得授权情况下进行渗透测试后得到，且截止文章发布本文文章所有漏洞均已修复

# 前言

前段时间，刚好大三的学长学姐开始渗透校园网，那作为遵纪守法的好学生怎么能够放过这种有授权的好机会，于是也麻溜和老师报备后来到了机房，经过了漫长的信息收集后，也是想起来了前端时间让我们下载的 APP ，那 APP 既然是学校自己开放的，那就懂得都懂。

至于 APP 抓包的相关文章，各个平台也都有，这里就不再过多赘述了，主要还是和各位师傅分享下挖洞的经历

# 1 敏感信息泄露

在首页刷新后拦截数据包

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicd3icHqcn54cPJKuzdrR0YTTNZa2fSVWQ5xfdzKMhCickjicAiafeMhx6GmA/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic#imgIndex=0)

可以遍历此userId

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdfia9STwD6wmNYic0huXRZicwGYWHaLL7NwQvSTtUXX6Dkicgez87pMHryw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1)

便可获取其他同学、老师信息

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdv2QbFXGh29YlqrjV6LBR4kgotQRFVqTR7WPBh3RYOqxLIibyiaq7RRMg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdbO0eBiaS61mYVvJ32NSKnRibTuQjTBUbG8mWIV2mcoNHZRaht25nNlbQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

泄露学号、专业、宿舍、人脸信息共计可达 19000 条左右

然后我们就可以利用这些信息，进行进一步攻击

# 2 水平越权

越权查看他人账号相关信息（平行越权）

经过测试1-14590 为学生 14590-15000左右为老师

在首页刷新后查看到userid

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdQibX0KnPRcicXRAeNPjicoqjguonV6VRpBXBicngWqkO8KsjJIeCpcgwtw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)

此时可以修改userid

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdvrJPIBBFVVvNl53JtHCQnYDc4eX24iaG6ZM3cISbibVqhWV6d7ibdZFpQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

后面关闭拦截放包即可

然后在手机界面进入

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdZd0A9xiaI3tdxmz2LLIJYg5175xdGoGXnfhqn1nrZRDNCT52c5YgScg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6)

此时点击三个功能点可进入其他用户的界面

可以查看到其他人的所有信息，无论是通行记录，人脸信息，宿舍号、班级、姓名等信息都可查看

# 3 垂直越权

还是在主页刷新，然后先放过前几个数据包

然后再通过前面越权得到的管理员权限信息进行修改

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicddqLfGV7XPnIXicQ0klOtEekLDBT5B6FF0Pe9HPjRSZXOn6E8fj50rwQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

可以发现首页界面出现了新的功能点-考勤改签接口

在进接口前需要修改 persontype

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdIJIno5UXlk27wDmiaxva5JZXZ4gXam4PCXnnw6qwPX05Tdsp4mKH6vg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8)

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdZvUsaG2tCKulJo0n3UQrd5w7Jql6zfZLZwymyHVULF4A5IF7iaTpjkQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=9)

一样能够进入其他系统

# 4 越权修改他人人脸照片

（ps：这里的数据包是我刚下下来 app 的时候抓的，只是没想到后面给这个功能点下下来了，然后联想到前面也没有鉴权，那修改人脸肯定不用说了）

大致的步骤是：登录账号A后，替换数据包的 Authorization ，确保经过 Authorization 的合法性校验，后更改数据包中的 base64 编码，通过本文第一个越权查看数据的数据包遍历id找到账号B的 userID ，然后将数据包的 userid 改为账号 B 的 id 即可替换

**具体复现步骤：**

抓包，找到关键数据包，修改userid查看数据

通过爆破 userId 可发现账号 B 的 userId=6299，personId=6297

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdia8DOPcDp5qAj4lH5WE8rAWPnMfEy3WdVyIZsP38kUtxSzxSxafrWUA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=10)

登录账号B可发现照片为这个样子

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdgQAxaPqUt3cRKuiaXu7Hc4K9ahlBRzCZiaqwn4khev1w1sLpHwrMpTTQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=11)

在任意数据包中发现Authorization参数，并放入数据包进行替换

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdcb2hKic5Jq0icZJTwPYcvW9qtTlfGgTuRrgQ1zGa0Shrib7ibejFVOMs0Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=12)

发包，然后发现已经修改成功了

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdTvjaELicqBMnpNk0icaL1bydkZDfD1tAAyZJKEPAniadex4psINoT68Ig/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=13)

登录账号 A 进行检验（各位师傅可以注意下照片的背景），发现已经成功修改

# 5 存储型xss

首页--->宿舍考勤记录--->找到申请改签

按照如下顺序找到功能点

发现有文件上传点

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdANukQOmlyO5icNNic8wZxGAEwU9v83J0oic7wRgMRT43Z1gibJHLicscvUw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=14)

选择图片

（这里不需要点击提交，选择好图片就自动上传了）

修改图片、将filename改为svg结尾的图片，然后把文件内容进行替换

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdoibe0MhLxWYx7hg0dTOsxUV2kKNdwl8uy60I9YmibqZ6OqupB5BGTBcQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=15)

提交之后可以看到如下路径

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdwmg0GYUmpK1uKxib6p9Q9ia1AKhWu4JhLdVM1x2CpZ0QZYfdDib43p3Lg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=16)

出现后半段路径

e3631982-e9fe-11ef-9f5e-e8611a36bf65/xxxxx/2/xxxxxx.svg

到这里原本就已经卡着了，因为在 APP 端是没办法触发这个 XSS 的，但是突然看到了数据包 Host：参数，然后尝试访问了下，发现竟然访问上了，而且还和 APP 端用的账号密码是相同的，Web站点的图片保存完整url路径的概率就非常大了

登录该平台的web站点

打开F12

放到这个右上角图像位置

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicd4Np9RSTuk82ecvDMWkv9yGTg2RQibYH8eby3PicdqPtQsIOs4POWWhMw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=17)

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicd0A6vAZvrtVX3C3ZNAtFGKvonTnhPtT5nI6jbAbq41vYOx51t1iciaoPw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=18)

这里打了码可能看的不太清

https://。。。。。/evo-apigw/evo-oss/【路径】?token=【TOKEN】

到这里相信师傅们也会了，只要替换中间的路径，就能访问之前上传的文件，触发这个 XSS 了

![图片](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTricibARzueSHBdEaHe7PCSicdcnhkzibXwA8o8iaibUT7Rxic1LVudvHfKo23q25mkDzXqLlMROlpHmW0aA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=19)

证明存在存储型xss

> **文章来源：亿人安全**

黑白之道发布、转载的文章中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途及盈利等目的，否则后果自行承担！

如侵权请私聊我们删文

**END**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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