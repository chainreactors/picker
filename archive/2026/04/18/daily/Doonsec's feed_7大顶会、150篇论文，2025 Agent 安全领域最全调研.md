---
title: 7大顶会、150篇论文，2025 Agent 安全领域最全调研
url: https://mp.weixin.qq.com/s/MqNnKJIXOpLneWApB5y_JA
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:51:14.098807
---

# 7大顶会、150篇论文，2025 Agent 安全领域最全调研

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PkfClzhSYiczlY05xPGoLPRpXRDPmGEn2DOguxvS4ibHLwIj8xPTpicCY9jXMrcicSJyaqGv0j9xyV6kH8icBQIjh8nFk7LbfVZ51ic2fJ5gVtMKs/0?wx_fmt=jpeg)

# 7大顶会、150篇论文，2025 Agent 安全领域最全调研

原创

i3eg1nner&林00
i3eg1nner&林00

SecureNexusLab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**「整理：丸一口 | 2026.04」**

> ❝
>
> 一开始整理这个材料的时候，只想着小范围传播，所以会有一些“锐评”和“idea废案”。没想到被SecureNexusLab的小伙伴邀请做广泛开源，内容比较多，没精力对这些碎碎念做删减了，希望不会影响到大家的阅读。
>
> ❞

---

## 📌

本文覆盖2025年 **「S&P / USENIX / CCS / NDSS / ICLR / NeurIPS / ACL」** 七大顶会，**「150+篇」**Agent安全相关论文，每篇带**「思路总结」**。

## 🔗

* **「GitHub」**：
  👉 https://github.com/Van-Echo/OpenWanYikou/tree/main/06-Survey
* **「原博主B站主页」**：
  👉 https://space.bilibili.com/3461572290677609
* **「评论/获取PDF」**：关注公众号后台发送“智能体安全”，获取完整版（含完整PDF及所有论文）

---

## 一、S&P 2025

| 论文关键词 | 一句话锐评 | 可用思路 |
| --- | --- | --- |
| 开源｜文生图越狱｜双Agent迭代种子池 | 两个Agent互相喂种子，越狱效率翻倍 | 红队测试可借鉴这种“左右互搏”思路 |

![](https://mmbiz.qpic.cn/mmbiz_jpg/PkfClzhSYicx75LqcgRZDUkRzHkW7f1QTq99TeaTuJrFT3krBmYibDiaAK72eQJDNZEs1g9b932iayNdI76q7BmZfic9tb0luhTj7Ik4B12Neod4/640?wx_fmt=jpeg)

## 二、USENIX 2025

| 论文关键词 | 一句话锐评 | 可用思路 |
| --- | --- | --- |
| 视觉验证码｜将视觉任务转化为搜索优化问题 | 把验证码当搜索题做，绕过率惊人 | 验证码厂商该升级了 |
| AgentFuzz｜用Agent迭代种子来找后门漏洞 | Agent自己学挖洞，Fuzzing进入next level | 可集成到CI/CD流程 |
| 修代码bug的Agent框架｜无训练｜规范化中间件 | 不训练就能用，中间件做规范化，很务实 | 生产环境可快速接入 |
| 主动防御｜无训练｜隐身诱饵陷阱 | 放诱饵让Agent踩，踩到就暴露 | 内部威胁检测的好思路 |

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PkfClzhSYiczFggSpcjhNdiaHZc9xgnj00ZSqLVHZ7DzG8btnULS8m0nhYZSB9WvR9pKaIWFIbaLJ8382YrOGlvC8jwJ5kQ9ol2pGiaq0T3Orw/640?wx_fmt=jpeg)

## 三、CCS 2025

| 论文关键词 | 一句话锐评 | 可用思路 |
| --- | --- | --- |
| 传感器（车联网）｜防御｜动态信任值 | 车联网传感器动态调信任分，防伪造 | 可推广到IoT场景 |
| 系统层面布置探针｜端到端防御 | 从输入到输出全链路防护，理想但重 | 适合高安全等级场景 |

![](https://mmbiz.qpic.cn/mmbiz_jpg/PkfClzhSYicz68Yc5dxP8zRgnjT5J8WgiatD4VDu7nhspRQShOLB27spkenTzvrzUkicljYYAZkonmEdEg1fuedZGn9e2T5hKGcPuwevBXiavics/640?wx_fmt=jpeg)

## 四、NDSS 2025

| 论文关键词 | 一句话锐评 | 可用思路 |
| --- | --- | --- |
| 离线强化学习｜unlearning｜通过对要遗忘的数据进行微调实现等效unlearning | 不想让Agent记住的数据，微调掉就行 | 合规场景（如GDPR被遗忘权）刚需 |
| 沙盒防御｜规定接口限制沙盒内的权限 | 沙盒里把接口卡死，Agent再强也出不去 | 多租户场景必看 |

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PkfClzhSYiczMyTU0Sl9M2a6ZUWTIOoPWLnG5OGbrLPL5vklkgmmL6atWvOEEubO5JRIXSnDvoTic4s5EGMx1HckWlia4tlAEibwYbYhmQhzJns/640?wx_fmt=jpeg)

## 五、ICLR 2025（含Poster）

