---
title: 攻防中前端加密的分析与突破
url: https://mp.weixin.qq.com/s/UfGnWAmeYZH53fTDPH23dw
source: Doonsec's feed
date: 2026-03-18
fetch_date: 2026-03-19T04:16:14.926862
---

# 攻防中前端加密的分析与突破

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RDiaL6j1Wgd69Ur2oib9H2hSCtYVZiaHEGAuSudIPDht5L8iaCeDP2Np1KODXEzPPNq8z9yor70MZh7pL5sk48bOa425ib5hwLLibW6tFIz2NH6SI/0?wx_fmt=jpeg)

# 攻防中前端加密的分析与突破

原创

尘佑不尘
尘佑不尘

泷羽Sec-尘宇安全

![]()

在小说阅读器中沉浸阅读

# 案例一

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7tHqpSZMqic0ibKdXgtUc5rILgfiafMYGiannlbosuheicicQdftWHWhUIlWTr3tkYZEMeq9ExAfCBY7CibAJDHr5rFfM9IoH3oLD17o/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd6VzpGov9Ow5cBuo8DH3oCwPhnZG9iboqRVibib5feNmaibQw8ibyYaeuEe9zPcTF11FM2r69PwFib2sYRJu3Ns0WnBMI9DX4zuXVZe4/640?wx_fmt=png&from=appmsg)

题目的意思就是要把20页里面的current\_array数组里面的值全部加起来，但是get请求里面有一个sign参数是不断变化的，就需要逆向出sign的加密逻辑，再用脚本爬取current\_array数组进行相加

找加密位置的3种方法：

方法一：既然知道了加密参数，那么找加密地点最快的方法就是直接全局搜索js文件里面含有sign参数的位置

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd4C2YIib3hsWicicwG9ic3wqhoSmqicB36uMqlUz0ZfjbJR1UQAOxiakNNVuhNjXGFicGb3lOUmhXphiclRm5f8RWicqpH1WyicQ2AeZYQ4w/640?wx_fmt=png&from=appmsg)

直接在这里下一个断点看看是不是加密后的位置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd5vvva8icjxaQZx0PKDORjueiaB1JuknicWWdVicXrEhlOT9ibETYdmNbMyboUyLBHorGm4uP2yGFnXUvl3SLJzpGZXPxIPxsAfJswo/640?wx_fmt=png&from=appmsg)

可以发现确实是

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7GLzOeqjgBHMBoABjnwgZmYwYctNjZeaibWJvhAQ1XiaRMMzgaMZU7CDrlhzeftVdUC4UPpZdaFYSCbcc330SmajxdpeHjCCDbA/640?wx_fmt=png&from=appmsg)

方法二：xhr打断点，找一个标志性的特征，一般选择url后的路由

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7FbB9lStqFdM6X94iaib6ia3dljaTCk9icQDkUbnhzbCQ5CzAaoYBCljKicr7LC35uZo7vpicMawiawEeP0E6iaXSUdpbf2qES5lP8fP8/640?wx_fmt=png&from=appmsg)

点击加号添加

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd4JgmpibEk6NwttdIIbwSBJNd4pRIZChibt8EYceicK9rBzAOL8eFvxCuUtr0XU7qVTaJhicV3JKblTBIdsc6WY70iaiaViaVzkZFt3ak/640?wx_fmt=png&from=appmsg)

刷新界面即可断住

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd5ic5WV1vKbVpT9C6hDABLI24c3ZM84v6ib8wQjWboaMNr8IiavMib4ibBg59PzSBu3Diasdb5iaiaqoMEk6NQFqyHdicCCeES9R5icM6tTQ/640?wx_fmt=png&from=appmsg)

方法三：启动器入手，从加载页面的这个js入手

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd5egeRqzT0dUmnibYgzNFGeCibe8GKEkXSSj2oKW338xvZfkEqgWochOyflevJSLbN9qVeA0MQ5jLSDiaU0X3cnwZVD4nE6Xf7vjc/640?wx_fmt=png&from=appmsg)

