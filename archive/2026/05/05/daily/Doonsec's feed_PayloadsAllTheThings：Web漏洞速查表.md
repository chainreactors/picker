---
title: PayloadsAllTheThings：Web漏洞速查表
url: https://mp.weixin.qq.com/s/qqbuxNFua4wF3ZJlDufewA
source: Doonsec's feed
date: 2026-05-05
fetch_date: 2026-05-06T05:08:59.501941
---

# PayloadsAllTheThings：Web漏洞速查表

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0zk3Ye7cp03kes7fsKfJhotg9mLpaibibI5unpszuP3L1iaYSt4yBGRMgTA1OaHlF4EgaKnANan8W10FHdVd3ZJoBrOGEQVtxr73MqovELQR30/0?wx_fmt=jpeg)

# PayloadsAllTheThings：Web漏洞速查表

原创

攻防路
攻防路

攻防录

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 简介

`PayloadsAllTheThings` 是一套按漏洞类型整理的 Web 安全知识库。它不只收 payload，还把绕过思路、测试方法、配图、样例文件和参考资料一起放进去了。

项目地址： https://github.com/swisskyrepo/PayloadsAllTheThings/

在线文档： https://swisskyrepo.github.io/PayloadsAllTheThings/

和很多“把 payload 往记事本里堆”的项目不一样，`PayloadsAllTheThings` 更像一套漏洞战术库。你能在里面看到同一个漏洞类型的默认打法、绕过路径、工具名单、实验链接和样例文件，而不是只看到几行字符串。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp02OMYalQuAUwYicb921RaCrMWgZJ5icBF0dprTarGacliafBU936qVhXkSuTkvOUngB6NICIeaMhcJZPgY66U8ibTKiavPp31Bor5Yg/640?wx_fmt=png&from=appmsg)

## 技术原理

这个仓库的优势，不是某一条 payload，而是“怎么把同一类漏洞的测试路径整理成能复用的套路”。

README 里写得很直接，每个章节通常会包含四类内容：

| 组件 | 作用 | 适合什么时候用 |
| --- | --- | --- |
| `README.md` | 漏洞说明、利用思路、典型技巧、参考资料 | 先建立方法感 |
| `Files/` | 样例文件、测试载荷、演示附件 | 做靶场和本地验证 |
| `Images/` | 图示、流程图、结果图 | 快速看懂边界和差异 |
| `Intruder/` | Burp Intruder 可直接喂的字典或样本 | 跑批量验证和模糊测试 |

本地拉下仓库后做了一次统计，当前仓库里能直接看到：

| 维度 | 数量 |
| --- | --- |
| 顶层漏洞章节 | 64 |
| `README.md` 文件 | 66 |
| 图片资源 | 83 |
| `Intruder/` 目录 | 8 |
| `Files/` 目录 | 12 |

它不是一份单文档，而是一套长期维护的漏洞材料库。

![](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp0179VvouacQb8s6q6Y4obbyFn4SaUq63p4KMPkvL9E8Ribe1jKACKQAxibicUWkReY1Cfaa48iaWa3ufKiaEdP7Rm2Xcw4PVJCJNxfA/640?wx_fmt=png&from=appmsg)

如果你看几个代表性章节，会发现它们几乎都不是“先丢 payload，再说别的”，而是先给测试路径，再给细分变体。

这些章节的共同点很明显：

1. 先用 `Summary` 把读者带进目录。
2. 再按 `Methodology`、`Bypass`、`Tools`、`Labs`、`References` 展开。
3. 有图就给图，有文件就给文件，需要批量测试时再补 `Intruder/`。

这套写法很适合安全工作。因为真实测试不是一句 payload 打天下，而是先判断入口，再看过滤逻辑，再决定是人工验证、样例文件、还是批量 fuzz。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0zk3Ye7cp01iaHZOwdPN2C5FD3509Iyq8kYsAgqFGUDMwfxZABib7AQySy1SHp1uPdzbDsOwP7sja0b81h5pdHtCS6S1ULt3Ecsvtg4y86jIY/640?wx_fmt=png&from=appmsg)

仓库根目录里放了 `mkdocs.yml`，主题用的是 `Material for MkDocs`。这意味着同一份 Markdown 内容，可以同时服务两种入口：

