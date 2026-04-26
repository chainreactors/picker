---
title: 全球SIM卡农场即服务网络曝光：17国87个控制面板浮出水面
url: https://mp.weixin.qq.com/s/ePnyAMU-VVLQ1hd8dZQLDw
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:56:46.076161
---

# 全球SIM卡农场即服务网络曝光：17国87个控制面板浮出水面

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0zkKfOcicRkR8xTSFmgcRho0jImcWia0FnhUelBxT7QHhrHKtUn5iaAqdrG2iaU7D46u96QAcWFBtsLXYknicsQEAsWgh8R0FIn2pc/0?wx_fmt=jpeg)

# 全球SIM卡农场即服务网络曝光：17国87个控制面板浮出水面

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0jDicRN4OmWQgpx9n5JSYOQVPNvWjiaZ4rdkUjM8yeYQQ12jcxBuRicL12vicELlL7hym2sGPjuk3d8frJk8ApToAs6NmFaVAxI6k/640?wx_fmt=jpeg&from=appmsg)

##

## 一项全球调查揭露了一个由名为ProxySmart的共享控制平台驱动的工业级移动代理生态系统。该网络横跨17个国家，暴露出87个控制面板，并关联至少94个实体手机农场站点，为商业规模的大规模欺诈、机器人活动及身份规避提供基础设施。

##

**Part01**

## ****SIM卡农场即服务网络架构****

2026年2月，基础设施情报公司Infrawatch对自称"SIM卡农场即服务"的供应商展开调查，发现其物理基础设施由成排的真实智能手机和直连运营商网络的4G/5G调制解调器构成。调查显示，一个位于白俄罗斯的ProxySmart软件平台作为共享控制平面，支撑着绝大多数已发现的农场设施。

Infrawatch在公开互联网上识别出87个暴露的ProxySmart控制面板实例，这些面板关联着全球至少24家商业代理供应商和35家移动运营商。其物理足迹覆盖北美、欧洲和南美至少94个农场站点，其中美国19个州尤为集中，从加利福尼亚、德州延伸至缅因州和特拉华州。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX10xWNbAq5Zhe6Fpt5Dck499pFQU71vfKRA6icLWVC9IX9JgrQdlptDMEyia7G507lGQQLGOKq4S8jFnmN8VcluqfRlKOygNaeJY/640?wx_fmt=jpeg&from=appmsg)

SIM卡农场（来源：Infrawatch）

**Part02**

## ****平台技术特性与规避手段****

ProxySmart作为即插即用的端到端解决方案，采用按SIM卡计费模式，提供设备管理、自动化IP轮换、客户配置、套餐执行及反机器人对策等全套功能。该平台同时支持物理智能手机和USB 4G/5G调制解调器，手机农场通过未签名的Android APK注册设备。

关键的是，ProxySmart包含操作系统指纹欺骗功能，允许运营商模拟macOS、iOS、Windows或Android的TCP/IP堆栈特征，有效规避反欺诈系统基于指纹的检测机制。平台还支持OpenVPN、SOCKS5、VLESS和HTTP代理等隧道协议，其中VLESS在俄罗斯、中国和伊朗常被用于规避审查。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2MLOxvBAeHD6nRab1esNrS8x5Zx9NbFGficZywMd5tNkXARymJ9DeqTb9tyxUgttAZOmP85ibDuN6UBqXXnSHLATogJ1MKAjWHY/640?wx_fmt=jpeg&from=appmsg)

SIM卡农场部署（来源：Infrawatch）

**Part03**

## ****运营商覆盖与犯罪应用****

通过ProxySmart接入的运营商网络包括AT&T、Verizon、T-Mobile、Vodafone、EE、O2、德国电信、Telstra、Rogers等全球30余家主要运营商。移动代理对威胁行为者的吸引力在于其部署在运营商级NAT（CGNAT）之后，单个IP可能被多个合法用户共享，使基于IP的封锁基本失效。

结合通过三秒切换飞行模式强制运营商重新分配IP的快速轮换技术，这些农场可随意更换地址，极大增加了检测和执法的难度。SIM卡农场支撑的非法活动包括：

* 通过短信验证码绕过实施账户接管与欺诈
* 虚假账户创建与社交媒体操纵
* 主流平台上的机器人活动与自动化交互
* 地理限制规避（包括绕过俄罗斯国家审查）
* 通过拦截金融验证码实施支付欺诈

**Part04**

## ****执法行动与全球影响****

调查发现部分ProxySmart供应商直接面向俄语用户推销美国移动网络接入服务，用于访问受地理限制的高级AI模型等平台。多数供应商缺乏有效的客户身份验证（KYC），部分甚至公开宣传零KYC要求，使得任何有支付手段的买家都能获得全球运营商接入。

Infrawatch的发现正值全球针对SIM卡农场基础设施展开系列执法行动。2025年9月，美国特勤局在纽约捣毁涉及300台SIM服务器和10万张SIM卡的电信威胁，其规模之大可能影响整个纽约市蜂窝网络。同年10月，欧洲刑警组织支持的拉脱维亚行动打击了依托SIM盒基础设施的网络犯罪即服务网络，逮捕7人并查获1200台SIM盒设备和4万张活跃SIM卡。

已确认的17个国家包括美国、加拿大、英国、德国、西班牙、葡萄牙、乌克兰、拉脱维亚、法国、罗马尼亚、巴西、爱尔兰、荷兰、澳大利亚、意大利、波兰和格鲁吉亚。美国部署密度最高，主要集中在4G/5G覆盖良好的大都市区。有案例显示，某运营商在发布的农场图片中意外暴露EXIF元数据，使调查人员得以定位到纽约的具体位置。

Infrawatch评估认为，该生态系统显著降低了运营移动代理基础设施的技术和操作门槛。结合运营商级NAT、快速IP轮换、多运营商接入和OS指纹欺骗等技术，传统以IP为中心的检测控制措施效果大打折扣，给全球平台完整性、欺诈预防和电信安全团队带来持续且可扩展的挑战。

**参考来源：**

Massive SIM Farm-as-a-Service Network Exposes 87 Control Panels Across 17 Countries

https://cybersecuritynews.com/sim-farm-as-a-service-network/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1NlibR8DpnkZguk1so3ThwkXScRIP7SKicZdaVeLa1eMHdfLgFsOaFCP6qt2JaDlnDPzLe5MJBV1micoP6YM0SG5C9X1ibsshUiccM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337140&idx=1&sn=134af642d92b85fc1076a8c83c09945c&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bKq2xLKwFuy1Yl63ibm7kJUCW7hP4uRIhllVu6icLPkYcerZIx5264cbnPu5uCLCpb0ic16Gm32GC3B6ou34yFia9Nm4YJTGU4iag/640?wx_fmt=png&from=appmsg)

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