---
title: 一个括号都不给，我照样让页面弹了窗
url: https://mp.weixin.qq.com/s/AnWYvQlY3qt0SOVL8J-WFg
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:57:09.615981
---

# 一个括号都不给，我照样让页面弹了窗

# 一个括号都不给，我照样让页面弹了窗

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

> 导语：这篇聊个老话题，但玩法一点不过时，注入点能塞 JS，括号和分号却被 WAF 全拉黑，这时候 XSS 还有没有戏？我会从 `onerror` 加 `throw` 这对老搭档讲起，一路拆到把浏览器报错当成代码执行，最后看两位同行怎么把字符串和 `throw` 也一并省掉。不用背 payload，把弯拐明白，下次碰到奇怪的过滤规则你自己就能凑出一条链。

---

干了十来年渗透，我有个毛病：遇到过滤规则特别刁的站，比真弹出个框还兴奋。

那回碰上的站就是这么个货色。注入点确认能进 JS，可括号、分号一提交就被拦，alert(1) 连服务器都到不了。我在那儿盯了半宿，脑子里翻来覆去就一句话【谁规定调函数非得用括号？】

还真没人规定。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGEGqVUwjqJ3hJvIh4jx4k9O4ILpwiapW1JyBKcV4n9aauEkichyIiacdibURpoILBvxkhOtMAOsmfnFmtnL4X0VCyBaffE6wic1F1qk/640?wx_fmt=png&from=appmsg)

## 先认识一下那位"值班的接警员"

浏览器里有个 window.onerror，页面上只要冒出没人接的异常，它就会被叫起来，顺手把报错信息递过去。而 throw 这东西，说白了就是自己按警铃，还能顺带塞点东西进去。

于是两个一拼，就有了最原始的那条：

```
onerror=alert;throw 1337
```

把接警员换成 alert，再故意扔个异常出去，弹窗就来了。全程没出现一对括号。

只不过浏览器会在报警单上自动印个抬头，Chrome 印的是 Uncaught，所以弹出来的其实是 Uncaught 1337。这个抬头看着碍事，待会儿偏偏是它帮了大忙。

还有个细节：throw 是语句，前面那句赋值得用分号断开，不然会被当成一个表达式。可分号也被拉黑了呀。

## 分号没了，花括号顶上

第一反应是找个东西把两条语句隔开，又不许用分号。JS 里花括号能单独围出一个块语句，块一结束，后面直接跟 throw 就行，连换行都省了：

```
{onerror=alert}throw 1337
```

能用，但不够漂亮。我当时就想，能不能连这个块都不要。

能。throw 后面接的是表达式，而逗号运算符可以把一串表达式串起来，只把最后一个的值交出去。那把赋值塞进 throw 里不就完了：

```
throw onerror=alert,'some string',123,'haha'
```

从左到右依次执行，最后 'haha' 被扔出去，接警员已经被换成 alert 了。读起来像一句绕口令，跑起来一点不含糊。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGGaWJTYFoUEmUVKOFXPLFoq2y0DGypFDvH0OIuG2sTs30ZjxsDc5pjFLiaia512pjPUD8bbicEAfz62gPbK7YFavZr5ewMd7ZLm0g/640?wx_fmt=png&from=appmsg)

## 把报警单当代码念一遍

真正让这招从"弹个框"变成"想干啥干啥"的，是把 onerror 换成 eval。

```
{onerror=eval}throw'=alert\x281337\x29'
```

\x28、\x29 是左右括号的十六进制写法，过滤器扫的是字面上的 ( 和 )，它不认这串转义，JS 引擎认。

关键在下一秒。Chrome 给这句加上抬头，递到 eval 手里的字符串是：

```
Uncaught=alert(1337)
```

那个烦人的 Uncaught，被前面补的一个 = 变成了赋值语句左边的变量名，后半截就成了要执行的表达式。eval 老老实实把这行报警单当代码念了一遍，框就弹了。

我当时看到这儿是真的乐了：白送的报错抬头，居然能拿来当变量名使。

## 换个浏览器，当场翻车

Firefox 不这么玩。它印的抬头是 uncaught exception，两个词，中间还带空格。拼出来成了 uncaught exception=alert(1337)，语法直接崩。

顺手记一个新手常踩的坑：这套东西在 DevTools 控制台里直接敲 throw 是不灵的，异常被控制台自己接走打印了，压根轮不到 onerror。想复现，老老实实存个 html 文件打开。

那 Firefox 这边怎么绕？得让报错信息别带那两个词。

有个现成的路子：抛一个 Error 对象出去，Firefox 的报错就只剩 Error: 我的内容。巧的是 Error: 在 JS 里是个合法标签，后面直接跟代码就行。可 new Error(...) 得用括号，又绕回死胡同了。

那就造个假的。

我拿 Hackability Inspector 把 Error 对象翻了个底朝天，看它身上都挂了哪些属性，一股脑塞进对象字面量里，结果成了。然后一个一个往下删，删到不能再删，剩下四个就够：

