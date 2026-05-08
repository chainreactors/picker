---
title: 某地高铁通信系统遭入侵，多趟列车触发紧急制动刹停
url: https://mp.weixin.qq.com/s/mnq7RaUnaT257eS8w5Kb6w
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:54:55.997918
---

# 某地高铁通信系统遭入侵，多趟列车触发紧急制动刹停

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9UworfcDkqMypL8ylnLb2UowSr2KlLhHiaRsOchCMcWvkm274qy9BlUCxMkcK1l5GEXVqaubFcSle2KeOOd4wFaRXYjmIy1osPmt3eMSl7O8/0?wx_fmt=jpeg)

# 某地高铁通信系统遭入侵，多趟列车触发紧急制动刹停

首席安全官

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/U5H18AI6dic6lh1icDfcLh4Ry4OMxLSng9MKJyhMHXXduVqrxh698icU4HdvvwB0ndPicnegUdic1lFwAjKYldvTfJA/640?wx_fmt=gif)

点击上方“**蓝字**”，发现更多精彩。

日前，台湾高铁TETRA集群通信系统遭人为干扰，导致4趟列车被迫紧急停车48分钟。

根据台北时报的报道，2026年4月5日23:23，台湾高铁公司（THSRC）调度中心突然收到一部属于维修部门的手持电台发出的警报信号。这个"General Alarm"（GA，通用警报）是TETRA系统中优先级最高的警报类型，会自动触发区域内所有列车切换到手动紧急制动模式。

警报信号直接触发列车紧急制动流程，导致4趟列车停车共计 48 分钟。

警方通过三角定位追踪到犯罪嫌疑人林某的出租屋（TETRA基站会记录每个上行信号的接入点，通过多点信号强度比对，可以把发射源锁定在某个区域），查获11部手持电台、1台笔记本电脑、1台SDR设备。

目前，这名林姓大学生因利用软件定义无线电（SDR）设备与手持对讲机，干扰台湾高铁（THSR）使用的 TETRA 集群通信系统，直接触发列车紧急制动流程而遭逮捕。未来将面临**十年以下有期徒刑**。

警方还原了嫌疑人林某的攻击路径：

**第一步：买设备。** 在网上买了一台SDR设备（软件定义无线电），接上天线和笔记本电脑。

**第二步：监听。** 打开软件，捕获THSRC的TETRA通信流量。

**第三步：解码。** 在软件里把相关参数解出来——TETRA的空口参数、加密配置，全部暴露。

**第四步：烧录。** 把这些参数写入自己的手持电台。一共11部，想用哪部用哪部。

**第五步：触发。** 找个信号覆盖范围内的位置，按下发射键——四列高铁应声停车。

台湾高铁是台湾省的高速铁路系统，在台湾岛西部沿海运营一条单一的双向线路，全长 350 公里，列车最高时速可达 300 公里/小时。该系统年运量为 8180 万人次，是一项关键交通服务，并获得政府的财政支持

对轨道交通、物流和基础设施行业来说，这类事件的警示意义非常强。安全问题早已不只是信息泄露，而是系统一旦被错误信号影响，现实世界的调度、运行和公共安全都可能被直接牵动。

复盘整个事件，几个关键安全点值得关基设施运营者警醒：

**1. 无线电参数必须定期轮换** TETRA系统的密钥、ID、频率参数必须按固定周期更换，不能一套用十九年。这不是可选项，是基本操作。

**2. 物理安全 + 逻辑安全缺一不可** THSRC的电台都在仓库里，但参数被人克隆——说明问题不在终端，在系统层面。基站侧必须具备异常接入检测能力。

**3. SDR降低了攻击门槛** 十年前，搞清楚铁路系统的无线电参数需要昂贵的专用设备。今天，一台几百块的SDR加开源软件就可以实现攻击。关键基础设施运营者必须认识到：**攻守门槛已经严重不对等。**

**来源： 安全365  安全内参**

精彩回顾

