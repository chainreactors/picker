---
title: YTray 实战案例：隔离浏览器越权测试与加密桥接
url: https://mp.weixin.qq.com/s/SuXuB918VwSWqxen3H-K7w
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:54:08.277859
---

# YTray 实战案例：隔离浏览器越权测试与加密桥接

# YTray 实战案例：隔离浏览器越权测试与加密桥接

原创

Yak
Yak

Yak Project

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdUYXaiccQFYhEArmU3f9ef0VNmBjcyLt7PUV08libAc8EmnhuFSzlnIiaJThN911S7468pdssPD8hgw/640?wx_fmt=png&from=appmsg)

它不只是“帮 AI 看网页”的插件。连接 Yak 引擎并获得用户授权后，Yakit Browser Agent 可以把真实浏览器中的登录态、页面操作、网络请求、前端运行现场和人工交互，变成 AI Agent 能够调用的能力。

上一篇文章里，[YTray: 浏览器隔离与分身测试新神器](https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247530142&idx=1&sn=748ccd8d4e8f1b5a193a4b93b1fb2f3a&scene=21#wechat_redirect)我们介绍了 YTray 如何管理浏览器、插件、代理和相互隔离的用户环境，并且简单提了一嘴 YTray 内置的浏览器插件。

<点击下方卡片查看>

[![](https://mmbiz.qpic.cn/mmbiz_jpg/jibGAup6p72H37utv5hPoeAp7ZNw7hLibhWcydVa0RYhXQIBFmUtNKzn2rUKfWzRGeu8p0dJfvklCl5Y0143WNLTeeRATOa1Aic7Qla5oPCnU4/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247530142&idx=1&sn=748ccd8d4e8f1b5a193a4b93b1fb2f3a&scene=21#wechat_redirect)

这一次，我们不再重复介绍 YTray，而是直接回答一个更重要的问题：

**当浏览器插件连接 Yak 引擎之后，AI Agent 到底能做什么？**

与其罗列一长串技术名词，不如先简单介绍能力，再用几个真实案例看看它如何工作。

一、从“看见网页”，到“使用真实浏览器”

过去让 AI 分析网页，常见做法是截图、复制文字，或者把页面地址发到对话框里。

但真实任务往往没有这么简单：

* 页面需要登录，公开链接无法还原当前账号状态；

* 同时打开了多个浏览器、多个账号，AI 不知道应该使用哪一个；

* 页面操作会产生真实网络请求，其中还可能包含动态参数、签名或加密数据；

* 登录流程遇到扫码、MFA、验证码或设备确认，必须由用户本人参与；

* 安全测试需要比较不同身份，而不能把两个账号的 Cookie 混在一起。

Yakit Browser Agent 的作用，是在用户明确授权后，把这些真实浏览器能力连接到本地 Yak 引擎：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72Fk75X1qJ9WGBefPQKZzcsYPQ3iah72scmOIQU3HyqjhS7NCpDTf0fD5YzzqChTcjt7BPcd6bFQLUwlY7D7Hk78zUCFQSQ9yfTA/640?wx_fmt=png&from=appmsg)

插件的配对流程如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72GxAEiaBic5V4E80Mpo4eHq50QibK9QdLpv3hVRgOgLaQ7nzBgyianfXR9ic1ecMAI3tlyg0ichakCQmbCv2XFiblMKcOvEsGdsws3PKg/640?wx_fmt=png&from=appmsg)

接入后，AI Agent 可以在授权范围内：

* 识别在线浏览器、浏览器类型、版本和已经打开的页面；

* 阅读页面结构，定位按钮、表单和其他可交互元素；

* 协助点击、输入、滚动、打开标签页并判断页面状态变化；

* 捕获真实浏览器请求，继续交给 Yakit 分析或重放；

* 利用页面正在运行的函数和状态处理前端加解密；

* 遇到扫码、MFA、验证码或设备确认时暂停，并邀请用户接管；

* 在相互隔离的 A/B 浏览器身份之间完成授权差异测试。

浏览器完成配对和页面授权后，用户直接描述任务即可。

二、开始之前，先让 Agent 认清浏览器现场

我们先做了一个很简单的测试：同时连接两个浏览器实例，然后问 AI Agent：

当前两个实例分别打开了什么网站？

Agent 先查询在线浏览器实例，再分别调用两个实例的标签页能力。最终，它准确区分了：

* 实例 A：Google Chrome，打开的是百度；

* 实例 B：Chrome for Testing，打开的是 Yaklang 官网；

* 两个实例各自有多少标签页，哪个标签页处于活动状态。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72GLN0ibEuJzhb6SibU1Ciaib5nsBzf5iccXtEhCeJkCzFlYx3PcibwwGNltgZy62usyTwcrXu2kfLxebYTS2yUu1WSHKxytuZQOvlNY8/640?wx_fmt=png&from=appmsg)

