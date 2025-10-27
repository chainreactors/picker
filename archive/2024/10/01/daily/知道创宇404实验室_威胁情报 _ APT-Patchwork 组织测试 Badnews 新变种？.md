---
title: 威胁情报 | APT-Patchwork 组织测试 Badnews 新变种？
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650988765&idx=1&sn=2bcaf1e549d0c3b99a4a7a2a492a2d08&chksm=8079a2efb70e2bf9337cf95a53e60317e784143479752191a61f155ec2e1cf0e37701e29b81b&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-10-01
fetch_date: 2025-10-06T18:52:33.255772
---

# 威胁情报 | APT-Patchwork 组织测试 Badnews 新变种？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT3eQDFuafBicBBgAdmkLU4luWJsypu3aRgAHFU7u64xibJDwTIEStJbsBT65iczgRqHcYVZsH9Ju11icg/0?wx_fmt=jpeg)

# 威胁情报 | APT-Patchwork 组织测试 Badnews 新变种？

原创

404高级威胁情报

知道创宇404实验室

**作****者：**知道创宇404高级威胁情报团队****

**时间：2024年9月30日**

**1 分析概述**

参考资料

近期，知道创宇404高级威胁情报团队在分析过程中发现一个与Patchwork组织历史TTP极其相似的样本，该样本使用Patchwork常用的donut加载执行最终的载荷。最终载荷与该组织已知的武器badnews在代码方面存在大量重合，相比老版本的badnews具备以下特点：

1) 使用base64+Salsa20进行数据加密。
2) 在badnews的基础上进行了功能插件化。
3) 去除了badnews部分已知的流量及文件检测特征。

基于上述特点我们将其归为badnews新变种，经过分析还发现攻击者下发的诱饵文件为空白PDF文档，同时我们大胆推测该样本或为Patchwork内部人员进行武器更新而提交的测试样本。

以下将对该样本进行详细分析。

**2 组织背景**

参考资料

Patchwork(摩诃草、白象)是一个来自南亚地区的APT组织，因其攻击活动中频繁使用各种开源工具而得名。该组织自2015年以来，长期针对中国、巴基斯坦等亚洲国家政府、医疗和科研等领域展开窃密攻击活动。

**3 样本分析**

参考资料

#### **3.1 攻击链**

根据分析，整体攻击链如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3eQDFuafBicBBgAdmkLU4lunmPmbJUf1m1wlFic98jZn0ASOYgicj8gsSLFU2kF76Wfibdbqav7wsXKA/640?wx_fmt=png&from=appmsg)

攻击链

#### **3.2 样本执行流程**

初始样本其指令参数解析如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3eQDFuafBicBBgAdmkLU4luJd7vfbQLY2VRUXKMvagtoVVbLPP4k4wXftedJvyuk75awSkkF22MDw/640?wx_fmt=png&from=appmsg)

lnk指令解析

lnk指令主要功能为：

1. 从下载服务器下载诱饵文档并存储然后运行诱饵文档。
2. 从下载服务器下载恶意载荷并存储为C:\ProgramData\hal，将其重命名为“C:\ProgramData\wer.dll”。
3. 从系统目录复制WerFaultSecure.exe到wer.dll同目录。
4. 创建计划任务，计划任务运行WerFaultSecure.exe。
5. 删除原文件。

wer.dll被加载后解密出shellcode，解密相关参数如下

Key：“Keet96vUkMdJThac”
IV：“ivnpFrICQCEKklCi”
解密流程为base64-AES-base64：

通过分析后确认shellcode为Patchwork频繁使用的开源加载器donut，该加载器能够加载和执行多种类型载荷，在本次样本中最终运行的载荷为badnews变种

#### **3.3 Badnews分析描述**

本次发现的badnews变种主要利用插件下发的形式实现主要的功能，这导致其载荷的文件大小相比以往捕获的badnews样本更小。具体分析如下：

获取MAC地址、用户名、主机私有ip.

将获取的MAC、用户名和私有IP拼接后计算其sha256值，在本样本中该值用来作为uid，对uid进行加密，后续该值在心跳及交互过程中均会进行回传。

除上述外，还会获取的数据包括：pid和windows版本，将获取的数据进行加密后使用“$”进行拼接，加密算法为base64-Salsa20-base64，其中Salsa20加密的相关参数如下：

