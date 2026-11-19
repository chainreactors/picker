---
title: 在茫茫大洋里找一艘“静默”航母：遥感 + Agent Harness 的找船实践
url: https://mp.weixin.qq.com/s/LhN7DW8hgiav7E5nfRmwkg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:39:35.067286
---

# 在茫茫大洋里找一艘“静默”航母：遥感 + Agent Harness 的找船实践

# 在茫茫大洋里找一艘“静默”航母：遥感 + Agent Harness 的找船实践

原创

mapxiaotu
mapxiaotu

空天感知

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

今年2月份了解到有找船这个业务需求，一直没时间研究。最近半个月，借助AI的强大能力，搭了一套pipeline，可以实现对外方（A国）的船只进行位置推理，置信度还不错，分享下成果。

常规开源追踪基本是“人肉等消息”：情报账号发张照片就标个点，下条消息出来前，中间两三天、上千公里的空白全靠猜。我尝试

## 一、找船是个很难的事情

在我试验过程发现找船至少有以下两个难点：

1、卫星看得清，但“找不到地方看”：10 米分辨率的光学卫星看航母绰绰有余，可单景幅宽有限、重访周期长，南海和印度洋还常年多云，满海漫无目的地拉图既慢又容易把碎云误认成船。

2、开源消息真假掺半，时间线经常错位：新闻、社媒里经常把几天前拍的旧图当成当天动态，稍微不注意就会把航迹推偏几千公里。

**我尝试用以下流程给出解法：**

**让开源情报和航道推演先把搜索范围压到局部海域，再用卫星切片做物理确认；全程使用大模型的能力参与推理，就像是一个经验丰富的参谋一样，并且要对大模型赋予Harness来确保成果的置信度。**

## 二、找船的自动化流程

首先输入是船名或舷号，加一个时间窗口。

系统将自己翻公开报道、舰队追踪、社媒目击，抽出时间地点；用航道、水深、航速筛掉不可能的点，做多源融合；再顺着航迹找当天过境、云量能接受的卫星切片，只取局部，跑检测；最后输出位置和搜索半径。

## 三、三次找船实践

## 在严格隔离事后消息、纯靠系统自动抓数与推演的前提下，我们连续验证了“罗斯福”号从南海进入印度洋的三次关键节点

### **11 月 4 日 · 南海万安滩西南**

系统顺着南海西南航道自动调取了当天的哨兵二号 10 米光学切片。由于 10 米图上灰色甲板和青白色尾迹经常粘在一起，我们通过主轴光谱剥离把船体和尾迹拆开测量：**实测舰长 335 米**（与尼米兹级 333 米高度吻合）、**尾迹长 1,103.5 米**、**航向 279.6°**，并在同一片海域抓到了两艘同向护航的 135 米级驱逐舰。

![](https://mmbiz.qpic.cn/mmbiz_png/cemuAg1hRPtAudpWrodXScw79UYPvGvbvnC4XakPVdhHCUYYZXPBMhpyOmLcBRcqvAGrxln0dEJZjIEmXK3PUL7Aiavg3ep45iaaCuPAkDYiaY/640?from=appmsg)

11 月 4 日，Sentinel-2 10m 光学实测检出 CVN-71 舰体与尾迹， 约 6.03°N, 108.47°E，航向约 280°

![](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPuavnAfgDaWq0ibUEvj9ibJwsibn5libQ1zWpO7r6bCyibQpwPL0rfSARGgtriaqdYFUjvM9SruicibFWqwn8rUA9jOgxBqQmaagibRXC3c/640?from=appmsg)

南海广域打击群切片：航母本体与伴随护航舰

### 11 月 6 日 · 新加坡樟宜外海

把系统时间严格截断在 11 月 6 日当天。系统自动检索到美国海军学会新闻网（USNI）发布的入港报道，随即把定位锚定在 **`1.32°N, 104.03°E`**。

对比推特卫星博主公布的 11 月 6 日 Landsat-8 实拍图（“罗斯福”号靠泊樟宜军港前 30 分钟，真值 **`1.2808°N, 104.1312°E`**），**纯代码推演结果与卫星真值仅相差 12 公里**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cemuAg1hRPvQseMvKkH3ngdHm3BY221qGuyicr3ibOlRFG1yeVXU5q0QbOiahXR6N8xiaRWhZQZhnDmxla1tYCabJ8ICmxUibwq1MqDunibicTGnKw/640?from=appmsg)

