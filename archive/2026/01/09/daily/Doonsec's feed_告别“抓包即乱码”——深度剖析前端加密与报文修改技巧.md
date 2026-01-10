---
title: 告别“抓包即乱码”——深度剖析前端加密与报文修改技巧
url: https://mp.weixin.qq.com/s/BluDT4RNzy13uhQm31iP6g
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:25:42.154604
---

# 告别“抓包即乱码”——深度剖析前端加密与报文修改技巧

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xkB4mPD62nPmzSLWHiaTJc1Mt0cWbdBwOBLvXv7zA5eYHboN4u2a2cfJ0uUuSbhzHjElQGCLiaP14uvBX7nORdFA/0?wx_fmt=jpeg)

# 告别“抓包即乱码”——深度剖析前端加密与报文修改技巧

原创

onttys000

T00ls安全

![]()

在小说阅读器中沉浸阅读

随着安全越来越卷，越来越多的站点对报文做了加密处理，不努力下次测试连个包都改不了

以某站点为例，对前端报文加密绕过处理做下总结

通过抓包可以看到网站对报文进行了加密处理

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPmzSLWHiaTJc1Mt0cWbdBwOZ2hIRBDPJ4HbaDXqmPHBrf0BicVJOiaHFPWZQnGs1lAOpz06yzDHkeuA/640?wx_fmt=png&from=appmsg)

针对这种前端报文加密的场景常考虑以下几种应对措施

```
1.分析加解密算法，流程，进行重写。密文=>解密=>加密
2.jshook，控制台操作
3.js rpc
```

以上三种方法，不可绕过的步骤都是前端加密逻辑分析。

### 加密逻辑分析

打开 F12 /开发者工具

浏览前端目录，一眼发现 security 目录，并且该目录下还存在 encrypt-sm.js /pnc-crypto-min.js 文件

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPmzSLWHiaTJc1Mt0cWbdBwOdGOib4POCOgHFrNybmwQBnpwibp1VicHZ8YicCZzicWlucdpVp57xoycbFw/640?wx_fmt=png&from=appmsg)

（没法一眼看出来的场景那就只能搜索关键字了）

快速查看两个 js 文件，发现加解密调用逻辑主要就存在jsencrypt-sm.js文件中

在关键位置进行断点，点击网页的扫码登录功能，很明显的发现参数 r 为请求报文体明文，参数 t 为加密密钥

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPmzSLWHiaTJc1Mt0cWbdBwOfKaZLhxJPzEQErj1ibKMVhlv4djChTISlg5Bhgg0VgqAb2rOfLoazzA/640?wx_fmt=png&from=appmsg)

根据堆栈信息可以找到调用加密的位置，可以看到密钥是通过YT.Security.getEncryptKey()获取到的， 每次调用getEncryptKey 密钥都会发生改变，跟踪函数发现生成密钥的位置如下

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPmzSLWHiaTJc1Mt0cWbdBwOnsCPYcniblXicSozt3wicVmN2pM2ryTW5XHm9PIgiaCJBaMZpC619Kib1iaw/640?wx_fmt=png&from=appmsg)

下面分析jsencrypt-sm.js 中的加密过程。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPmzSLWHiaTJc1Mt0cWbdBwO2C9pKmUkSSDD3QQGFFoDF7LgM1vEF9iadrEbq5ceMYofbuymoVJ1Sgg/640?wx_fmt=png&from=appmsg)

下面是整个请求报文体的加密处理过程

```
将报文体转换为byte数组

计算byte数组的长度

补齐数组长度到16的倍数，用随机数进行补齐，随机数计算方法

第一位制定为29(做分隔符) 后续Math.round(150 * Math.random()) % 150 + 30;

String.fromCharCode(29))  =〉 \x1D

生成混淆数组Math.round(255 * Math.random()) % 255;

然后将补齐后的字节数组逐位与混淆数组进行异或运算

异或结果+混淆数组进行拼接成新的数组

将拼接结果转换为hex字符串

密钥转换为字节数组

将以上两项进行sm4

将sm4结果从byte转换为hexstr

将sm4密钥进行sm2

拼接明文请求报文+对称密钥+YTGSRCU 然后将拼接结果进行sm3

u：sm3结果byte数组

o：sm4结果hexstr

s：sm2结果

拼接return "#10" + [Code.bytes2hexStr(u), o, s].join(String.fromCharCode(29))

最终请求报文
```

