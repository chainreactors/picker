---
title: 实战分享——从简单前端加解密对抗到高危任意文件读取
url: https://mp.weixin.qq.com/s/uoBx7gYM5BI2ZtEOuTzVPw
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:06:06.945340
---

# 实战分享——从简单前端加解密对抗到高危任意文件读取

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0otI706xCFPKJY26mubuphoUaBkeTK0nIQ9qBs64XeCvia9JbRZFTBUWXoZGrCiaXtMYBAvTHiaxpdCOnVYiaPycxprPfrax5qh9rmyBCyPpmH8/0?wx_fmt=jpeg)

# 实战分享——从简单前端加解密对抗到高危任意文件读取

原创

SaltyApp1e
SaltyApp1e

咸苹果学安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

好久没写东西了，最近实在是太忙了，忙的主播有点仰郁了（

今天来看一个给某超敏单位做的渗透项目，在面对棘手的传输加解密对抗下抠出的一些中高危漏洞，图片已重码还请师傅们见谅

## 开测

首先拿到资产，客户为了方便测试提供了测试账户，但是还是常规的测试流程，我习惯先测前台，登录框的弱口令SQL注入逻辑绕过都要全部过一遍，看了看数据包，全加密啊...

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0otI706xCFNrzhkmzDQotCBb5n6uPZT5kJr9OVq7dM4Fu7HZhIPicXy4iaDjCOJ1UDRt3FHEkpI7BDuCHE8mFibjgzjKmR6FWTo1cNINL2N5n0/640?wx_fmt=png)

不过我再一翻，欸，有jsmap泄露，又能水个漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0otI706xCFOoDWEog33UVH13PdwyK9f60TdsfFkojshOrddO4plP4yxbVRzciaPUPldQbK8Phwe7p744ibETEHH505W4ibt0ZKmCibGjbfqBDibo/640?wx_fmt=png)

全加密有点难搞，不过先拿二级目录跑一下有没有什么东西，还真给我跑出点东西了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0otI706xCFOZPKJSTJoRQ4mfRO2VWaYmLicJzrjibbgGLOWtiae6CiaVHCfiapvGgtu86oSk4EFW0KiaUxS0EKws1c67mns0ky0lpJ5EhTp0x3JW8/640?wx_fmt=png)

泄露了一个SVN的数据库文件，里面存放着一些源码路径之类的信息，有点类似于前面的jsmap泄露，直接导入到Navicat就可以看到具体信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0otI706xCFPhPEr1gQhaZn5hD5iaOicYYnfYKoId2YMhuGibia7kVkmoYu2nR4JwWrwBkQ5nr1zuht0L0DBDxAI4niaWN5gK0hc73rxKk3sBDtQ8/640?wx_fmt=png)

好，常规流程都走完了，是时候搞一下前端加密的问题了，常见的前端加密有AES、DES、RSA、以及国密SM4和SM2。如果说是AES、DES和SM4那还好说，这种对称加解密，一般都能在前端js文件中找到相对应的密钥、向量iv等加密信息，除非动态密钥或者超强前端混淆的情况，那就比较难办一些；如果是很不幸地遇到RSA、SM2这种非对称加密，基本没招（除非开发送饭吃，把私钥写在前端了）这边的登录接口就是用的动态公钥RSA，而且没泄露私钥，所以没啥好测的

介绍完了回到案例，这里很幸运，是AES加密，而且还在前端js文件中发现的硬编码key

![](https://mmbiz.qpic.cn/mmbiz_png/0otI706xCFPJSYsO2v9u4c1t2jP1tahf0Q0acwqHgIPYSxGXEIm8640s67Algs7cDQ5zauzVzVibOZU2KebO6TTPGiawKkOzQWkynmD4bKWjU/640?wx_fmt=png)

甚至还是我最爱的ECB加密，省时又省心，也是成功解密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0otI706xCFMzbSdLM4qGBicIoQpleQzDj0x5f5ugDGKfoFdicuQiaicfQpTKOXqxPWXaNqgDNhT2HTzBUKKa6Oc0UiaYsW7H8J1JgTEa1orITTtM/640?wx_fmt=png)

那么接下来就可以写一个yak的热加载代码，进行解密替换重放包等一系列操作，便于进一步测试，写代码啥的就没必要自己写了，这里推荐一个写yaklang热加载代码的AI，我觉得还挺好用：

```
https://deepwiki.com/yaklang/yaklang
```

