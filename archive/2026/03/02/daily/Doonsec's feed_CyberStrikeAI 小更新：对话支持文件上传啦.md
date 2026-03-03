---
title: CyberStrikeAI 小更新：对话支持文件上传啦
url: https://mp.weixin.qq.com/s/vWJncUaUsJNowksPXq0hPw
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:07:33.198206
---

# CyberStrikeAI 小更新：对话支持文件上传啦

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ufQ2xnAD33vm8pgNBDRw43L2nvTtWsW0fZYibSa2B9ARBXe21FZ6OGbVLULUNb9mHqBNT4PKS66iaCRKF6AaRK4oSxVuSqoR2Sly22TibJ8H1s/0?wx_fmt=jpeg)

# CyberStrikeAI 小更新：对话支持文件上传啦

原创

学安全也就图一乐
学安全也就图一乐

低调学安全

![]()

在小说阅读器中沉浸阅读

**一次小更新，让对话更顺手。**

CyberStrikeAI 作为 AI 原生安全测试平台，一直在围绕「对话」做体验优化。这次我们加了一个很多人提过的能力：**在对话里直接上传文件（支持点击上传和拖拽上传）**，让 AI 能基于你提供的二进制文件、压缩包、文档、配置、日志等内容做分析和测试。

![](https://mmbiz.qpic.cn/mmbiz_png/ufQ2xnAD33tkMJ1guIcU1Jsd0mtY4prrKSmeNAk49IUO9HPYIrQ14VK7MDDrdDzar21ibqiag1HsTUsldv5EJxM9uwYa7oCPBBrfjBDQvhy0M/640?wx_fmt=png&from=appmsg)

---

## 能做什么？

* **上传方式**：在输入框旁点击「上传」按钮选择文件，或者**直接把文件拖拽到输入区域**，支持多选。
* **数量**：单次最多上传 **10 个文件**，满足多文件联动的分析场景。
* **类型**：不限制格式，文本、配置、脚本、日志等都可以。系统会按类型智能处理：

+ 文本类（如 .txt、.json、.xml、.yaml、.log 等）：内容会直接给模型，便于快速理解。
+ 其他类型：以后端约定方式交给模型，并会保存到本地路径，模型可通过工具按路径读取。

* **不发文字也能用**：只上传、不输入任何文字时，会默认发送一句「请根据上传的文件内容进行分析」，你只需选好文件点发送即可。
* **可追溯**：上传的文件会按日期和会话保存到 `chat_uploads` 目录，对话历史里也会保留附件名与路径，方便审计和后续继续聊。

---

## 典型用法

* 丢一份 **配置文件 / 接口文档**，让 AI 帮你做安全配置检查或接口测试建议。
* 上传 **漏洞报告、扫描结果**，让 AI 做摘要、风险排序或复现步骤整理。
* 贴 **日志片段**，让 AI 协助排查异常或识别攻击特征。
* 上传 **脚本或规则文件**，让 AI 结合当前角色/Skills 做代码审查或加固建议。

---

## 小结

这次更新不大，但让「带着文件聊」变成了默认能力：**选文件或拖进去 → 可选填一句说明 → 发送**，AI 就能结合文件内容做分析、测试建议或执行后续工具调用。

如果你在用 CyberStrikeAI 做内网/渗透/合规类测试，不妨试试在对话里直接挂上目标配置或日志，体验会顺很多。

---

*CyberStrikeAI — AI 原生安全测试平台，从对话到漏洞发现与攻击链分析，一站搞定。*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

低调学安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KzNYA6icKe6ny3nDMkDelsYYnPJzRX2erWFEia2S7Bqqc7CjicEpJYQtId7a2jXKCial6Mw8ck8IFQEqmZnldrG2EQ/0?wx_fmt=png)

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