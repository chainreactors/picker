---
title: 滴滴多篇成果入选CVPR 2026，产学研协同创新结硕果
url: https://mp.weixin.qq.com/s/rKM3gJfjWnOEjiqgP9Enog
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:44:19.754638
---

# 滴滴多篇成果入选CVPR 2026，产学研协同创新结硕果

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1kYDdPrxHSrJvQvORwBclCxddPiaVpEW3L7iaZ0QbyKhicZrVAvVLISsiaicVKTKib9De1ic0mzEvibsBRTFU3TH5aUMdquwhMP3fNT5tee3iaa4ptYI/0?wx_fmt=jpeg)

# 滴滴多篇成果入选CVPR 2026，产学研协同创新结硕果

滴滴技术

![]()

在小说阅读器中沉浸阅读

**近日，计算机视觉顶级会议 CVPR 2026 录用结果揭晓。滴滴技术团队立足真实业务场景中的关键问题，联合高校产学研攻关，多篇论文成功入选。**

**本文分享的几篇成果是由滴滴云平台事业群、安全产品技术部及自动驾驶团队，与武汉大学、北京邮电大学、香港中文大学、香港中文大学（深圳）、香港大学等高校联合研发完成。成果覆盖智能驾驶安全预警、人脸反欺诈与可解释性AI、自动驾驶轨迹规划、机器人精确控制、视频几何重建与时序稳定化等前沿领域。未来，滴滴将继续深耕业务场景，让前沿探索与产业需求相互激发，与学界携手推动更多技术成果落地。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kV4XHiaammJ7P2wavRml3zTNxADcw3YexZG3At1qb8icSBiaRiaoz7HwHiaErfyEbLro4WgEJq9RWOj3p4ibmM2vu0Jk91UYcOGUvUGPP53z7FkPY/640?wx_fmt=png&from=appmsg#imgIndex=0)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/kV4XHiaammJ5KX5etFFJkP7EHu1UBRO02iaibfuLYTsC1fpEUSAZTLAY0X6f9DfS1C23I7HrKR5ia3K4sQNzKKQaJ08QH9h2ialCEyyhQ4nzXdPY/640?wx_fmt=gif&from=appmsg#imgIndex=1)

中稿论文如下（排名不分先后）：

**1、RiskProp: Collision-Anchored Self-supervised Temporal Constraints for Early Accident Anticipation（以碰撞时刻为锚点的自监督时序约束交通事故预警）**

**作者：**

Yiyang Zou, Tianhao Zhao, Peilun Xiao, Hongyu Jin, Longyu Qi, Yuxuan Li, Liyin Liang, Yifeng Qian, Chunbo Lai, Yutian Lin, Zhihui Li, Yu Wu

**摘要：**

该论文提出了一种基于时序事故风险传播 (RiskProp) 的自监督训练范式，专注于真实交通事故的实时预警场景，在公开数据集 CAP 和 Nexar 事故预警任务中取得了 SOTA (state-of-the-art) 效果。方案通过两个互补的损失函数建模风险演化：首先，由于未来帧包含更多信息线索且只有事故碰撞帧有客观标签，论文引入未来帧正则化损失，将风险信号从碰撞帧反向传播到早期帧，引导模型学习有意义的风险进展；其次，为了反映事故前风险的自然积累，应用单调约束损失以确保预测风险分数随时间一致变化。论文有效解决了以往工作中时序预测结果不稳定和预警时间短的问题，并在不同尺寸的模型上均表现出正向提升，目前已应用于滴滴桔视端到端 ADAS 安全预警业务场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kV4XHiaammJ5pj5TEUTBfAgiaR96fWuxDkibNlZsochHoCQBn6MNKeAa6joVgrY5rDaqdhlBRuvhabEibKoUk7q1S4JkqvDPoRsqwdu0Fu0zCP8/640?wx_fmt=png&from=appmsg#imgIndex=2)

图: RiskProp架构示意图

**2、Harnessing Chain-of-Thought Reasoning in Multimodal Large Language Models for Face Anti-Spoofing（基于多模态大模型链式思维推理的人脸反欺骗检测）**

**论文链接：**https://arxiv.org/pdf/2506.01783

**作者：**

Honglu Zhang, Zhiqin Fang, Ningning Zhao, Saihui Hou, Long Ma, Renwang Pei, Zhaofeng He

**摘要：**

该论文首先构建了FaceCoT，首个面向人脸反欺诈的、百万级视觉问答式思维链数据集，通过模拟人类思维过程设计六阶段层级式思维链结构,首次引入结构化、可解释的推理标注机制，不仅给出真假标签，更明确呈现“攻击成立的依据与逻辑路径”，为模型学习“为什么是欺诈”提供清晰且高质量的监督信号。此外，提出CEPL多阶段渐进式学习框架，通过阶段化训练策略，引导模型先精准建模关键欺骗特征，再逐步学习显式推理表达，实现检测精度与决策可解释性的协同优化，使模型从“只会判断”升级为“能够说明判断依据”。在 11 个主流基准数据集上的系统评测表明，该方法全面超越现有 SOTA，展现出稳定且显著的性能优势。

