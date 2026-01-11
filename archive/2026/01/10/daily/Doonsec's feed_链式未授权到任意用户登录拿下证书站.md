---
title: 链式未授权到任意用户登录拿下证书站
url: https://mp.weixin.qq.com/s/yWYUefqWMJI0-sezI3ys3w
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:39:33.539057
---

# 链式未授权到任意用户登录拿下证书站

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkUxKGvPall7yhB2KYAFkXLPu26EhrqXgPAeA91IlAblAVjWDiaBAjkjQ/0?wx_fmt=jpeg)

# 链式未授权到任意用户登录拿下证书站

原创

zkaq-bielang

掌控安全EDU

![]()

在小说阅读器中沉浸阅读

扫码领资料

获网安教程

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BwqHlJ29vcpWCJgOGbsEvLDiaWKNibMPoftC4gYTibHo0F3gr0bvL0wNSu5bbvbLUiadN2KSKac8GUDP9wwMMr4pjA/640?wx_fmt=jpeg&from=appmsg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

# 本文由掌控安全学院 - **bielang** 投稿

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn**）****

# 一.前言

本文涉及的相关漏洞均已修复、本文中技术和方法仅用于教育目的；

文中讨论的所有案例和技术均旨在帮助读者更好地理解相关安全问题，并采取适当的防护措施来保护自身系统免受攻击。

# 二.大概流程

1. 1. **入口获取**：通过已获得的统一身份认证账号密码登录系统，进入目标子系统。
2. 2. **存储型XSS漏洞挖掘与利用**：

* • 发现附件上传功能，前端仅做了JS校验；
* • 通过Burp Suite改包绕过前端限制，实现任意文件上传；
* • 上传HTML文件（如XSS payload）但无法解析 jsp；
* • 通过分析前端JS代码发现图标资源路径，拼接出上传文件的访问URL，成功触发XSS。

1. 1. **未授权访问漏洞（文件删除与信息泄露）**：

* • 使用工具（如findsomething、LoveJS）提取JS中的接口，并配合手工审计；
* • 发现 `**/detail?id=**` 接口存在未授权遍历，可获取敏感文件信息；
* • 发现 `**/delete?id=**` 接口存在未授权删除风险（未实际测试）；
* • 发现工单查询接口未授权泄露用户学号、姓名、手机号等敏感信息。

1. 1. **未授权访问漏洞（任意用户登录）**：

* • 通过泄露的手机号，调用 `**/getUserByPhone?phone=**` 接口未授权获取用户密码（明文或可逆加密）；
* • 结合泄露的学号、手机号及密码，实现任意用户登录。

1. 1. **JS逆向获取超管权限**：

* • 发现子系统独立登录口（非CAS集成），但统一账号无法直接登录；
* • 分析登录请求中的加密参数，通过JS逆向获取加密逻辑；
* • 使用Burp插件（如cloudx）实现自动化加密，对账号密码进行爆破；
* • 成功爆破出管理员账号密码，登录后台并发现多处XSS漏洞。

# 三.正文

之前的证书站好久没发货了，所以想挖点其他的证书，顺便上上 rank，于是有了这篇文章。

前言：拥有了某大学的统一身份认证权限（账号密码），进入统一之后发现系统很多，点开一个一个测试，最后在某个子系统发现了漏洞：

# 存储 xss

子系统下有一个附件上传的点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkdyJiavqlahquMia94libTt7uEiaBQ3y3P7NdQjyrs8a0hAxwjiaySzxUzwg/640?wx_fmt=png&from=appmsg "null")

前端 js 做了校验，所以上传 png 后 bp 改包发现任意文件上传，但是上传 shell 发现无法解析，这套系统是若依二开的，所以传上去也无法解析，就只能打 xss 了。

```
POST xx/xx/uploadImg HTTP/1.1
Host: xx.xx.edu.cn
Cookie:
Content-Length: 211
Sec-Ch-Ua-Platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Sec-Ch-Ua: "Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary1NKotycTLlciokiM
Sec-Ch-Ua-Mobile: ?0
Accept: */*
Origin:
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer:
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Priority: u=1, i
Connection: keep-alive

------WebKitFormBoundary1NKotycTLlciokiM
Content-Disposition: form-data; name="file"; filename="hack2.html"
Content-Type: image/html

<script>alert(1)</script>
------WebKitFormBoundary1NKotycTLlciokiM--
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkgs4LcRVlSZD5WTCq6UUrNjmtbo7NK5bDNnUaog3OGcxl7FHZG0o6Kw/640?wx_fmt=png&from=appmsg "null")

虽然传上去了，但是没有返回路径，尝试拼接了好几个接口都不行，而且这个时候只能从前端找一下静态资源文件，但是前端也没有图片之类的，但是运气很好，最后在 js 中发现一个 icon 的地址：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLk9LRMdduWBNlMCfdsj5yhWUia5ToS7bQ4TgEQ48MhpYB5SicP6y5zG9lA/640?wx_fmt=png&from=appmsg "null")

最终找到一个下载地址：

```
https://xxx.xxx.edu.cn/xxxx/xxx/24102xxxx.svg
```

改后面的文件名称为刚才上传的，成功触发：

```
https://xxx.xxx.edu.cn/xxxx/xxx/250821220651263926.html
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkSq3bGnwW0m1eqN8wYm0oKgZmE3vhHbcTHjUSia7tlibcjo2iaiclXWlzgA/640?wx_fmt=png&from=appmsg "null")

# 未授权 1 (文件删除)

刚开始我是使用了 `**findsomthing**` 和`**LoveJS V1.2****👋**`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLk5cMuKHNS0jTFur9Nv2RKhXjHgQFZsIJHJmHMP9AicN2a3WQ1ibWkZ5YQ/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkib6gian9iaZo6G7jYiatk0OBN7zjYeBnGRKoC5AZ21eAOn3w9wqJeFdfEQ/640?wx_fmt=png&from=appmsg "null")

