---
title: 【AI安全】智能体提前拿到授权，真正执行时还算数吗？ZeroGate 的一次性通行证
url: https://mp.weixin.qq.com/s/8M171j01QBK1YYCc-SEF1w
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:34:26.762402
---

# 【AI安全】智能体提前拿到授权，真正执行时还算数吗？ZeroGate 的一次性通行证

# 【AI安全】智能体提前拿到授权，真正执行时还算数吗？ZeroGate 的一次性通行证

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 一、报告已批准上传，临出手前文件却变了

##### [Oxo Operator为安全工程师而来！](https://mp.weixin.qq.com/s?__biz=MzkxNzU2NDgxNQ==&mid=2247488841&idx=1&sn=6980ae43228319cdcdb598f74cffedda&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

想象一个定时上传报告的智能体：文件、目标存储桶和执行账号在上午就定好了，下午才到发送时间。如果上午批准的是 A 文件，下午智能体却换成 B 文件，旧批准还能放行吗？这不是“有没有权限使用上传工具”的问题，而是**这一次具体请求是否仍符合获批条件**。⏱️

ZeroGate 论文（arXiv:2609.25443v1）研究的就是这个执行关口。作者设计了一个短期有效、带签名的 ActionPass：批准方先审查确切动作并签发；可信运行时在真正派发前重新组装最终请求，再核对请求内容、权限条件和一次性标识。论文给出的上传场景是解释性例子，云端测量则是作者自己部署的 Azure Blob 对象写入实验，并非某家生产服务已经遭攻击或上线此方案。

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHT52w4evDibdq4pYTc2rHOE63uvmHSaZ64zabJhuLd5uuicyMVzrNQKe0rAJXraRPHtNMuAO5RsJfwIuiaFqzF931vfMSIbA3WUZM/640?wx_fmt=png&from=appmsg)

📌 先区分三件事：

| 记录 | 它能证明什么 | 它不能证明什么 |
| --- | --- | --- |
| 签名 ActionPass | 某个确切动作曾经获批 | 执行时外部状态依旧新鲜 |
| 放行收据 | 本地关卡允许派发一次 | 云端对象已经写入成功 |
| 结果证据 | 目标服务实际返回或读回的内容 | 先前批准必然合理 |

论文中两种模式都需要批准方和本地关卡。差别是同步模式在执行工人拿到任务后才请求批准；预备模式把这一步提前到等待期间。4800 次云端尝试里，预备模式从工人接手到允许派发的 p95 为 9.802—11.374 毫秒，同步模式为 25.018—334.000 毫秒，取决于测试并发。**这只是局部关口的延迟，不是端到端加速。** 作者明确报告预备模式的平均完整生命周期在每个并发级别都更长，因为预备和等待时间仍要计入。📏

对安全工程师，第一步不是追求更小的毫秒数，而是问：业务能否在等待期间固定最终参数？若收件人、文件内容或执行身份临时生成，提前批准一个“差不多”的动作，反而会扩大权限。

# 二、通行证不认“同类动作”，只认最终请求

ZeroGate 的信任链从“确定对象”开始。批准方看到的不是“允许上传”四个字，而是含目标、内容承诺及权限限制的规范化动作。ActionPass 把这些字段的绑定关系签进去，带上短时有效期和 nonce——一次性随机标识。它不是可反复刷的通用票。🔐

到执行时，可信适配器重新构造即将发给外部服务的真实请求。本地关卡验证签名、有效期、动作指纹与权限依赖；如果目标或内容变了，就拒绝旧票。若通过，SQLite 事务把 nonce 消费、适用额度更新和放行收据合在一起，避免两个并发执行者都以为自己抢到了同一张票。

这个顺序可以画成一条线：

1. 🧾**预备**

   ：最终文件与目的地确定，批准方签发确切动作的票。
2. 🔎**重建与重验**

   ：执行前从真实请求重新算指纹，并检查期限、状态和额度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHRFNucgAAfXQBWlHNcwcWVEQphwQ2PLYkt6WxpbKMAXO3NWpiaRfVkG3kRbib94ssjubQKLpdAFeJj5FW3Iohbrzs6icTlbFkCiaJE/640?wx_fmt=png&from=appmsg)

1. 🔒**原子消费**

   ：同一个本地事务占用 nonce 和预算，记录放行。
2. ☁️**外部执行**

   ：请求发往云端；另行查证是否真的完成。

最容易误读的是第二步。两个旧哈希相同，只说明“请求没改”，不说明用户权限、撤销状态或外部对象在此刻仍符合政策。论文给出的“与同步政策决策一致”是**有条件命题**：批准本身正确、所有政策依赖都被表示并保持新鲜、观察可靠、消费原子，结论才成立。参考实现本身既不保证现实世界状态绝对新鲜，也不保证远程副作用恰好发生一次。⚠️

因此，一个可执行的首检是抽取一条真实写操作：记录签票时和派发时的账号、目标、请求体摘要、撤销状态、额度与 nonce；再故意改变其中一项，确认旧票在执行关口被拒绝。还要模拟并发重复派发和崩溃恢复，检查本地收据与云端实际对象能否对账。若只是看到“签名有效”，检查还没完成。

# 三、云端实验把两只时钟分开看

🎯 核心问题：同一张 ActionPass 在崩溃重试时怎样证明只放行一次？

云端实验把“工人接手到允许派发”和“准备到读回验证”分开计时：为什么前者的 p95 下降，后者的平均时间却更长？如果目标服务已经写入，而本地只留下放行收据，又该怎样对账？

我们在知识星球继续拆解这两只时钟、nonce 消费与远程副作用之间的边界，附上核查清单。

📚**AI 文献解读：最前沿的 LLM 安全论文深度剖析。**

🐛**AI 漏洞情报：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。**

🛡**AI 安全体系：从红队攻击到蓝队防御的全方位知识图谱。**

🛠**AI 攻防工具：红队专属的自动化测试与扫描工具箱。**

🚀立即加入 **Oxo AI Security 知识星球**，掌握 AI 安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHRy2nZH6S7gzEkSbJnlJu1zIywWiaNFSlmNhnylG29ETiatRN7MkD64QPQGpxIiaR9xbVOr7Zhn1TdziaC6KjJnBDHPibFfkJ5OAMGs/0?wx_fmt=png)

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