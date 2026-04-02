---
title: 给AI Agent配置JS逆向MCP
url: https://mp.weixin.qq.com/s/D9mJdlNwxfeMXsNKbJVa0w
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:22:03.940158
---

# 给AI Agent配置JS逆向MCP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVnPXyqSmpXia92PUTQ1htoH4CUl6TIYtticMXMx28bYlDfQdetwULEJhN3UkXOdtSfiaR9yJYLBxsH4cUKrngQfHq3eGqsHupleHA/0?wx_fmt=jpeg)

# 给AI Agent配置JS逆向MCP

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 221，阅读大约需 2 分钟

## 前言

JS 逆向 MCP + skills/提示词。

依旧是在 TRAE CN 中配置，下面是我最近做猿人学 JS 逆向题目时候的配置。

## chrome

chrome 启动远程调试端口：

```
chrome.exe --remote-debugging-port=9222 --user-data-dir="D:/chrome-reverse"
```

验证
http://127.0.0.1:9222/json/version

![50bf83e16dc551e8b8ce2f4522492875.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmcGDCHE261oQWwN1oCph1kDjbJiau1DlGZDpxEJW65qupUQRp003p0bhC2tPicHIYry8qJrbwj6AV5ibhnuGn9Ks66TkO5jXmIick/640?from=appmsg "null")

50bf83e16dc551e8b8ce2f4522492875.png

chrome 可以用官方的，也可以用二开的。
**YSbrowser 指纹浏览器**
项目地址：https://github.com/selfshore/YSbrowser

启动没区别

## MCP

### JSReverser-MCP

link： https://github.com/NoOne-hub/JSReverser-MCP

![3faa528c192d0b0748696c0073893fcf.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnqT8ibLLVUNnHcANOdLgs2kDwWzgxiajRia5v4KiblJ2KheAuYNHm2SKaD1KP3QtAHoqSrQ4w12PZ5S3sDtXu9TI1JRJMP2pxm4M8/640?from=appmsg "null")

3faa528c192d0b0748696c0073893fcf.png

下载项目到本地，安装依赖并构建

```
npm install
npm run build
```

在 MCP 中配置

```
{
  "mcpServers": {
    "js-reverse": {
      "command": "node",
      "args": [
        "D:/AIskills/mcp/JSReverser-MCP/build/src/index.js",
        "--browserUrl",
        "http://127.0.0.1:9222"
      ]
    }
  }
}
```

验证：
![1170976ceea9c0e8930a39a274c875f1.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnNv9rqMtEoPsJ6zpcia6ZGHdBb2picJfVialFk6iazKURTKWWA4NibhsHriaibbMOicN2jAtia3eN5g0U5ZBK1zDlhn1eSlZUcEjpsxVWk/640?from=appmsg "null")

1170976ceea9c0e8930a39a274c875f1.png

### chrome-devtools

TRAE 中配置

```
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--browser-url=http://127.0.0.1:9222"
      ]
    }
  }
}
```

验证：
![f28ebb27a25774ac03a1bfe39e8450de.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkXaxgXv8gNK3LXicUibNgOmIMBZWnmQnVyBTmUWGqmsP99oj1sQDTicxAu3NI9gHJposFFdbTBC0UbWewCMwT9LY0zvJoEBYRSZw/640?from=appmsg "null")

f28ebb27a25774ac03a1bfe39e8450de.png

### playwright-mcp-server

```
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@executeautomation/playwright-mcp-server"
      ]
    }
  }
}
```

### 提示词

* • GPT 提示词，让 AI 接管 WEB 和 APP 逆向 [https://mp.weixin.qq.com/s/F70Rj5sYA0RNr5MDCS37Ww](https://mp.weixin.qq.com/s?__biz=MzcwMzIxNDAxMQ==&mid=2247483699&idx=1&sn=2e8150e2f09fb25b8c1e687dae31a64c&scene=21#wechat_redirect)
* • Vibe coding 用 AI 做 JS 逆向食用教程 [https://mp.weixin.qq.com/s/aWTEFgqb\_B8gxvzxpJpypA](https://mp.weixin.qq.com/s?__biz=MjM5NjE0NTY5OA==&mid=2448550187&idx=1&sn=ac40d01b17633789ad81b23eb481274a&scene=21#wechat_redirect)

## 参考资料

* • [https://mp.weixin.qq.com/s/N2MDsuxf1-5jDRYxlRWKZg](https://mp.weixin.qq.com/s?__biz=MzIwNDQyMTg0Nw==&mid=2247486925&idx=1&sn=741a553ae0de73e827ee24d59c5c486a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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