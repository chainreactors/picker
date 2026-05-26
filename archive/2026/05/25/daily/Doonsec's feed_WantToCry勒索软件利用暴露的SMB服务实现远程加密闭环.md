---
title: WantToCry勒索软件利用暴露的SMB服务实现远程加密闭环
url: https://mp.weixin.qq.com/s/Do60cVJOlYuUZhsx3_yESg
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T05:59:24.438999
---

# WantToCry勒索软件利用暴露的SMB服务实现远程加密闭环

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3qz4LJC7nhDlbayicEONTHiaJVJIRMseosEUKWQzkglYbIlCBW4o3vCYfMIcgQKcOKyEF5aSUkY9nZOjHboUBn5snJ65Ricmr0UQ/0?wx_fmt=jpeg)

# WantToCry勒索软件利用暴露的SMB服务实现远程加密闭环

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX0UFTEiabibUz504OOhYx1AaR6aoicN6GusicefL2p1YY9wdCm0mTWdt5dEicz6NITAdlXYQstTTU4TfFGhiaYC36PwCJ9dnSzAicWOnE/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0MiaTq3d299yCESPXfe4Xiaicztqy55XeAcia8fEILQj56pNgP4NbllRKibef3gP26q3Me4QNYEbLicYlDU4vFgZDRqyZGFtPdibibIJs/640?wx_fmt=png&from=appmsg)

最新分析的勒索软件攻击活动彻底颠覆了传统终端防御策略——其整个加密过程无需在本地执行任何恶意代码。Sophos反威胁研究团队深入调查发现，WantToCry对传统终端检测与响应（EDR）平台构成了独特挑战：攻击者利用暴露在互联网的服务器消息块（SMB）文件共享服务，远程静默提取、加密并覆盖目标网络数据。

![2](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2Hk50Qqia33mmqTLUofS7QNywVfY7s1FRXiaZ0vZ3hH93Ba4Ticzjm66AIpVHTibrjlfhDrRIfRUYyTGqTxL3DX4ynbMNibLJ3UFak/640?wx_fmt=png)

Part01

无本地执行的攻击范式

Sophos反威胁研究团队在核心情报简报中强调：

"由于WantToCry无需本地恶意软件执行即可运作，且除窃取文件并重写磁盘外无其他入侵后活动，其检测面大幅缩小。"

攻击者刻意选用这个名称，意在影射2017年肆虐全球网络的WannaCry勒索蠕虫。但Sophos分析师指出，两者的运作基础截然不同——旧版利用核心代码漏洞实现自我传播，而WantToCry完全依赖扫描和认证暴力破解开辟入侵路径。

Part02

三阶段攻击闭环

攻击流程绕过了典型的入侵后网络定位，形成从初始访问到数据加密的紧密闭环：

侦查阶段：通过大规模互联网扫描基础设施，探测开放SMB端口TCP/139和TCP/445的主机

暴力破解：自动化脚本持续攻击暴露端口，测试默认或弱密码直至获取有效凭证

远程置换：认证成功后，攻击者控制远程服务器接管SMB会话，系统性发起文件读取请求，在其本地硬件加密后，再通过写入命令将密文回传至受害者存储设备

由于未执行非常规二进制文件、未修改注册表且无异常系统进程，本地反恶意软件工具对网络文件共享中的破坏活动完全无感知。

Part03

基础设施溯源

Sophos追踪到攻击活动涉及德国、俄罗斯、美国和新加坡的五个全球分布式IP地址。取证分析发现两个反复出现的计算机名（WIN-J9D866ESIJ2和WIN-LIVFRVQFMKO）驱动着自动化文件写入操作，这些虚拟机最初由正规IT基础设施提供商ISPsystem出租，后被恶意防弹托管中介转租。

Part04

异常低廉的赎金

完成文件置换后，恶意软件会留下赎金票据，指示受害者通过临时qTox或Telegram通道获取比特币钱包信息。值得注意的是，赎金金额异常低廉——每起事件固定索要600美元。Sophos指出，这与动辄数百万美元的企业勒索形成鲜明对比，直接反映出"勒索软件部署范围的局限性"，因为加密通常仅针对直接暴露SMB服务的单一设备。

参考来源：

WantToCry Ransomware Leverages Exposed SMB for Remote Encryption Loops

https://securityonline.info/wanttocry-remote-ransomware-smb-brute-force-no-local-code/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1SRP5DY7WibSicW4eWTtYzFWDTfVGMqCQ4UicdvaeHbSfA0ReLjXu6why8RH43kXBsNQ39qgiaxrmAsN9kbEnVENaHKmtQZib2otm8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651338613&idx=1&sn=d0ae0c38319293b058cc4ff73b9319ae&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2SyOCpMWiaRGCVOcBia89UPEschd9VicMFd7SM1rhpC18v24yZmRTYBC8tEqUDDS3qdYSfbjKdJickyhKGibU8gBkvBNA4wk6YmXR4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3mb4znpvVn7Tanmxv7xsbAiaAv5eR18aaDCHkP1PGOckEBsB57dAr9KGgiczeLWoZplmLgF6wicnGQGVafcl4VOoCxWcRakleZ3c/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3fDkAWr1kS65Mic6sY2ibrnv8XPk4ISwiaRAQ3RIe5hTstpVFiaF6grRuMQPUaAskict7GRaIvOMdL1MiaGXYic0TxicqibathIZ6YKNpQ/640?wx_fmt=png)

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