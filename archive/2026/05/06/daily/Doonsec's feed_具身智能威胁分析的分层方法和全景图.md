---
title: 具身智能威胁分析的分层方法和全景图
url: https://mp.weixin.qq.com/s/lXkKpvotnsJNmAzUZloufw
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:25:26.449490
---

# 具身智能威胁分析的分层方法和全景图

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ccVb6wGibibCH6Fow9wwLkbYicf6FfsWIqmxv9x4qOO6DG41LGElGp5aECR9pRL8Y4O0uHiaOIfjLsowV2WX1tmQevxyibKN8MVOicr7MQ1F9u76k/0?wx_fmt=jpeg)

# 具身智能威胁分析的分层方法和全景图

原创

孙志敏
孙志敏

AI与安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

威胁分析及消减是安全设计的核心内容，完整的威胁分析对于系统的安全非常重要。

具身人工智能（Embodied AI）将感知、认知、规划与交互能力整合到能够在开放世界及安全关键环境中运行的智能体中。随着这些系统获得自主性并应用于交通、医疗、工业或辅助机器人等领域，确保其安全性不仅面临技术挑战，更具有社会层面的迫切需求。

现有的人工智能安全研究主要聚焦于纯数字系统，例如视觉基础模型、大型语言模型、多模态大型语言模型或数字智能体等。虽然这些研究提供了有价值的攻击与防御分类体系，但鲜少涉及感知、认知、规划和交互紧密耦合且必须在现实世界约束下运行的具身化场景。

近期，复旦大学，上海创智学院等多个组织，对400多篇论文进行分析后，提出了完整的具身智能威胁分析的全景，值得借鉴。

论文在

https://arxiv.org/pdf/2605.02900

01

能力分层与风险的对应关系

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCGFaa76CgUfWoQu4C1lboeh2YkAfjMGRp1F1d7S6bIoOw628Y2ll4NaxyzZvdwyOKajnImRHRQibeh7a5ls4lJUuTQV5FdArvfM/640?wx_fmt=png&from=appmsg)

如上图左，将智能体的能力分层，分别为：感知层（最内层），认知层，规划层，动作层和智能体系统（最外层）的嵌套式能力层级结构，各层级分别对应不对的风险，如上图右，随着能力向外扩展，攻击面相应扩大——内层漏洞会级联影响外层系统，从而加剧高度自主系统的安全风险。

02

各层的攻击方法及危害

对于五层攻击的关系，论文中给出下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCHemsbhpRKQ60nJpHAGSAJEtvAHvGgall37lkYHkNlhKHibZ7hhwiaAAIhIicouAjkxMKbZbg8WZLPH3bRQuiaBLQ9KmPEfiacicK1BY/640?wx_fmt=png&from=appmsg)

这个图比较形象，但看起来有点费劲，画个脑图是这样的，每个叶子节点对应一个威胁分类，其中$xx代表论文中的章节：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ccVb6wGibibCE9JTVc859v2nzNHcfolsm4L31XmPK2QcO9kCexufSdkcFuxVeXaf60yD1SpeMAxFIuaT0KZwvBqA93wv3j8Fkmdiblg6uM9gak/640?wx_fmt=png&from=appmsg)

03

完整的攻击和防护方法

