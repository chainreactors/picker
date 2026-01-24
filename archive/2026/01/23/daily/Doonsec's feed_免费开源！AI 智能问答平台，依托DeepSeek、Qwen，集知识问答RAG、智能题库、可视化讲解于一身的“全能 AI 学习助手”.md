---
title: 免费开源！AI 智能问答平台，依托DeepSeek、Qwen，集知识问答RAG、智能题库、可视化讲解于一身的“全能 AI 学习助手”
url: https://mp.weixin.qq.com/s/pApBfa--nwiLvTgWGNBEzw
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:26:37.629901
---

# 免费开源！AI 智能问答平台，依托DeepSeek、Qwen，集知识问答RAG、智能题库、可视化讲解于一身的“全能 AI 学习助手”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKaZKuBYlT2jjeZLY4jzEVL3YEQxGx89pDZcd4oja4Ehfh1yQEQNs76Ow/0?wx_fmt=jpeg)

# 免费开源！AI 智能问答平台，依托DeepSeek、Qwen，集知识问答RAG、智能题库、可视化讲解于一身的“全能 AI 学习助手”

.
.

IoT物联网技术

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKauc8SkT3XibDPGyibJD66bibl6z1jWrdZkZnbiaThNIZ2ich33edl9sWIl9w/640?wx_fmt=other&from=appmsg)

> 文末联系小编，**获取项目源码**

DeepTutor是由香港大学 HKUDS最新开源的一款非常爆火的依托AI大语言模型（OpenAI、DeepSeek、Qwen等）的个人学习助手，集成了文档问答、可视化讲解、智能出题、深度研究于一体的“全能 AI 私教”。完美解决了自学路上的三大痛点：资料太多找不到答案、复杂概念看不懂、学会了没地儿练。

在 AI 教育这个赛道，有很多产品有的擅长语言教学，比如多邻国；有的擅长翻译，比如有道；有的擅长总结，比如豆包；有的擅长做题，比如小猿搜题。但能把 “学、练、测、研” 这一整套闭环全部打通，并且还开源免费的，DeepTutor 绝对是目前顶尖级别的选手。

📚 海量文档知识问答

智能知识库：上传教科书、研究论文、技术手册和领域特定文档。构建全面的 AI 驱动知识库，实现即时访问。

多 Agent 问题求解：双循环推理架构，集成 RAG、网络搜索、论文搜索和代码执行——提供带精确引用的分步解决方案。

🎨 交互式学习可视化

知识简化与解释：将复杂概念、知识和算法转化为易于理解的可视化辅助工具、详细的分步分解和引人入胜的交互式演示。

个性化问答：上下文感知对话，适应您的学习进度，提供交互式页面和基于会话的知识跟踪。

🎯 知识强化与练习题目生成器

智能练习创建：根据您当前的知识水平和特定学习目标，生成有针对性的测验、练习题和定制评估。

真实考试模拟：上传参考考试，生成完美匹配原始风格、格式和难度的练习题——为

您提供真实考试准备。

🔍 深度研究与想法生成

全面研究与文献综述：通过系统分析进行深入的专题探索。识别模式，连接跨学科的相关概念，综合现有研究发现。

新颖见解发现：生成结构化学习材料并发现知识空白。通过智能跨领域知识综合，识别有前景的新研究方向。

DeepTutor 不再是简单的搜题软件或者网课平台，它是一个真正懂你、能看见你的困惑、能陪你练习的 AI 智能体。

* 如果你是学生：可用它来复习备考，克隆真题，查漏补缺。
* 如果你是开发者：还能用它来啃那些晦涩的技术文档，通过可视化图表快速理解架构。
* 如果你是研究人员：那用它的深度研究模式来做文献综述就再好不过了。

**DeepTutor 平台技术架构**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKasVK3A9YRFTd63GqEGp0JSOCFSkDRYAImqnTicLMFLcKaNsLRiaF2vz5g/640?wx_fmt=png&from=appmsg)

💬 用户界面层

• 直观交互：简单的双向查询-响应流程，实现直观交互。

• 结构化输出：结构化响应生成，将复杂信息组织成可操作的输出。

🤖 智能 Agent 模块

• 问题求解与评估：分步问题求解和定制评估生成。

• 研究与学习：用于专题探索的深度研究和带可视化的引导式学习。

• 想法生成：自动化和交互式概念开发，具有多源见解。

🔧 工具集成层

• 信息检索：RAG 混合检索、实时网络搜索和学术论文数据库。

• 处理与分析：Python 代码执行、查询项查找和用于文档分析的 PDF 解析。

🧠 知识与记忆基础

• 知识图谱：实体-关系映射，用于语义连接和知识发现。

• 向量存储：基于嵌入的语义搜索，用于智能内容检索。

• 记忆系统：会话状态管理和引用跟踪，用于上下文连续性。

DeepTutor 运行环境

> Python 3.10+
>
> Node.js 18+
>
> LLM API 密钥（OpenAI、Qwen、DeepSeek 等）

```
# 克隆并设置git clone https://github.com/HKUDS/DeepTutor.gitcd DeepTutor# 配置 API 密钥cp .env.example .env# 编辑 .env 填入你的 API 密钥# 安装并启动bash scripts/install_all.shpython scripts/start_web.py
```

**DeepTutor 平台业务功能**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKakE9QNJ16DBdviaibrxzJq2qzPrnsojIcxr8Dzjjq0Ebopf5H56sUndibA/640?wx_fmt=png&from=appmsg)