```
{onerror=eval}throw{lineNumber:1,columnNumber:1,fileName:1,message:'alert\x281\x29'}
```

Firefox 看见这几个字段，就把它当成一个正经错误，message 原样递给 eval，alert(1) 执行。连 fileName 都能利用，它会作为第二个参数送到处理函数，两个参数一次到位：

```
{onerror=prompt}throw{lineNumber:1,columnNumber:1,fileName:'second argument',message:'first argument'}
```

补一句后来的事：Firefox 前阵子把"抛仿 Error 对象"这条路给堵了，这边又补了个不用括号构造真 Error 的写法：

```
throw onerror=eval,x=new Error,x.message='alert\x281\x29',x
```

老技巧没死，只是得跟着浏览器一起长。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGEVMve4xyZcrRSuFr0ibLUKjZBNLafyGtgZtS9mAibuydMkCvT4lM7JDjhyWTk5YGnenoGjzwYA1s5M4jKa58mDUs11dEOv46hibY/640?wx_fmt=png&from=appmsg)

## 两位同行把活干绝了

这套东西发到推上没多久，我的另外两个好友就各甩了一条更狠的。

先看 A 的，连字符串字面量都给你戒了：

```
throw/a/,Uncaught=1,g=alert,a=URL+0,onerror=eval,/1/g+a[12]+[1337]+a[13]
```

别被这一长串吓着，拆开特别有意思：

* 开头 `/a/` 是个正则，纯粹用来顶掉 `throw` 后面必须有的空格，顺手占个位；
* `Uncaught=1`

  提前把 Chrome 要印的那个词声明成变量，免得待会儿报 `ReferenceError`；
* `g=alert`

  给函数起个短名；
* `a=URL+0`

  是全场最妙的一手。`URL` 是个内置函数，函数加 0 会被转成字符串 `function URL() { [native code] }0`，数到第 12、13 位，正好是 `(` 和 `)`——等于从浏览器的自我介绍里偷了一对括号出来，自己一个字都没写；
* 最后 `/1/g` 正则转字符串是 `/1/g`，`[1337]` 数组转字符串是 `1337`，加上偷来的那对括号，拼出 `/1/g(1337)`。

Chrome 一盖抬头，报错变成 Uncaught /1/g(1337)。这回 / 不再是正则，而是除法：Uncaught / 1 / g(1337)。g 就是 alert，弹窗。

B 更绝：连throw都不用了。

```
TypeError.prototype.name ='=/',0[onerror=eval]['/-alert(1)//']
```

思路换了个方向，不自己按警铃，让浏览器自己出错，还顺便替我们把报警单写好。

TypeError.prototype.name 是可以改的，改成 =/ 之后，任何类型错误的开头都变成 Uncaught =/。后面 0[onerror=eval] 在方括号里顺手完成赋值，等价于对数字 0 取一个不存在的属性，拿到 undefined；再往 undefined 上取一次属性，TypeError 必然触发。

于是 eval 收到的差不多是这么一句：

```
Uncaught =/: Cannot read properties of undefined (reading '/-alert(1)//')
```

= 把 Uncaught 变成赋值左边，紧跟着的 / 开了一个正则，把中间那堆英文全吞进去，直到撞上属性名里第一个 / 才收口；后面的 -alert(1) 就成了一句正经表达式，// 再把尾巴注释掉。不用 throw，报错本身就是代码。

别把这几条当万能钥匙收进收藏夹就完事

报错文案是浏览器给的，人家改过好几轮。那条在较新的 Chrome 上常会栽在报错文本里的那个 ( 正则被撑成了未闭合分组，属性名前补一个 ) 才顺；Firefox 的报错又不在 name 前印 Uncaught，得自己先垫个变量名，=/ 直接写会语法错。前面提到的 Firefox 堵掉仿 Error 对象，也是同一类事。

真到了项目里，我的顺序一直是：先看清注入点落在哪个上下文（标签里、属性里、还是 JS 字符串里），再摸一遍 CSP 和过滤黑名单，最后才挑链子。把"报错能当代码""函数能不带括号调用""被禁的字符能从运行时拼出来"这几个弯装进脑子，比存一百条 payload 顶用得多。

也啰嗦一句规矩：这些只在自家环境或授权范围里复现，赏金项目按 scope 来，别拿别人的站练手。挖洞这行，边界感比技术值钱。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGFkYaAnAuyzRmD1b4GqIeA521ibNREqUnbDSv04FzCycZfqqG1Qc0DFeo9UUnL4bmicOYJBrmNQ7uW6p0ApHjA6VNK9CHNRHlsnw/640?wx_fmt=png&from=appmsg)

说到底，安全里最值钱的从来不是那串字符，是"报错单也能当命令行"这种拐了个弯的念头。

---

今天就写到这儿，这类"老技巧、新拆法"的笔记我还会陆续更。

觉得有用，顺手点个赞、点个推荐；想接着看，就关注一下不迷路；身边要是有正卡在过滤规则上半宿的兄弟，转发给他，能省一顿熬夜。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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