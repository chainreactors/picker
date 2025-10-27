---
title: 什么是负责任的 Web 服务器扫描？
url: https://mp.weixin.qq.com/s?__biz=MzkyMzE5ODExNQ==&mid=2247487392&idx=1&sn=53b8c39e11765294962564b83d0fbd35&chksm=c1e9f86cf69e717afaf4e242cc102da3c928479386a7a99b38b8844e91dfcfe19f72a51efb8d&scene=58&subscene=0#rd
source: 威胁棱镜
date: 2024-10-22
fetch_date: 2025-10-06T18:52:11.350986
---

# 什么是负责任的 Web 服务器扫描？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dlhiccJOdNYaPnw3V57MricIgeiczGNCiaNzmeg8JGTrgmX5UbhZFiaiczaMsgh5uJwVMGPnVoIibcG2MVSSCXb1hCvjA/0?wx_fmt=jpeg)

# 什么是负责任的 Web 服务器扫描？

原创

Avenger

威胁棱镜

**工作来源**

S&P
2024

**工作背景**

Web 服务器存在各种各样的漏洞，研究人员通过自动化测量分析了解现实世界的情况。但在扫描测绘的过程中，其实存在一些困境：法律问题、道德伦理问题和被扫描方的担忧。

网络空间中的大规模扫描测绘，很可能跨越许多司法管辖区，此处以德国法律为例进行介绍。根据德国刑法，Web 服务器扫描可能会触发包括数据间谍罪在内的多条法律。受害者可以援引民法，要求对扫描造成的损害进行赔偿。除了联邦法律之外，欧盟包括 GDPR（通用数据保护条例）在内的多项法律以及各州的法律都有相关约束。

伦理问题的考量则更加微妙，许多大学都成立了专门的委员会来对伦理道德进行审查。安全研究产生的伦理问题则更加特别，USENIX Security 与 IEEE S&P 已经都成立了伦理委员会（REC）对研究中可能存在的伦理道德问题进行审查把关。

**工作设计**

研究人员设计了一系列模拟实际场景的小例子对相关方进行访谈，每次访谈持续 37 到 116 分钟不等，然后整理数据得出相关结论。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPnw3V57MricIgeiczGNCiaNznVuyJqCdn589dBEKGjDhe5vSeibZU1U4ZUuKarIA1ryyVgglI7l6QDg/640?wx_fmt=png&from=appmsg)

小例子如“Alice 检查 Web 服务器是否存在 SQL 注入，通过类似 sleep 函数来延迟数据库相应，判断该服务器是否存在漏洞”，“Bob 向 Web 服务器发送的非标准 HTTP 请求会导致网站崩溃，且只能由 IT 部门重新启动服务器解决”。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPnw3V57MricIgeiczGNCiaNzrTCnCKC36Aayyr1AiadCkl2hjSoCmZNjM6qwyUZ8m4gjedvltrNeiaMw/640?wx_fmt=png&from=appmsg)

研究人员向 Tranco 的 TOP 一百万域名的通用电子邮件地址 webmaster@domain 发送调查问卷，最终收到 119 份有效回复。

**工作准备**

23 次访谈的受访者情况如下所示，其中包括 9 名法律专家、10 名网站运营方、5 名伦理委员会成员。研究人员已经努力进行多元化拓展，Twitter 和 LinkedIn 上的广告分别展现了 4 万次与 2 千次。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPnw3V57MricIgeiczGNCiaNzIwM7CotwRezmfKGMOo6nuuZhMR1zq4dZmv95ekC2JjYcH2OCxVzbEg/640?wx_fmt=png&from=appmsg)

119 份有效调查问卷的回复中，参与者的平均年龄为 43 岁、平均运营 343 台服务器。最多的是全栈工程师（Full-Stack Developer）、其次是系统工程师（System
Engineer）与运维工程师（DevOps）。**92.4% 的参与者都表示接受过安全培训，以“自学“和”边做边学“为主**。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPnw3V57MricIgeiczGNCiaNzoEb5syeFm2R8wFqmKtzNWrV53Nkic6XfGV72tcHsLbfArC1oCkCwbfQ/640?wx_fmt=png&from=appmsg)

**工作评估**

法律专家认为，目前此类安全研究只能在法律的灰色地带进行，截止 2023 年 8 月，德国法院还没有对此类案件的公开判决。检察官使用自由量裁权，在审判前认为起诉缺乏“公共利益侵害“或者是”罪名不大“。尽管定罪的可能性很小，但如果检察官坚持提起诉讼，也会给安全研究人员带来极大的压力。**即便不触犯刑法，运营方援引民法也可以要求研究人员进行赔偿**。

