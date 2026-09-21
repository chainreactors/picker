---
title: Hx0鹰眼 1.0.6-0920：MCP 升到 1.0.12，双浏览器共用一份服务
url: https://mp.weixin.qq.com/s/rOlj4SITrW0Q61RiLkpglg
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:24:17.117256
---

# Hx0鹰眼 1.0.6-0920：MCP 升到 1.0.12，双浏览器共用一份服务

# Hx0鹰眼 1.0.6-0920：MCP 升到 1.0.12，双浏览器共用一份服务

原创

asaotomo
asaotomo

Hx0极客圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Hx0鹰眼 · 0920版本更新

9 月 20 日，Hx0 鹰眼 v 1.0.6 - 0920版本正式发布。这次不堆新功能，主攻三件事：MCP 服务升到 1.0.12、Chrome 与 Firefox 共用同一份 MJS、长任务回执和分页更干净。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOibg0wJht8gV8lJTynaCzicN9mlrvcib7VftcteUwibPcaufs7xvBulT4G8MkArT6EGA26WKCWMciaIWvATYNYoGtQQKvYnah8wrdQE/640?wx_fmt=png&from=appmsg)

Hx0 鹰眼：浏览器里的抓包、拦截、重放与 MCP / Agent 工作台

先说结论

0920 是v 1.0.6 的稳定性优化版本。功能边界没变：社区版继续覆盖抓包、拦截、分流、深搜和敏感信息匹配；HawkEye MCP 与浏览器级 Agent 仍是专业版能力。

升级必须三步一起做：替换扩展并重新加载，替换 hawkeye-mcp-server.mjs，重启 MCP 服务。只更扩展、不换 MJS，Cursor / Codex 里仍可能连到旧服务。

MCP 1.0.12：一份服务，两份浏览器

这是 0920 最值得升级的一点。Chrome 和 Firefox 现在共用同一份 MJS，两套浏览器可以同时连上、待命，不用再为每个浏览器各起一套服务。

同时修了几个会把 Agent Host「卡死在半连接」的问题：

· 端口被占用时服务不再假活着不退出

· stdio 结束后残留进程

· Firefox 导航取消信号错位

· 原生输入回执对不齐

工具还是 51 个，能力档位没砍。变的是 schema 兼容和分页：大结果用 next\_page\_token 续读，不再靠反复重跑同一条工具去翻下一页。

回执变短，证据还在

给 Cursor、Codex、LM Studio 这类 Host 用的时候，工具默认不再把整页快照塞回来。点击、输入、选择、按键和等待默认返回精简回执，只留状态变化和输入证据；需要页面详情时再开 include\_elements。

几条常用工具也按这个思路收了一遍：

· browser\_read\_text：正文和结构化 value 同步返回，缺正文会明确报错，不再默默给空结果

· evaluate：默认不带控制台日志，需要时再开 include\_logs

· navigate：默认给带 ref 的精简预览，完整观察用 include\_snapshot

另外修了 SPA 换页后 ref 被复用、标题误判、查找上下文重复。这些都是长任务里最容易让模型点错控件的点。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO8ImTqQOCH9icrFfMib2FicQGDQR1mqSh6x2dMR1YrXAOhsVXtsFfr302WcAA73hWaGvRt4QR6HxibL28Mee0RStbuVkpD8zrnnQYM/640?wx_fmt=png&from=appmsg)

侧栏工作台还在：抓包、重放、AI 生成用例，和 MCP 共用同一套浏览器会话

分流、脚本、Agent：三处实打实的修复

智能代理分流修了默认端口校验、无效地址被误应用、以及浏览器代理读取。Firefox 改走原生请求分流；Chrome 未命中规则时直连，Firefox 保留浏览器默认路径。社区版从 1.0.6 起就能用分流器，把命中站点转到 Burp / Yakit，其它请求保持原路。

页面脚本修了刷新漏注入、保存失败仍跑旧代码、重复注入、禁用脚本被执行，以及目标偏移。注册改成串行，并校验保存回执——写脚本的人会直接感到差别。

Agent 截断：遇到输出耗尽时，这次会增加输出预算并关闭该轮思考；如果持续耗尽，会明确提示暂停和恢复方式，不再让任务无声卡死。

实用场景：一句话给百度首页加天气

