---
title: CSA GCR 2024 | 深度解析大模型原生安全的系统构建
url: https://mp.weixin.qq.com/s?__biz=MzA3NTQ3ODI0NA==&mid=2247487459&idx=1&sn=c2d849d7331779d849b3529eb6fc5f6e&chksm=9f6eaa68a819237eb1b6795d65f337a72f327ba865a6538de4e6609f50d932153c767581b13e&scene=58&subscene=0#rd
source: 百度安全实验室
date: 2024-11-20
fetch_date: 2025-10-06T19:19:16.681506
---

# CSA GCR 2024 | 深度解析大模型原生安全的系统构建

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2fvCZicH9HWS2TFqg7SibfDHC9iaW4aLQjUlyEdsFaeIyYSvB0ZX5LichYgAMoAQMicDPnBgTPS3LMF4MmytqcmmVhg/0?wx_fmt=jpeg)

# CSA GCR 2024 | 深度解析大模型原生安全的系统构建

百度安全实验室

**11月15日，第八届云安全联盟大中华区大会在北京成功举办，**本次大会以"云安全·AI，迎接未来"为主题，汇聚联合国科学和技术促进发展委员会主席Muhammadou M.O. Kah、中国友谊促进会理事长陈智敏、工信部国际经济技术合作中心信息化所所长李苑、云安全联盟CEO Jim Reavis、CSA大中华区主席李雨航等来自全球的顶尖专家和行业先锋，聚焦数字化时代的技术与安全变革，探讨云安全进入3.0时代AI与云计算的融合下的安全挑战。**会上，百度安全技术委员会主席包沉浮以"大模型原生安全构建之路"为题，深入剖析了大模型安全体系的系统构建。**

