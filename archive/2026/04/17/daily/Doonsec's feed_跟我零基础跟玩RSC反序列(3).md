---
title: 跟我零基础跟玩RSC反序列(3)
url: https://mp.weixin.qq.com/s/ev1ffisbI9FePqwSIoJiMg
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:24:31.823443
---

# 跟我零基础跟玩RSC反序列(3)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SPfHPOgCrHqn89D4IB0aiaNrlzR8vKQk47iaSORjyciaXZvE5OIjzHIpCIHiaMyULKnmX9goych0m6g80bSpRbzCUvw08cCvlHpAzCpdvtYJQNE/0?wx_fmt=jpeg)

# 跟我零基础跟玩RSC反序列(3)

原创

YMsora
YMsora

YMs0ra的安全漫路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

```
if (isFetchAction) { // A fetch action with a multipart body. const busboy = require('next/dist/compiled/busboy')({ defParamCharset: 'utf8', headers: req.headers, limits: { fieldSize: bodySizeLimitBytes } }); // We need to use `pipeline(one, two)` instead of `one.pipe(two)` to propagate size limit errors correctly. pipeline(sizeLimitedBody, busboy, // Avoid unhandled errors from `pipeline()` by passing an empty completion callback. // We'll propagate the errors properly when consuming the stream. ()=>{}); boundActionArguments = await decodeReplyFromBusboy(busboy, serverModuleMap, { temporaryReferences });
```

前置我们已知busboy过decodeReplyFromBusboy解析后返回了boundActionArguments，body被pipeline进了busboy，这里busboy处理逻辑不做赘述。

因为

```
 pipeline(sizeLimitedBody, busboy, // Avoid unhandled errors from `pipeline()` by passing an empty completion callback. // We'll propagate the errors properly when consuming the stream. ()=>{});
```

所以参数busboy是作为流式数据源，serverModuleMap便是函数的映射表。

我们接着溯源到函数decodeReplyFromBusboy

```
exports.decodeReplyFromBusboy = function ( busboyStream, webpackMap, options ) { var response = createResponse( webpackMap, "", options ? options.temporaryReferences : void 0 ), pendingFiles = 0, queuedFields = []; busboyStream.on("field", function (name, value) { 0 < pendingFiles ? queuedFields.push(name, value) : resolveField(response, name, value); }); busboyStream.on("file", function (name, value, _ref2) { var filename = _ref2.filename, mimeType = _ref2.mimeType; if ("base64" === _ref2.encoding.toLowerCase()) throw Error( "React doesn't accept base64 encoded file uploads because we don't expect form data passed from a browser to ever encode data that way. If that's the wrong assumption, we can easily fix it." ); pendingFiles++; var JSCompiler_object_inline_chunks_251 = []; value.on("data", function (chunk) { JSCompiler_object_inline_chunks_251.push(chunk); }); value.on("end", function () { var blob = new Blob(JSCompiler_object_inline_chunks_251, { type: mimeType }); response._formData.append(name, blob, filename); pendingFiles--; if (0 === pendingFiles) { for (blob = 0; blob < queuedFields.length; blob += 2) resolveField( response, queuedFields[blob], queuedFields[blob + 1] ); queuedFields.length = 0; } }); }); busboyStream.on("finish", function () { close(response); }); busboyStream.on("error", function (err) { reportGlobalError(response, err); }); return getChunk(response, 0); };
```

接收的busboystream便是busboy对象输出的数据流，webpackMap也就是映射，便是serverModuleMap，只是换了个名字。

接下来便是busboystream输出的分块表单，进行回调函数处理，并且设置了队列queuedFields

```
 busboyStream.on("field", function (name, value) { 0 < pendingFiles ? queuedFields.push(name, value) : resolveField(response, name, value); });
```

4是控制field字段的队列，下面都是针对data为file情况的解析。

目光拉回creatResponse

```
 var response = createResponse( webpackMap, "", options ? options.temporaryReferences : void 0 ),
```

溯源:

```
function createResponse( bundlerConfig, formFieldPrefix, temporaryReferences ) { var backingFormData = 3 < arguments.length && void 0 !== arguments[3] ? arguments[3] : new FormData(), chunks = new Map(); return { _bundlerConfig: bundlerConfig, _prefix: formFieldPrefix, _formData: backingFormData, _chunks: chunks, _closed: !1, _closedReason: null, _temporaryReferences: temporaryReferences }; }
```

webpackMap作为bundlerconfig传入，校验之后创建new formdata()对象

变量在这里再次更新后return

bundlerconfig,也就是webpackmap=\_bundlerconfig。 \_chunks变为new Map()对象.

\_prefix为空字符串。

最后在这些状态挂在response对象的情况下进行getchunk

```
return getChunk(response, 0);
```

并且注意到挂载队列的处理函数是resolveField

溯源

```
function resolveField(response, key, value) { response._formData.append(key, value); var prefix = response._prefix; key.startsWith(prefix) && ((response = response._chunks), (key = +key.slice(prefix.length)), (prefix = response.get(key)) && resolveModelChunk(prefix, value, key)); }
```

这里response已经是挂载成一个集函数map的对象了，并且prefix因为是空字符恒成立，并且将response挂载为chunks

这里的chunks为一个空的对象。上面的key就是name字段，而response便是多表单为解析的空map()对象

这里区分一下，createResponse行为相对是单次的，而resolveField是每次表单执行一次

阶段来说。代码块8的response是有formdata和map两个空对象的

每次都将key和value字段存入formdata。但是另外的chunk开始是空的，也就是取不到key。

也就进不了resolveModelChunk分支。

但是每次decodeReplyFromBusboy结束前都会进一次getchunk。

继续跟进吧

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