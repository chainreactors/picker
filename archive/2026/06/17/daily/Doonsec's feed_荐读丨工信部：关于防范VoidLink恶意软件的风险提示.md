---
title: 荐读丨工信部：关于防范VoidLink恶意软件的风险提示
url: https://mp.weixin.qq.com/s/5S-SYP_GPoBxKC4Ujbo60w
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:47:47.095487
---

# 荐读丨工信部：关于防范VoidLink恶意软件的风险提示

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kdBgUloeCuibthLBjqdfuPWc1po2laRxllKyVO0xLcvPdHbJWYkQCIvuAshHJGVsAWdmxuYGicpU9D24NWmNBTTzEV8a6TExAErd6Kfrwkia5w/0?wx_fmt=jpeg)

# 荐读丨工信部：关于防范VoidLink恶意软件的风险提示

工业安全产业联盟平台

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

VoidLink恶意软件持续活跃，主要针对云环境中的Linux服务器发起攻击，可造成供应链攻击、服务器被控和业务中断等风险。

近期，工业和信息化部网络安全威胁和漏洞信息共享平台（CSTIS）监测发现，VoidLink恶意软件持续活跃，主要针对云环境中的Linux服务器发起攻击，可造成供应链攻击、服务器被控和业务中断等风险。

VoidLink是一个高度模块化的恶意软件，专为攻击云与容器环境设计，其样本于2025年底首次被发现。攻击者通过供应链污染、云环境配置漏洞及容器逃逸等手段植入具备环境感知能力的恶意加载器，利用未签名的容器镜像、泄露的凭证等配置弱点，实现隐蔽初始入侵。当VoidLink在受害Linux系统激活后，会收集主机详细信息，并通过LD\_PRELOAD、eBPF、LKM模块等内核级Rootkit技术隐藏自身进程、文件及网络活动，实现持久化驻留并规避常规检测。随后，VoidLink使用名为“VoidStream”的自定义协议连接其主控C2服务器，该协议支持HTTP/S、WebSocket、DNS、ICMP等多种隐蔽信道及P2P网状网络。借此，攻击者可以远程下发指令，实现对受感染系统的完全控制，进行数据窃取和横向移动等恶意操作。

建议相关单位及用户加强监测，及时修复系统、云组件及开发工具已知漏洞，防范开发工具链及容器镜像污染风险；部署带行为检测的终端安全工具，重点监控异常进程、隐蔽网络连接及未知内核模块加载行为；将相关威胁指标纳入监控体系，持续追踪分析异常网络流量与可疑云环境感知活动，有效识别并阻断此类高级威胁。

**相关IOC信息**

SHA256：

05eac3663d47a29da0d32f67e10d161f831138e10958dcd88b9dc97038948f69

13025f83ee515b299632d267f94b37c71115b22447a0425ac7baed4bf60b95cd

28c4a4df27f7ce8ced69476cc7923cf56625928a7b4530bc7b484eec67fe3943

4c4201cc1278da615bacf48deef461bf26c343f8cbb2d8596788b41829a39f3f

6850788b9c76042e0e29a318f65fceb574083ed3ec39a34bc64a1292f4586b41

70aa5b3516d331e9d1876f3b8994fc8c18e2b1b9f15096e6c790de8cdadb3fc9

7b75ce1d60d3c38d7eb63627e4d3a8c7e6a0f8f65c70d0b0cc4756aab98e9ab7

SHA1：

3355f84f97e06a74586fdb170d023ebc7545fa1a

5ffe44b04c0c47c83c1cd694b28c432fcde5867d

87158bda34066ce732da8b593746f5516aedbd66

9cdbc16912dcf188a0f0765ac21777b23b4b2bea

MD5：

17dd7ee893698205c715eeff87496b37

2c1d348131c4e3e1cb00002f226bad7e

4d8671ffc41252bc189b62699cb8cf90

bb1200ff20a257135e845c2388e46c90

**· end ·**

来源 | 网络安全威胁和漏洞信息共享平台

责任编辑 | 赫敏

声明：本文由工业安全产业联盟平台微信公众号（微信号：ICSISIA）转发，如有版权问题，请联系删除。