0920 把 Agent 和页面脚本修稳之后，最直接的用法是：当场改页面，再把改动存成下次自动跑的脚本。下面用「给百度首页加天气」走一遍。

打开百度首页，对 Agent 说「在当前页面新增显示合肥天气」。它会自己读页面、拉天气数据、再把卡片挂上去——snapshot、fetch、evaluate 一轮就能做完。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO8Jde6ia4QQDlJWk1gnKTiaU1aDiad5ulY9FHTOK0icFTISicxaiaG4PsXK90QxlAH1etokamg2Dpicicu1VsuvIX9bEhg5NwTRE6tSEA8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOibA3Cwr3YhAeXsRTCqDNJ6YibW6yedEg7fvsUiaJBIkS6ibDoSP7DQWS9HfOoqkoPDkGtU5YonCYxuwZibcz3aETB2eBUozMSDkWBM/640?wx_fmt=png&from=appmsg)

Agent 模式：一句话给百度首页挂上合肥实时天气

这次改动能立刻固化成页面脚本：匹配 baidu.com，下次打开百度自动注入，不用再走一遍对话。脚本库里还能和 AES 解密、站点小工具放在一起。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOibRicBg4QdfDxVrVUm0VIHIK64YZS3BW9DTiaRXwH1dPzByziawRTfQxHMyF7IoY81JXva5FF9ibPANnf7Ka0DWOBlKgzicoPYmG8oA/640?wx_fmt=png&from=appmsg)

保存为页面脚本后，匹配 baidu.com 的页面会自动加载

关掉侧栏，首页右上角就是一张可关的天气卡片。Agent 负责当场改，脚本负责下次还在。

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOib9ic81xlg2zMibN6gticuU2LTOZz5FVLf9EznBWMdcZjB2yf2R39QYVUL2Eb8hxZSofUbiaq7bibL0kf7kTLgOrVwlkiaxReGAUaBic8/640?wx_fmt=png&from=appmsg)

成品：百度首页右上角的天气卡片

怎么升级

请只从仓库下载对应浏览器的正式 ZIP，本版不发布 CRX / XPI：

· Chrome / Edge：Hx0-HawkEye-Chrome-V1.0.6-Official.Release.zip

· Firefox：Hx0-HawkEye-Firefox-V1.0.6-Official.Release.zip

Chrome / Edge：解压到固定目录，扩展管理页开启开发者模式后加载已解压的扩展。升级时先导出要保留的数据，用新包覆盖原目录，再点重新加载。不要同时加载两个目录，避免扩展 ID 和本地数据各搞一套。

Firefox：普通正式版仍是临时载入。解压后到 about:debugging 载入 manifest.json；浏览器重启后需再载一次。

MCP：在扩展弹窗重新下载 hawkeye-mcp-server.mjs，覆盖旧文件后重启 Host 里的 MCP 服务。需要 Node.js 18+，不用 npm install。

下载与试用

仓库：https://github.com/asaotomo/Hx0-HawkEye

官网：https://www.hx0.store/products/hawkeye

新安装用户可先体验 1 天鹰眼 Pro 会员。MCP 和浏览器级 Agent 只在有效试用或专业版授权下可用；用完请在授权范围内测试，不要对未授权系统做拦截、重放或 Fuzz。

限时活动

即日起至 9 月 30 日 24:00，购买鹰眼 Pro 永久会员，加送一年 Hx0战队知识星球会员。活动截止后恢复原权益，下单前请以官网说明为准。

一句话：0920 让鹰眼的 MCP 更像一份能同时伺候 Chrome 和 Firefox 的本地服务——工具还是 51 个，回执更短，连接更稳。

来源：Hx0-HawkEye 仓库 README v1.0.6 0920 更新说明

Hx0战队交流群

欢迎安全区的小伙伴加入～

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9FaiaIVqn0HoZtT4yicgWiaOY74qUiaqrCk2qkazIIUEk7bORk93cb05IMAzrHCQIgLhYHcZ9bu3xKKOaj4lprYUoDZF1Le5yMibZg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO96vQKict5Njccs0NxhzcTHbkVeVnSnNvIwf6d01l7x12WMEFaxAwJIPG1feicAbYLzUoDjBbAvhRE9t9FbusNWcVHpIUs20TSyc/0?wx_fmt=png)

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