| 入口 | 优点 | 适合人群 |
| --- | --- | --- |
| GitHub 仓库 | 方便协作、提交 PR、直接看原始文件 | 维护者、贡献者 |
| 在线文档站 | 搜索、目录、阅读体验更好 | 日常查资料的人 |
| 本地 clone + `rg` | 搜索速度快，适合离线整理 | 审计、培训、做手册的人 |

很多人第一次打开 `PayloadsAllTheThings`，容易把它当成“payload 仓库”。其实更好的用法是先按漏洞类别看测试路径，再决定要不要把某条样例拿去验证。

比如：

1. SSRF 章节先讲目标、过滤绕过、协议利用，再落到工具和实验。
2. Upload 章节先讲扩展名、MIME、魔术字节、文件名，再讲图像压缩、元数据和 ImageMagick。
3. IDOR 章节会把枚举目标从数字 ID 扩展到邮箱、哈希、对象 ID 和通配符。

这才是它长期好用的原因。你拿到一个新系统时，不一定马上知道 payload，但通常能先知道“该从哪种路径试起”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0zk3Ye7cp02IHnrWib2aiaUlm0Qp2tnedqezh3YBcLatvQrP3SIo20yLEB2oia15Z90XsX4diabGiazDhaqP7tDpibGicpcspMF8LMITVAJ9zZ7VNA/640?wx_fmt=jpeg)

## 快速上手

### 1. 拉取仓库拉到本地

```
git clone https://github.com/swisskyrepo/PayloadsAllTheThings.git
cd PayloadsAllTheThings
ls
```

### 2. 从一个熟悉漏洞开始，先读 `Summary` 和 `Methodology`

```
sed -n '1,120p' 'Server Side Request Forgery/README.md'
sed -n '1,120p' 'Upload Insecure Files/README.md'
```

建议别一上来就看 payload。先看章节怎么分段，特别是 `Summary`、`Methodology`、`Labs` 这些位置，能更快建立测试路线。

### 3. 用 `rg` 按关键词横向搜索

```
rg -n "bypass|polyglot|metadata|redirect|gopher" .
rg -n "^## Tools" .
```

`PayloadsAllTheThings` 适合横向搜。比如你在做文件上传审计，想看 `metadata`、`polyglot`、`magic bytes`，直接搜会比一个个目录翻快很多。

## 使用场景

### 1. 授权测试前的速查

**任务示例**：接到一个 Web 审计项目，先按业务功能判断它更像 SSRF、上传、IDOR 还是模板注入，再去对应章节看测试路径。

**技术要点**：先看 `Methodology` 和 `Tools`，再决定是否要用章节里的样例素材，不要反过来先挑 payload。

### 2. 团队培训和知识库整理

**任务示例**：给新同事做 Web 安全培训，按章节挑 3 到 5 个漏洞家族，直接用仓库里的图和结构做讲义。

**技术要点**：这个仓库的好处是章节结构相对统一，拿来改内部文档时不容易散。

### 3. Burp、靶场和本地实验素材补充

**任务示例**：在授权靶场里补充文件样例、字典、截图和练习资料，不想每次都手工拼装。

**技术要点**：优先看 `Files/` 和 `Intruder/`。这两个目录比 README 更像“能直接拿来练”的部分。

### 4. 代码审计时的思路校对

**任务示例**：审一段上传、跳转、模板渲染或参数鉴权逻辑时，用仓库对应章节做思路对照，避免只盯一种漏洞变体。

**技术要点**：它更适合做“思路清单”，而不是直接替代人工判断。特别是在授权控制、业务逻辑和上下文约束这类问题上，仍然要回到代码和流量本身。

往期推荐 📚

[taste-skill：AI前端审美外挂](https://mp.weixin.qq.com/s?__biz=MzY5ODAyOTAwMg==&mid=2247484810&idx=1&sn=26bdcc11d8d2221d3d6d7694a78d2118&scene=21#wechat_redirect)

[GPT-Image-2 提示词模板库](https://mp.weixin.qq.com/s?__biz=MzY5ODAyOTAwMg==&mid=2247484779&idx=1&sn=e68487ce016b54a7e6bdb920a04047a6&scene=21#wechat_redirect)

[给 AI 装上黑客大脑：hack-skills](https://mp.weixin.qq.com/s?__biz=MzY5ODAyOTAwMg==&mid=2247484729&idx=1&sn=071a29c95f77d9960cc24bf7bb283885&scene=21#wechat_redirect)

欢迎关注“攻防录”✨

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

攻防录

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

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