![](https://mmbiz.qpic.cn/mmbiz_png/0otI706xCFNibkiaMt8j6ibzkOWHaI2rVmLfvsOz9Yt3xk6Epc1T0Leia7G3MdJmGs3PsZgFq70ooZSDCmPokfl4vO2OEiaAn5j4W8b3yKGBO9zQ/640?wx_fmt=png&from=appmsg)

解决了加密的问题，那就很好办了，进后台开测！

进了后台，虽然客户说是测试系统，但是看到有很多流程、文件和工作流等东西，过于敏感这里就不放图了，感觉就像是个正式系统，所以也没敢开插件乱扫，大家平时测试的时候也要多多小心，万一插件把站给整崩了就又得背锅了。随便测了一下，整了一些反射型XSS、未授权之类无关紧要的漏洞（未授权是因为接口非常隐蔽而且无序，一般来说不会有什么大问题）回看数据包，这时看到了一个接口

![](https://mmbiz.qpic.cn/mmbiz_png/0otI706xCFMSjPiaOUOnHNttgJCXedzF9jlTr7tUuppgnE1OlmRicdFKJkv6mIrEczb8RwgkXr9iahR1pMCs1EGO8mPhoAnfnkpoAYTCh301n8/640?wx_fmt=png)

这个接口是用于请求图片的，图片以base64的格式返回，聪明的师傅肯定马上想到，对请求体解密，看看参数是什么样的

![](https://mmbiz.qpic.cn/mmbiz_png/0otI706xCFPytap1nefxp8AG3zpicze8mK9rWVYXqNJ2IqBOLMTmKY4CkCTKudlO2mLHez2Nu6ytiaD3TCV2bL2agszyyyOlh5FNH3GTrquS0/640?wx_fmt=png)

果断发现了一个很刺眼的参数：path。第一时间想到目录遍历和任意文件读取，尝试了目录遍历，似乎是不存在

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0otI706xCFNvWLs9IJiaC0NSuCPWkaibWOA2jXEUWfwF32olZibpZib0LFnTQ6PLzqvKS9v0JGbXAicsDjUrFguJRzuvhdtPHYnicELbdDzVPHLmQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0otI706xCFNCpzX2jCNk4Q7Xscxlz8B3jGdg2eUB2QJlibEfT2cHYaib0KHxvlmqxTANiaRIMyuTH83FKthan5ftRjicBlRwwFrmK7UiaEkjAcV0/640?wx_fmt=png)

那么任意文件读取呢...

![](https://mmbiz.qpic.cn/mmbiz_png/0otI706xCFOUJibIwxQYU9VQNxT84YJmF1uo1VG6Un1vk3iabXicpu3ib67aszCnKBT5YeichVWPaAiaJV7lvy7FhicL62Nibicp1NDlPiajbWXfpJU5M/640?wx_fmt=png)

一看这个长度就不简单，素素解密一下！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0otI706xCFMsT9uicQ5TUxxZlSrClMniaDmDWP722IcU13G5Q06Lwfxj1QqvtjplBoH50mf6rtC4BEPrJ9OX2mG4Nworv9UHkdpJUDOjWzDzs/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/0otI706xCFNmFd8KLOmuHZw9s9II0JnnCL9N9gN66CvQOibKApOoicBX61mF9WeobBKD4X9Pgjgkxu250KLoXnp3Yf8SHBmycC9ia5TkCzictBI/640?wx_fmt=png)

直接起飞，任意文件读取拿下！而且回看数据包列表，基本上所有请求图片都是通过这个接口进行请求的，而且还有一个接口是登录页的图片，也就是说存在一个未授权任意文件读取，妥妥的高危没跑了

后续也没挖出什么漏洞了，而且利用那个任意文件读取翻了几个常见的配置文件，翻到了很多很敏感的东西，zwy账户密码、一些数据库凭证和备份文件什么的，已经可以充分证明危害了，直接美美下机

## 总结

渗透测试，除去长年累月的经验积累和各种不为人知的奇淫巧计，剩下的就是比谁更耐心更细心，还有一丝丝的运气加持~

马上又是紧张刺激的攻防演练咯，回头又有东西写了

6aG65bim5LiA5o+Q77yM5oOz6Zeu5LiA5LiL5pyJ5rKh5pyJYmFzZeWNl+S6rOeahOa4l+mAj+aIluiAhee6oumYn+WGheaOqO+8jOacieeahOivneasoui/juengeS/oeS4u+aSreivpuiwiA==

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BL6Bl6SWr6b7yj0iaKfvup9lOXXxEiawM8yGmhQJEvF9picNYWZE1fq0HF1uDiaprGeSZSicsmQtGlNVxRd6I6dV5MA/0?wx_fmt=png)

咸苹果学安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BL6Bl6SWr6b7yj0iaKfvup9lOXXxEiawM8yGmhQJEvF9picNYWZE1fq0HF1uDiaprGeSZSicsmQtGlNVxRd6I6dV5MA/0?wx_fmt=png)

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