伦理道德问题上，主要就是无法控制对远程系统产生的影响，无法判断这种扫描是否是道德的。很难确定红线在哪里，一般来说大家会认为（1）对随机内容进行模糊测试（2）故意破坏服务运营（3）提取任何类型的个人信息，这都是显然违背伦理道德的。

**运营人员其实对安全研究中的扫描持积极态度**，因为毕竟扫描本来就是互联网的一部分，坏人不打招呼也肯定会这样做，运营方有义务要做好准备。尽管大家理解此类行为，但很难认同其“合法性“。并且表示，这种”不请自来“的扫描根本不可能知道幕后会触发什么业务流程。扫描行为一定要避免导致服务器过载或者拒绝服务，业务受到影响肯定是不可接受的。另一方面，安全研究会提高组织的成本。组织的云服务可能会基于流量进行收费，或者是商业安全服务带来的噪音告警。运营方一旦确认是扫描，沟通无果后一般都会采取封禁 IP 的策略，同时也保留报警起诉的权利。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPnw3V57MricIgeiczGNCiaNzPM0aeWHe5ZFnSNCxqzAt09B5jXhKeTWicouibDPBm9WvCnKO2FQE2H3g/640?wx_fmt=png&from=appmsg)

具体的案例来说，如“Alice 检查 Web 服务器是否存在 SQL 注入，通过类似 sleep 函数来延迟数据库相应，判断该服务器是否存在漏洞”。

* 大多数法律专家认为这种行为没什么危害，但也有人指出严格的司法解释可能会认为这种行为是“未授权的数据操纵“。而且 Alice 其实无法控制服务器作出什么反映，如果执行 sleep 命令没有睡眠而是导致了崩溃，可能也会陷入法律纠纷。
* 伦理委员会的人觉得使用 sleep 已经算是负责任的方式，这种研究不会引起伦理道德争议，论文可以正常发表。
* 运营人员考量的则更多，例如这样操作即使不导致崩溃也可能导致缓存被影响，又或者拖慢了数据库在极端场景下可能会造成重大财物损失。

具体的案例来说，如“Bob 向 Web 服务器发送的非标准 HTTP 请求会导致网站崩溃，且只能由IT部门重新启动服务器解决”。

* 法律专业人士最关心 Bob 的意图，这样的后果是不是由于他潜在的疏忽导致的。如果 Bob 能够预料到会发生什么，并且崩溃的概率很大，很可能犯了计算机破坏罪。
* 伦理委员会的人关心 Bob 事先做了哪些努力来减轻损害？如果一开始 Bob 没有意识到这个问题，是合乎道德的。一旦发现扫描会导致服务器崩溃，就看应该立刻停止扫描，向运营方披露问题，并在论文中对这一现象进行讨论。
* 运营人员只能接受一次崩溃，服务暂时中断后续可以吸取教训防止此类崩溃，但研究人员如果持续造成崩溃就不可接受。

**工作思考**

法律专家强调要加强立法，把行为规范以法律的形式明确下来，避免产生模糊地带引起法律纠纷。**尽管德国避免了对安全研究/白帽类人员的起诉，但这样也阻碍了法理学的进步**。缺乏相关法律和判决，导致法律专业人士也没有办法提供专业意见。荷兰在法律中引入了豁免条款，但适用范围仍然存在巨大争议。

参考药物研究的例子，有人建议建立预注册审批制度。法律专家十分赞同这个想法，但也提出了跨国界、跨州界等法律边界的问题。**运营人员反对由政府牵头管理审批，避免官僚主义对研究产生重大影响**。运营人员希望研究过程要尽可能地公开透明，负责任地进行披露是很重要的，例如有特定的标头标明扫描、在固定时段扫描等都可以帮助将此类扫描与恶意扫描分开。

总结一下，负责任的扫描要做到
① 在实验室预先测试，最大限度降低影响 ② 收集存储数据最小化 ③ 将对服务器数据的操纵限制在最低，避免更改用户有关的数据 ④ 资源占用尽可能小，很多请求要尽量拉长时间
⑤ 始终监控扫描的状态和结果 ⑥ 提高透明度 ⑦ 使用固定IP 地址 ⑧ 给于被扫描者退出的权力。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYZBhjxOrevSQ7fNoZZStU2H13yWTsib8BM6btaYA5C1wIiaXjpyFHQYqLPPqePw0z8Kxj0BguP0nkow/0?wx_fmt=png)

威胁棱镜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYZBhjxOrevSQ7fNoZZStU2H13yWTsib8BM6btaYA5C1wIiaXjpyFHQYqLPPqePw0z8Kxj0BguP0nkow/0?wx_fmt=png)

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