点击即可跳转到这儿

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd76AI1Oic4eVJ23ZLLnAC3c1d9gkDQ9RmgmAMjRjqjxJgriconC7I22kucJaaStT4P1U5MbgYIicfzJpzaNWu7LNM9oVextWyE0dY/640?wx_fmt=png&from=appmsg)

打上断点，刷新界面，即可发现加密位置

那么我们就可以从js代码中获取这些信息

```
sign=window.token
window.token = window.md5("tuling" + timestamp + pageNumber)  //MD5加密，tuling为盐值
const timestamp = new Date().getTime()
pageNumber    //参数为页数
```

加密所需要的参数及加密方式已经确定了

接下来可以扣js代码了,大致的逻辑就是这样了，接下来看看还缺什么参数接着扣

```
function get_sign(pageNumber) {
    const timestamp = new Date().getTime()
    const sign = window.md5("tuling" + timestamp + pageNumber)
    console.log(sign)
}
```

![](https://mmbiz.qpic.cn/mmbiz_png/RDiaL6j1Wgd7V1eHAabojMtejrPSnTJTTgbgs6Lz9FVItMmibRM7AoKBoDqxYXibWBYhibdPkD0vjsbNKgwMScPthS6KXUyQjm4Bh19j45jURNE/640?wx_fmt=png&from=appmsg)

MD5加密在我们本地肯定是没有的，但是它的js代码对MD5加密进行了重写，那我们只需要把window方法也给扣下来即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RDiaL6j1Wgd7pqBpACttqKqZjOU8PCCtLPrgRB7O1FhxUpCOFXNG2amIJQgiapyiayKonRiadWwfgv9rMf91B0D9ib40rLOcl6JvYDtjmAjjQ7qQ/640?wx_fmt=png&from=appmsg)

最终代码如下：

