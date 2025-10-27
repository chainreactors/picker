---
title: Src实战案例分享
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496175&idx=1&sn=95930a0e2e553c9e841265e8019d00b4&chksm=e8a5fb8cdfd2729a236f6266c5c0caf2bf41570798b529f8dfea139d77c7d2ca1f13e8071878&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-20
fetch_date: 2025-10-06T18:50:27.085090
---

# Src实战案例分享

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ELQKhUzr34yjhZpiaWn8TRIC0m9U1w8jEpu1Qhjw0DrfJyOzD79ib9BaRTV8QLstciad3JuibAPg5zlR7ZWUYbxYAQ/0?wx_fmt=jpeg)

# Src实战案例分享

迪哥讲事

以下文章来源于隐雾安全
，作者隐雾安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM726qqnXD4ibQaXQjLVHp9Gxyv9TJsiaWicUIvUnjPWalVYA/0)

**隐雾安全**
.

隐雾，为您提供职业成功的关键。

**No.0**

**前言**

挖洞就是要多思考，要是没有权限我们需要如何突破限制进行测试

，我是

**No.2**

**案例一**

首先登录XXXX平台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34w54bBvC9p1TuYnicjQaQE6EDncyUQuRUiaibpOa4oNMmiaNKfPYuvJHIA22LohllVVibtQ8PYP482htQw/640?wx_fmt=png&from=appmsg)

然后找到以下接口。

```
GET /user/credit?company=111111 HTTP/1.1Host: nXXXXCookie: XXXXXSec-Ch-Ua: "Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"Sec-Ch-Ua-Mobile: ?0Sec-Ch-Ua-Platform: "Windows"Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Sec-Fetch-Site: same-originSec-Fetch-Mode: navigateSec-Fetch-User: ?1Sec-Fetch-Dest: documentAccept-Encoding: gzip, deflate, brAccept-Language: zh-CN,zh;q=0.9If-Modified-Since: Tue, 02 Jul 2024 10:44:17 GMTPriority: u=0, iConnection: keep-alive
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34w54bBvC9p1TuYnicjQaQE6ENMITzxw0tCqICNG8Bhaib4BSDztjS8PnlmVkMib6HphokWib70fSly7KQ/640?wx_fmt=png&from=appmsg)

返回包：

```
HTTP/1.1 200 OKConnection: keep-aliveContent-Type: application/json;charset=UTF-8Date: Fri, 16 Aug 2024 09:50:07 GMTX-B3-Spanid: 663d4f5fb8605800X-B3-Traceid: eb7f16085bb411ef96336f37270dcc88Content-Length: 375

{"code":200,"message":"success","data":"https://xxxxxx/trust/vmagic/bacct-service?appid=11&dimid=1001683651&token=jBpHCy8CWzqksLDpKjX4GAUNUSoasO8ZChWIiG8Lrnyt6tBreLiZi6bBqvNc-imcXz5rXdDg.&theme=bluemode"}直接访问该链接。https://xxxxxxx/rust/vmagic/bacct-service?appid=11&dimid=1001683651&token=jimcXz5rXdDg.&theme=bluemode
```

可直接访问对公打款认证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34w54bBvC9p1TuYnicjQaQE6EzZjqwyz7SdSXAkyur4LJ50rC4gXglm7BgqGWtsuJBvtwlKGW8lPrNQ/640?wx_fmt=png&from=appmsg)

填了下信息并提交，显示待打款状态，提交成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34w54bBvC9p1TuYnicjQaQE6EibicZFbevbfPFupD3XXja45XrkD7ewvYb4UWwMDzEhtqJZxg2jlobkEw/640?wx_fmt=png&from=appmsg)

而正常的流程是这样的。

首先进入认证。

https://xxxxx/uauth/login

进入后台需要经过资质认证才能进行对公打款认证。这样的话，就可以绕过资质认证，直接进入打款认证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34w54bBvC9p1TuYnicjQaQE6ErDSl7n9EMAqcDqX4PJerGeoRjc7equiaDajgJk7hR0uY6kRnR741rXg/640?wx_fmt=png&from=appmsg)

**No.3**

**案例二**

Web无账号，不能查看后台接口

此时app的js刚好泄露了匿名token

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34w54bBvC9p1TuYnicjQaQE6EIbwyibJ63ORicNtsjaVp1ju2XpRGmtoXfY4yk6wXfb0mTRozfxmed8ag/640?wx_fmt=png&from=appmsg)

我们把匿名token拼接在web接口上

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34w54bBvC9p1TuYnicjQaQE6Ex28oyxHAiaDaaD8obmTzSMSPAPHo70UBics1RV1MVjRnqFRGDPhxRu6w/640?wx_fmt=png&from=appmsg)

如果没有token，是提示401的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34w54bBvC9p1TuYnicjQaQE6Em6eIDHhhCQaic9icaZTcW68Sic8Kou7VgL5mleDjhLc1icILYLiazAb2JSw/640?wx_fmt=png&from=appmsg)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj6mvgKoAUx8erw2mI4mkfwHowtRWQ9bUtrkvyycRE8yPznfChIIQEmWh10eic5ibywjLrB4X1kRNApA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

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