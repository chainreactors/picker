---
title: 【转载】某银行员工维修APP渗透测试总结
url: https://mp.weixin.qq.com/s/S42aSByrI_l498WseDFAjg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:34:19.293662
---

# 【转载】某银行员工维修APP渗透测试总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DJX1rNqJe4keylvMj5D2SWMxP9Gic8hGZ6y7q8dejFuq8ibIFfqErcZQNPicJwcWlE9FUf6Tywq401AEncxvGibtM6HPPUvc1aumnyLsBic6QEbs/0?wx_fmt=jpeg)

# 【转载】某银行员工维修APP渗透测试总结

隐雾安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

好文推荐

文章作者：先知社区(WMBa0)

文章来源：https://xz.aliyun.com/news/17265

上周对某行的4个app（其实都是一个app写的模板）进行了渗透测试，记录自己渗透的一些思路和过程，已打码，仅供学习和参考。

个人是逆向出身，后来对Android感兴趣逐渐深入学习，更加偏向于本地漏洞+web渗透测试，其实还是菜鸡一个。

可能大多数厂商认为Android本地漏洞，不造成服务器危害，就不重视，甚至感觉没意义。那么本文就从一个毫不起眼的app信息泄露开始吧

# 脱壳

360免费版加固，frida-dexdump、blackdex都可以脱掉,这里就不演示了

https://github.com/hluwa/frida-dexdump

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmmmB2eFwjG8rvP65r4voHyKx0CYLJH2ppiajkq7a7C5E7nY8QPJOX8y5uNP9byAdgESFT4icyzNWfg/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic#imgIndex=0)

# 密码泄露

经过对app登录界面，又对密码强度进行了验证

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmmmB2eFwjG8rvP65r4voHyqmIkptR8GJ5kq3uPUdgYqtyfaJRickrmLsK7Kc1MWeE2wzwcWVKJlEw/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic#imgIndex=1)

经过对该类的方法进行hook（frida），密码直接弹出来了

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmmmB2eFwjG8rvP65r4voHyfDwZ6Q3UwN9NyFQXzz69hKCrhTic35yeogugVnkQcoCRyBQpu96VicpA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)

这样的校验方式只能说太危险了，做的很草率

如果用户安装了木马监听app，这样密码就泄露啦

正确做法，密码不要存储在本地进行校验，发包发给服务器进行校验

那么厂商认为这样没什么危害，我也很吃惊，可能真没啥危害吧，毕竟没有直接危害他们的服务器

# activity越权

看了他们的Androidmanifest.xml文件，发现每个activity全是导出状态（默认）

直接上objection进行，activity列出

```
android hooking list activities查看当前activityandroid hooking get current_activity启动某个activityandroid intent launch_activity
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmmmB2eFwjG8rvP65r4voHyeibUI5Gug9kDqfichibqEnHt5scrJqvDRTSFLrRtzcoJfEibvUyLcLKeCA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

这里面的每一个activity都可以通过objection唤起

可能感觉没啥用，但是每个activity都是具备一定功能的，有的开发者没对功能做身份校验。

经过对activity的遍历启动，我发现了里面有个员工信息查询的activity

可以直接打开，然后查询数据，没有对操作的行为进行验权

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmmmB2eFwjG8rvP65r4voHyGfj9ib0fxv1yIyJSZB9APOIo6to4W7WtibV7fhaek9GDsSgxgQOYdHFQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)

比如这个，我添加数据居然成功提交了

activity越权属于Android客户端漏洞

# Log日志信息泄露

这个漏洞属于开发者在开发过程中，用于输出辅助信息

该app逆天的地方在于，直接把数据包未加密的时候的数据也输出出来。

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmmmB2eFwjG8rvP65r4voHyHib3v5rJq54y6MkibPtSaF1I9RBRFXVYBicr7QUbiaaaa2whyUqqMFDNpQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

adb logcat zcxxxx

即可看到每次数据包加密前的内容，还有其他的地方也有log打印，这里只是看到其中一处哈

对该漏洞进行提交，厂商认为没有危害服务器不给予认同。

攻击：木马app监听Log日志，直接获取用户名+密码

防护：release版删除log日志相关函数

# 数据包加密方式+秘钥泄露

经过脱壳后，app的所有应用层代码直接呈现在渗透测试者面前

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmmmB2eFwjG8rvP65r4voHyicvO72E6NPIYUuicZxjfTDiapsbRJrvpIAdCwQpG65xsrUkQWGQ1vPIiaw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6)

(⊙o⊙)，其实该类我们可以直接使用IDEA复制粘贴加密和解密方式

对数据包解密就可以得到明文

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmmmB2eFwjG8rvP65r4voHy0CoNBnMD0HlsRm4I4Gms0rGUZASfGCzAZq3zLDNiayErSjXYnIMCMRg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

解密后的数据包，没有sign值校验，意味着攻击者可以爆破用户名和密码

爆破参数，测试参数等等都可以

那么厂家也不认同这个漏洞。ε=(´ο｀\*)))唉

原话：实际环境难以造成影响，无法达到收录标准

# 任意用户密码修改漏洞

app其实还有其他漏洞的哈，这里就拿前面提到的activity越权+数据包解密来结合一下

因为存在activity越权，所以我们可以唤醒密码修改功能的activity界面

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmmmB2eFwjG8rvP65r4voHywEMMMughpUIdOPtPsdVMPuibPicoE2CYtiaNIOBTHxIcYnVdqJ9Pbexnw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8)

该界面没有验证码，没有手机号验证

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmmmB2eFwjG8rvP65r4voHyYwibLw1YgmSrJ4vuwGm7hxEIibibpQGlHszXW2Q1RmzWwz8yU8zOMFYPQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=9)

很简单的3个框，渗透测试狂喜

尝试admin用户名

对返回包解密，结果为：“查无此供应商键值”

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmmmB2eFwjG8rvP65r4voHy8Efjr2EpfdPdPtJWibOmL3ia0Azf4qahjgVZGlsJu80N2nqQRklWe4BQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=10)

到现在可以爆破用户名，可以对输入框进行一系列测试等等操作

厂商认为该漏洞不给予收录，需要我证明可以修改用户名密码。

那我建议给我一个测试用户，不需要密码，只要服务器那边有该用户就行，我证明一下能不能修改。（app没有注册用户功能，是内部的app）

厂商也不愿提供

实在不行我爆破用户名吧，厂商也不愿担责任，禁止爆破

所以结果就是不认同，因为我没证明可以修改。我勒个逆天回复

# 文末总结

ε=(´ο｀\*)))唉太菜了，挖的都是垃圾。

希望可以给师傅们提供一个漏洞挖掘的思路哈

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ELQKhUzr34xNiazXVTT6qEbEU7UjrgFplQqq3mt9dTpB7qCTQSsP9FMqic1ub553HR5NPeVcHnI7QSwde7madgCQ/0?wx_fmt=png)

隐雾安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ELQKhUzr34xNiazXVTT6qEbEU7UjrgFplQqq3mt9dTpB7qCTQSsP9FMqic1ub553HR5NPeVcHnI7QSwde7madgCQ/0?wx_fmt=png)

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