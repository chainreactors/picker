---
title: 首个区块链C2僵尸网络Aeternum问世，传统查封手段彻底失效
url: https://mp.weixin.qq.com/s/n-j_x-qbWaVp_VRU2wZo5g
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:16:37.523121
---

# 首个区块链C2僵尸网络Aeternum问世，传统查封手段彻底失效

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3KTibagTNQEmS5icX3Rmp01f1H1SftXibu3NSW6HLpC1YictjVkWg0TW6eETk2hQNMcFXAbzqCjEBLPQKzTfuj2YibbjHY4vp34jmg/0?wx_fmt=jpeg)

# 首个区块链C2僵尸网络Aeternum问世，传统查封手段彻底失效

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3lnKEJG9p4H68Er21DyeRIiaXavoloRWehd0ISDEiciceGvUcFUebCV8pKOJIib3CkuwZdLKTFsQ2jibodk9shfLsDIe5YTqtAE7U0/640?wx_fmt=png&from=appmsg)

##

多年来，捣毁一个僵尸网络通常意味着找到它的命令与控制（C2）服务器、查封域名，然后看着这个网络彻底瘫痪。执法部门曾用这种方法成功摧毁了Emotet、TrickBot和QakBot等大型犯罪团伙。

然而，新发现的名为Aeternum C2的僵尸网络加载器，专门设计用来堵住这道防御之门——它所有的指令都不存储在服务器或域名上，而是直接记录在Polygon区块链中。Polygon是一条公共区块链，在全球数千个节点上同步复制，确保数据永不丢失。

由于没有单一的服务器可以查封，也没有域名可以暂停，无论任何权威机构或平台采取什么行动，这套基础设施都能持续运作。对于那些多年来依靠查封基础设施来瓦解僵尸网络的安全防御者来说，现在面临一个让传统策略完全失效的新模型。Aeternum似乎是首个将基于区块链的C2打造成即用型产品的商业化实现。

Qrator Labs的分析师在监控网络犯罪活动时发现了这个加载器。他们注意到，该加载器采用原生C++编写，并提供32位和64位两种版本。

##

**Part01**

## ****区块链C2架构：****

## ****运行原理与规避机制****

研究人员发现，发送给受感染设备的每条命令都作为交易记录在Polygon区块链上，僵尸程序通过公共远程过程调用（RPC）端点读取这些命令。根据卖家文档，所有活跃僵尸程序能在两到三分钟内接收更新——比传统点对点僵尸网络更快、更稳定。

该僵尸网络在地下论坛以两种形式销售：包含预配置构建的终身许可证，或提供持续更新的完整C++源代码。运行成本极低：仅需价值约q的MATIC（Polygon原生代币）即可支持100到150次命令交易。由于无需租用服务器或注册域名，维护弹性僵尸网络的运营成本几乎为零，使得更多威胁行为者能够轻易获取。

基于此模型的僵尸网络潜在危害远超单个攻击活动。一旦部署，它们可以不受干扰地扩张，用于大规模DDoS攻击、凭据填充、点击欺诈、代理即服务滥用和数据窃取。即使彻底清理受感染设备，攻击者的智能合约仍完好无损，意味着随时可以完整重新部署而无需重建基础设施。

**Part02**

## ****操作流程与反检测机制****

攻击者通过基于网页的控制面板管理一切。从这个界面中，攻击者选择智能合约、指定命令类型——无论是针对所有僵尸程序、按硬件ID（HWID）ping特定设备，还是推送DLL加载程序——然后提供有效载荷URL并将更新发布到区块链。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2vUtaJX1UVpYjtzWZ8IicIUvIo7swJuibH1xtMsTaznSN8SS9ibPxpek6IWuSqZWiaEbwwaTcOr79yXkSGtQ14lNexxoyibJzN1I9w/640?wx_fmt=jpeg&from=appmsg)

链上确认后，除钱包所有者外无人能修改或删除命令。攻击者可同时运行多个合约，每个合约对应不同功能，如剪贴板窃取器、信息窃取器、远程访问工具（RAT）或挖矿程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1xdBe64ibEJ9IkvBiaTwicPxVJCc7GI7agcJNGEkdBH7Q55NAPMGj1xdHbANrwlevk72icsnicHE4bZP1VsgrTZRWnflGQOZjq3tn4/640?wx_fmt=jpeg&from=appmsg)

Aeternum还包含反虚拟机检测功能，会阻止在杀毒厂商和恶意软件分析师常用的虚拟化环境中执行。卖家捆绑了由Kleenscan API驱动的扫描时检测器。测试显示，37个检测引擎中只有12个标记了样本，而CrowdStrike、Avast、Avira和ClamAV在测试时均返回清洁结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3hBs0apQVAy0WdkaxEUQ5QXsTeDs4veiar21npkPYxtsIyqLgMjhg2uSDLicVOaMMY5LNEhSt3MmhPqNq8ewiaiaiaZHKfKuMsY4I4/640?wx_fmt=jpeg&from=appmsg)

**Part03**

## ****防御策略转型****

传统的域名查封和服务器关停无法阻止基于区块链的C2通道。安全团队应聚焦终端检测、行为监控和严格的应用程序控制，及早发现可疑可执行文件。网络防御者应评估是否能在不影响合法操作的情况下，监控或限制对已知Polygon RPC端点的出站连接。

由于基础设施层面的关停对此模型不再有效，在网络边缘实施主动流量过滤仍是最可靠的防御手段。

**参考来源：**

Researchers Uncover Aeternum C2 Infrastructure with Advanced Persistence and Network Evasion Features

https://cybersecuritynews.com/researchers-uncover-aeternum-c2-infrastructure/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3tSDVhn4H8MfzIKxtt4We0D52fia93Y5a2TI7y0t4j0PpiclCRBqdQCZWYrwG4B4hpaT2593sVoic8GylJKxPrgP1gyC1304Y78I/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX16d9YFd8C2ZLm5AxSaONt9eF8xcnfW9nhy3jyhoyrY28GWAnNeXJ0ojss2bj9w5V2asdI31nwVv2SUldtdhLfWuCE2l8fCzT8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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