| 论文关键词 | 一句话锐评 | 可用思路 |
| --- | --- | --- |
| 强化学习｜通用物理控制Agent｜物理世界 | 让Agent在物理世界干活，RL玩家狂喜 | 机器人控制方向可追 |
| 图形用户界面Agent｜构造数据集｜训练模型 | GUI自动化新基线 | RPA场景直接对标 |
| 构造医学数据集 | 医学Agent的基建工作 | 医疗AI赛道必备 |
| 评估Agent端到端机器学习工程能力的BenchMark | 测Agent会不会写ML代码，很刚需 | MLE面试新题库（笑） |
| （批改）多Agent｜纳什均衡｜强化学习 | 多Agent博弈，最后到纳什均衡 | 多智能体对抗场景 |
| 自动化生成工作流｜蒙特卡洛树搜索 | MCTS帮你自动编排Agent工作流 | AutoGPT类项目可借鉴 |
| RAG｜通用Agent | RAG套壳？但做得扎实也能发 | 所有RAG应用都该看一眼 |
| 教师模型｜偏好对齐｜运动 | 让Agent学会“像人一样动” | 人机交互方向 |
| Agent组网｜协议｜有意思 | Agent之间怎么通信？这篇很有意思 | 多Agent系统的底层基建 |
| 多智能体集思广益 | 多个Agent一起brainstorm | 创意生成类任务可用 |
| 红队测试｜防越狱｜Agent角色扮演左脚踩右脚 | 让Agent扮演红队互相攻防，自我进化 | 红队自动化最优雅的方案之一 |

![](https://mmbiz.qpic.cn/mmbiz_jpg/PkfClzhSYicx6MEiaIzHsnu2LRnDOPOHuCIYhPuAtdDLAZLNiaicOjGbCToWn1qytKtg5gcrqWWNErwPslicT6JWErLxf1NESJ0JrCegzrQCQsZo/640?wx_fmt=jpeg)

## 六、NeurIPS 2025

| 论文关键词 | 一句话锐评 | 可用思路 |
| --- | --- | --- |
| 推理阶段多次推理取最优 | 不训练，只靠多次采样+投票 | 成本不高，效果不错，直接能用 |
| 对闭源的蒸馏｜数据集构建｜计算机使用 | 把闭源Agent（如Claude Computer Use）的行为蒸馏出来 | 平替闭源Agent的核心技术 |
| Web Agent｜按步骤给奖励｜过程奖励模型PRM | 不只看结果，每一步都给奖励 | Web自动化训练新范式 |
| 大世界｜强化学习&持续学习｜马尔科夫链 | 大世界环境下的Agent持续学习 | 开放世界游戏Agent必读 |

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PkfClzhSYicxk0tIGHkbQ794C0APtvXuuLOhqC82sf4iaRxoyyHf6v68Pq4TkIWGAkf1bCuBNET9LwwXZ7rhiadZws1WWJwWW93J7nTbXaB5gY/640?wx_fmt=jpeg)

## 七、ACL 2025（精选）

| 论文关键词 | 一句话锐评 | 可用思路 |
| --- | --- | --- |
| 事实核查｜多Agent左脚踩右脚 | 多Agent互相纠错，事实核查新范式 | 内容审核场景可借鉴 |
| 创造性智能｜用Agent玩密室逃脱 | 测Agent的创造性，密室逃脱是绝佳场景 | 游戏AI + 创造力评估 |
| 监测有害Meme梗图｜多Agent左脚踩右脚 | 让Agent自己识别有害梗图 | 内容安全审核 |
| 编译｜让Agent模仿人类面对github项目时的工作流 | Agent学会看文档、装依赖、编译 | 自动化DevOps |
| 安卓BenchMark｜数据集 | 移动端Agent的标准化测试 | 手机自动化方向必看 |
| 金融决策BenchMark｜分层记忆 | 让Agent学会炒股，分层记忆是关键 | 量化交易Agent |
| BookWorld｜把世界观提取出来｜有意思 | 从小说提取世界观，Agent在里面演化 | 游戏NPC + 自动化故事生成 |

![](https://mmbiz.qpic.cn/mmbiz_jpg/PkfClzhSYiczAialLo9P0pbia4AsgicDwhHFquyv6PjXS7yOYOqKcIstNGnhMWuOEqwraheWAxSegVorguh36U5JTJia6tx6BIicicf3bkichFFwzw8/640?wx_fmt=jpeg)

## 💡 几个“废案”想法（可能对你有启发）

1. **「Agent越狱的“疫苗”思路」**：能不能让Agent提前见过所有越狱模板，就像打疫苗一样？—— 成本太高，放弃了
2. **「用验证码反制Agent」**：既然Agent能过验证码，那能不能动态生成Agent过不了的验证码？—— 猫鼠游戏，没想清楚边界
3. **「多Agent“相互水论文”」**：让多个Agent互相review + 改稿，自动产出文献综述 —— 试过，质量太差，但未来可期

如果对你有帮助，欢迎**「转发、在看、分享」**给更多朋友。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkLGDzh5WQ5kuYab29V2PteuUrCj2HeRIHibmjQEK7plD7iccC97duj94oGugfkHdQdxcaXtB7w5icmg/0?wx_fmt=png)

SecureNexusLab

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ny8tG5SicPMkLGDzh5WQ5kuYab29V2PteuUrCj2HeRIHibmjQEK7plD7iccC97duj94oGugfkHdQdxcaXtB7w5icmg/0?wx_fmt=png)

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