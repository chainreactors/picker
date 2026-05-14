---
title: spider-king 面向 Web 协议恢复与参数还原场景的 Skill
url: https://mp.weixin.qq.com/s/n6B5B1mIJb2zrsQ695zfyw
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:43:01.760586
---

# spider-king 面向 Web 协议恢复与参数还原场景的 Skill

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVkGPvwYyEW0eudicriapBu3jW2VRYTW5ZkEGTJ8iaG6ibeU7lrlV1EBn1bWGuwK2Wz6tyo4jLLHQUASs4BGHSIibnJTkmnsxNWnFKh8/0?wx_fmt=jpeg)

# spider-king 面向 Web 协议恢复与参数还原场景的 Skill

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 299，阅读大约需 2 分钟

## 前言

Github 上新的 web 逆向分析的 AI-skills

`Spider King` 是一套面向 Web 协议恢复与参数还原场景的逆向工程 Skill。

它的目标不是“把网页点通”，也不是“用浏览器把请求糊过去”，而是把看起来依赖浏览器环境的目标，拆回到可复现、可验证、可长期维护的纯协议采集链路中。

这套 Skill 默认面向自有系统、已授权平台、合法安全测试与教学研究场景，强调以下交付原则：

* • 先证据，后结论
* • 先协议，后自动化
* • 先还原动态状态，再谈分页、并发和规模化
* • 最终交付必须脱离浏览器运行

项目地址：https://github.com/aoyunyang/spider-king-skill

![9fd563ffff78b0796ba87aa4343c4bfe.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlA4r64Zef4CRP0d4ia9qjD436R80twKzF9AtGicpxZvxZllw1u7QEDDkSo5WgwNVBia9jkRgVlBkMTLzXq9u9gW5WrLtOoIFbFcY/640?from=appmsg "null")

9fd563ffff78b0796ba87aa4343c4bfe.png

## 环境

* • Windows 11
* • cc-switch
* • cluade code
* • deepseek v4 pro
* • chrome

chrome 启动远程调试端口：

```
chrome.exe --remote-debugging-port=9222 --user-data-dir="D:/chrome-reverse"
```

### mcp

* • chrome-devtools

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

* • js-reverse

```
{
  "command": "node",
  "args": [
    "D:/mcp/JSReverser-MCP/build/src/index.js",
    "--browserUrl",
    "http://127.0.0.1:9222"
  ]
}
```

### skills

spider-king-skill
https://github.com/aoyunyang/spider-king-skill

## 测试

```
通过mcp和skills，读取当前chrome当中的页面中的题目，并给出答案，将获取的过程转换为python脚本
https://match.yuanrenxue.cn/match/12
```

结果
![1ba72dfe5aaae54737a8d332d39b8f09.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmOibdtiaDp2bcwuSTqZ3IucR2RU5R3o5pLTgyuSEFibYDy6eT84HjfXRXY0Els8KAamLIlr9lC7nScIQ1IHCw5NlicHp6G5ibFItIg/640?from=appmsg "null")

1ba72dfe5aaae54737a8d332d39b8f09.png

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