---
title: 一张图片拿下 Rails 服务器，CVSS 9.5 命令执行零门槛
url: https://mp.weixin.qq.com/s/birSjBq7p5wjoxnPCUfFow
source: Doonsec's feed
date: 2026-07-30
fetch_date: 2026-07-31T05:27:51.194441
---

# 一张图片拿下 Rails 服务器，CVSS 9.5 命令执行零门槛

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LAQpgdWQScu3YT5IdVQJlwPmMRNjveEJibPcH4l0AH8p3JN1aP8h2XayxLt4bPvX4WoenPbKkC1AQWBQVphQiabZqbe1qhC86LpNqBibCAUEs4/0?wx_fmt=jpeg)

# 一张图片拿下 Rails 服务器，CVSS 9.5 命令执行零门槛

YGnight
YGnight

night安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LAQpgdWQSctVS8Ps0NsFTqMiasz8uDibcvoib0spt17ORFYGT7Lk8y0JElHpWukiczXboIicO8mrOUut0DwfE4PvMwpuReeibS0yQHqN8Tictdm4Z4/640?wx_fmt=png&from=appmsg)

用 Rails 7.x 或 8.x、又开了图片上传的朋友，先停下手里的活。攻击者根本不需要账号，往你的服务器丢一张普通的图片，就能拿到 进程级命令执行权限。一张带毒的头像图，足够把你的 Rails 服务摆上砧板。

一、危害

这是个被研究团队起名 KindaRails2Shell 的漏洞，编号 CVE-2026-66066，CVSS 9.5，严重级别。它最离谱的地方在于，攻击者连账号都不用有，丢一张看着人畜无害的图片到服务器，就能直接上手命令执行。

**CVSS 3.1** 评 9.5 分，网络可达、无需权限、机密性和完整性影响拉满。

**官方 CVE 编号** CVE-2026-66066，研究团队命名 KindaRails2Shell，影响 Rails 7.x 与 8.x 默认配置。

|  |  |  |  |
| --- | --- | --- | --- |
| 版本区间 | 受影响范围 | 修复版本 | 状态 |
| Rails 6.x | 6.0.0 - 6.1.7.10 | 7.2.3.2+ | 需非默认配置 |
| Rails 7.x | 7.0.0 - 7.2.3.1 | 7.2.3.2 | 受影响 |
| Rails 8.0.x | 8.0.0 - 8.0.5 | 8.0.5.1 | 受影响 |
| Rails 8.1.x | 8.1.0 - 8.1.3 | 8.1.3.1 | 受影响 |

注，7.x / 8.x 这几行在默认配置下即受影响，无需任何额外自定义，6.x 需非默认配置才会躺枪。

⚠️ 风险定性，Active Storage + vips + 未授权传图 三件套，在 Rails 默认配置下直接命中，公开站点零登录即被打穿。PoC 和利用链被 Ethiack 与 GMO Flatt 捂到 8 月 28 日才放，空窗期里难保没人已经私下跑通，风险偏高。

二、原理分析

问题出在 Rails 自带的 Active Storage 组件。它管文件存储和图片处理，几乎所有开了文件上传的 Rails 项目都在用。默认情况下，它调用 `libvips` 这个库，给用户传的图做缩略图和格式转换。

麻烦就在这个 libvips。在特定组合下，它存在可被利用的未授权文件读取和命令执行缺陷。只要满足三个条件，整条链就通，用了 vips 做图片处理、允许匿名用户传任意图片、跑在 Rails 7.x / 8.x 默认配置上。三件套一叠加，从传图到命令执行一气呵成。

只有一部分项目用 MiniMagick 当处理器，那种暂时不在该风险组合里。但官方 Docker 镜像和 Debian / Ubuntu 默认包带的都是 vips，所以用官方镜像或系统默认包的项目，默认就躺在这个风险组合中。

三、完整攻击链

技术细节被捂到 8 月 28 日才放，但触发条件极普通，生产环境里满地都是。整条链的走向大致如下，仅供防御侧理解，不展开任何可复现的利用代码。

1匿名上传带毒图片

攻击者无需登录，直接往头像或资料图上传接口丢一张精心构造的图片，看着和正常图没两样。

2Active Storage 调 libvips 处理

框架默认用 vips 生成缩略图、转格式，恶意图片被送进解析流程，触发点就在这。

3libvips 触发未授权文件读取

在特定组合下越权读取服务器任意文件，读取身份是 Web 进程，也就是 Rails 服务本身。

4拖走核心凭证

`config/secret_key_base`、Rails master key、数据库连接凭据、云存储密钥、API Token 悉数被读走。

5远程命令执行

借机写入 webshell，横向移动至内网，把这台服务器当跳板继续往里打。

📌 关键认知，从第一步上传到最后一步 RCE，全程不需要任何账号。公开站点只要开着匿名传图，基本等于裸奔，攻击者喝杯咖啡的功夫就能拿下进程级权限。

四、自主排查

下面两个排查都是只读动作，只确认你是否在风险组合里，请在自己的授权资产上跑，别对别人的站点用。

排查项 1 · 图片处理器核验

```
# 看图片处理后端bundle list | grep -iE "image_processing|libvips|ruby-vips"# 看 Active Storage 配置grep -rn "image_processing" config/ 2>/dev/null# 期望命中（在风险组合中）image_processing (1.x)libvips (8.x)ruby-vips (2.x)
```

排查项 2 · 上传路由与鉴权核验

```
# 列出上传相关路由bin/rails routes | grep -iE "active_storage|direct|upload|avatar"# 看附件模型是否对外放开grep -rn "has_one_attached\|has_many_attached" app/models/# 重点确认 direct upload 端点是否对匿名用户可达# 若未加鉴权即返回 200，则命中条件二
```

✅ 判定逻辑

· 命中 vips + 允许匿名上传 + Rails 7.x / 8.x 默认配置 → 立刻处置。

· 处理器是 MiniMagick → 暂不在该风险组合，但仍核对版本。

· 返回 401 / 404 或缺少上述特征 → 大概率已修复或已加固，但仍建议核对版本。

✅ 最稳妥

打开 `Gemfile.lock`，比对 rails、image\_processing、ruby-vips 版本与上方的版本表，版本落在受影响区间内的直接升。

五、修复防御方案

① 升级到修复版本

Rails 升到 7.2.3.2 / 8.0.5.1 / 8.1.3.1 或更高，libvips 同时升到 8.13 以上。只升 Rails 不升库挡不住，两边都得补。这是最直接有效的办法。

② 临时缓解

暂时升不动就设环境变量 `VIPS_BLOCK_UNTRUSTED=true`，或在 initializer 调 `Vips.block_untrusted(true)`（ruby-vips 2.2.1+）。这只是缓解，没根除，别当永久方案。

③ 给上传加鉴权

上传接口必须登录后才放行，别让匿名用户直接传图。另外别指望 WAF，它的拦截效果看你的存储方式和上传接收逻辑，参差不齐，救不了命。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LAQpgdWQSctTWicwicwovsVtMLAjYPfEB9lMRmJJiaIozWIuicwrbneXZ3pGly4lRNAd1WrP6AKYA925Iz4c1EbnMLCOqWzkCmdCLXDQibsG4VQw/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SaibaRNhOjqiaCicRfSc5cJ3oiaCRqb97SmncCWWvuTyytibyIDxB9ZXWOuNaiaGAX2t0DYAAbdJ7aicS6WeCz4wfMoUg/0?wx_fmt=png)

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