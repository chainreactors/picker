---
title: postMessageXss续2 - 飘渺红尘✨
url: https://www.cnblogs.com/piaomiaohongchen/p/18305112
source: 博客园 - 飘渺红尘✨
date: 2024-07-17
fetch_date: 2025-10-06T17:41:24.295480
---

# postMessageXss续2 - 飘渺红尘✨

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/piaomiaohongchen/)

# [飘渺红尘](https://www.cnblogs.com/piaomiaohongchen)

## 永远年轻永远热泪盈眶,永远在路上 星光不问赶路人,时光不负有心人

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/piaomiaohongchen/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E9%A3%98%E6%B8%BA%E7%BA%A2%E5%B0%98%E2%9C%A8)
* 订阅
* [管理](https://i.cnblogs.com/)

# [postMessageXss续2](https://www.cnblogs.com/piaomiaohongchen/p/18305112 "发布于 2024-07-16 15:37")

原文地址如下:<https://research.securitum.com/art-of-bug-bounty-a-way-from-js-file-analysis-to-xss/>

   在19年我写了一篇文章，是基于postMessageXss漏洞的入门教学:<https://www.cnblogs.com/piaomiaohongchen/p/14727871.html>

   这几天浏览mXss技术的时候，看到了一篇postMessaage的分析文章，觉得不错，遂翻译写成文章，每一次好的文章翻译，都是一次很好的学习的机会。生硬的translate，对技术提升没有任何帮助，这里我以第一视角代入翻译此篇文章，加入自己对漏洞的理解。

   这篇文章的难点在于对source的构造。

   正文内容如下:

   在研究期间，我决定查看 tumblr.com 主页，计划是查看它是否处理任何 postMessages。我发现 cmpStub.min.js 文件中有一个有趣的函数，它不检查 postMessage 的来源。在模糊形式下，它如下所示：

```
            var e = !1;
            function t(e) {
                var t = "string" == typeof e.data
                  , n = e.data;
                if (t)
                    try {
                        n = JSON.parse(e.data)
                    } catch (e) {}
                if (n && n.__cmpCall) {
                    var r = n.__cmpCall;
                    window.__cmp(r.command, r.parameter, function(n, o) {
                        var a = {
                            __cmpReturn: {
                                returnValue: n,
                                success: o,
                                callId: r.callId
                            }
                        };
                        e && e.source && e.source.postMessage(t ? JSON.stringify(a) : a, "*")
                    })
                }
            }
```

  为了方便理解，把代码丢入webstorm，webstorm会有高亮提醒:

![](https://img2024.cnblogs.com/blog/1090320/202407/1090320-20240716135026838-1337669902.png)

 通过我的截图标记，我们知道这是个套娃行为，他的可控source点的套娃行为如下:

```
e.data <- n <- n.__cmpCall <- r <- r.command && r.parameter
```

如果要本地模式这种套娃行为，那么这种source套娃模拟就是如下:

```
data= '{"name":"admin","list":{"test1":"test12","test2":"test2"},"age":16}'
// data='123'
var n = JSON.parse(data);
console.log(n.list.test1)
```

![](https://img2024.cnblogs.com/blog/1090320/202407/1090320-20240716135625304-22578046.png)

 两个逻辑处理分支:

```
(1)n = JSON.parse(e.data)
(2)window.__cmp(.,.,.xxx
```

 第一个是使用parse函数把我们监听接收的数据从JSON 字符串转换为 JavaScript 对象，说明我们传递的source是个json字符串

 source套娃点，会传入\_\_cmp(函数，跟进这个函数:

```
     if (e)
                return {
                    init: function(e) {
                        if (!l.a.isInitialized())
                            if ((p = e || {}).uiCustomParams = p.uiCustomParams || {},
                            p.uiUrl || p.organizationId)
                                if (c.a.isSafeUrl(p.uiUrl)) {
                                    p.gdprAppliesGlobally && (l.a.setGdprAppliesGlobally(!0),
                                    g.setGdpr("S"),
                                    g.setPublisherId(p.organizationId)),
                                    (t = p.sharedConsentDomain) && r.a.init(t),
                                    s.a.setCookieDomain(p.cookieDomain);
                                    var n = s.a.getGdprApplies();
                                    !0 === n ? (p.gdprAppliesGlobally || g.setGdpr("C"),
                                    h(function(e) {
                                        e ? l.a.initializationComplete() : b(l.a.initializationComplete)
                                    }, !0)) : !1 === n ? l.a.initializationComplete() : d.a.isUserInEU(function(e, n) {
                                        n || (e = !0),
                                        s.a.setIsUserInEU(e),
                                        e ? (g.setGdpr("L"),
                                        h(function(e) {
                                            e ? l.a.initializationComplete() : b(l.a.initializationComplete)
                                        }, !0)) : l.a.initializationComplete()
                                    })
                                } else
                                    c.a.logMessage("error", 'CMP Error: Invalid config value for (uiUrl).  Valid format is "http[s]://example.com/path/to/cmpui.html"');
// (...)
```

代码臭长臭长的，不要管，只要抓住重点

(1)在javascript中当出现n.x.y或者n.x.y.z说明是套娃+套娃，跟紧咬死source点

(2)寻找潜在风险函数

![](https://img2024.cnblogs.com/blog/1090320/202407/1090320-20240716140249301-498383961.png)

发现有个if逻辑判断，如果不为真，就else输出报错，那么这里要想办法让条件为真，跟进isSafeUrl函数:

```
isSafeUrl: function(e) {
           return -1 === (e = (e || "").replace(" ",
           "")).toLowerCase().indexOf("javascript:")
}
```

正常我们写代码都是function isSafeUrl(x) 。这是两种不同的写法，效果类似，一种是对象方法定义，一种是直接函数说明。

 这段逻辑代码很好理解:如果输入的字符串中不包含"javascript:"，函数返回 true;如果包含，返回 false。

 这里想返回真，那么我们就不能包含javascript:字符串，他这么做是为了防止xss攻击。做过一些代码审计的朋友应该都知道，使用包含这种黑名单的修复手法，是很危险的，是很容易被绕过的。

 那么这里的包含，为后面的利用留下了伏笔。我们继续往下研究，假设我们不包含javascript:字符串，为真了，会触发下面的逻辑处理代码:

![](https://img2024.cnblogs.com/blog/1090320/202407/1090320-20240716140930237-1076361796.png)

  通过不断的debug进入逻辑处理函数，发现一个可疑逻辑处理函数

```
 e ? l.a.initializationComplete() : b(l.a.initializationComplete)
```

  跟进b函数:

```
         b = function(e) {
            g.markConsentRenderStartTime();
            var n = p.uiUrl ? i.a : a.a;
            l.a.isInitialized() ? l.a.getConsentString(function(t, o) {
                p.consentString = t,
                n.renderConsents(p, function(n, t) {
                    g.setType("C").setGdprConsent(n).fire(),
                    w(n),
                    "function" == typeof e && e(n, t)
                })
            }) : n.renderConsents(p, function(n, t) {
                g.setType("C").setGdprConsent(n).fire(),
                w(n),
                "function" == typeof e && e(n, t)
            })
```

![](https://img2024.cnblogs.com/blog/1090320/202407/1090320-20240716141446313-1030288719.png)

在这里，将触发真正的sink点:n.renderConsents(p, function(n, t) {，跟进对应函数:

```
 sink:
                    renderConsents: function(n, p) {
                        if ((t = n || {}).siteDomain = window.location.origin,
                            r = t.uiUrl) {
                            if (p && u.push(p),
                                !document.getElementById("cmp-container-id")) {
                                (i = document.createElement("div")).id = "cmp-container-id",
                                    i.style.position = "fixed",
                                    i.style.background = "rgba(0,0,0,.5)",
                                    i.style.top = 0,
            ...