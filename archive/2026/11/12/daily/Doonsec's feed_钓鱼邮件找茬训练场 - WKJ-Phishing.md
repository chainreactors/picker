---
title: 钓鱼邮件找茬训练场 - WKJ-Phishing
url: https://mp.weixin.qq.com/s/ZbHBR-uQLLljjRI8fTcYPw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:57:23.839051
---

# 钓鱼邮件找茬训练场 - WKJ-Phishing

# 钓鱼邮件找茬训练场 - WKJ-Phishing

GSDK
GSDK

GSDK安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

01项目地址

`https://github.com/Jiafu318/wkj-phishing`

02项目介绍

安全意识培训年年做，钓鱼邮件防御年年讲，效果怎么验证？

`PPT 上写"注意仿冒域名"，员工点头，
真收一封 BEC 邮件，照样把 18.6 万转出去，
培训考核就是判断题"以下哪个是钓鱼邮件"，
考完就忘，因为从头到尾没"亲手"上过当。`

**WKJ-Phishing** 是一个纯静态的单页钓鱼邮件找茬训练工具：读一封模拟邮件，凭自己的判断**点出可疑之处**，提交后逐条对照解读——看到什么线索、为什么需要警惕、下一步应该怎样核实或处理。它不模拟真实攻击、不收集任何数据，只做一件事：把"识别钓鱼邮件"从一句口号拆成一条条可以练习的判断。

内置题目就是经典 BEC 场景：「CEO 王总」要求 3 点前完成 18.6 万转账——发件域名 company-group.cn 冒充 company.com、"不要跟其他人说"的保密话术、陌生收款账户，全部等你亲手标出来。

![标记风险点](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA18X2ITKxn2RaOVw0xsSuqHoerAqX7Kt9oaDSr9TOAxXiciabj0ZJcGD8qY2IzOhI0KFApbFsbrXw1jYUbibNFhyzxHAY4HdQj1mRc/640?from=appmsg)

标记风险点

**一句话概括：钓鱼邮件"找茬"训练场——点出可疑处才得分，点错倒扣，每个风险点都教你"为什么 + 下一步怎么做"。**

03核心亮点

`🧠 两类线索分开教：「硬证据」（仿冒域名、陌生收款账号、索要验证码）与「话术手法」（紧迫时限、保密要求、权威包装）分色标注，不把单一表象直接判为恶意
🖱️ 点击标记交互：点击邮件里任何可疑的文字、按钮、链接或发件人地址，再点一次取消；桌面手机完全同款交互
🧮 误点轻惩罚：非风险区域每次 -1 分（规则答题前明示），命中按严重度加权（低+1 / 中+2 / 高+3 / 严重+4），碰运气无利可图
📖 不止告诉你错：每个风险点给"为什么危险 + 正确做法"，每封邮件附"下一步怎么做"——用通讯录号码致电确认、大额只认合同审批流程、转交安全部门备案
🧩 加题零门槛：题目全在 index.html 的 EMAILS 数组，一封邮件一个对象，追加刷新即生效，标注语法有文档
🚫 零依赖零收集：无登录、无后台、无跟踪，所有内容随页面一次性加载，双击 index.html 就能跑`

![首页](https://mmbiz.qpic.cn/mmbiz_png/Wq4VJsQicA195SW1MAHRkp1tUc32vAZhK0q8UTN2wrCtSd4QZHq3FZluz6m8tB7gVjNuR05FaPlZAiciaSVFlEJt8iaxiaUUhTkWtvJHk9icxSTQ8/640?from=appmsg)

首页

04快速开始

**在线直接体验**（GitHub Pages 托管，无需登录）：

`https://jiafu318.github.io/wkj-phishing/`

本地运行或内网部署给学员用：

`git clone https://github.com/Jiafu318/wkj-phishing.git
cd wkj-phishing
python -m http.server 8000        # 或 npx serve .

# 容器部署
docker run -d -p 80:80 -v $(pwd):/usr/share/nginx/html:ro nginx:alpine`

训练流程：选题 → 标记 → 提交（不提示点没点对）→ 统一揭示解读 → 按处置建议行动。当前内置 6 封邮件、48 个风险点，不保存进度和成绩——刷新即重置，这是有意的隐私取舍。想做内部培训，直接照文档往题库里加自己公司的模拟场景就行。

设计取舍也很清醒：不设 hover 提示（等于把答案标出来）、误点轻惩罚而非零成本、不做账号体系和数据收集——一个可以直接发给学员的练习页面。

⚠️ 免责声明

注：工具仅供安全研究与学习之用，若将工具做其他用途，由使用者承担全部法律及连带责任，作者及发布者不承担任何法律及连带责任。信息及工具收集于互联网，真实性及安全性自测！！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xu1xJEZRrFjUe1HmsusbqLJiaQvscUlHp1kgYagMRTFy1TyiaryxmOjvkpS6UKic5ricVOjdicibiaLMTibKkUqiafYD8vw/0?wx_fmt=png)

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