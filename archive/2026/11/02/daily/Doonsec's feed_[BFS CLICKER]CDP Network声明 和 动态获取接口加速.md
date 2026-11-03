---
title: [BFS CLICKER]CDP Network声明 和 动态获取接口加速
url: https://mp.weixin.qq.com/s/rJKCB2KNQCyHCn_4r1oI-Q
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:46:41.996358
---

# [BFS CLICKER]CDP Network声明 和 动态获取接口加速

# [BFS CLICKER]CDP Network声明 和 动态获取接口加速

原创

Lior1969
Lior1969

Moonlight安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

BFS CLICKER · 系列 01

![bfs-clicker 项目总览：Web Exploration、Mobile Evidence、MCP Gateway](https://mmbiz.qpic.cn/mmbiz_png/vP5icicMocf9ht3xYia5WRDWuib9vmiblfb0YvCCZVxZRROPhWJHyvzEfYg3tmB7xoJtzbzIxOOIt8CDEPvib0TkLTSf5NQkYWP7FYDQCmQ008ImM/640?wx_fmt=png&from=appmsg)

![少等待，少重放，BFS 升级实录](https://mmbiz.qpic.cn/sz_mmbiz_png/vP5icicMocf9jJzuD7roGHsajic6QEmXnSrTmEc2roXvgz0ibwk7zjgFJq4ZLCFmqNqD3NcMkLZXYsB9w7qpIBic5xzicPy6vZnOtSKWDp5EiaU2cU/640?wx_fmt=png&from=appmsg)

本地验证版 · BFS Clicker 系列专题

遍历仍采用 BFS，这次工程升级减少重复等待、路径重放与全量写盘。用同覆盖基准核对结果，再看技术改动怎样变成实际收益。

网页探索慢，未必慢在遍历算法。浏览器已经停稳，多个步骤却各等一遍；刚走到深层页面，又回入口重走；改动一个状态，还要重写整份断点。时间被这些重复工作一点点吃掉。

BFS Clicker 这次仍用原来的 BFS。改的是让每次等待、点击和写盘更有价值。

01 / 技术升级

## 等待保留，重复等待减少

浏览器观察网络和页面变化，同一段已经确认稳定的结果可以复用；点击等动作会先使旧结果失效，下一次仍检查 DOM 是否变化。默认连续观察窗口保留 160 毫秒，没有整体压成一个容易漏控件的短延时。

120 毫秒后才出现链接的本机页面被放进回归：要证明它更快，也要证明链接仍被发现。有界观察无法包办任意未来定时器，报告继续保留这类边界。

![BFS Clicker 技术升级图解](https://mmbiz.qpic.cn/mmbiz_png/vP5icicMocf9jVuQS2Nekg7ROZJWU8VtVvfKzWnROGwTdalOwMujCKCTcJGRwH4uaZObFzs4lmXYUFQH9WeX12yJhS1JXJmoGTialR78rPx3aw/640?wx_fmt=png&from=appmsg)

本地基准图｜18 次浏览器对照，三类场景均保持状态与已响应 API 覆盖一致。

02 / 技术升级

## 刚到的新页面，验证后接着走

深链里最浪费的是反复回入口。现在，刚构建的新状态若仍驻留当前页面，可在完整语义指纹复核、路径可安全重放后继续探索。执行任意动作前即废弃旧复用资格，命中已有指纹也不重新启用。URL 和画面相同，并不足以证明隐藏的业务状态没变。

六层深链夹具每轮请求从 56 次降至 14 次，重放动作从 15 次降至 0 次。不同分支仍按需要恢复页面，这条隔离规则没有为提速让步。

03 / 技术升级

## 把磁盘和正文预算留给有效证据

断点先追加带序号、身份和校验和的增量日志，每次 fsync，再周期性合并完整快照。只变动一个状态，不必次次重写整张图；损坏记录会被识别。动作已生效、结果尚未提交时遭遇强杀，仍可能需要重做，不能许诺外部副作用只发生一次。

正文队列优先保留 HTML、脚本和接口文本；图片、字体等二进制默认只记元数据。图查看器也预建索引，缓存最近八个视图，选节点只更新样式，保住缩放和平移。

04 / 技术升级

## 提速要和覆盖一起看

最新本机 18 轮对照中，分叉树、六层深链、延迟页面的吞吐分别约为基线的 1.09、3.42、1.20 倍。双方保留相同默认截图、请求间隔和策略，状态指纹、成功动作及实际有响应 API 集合一致。范围和危险动作拦截没有放宽；图导出与报告等收尾成本，也计入了采集基准。深链收益明显，分叉场景较小，这才是结果的真实形状。

当前本地 Web/MCP 版本通过 183 项回归。这不是整仓移动端验收，也不能外推为所有站点的固定倍数；测试环境是 macOS、Node 26 和本机夹具。

05 / 技术升级

## 这些提升，具体用了什么技术

|  |  |
| --- | --- |
| Playwright / Chromium | 真实点击、页面观察与网络证据 |
| MutationObserver / 活动代次 | 复用已稳定观察，动作后重新检查 |
| 语义指纹 | 验证刚构建状态后再继续探索 |
| journal + fsync + compact | 增量先落盘，再合并完整快照 |
| CDP Network | 记录浏览器提供的请求发起上下文 |
| Map 索引 / LRU / SVG 复用 | 减少查询扫描与重复画布构建 |

系列展望：下一步，让网站和 App 的观察信息，逐步形成可生成、可验证、可更新的 MCP 能力。

这次升级的价值，是让重复成本更少，让覆盖和恢复证据仍然可查。接下来遇到更复杂的站点，也有一套能复跑、能对照的办法回答：快在哪里，漏没漏。

关注后续进展

BFS Clicker

欢迎加入Moonlight安全交流群～一起探索安全姿势

github.com/8eeth0ven/bfs-clicker ↗![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/vP5icicMocf9gLIicOHuM0kJr2y9iatpnchQqaLBMRLpycEe2pVXZXf1jjonHHic6DDaiah5bOSMSGLsVytBmjQQ5PNyibYo6Dy8Lr6mr9FkqEVIME/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

BFS CLICKER / SERIES 01 / 2026

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icm3TqwJIic5jOEtrL6tj26a9ALCsb485iaxPGtEBmk3QfHB3OJnRryNpUloSzrpCyOVO0S4AvCgxLZ1fZ3aVDZYw/0?wx_fmt=png)

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