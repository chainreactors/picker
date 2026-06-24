---
title: 15MB干翻DBeaver！这款国产神器支持40+数据库，还自带AI助手，太香了！
url: https://mp.weixin.qq.com/s/lbnElR_zCC1OLiLa9-CJsw
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:01:02.748371
---

# 15MB干翻DBeaver！这款国产神器支持40+数据库，还自带AI助手，太香了！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kztGyHFwmfxTG7ttJzo0STEbcx78GstWkzlv3rx68WfflqJP0LO1YqF1slp5802RrZnXibglMnaWcMXuk0x3uhgvlDugEqItDHzw66d6StYI/0?wx_fmt=jpeg)

# 15MB干翻DBeaver！这款国产神器支持40+数据库，还自带AI助手，太香了！

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

大家好，我是日常跟各种数据库打交道的开发者。以前用 `DBeaver` 要装 `Java`，用 `TablePlus` 只能 `Mac`，用 `Beekeeper Studio` 又觉得不够强……每次换电脑、换项目都要折腾半天，烦！

![图片](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfz9EPs3A4lBovhPPKwbP5Fh5aSybiagagTaKibqyFw65CL1Gkrucd4pXtxNeFvnRpu5bicmuICVbuRfJKSIglRqy2JVng6mpREn9k/640?wx_fmt=png&from=appmsg)

直到我遇到了 **DBX** —— 一个只有 **15MB** 的数据库客户端，直接把我震惊了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfzteXSWPraTtIDck7mUYwD27YfXzJP8MXnEfHDFsVGG0b52wgmeibhIUbVbAo3ZKoiaiaHt7RksYEm97NXSsIAPQBGBJB1j1N1laM/640?wx_fmt=png&from=appmsg)

## 为什么说 DBX 要“爆”？

### · · · 1. 极致轻量，真正的“下载即用” · · ·

* ●单个二进制文件，**15MB** 左右
* ●**无需 `Java`、无需 `Python`、无需 `Chromium`**，全平台（`Windows`、`macOS`、`Linux`）原生运行
* ●对比 `DBeaver` 那庞大的运行时依赖，`DBX` 简直是“轻量化战士”

### · · · 2. 一工具通吃 40+ 数据库 · · ·

支持 `MySQL`、`PostgreSQL`、`SQLite`、`Redis`、`MongoDB`、`DuckDB`、`ClickHouse`、`SQL Server`、`Oracle`、`Elasticsearch`、`TiDB`、`OceanBase`、`Doris`、`StarRocks`……还有一大堆国产数据库（`KingBase`、`GaussDB`、`DM` 等），甚至通过 `JDBC` 还能扩展更多。

再也不用为不同数据库装一堆客户端了！

### · · · 3. 内置 AI SQL 助手，生产力直接起飞 · · ·

* ●在编辑器里选中表，用自然语言描述需求（“帮我查最近 7 天订单总额 `Top10`”），`AI` 直接生成 `SQL`
* ●还能解释 `SQL`、优化语句、修复错误
* ●支持 `Claude`、`OpenAI`、`Ollama` 本地模型，并且**内置安全检查**，防止 `AI` 乱写危险语句
* ●这才是真正的“`AI` 原生”工具，不是后面加个插件那么简单

### · · · 4. `MCP` 协议加持，让 AI 编程助手直接用你的数据库 · · ·

这是我认为最黑科技的功能之一：

* ●通过 `MCP Server`，**`Claude Code`、`Cursor`、`Windsurf`** 等 `AI` 编码助手能直接调用你已经在 `DBX` 配置好的数据库连接
* ●配置一次，`AI` 编程时就能实时查数据、写 `SQL`，效率拉满！

### · · · 5. 强大到离谱的功能集 · · ·

* ●现代查询编辑器（`CodeMirror 6` + 智能补全 + 多主题）
* ●虚拟滚动数据表格，支持百万级数据轻松浏览、行内编辑、`DataGrip` 风格过滤
* ●`Schema` 浏览器、`ER` 图、结构对比、执行计划、字段血缘分析
* ●`Redis`/`MongoDB` 专项浏览器
* ●数据导入导出、迁移、对比、`SQL` 文件执行
* ●`SSH` 隧道、危险操作确认、加密配置等安全功能
* ●深色模式 + 精致 `UI` + 自动更新

### · · · 6. 桌面 + `Docker` + `Web` 三种形态 · · ·

* ●本地桌面 `App` 最丝滑
* ●`Docker` 一键自托管，团队共享用 `Web` 版
* ●浏览器纯 `Web` 环境也能用，配置同步

## 安装超级简单

* ●**`macOS`**：`brew install --cask dbx`（或从 `Releases` 下载）
* ●**`Windows`**：`Scoop` 一键安装
* ●**`Docker` 自托管**：

```
  docker run -d --name dbx -p 4224:4224 -v dbx-data:/app/data t8y2/dbx
```

浏览器访问 `http://localhost:4224` 即可。

### · · · 项目演示 · · ·

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxtv5J7qpR14RJmfc7wsCkC0U4YRapPwSib4DXJ5oHfh1mOtpkeiarMQdvqzby6ibp6IiajXEda1PpTCibvzR4HAUfxMlTy4a4GB4iao/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfz53aRiaMQAEnP0uo8icb2Hz6hx7ZTia2pE24DUqKibvkDXiayNfEpkL2YtmLswYnxynpBwolKJGbck9aibfh8jqaOI1O2meOo3DnNqk/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfyh8dicfPwAkkb3QmMBAfkMe9BwK6NYMLemLCuayNvMEn6pqEVRfUlP9WboBVy526ictCANReURBeFtGLg1bmmUVdyMCeF5gQQkA/640?wx_fmt=png&from=appmsg)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfx3mfWbXgTVe8o4kQk3ibTibYib9oxicvF6wfWTsibvq3GWI1sP6Y0nevLlhx7esCkDeIy3XLOQadvotczoshv39lkf2fS150fSehW0/640?wx_fmt=png&from=appmsg)

完全开源（AGPL-3.0），**不收集任何遥测数据**，离线可用（AI 功能需联网或本地模型）。

### · · · 谁适合用 DBX？ · · ·

* ●后端开发者、`DBA`、数据工程师
* ●`AI`时代想让大模型直接操作数据库的玩家
* ●追求轻量、跨平台、不想折腾环境的极客
* ●团队需要自托管数据库管理工具的公司

GitHub地址[1]

我已经把它设为日常主力工具了。用了之后，真的回不去了——轻、快、全、聪明，这四个字它都占全了。

你还在用那些又大又重的老客户端吗？欢迎评论区说说你的数据库管理痛点，或许`DBX`就是那个能解决你所有烦恼的神器！

**点赞 + 转发**，让更多开发者看到这个宝藏项目！🚀

参考资料:

[1] GitHub地址: https://github.com/t8y2/dbx

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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