### 修改报文方式一（做成工具，自动化操作）

通过上面的加密逻辑分析，可以确定以下几点

1. 1. 对称加密密钥是随机生成的 应对方法：固定密钥（修改 js 文件使对称加密密钥保持不变）

   ```
    a. 调用加密算法时传入写死的字符串作为密钥

    b. 修改生成密钥的函数，使函数的返回值保持不变
   ```
2. 2. 组合加密，数字信封，对称+非对称+摘要 a. 固定对称加密密钥后非对称加密部分不需要操作 b. 对称加密部分，需要根据分析出的加密逻辑进行逆运算，将加密后的报文解密得到明文，修改报文后，再重写加密逻辑将明文加密成密文 c. 将修改后的报文重新算摘要

整体实现难度较大，但实现后将其做成 burp 插件，或者在 burp 上再叠一层 mitmdump 处理加解密 ，后续可以很方便测试。

### 修改报文方式二（适用于简单测试，验证，不方便批量操作）

通过调试找到调用加密函数的位置，可以在开发者工具中对指定参数进行修改，大变量需要在 console 窗口中进行修改

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPmzSLWHiaTJc1Mt0cWbdBwOntenSn9aSPDjYkfa0ckaDjZ0bnDibN4IjwZYIENopzwnLtdgbia1ibwNA/640?wx_fmt=png&from=appmsg)

### 修改报文方式三

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPmzSLWHiaTJc1Mt0cWbdBwOOy1AqkXhHT2pfQRDZic2ibAicSJ3etW5ET4ztcwicHkfM9EY8X3Q1reh5w/640?wx_fmt=png&from=appmsg)

可以看到报文的格式时 json，并且有调用的 JSON.stringify(r)，可以对JSON.stringify(r)进行 hook

每当调用JSON.stringify(r)时可以走入我们自定义的函数中，我们可以再此对传入的加密前的明文 body 进行修改

但此处不行，因为传入的 r 本身就是 string 类型走不到JSON.stringify(r)

跟对堆栈往前找

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPmzSLWHiaTJc1Mt0cWbdBwOvPuYCN330e0L5IuhIRPiaq2zw0XBdic0rrSdLJYvjWnp7ibbicicgWfe1CA/640?wx_fmt=png&from=appmsg)

可以对YT.Security.encrypt 进行 hook，此时代码走入了我们的自定义逻辑中，同样可以修改加密前的明文 body

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPmzSLWHiaTJc1Mt0cWbdBwOP2RXDicuPuTr2rzx5y0YLpz119Aykl8QwBWE4pt4r2uGLGshBsKrEYA/640?wx_fmt=png&from=appmsg)

### 修改报文方式四

通过 jsrpc 的方式，主动调用 js 中的报文加密和解密函数，对报文进行加密或解密

但是此处可以响应报文的解密适用该方法，加密逻辑复杂，网站 js 代码中未提供可以解密请求报文的函数

此处同样需要提前对密钥进行固定

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nPmzSLWHiaTJc1Mt0cWbdBwO5I27b5C0YL3UTtDzbJevsyFdVRk1QEVhBGJYbsicltCdhZJ6OBA1yWQ/640?wx_fmt=png&from=appmsg)

### 总结

其实针对用web端系统的前端加解密还是比较好解决的，可能难点在于js混淆，就是需要慢慢调试，理清逻辑后还是很好操作的，实在不行，前端代码都给了，直接上手改呗。

另：现在进入ai时代了，大不了扔给ai分析呗。

### 这里贴一段jsencrypt-sm.js 代码