引导式个性化学习系统：基于笔记本内容，自动生成递进式学习路径，通过交互式页面和智能问答，实时状态与会话持久化，笔记本内容自动分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKakE9QNJ16DBdviaibrxzJq2qzPrnsojIcxr8Dzjjq0Ebopf5H56sUndibA/640?wx_fmt=png&from=appmsg)

双模式题目生成系统：支持 基于知识的自定义生成 和 参考试卷模仿，带自动验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKaHCXwFa1gyibcPBwTj1YmKuBBGUKiaGGzLNhAbvUOJibYMfrUoicKf7icDSw/640?wx_fmt=png&from=appmsg)

智能问题求解系统：基于 分析循环 + 求解循环 双循环架构，支持多模式推理和动态知识检索，实时显示推理过程工具集成RAG (naive/hybrid)、网络搜索、查询项、代码执行持久化记忆基于 JSON 的记忆文件用于上下文保存引用管理结构化引用和引用追踪。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKa3QBOiaYiaJSKNGDMKExGnZAx0ibaHzGGLmXEtlibmUL8XR8fuCVHaCGYdQ/640?wx_fmt=other&from=appmsg)

智能 Markdown 编辑器，支持 AI 辅助写作、自动标注和 TTS 叙述。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKaibW49SBQAWmetMmkXDSVLdzH3Y9sy1FKibicSKEAvZyksNrGGrWVAf7Tw/640?wx_fmt=png&from=appmsg)

DR-in-KG（知识图谱中的深度研究）— 基于 动态话题队列 架构的系统化深研系统，支持三个阶段的多Agent协作：规划 → 研究 → 报告。

* 规划：RephraseAgent（话题优化）+ DecomposeAgent（子话题分解）
* 研究：ManagerAgent（队列调度）+ ResearchAgent（研究决策）+ NoteAgent（信息压缩）
* 报告：去重 → 三层大纲生成 → 带引用的报告撰写

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKa1uLjzic7qiaEET78hslcFxttXbtzRtfHSMZxicIv7YxoTRTlyIYq1BvIA/640?wx_fmt=png&from=appmsg)

研究想法生成系统，从笔记本记录中提取知识点，通过宽松过滤 → 探索想法（每点 5+ 个）→ 严格过滤 → 生成 Markdown多阶段过滤生成研究想法。

**DeepTutor 平台演示**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKa6LVVPhU3DZibkiaC7h2ajbJOicCk0UoCZNyzH0AUDY3NPuQjwqcPA7BicQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKaGw40s50eCFEDkTXLbsO7e7ICHUpYaNqasIn8khlyqOshsNaTUgIejA/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKa57mPbCEdDJxYJH48zic5Lk3CLsjqLD4l9g2f8VEgMdIyKXweAicqicaBQ/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/tnMEWNbfO5c2R6xWQiaEF3tDeaa03icxKatx1xHXEFRm1C88wThibFA3L2gDU5AG2pb3ytI4GCvCGqvK6BfBudD5Q/640?wx_fmt=gif&from=appmsg)

---

如有IoT 源码采购和项目交付需求，请扫码联系小编，微信号: beacon0418

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5f04Y8JFlm3FEtG8Llf70k5nic2LKxBTnnq57QZozVbcl4XITgxgCvm0LyUCBicGQ0uCKbxaynic2rAw/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN4iaZuxem4fsJcVq1icNPbWKX3tn2fNaLMILaMH0RKibLocwse4PQOtw2Ew/640?wx_fmt=other)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454939032&idx=1&sn=5679fa0132dd03f96b7854e02250f5bb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN4nJPPZIh6azfSNld68R6DUJneWzEdAm0vHbaGxD8KIQe6hsIV3gRK9Q/640?wx_fmt=other)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454938828&idx=1&sn=c23447c25873fe4f344373b3b2f5303e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN47gLQy8lk4YYLpQk8BVeZw8sia3DpZKibBxKtV1uBM9d0HmMMZYrSCZBg/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454938751&idx=1&sn=1370c202ad106571ec7053ee732a8458&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN4mGxtr8aB0WoDbARcEnSdribwoaxkBXhbktnCUs9nGWtMjWaNALNxQhQ/640?wx_fmt=other)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454938509&idx=1&sn=5c1328edb68ac69a8eee420e8f062826&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5dibJicMpcVDWcBZMOLVCnPw8ibdqLicqp0TNKiaZsYK80pIleBPUobqmib1RAZL1UPfpCcuSb4zMic5yNQQ/640?wx_fmt=png&from=appmsg)

**往期推荐**

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[4万元，国产信创私有化部署，破解县域无人机AI巡检平台落地难题](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941157&idx=1&sn=b63f67eb0f573b247f47059347b9e407&scene=21#wechat_redirect)

☞[上班摸鱼, 智能AI 监控老板行踪](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454932745&idx=1&sn=532fc401409718148a07b35002c40b98&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/aRoNYXy7XwP3Wia8XicKjpUoIAyCCQRic4od2Qyjcyicv4eXLjQibgc9LBLf8grWXbExIt2h2pclFibLefwW1ic4SWwfw/640?wx_fmt=other)

![图片](https://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5e5kmyNqfUojBMkpIARnHdIqFFTgHWRQw9nKHFkymQVayjicoDSz3QL1Jnyp4ZpvJ25ibQ246UQjCdw/640?wx_fmt=png)

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请告知我们，我们将尽快处理。主理人微信: beacon0418

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

IoT物联网技术

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

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