提取接口然后 bp 跑了 get 和 post 请求，但是都没有什么泄露的信息。

最后还是自己审计 js 发现两个接口：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkPicVgZ4OqfykTGRLfHJehReQFOMSxYiczzwpk6y2pBtxyicpfLicCCVBPg/640?wx_fmt=png&from=appmsg "null")

```
/xxx/xxx/delete?id=    /删除接口

/xxx/xxx/detail?id=         /详情接口
```

使用 bp 跑详情接口：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkWBMGEj0tkqsibpY8XqHzicOy9vV1BJMBE68eiaibgcQCBDibLNvq15V8DaA/640?wx_fmt=png&from=appmsg "null")

可以发现是可以遍历出文件的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLk0K28ibpOpzS9msoUPBDIPkUFN14HHgeo79ticQuMibmeOGwRSFVmPBOIA/640?wx_fmt=png&from=appmsg "null")

同理，删除接口应该也存在这个问题，但是接口过于敏感，我并未测试

# 未授权 2（任意用户登录）

依旧是审计 js，发现`**?id**`这个参数很多，所以着重看了带这个的接口，最后发现一处可以未授权获得别人提交的工单 ：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkPBcXkEoguJiatlUibWribgYUiaiaQ2FlhVRJn7QVXqqha7DajAe4s0ucIVw/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkRIFgzB1iaA4PYEAbTygdjpn7h5xQBqbfd7GHmQo0stajhVT3zbNwC4A/640?wx_fmt=png&from=appmsg "null")

发现这个工单中是返回了当前 id 的学号、姓名、手机号以及工单信息。

然后想着还是没有太大危害，这个泄露的信息 edu 也不收，就只能继续看下去，因为看了好几个接口都存在未授权问题的话，那么这套系统大概率其他接口都存在这个问题，同时在上面我们获得了用户的学号和手机号，那么我的思路就是看看能不能从这两个字段搞到一些敏感信息，所以我检索了 xh 和 phone 这两个参数，最后检索到这样一个接口：

```
/xxx/xxxxx/getUserByPhone?phone=
```

很明显这个是获取用户详情的一个接口，于是使用上面获得的手机号跑一下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkXMCIibuXX1T6nVfkmn0Ogdd8R4uZQc4Qgsh8Bdhzf3wiaxNuf8srPUFg/640?wx_fmt=png&from=appmsg "null")

成功得到用户的密码。

# js 逆向到超管权限

刚开始我是从 cas 传递的令牌进入的这个系统，后面我退出登录后，发现它其实有单独的登录口，没有走 cas 的集成，但是统一的那个账号却在这里登录不上，显示无账号存在

```
https://xxx.xxx.edu.cn/login
```

所以感觉这里可能有弱口令，但是当前的登录口登录抓包发现存在加密：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkdd0StMsfATfXiaEBhaxJy6DWLm0jVibSbwK3zJTgsqJibGPicUUJITSQoQ/640?wx_fmt=png&from=appmsg "null")

这个时候其实不太想打了，因为上面的已经可以换到证书了，哈哈，但是从老大那里学到了 js 逆向，那就必须得逆一下咯。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkmP7YicqU4M1gptRibclibImNyxr69Vh55Zze6nQAkuVgIPx9XtdT5wYug/640?wx_fmt=png&from=appmsg "null")

验证没问题：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkNuhU1WicicQO40OL2Etb45TQODuHbLJiblnoYekKfS436RQNdeNo2W4uQ/640?wx_fmt=png&from=appmsg "null")

设置 bp 插件 cloudx：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLk7SFUQhUL1jV8dI9Poj44HnHict4a7f4GRosNOy6PlqJdheslkoS58CA/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkg2Rd8GTwicibkvpyDP0fQ2pEKOWZ96wllvYBadYJT4mDevzgOXz5DGRA/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLktR9mvgeNH5eHCSRgLYhl0eRglPGIn0ibgsTNUSs9DrsxUia1CYfD6Q6w/640?wx_fmt=png&from=appmsg "null")

接下来 就是发送到爆破模块去爆破账号了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkH9O4HBSF5msjCic1hp90XVJWRib5zicTBLruGSW7mWZZCibemeXrgubqCQ/640?wx_fmt=png&from=appmsg "null")

成功爆破出账号密码，登录后台：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkztGq2SuBhPd55vzE4EiaVufI6bC0ObM32da0m49Muib6uD95murhXiaQQ/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLkLdG09dRwbeua86ic14BoWE1ScZqPvhficOI5L7BziauRfrFDy0OsefWQw/640?wx_fmt=png&from=appmsg "null")

同时后台也有很多 xss 漏洞。

# 四.总结

最后也是如愿换到了证书：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrmiaoZ6wZOCVCHoINnU9CLk7sU9Afcrt1XNEHRFK9GRJtjeibYhUt41FLyVWiaZUEMJGicuKE3IzZdYQ/640?wx_fmt=png&from=appmsg "null")

总体难度不大，带点狗运，主要是审计 js 接口，有不对的地方请师傅们指正，感谢观看。

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

**没看够~？欢迎关注！**

**分享本文到朋友圈，可以凭截图找老师领取**

上千**教程+工具+交流群+靶场账号**哦

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BwqHlJ29vcpWCJgOGbsEvLDiaWKNibMPoftC4gYTibHo0F3gr0bvL0wNSu5bbvbLUiadN2KSKac8GUDP9wwMMr4pjA/640?wx_fmt=jpeg&from=appmsg)

**分享后扫码加我！**

**回顾往期内容**

[我与红队：一场网络安全实战的较量与成长](https://mp...