* [六大原因让Mythos成为人工智能和全球安全转折点](https://mp.weixin.qq.com/s?__biz=MzA4NDA3ODc3OQ==&mid=3045898341&idx=1&sn=1a5ac37298089f5fea2317e96e6d0b98&scene=21#wechat_redirect)
* [这家中国网安企业达到 Mythos 级的 AI 漏洞挖掘能力](https://mp.weixin.qq.com/s?__biz=MzA4NDA3ODc3OQ==&mid=3045898349&idx=1&sn=8d6f0ca009e4790dd50f70c204e11cd9&scene=21#wechat_redirect)

* ## [推特上最全的信息安全关注列表](http://mp.weixin.qq.com/s?__biz=MzA4NDA3ODc3OQ==&mid=3045892625&idx=1&sn=9d1074bf787e61ac042a6e0e745bc314&chksm=af94bbc598e332d36260ca20c4ad5927dcf427b862efecc199ecb6dbd482c9e8a2b9e1f10818&scene=21#wechat_redirect)
* [已发布314项网络安全国家标准清单](http://mp.weixin.qq.com/s?__biz=MzA4NDA3ODc3OQ==&mid=3045892472&idx=1&sn=3c33bb824f48ff1af6c5080f64aaad2c&chksm=af94b8ac98e331ba9d89b157828fccf3a148a23150b9d0f768eb89d4b9bbe67e8522a0ae74e9&scene=21#wechat_redirect)
* ## [附下载 l 最全网络安全意识课件](http://mp.weixin.qq.com/s?__biz=MzA4NDA3ODc3OQ==&mid=3045892584&idx=1&sn=00497eac7ecacdfefcbb551ce6c23240&chksm=af94b83c98e3312ac5a08179f30b5dc644d794300302b11a9406655965cc997d4e3be8c31ab0&scene=21#wechat_redirect)
* ## [全国网络安全等保测评机构最新名录](http://mp.weixin.qq.com/s?__biz=MzA4NDA3ODc3OQ==&mid=3045893903&idx=1&sn=2aa170be2d5dac7407906aad50ad3a12&chksm=af94bedb98e337cd8f14078bf7f6c8090f52b1f60a9b51454af254d6936a95dfa5f08bb430c9&scene=21#wechat_redirect)
* ## [主流的SOC平台产品及行业实践](http://mp.weixin.qq.com/s?__biz=MzA4NDA3ODc3OQ==&mid=3045893587&idx=1&sn=de955d15f0f98cf40f26845499b59cce&chksm=af94bc0798e335119d64067bf1ecc91910c3624b3b129f2165ae8d0cc35ab2b25795ee052ecb&scene=21#wechat_redirect)
* [CSO如何展示安全建设的商业价值？](http://mp.weixin.qq.com/s?__biz=MzA4NDA3ODc3OQ==&mid=3045893020&idx=1&sn=f183d7e3a18a5698aaa8d7b81139c879&chksm=af94ba4898e3335e19032af27fb815e5352140d40cd1b9c032ebbaeaf7318441cdec5da08efb&scene=21#wechat_redirect)
* [避坑指南：安全负责人如何向高管层汇报](http://mp.weixin.qq.com/s?__biz=MzA4NDA3ODc3OQ==&mid=3045892790&idx=2&sn=b3d22b5d38f32b9aa29626d12db90930&chksm=af94bb6298e33274903d62cbe0d284db6e7e24c872052da1216eef022a676a2658a0569bff9e&scene=21#wechat_redirect)
* [网络安全从业者需要了解的法律知识](http://mp.weixin.qq.com/s?__biz=MzA4NDA3ODc3OQ==&mid=3045893476&idx=1&sn=08f54e43ec3ddc2631ecd60370474379&chksm=af94bcb098e335a68e90b92afa8ad630b33ac2059ad440bfb6a38285bd9f13d434a3091ab08d&scene=21#wechat_redirect)
* [CSO应关注20个网络安全指标](http://mp.weixin.qq.com/s?__biz=MzA4NDA3ODc3OQ==&mid=3045893314&idx=1&sn=d694848112fff27f3da268cb45f48000&chksm=af94bd1698e334001f8f2cafbe935a3277a3273b9fadb4e40a9f1ab17ca4046918ffd08f63d2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/U5H18AI6dic510wmdiaLrWyTxia5Yy7pibwz4bBO0BUibSibqic8jMDXXBkYhicrPNcxnDn93Nic4qAnAsMUa2ZgBqJv0GA/640?wx_fmt=jpeg)

（CSO安全主管群、产业群、市场群、安全意识...）

合作投稿，加群分享交流

请添加微信：CSOAlliance

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/U5H18AI6dic5kYfREy5RDDL1MWicia8cib7teSpiaWXVEHgKezdStXwuCEGibr6jwAjITtuavycrzFk8Csib1xpYvQibkg/0?wx_fmt=png)

首席安全官

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/U5H18AI6dic5kYfREy5RDDL1MWicia8cib7teSpiaWXVEHgKezdStXwuCEGibr6jwAjITtuavycrzFk8Csib1xpYvQibkg/0?wx_fmt=png)

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