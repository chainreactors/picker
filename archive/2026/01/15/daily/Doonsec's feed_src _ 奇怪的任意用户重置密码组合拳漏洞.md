---
title: src | 奇怪的任意用户重置密码组合拳漏洞
url: https://mp.weixin.qq.com/s/aQPGjD_lgc2yeiRvlh21tQ
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:26:40.653274
---

# src | 奇怪的任意用户重置密码组合拳漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNqx9LricZvJhCiau5chWfCT2S1cePRJRl0SHtdViaAN9w1X9z0ghKTFOUPw/0?wx_fmt=jpeg)

# src | 奇怪的任意用户重置密码组合拳漏洞

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

以下文章来源于有恒安全
，作者有恒

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4P2gbKZcItyLUXAbDPIo3k3pnwpOxcoibDho6RTsh2Z7A/0)

**有恒安全**
.

安全技术知识分享

分享一下之前挖src遇到比较奇怪的任意用户重置密码。该漏洞在是两个不同学校的网站相互配合导致的组合拳漏洞。

**一、收集到的信息**：

1、学校a:https://aaaaaaaa.cn/user

2、学校b:https://bbbbbbb.cn/user

3、a学校与b学校是同一个系统。

4、b学校的学生：杨\*\*，学号与姓名，但不知道密码

5、b学校的学生：于\*，学号，姓名与密码。

**二、漏洞复现**

1、打开a学校网站，a学校的登录分为两步。第一步输入学号与姓名。

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNqStpmJB6Cf3GkRAURfBBdFOZSsKU8YgamueAuvYoOXuA8EiaokiapsUnQ/640?wx_fmt=png&from=appmsg)

当学号与密码正确后再进入第二步输入密码。

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNq94664HkFzrpbNCOY49WPQ9Q9q8NlMgryznPdYb2eZLPkibkODx5yXwQ/640?wx_fmt=png&from=appmsg)

2、在a学校输入信息收集到的b学校的杨\*\*学生学号与姓名。

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNqhmZKcADuknicgUMuKFjVlyIu5kWJAibsWyy6BkUFB2DUYribicpcOhY6qQ/640?wx_fmt=png&from=appmsg)

下一步显示需要杨\*\*的密码，密码未收集到，但问题不大，从响应包中成功获取到了杨\*\*的userid。

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNqia4UYnz26TZ52BngnRVMNazBPLkzsWT1LA5sNcl2ZzGIbdJsvYoBu5A/640?wx_fmt=png&from=appmsg)

3、打开b学校网站https://bbbbbbb.cn/user，系统与a学校网站相同。不同的是，b学校的登录步骤只有一步，即输入学生的学号，姓名与密码。

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNq4k7wibOzfuslgibbB9OVGT7JNMqlKPThZdGicjkIozG2GjF9WBhlTMFgA/640?wx_fmt=png&from=appmsg)

输入信息收集到的b学校学生，于\*\*的学号姓名与密码进行登录。

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNqxyU45NuFP38NozHSA75XjfomMxLqL37aXficlH7gP7stLNyq7Bw8ZFQ/640?wx_fmt=png&from=appmsg)

4、在登录后的个人信息设置里，填写好要绑定的手机号验证码信息，抓包。

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNqCqOulZo6iaibvZATOPjmYafJGaTHibMcGuzZM3vSgGVZTkcOuTx0xEjfg/640?wx_fmt=png&from=appmsg)

修改userid为从a学校中获取到的杨\*\*userid

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNq0tibeMyOaVWC0gD48DuXn12DIQXKSfXVRkxIrcQLoIM9SRw64icAvc4A/640?wx_fmt=png&from=appmsg)

响应包显示修改成功

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNqhibW5BMfQT9SE4cPhUArC4Fl2gJ2A4OVPdTqIia4VLQgxdjibusp0gxSg/640?wx_fmt=png&from=appmsg)

5、打开b学校的找回密码功能，输入杨\*\*学生的学号与刚才越权绑定的手机号，获取验证码信息,新密码为Aa123456@

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNqk3XmqFcSibsSCUD7icvicwgAQ63mb50dtvZLh6Dr4zCKgFvNFKwNDiaInQ/640?wx_fmt=png&from=appmsg)

修改成功

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNqH0hAWQeDtgIpMKiaUpMwmmOSiaoXFl4ziaQ66mdmPLoPz1ZYFesxZaFKA/640?wx_fmt=png&from=appmsg)

6、重新登录b学校，输入杨\*\*的学号与刚才成功修改的新密码Aa123456@。

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNqb7benDYo841EN1zxe2Hm6Xh9mdUg8icBlwLcKY18J6AEs0qibDFSgTtw/640?wx_fmt=png&from=appmsg)

成功登录杨\*\*账号

![](https://mmbiz.qpic.cn/mmbiz_png/fp1zrrz1Uibic25n4Wib6WWHARsYuvXxyNqXS2meI6JcmGJHUFfmicOKn5T3TqsPAkhOibtcLvSyU6HXZjPqDwmIsgg/640?wx_fmt=png&from=appmsg)

**三、漏洞总结：**

1、a学校登录分为两步，b学校登录只需要一步。且该两个网站疑似共同同一个数据库。

2、b学校登录只有一步，无法直接获取到userid，所以可以在a学校中的第一步登录b学校学生，获取到b学校学生的userid。

3、通过userid越权绑定手机号，最终实现任意用户修改密码的组合拳漏洞。

建了个src专项圈子，内容包含**src漏洞知识库**、**src挖掘技巧**、**src视频教程**等，一起学习赚赏金技巧，以及专属微信群一起挖洞

圈子专注于更新src相关：

```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例2、分享src优质视频课程3、分享src挖掘技巧tips4、小群一起挖洞
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg41LkR0ezBlmjJY4Lwgg8mr1A5efwqe0yGE9KTQwLPJTe9zyv3wgYnhA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=24)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=25 "null")

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOApVm8H605qOibxia5DqPHfbWD6lmcweDjGv4DLl45waD068ugw2Iv2vg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=26)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWr5g7s0TNF4tBZqNbdewPNswTDOfvN6PkggCqz8j3mib6Vf3z4ia83asg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=27)

图片

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4Bd1oBmTkA5xlNwZM5fLghYeibMBttWrf57h8sU7xDyTe5udCNicuHo8w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=28)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYrUoo5XZpxN9Inq87ic71D6aUeMdaWrKXgYYia2On8nMA7bqWDySa8odAq1a0kkp3WFgf0Zp0Eut0A/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=29)图片![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4KKlic4yiafWTpLdejicQe3MllEQc24ypeI3anaK7IjJDVyq1WVQN2yKBA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=30)

图片

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWHjP3FUnZpXdrOicRWrCf9MibaglQia7WesCVs0ibtBhC4c2XiaT9HibE1Drg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=32)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWXytl9Ioah3X7tw7EMlWV96wWXEHFEM4m6NwlvvkcmEcPqcxcE9MQDg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=33)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaDpuFU7U9TMK5eIpY8iaJcXCicmTB6fsRd8icmH7K1X99YbC07GaJbCRReocORsnDGNU7H7PeqcysIA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuaDpuFU7U9TMK5eIpY8iaJcXzeTsials9fwTK9lb0iavN5ya2KJAT9sXIBShtRdfRWHNUpgPKjmEnpsA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=21)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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