本部分比较长，适合作设计的时候使用，可以结合 [AI时代的威胁建模框架：MAESTRO](https://mp.weixin.qq.com/s?__biz=Mzg5NTMxMjQ4OA==&mid=2247485921&idx=1&sn=5c534fe603abc71968a94c9ee2e40c34&scene=21#wechat_redirect)，同时需要强调，文中的威胁和防护方法，提到了诸多的论文，直接引用可能比较困难，但非常值得参考。对于新兴的威胁，我们将持续深度分析，有兴趣的请关注跟踪。

建议收藏，以备使用。实际使用表格更方便一些，如果需要，文后扫码联系。

§ 2

👁  感知层 Perception

▸ 视觉感知 Visual Perception (§ 2.1)

⚠ 对抗攻击

🔴 攻击方法

•白盒数字:RTAA、TrackPGD 利用时序信息扰动单目标跟踪

•白盒物理:DARTS、RP2 在交通标志贴对抗贴纸;ShapeShifter 拓展物理域

•黑盒物理:CAMOU 扰动车辆外观;MobilBye、SSPA 投影幻影目标

•针对 CLIP:AnyAttack 在 LAION-400M 预训练扰动生成器,跨模型迁移

•光流:PCFA 全局扰动将预测光流推向攻击者目标

🟢 防护方法

•鲁棒训练:DSNet/IA-YOLO/BAD-Net 联合学习能见度增强与目标检测

•对抗训练:RP-PGD 用于语义分割

•输入审核:AOD-Net 除雾;DGFN 通过门控融合相机与 LiDAR

•CLIP 防护:TeCoA 对比对抗微调,Robust CLIP 无监督对抗微调

•输出审核:SentiNet 定位可疑区域

⚠ 后门攻击

🔴 攻击方法

•训练操控:TrojViT 通过 RowHammer 位翻转;SWARM 针对 prompt-tuned ViT

•数据投毒:Han 等以物理对象为触发器投毒目标检测

•BadLANE、DBALD 通过元学习/扩散合成嵌入视觉模式触发器

•BadEncoder 在 CLIP 等预训练编码器中注入后门(供应链威胁)

•BadCLIP 双嵌入引导;BadVision 利用 SSL 后门诱导 LVLM 视觉幻觉

🟢 防护方法

•ViT 防护:Doan 等利用 patch 变换响应特性检测触发器

•CleanCLIP 通过多模态对比微调重对齐表征以削弱后门关联

•DECREE 在无分类头/标签条件下检测预训练编码器后门

•BDetCLIP 通过对比性 prompt 实现高效测试时检测

•(任务专用视觉后门防御研究尚不充分,是开放挑战)

▸ 听觉感知 Auditory Perception (§ 2.2)

⚠ 对抗攻击

🔴 攻击方法

•白盒物理:Carlini 等将语音命令转为人耳无法理解形式

•CommanderSong 将扰动嵌入歌曲;Metamorph 用背景类音频扰动

•Li 等加入房间冲激响应保持空中播放有效

•黑盒:Devil's Whisper 配对查询替代与白盒识别器构造对抗样本

•Vaspy 通过语音识别和声音克隆合成激活关键字

🟢 防护方法

•Samizade 等提取 MFCC 特征用 CNN 分类

•Yang 等用扰动、压缩、量化、平滑、重构等预处理

•AudioPure 通过扩散模型净化和恢复输入信号

•AntiFake 嵌入保护性扰动以防止声音克隆

•MVP-EARS 多模型交叉验证转写一致性

⚠ 后门攻击

🔴 攻击方法

•TrojanModel 通过训练操控将后门注入声学模型

•(听觉后门研究尚处萌芽阶段)

🟢 防护方法

•暂未提出针对听觉后门的专用防御

•可借鉴视觉编码器后门防护:模态间对比微调、测试时检测

•建议:多模型交叉验证 + 异常输入特征分布检测

•(语音具身系统后门防御是重要的开放挑战)

▸ 空间感知 Spatial Perception (§ 2.3)

⚠ 对抗攻击

🔴 攻击方法

•白盒数字:FLAT 操控车辆轨迹影响 LiDAR 运动补偿;SlowLiDAR 慢动作扰动

•Poison-Splat 攻击 3DGS 自适应密度控制,造成内存/算力 DoS

•白盒物理:LiDAR-Adv、Tu 等优化 3D 网格几何

•Adv3D 直接将对抗对象嵌入 NeRF;ShadowHack 操控阴影模式

•AoR 用对抗补丁触发假闭环导致定位漂移

•黑盒:SpotAttack 用遗传算法搜索非反光对抗点;DoubleStar 远程光斑伪造障碍物

🟢 防护方法

•鲁棒训练:Defense-PointNet、PointCutMix 数据增强

•3D-VField 矢量场对抗增强;LISA LiDAR 专用增强

•形式化方法:CATNIPS 严格估算碰撞概率;SAFER-Splat 在 3DGS 嵌入 CBF

•多模态融合:AcousticFusion 融合听觉与视觉 SLAM

•输入审核:PointGuard 提供认证鲁棒性;LiDARPure 用扩散模型净化点云

•ShadowCatcher、LOP 通过物理不变量检测对抗点云

⚠ 后门攻击

🔴 攻击方法

•Zhang 等在鸟瞰图(BEV)表征中注入像素级触发器

•BadLiDet 在 3D 目标检测器中嵌入不可感知的点级扰动

•BadLiSeg 通过精心制作的伪造模式在 LiDAR 分割中嵌入后门

🟢 防护方法

•暂无专门针对空间后门攻击的防御方案

•建议:借鉴视觉后门防御的检测-清除范式

•建议:辅以 3D 几何一致性校验

•建议:多传感器融合冗余,对单一通道注入做交叉验证

•(3D 感知后门安全是关键开放挑战)

▸ 运动感知 Motion Perception (§ 2.4)

⚠ 传感器攻击 - 欺骗

🔴 攻击方法

•GNSS 重放欺骗:Lenhart 用商用 SDR 长距离实时中继

•GNSS 生成欺骗:FusionRipper 融合感知扰动;Dasgupta 慢漂移攻击

•IMU 声学注入:Son、WALNUT、KITE 利用机械共振诱发陀螺仪偏差

•超声波声学注入:Yan、Xu、Gluck 等用伪造回波欺骗距离测量

•毫米波雷达 RF 注入:mmSpoof、MetaWave、TileMask 用元材料操控雷达反射

🟢 防护方法

•GNSS 检测:Crowd-GPS-Sec 跨设备时空一致性;DeepSIM 卫星图匹配

•GNSS 认证:SAS 加密认证序列;NMA(Galileo TESLA);Chimera 时间绑定标签

•GNSS 缓解:UNROCKER 去噪自编码;VIMU 物理建模 + 异常检测

•IMU 防护:SDI 跨传感器一致性;CPD-MhIMU 多种异构 IMU + 自适应 EKF 融合

•超声波:SoundFence 随机化脉冲周期;SecureTrack 集成 EMI 监测

•毫米波:Sun 提出挑战-响应机制;Nallabolu 设计混合斜率啁啾

⚠ 传感器攻击 - 干扰

🔴 攻击方法

•声学干扰:Lim 用大功率声波干扰超声波,导致漏检与控制失稳

•电磁干扰:Jang 等远程电磁注入,破坏 IMU 与飞控通信

•(干扰类攻击通过物理层漏洞用高能噪声压制感知通道)

🟢 防护方法

•GNSS 抗干扰检测:Swinney 用 VGG16 迁移学习融合时频域

•Spanghero 用 VTOL UAV 定位干扰源

•GNSS 抗干扰缓解:Wang 用 Reservoir Computing + LSTM 重建受扰信号

•MFMC 多频率多星座接收机利用信号多样性

•建议:跨传感器冗余(GPS/IMU/视觉里程计互校验) + 可信回退模式

▸ 跨模态感知 Cross-Modal Perception (§ 2.5)

⚠ 对抗攻击

🔴 攻击方法

•Li 等仅扰动 LiDAR 单通道即可欺骗融合模型(200 个对抗点 99% 成功率)

•DejaVu 利用同步依赖,单帧 LiDAR 延迟使 3D 检测 mAP 降 88.5%

•Cao 等首个物理世界攻击同时欺骗相机与 LiDAR(3D 打印对抗对象)

•Hallyburton 提出 frustum 攻击,通过黑盒 LiDAR 欺骗规避 8 种主流融合检测

•Li 等用单一对抗对象同时攻击相机/LiDAR/雷达三模态

🟢 防护方法

•鲁棒训练:Wang 等提出多通道对抗训练对抗跨通道外部性

•认证防护:MMCert 通过跨模态随机平滑导出可证明鲁棒性界

•输入消毒:Yang 等开发的稳健多传感器融合在融合前对各模态分别消毒

•工程建议:在融合层强制时间同步校验,异常通道权重降级

•工程建议:利用模态间冗余设计 fallback(模态降级而非全面失效)

§ 3

🧠  认知层 Cognition

▸ 指令理解 Instruction Understanding (§ 3.1)

⚠ 越狱攻击

🔴 攻击方法

•白盒越狱:CHAI 针对物理智能体 LVLM 命令层优化对抗指令

•黑盒越狱:构造语义合理 prompt 利用安全过滤器弱点

•BadNAVer 证明具身导航中越狱直接触发不安全的物理动作

•其他向量:利用安全对齐失配、上下文越狱、概念欺骗

🟢 防护方法

•J-DAPT 引入多模态域适配,通过视觉-语言对齐识别对抗指令

•Abuduweili 等结合可达性分析与 LLM 控制机器人,提供形式化安全保证

•通过『拒绝预测违反安全包络的指令』实现可达性强制

•评测基准:IndustryEQA、AGENTSAFE、EmbodiedBench 等具身安全 benchmark

▸ 世界模型 World Model (§ 3.2)

⚠ 幻觉新兴风险

🔴 攻击方法

•Chen 等揭示多目标幻觉在 VLM 具身场景理解中普遍存在

•Tao 等证明视觉-文本任务中幻觉对具身代理尤为严重

•Baraldi 等识别场景生成病理性标准:时间一致性、物理符合性、条件一致性

•MASH-VLM 揭示视频 LLM 中动作-场景误归属问题

🟢 防护方法

•MASH-VLM 通过 DST-attention 解耦时空 token 削弱幻觉

•建议:VLM 输出与多模态感知交叉一致性校验

•建议:幻觉检测器 + 物理可行性验证(可结合 affordance grounding)

•建议:视觉-文本对齐损失增强训练,降低描述与场景偏差

⚠ 规则违反

🔴 攻击方法

•Li 等指出错误累积/分布漂移/物理一致性是世界模型关键挑战

•Wen 等发现视频预测 rollout 累积误差限制长时域可靠性

•(模型可能违反物理定律、领域规则、安全约束,直接转化为不安全行为)

🟢 防护方法

•HRSSM 学习潜在动态稳健表征改善对分布漂移的弹性

•SafeDreamer 在 Dreamer 框架集成 Lagrangian 安全约束

•VL-SAFE 用 VLM 派生的安全分数监督世界模型

•Drive-WM 用多视图扩散用于更安全的轨迹选择

•(注意:用 WM 生成数据训练规划器会引入级联风险)

▸ 推理 Reasoning (§ 3.3)

⚠ 推理攻击

🔴 攻击方法

•CoT 劫持:H-CoT 通过插入对抗步骤劫持思维链至有害结论

•Grounding 失败:Chakraborty 等证明场景-任务不一致使幻觉率提升 40 倍

•Han 等证明 LLM 在火灾导航中引导机器人冲向服务器机房而非紧急出口

•(高总体准确率可能掩盖安全敏感场景的关键 grounding 失败)

🟢 防护方法

•建议:CoT 审计 - 对中间推理步骤做安全验证

•建议:场景-任务一致性检测器,对 grounding 失败预警

•建议:借鉴 SayCan affordance grounding 与 Inner Monologue 反馈闭环

•建议:对安全敏感任务设置 fallback(无法执行优先停止)

•建议:可结合规划层的 SafePlan 等形式化逻辑验证机制

§ 4

🗺  规划层 Planning

▸ 任务规划 Task Planning (§ 4.1)

⚠ 对抗攻击

🔴 攻击方法

•Islam 等证明小幅视觉扰动可误导 CLIP 类视觉-语言导航

•Vemprala & Kapoor 证明对抗状态构型可使经典优化规划器特征结构退化

🟢 防护方法

•建议:对规划输入做异常检测(图像/状态),触发 fallback

•建议:多假设规划 + 风险加权选择,降低单一被扰动方案被采纳的概率

⚠ 越狱攻击

🔴 攻击方法

•白盒:EIRAD 调整梯度后缀优化;POEX 用变异-选择-评估循环

•黑盒:RoboPAIR 自动化越狱,加机器人专用 prompt 与语法检查

•BADROBOT 识别三类具身专属攻击面:上下文越狱、安全对齐失配、概念欺骗

•POEX 在真机器人验证攻击,引入 Harmful-RLBench 良性-有害任务对比基准

🟢 防护方法

•SafeEmbodAI 集成安全 prompt、状态管理、安全验证模块

•NPE 用 Chain-of-Thought、Plan-and-Solve 结构化模板增强鲁棒性

•J-DAPT 通过注意力融合文本/视觉嵌入,适配机器人专用越狱数据集

•RoboSafe 结合反向反思推理与正向预测推理,生成可执行谓词级安全逻辑

•CEE 将内部表征引导至安全概念以防御越狱

•SafePlan 在 CoT 流水线多点插入形式化逻辑验证以过滤不安全计划

⚠ 后门攻击

🔴 攻击方法

•CBA 用文本 + 视觉触发器投毒上下文示范以激活有害行为

•BALD 系统化分类基于 LLM 规划器后门路径(词级/场景操控/RAG 注入)

•Robo-Troj 通过软提示有毒微调注入恶意计划,触发词出现时激活

🟢 防护方法

•建议:对训练数据做触发器扫描,对 In-Context demos 做完整性校验

•建议:对 RAG 知识库做来源验证与签名,防止知识投毒

•建议:运行时对计划做安全前置检查(可结合 RoboSafe、SafePlan)

•(任务规划后门防御研究尚不充分,是开放挑战)

▸ 轨迹规划 Trajectory Planning (§ 4.2)

⚠ 对抗攻击

🔴 攻击方法

•白盒:Zhang 等扰动名义车辆轨迹最大化预测误差;AdvDO 构造可信轨迹

•KING 用可微分运动学高效搜索关键场景;Adv-GAN 配合 MPC 优化

•ADvLM 通过语义不变诱导针对 VLM 自驾

•黑盒:AdvSim、STRIVE、AdvDiffuser 用扩散指导生成失败诱导场景

•Avatar 用 RL 优化对抗轨迹;NADE 生成自然主义对抗驾驶场景

•JackZebra 通过攻击者车辆对抗补丁实现长时域目标劫持

🟢 防护方法

•鲁棒训练:Thumm 提出主动替换与投影方法在 RL 训练时减少 failsafe 介入

•AR-ICRL 扩展逆 RL 从专家演示推断安全约束

•鲁棒推理:SMPC 用随机 MPC 加备份轨迹(可达集),违反约束时覆盖输出

•Yurtsever 在运行时识别危险行为,过滤或降权高风险机动

•CSP-GAN-LSTM 结合卷积池化与注意力轨迹预测,推理时计算碰撞风险

⚠ 越狱攻击

🔴...