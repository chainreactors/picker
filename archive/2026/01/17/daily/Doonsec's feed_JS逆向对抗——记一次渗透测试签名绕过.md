---
title: JS逆向对抗——记一次渗透测试签名绕过
url: https://mp.weixin.qq.com/s/QAD6_65LQil1bz3JZ4st_g
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:33:43.858896
---

# JS逆向对抗——记一次渗透测试签名绕过

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WsdWKvWsNdtNM2Ot2IvR1SfY7w0j40z74qXoky6kiaPH6Ee7crg6aBZw/0?wx_fmt=jpeg)

# JS逆向对抗——记一次渗透测试签名绕过

点击关注 👉
点击关注 👉

马哥网络安全

![]()

在小说阅读器中沉浸阅读

在测试中我们一般都是通过修改前端传入的参数来测试目标是否存在相对应的漏洞，但是如果网站设置了签名验证机制，只要你修改了前端的参数，就会返回签名验证失败从而阻挡了你测试的脚步

但是JS逆向的魅力就在于，只要是你发起的请求带有的参数，无论是什么加密，总能在前端找到相对应的加密逻辑。

只要我们拿到它的加密逻辑，我们就可以编写相对应的加解密脚本来伪造，从而实现绕过签名/加密的防御

下面我就是在测试过程中遇到了签名验证的一个例子，我们接下来就在前端找一找他的实现逻辑

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WhSeicY33bpUxmUflafMHIE0copZgINX9ibEtdYZdqEWIuianiayI8dMYBg/640?wx_fmt=png&from=appmsg)

首先我们要先找出他的实现代码在什么位置，这就涉及到关键字的选用了，像下面这个例子我们看他的签名的参数sign很常见，我们一般不直接搜sign，这样直接搜一大堆，效率太慢，但是其他参数比如noncestr就不太常见，我们就可以直接使用这个去间接定位sign值的位置

全局检索noncestr，只有一个匹配，这样就大大提高了我们的定位效率，再周围查看sign值实现代码在哪里

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WH9CPbzAO5S47WRebDEAibsB2XCJJj0ppGyv3L34w9UKv4SRtMLQDhiaw/640?wx_fmt=png&from=appmsg)

可以看到，就在他的周围就有sign

一般这种参数都是一起封装的，我们只要找到一个的位置，那么在其周围都可以找到其他的参数

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WtJu1hHk7iaPSibicf1UyRguUVcALRll0wmBUYJqDLlXELHPicnjcqSWa2Q/640?wx_fmt=png&from=appmsg)

找到位置后我们打个定点

可以看到就是这个位置，传入了f的值，然后通过这个值来加密形成签名

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WrGuXvRBrTCYlKtqpJIm2HnlMbDsktJyvdZg2hWA1jHicfNblnTG5iasg/640?wx_fmt=png&from=appmsg)

我们在控制台打印看看f的只是什么

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WVibrMM2czKkEr6IsojqWSZ9aHRFhWyic1yVh5eGsNFiaCzFmuPQzc5PoA/640?wx_fmt=png&from=appmsg)

ok，接下来我们跟进签名实现的方法，看看代码逻辑

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WDfBMYwLaFUs7AJiaoDnjpV7LovUMReLTKtwPAo0pmG2DDibyvFpUiaia5A/640?wx_fmt=png&from=appmsg)

```
 c = function(e, n)  {   var r = t.wordsToBytes(s(e));   return n && n.asBytes ? r : n && n.asString ? i.bytesToString(r) : t.bytesToHex(r) }
```

当我们走完这个方法后，sign值就出来了

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WBoFpKyvlRsdtvqKA99ibgWhsEtm9knM8VUpyQpaibAYZJwYDbNUeBj4A/640?wx_fmt=png&from=appmsg)

控制台输出一下

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WegBcGFNI2sTyicq4Zf3wL1ubowiaoqX7o6nrm5rRGlFJXwyqbkrnQBgA/640?wx_fmt=png&from=appmsg)

可以看到，这里s()这个方法就是sign值的生成方法

我们改一下参数，生成其他的值了，这样我们就可以任意伪造sign的值了

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9W4MJU23yrqeCuibuMJuFKCjZZ3MB1bibBeaQeMM1FGCmD7lFh7cMpdonQ/640?wx_fmt=png&from=appmsg)

我们将生成的值放入我们的数据包，成功实现签名伪造绕过

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WdG2FNvFCcNSY6Xnb4O6AaLAN7Vvf7ocsTic9KiavdxVUzYCUdF2saRnQ/640?wx_fmt=png&from=appmsg)

如果不想手动还原代码，就把你拿到的加密逻辑一股脑丢给AI，让AI分析并写出加密逻辑