```
define(function(require) {
    require("js/security/pnc-crypto-min");
    var r = YT.Security = {
        encrypt: function(r, t) {
            "string" != typeof r && (r = JSON.stringify(r));
            var n = function(r, t) {
                for (var n = r.length, e = t.length, o = newArray, s = function(r, t) {
                    for (var n = r.length, e = newArray, o = n / 16, s = 0; s < o; s++)
                        for (var u = 16 * s, i = 0; i < 16; i++)
                            e[u + i] = r[u + i] ^ t[i];
                    return e
                }(r, t), u = 0; u < s.length; u++)
                    u < n && o.push(s[u]);
                for (var u = 0; u < t.length; u++)
                    u < e && o.push(t[u]);
                return o
            }(function(r) {
                var t = r.length
                  , n = t % 16;
                n = 16 - n;
                var e = newArray;
                e[0] = 29;
                for (var o = 1; o < n; o++)
                    e[o] = Math.round(150 * Math.random()) % 150 + 30;
                var s = newArray;
                s = [].concat(r);
                for (var o = 0; o < e.length; o++)
                    o < n && s.push(e[o]);
                return s
            }(Code.str2bytes(r)), function(r) {
                for (var t = newArray, n = 0; n < 16; n++)
                    t[n] = Math.round(255 * Math.random()) % 255;
                return t
            }())
              , e = _Sm4.encode(Code.bytes2hexStr(n), Code.str2bytes(t))
              , o = Code.bytes2hexStr(e)
              , s = _Sm2.encode(t)
              , u = _Sm3.hash(Code.str2bytes(r + t + "YTGSRCU"));
            return"#10" + [Code.bytes2hexStr(u), o, s].join(String.fromCharCode(29))
        },
        decrypt: function(r, t) {
            var n = r.substr(14)
              , e = parseInt(r.substring(3, 5), 16)
              , o = parseInt(r.substring(5, 7), 16)
              , s = parseInt(r.substring(7, 8), 16)
              , u = parseInt(r.substring(8, 14), 16)
              , i = n.substring(e, e + o)
              , a = i.length
              , h = [];
            switch (h.push(n.substring(0, e)),
            s) {
            case1:
                h.push(i.charAt(a - 1)),
                h.push(i.substring(1, a - 1)),
                h.push(i.charAt(0));
                break;
            case2:
                for (var f = 2; f <= a; ++f)
                    f % 2 == 0 && (h.push(i.charAt(f - 1)),
                    h.push(i.charAt(f - 2)));
                if (a % 2 != 0 && 0 < a) {
                    h.push(i.charAt(a - 1));
                    break
                }
            }
            return0 != s && (h.push(n.substring(e + o)),
            n = h.join("")),
            n = n.substring(0, u),
            function(r) {
                for (var t = [], n = 0, e = r.length; n < e; n++)
                    240 <= r[n] && r[n] <= 247 ? (t.push(String.fromCodePoint(((7 & r[n]) << 18) + ((63 & r[n + 1]) << 12) + ((63 & r[n + 2]) << 6) + (63 & r[n + 3]))),
                    n += 3) : 224 <= r[n] && r[n] <= 239 ? (t.push(String.fromCodePoint(((15 & r[n]) << 12) + ((63 & r[n + 1]) << 6) + (63 & r[n + 2]))),
                    n += 2) : 192 <= r[n] && r[n] <= 223 ? (t.push(String.fromCodePoint(((31 & r[n]) << 6) + (63 & r[n + 1]))),
                    n++) : t.push(String.fromCodePoint(r[n]));
                return t.join("")
            }(_Sm4.crypt(Code.hexStr2bytes(n), Code.str2bytes(t), 0))
        },
        getEncryptKey: function() {
            return r.uuid(32, 16)
        },
        uuid: function(r, t) {
            var n, e, o = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split(""), s = [];
            if (t = t || o.length,
            r)
                for (n = 0; n < r; n++)
                    s[n] = o[0 | Math.random() * t];
            else
                for (s[8] = s[13] = s[18] = s[23] = "-",
                s[14] = "4",
                n = 0; n < 36; n++)
                    s[n] || (e = 0 | 16 * Math.random(),
                    s[n] = o[19 == n ? ...