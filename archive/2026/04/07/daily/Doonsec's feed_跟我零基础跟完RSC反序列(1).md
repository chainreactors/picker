---
title: 跟我零基础跟完RSC反序列(1)
url: https://mp.weixin.qq.com/s/94EXdMcMTo9g_uKVC6BGFA
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:36:44.705069
---

# 跟我零基础跟完RSC反序列(1)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SPfHPOgCrHq5xKLChkDxrJ4W51XhPasF1ALFsRNUXJK1AyRMia98c6KPDKTPDpFq21fSObG6DPRl3KyDoH3DojGdfyAo3jxkZM8GdYF6erWo/0?wx_fmt=jpeg)

# 跟我零基础跟完RSC反序列(1)

原创

YMsora
YMsora

YMs0ra的安全漫路

![]()

在小说阅读器中沉浸阅读

(1)

1.React框架的next-action初步

业务逻辑的跟进

关于next-action这个头，是一种函数身份的定位，也就是一串hax值，react框架构建以来，每个函数会绑定一串hax，作为标识符.

当然我的审计是从next-action的识别及后续开始的，所以我暂时不会在初步构建以及hax加密这块去做工作。

另外，为了加强文档可读性，我会较多换行。那就 START

```
if (actionId) {
        const forwardedWorker = (0, _actionutils.selectWorkerForForwarding)(actionId, page, serverActionsManifest);
        // If forwardedWorker is truthy, it means there isn't a worker for the action
        // in the current handler, so we forward the request to a worker that has the action.
        if (forwardedWorker) {
            return {
                type: 'done',
                result: await createForwardedActionResponse(req, res, host, forwardedWorker, ctx.renderOpts.basePath)
            };
        }
    }
```

其中selectWorkerForForwarding这个函数，溯源之后是.d.ts的声明文档，在同目录下的js文件处找到了源function。

```
function selectWorkerForForwarding(actionId, pageName, serverActionsManifest) {
    var _serverActionsManifest__actionId;
    const workers = (_serverActionsManifest__actionId = serverActionsManifest[process.env.NEXT_RUNTIME === 'edge' ? 'edge' : 'node'][actionId]) == null ? void 0 : _serverActionsManifest__actionId.workers;
    const workerName = normalizeWorkerPageName(pageName);
    // no workers, nothing to forward to
    if (!workers) return;
    // if there is a worker for this page, no need to forward it.
    if (workers[workerName]) {
        return;
    }
    // otherwise, grab the first worker that has a handler for this action id
    return denormalizeWorkerPageName(Object.keys(workers)[0]);
}
```

这里的serverActionManifest参数类似一张actionid和worker进程的对应表单，下面就是return，其中denormalizeWorkerPagename是返回转发路径的。

也就是说，serverActionsManifest的action匹配的workers值被赋值给workers，然后denormalizeWorkerPageName将所有对应的workers的路径返回。

```
*/ function denormalizeWorkerPageName(bundlePath) {
    return (0, _apppaths.normalizeAppPath)((0, _removepathprefix.removePathPrefix)(bundlePath, 'app'));
}
```

接下来就是1返回的createForwardedActionResponse，简化的最终请求就是

```
const response = await fetch(fetchUrl, {
            method: 'POST',
            body,
            duplex: 'half',
            headers: forwardedHeaders,
            redirect: 'manual',
            next: {
                // @ts-ignore
                internal: 1
            }
        });
```

body经过strearm之后可以分块读取数据，body是我们的req，headers是扒res的cookie之类的字段送过去

```
const forwardedHeaders = getForwardedHeaders(req, res);
```

以上，next-action的前置分析完成，再者就到了action的server接收以及解析。

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