Key：WfqZP6j5IXWaZXJy0KyVh1KFPatF3Uod

nonce：xKPiP4K9

首次上线时，还将固定字符“Nexe”和硬编码的User-Agent“zc9k4OMihkyxpJIGR8CjxVgoBvv9PB”一起拼接后上传：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3eQDFuafBicBBgAdmkLU4luFKATB0CCYXxFsbb9WAjmtXRsy5QpE1pBkic6Z7Yj8kcEDeqWnHulzicA/640?wx_fmt=png&from=appmsg)

使用固定User-Agent通信

创建两个线程，一个为负责与服务端保持心跳，一个则负责从服务端接收数据并实现相关功能 从服务端获取的数据经过解密后使用“||”对其中的指令进行分割，支持的指令有：filelist、download、upload、uplexe和screenshot。除指令外解密的数据中还包含了对应功能需要使用的参数及组件下载地址。当服务端下发的指令为uplexe时执行参数中的cmd命令，若为其它时则需要从返回数据中提取出组件下载地址并下载，最终将组件加载执行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3eQDFuafBicBBgAdmkLU4lu8bDZUxoHX46N3nml1IIgic0iax2Oia1svibbAODtS841GhAVsxQnPJ4HGA/640?wx_fmt=png&from=appmsg)

指令分支

下载的组件使用QueueUserAPC注入到explorer.exe中：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3eQDFuafBicBBgAdmkLU4luSH7bnCRscSdyd5MI2QqMTOgBdYcag5pCVhz6ZMcU7uYj53SBgZxSpw/640?wx_fmt=png&from=appmsg)

组件注入执行

以下为通信格式及功能说明：

| Url | Body | 说明 |
| --- | --- | --- |
| /cDiCQddlQr | cd=[uid]&...&kossecca=SCq4TeCn0C3i58/FA4lEtFM1dTTvZ6tq | Online |
| /chBXgPelzd | cu=[uid]&mod=TCuSbveH2Ho=&kossecca=SCq4TeCn0C3i58/FA4lEtFM1dTTvZ6tq | GetCommand |
| /peCDMAFXQN | cu=[uid]&kossecca=SCq4TeCn0C3i58/FA4lEtFM1dTTvZ6tq | heartbeat |
| /DBbCKhYPhhY | did=[command]&pk=[parameter]&inf=[result data]&ack=[decrypt 1]&[uid] | UploadResult |

**4 归因及总结**

参考资料

本次捕获的样本与Patchwork组织近期频繁使用的TTP有诸多相似之处，例如在团队在7月份曝光的该组织针对不丹的攻击活动中lnk参数部分与本次在结构上几乎一致：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3eQDFuafBicBBgAdmkLU4luGeDjowroXGuic3roZXwTrH0k8GjfMcVoDHzGVKfpRpY8y1viaQGsYkKA/640?wx_fmt=png&from=appmsg)

针对不丹攻击中lnk参数解析

在加载器方面，Patchwork是目前已曝光APT组织中使用dount最频繁的，特别是近两年使用NorthStar的攻击链中，这与该组织使用开源武器的“传统”是一致的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3eQDFuafBicBBgAdmkLU4lu9TOjeJ4QNJpiatB7dCYzEyibS09Qdve3l7Peic0VC7V2NLtEIegJCkGYw/640?wx_fmt=png&from=appmsg)

Patchwork组织常用的donut-NorthStar TTP

本次的最终载荷与归属于该组织的独有武器badnews有诸多相似之处，详细如下：

1、以往曝光的badnews中加密算法从RC4-Base64到AES-Base64再到base64+AES+base64，base64始终是该武器加密算法中的一部分，与本次在加密算法有相似之处：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3eQDFuafBicBBgAdmkLU4lucy2G68VEzLcaF5ONboRZXecicX1GOgdp1Hh2jOdtt6S7gAg61yzaqPw/640?wx_fmt=png&from=appmsg)

Badnews使用base64+AES+base64加密数据

2、都利用公开API获取主机公共IP：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3eQDFuafBicBBgAdmkLU4luUOzRInpxeR0JOK9ibtRg8eO8ECFgZyDqicW9h3Bn1icUUVGiaibic4jhomaQ/640?wx_fmt=png&from=appmsg)

Badnews使用公共API查询IP