AI Agent 分别读取实例 A、实例 B 的浏览器类型、页面标题和 URL。

这一步看似简单，却是后续复杂任务的基础。

AI Agent 面对的不再是一个模糊的“当前网页”，而是多个可以明确区分、登录状态互不干扰的真实浏览器现场。并且通过浏览器插件暴露的能力进行相关的操作，接下来，无论是多账号验证、请求分析还是人工接管，都可以在正确的实例中继续进行。

三、案例一：用 A/B 真实身份测试越权

***YAK***

**3.1 同一个资源，换一个账号还能不能访问？**

越权测试最容易出现的问题，是测试环境本身不可靠。

如果两个账号共用同一个浏览器 Profile，Cookie、缓存和登录状态可能互相污染；如果只复制一条请求修改参数，又很难证明请求仍然代表另一个真实身份。

YTray 可以启动两个相互隔离的浏览器环境：

* 浏览器 A 登录账号 A；

* 浏览器 B 登录账号 B；

* 两边分别完成一次相同的正常业务操作。

Yakit Browser Agent 会先检查两边的认证上下文是否真正隔离，再捕获双方最近一次同类业务请求，建立正常基线。

以水平越权测试为例，系统会形成四组对照：

1. 1. A访问 A 自己的资源；
2. 2. B访问 B 自己的资源；
3. 3. A 尝试访问 B 的资源；
4. 4. B尝试访问 A 的资源。

交叉测试只交换经过用户确认的资源字段，同时保留 A、B 各自真实的认证材料。Agent 再结合状态码、响应结构、业务字段和资源归属证据，整理出可以复核的差异。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72HZMVV2DoMz0Bw9QIIlBzBBB2f3xqGmCxDeCbA5sXxdvKQhsjhR4wUiaIYJEPaKo1OnIkHYcBGiaOPmO1b9jiarKUHjvSFHR2RgN4/640?wx_fmt=png&from=appmsg)

这里有一个很重要的原则：

**接口返回****`200`****，不代表一定存在越权。**

有些接口即使拒绝访问，也会返回统一的 `200`；有些响应看似成功，实际没有返回目标资源。因此，插件负责提供确定性的请求与响应证据，AI Agent 负责归纳和解释，最终仍由测试人员结合业务规则判断。

你可以直接告诉 Agent：

当前打开了两个实例，并且登录了两个不同权限的账号，帮我测试一下有没有越权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72GOCic7fNycT6RU5GNfLawKPepuYp4KvFWJibIh2TH3s5WkWj9AJicyrJ3LHzTu3dyYDqBcdEicYmayn5YsPajDB29ESLtoHOxric8k/640?wx_fmt=png&from=appmsg)

这个案例证明的不是“AI 会修改一个 ID”，而是它能够围绕两个真实身份组织测试、保留证据，并避免把猜测直接写成漏洞结论。

四、案例二：让 Web Fuzzer 编辑明文，让浏览器处理密文

这是前端加密场景中非常常见的问题。