OSINT Digest 公布的 6 日 Landsat-8 实拍

![](https://mmbiz.qpic.cn/mmbiz_png/cemuAg1hRPtBUlibRW7WNfaFpNQfADaevBVRswI2BjELglsvZrgLhjMHwQJlH3iaRlxsZwFStF0xgSHWA8icfbz7tt68a0jvyx2rfxOF0g6bdw/640?from=appmsg)

绿圈是系统推算，橙星是实拍，相距 12.06 公里

### 11 月 13–14 日 · 印度南端外海

11 月 8 日航母西出新加坡海峡进入印度洋后，新闻报道明显变少。系统通过定向社媒检索捕捞到离开新加坡的目击动态，顺着“马六甲 → 斯里兰卡外海 → 阿拉伯海”航道，将 11 月 14 日深夜位置推演至 8.82°N, 72.82°E。

对照 OSINT Digest 发布的 11 月 13 日印度最南端外海实拍真值（6.42°N, 77.03°E），两者刚好在同一条西北进阿拉伯海的航线上，顺航向推进约 534 公里——正好对应航母一天左右的正常航程。

![](https://mmbiz.qpic.cn/mmbiz_jpg/cemuAg1hRPvjWENvjJRXV8g2ibXkCK9T7Aqxn55Cwy42xuoAkpp3T6e0NiaGoWAIxKnqaCe5jNJ1Eo7HickNSjiavGHcXEu71L1UicbzJj4ML5ps/640?from=appmsg)

OSINT Digest 公布的 13 日实拍

![](https://mmbiz.qpic.cn/mmbiz_png/cemuAg1hRPsnUxL93jdNfvI2RdESKKjx2fficpgOm43G3pr1Am4RAEMCm3rqe1vIf8pxWMO8OdgPWThmhrpibiapdjmkWLFabUvrbiarcSJeCQU/640?from=appmsg)

11 月 2–14 日推演航迹与三次卫星真值

## 三、技术重点：关键是Agent Harness，而不单纯是模型

这里必须要提的是，在这个严肃场景下，如果是纯Agent，让AI自己去“让它自己决定要不要搜推特、自己猜经纬度、自己决定要不要下卫星图”极易产生幻觉。

**这套系统是 `Agentic`**：主流程由确定性代码编排，但系统具备明显的“能动闭环”——比如新闻/社媒缺口时自动触发全网与 X 分片检索、航线外推远了自动去开卫星天窗、卫星真检出船体了再自动回灌修正航迹，最后由 **Agent Harness（智能体约束框架）**兜底核验才能输出结论。

比如以下的例子：

1. **算力与几何全部留给确定性算法**

   相关的地理投影、航迹计算、舰船检测，全部由物理与视觉算法完成；大模型只负责读懂文本、拆解时间地点和梳理证据冲突，**绝不让它直接算坐标**。
2. **没有实证就老实说“不知道”**

   Harness 会逐条核验模型输出的依据。只要卫星图被云挡住或者没检出匹配尺度的船体，系统就必须诚实标为“未确认”，禁止靠模板或想象力补全结果。
3. **只按局部窗口采样，算清每一笔账**

   无论是只拉几兆的局部卫星切片，还是按账号分片检索公开推文，Harness 把每一次外部调用都锁死在预算和配额门限内，保证系统能长期稳定跑在真实业务里。

一些受限：

目前找船的信息收集还集中在A国，其他国家的也暂没有精力做，并且还集中在航母上。如果是根本没有任何开源QB的，比如针对海事缉私等要抓的暗船，那我这套方法是不起作用的。

## 最后

有个十分真切的感受，AI的能力已经十分强大。仅仅找船这一个小场景，Agent就能做到在处理海量数据、复杂任务时的超人类能力。

而不论是军事还是其他场景，可能就是多个Agent之间的串并联来高效解决，未来的竞争，就在于AI模型能力的比拼。

「找船」这个工具开发过程中得到了公众号“Remote Sensing

 Dong”的博主大力支持，在此表示感谢~Dong是经验十分丰富的遥感专家，对于找船也有一套独到的方法。如果读者朋友们对找船或者类似方向有业务场景，也欢迎多沟通。

（联系作者：mapxiaotu)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ObyhaySm97WZNjpySwibqk7H5ntMHKzv68D9ES1ajKEoa99iaKyw0UHfrzyqxcAe0RgoS61lwXicia92djIK593Atg/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过