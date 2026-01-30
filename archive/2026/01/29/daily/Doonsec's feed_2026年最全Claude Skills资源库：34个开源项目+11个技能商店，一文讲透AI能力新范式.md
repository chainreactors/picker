---
title: 2026年最全Claude Skills资源库：34个开源项目+11个技能商店，一文讲透AI能力新范式
url: https://mp.weixin.qq.com/s/7ymayG4vnGIPdK4bCwKAPw
source: Doonsec's feed
date: 2026-01-29
fetch_date: 2026-01-30T04:01:41.785337
---

# 2026年最全Claude Skills资源库：34个开源项目+11个技能商店，一文讲透AI能力新范式

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BibeFvVBkRA9xiaKTyyJeCJgF72qibFT2cdLT98SHq4zfJIYibdnYPicUic50gbSpgUPfqBLH73F55x0qrVe9uInf2rg/0?wx_fmt=jpeg)

# 2026年最全Claude Skills资源库：34个开源项目+11个技能商店，一文讲透AI能力新范式

原创

AI安全工坊
AI安全工坊

AI安全工坊

![]()

在小说阅读器中沉浸阅读

# 2026年最全Claude Skills资源库：34个开源项目+11个技能商店，一文讲透AI编程新范式

> 这不是一篇简单的资源罗列，而是一份经过实测的选型指南。收藏这一篇，少走三个月弯路。

---

## 开篇：一个让我震惊的数据

Anthropic官方Skills仓库，**57,871 Star**。

这个数字意味着什么？作为对比，Vue.js是47k，React是232k。一个刚发布不到一年的"配置文件规范"，Star数已经超过了Vue。

这说明一件事：**Agent Skills不是昙花一现的概念，而是AI编程的下一个基础设施。**

### 什么是Agent Skills？

一句话：**把专家经验打包成AI可以直接调用的知识模块。**

传统方式：你告诉AI"帮我剪视频"，它给你一堆FFmpeg命令，你还得自己调参数。

Skills方式：你说"帮我剪掉口误"，AI自动识别608处问题，精准剪辑，输出成品。

差距在哪？**Skills把"怎么做"这个知识封装好了，AI不用从零推理。**

### 为什么你必须现在了解？

三个信号：

1. 1. **Anthropic、OpenAI、Google、Microsoft、Cursor** 已全部支持Skills标准
2. 2. **skillsmp.com** 社区市场已收录 **6万+** 技能
3. 3. 国内头部AI博主（宝玉、归藏、Anthony Fu）都在做Skills

这篇文章，我整理了**34个顶级开源项目**和**11个技能商店**，并附上GitHub Star数据和实测评价。

---

## 速查表：30秒找到你需要的

| 你的需求 | 推荐项目 | Star数 |
| --- | --- | --- |
| Claude Code全套配置 | everything-claude-code | 34.4k |
| 小红书/公众号内容创作 | baoyu-skills | 3.2k |
| Rust开发 | rust-skills | - |
| 科研/生物医药 | claude-scientific-skills | 7.5k |
| Vue/Vite/Nuxt开发 | antifu-skills | 2.1k |
| 口播视频剪辑 | videocut-skills | 660 |
| Obsidian知识管理 | claudesidian / obsidian-skills | 1.7k / 8.6k |
| 技能安全管理 | agent-skills-guard | 214 |
| AI编程入门 | vibe-coding-cn | 7.5k |
| 跨平台技能加载 | openskills | 7.4k |

---

## 第一部分：34个开源项目深度解析

### 一、综合技能集合（11个）

#### 1. everything-claude-code [Star: 34,368]

**地址**：https://github.com/affaan-m/everything-claude-code

**来源**：Anthropic黑客松冠军作品，10个月实战打磨

**为什么排第一**：这是目前最完整的Claude Code配置库，不是简单的技能堆砌，而是一套完整的工作流体系。

包含：

* • 12个专业Agent（前端、后端、安全、PM、QA等）
* • 16个技能模块
* • 11个工作流命令
* • 自动化Hooks

核心价值：

* • Token优化：模型选择、系统提示精简
* • 记忆持久化：跨会话自动保存/加载上下文
* • 持续学习：自动从会话中提取模式生成技能

**安装**：/plugin marketplace add affaan-m/everything-claude-code

**适合人群**：Claude Code重度用户，想要一步到位的配置

---

#### 2. baoyu-skills [Star: 3,218]

**地址**：https://github.com/JimLiu/baoyu-skills

**作者**：宝玉（知名AI博主，X/Twitter粉丝50万+）

**定位**：内容创作者的效率工具箱

这是国内最受欢迎的Skills集合，专注解决内容创作痛点：

| 技能 | 功能 | 亮点 |
| --- | --- | --- |
| xhs-images | 小红书信息图 | Style×Layout二维系统 |
| infographic | 信息图表 | 自动排版 |
| slide-deck | PPT生成 | 多种风格模板 |
| comic | 漫画创作 | 分镜自动生成 |
| post-to-wechat | 发布公众号 | 一键排版发布 |

