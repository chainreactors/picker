---
title: 【安全圈】广联智通（GL.iNet）路由器与KVM遭黑客批量入侵
url: https://mp.weixin.qq.com/s/SWWAtuglWcN15l1QZbje2g
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:39:44.653123
---

# 【安全圈】广联智通（GL.iNet）路由器与KVM遭黑客批量入侵

# 【安全圈】广联智通（GL.iNet）路由器与KVM遭黑客批量入侵

安全圈
安全圈

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

**核心事实**：国内物联网智能网关及远程管理设备提供商广联智通（GL.iNet）官方确认，其旗下多款智能路由器及远程 KVM 硬件遭到黑客在野批量利用。攻击者利用远程云管服务 GoodCloud 的授权缺陷及设备端后台命令注入漏洞，绕过常规鉴权向设备植入恶意程序并获取最高 root 控制权。第三方安全团队抽检发现，受管设备中有超过 83% 出现入侵痕迹，部分设备被常驻反弹 Shell。官方已紧急发布安全固件并通报修复。

广联智通硬件因采用 OpenWrt 底层、支持便携旅行组网、内置 WireGuard/OpenVPN 及提供低成本 IP-KVM 远程带外维护，在极客、跨国远程办公人员及小型企业机房中拥有广泛装机量。此次入侵直接针对连接至官方 GoodCloud 云管平台的设备，暴露出“云端管理接口+固件特权服务”复合利用链带来的严峻安全风险。

## 🔍 攻防还原：三层复合漏洞如何打穿底层系统

根据官方安全披露与安全研究团队 RemoteToHome 的逆向复盘，本次攻击由云管鉴权缺陷与设备端未过滤接口串联而成：

* **云端消息鉴权绕过（GoodCloud v3.19.13）**

  ：设备与云端之间依托 MQTT 消息队列（EMQX）维系管理长连接。因服务端鉴权机制存在逻辑缺陷，攻击者可向任意在线设备伪造下发配置指令或调用管理 API。广联智通已于 11 月 20 日紧急将云端服务升级至 v3.19.14 封锁利用链路。
* **AstroWarp/SD-WAN 接口命令注入（Root RCE）**

  ：设备端 GoodCloud 客户端以最高 root 权限处理下行消息，在调用内部 API 解析 `virtual_ip_info` 参数时缺少入参转义，直接导致命令注入。最危险的是：**即便用户从未开启过 AstroWarp 或 SD-WAN 组网功能，该监听组件也默认在后台常驻运行**，代码隐患最早可追溯至 2024 年 12 月发布的旧版固件。
* **RTTY 远程终端与 TLS 证书双重绕过**

  ：攻击者进一步通过改写本地 rtty 反向终端代理的启动参数，直接绕过设备预设的 TLS 证书校验，强制将交互式 Shell 指向攻击者控制的外部 C2 服务器。

## 💥 在野感染实测：199台抽检设备中166台遭入侵

安全团队 RemoteToHome 对其名下集中管理的 199 台广联智通路由器进行了全量取证测试，结果显示：

* **大面积失陷**

  ：高达 166 台设备命中攻击特征，其中 24 台设备已被部署了活跃的 root 权限反向交互 Shell。
* **后门进程隐匿伪装**

  ：在野捕获的核心入侵指标（IOC）为一个伪装的定时任务守护进程：

crond -i /tmp/.log

黑客通过欺骗系统调度程序，使其持续读取隐藏临时文件并维持反弹连接。官方在 11 月 23 日的最新补充通告中强调：**单纯检查是否存在该进程无法完全排除风险**。部分设备在植入木马或完成敏感凭证抓取后可能擦除了部分驻留特征，没有发现该进程并不代表设备处于安全状态。

## ⚠️ 严重次生危害：带外 KVM 设备恐连累物理内网

与普通路由器沦陷不同，广联智通的远程 KVM（如 GL-RM1、RM10 等硬件）属于工业与机房级带外管理设备。部分 KVM 出厂设置中即便尚未完成账号绑定，后台云端连接也是默认处于就绪状态。

当黑客掌握 KVM 的 root 权限后，威胁不仅停留在网关层面，更直接降维打击至被管理的物理主机：

* **监控屏幕与击键盗取**

  ：攻击者可调阅 HDMI/视频流并劫持 USB 虚拟键盘接口，嗅探管理员在物理机控制台输入的 BIOS 密码与系统登录凭据。
* **虚拟介质挂载投毒**

  ：利用 KVM 自带的 Virtual Media 功能，攻击者可远程向物理宿主机挂载恶意的 ISO 或镜像文件，从而实现内网跳板横向渗透。

## 🛠️ 应急响应指引：避开“升级却未清除”的致命盲区

广联智通已为全系主要型号发布了紧急安全固件（包括 GL-MT3000、GL-MT6000 的 4.11.1 版本，GL-BE3600 的 4.10.2 版本，GL-E5800 的 4.10.3 版本等）。受影响用户需立即采取以下四步规范处置：

**第一步：下载固件并坚决“取消保留设置”**
在设备管理页面手动上传对应型号的最新正式版安全固件。官方明确指出，刷入新固件时，**请务必取消勾选“保留当前设置”（Keep Settings）**。常规升级只能覆盖默认系统镜像，若黑客在配置目录（如 /etc/config、/etc/rc.local）中留存了持久化脚本，保留配置更新可能导致后门残留。重新配置系统是彻底消灭隐蔽驻留的最佳选择。

**第二步：全量强制轮换机密凭证**
固件升级只能阻止未来攻击，无法废止黑客此前已经下载的敏感数据。系统重置完成后，必须立即重置以下凭据：
1. 路由器 Web 控制台管理密码；
2. 托管在设备上的 SSH 访问公私钥；
3. WireGuard、OpenVPN 等内网穿透与组网客户端配置文件及私钥；
4. 动态域名解析（DDNS）服务商的 API Token 与第三方云同步密钥。

**第三步：排查 KVM 关联主机安全基线**
若受影响设备属于 KVM，除设备本身刷机外，应立即对 KVM 直连的目标物理机进行安全审计：检查系统是否有未知新增的影子管理员账号、排查异常外接 USB 介质挂载历史及系统最近异常重启事件。

**第四步：关闭非必要的远程云管开关**
若无需通过外网或官方云端随时随地监控设备状态，建议在系统控制面板中明确关闭“GoodCloud”远程管理功能，收敛公网攻击面，转用经过双因子验证的自建 VPN 隧道进行带外运维。

***END***

阅读推荐

[【安全圈】英伟达热修复驱动翻车：闲置9小时仍偷写36GB日志](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080032&idx=1&sn=763967cc27dfc41b9938316226fa2d69&scene=21#wechat_redirect)

[【安全圈】AI Agent自主挖掘零日漏洞：11分钟拿下医疗服务器](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080032&idx=2&sn=0979762f073753e029a45dc071f89129&scene=21#wechat_redirect)

[【安全圈】CISA紧急预警：VMware与Cisco等四枚高危遭在野利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080032&idx=3&sn=cd19a06b8fed5919a4de9fec4b756e3a&scene=21#wechat_redirect)

[【安全圈】单月1130起勒索，3.11亿条数据被挂牌](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080017&idx=1&sn=70d92ae03f620a7ace3b8888d687816a&scene=21#wechat_redirect)

[【安全圈】UAC被曝蠢到离谱的绕过，微软不分配CVE](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652080017&idx=2&sn=c4ef9c02feb49f867d9b5e707a06405a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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