![](https://mmbiz.qpic.cn/mmbiz_png/nTljOhrUdlXhkLu8lkvZ0ZcwibcaBrqib08DiagsjqoIIicKSrq41AZXxv0ibOK3GKhqHFwRwsibDiaRTjpQeXV0n67AA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)百度安全技术委员会主席包沉浮

大模型在其训练、部署、运营等各阶段面临着不同的安全挑战，如训练数据的选择与保护、防止模型参数泄露、应对恶意输入等，需要全面的、系统的安全策略来应对。随着新技术的快速发展，其安全问题也日益凸显。**包沉浮在演讲中首先强调了大模型内生安全的三大支柱：基础能力、语料安全和安全对齐**。他指出，提升模型的基础能力是保障安全的根本，这一理念基于"更强大的智能往往意味着更好的安全性"的假设。在语料安全方面，通过严格的数据筛选和清洗，可以从源头降低模型产生不安全内容的风险。而安全对齐则试图通过强化学习等方式调整模型行为，使其符合预期的安全标准。这种多层次的内生安全架构为大模型的基础安全提供了重要保障。

然而，仅依靠内生安全是远远不够的。百度安全技术委员会主席包沉浮，向与会专家示例即使经过安全对齐的模型也可能存在"表面对齐"的局限性，在面对特定提示词时可能产生意想不到的输出。这种现象不仅凸显了构建更全面的原生安全体系的必要性，也反映出大模型安全问题的复杂性远超传统安全范畴。而**大模型原生安全框架包含四大核心要素：内生安全、纵深防御、红蓝对抗和持续运营。**即在保持内生安全基础的同时，通过纵深防御在模型外围构建多重防护屏障。这包括专门的内容安全机制、大模型防火墙系统、多模型协同以及RAG检索增强等技术手段，形成立体化的防护体系。

![](https://mmbiz.qpic.cn/mmbiz_png/nTljOhrUdlXhkLu8lkvZ0ZcwibcaBrqib0Mvfh8iaVNdq7e7t5I5NCABKgia1s0RnEZKOKWkvj7LlyHSLye2HicUqqg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)大模型原生安全

在**纵深防御**建设方面，百度特别关注对抗性攻击的防护，包括越狱攻击检测、注入攻击检测、异常输入检测等多个维度。结合多模型协同机制，系统能够针对特定场景调用专门训练的安全模型，与主模型形成分工配合，从而提升整体安全性。并基于RAG技术的引入有效解决了知识不足导致的"幻觉"等安全问题。

在**红蓝对抗**上，不同于传统静态的安全评估方式，转而采用动态模型红队测试。这种方法不仅包括人工红队测试，还包括自动化的安全评估和结果分析，通过持续的攻防对抗来提升系统的安全防护能力。特别值得一提的是，**百度安全建立了包含文本、图像、多模态混合等多个维度的评测体系，确保安全防护的全面性。**这种动态进化的安全评估方法，使得系统能够不断适应新出现的安全威胁。

在**持续运营**层面，百度构建了多维度的风险感知和处置机制。通过语义干预技术，系统能够及时识别和应对突发性风险；通过安全巡检，可以定期发现潜在的安全隐患；而基于设备、账号、流量等多维度信息的安全风控体系，则确保了异常行为的实时识别和处置。这种全方位的运营体系不仅提高了安全防护的效率，也增强了系统应对未知威胁的能力。

此外，百度安全格外的重视智能体应用场景下的安全问题。随着AI技术向智能体方向演进，新的安全挑战不断涌现，包括Prompt泄露、RAG检索增强生成投毒、非预期执行等新型风险。针对这些新兴威胁，百度安全开发了一系列创新性的防御措施，包括行为约束机制、权限管控体系等，为智能体应用的安全发展提供了重要保障。

![](https://mmbiz.qpic.cn/mmbiz_png/nTljOhrUdlXhkLu8lkvZ0ZcwibcaBrqib0QbOhCib2No6xSyCM3ytBxhRrgPtTlUmSXPHYI4egLpFgXmP7ane4EYA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)百度大模型安全解决方案

随着大模型应用场景的不断拓展，相应的安全需求也将持续增长。百度安全技术委员会主席包沉浮认为，尽管大模型带来了全新的安全挑战，但传统安全领域积累的经验仍然具有重要价值，大模型安全的核心关键在于如何将传统安全理念与大模型的特点有机结合。基于这一理念，百度安全将继续深耕大模型安全领域，秉持着开放合作的理念，携手产业各方共同探索更安全、更可靠的大模型应用实践，通过技术创新和实践积累，为人工智能技术的健康发展保驾护航，构建更加全面、可靠的大模型安全防护体系。

**相关****阅读**

[再获认可！百度多模态内容安全解决方案获WitAwards 2024年度大奖](http://mp.weixin.qq.com/s?__biz=MjM5MTAwNzUzNQ==&mid=2650510914&idx=1&sn=280a03ac6d9b283e7b76ed346eade8c7&chksm=beb3200289c4a914c2fe545f0e97edb397ef95af485fab2a5d8175de1bbb07e18befce564372&scene=21#wechat_redirect)

[2024百度云智大会 | 百度大模型内容安全合规探索与实践](http://mp.weixin.qq.com/s?__biz=MjM5MTAwNzUzNQ==&mid=2650510876&idx=1&sn=36baa152b6b7a391252d6467e0ebb7c3&chksm=beb3205c89c4a94ac676e9bcb6e23910a4ef2902ef072b06c80c4e1df686076421c0d0bddbe4&scene=21#wechat_redirect)

[成都网安周暨CCS2024 | 大模型安全与产业应用创新研讨活动成功举办](http://mp.weixin.qq.com/s?__biz=MjM5MTAwNzUzNQ==&mid=2650510747&idx=1&sn=fd8191015fe63bb17552c12b6d85a603&chksm=beb323db89c4aacd3ba25232aec7304f6b777ffa2b83d3b63312476181fd260c42b3ba7b1972&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/2fvCZicH9HWT0GPhoxs1icEkNDiaupy7wkL8I7KOS0PRnUEeRQZWowpchdBlYpL6ppKkB98zLJrcoyiaayAia6yRzBg/0?wx_fmt=png)

百度安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2fvCZicH9HWT0GPhoxs1icEkNDiaupy7wkL8I7KOS0PRnUEeRQZWowpchdBlYpL6ppKkB98zLJrcoyiaayAia6yRzBg/0?wx_fmt=png)

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