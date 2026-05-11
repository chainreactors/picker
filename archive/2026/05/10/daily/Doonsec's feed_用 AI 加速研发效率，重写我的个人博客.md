---
title: 用 AI 加速研发效率，重写我的个人博客
url: https://mp.weixin.qq.com/s/IuVfpkQETLX7wIbd6NPStQ
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:54:12.139830
---

# 用 AI 加速研发效率，重写我的个人博客

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/urdbr8VMr8uIiclJIezNgdpbgjwvvHjd26tpkfetOibuKDffYtDSW5UZ2T9wnM5zFklicx63AeSibavJnoFq5p0xU9IAfHRQEiafP2ictGsOAOhOI/0?wx_fmt=jpeg)

# 用 AI 加速研发效率，重写我的个人博客

原创

0x584A
0x584A

一个人的安全笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/urdbr8VMr8uHJO0FqMkuaCH7zvazlRkkc0jwQgBdjic91GA0n9oibjn5avpwBTb6PdJVZpzBwcstwIXvpFVYTzX01vP2ibYOwELDN2bOibe1yjw/640?wx_fmt=png&from=appmsg)

这是我重新写个人博客项目的 Git 记录，整体是这样的：

```
```
2023-12-26  项目初始化
2024-07-31  更换 UI 组件
2024-08-09  更新部分样式
2024-12-10  依赖升级
（———— 长达 5 个月的空白 ————）
2026-05-08  全面重写 Nuxt4（12 commits）
2026-05-09  功能完善（7 commits）
2026-05-10  收尾冲刺（10 commits）
```
```

前 500 天只动了 4 次代码，后面 3 天干了 29 个 commit。而**这 29 个 commit，每一个都由 AI 完成。**

而博客重写之前是长下面这样的，用的技术栈是 vuejs+go+mysql。而现在用的是 Nuxt+sqlite3，主打一个快、轻量化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/urdbr8VMr8scmicjmprzXRPvGIWfm9AYLklAUvLfBIFUtJrgn56OSqmHnPvErjQhu2bOpxjm3Cq8ibdJKkL8g87HD75YDGGvoI7kib9bEPtEibU/640?wx_fmt=png&from=appmsg)

三天内全程与 AI 的对话共分三个阶段：

| 阶段 | 内容 | commits | AI 参与 |
| --- | --- | --- | --- |
| 5/08 | Nuxt 4 框架搭建：列表页、详情页、样式 | 12 | 全程 |
| 5/09 | 功能完善：搜索、标签、密码保护、后台管理 | 7 | 全程 |
| 5/10 | 收尾：配色、Sitemap、RSS、清理、部署 | 10 | 全程 |

模型用的是：DeepSeek V4 Flash，合集费用：5 块钱。

人力成本：三天累计研发工时约 12 小时，AI 对话交互时间约 2 小时（分散在三天内）。其实 AI 成本基本可以忽略不计，DeepSeek 太特么便宜了。真正的大头永远是人的时间。

## # Feature 1：配色重构（人工决策 + AI 执行）

旧的配色方案是一年前随手调的：`#FF6600` 刺眼橙色做主色，蓝色链接、珊瑚色标题、粉色引用、紫色引用边框。四五种强调色主打一个各说各的。

![](https://mmbiz.qpic.cn/mmbiz_png/urdbr8VMr8vMAfuZyBgyPDBet8bROFhNuqGafMQq5ZCicRcD80c4K68uKZz1kFQlzXoLVPaslkJfXHf3cbT5WF3bahd1nZDiaribPsHviaLRDGg/640?wx_fmt=png&from=appmsg)

人工决策要用暖色系，确定设计方向差不多5 分钟吧。

AI对话帮我完成：扫描 `main.css` 和全部组件、生成完整配色替换方案、跨 5 个文件 20 多处批量修改、build 验证通过，8 分钟。

## # Feature 2：Sitemap 动态化（AI 定位 + AI 修复）

后台有个"刷新 sitemap.xml"按钮，点了永远不生效。人工排查可能要翻 Nuxt 文档半小时，AI 直接定位原因：

```
```
// 旧代码：写文件到 public/
writeFileSync(resolve(process.cwd(),'public/sitemap.xml'), xml)
```
```

Nuxt 生产环境下 `public/` 在构建时就打包进了 `.output/`，运行时写文件根本没更新实际文件的内容。点击按钮反馈说成功，实际无事发生。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/urdbr8VMr8txzicULGKAS7G83hklOu066NS8VaIZB5EjJSqRI24frofklc4qxqjUnXIJKBKJ7JzfECv0KCWEPqkgfHBEMjoaLoXe1PiaAIQ80/640?wx_fmt=png&from=appmsg)

