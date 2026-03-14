---
title: 再发预警！事关OpenClaw“养龙虾”安全风险
url: https://mp.weixin.qq.com/s/g7ZOVuLhf9D4u3L1ZRyXyA
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:06:26.005114
---

# 再发预警！事关OpenClaw“养龙虾”安全风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LJwWAbW20ChzIlWq95iaEG2eOpFdnDiadWkfXzLbABaO0EEh57qEnoymmv1IdWluribkiamMupKUPazic5545KwRBJdoUBekPlt9AcEpgGcMad1U/0?wx_fmt=jpeg)

# 再发预警！事关OpenClaw“养龙虾”安全风险

中国信息安全

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_gif/LJwWAbW20ChOhrO8sO0HcgPW3eCRfFBdMTgmvTTQFpq0jtS1dfVyIbkgXxYssxdw9pibCa9q15iciaomMVuXVxnk22YK1rtjS2JmM48XHNWZ3Y/640?wx_fmt=gif&from=appmsg)](https://cisat.cn/all/14915419?from_tag=1)

OpenClaw自发布以来，凭借其强大的自动化任务处理能力与开放式插件生态，在全球范围内引发部署热潮。国家网络与信息安全信息通报中心监测数据显示，目前全球活跃的OpenClaw互联网资产已超20万个，其中境内活跃的OpenClaw互联网资产约2.3万个，呈现爆发式增长态势，主要集中在北京、上海、广东、浙江、四川、江苏等互联网资源密集区域。大量暴露于互联网的OpenClaw资产存在重大安全风险，极易成为网络攻击的重点目标。

一、OpenClaw主要安全风险

OpenClaw在架构设计、默认配置、漏洞管理、插件生态、行为管控等方面存在较大安全风险，一旦被攻击者利用，可能导致服务器被控制、敏感数据泄露等严重安全问题。

1、架构设计缺陷多，层层皆可破。OpenClaw采用多层架构，但是每层均存在设计缺陷。IM集成网关层可被攻击者伪造消息绕过身份认证，智能体层可被多轮对话修改AI智能体行为模式，执行层与操作系统直接交互存在被完全控制风险，产品生态层遭投毒的恶意技能插件可批量感染用户设备。

2、默认配置风险高，公网暴露广。OpenClaw默认绑定0.0.0.0:18789地址并允许所有外部IP地址访问，远程访问无需账号认证，API密钥和聊天记录等敏感信息明文存储，公网暴露比例高达85%。

3、高危漏洞数量多，利用难度低。OpenClaw历史披露漏洞多达258个，其中近期暴露的82个漏洞中，超危漏洞12个、高危漏洞21个、中危漏洞47个、低危漏洞2个，以命令和代码注入、路径遍历和访问控制漏洞类型为主，利用难度普遍较低。

4、供应链投毒比例高，生态不安全。针对ClawHub的3016个技能插件分析发现，336个插件包含恶意代码，占比高达10.8%。17.7%的ClawHub技能插件会获取不可信第三方内容，成为间接引入安全隐患的载体。2.9%的ClawHub 技能插件会在运行时从外部端点动态获取执行内容，攻击者可远程修改AI智能体执行逻辑。

5、智能体行为不可控，管控难度大。OpenClaw智能体在执行指令过程中易发生权限失控现象，导致越权执行任务并无视用户指令，可能会出现删除用户数据、盗取用户信息、接管用户终端设备等情况，造成重大经济损失。

二、OpenClaw风险防范建议

1、及时升级版本。通过可信来源获取安装程序，关注官方安全公告，及时更新至最新版本，及时修复已披露安全漏洞。

2、优化默认配置。仅在本地或内网地址运行，避免绑定公网地址或开放不必要端口，如使用反向代理，需配置身份认证、IP白名单和HTTPS加密。

3、谨慎安装第三方插件。通过官方渠道获取第三方技能插件，避免安装来源不明的扩展程序。对已安装插件进行功能审查，发现可疑行为立即卸载。

4、加强账户认证管理。启用身份认证机制，设置高强度密码并定期更换，避免使用弱口令。

5、限制智能体执行权限。对AI智能体的操作能力进行必要限制，仅允许执行白名单中的系统命令和操作权限，防止AI智能体被恶意指令利用后对个人终端设备造成实质性破坏。

（来源：国家网络安全通报中心）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LJwWAbW20CjauiaQEcdBr1THD0oeQicYZKaT1MUmOoRibicxklQ98OMQwMNGL44An2lBEoibzqr6Y2gvRKWpuSVdPeIn3QtmflEBmDic1ib0C69AsI/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/LJwWAbW20CjCmAhdiczQ05Uiayj6ZundjbnF9P0jaBWaYuXIvjic2f5x33kgArwp83HunhsuG27dmZibKTWiaP8CcJxYWia5bWW0RNzy77CPvaNQ0/640?wx_fmt=png&from=appmsg)](https://cisat.cn/)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

中国信息安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

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