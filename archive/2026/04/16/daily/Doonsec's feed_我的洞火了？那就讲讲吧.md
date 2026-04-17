---
title: 我的洞火了？那就讲讲吧
url: https://mp.weixin.qq.com/s/UUMx2_NjgdWkj53Wyrs9DQ
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:44:05.257963
---

# 我的洞火了？那就讲讲吧

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ogrJiczzwv0AvPWT87IYCic54RI47r73cJ44CJBm90kY7pSseAaNF8Bs3aGcqzC0VewOFQIN9CX2dUuIYRbuEE6u94IevDg9J2WnpKS8J2Tg8/0?wx_fmt=jpeg)

# 我的洞火了？那就讲讲吧

原创

秋风
秋风

秋风的安全之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

CVE-2026-39987相信有部分师傅应该刷到了

不管是网页还是x还是公众号还是比较多人发的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogrJiczzwv0D2RAz5Oj2qoEm4TdLj4hVOvXib3CuM5BqWOgsfYz4PHeTZaj6od0hDa7TW1FnFXOCHQelVgtFpfJGrf8AJKr0MFvGJexiaRLCWM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogrJiczzwv0AiaPxf1C0R0XNKObtYIDaNZGZtbP4euicDvwYpbg0yKbian47SsXQZGZX4AtISZLNs7o0VKFsx8nD6oRhV9pFH0DqOVLonQB1Fs8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogrJiczzwv0AKSFopeU66tpIod5buhbKJvPBceEf4lABKVoOysaHRneiaicpibp0xQ8VAArDVcWzg9RNsXwYzMoqbgJLhJplgbHRPKDABRVNR54/640?wx_fmt=png&from=appmsg)

这个洞其实并非很复杂

Marimo 的终端 WebSocket 端点 /terminal/ws 缺少身份认证检查，允许任何人（包括未认证的攻击者）直接连接并获得一个完整的 shell，从而执行任意系统命令

可以看到：

```
# marimo/_server/api/endpoints/terminal.py (第 340-356 行)@router.websocket("/ws")async def websocket_endpoint(websocket: WebSocket) -> None:    app_state = AppState(websocket)
    if app_state.mode != SessionMode.EDIT:        await websocket.close(...)        return
    if not supports_terminal():        await websocket.close(...)        return
    await websocket.accept()
    child_pid, fd = pty.fork()
```

这我觉得很明显是遗忘了

可以看到他另一处的处理

```
#ws_endpoint.py (第 67-82 行)@router.websocket("/ws")async def websocket_endpoint(websocket: WebSocket) -> None:    app_state = AppState(websocket)    validator = WebSocketConnectionValidator(websocket, app_state)
    if not await validator.validate_auth():        return
```

调用了validate\_auth()进行身份的验证

Marimo 使用 Starlette 的 AuthenticationMiddleware，有一个局限性就是它会将失败的认证标记为UnauthenticatedUser，但是不会拒绝WebSocket的连接，实际需要@requires()或者validate\_auth()方法

所以就有了如下攻击链:

```
1. 连接 ws://目标服务器:2718/terminal/ws (无需任何认证)   ↓2. 服务器直接调用 websocket.accept() 接受连接   ↓3. 调用 pty.fork() 创建伪终端子进程   ↓4. 获得完整的交互式 shell   ↓5. 可以执行任意系统命令   ↓6. root
```

ref:

https://github.com/marimo-team/marimo/security/advisories/GHSA-2679-6mx9-h9xc

https://links.marimo.app/cwe-306-terminal-ws-auth-bypass

https://github.com/marimo-team/marimo/security

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibdxaL75td0eTNNW0FhzOdr3ZNYyhwH5qgiclNDLlViaWVkMtdpxGhxWNuroULUXVC2P0AekKicV9NZShl297HPmRw/0?wx_fmt=png)

秋风的安全之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibdxaL75td0eTNNW0FhzOdr3ZNYyhwH5qgiclNDLlViaWVkMtdpxGhxWNuroULUXVC2P0AekKicV9NZShl297HPmRw/0?wx_fmt=png)

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