用户在页面中输入的是明文，但真正发到服务器的内容，可能已经经过加密、签名、编码或多层封装。算法还可能依赖页面闭包、动态密钥、`CryptoKey`、Worker、WebAssembly，甚至某个正在运行的对象状态。

传统做法通常要花很多时间阅读混淆代码、寻找密钥、重写算法，再尝试在浏览器之外复现整条链路。

明文网关提供了另一种思路：

不急着把整个算法手工复刻，而是借助浏览器的上下文环境完成它原本就会做的事情。

一次典型流程是：

1.选中需要录制的 tab 页面，在真实页面中开始录制；

本次使用 vulinbox 的靶场 SQL 注入（从登陆到 Dump 数据库）http://localhost:8080/crypto/sqli/aes-ecb/encrypt/login

2. 完成一次尽可能短的登录、查询或提交操作；

登录时，尽可能的输入错误的用户名或密码，对于一些登录成功后，会发生页面跳转的地址，能很好的降低录入到其他页面事件

3.点击录入，登录页面尝试登录后，插件会显示整理页面输入、加解密调用和最终请求之间的时间线；

1. a.证据充分时生成明文网关,

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FrfnXy99Ws5KMRxaKeoxcDXIMDfpYsruRR3sOLejueCdvjp6LmDJFbGQEUf6n6uxK3as66YibgeJCE0KJrIgk6aFehciawticddc/640?wx_fmt=png&from=appmsg)

1. b.证据不足时提示进行深度捕获

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72GOL2R1VXgjA4pTfEM7ouG19awrEGnj38KiaNvC4bS0g5JMItGmGTosTZnFSFlExPI9yrr3nTDsC2cIpkNpULl8yHYGjmIianDAw/640?wx_fmt=png&from=appmsg)

此时会出现下图，可以发现插件使用了 浏览器的 debug 功能，深度捕获流程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72GLhmeH8akBH4B4jCsCnXSSfsQiaT2QCn4s6pjsHBF2CrpTNGBSIow1mrEZ7PE9Z1xMd0ItIQdOuBchVugW2ficPOAw1t0UqCSFs/640?wx_fmt=png&from=appmsg)

此时需要你返回登录页面，再次登录一次，如果成功，将会直接跳到明文网关tab 页面

4.查看生成的明文网关；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72FP3BsRNz2fOMRCbHUpold3UnQaPxzEaIdsB9eBlgSVU5cAzQSx4wUiayLUfXNPArFkrPiaTKjGfWOZk9B8mtJa3Oicu2EL6vIOYU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72FGK9eygeoeK3t5mRDvXmc9QUK3oUkfAJDZ9WRibjUUB8o5Pmc7BWqMTibG4BFRP0wdXqGqWYTorygblIugB8oM8iaFt8ibsKqSbRw/640?wx_fmt=png&from=appmsg)

可以发现这是一个请求和响应都有加密的登录

5.在 Web Fuzzer 中打开浏览器明文，选中我们刚才生成的明文网关，可以看到目前有两条（为了演示，实际两条都是同一个登录地址的明文网关），并且都是**请求**和**响应**都有的网关；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72HoZMUwMMbuAzpIOff48FUDnbq6icoFHa0oa4CiaTNxvyQsHIm5ziaicoKmR3r88nricyrn0cdWjWQd5RrthicP0AlgdnSfFgEKickDpA/640?wx_fmt=png&from=appmsg)

6.发送前，由当前浏览器页面生成服务器真正接受的密文、签名或请求封装；

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FXXBarBn27GdBh4LzbsGibrgYLwmvuasOanENPpmaJufic0qnUznzlrg7QQT064bGBpC0ZNyanZ48Iq8VQlpIdxkfuDDaoapZgs/640?wx_fmt=png&from=appmsg)