AI 直接自己修复了这个问题，并改变了需求实现逻辑：改为动态路由，这样每次请求实时查数据库生成。

```
```
// server/routes/sitemap.xml.get.ts
exportdefaultdefineEventHandler(async(event)=>{
setHeader(event,'Content-Type','application/xml; charset=utf-8')
return xml
})
```
```

## # Feature 3：RSS Feed（AI 生成）

一句话需求："AppFooter.vue 有个 /feed 用于 RSS 订阅，也使用动态路由帮我实现"。AI 参照 sitemap 动态路由模式，生成 `server/routes/feed.get.ts`，20 行代码实现标准 RSS 2.0。

## # 完整研发时间线

```
```
5/0822:07 ── AI 辅助：修复样式，完善页面取值
5/0822:12 ── AI 辅助：完善首页 PopularTags
5/0822:23 ── AI 辅助：完善文章列表页
5/0822:42 ── AI 辅助：完善页面详情
5/0822:55 ── AI 辅助：完善 about 样式
5/0823:11 ── AI 辅助：完善数据查询、文章详情页样式
5/0823:18 ── AI 辅助：hljs 样式实现
5/0823:26 ── AI 辅助：优化样式
5/0823:31 ── AI 辅助：完善首页文章搜索功能
5/0823:47 ── AI 辅助：完善 tag 列表页面
5/0900:30 ── AI 辅助：完善文章密码验证
5/0900:37 ── AI 辅助：完善管理员登录和后台管理页面
5/0920:28 ── AI 辅助：完善用户会话状态判断
5/0921:56 ── AI 辅助：v1.0
5/0922:11 ── AI 辅助：修复生产发布前的问题
5/0922:21 ── AI 辅助：懒加载和 SEO 优化
5/0923:31 ── AI 辅助：优化
5/1000:54 ── AI 辅助：文章详情图片优化
5/1001:26 ── AI 辅助：优化生产部署错误
5/1001:49 ── AI 辅助：修复登录错误
5/1009:39 ── AI 辅助：完善 nginx 部署配置
5/1009:54 ── AI 辅助：优化整体颜色
5/1010:07 ── AI 辅助：完善介绍
5/1013:18 ── AI 辅助：修复 sitemap.xml
5/1013:28 ── AI 辅助：完善 RSS 订阅
5/1013:32 ── AI 辅助：完善脚本
5/1014:03 ── AI 辅助：优化代码残留
```
```

## # 最后

从 5 月 8 号第一条 prompt 到 5 月 10 号最后一个 commit：

* **人力投入：12 小时**

  ，这是真金白银的成本
* **AI 对话时间：约 2 小时**

  （分散在三天）
* **AI API 费用：几块钱**

几块能干什么？喝瓶快乐水的钱。但在 AI 的辅助下，一个拖了一年半没动的项目，三天内从零重写完毕。AI 的价值从来不是省那两毛七，而是把"不想动"变成了"试一下"，把"下次再说"变成了"现在搞定"。

> 嗯，这篇文章也是 AI 帮我写的。我目前就职的公司从去年就开始全员拥抱 AI ，到现在全员使用 AI，技术变革实在是太快了。能明显感觉到在 AI 的浪潮下，你要去接受它了解它，最重要是要学会使用它。

预览时标签不可点

阅读原文

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icAwZGuVmZqwSHjGhRbxn7zqVg44biaTkZrT9foJEcyC9k9WuBIvkyQ8TyaU0Wia8nDiaKOgW4kdM663g9bOPFmTxQ/0?wx_fmt=png)

一个人的安全笔记

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icAwZGuVmZqwSHjGhRbxn7zqVg44biaTkZrT9foJEcyC9k9WuBIvkyQ8TyaU0Wia8nDiaKOgW4kdM663g9bOPFmTxQ/0?wx_fmt=png)

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