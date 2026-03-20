---
title: 我 Vibe Coding 了一个日本看房神器：BukkenAI
url: https://blog.einverne.info/post/2026/03/bukkenai-ai-powered-japan-real-estate-neighborhood-analysis.html
source: Verne in GitHub
date: 2026-03-19
fetch_date: 2026-03-20T04:07:06.525357
---

# 我 Vibe Coding 了一个日本看房神器：BukkenAI

[Verne in GitHub](/)

* [Archive](/archive.html)
* [Categories](/categories.html)
* [Friends](/friends.html)
* [Tags](/tags.html)
* Other
  + [About](/about.html)
  + [投资笔记](https://invest.einverne.info/)
  + [券商推荐](https://broker.einverne.info/)
  + [图书分享](https://book.einverne.info/)
  + [相册](https://photo.einverne.info/)
  + [Kindle 笔记](https://kindle.einverne.info/)
  + [IPFS 镜像](https://ipfs.einverne.info/)
  + [服务状态](https://status.einverne.info/)
  + [在线嘟嘟](https://m.einverne.info/%40einverne)

# 我 Vibe Coding 了一个日本看房神器：BukkenAI 输入地址，AI 自动分析周边环境、车站、灾害风险

Posted on 03/19/2026
, Last modified on 03/19/2026
by [Ein Verne](https://x.com/einverne)
| [View revision history](https://github.com/einverne/einverne.github.io/commits/master/_posts/2026-03-19-bukkenai-ai-powered-japan-real-estate-neighborhood-analysis.md)

最近在东京认真找房子，每次拿到一个物件地址，我都要重复做同样一套操作：打开 [[Google Maps]] 搜地址，确认大概位置；找最近的车站，看步行距离；切到 Yahoo 地图查灾害风险图；再搜一圈附近有没有超市、医院、药局。做完一遍下来，十几分钟就过去了，物件多的时候，这些重复的信息收集工作比看房本身还累。某天做完第 N 遍之后，我决定干脆自己做一个工具，输入地址，全部自动搞定。这就是 [BukkenAI](https://bukkenai.com) 的起点。

## 看房人的重复劳动

日本的看房信息通常只有地址和最近车站，缺乏对”周边生活环境”的系统性描述，不同平台的信息分散，每次都要自己东拼西凑。交通方面要查最近的车站是哪个、步行几分钟、有几条线路可以换乘；生活便利方面要找附近的超市、便利店、药妆店；医疗方面要确认最近的医院、诊所、药局在哪里；还有小孩就学的学区划分、周边的绿地公园，以及这一带的灾害风险——洪水、滑坡、海啸——在日本这个自然灾害频发的国家，买房或租房都不能忽视这件事。每一条信息单独查都不难，但要每次都把这些全部查完，拿着手机在多个 App 之间反复横跳，是一件相当磨人的事情。

## Vibe Coding 开干

我是以”Vibe Coding”的方式来做这个项目的——不是从零开始设计架构，而是带着一个具体的痒点，边做边想，边想边改。用 [[Claude Code]] 作为主要的编程助手，迭代速度比我以往做 side project 快很多，很多时候是先把想法说给 AI，它出一版实现，我来 review 和调整，如此反复。技术栈上没有太多纠结：后端用 [[FastAPI]] 加 [[SQLAlchemy]] 异步 ORM 和 [[PostgreSQL]]（带 PostGIS 地理扩展），前端是 [[Next.js]] 搭配 [[React]] 和 [[TailwindCSS]]，数据来源是 [[Google Maps]] Places API 负责周边设施搜索，国土交通省的 REINFOLIB API 提供灾害风险和地价数据，最后用 [[Claude]] API 把收集到的数据汇总成一份可读性强的分析报告。

## 核心功能拆解

整个核心流程只需要输入一个日本地址，系统就会在几十秒内完成：用 Google Places API 搜索周边一千到一千五百米范围内的各类设施，查询国土交通省的灾害风险图数据，拉取同区域近三年的房价交易参考，最后把这些数据交给 AI 做综合分析，生成报告。

报告的核心是六个维度的评分，全部采用零到十分制，分别是教育、医疗、交通、自然环境、安全和生活便利。评分逻辑特意设计成”距离优先”——距离最近设施的远近是主要信号（零到七分），数量作为加成（零到三分）。这样可以避免”设施数量多但全都在两公里外”这种情况被高估，实际上距离最近的那家超市或者车站距离，才是真正影响日常生活感受的关键数字。安全维度则从满分起扣，高风险区域扣三分，中风险扣一点五分，低风险扣零点五分，直接反映灾害风险的轻重。

灾害风险分析是我个人觉得最实用的功能之一。日本的地震、洪水风险在各地区差异很大，但这类信息平时不太容易直观地查到，很多人买房的时候也容易忽视。BukkenAI 接入了国土交通省的 REINFOLIB API，可以查询洪水淹没、土砂灾害（滑坡）、海啸、高潮（台风引发的风暴潮）四类风险，每类风险标注高中低三个等级，并显示最近的指定避难场所位置。

## 图片一键提取地址

找房过程中经常会收到物件的截图，地址就印在图片里，手动打字输入是一件小而烦的事。所以我加了一个图片上传功能：上传物件照片或截图，AI 自动 OCR 识别并提取地址，确认后直接进行分析。这个功能做完之后自己用起来确实方便，有时候对方发来的图片质量并不高，识别结果还需要手动确认一下，但大多数情况下准确率不错，省去了不少打字的工夫。

## 报告版本与分享

每份报告都有固定 URL，可以直接分享给家人或者一起看房的朋友，对方打开就能看到完整的分析内容，不需要注册账号。考虑到周边环境会随时间变化——新车站开通、新医院开业、新的楼盘落成——报告支持”重新生成”，使用最新数据生成新版本，同时保留旧版本可以对比查看，这样可以追踪一个区域的环境变化情况。

## 最后

整个项目从第一行代码到上线，用了大概两三周的业余时间，功能比我最初预期的要丰富不少。Vibe Coding 的最大体验是：可以快速把一个”有点烦”的真实需求变成可用的东西，而不是被技术细节卡在起步阶段。当然代价是需要持续地和 AI 一起 review 生成的代码，尤其是涉及数据准确性、缓存策略、权限控制这些地方，不能完全放手，生成的代码质量参差不齐，还是要靠自己把关。如果你也在日本找房，或者对某个地址的周边环境感到好奇，欢迎去 [BukkenAI.com](https://bukkenai.com) 试试，输入一个地址看看报告长什么样——因为 Token 使用有成本，所以设定了限制，未登录用户有一次免费额度，注册之后有三次。

## Related Posts

* [我 Vibe Coding 了一个日本看房神器：BukkenAI](/post/2026/03/bukkenai-ai-powered-japan-real-estate-neighborhood-analysis.html) - 03/19/2026
* [CopilotKit：让你的 React 应用 10 分钟拥有上下文感知的 AI Copilot](/post/2025/12/copilotkit-intro.html) - 12/09/2025

---

* [← Previous（前一篇）](/post/2026/03/entire-git-ai-session-capture.html "Entire：让 AI 编程会话成为 Git 历史的一部分")
* [Archive（目录）](/archive.html)
* Next（后一篇） →

---

如果要使用 Remark42 进行评论确保访问的域名为 <https://blog.einverne.info> 或者点击 [这里](https://blog.einverne.info/post/2026/03/bukkenai-ai-powered-japan-real-estate-neighborhood-analysis.html)评论。

* [产品体验 210](/categories.html#产品体验)

* [vibe-coding 1](/tags.html#vibe-coding)
* [japan 7](/tags.html#japan)
* [real-estate 1](/tags.html#real-estate)
* [side-project 1](/tags.html#side-project)
* [ai 53](/tags.html#ai)
* [nextjs 3](/tags.html#nextjs)
* [fastapi 2](/tags.html#fastapi)

---

© 2026 Ein Verne. Powered by [Jekyll](http://jekyllrb.com "The simple, blog-aware, static site generator."). Hosted on [GitHub](https://github.com/einverne "Ein Verne's GitHub Repos") & [IPFS](https://ipfs.einverne.info "IPFS") & [BandwagonHost](https://gtk.pw/bwg "my own vps"). Join [Telegram group](https://t.me/%2BRUBhyY60iVcl6hdX "Verne's Blog Telegram Group").