![](https://mmbiz.qpic.cn/mmbiz_png/4FpQm8QaW5kiaicHTUwSf9sId0er1ytR3D1Sc1RPfDpmk8FiciciadlBic9jSUbt1ciaE3G3aKiaicickE5ficq81KuYplgow/640?wx_fmt=png)

**如需合作或咨询，请联系工业安全产业联盟平台小秘书微信号：ICSISIA20140417**

**往期荐读**

# **重磅 | [《自动化博览》2026年第二期暨《工业控制系统信息安全专刊（第十二辑）》上线](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247538207&idx=1&sn=b6029b0c433c25c3fefb43e5213e8167&scene=21#wechat_redirect)**

# **征求意见稿丨**[网络安全技术 工业控制系统网络安全防护能力成熟度模型（附下载）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247534222&idx=1&sn=d68a32374971e527f09613e27be69e7e&scene=21#wechat_redirect)

# **工信部丨**[关于防范针对DeepSeek本地化部署实施网络攻击的风险提示](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247532396&idx=2&sn=60d0742822974a8d649ef771a671fcae&scene=21#wechat_redirect)

# **干货丨**[长输油气管网工控安全防护：策略、实践与展望](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247532389&idx=1&sn=3369308f4696e8b953678a13d59bfa71&scene=21#wechat_redirect)

**DeepSeek分析丨**[零信任安全架构在工业领域的发展现状与未来展望](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247532379&idx=1&sn=1603721f3f669d1fe6c5773b5fb55489&scene=21#wechat_redirect)

# **数字化安全丨**[工信部印发《高标准数字园区建设指南》（附全文+图解）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247536123&idx=1&sn=5f062ee2b518557bce3d117e14135ab9&scene=21#wechat_redirect)

# **AI安全丨**[人工智能安全治理框架2.0版（附下载）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247534922&idx=2&sn=2e8770ce10818f912137a9be36d4359e&scene=21#wechat_redirect)

# **干货丨**[工业可编程控制系统加密技术研究](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247531456&idx=1&sn=847458b642638a1a1a849e4bf4916407&scene=21#wechat_redirect)

# **荐读 |**[安全人视角的DeepSeek洞察与思考](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247531456&idx=2&sn=32075f2a360b824080569155dd6929de&scene=21#wechat_redirect)

# **可信数据丨**[中国城市可信数据空间行业研究报告（附全文）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247535945&idx=2&sn=748a35cd2b21d11be2183522b875fd73&scene=21#wechat_redirect)

# **关注丨**[网络关键设备安全检测结果（第19批）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247531380&idx=2&sn=f2148e66d4e29457b7af1e644e232161&scene=21#wechat_redirect)

# **数据安全｜**[国家标准支撑《网络数据安全管理条例》生效施行（v1.0）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247535879&idx=1&sn=d8bb3dd7a37bc6a7f8e157fdc1f5866d&scene=21#wechat_redirect)

# **工信部、国家标准委联合印发丨**[云计算综合标准化体系建设指南（2025版）](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247535167&idx=1&sn=f73612b1cd769b542520001fd9bb051b&scene=21#wechat_redirect)

# **国家标准丨**[数据安全国家标准体系（2025版），附下载](https://mp.weixin.qq.com/s?__biz=MzI2MDk2NDA0OA==&mid=2247534784&idx=1&sn=a6bba24ce93af1ad70d4372d9cd411e2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4FpQm8QaW5kl2a8G7lfZTXQ65jPLzCdpyKsyPqcbQnzEqbmYSDib90bZicWWGDc7kFPbaRiaVzC16MXUp4T0FY8cA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4FpQm8QaW5kl2a8G7lfZTXQ65jPLzCdpMs8tAvMDjxib9jwveZic6lrGG8K5iaoRIibBzbMEOZ1iay9MmF0aJtvicHmQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4FpQm8QaW5kl2a8G7lfZTXQ65jPLzCdpQrnsLdgPsjvdBHkvnibporOYKicPv4aBgHkEw0tLgNnDuOTOOAia2tPug/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4FpQm8QaW5kl2a8G7lfZTXQ65jPLzCdpgJgfShwDlZNGBxX5EkH8XMYawAfotAVmiaoD9icCOE7l306nqjCsuibCw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4FpQm8QaW5kl2a8G7lfZTXQ65jPLzCdp1IQNNBb9Hm4vRAiaKFBY2gMMDZB2IBvpkaCEetNoQvPFnwv2Tb13PuA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4FpQm8QaW5m076ZlbiboUbvLF6NlQdgP5sIgcKu4LiajXajBhNx9r9tkzBcU4snLHa9hUSZp0AO3Nicrz3FiaDp3ibw/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4FpQm8QaW5mEU31mWUSZmGicwwT1Uib60NRHysYs82ggViaSvTIFolS7YLNhzOrphBrAZfUweSeLUKsjib1bynaAqw/0?wx_fmt=png)

工业安全产业联盟平台

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4FpQm8QaW5mEU31mWUSZmGicwwT1Uib60NRHysYs82ggViaSvTIFolS7YLNhzOrphBrAZfUweSeLUKsjib1bynaAqw/0?wx_fmt=png)

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