```
f = function() {  var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}    , n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : u    , r = arguments.length > 2 && void 0 !== arguments[2] && arguments[2]    , o = t({}, e)    , i = {      appSignKey: n    }    , a = Date.now();  e.serverTimestamp && !l && (l = e.serverTimestamp - a),    o.timestamp = a + l,    o.noncestr = c(8, "number");  var f = Object.keys(o).filter((function(e) {    return void 0 != o[e] && "" !== o[e] || (delete o[e],                                             !1)  }                                )).concat("appSignKey").sort().map((function(e) {    var t = i[e] || (void 0 == o[e] ? "" : o[e]);    return "".concat(e, "=").concat(t)  }                                                                   )).join("&");  return r && console.log("sign", e, f),    o.sign = s(f),    o}
//下面是s()实现function(e, n) {                            var r = t.wordsToBytes(s(e));                            return n && n.asBytes ? r : n && n.asString ? i.bytesToString(r) : t.bytesToHex(r)                        }
```

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9WxpvPAffZ0At4Hyvprl5rJ8JnRbs3SzURXMk94dAVFk4BwMzAC8B8iaQ/640?wx_fmt=png&from=appmsg)

```
import hashlib
def generate_sign(sign_str):    """    核心SHA1加密方法 (还原JS里的s()函数)    :param sign_str: 拼接好的待签名原始字符串    :return: 小写的sha1签名结果，和JS完全一致    """    sha1 = hashlib.sha1()    # 转bytes格式，utf-8编码，JS默认也是该编码，无乱码问题    sha1.update(sign_str.encode('utf-8'))    # 生成16进制小写字符串，完美还原 JS bytesToHex + 转小写    return sha1.hexdigest()
# -------------------------- 你提供的【正确待签名串】 --------------------------raw_str = "appSignKey=4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&noncestr=48025550&timestamp=1768236168865"# 生成签名final_sign = generate_sign(raw_str)# 打印结果print("最终生成的sign签名值：", final_sign)
```

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnpMCEL5CrwsdQ92DGZ4r9Wk5d8icRPkkt1LfPE0kNAHGLsRTkeKYPT7pC8uNLYAOzYgCnVicK5LatQ/640?wx_fmt=png&from=appmsg)

这篇文章主要是分享一个加密逻辑的定位技巧，还有如何结合AI编写加密脚本，例子不重要，思路才重要。

文章转自先知社区，原作者云逸，侵删

![](https://mmbiz.qpic.cn/mmbiz_png/INa3lxHH4I2aV3zCmfiaj4cXeQ2HQd6s53wJS36HYI65ib48fujDK8najfWiahicsljzsdT3dfVS8HHyxaviaSd8g2g/640?wxfrom=5&wx_lazy=1&wx_fmt=png&wx_co=1)

**今日福利**

为了帮助大家入门网安，给大家推荐一份**《新手Web安全入门到精通》**，共474页，包括**代码审计、web漏洞、靶场实例分析、信息收集、渗透思路**等，将Web安全攻防知识点一网打尽。

代码配图，简单明了，攻防思路清晰透彻，关键是里面还配有多张思维导图，通俗易懂，实用性非常强，很适合新手学习参考~

![图片](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnknFkWScXBu74vvYnrsKQeSxTJrcrLN5T9jWmO0WejeeRJzjYSo3QGnGGfibOmCRIZ8EGptiaTnKdQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnknFkWScXBu74vvYnrsKQeF72M9DhzWE0U5434e5vlcoySfD4kicEibGeMVZpdnNRQqqWubWRUPHjg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnknFkWScXBu74vvYnrsKQeoy1Raic5D6tP84jY8W0WQhGOnVCxrSsy1hAuOj9YIcsDnbXicRXxDyyg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

![图片](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnknFkWScXBu74vvYnrsKQe0TTJ1MOQuQjyAMbyichkoSYxqLTCbNnIEJ8osu9dso3rJULxpwr6nUQ/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

![](https://mmbiz.qpic.cn/mmbiz_gif/NUwbCdTuQQxsJibSZGyA8akP9TVyJfPcpJ4uIZJDj3akRUfv6cNbnksGJQsibq1aH8iaGDic7TvOaSwNGXLdQ8PC9A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

以上资料获取请扫码

![](https://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAmQO922RsJH8oNVNo28hujdEqkbnrZTKI5IXibkbQGT3Es1s6wruZu9giczEsvg0Qr6G06ldEuVGFPg/640?wx_fmt=png&from=appmsg)

识别上方二维码

备注：***web安全入门到精通***

100%免费领取

（是扫码领取，不是在公众号后台回复，别看错了哦）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

马哥网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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