**实测体验**：小红书图文生成质量很高，风格选择丰富，是我目前用得最多的内容创作Skills。

**适合人群**：自媒体创作者、运营人员

---

#### 3. rust-skills [版本: v2.0.9]

**地址**：https://github.com/ZhangHanDong/rust-skills

**定位**：不是代码补全，是Rust开发的"元认知框架"

这个项目的设计理念很独特——它不是简单地帮你写代码，而是教AI像资深Rust工程师一样思考。

**三层认知模型示例**：

传统AI：

* • 用户：“交易系统报E0382错误”
* • AI：“用.clone()” ← 表面修复，忽略业务约束

Rust Skills：

* • 用户：“交易系统报E0382错误”
* • AI分析：

+ • Layer 1: E0382 = 所有权错误 → 为什么需要这个数据？
+ • Layer 3: 交易记录是不可变审计数据 → 应该共享，不是复制
+ • Layer 2: 使用Arc作为共享不可变值
+ • 建议：重新设计为Arc，而不是clone()

**支持领域**：FinTech、ML、Cloud-Native、IoT、Embedded、Web、CLI

**适合人群**：Rust开发者，尤其是从其他语言转过来的

---

#### 4. claude-scientific-skills [Star: 7,461]

**地址**：https://github.com/K-Dense-AI/claude-scientific-skills

**来源**：K-Dense团队（斯坦福、MIT研究人员在用）

**规模**：140个科学研究技能

这是科研人员的福音，覆盖完整的研究工作流：

* • 生物信息学与基因组学
* • 化学信息学与药物发现
* • 蛋白质组学与质谱分析
* • 临床研究与精准医学
* • 医疗AI与临床ML
* • 医学影像与数字病理
* • 机器学习与AI
* • 数据分析与可视化

**核心亮点**：直接对接28+科学数据库API（OpenAlex、PubMed、bioRxiv、ChEMBL、UniProt等）

**适合人群**：科研人员、生物医药从业者、数据科学家

---

#### 5. antifu-skills [Star: 2,054]

**地址**：https://github.com/antfu/skills

**作者**：Anthony Fu（Vue/Vite核心贡献者，GitHub 70k+ followers）

**定位**：Vue/Vite/Nuxt生态一站式技能集

如果你主要使用Vue技术栈，这个集合必装：

| 技能 | 来源 | 说明 |
| --- | --- | --- |
| vue | vuejs/docs | Vue3核心文档 |
| nuxt | nuxt/nuxt | Nuxt框架 |
| vite | vitejs/vite | 构建工具 |
| vitest | vitest-dev/vitest | 测试框架 |
| unocss | unocss/unocss | 原子CSS |
| pnpm | pnpm/pnpm.io | 包管理器 |

**技术亮点**：使用git submodules直接引用源文档，保持与上游同步更新。

**适合人群**：Vue/Vite/Nuxt开发者

---

#### 6. skills [Star: 57,871]

**地址**：https://github.com/anthropics/skills

**来源**：Anthropic官方

**定位**：官方技能示例库和规范参考

包含Creative & Design、Development & Technical、Enterprise & Communication、Document Skills等分类。

**价值**：学习Skills怎么写，看官方示例是最好的方式。

---

#### 7. agentskills [Star: 7,840]

**地址**：https://github.com/agentskills/agentskills

**定位**：Agent Skills开放标准的规范和参考实现

如果你想开发自己的Skills或者集成Skills到产品，这是必读仓库。

---

#### 8. obsidian-skills [Star: 8,596]

**地址**：https://github.com/kepano/obsidian-skills

**作者**：kepano（Obsidian Minimal主题作者）

**定位**：Obsidian专用技能包

---

#### 9. skill-wlzh

**地址**：https://github.com/wlzh/skills

**定位**：YouTube转播客工具集

包含：

* • youtube-to-xiaoyuzhou：YouTube视频自动下载并发布到小宇宙播客
* • voice-changer：RVC AI模型变声处理
* • audiocut-keyword：音频关键字过滤
* • text-to-speech：文本转语音（18+种中文声音）

**适合人群**：播客创作者、内容搬运

---

#### 10. skills2 [Star: 25]

**地址**：https://github.com/mzbac/skills

**定位**：Codex技能集，包含code-review-low、diagram-first、planning-with-files等。

---

#### 11. skills3

**地址**：https://github.com/remotion-dev/skills

**定位**：Remotion（React视频框架）内部技能包

---

### 二、视频与内容创作（5个）

#### 12. videocut-skills [Star: 660]

**地址**：https://github.com/Ceeon/videocut-skills

**定位**：口播视频剪辑Agent

**解决的痛点**：剪映"智能剪口播"的两大缺陷——不理解语义、字幕识别差

**功能对比**：