![](https://mmbiz.qpic.cn/mmbiz_png/kV4XHiaammJ7sic7re3ibcoicMKpQdG2fZOVicHvskSqaQK4AsXbIja8KNpu4vibbKvHIIBdVfibPs2cmWzr9GfwCAia2dHs5J9azdQDt1v2niasic0OU/640?wx_fmt=png&from=appmsg#imgIndex=3)

图: FaceCoT数据生成示意图

**3、ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving（一种结合认知式隐空间推理与层次化并行预测的轨迹规划方法）**

**论文链接：**https://arxiv.org/abs/2512.22939

**作者：**

Qihang Peng, Xuesong Chen, Chenye Yang, Shaoshuai Shi, Hongsheng Li

**摘要：**

该论文提出了一种结合隐空间推理与层次化并行预测的轨迹规划方法，专注于真实交通场景的高效路径规划，该方案在公开数据集nuScenes的开环与闭环评测中均取得了SOTA(state-of-the-art)效果。通过设计统一的视觉-语言-动作模型的框架，该方案解决了以往工作中推理速度慢与文本轨迹不稳定的问题，并且将多模态信息在隐空间中进行了统一，在保持推理能力的同时提高了模型的效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kV4XHiaammJ67vrhibKYulC5k6DjDEW9yd81F7c09tJzhM2AJT9YqUSymksrF6FrB2tHnNyIyb97Vl5pb7ppmNoJyamVzg8ZVbALicaWqGgHrw/640?wx_fmt=png&from=appmsg#imgIndex=4)

图: ColaVLA框架示意图

**4、GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation（一种基于预测性运动学与3D高斯几何的视觉-语言-动作机器人操控方法）**

**论文链接：**https://arxiv.org/pdf/2512.16811

**作者：**

Jingjing Qian，Boyao Han，Chen Shi，Lei Xiao，Long Yang，Shaoshuai Shi，Li Jiang

**摘要：**

该论文提出了一种名为GeoPredict的几何感知视觉-语言-动作（VLA）框架，专注于提升机器人在复杂操纵任务中的精确3D推理能力。该方案在公开数据集RoboCasa Human-50和LIBERO以及真实世界操纵任务中均取得了SOTA (state-of-the-art)效果。通过引入轨迹级运动预测和预测性3D高斯几何（3DGS）模块，该方案有效解决了以往 VLA 模型过于依赖2D视觉且缺乏显式3D空间建模的问题，显著提升了模型在几何密集型和空间敏感场景下的物理一致性与泛化表现。此外，预测模块仅作为训练时的监督信号，推理过程无需进行3D解码，确保了实时机器人控制的轻量化与高效性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kV4XHiaammJ7HeeYZ38qhTn31K49MjdULiag5S3A8wKJxpA30E1EKOmOkDVlibT3N0x9Gn0O1So2fG9f1aibZel9MSyUxhYIheLyIc6HJjXR7B8/640?wx_fmt=png&from=appmsg#imgIndex=5)

图: GeoPredict框架示意图

**5、Stabilizing Streaming Video Geometry via Dynamic Feature Normalization（基于动态特征归一化的流式视频几何估计方法）**

**作者**：

Xiaoyang Lyu，Muxin Liu，Xiaoshan Wu，Ruichen Wang，Yi-hua Huang，Yang-tian Sun，Shaoshuai Shi，Xiaojuan Qi

**摘要：**

该论文提出了动态特征归一化模块，来提升streaming depth的时序稳定性。现在monocular depth estimation的相对精度已经非常高了，但是在streaming input的情况下， 因为尺度和坐标原点的不一致，导致时序连续性很差。我们发现仅仅调节latent space的均值和方差就可以很好的调整output space的尺度和坐标原点。因此论文设计了动态归一化模块(DyFN: Dynamic Feature Normalization)，来实现streaming input下尺度一致性的几何估计。该方法在只用训练5%的参数下，在video depth estimation中可以超过现有所有的方法的精度，包括视频深度估计模型。该方法可以充当尺度一致的几何深度传感器，来帮助构建更好的重建，并且可以在长视频上实现一致的几何估计。

![](https://mmbiz.qpic.cn/mmbiz_png/kV4XHiaammJ6773sehUZdTib2M1ZrTLicfficUTfa9Tiad4gHTCQZj5Mv9vicpNNtTEu25m34wKkgmZiacL9UhibmJCpP1sMHLUyVPpZqIbkEJUUsY8/640?wx_fmt=png&from=appmsg#imgIndex=6)

图：DyFN整体框架结构图

计算机视觉与模式识别领域国际性会议（The IEEE/CVF Conference on Computer Vision and Pattern Recognition 2026，简称**CVPR**），由IEEE Computer Society主办，是计算机视觉领域最具影响力和公认度最高的顶级会议之一，被中国计算机学会（CCF）推荐为人工智能领域的A类会议。根据会议官方邮件通知，2026年大会共有**16,092** 篇论文进入评审流程，最终推荐接收**4,090**篇，**接收率为25.42%**。第43届CVPR将于2026年6月3日至7日在美国丹佛会议中心举行。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1wBZCGiaYqBHxH4cCwCOochEJ8ekFkaFCpZPtJBXXibYk1vt31HhZ7McAeVAryqYqUickFl10bkD5Q7922uSgGEhg/0?wx_fmt=png)

滴滴技术

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1wBZCGiaYqBHxH4cCwCOochEJ8ekFkaFCpZPtJBXXibYk1vt31HhZ7McAeVAryqYqUickFl10bkD5Q7922uSgGEhg/0?wx_fmt=png)

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