7.查看经过浏览器插件的前后数据情况，点击 明文/线上，可以发现我们发送的明文请求包，确实被插件的网关进行了加密处理

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72EVemYib6zh7rccLQbN98gcpjImGPXwXtfUku25MtsibAwo7QYxewKvluaHQe5Aic7xxibaWjAIMqVzyhr2ib6mK7BDDLfHm8nwnqCY/640?wx_fmt=png&from=appmsg)

返回包也一样的，被插件的网关进行了解密处理

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72FXac5iatLsm5xvd5DdYUI6L6zH6fDKo6te2jU3CIl919icujibparEszEw2DXClIFlsnqHkv9pCY0aLXCyv7RKVuetSlDL48iajKU/640?wx_fmt=png&from=appmsg)

试试输入错误的密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72HUTKfPHOTHCA9uq0VmktkNDhMn3XjVd4KPrSmicTU5JEkdndsTVu5icoNia6iabQ5qhHu1lsXT4icE0H3hjs13RIPt7gBF5ibhUvErU/640?wx_fmt=png&from=appmsg)

在这个过程中，测试人员可以并排查看：

* 自己编辑的明文请求；

* 浏览器实际发送的线上报文；

* 服务器返回的线上响应；

* 经过页面逻辑还原后的明文响应。

上述展示了手动情况下的插件能力，同理你可以让 AI Agent 协助你快速的分析，比如如下的简单话术：

我打开了实例A，你帮我测试一下加解密的靶场，并且我希望能看见明文网关，不需要每一个靶场都测试，就测试 第一个就行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72FFyfR9VNR0qHzUxaxqia25KQZlBhg3icCxEibOdqUL5oiaviaUIVZwib8epwiacEibIgAS9PiaJIAtmkQlM4sKOvATdRYzX7YkPtRP9ZiaY/640?wx_fmt=png&from=appmsg)

可以看到 AI Agent 也很好的借助了浏览器的明文网关，生成了 HTTP 流量

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72GILIdnNuTdq1zBGporsWWXa9jG9Q71L0yaDIbLGO70IGuyEbx5B1867EPI8ibyu8lqtElvDNnwXUJPUtheYjhX3sOfvZCsH99M/640?wx_fmt=png&from=appmsg)

我们打开 HTTP 请求中的 明文网关部分，可能看到如下的转换逻辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jibGAup6p72ECulVZsibtp2vTp3lLXYmcv7UZsBYbgTr4NvyS4mg5uy1YTY0hTOeVhIZgSdTwAC13Sb4AnNanbxbSXKFtxhNq7wTo7oE1MSPI/640?wx_fmt=png&from=appmsg)

五、案例三：遇到二维码登录，把操作权交还给用户

***YAK***

**5.1 自动化不应该试图绕过所有人工步骤**

扫码登录、MFA、验证码、设备确认，本来就是为了要求真实用户参与。

一个可靠的 Agent，不应该在这些环节继续“硬闯”，而应该知道什么时候暂停、把正确的页面呈现给用户，等用户完成后再继续任务。

在下面的案例中，我们直接告诉 AI Agent：

随便选择一个浏览器实例打开 B 站，我要扫码登录。

Agent 随后完成了这些步骤：

1. 1. 在浏览器实例A中新建标签页并打开B站；

1. 2.读取页面DOM，定位右上角登录入口；

1. 3.点击登录按钮，唤起二维码弹窗；

1. 4.发起二维码登录的人工接管任务；

1. 5.在Yakit中显示当前二维码和“等待扫码”状态；

1. 6.暂停执行，等待用户用手机完成确认；

1. 7.用户确认完成后，再重新读取页面状态并继续后续任务。

![](https://mmbiz.qpic.cn/mmbiz_png/jibGAup6p72Gu6pfIsNuQvibmuMxlJtf5BOB0XestwSleU9fWQo82Qdib2Wjajhha6b5icnV8GMJ2vwaXQUXr8jLpsNF2VIWaL4OWl1smpINK88/640?wx_fmt=png&from=appmsg)

Agent 完成页面导航与登录入口定位后发起 handoff，在用户扫码期...