```
window = this, function (n) {
    function r(n, r) {
        var t = (65535 & n) + (65535 & r);
        return (n >> 16) + (r >> 16) + (t >> 16) << 16 | 65535 & t
    }

    function t(n, t, o, u, e, c) {
        return r(function (n, r) {
            return n << e | n >>> 32 - e
        }(r(r(t, n), r(u, c))), o)
    }

    function o(n, r, o, u, e, c, f) {
        return t(r & o | ~r & u, n, r, e, c, f)
    }

    function u(n, r, o, u, e, c, f) {
        return t(r & u | o & ~u, n, r, e, c, f)
    }

    function e(n, r, o, u, e, c, f) {
        return t(r ^ o ^ u, n, r, e, c, f)
    }

    function c(n, r, o, u, e, c, f) {
        return t(o ^ (r | ~u), n, r, e, c, f)
    }

    function f(n, t) {
        var f, i, a, h, g;
        n[t >> 5] |= 128 << t % 32, n[14 + (t + 64 >>> 9 << 4)] = t;
        var l = 1732584193, d = -271733879, v = -1732584194, C = 271733878;
        for (f = 0; f < n.length; f += 16) d = c(d = c(d = c(d = c(d = e(d = e(d = e(d = e(d = u(d = u(d = u(d = u(d = o(d = o(d = o(d = o(a = d, v = o(h = v, C = o(g = C, l = o(i = l, d, v, C, n[f], 7, -680876936), d, v, n[f + 1], 12, -389564586), l, d, n[f + 2], 17, 606105819), C, l, n[f + 3], 22, -1044525330), v = o(v, C = o(C, l = o(l, d, v, C, n[f + 4], 7, -176418897), d, v, n[f + 5], 12, 1200080426), l, d, n[f + 6], 17, -1473231341), C, l, n[f + 7], 22, -45705983), v = o(v, C = o(C, l = o(l, d, v, C, n[f + 8], 7, 1770035416), d, v, n[f + 9], 12, -1958414417), l, d, n[f + 10], 17, -42063), C, l, n[f + 11], 22, -1990404162), v = o(v, C = o(C, l = o(l, d, v, C, n[f + 12], 7, 1804603682), d, v, n[f + 13], 12, -40341101), l, d, n[f + 14], 17, -1502002290), C, l, n[f + 15], 22, 1236535329), v = u(v, C = u(C, l = u(l, d, v, C, n[f + 1], 5, -165796510), d, v, n[f + 6], 9, -1069501632), l, d, n[f + 11], 14, 643717713), C, l, n[f], 20, -373897302), v = u(v, C = u(C, l = u(l, d, v, C, n[f + 5], 5, -701558691), d, v, n[f + 10], 9, 38016083), l, d, n[f + 15], 14, -660478335), C, l, n[f + 4], 20, -405537848), v = u(v, C = u(C, l = u(l, d, v, C, n[f + 9], 5, 568446438), d, v, n[f + 14], 9, -1019803690), l, d, n[f + 3], 14, -187363961), C, l, n[f + 8], 20, 1163531501), v = u(v, C = u(C, l = u(l, d, v, C, n[f + 13], 5, -1444681467), d, v, n[f + 2], 9, -51403784), l, d, n[f + 7], 14, 1735328473), C, l, n[f + 12], 20, -1926607734), v = e(v, C = e(C, l = e(l, d, v, C, n[f + 5], 4, -378558), d, v, n[f + 8], 11, -2022574463), l, d, n[f + 11], 16, 1839030562), C, l, n[f + 14], 23, -35309556), v = e(v, C = e(C, l = e(l, d, v, C, n[f + 1], 4, -1530992060), d, v, n[f + 4], 11, 1272893353), l, d, n[f + 7], 16, -155497632), C, l, n[f + 10], 23, -1094730640), v = e(v, C = e(C, l = e(l, d, v, C, n[f + 13], 4, 681279174), d, v, n[f], 11, -358537222), l, d, n[f + 3], 16, -722521979), C, l, n[f + 6], 23, 76029189), v = e(v, C = e(C, l = e(l, d, v, C, n[f + 9], 4, -640364487), d, v, n[f + 12], 11, -421815835), l, d, n[f + 15], 16, 530742520), C, l, n[f + 2], 23, -995338651), v = c(v, C = c(C, l = c(l, d, v, C, n[f], 6, -198630844), d, v, n[f + 7], 10, 1126891415), l, d, n[f + 14], 15, -1416354905), C, l, n[f + 5], 21, -57434055), v = c(v, C = c(C, l = c(l, d, v, C, n[f + 12], 6, 1700485571), d, v, n[f + 3], 10, -1894986606), l, d, n[f + 10], 15, -1051523), C, l, n[f + 1], 21, -2054922799), v = c(v, C = c(C, l = c(l, d, v, C, n[f + 8], 6, 1873313359), d, v, n[f + 15], 10, -30611744), l, d, n[f + 6], 15, -1560198380), C, l, n[f + 13], 21, 1309151649), v = c(v, C = c(C, l = c(l, d, v, C, n[f + 4], 6, -145523070), d, v, n[f + 11], 10, -1120210379), l, d, n[f + 2], 15, 718787259), C, l, n[f + 9], 21, -343485551), l = r(l, i), d = r(d, a), v = r(v, h), C = r(C, g);
        return [l, d, v, C]
    }

    function i(n) {
        var r, t = "", o = 32 * n.length;
        for (r = 0; r < o; r += 8) t += String.fromCharCode(n[r >> 5] >>> r % 32 & 255);
        return t
    }

    function a(n) {
        var r, t = [];
        for (t[(n.length >> 2) - 1] = void 0, r = 0; r < t.length; r += 1) t[r] = 0;
        var o = 8 * n.length;
        for (r = 0; r < o; r += 8) t[r >> 5] |= (255 & n.charCodeAt(r / 8)) << r % 32;
        return t
    }

    function h(n) {
        var r, t, o = "0123456789abcdef", u = "";
        for (t = 0; t < n.length; t += 1) r = n.charCodeAt(t), u += o.charAt(r >>> 4 & 15) + o.charAt(15 & r);
        return u
    }

    function g(n) {
        return unescape(encodeURIComponent(n))
    }

    function l(n) {
        returnfunction (n) {
            return i(f(a(n), 8 * n.length))
        }(g(n))
    }

    function d(n, r) {
        returnfunction (n, r) {
            var t, o, u = a(n), e = [], c = [];
            for (e[15] = c[15] = void 0, 16 < u.length && (u = f(u, 8 * n.length)), t = 0; t < 16; t += 1) e[t] = 909522486 ...