3、相似的数据回传结构，在以往曝光的badnews中，使用与本次类似的结构回传获取的主机信息，并且在末尾使用固定的字符，例如此前使用“crc=e3e6”，本次则使用“kossecca=SCq4TeCn0C3i58/FA4lEtFM1dTTvZ6tq”

4、在武器功能方面，本次样本与badnews在功能上几乎一致，下图为badnews功能列表：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3eQDFuafBicBBgAdmkLU4luODagboTn0bNkrqFD3lx9VahvRMgRZFmiaPlWOqlOahJia4S4jolxSAmA/640?wx_fmt=png&from=appmsg)

综上我们有极大的信心认为本次捕获样本系Patchwork组织最新badnews变种，该组织开发人员目前正在对badnews进行改造，例如，在样本侧对已知的部分文件特征进行修改或删除，同时将部分功能组件化，以达到载荷轻量化的目的；在流量侧则积极使用https进行加密通信，并对流量结构进行了升级。此外，正如开篇所言，本次捕获的样本在诱饵文档中使用空白文档，这让我们有理由怀疑目前变种badnews正在积极测试中，当然也不排除攻击者故意为之，毕竟当点开lnk文件的那一刻起，整个攻击活动已经进行了，诱饵文档只能在一定程度上麻痹受害者。截止分析时，我们还溯源到多个同类型样本，样本主要分为EXE文件和DLL文件两种形式，整体执行流程是一致的，其中EXE文件暂未溯源到初始载荷，后续团队将持续跟踪此类型攻击活动。

安全不可能是一成不变的，面对日趋严重的APT攻击活动，在此提醒广大网民朋友，守住好奇心，切勿点击未知的文件，及时更新系统补丁。

**5 IOC**

参考资料

Hash：
d7b278d20f47203da07c33f646844e74cb690ed802f2ba27a74e216368df7db9
ba262c587f1f5df7c2ab763434ef80785c5b51cac861774bf66d579368b56e31

C2：
scapematic.info
iceandfire.xyz

对本次报告的更多相关内容感兴趣，请联系知道创宇404高级威胁情报团队 intel-apt@knownsec.com

![](https://mmbiz.qpic.cn/mmbiz_gif/3k9IT3oQhT0Z79Hq9GCticVica4ufkjk5xiarRicG97E3oEcibNSrgdGSsdicWibkc8ycazhQiaA81j3o0cvzR5x4kRIcQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**往 期 热 门**

(点击图片跳转）

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3zWxDukibIv3z7ld9Hn07vSnt3QR3OWvewW02teMkdvAAGX9uafrfapA5eQCheDPRPInG2x3iah9gQ/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650988737&idx=1&sn=b8775b1bc9b159024497056a959eccf6&chksm=8079a2f3b70e2be551d85ccb0612acabd5ae1a8b983c7b0682ce397c437725eaceb1e8dd773e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT12gYOMHmfMeISpj5ibEGHxltIJSd9MIY6u8ORKtZZNG0oxfmTK2Iuo7rgYc7ujXmqVWYbygYAYkcg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650984694&idx=1&sn=7ba5d62b933542ac64cecc692e8fc282&chksm=807992c4b70e1bd2f0588c7c9f865cc4200bce4a37f718e61a4d8c85eaaf9bd84e6498ad191a&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GZ2mYNZYnqOD2pAicQctCmNHw5fre6QTGr4XJ0CJGqmEncGw9z0z7BYA/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650986722&idx=1&sn=683cdf211094018be422a0e4ef628522&chksm=80799ad0b70e13c6ae3b436f74551c84a1d3d93e1653e6610787182e935d2238b33c9c8ab14c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/3k9IT3oQhT3XlD8Odz1EaR5icjZWy3jb8ZZPdfjQiakDHOiclbpjhvaR2icn265LYMpu3CmR1GoX707tWhAVsMJrrQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

戳“阅读原文”更多精彩内容!

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3iahqCkYYjmw1gI9aGgwgAAqbmakWhGyibh4nQyU7npz3YyfZqosFKqfjdkRFRUwhmUwarcpQRrp0w/0?wx_fmt=png)

知道创宇404实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT3iahqCkYYjmw1gI9aGgwgAAqbmakWhGyibh4nQyU7npz3YyfZqosFKqfjdkRFRUwhmUwarcpQRrp0w/0?wx_fmt=png)

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