| 功能 | 剪映 | videocut-skills |
| --- | --- | --- |
| 语义理解 | 只能模式匹配 | AI逐句分析 |
| 静音检测 | 固定阈值 | 可调阈值(>0.3s) |
| 重复句检测 | 无 | 相邻句开头≥5字相同自动删除 |
| 句内重复 | 无 | 智能删除重复部分 |
| 词典纠错 | 无 | 自定义专业术语词典 |
| 自更新 | 无 | 记住偏好，越用越准 |

**实测数据**：19分钟原片 → 自动识别608处问题 → 剪辑后72MB

**适合人群**：口播视频创作者、知识博主

---

#### 13. concept-viz-agent [Star: 100]

**地址**：https://github.com/lbq110/concept-viz-agent

**定位**：概念可视化Agent，将文章转化为科学风格概念图

**输出规格**：4K超高清（5504×3072），中文字清晰正确

**工作流程**：/discover → /analyze → /map → /design → /generate

**支持图表**：金字塔、网络图、流程图、地形图等10+种

---

#### 14. guizang-s-prompt [Star: 918]

**地址**：https://github.com/op7418/guizang-s-prompt

**作者**：归藏（知名AI创作者，PPT生成领域标杆）

**内容**：高质量AI提示词库

精选提示词：矢量插画风格PPT、Anthropic风格PPT、渐变拟物玻璃卡片风格PPT、3D信息图、社交媒体卡片、影视剧场景海报等

**适合人群**：PPT设计、海报创作、社交媒体运营

---

#### 15. Humanizer-zh [Star: 1,850]

**地址**：https://github.com/op7418/Humanizer-zh

**定位**：AI写作去痕工具（中文版）

**效果示例**：

输入：坐落在风景如画的杭州市中心，这家咖啡馆拥有丰富的文化底蕴和令人叹为观止的装饰…

输出：这家咖啡馆在杭州市中心开了三年，以手冲咖啡和老建筑改造的空间出名。

**适合人群**：需要降低AI痕迹的内容创作者

---

#### 16. skill-prompt-generator [Star: 955]

**地址**：https://github.com/huangserva/skill-prompt-generator

**定位**：基于Skills的智能提示词生成系统

**规模**：1246+元素库

**v2.0三种模式**：Portrait（人像502元素）、Cross-Domain（跨域995元素）、Design（设计20万+组合）

---

### 三、Obsidian集成（4个）

#### 17. claudesidian [Star: 1,686]

**地址**：https://github.com/heyitsnoah/claudesidian

**定位**：Claude Code + Obsidian启动套件

**理念**：把Obsidian变成AI驱动的第二大脑

**预配置命令**：

* • /thinking-partner：协作探索
* • /daily-review：每日回顾
* • /research-assistant：深度研究

**文件夹结构**（PARA方法）：00\_Inbox、01\_Projects、02\_Areas、03\_Resources、04\_Archive

**适合人群**：Obsidian用户、知识管理爱好者

---

#### 18. obsidian-md2wechat [Star: 186]

**地址**：https://github.com/geekjourneyx/obsidian-md2wechat

**定位**：一键将Markdown转换为微信公众号样式

**主题样式**：默认温暖风、苹果风、字节范、赛博朋克

**适合人群**：用Obsidian写公众号的创作者

---

#### 19. axton-obsidian-visual-skills [Star: 1,067]

**地址**：https://github.com/axtonliu/axton-obsidian-visual-skills

**定位**：Obsidian可视化技能包

**支持格式**：Canvas、Excalidraw、Mermaid

**图表类型**：Flowchart、Mind Map、Hierarchy、Relationship

---

#### 20. opencode-obsidian [Star: 196]

**地址**：https://github.com/mtymek/opencode-obsidian

**定位**：OpenCode AI助手嵌入Obsidian

**使用场景**：总结长文、起草写作、查询知识库、生成大纲

---

### 四、开发工具（7个）

#### 21. mcp-probe-kit [Star: 24]

**地址**：https://github.com/mybolide/mcp-probe-kit

**定位**：AI驱动的完整研发工具集

**规模**：42个实用工具

**工具分类**：

* • 工作流编排（10个）：start\_feature、start\_bugfix、start\_review、start\_ui
* • 代码分析（7个）
* • Git工具（4个）
* • 生成工具（7个）
* • 项目管理（7个）
* • UI/UX工具（6个）
* • 产品设计（3个）：gen\_prd、gen\_prototype、start\_product

---

#### 22. antigravity-kit [Star: 3,497]

**地址**：https://github.com/vudovn/antigravity-kit

**定位**：AI Agent模板库

**规模**：20个Agent + 36个Skills + 11个Workflows

**智能Agent自动检测**：无需手动指定，系统自动识别任务类型并调用合适的专家

---

#### 23. openskills [Star: 7,412]

**地址**：https://github.com/numman-ali/openskills

**定位**：通用技能加载器

**兼容**：Claude Code、Cursor、Windsurf、Aider、Codex

**核心价值**：一次编写，到处运行

---

#### 24. tiki [Star: 71]

**地址**：http...