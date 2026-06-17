---
title: Agent分析JS加解密函数自动生成autodecoder脚本
url: https://mp.weixin.qq.com/s/UN-f97ebDmJ_F64ikiDvfw
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:01:06.439837
---

# Agent分析JS加解密函数自动生成autodecoder脚本

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVlrq5UjeNS49gFyGLyTStq9b9cDwqO2PaPDWbC5RldNicOf4ibPUsCMQuHpyOhrfctweV4L0erj7iaejVX4P6G0UFzib3yicTyd6dXQ/0?wx_fmt=jpeg)

# Agent分析JS加解密函数自动生成autodecoder脚本

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 544，阅读大约需 3 分钟

## 前言

现在很容易遇到网站、小程序和 APP 的请求和响应包加解密的情况。

常见的解决方案就是找到加解密函数，用 Python 实现后，通过 Burp 插件 autodecoder 实现 Burpsuite 明文操作。

现在也可以用 AI 来帮助我们解决。

## 环境准备

* • claude code
* • deepseek pro v4
* • cc-switch
* • Burpsuite
* • autodecoder

### autoDecoder

简单的 python 脚本，也不需要写什么 skills，下载项目到本地，去除源码

```
git clone https://github.com/f0ng/autoDecoder
```

![96d24fb61878dfb17e5e6ec79e189f0f.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkW1mcLtf7sNtcbEaf1MEQz9cibdXicYfkQeiaOQuZJUjnKkqzd9Oa82PmxiaaPg1SGfAILb2jp3roHWpxVGfUuwVwwEQZNy3hiagnE/640?from=appmsg "null")

96d24fb61878dfb17e5e6ec79e189f0f.png

在当前目录下执行

```
claude --dangerously-skip-permissions

# 初始化项目，生成 CLAUDE.md
/init
```

### 下载 JS 代码

将 web 系统的加解密相关的 JS 文件下载到本地

比如用 Webpack\_extract 将 js 打包下载
![20e2563ff24ce9d276d58165982d3aec.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlib3kLmSjL60fGyft6gDnW6MM8LWib0VcFc0ZBibH1hCqoqco65DMHtDvaRLMhZ3ZqE6QTJicNgzRczkcXdMRt94qtk9G0D8QSRicw/640?from=appmsg "null")

20e2563ff24ce9d276d58165982d3aec.png

> 项目地址：https://github.com/xz-zone/Webpack\_extract

或者用 chrome 的 mcp

chrome 启动远程调试端口，然后访问网站

```
chrome.exe --remote-debugging-port=9222 --user-data-dir="D:/chrome-reverse"
```

`chrome-devtools-mcp`配置

```
{
  "command": "npx",
  "args": [
    "-y",
    "chrome-devtools-mcp@latest",
    "--browser-url=http://127.0.0.1:9222"
  ]
}
```

## 分析加解密 + 实现 autoDecoder 的 python 脚本

如果 JS 没有混淆，也不需要什么 skills，直接跑

```
1、读取 jsfiles 下的JS文件，分析加解密。
2、写一个Burpsuite插件autoDecoder的python脚本，实现请求包的加密和响应包的解密 autoDecoder相关信息参考文件夹autoDecoder

请求包和响应包如下：
<贴上真实的请求包和响应包，如果怕信息泄露，可以给关键信息打码>
```

![b8740193de6cdfe9f060f9c5e4c6ae11.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkC4eP3gfqc5yNAuHeocrJryAxzRRibZGp1Bv3WvyHMia31mhtrVfX7AtokLcCiapNbYoQ5GM6pp3libZunuSWFtyygbPuWPlxrFr8/640?from=appmsg "null")

b8740193de6cdfe9f060f9c5e4c6ae11.png

不是魔改二开的加解密方法的话，基本就能直接跑出来了。

![d9f2c999877398ff097be2e0b57f7c06.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmpDQK3IKv3nQhZ5vldPAPLGicAdBEdSHm3AsX1CuhDsVzJgy6eXB8s4t0QgsBGbKTpAWzV6FofpX5II0SJ9EyePhrFTYF3vbTs/640?from=appmsg "null")

d9f2c999877398ff097be2e0b57f7c06.png

启动后，在 autodecoder 中验证加解密
![85f043c407d28170d7500f0f732060b0.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkrUIQlSoQyMBmtLlm4k0KonRaVNNV9PmLibiah7WkEKQ7TpZq16ybDIdiafcBYyXydPicCx5fDJ7mhehjw2gzv4heMj1fnIHiaToUQ/640?from=appmsg "null")

85f043c407d28170d7500f0f732060b0.png

如果是复杂的，建议分成两步，先确定加解密函数成功解析出来，能手动加密发包，并且手动解密响应包成功时，再让大模型写 autoDecoder 的 python 脚本也不迟。

对于魔改的情况，让 python 直接调用加密库可能对不上，就让大模型通过 python 使用代码层面的实现而不是单纯调用函数

## 总结

大体思路就是如此，可以根据情况做调整。在不存在 JS 代码复杂混淆的情况，deepseek 基本足够了，如果有混淆，可以用 GLM5.x 或者 GPT5.5 什么的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a1BOUvqnbriaKQaulUawUmcqevsicgRXaDWWcgmsbG7iaTtKE89ZwJEkPHzibEzXwcibLn8PKu1hGoicqAEIW9uQjyBw/640?wx_fmt=jpeg)

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