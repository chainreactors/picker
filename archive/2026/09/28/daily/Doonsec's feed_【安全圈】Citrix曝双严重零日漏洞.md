---
title: 【安全圈】Citrix曝双严重零日漏洞
url: https://mp.weixin.qq.com/s/Kiw97NtqTjcjleTs_6jsvw
source: Doonsec's feed
date: 2026-09-28
fetch_date: 2026-09-29T07:39:40.193394
---

# 【安全圈】Citrix曝双严重零日漏洞

# 【安全圈】Citrix曝双严重零日漏洞

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

**核心要点：**美国网络安全与基础设施安全局（CISA）于 9 月 27 日将 Citrix NetScaler ADC 与 Gateway 的两个严重远程代码执行（RCE）零日漏洞列入已知被利用漏洞目录（KEV），正式确认黑客正针对全球企业边界设备发起大规模在途攻击。两个漏洞评分均高达 CVSS 9.5，攻击者无需任何前置账号认证即可拿下系统权限。CISA 已签发指令，要求美国联邦民事行政机构必须在 9 月 30 日（周三）前全部完成加固升级。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHob1GwmnuMiafewrTcPT7kQOuK1vohv9bjcmN9b2Ps53wTRiafIj9NgicXIqtbtg4JEwcWvX8y9pKuBueUQL4VlssS01RJWAD4ibQ/640?wx_fmt=other&from=appmsg)

## 🚨 边界设备再次沦陷：双 9.5 分 RCE 漏洞机理拆解

Citrix NetScaler ADC 与 NetScaler Gateway 作为全球大型企业部署在网络边缘的核心负载均衡与 VPN 接入网关，历来是 APT 组织与勒索团伙撕裂内网的最高价值目标。

安全机构 watchTowr 率先披露两枚 0day 已被用于定向实战渗透，随后部分系统管理员因无法立刻打补丁而选择紧急将网关设备物理断网拔线。Citrix 随后证实了漏洞的存在并公布对应标识：

* **CVE-2026-88771（CVSS v4: 9.5）：**

  输入验证缺陷（Improper Input Validation）。未经身份认证的攻击者可发送特制数据包执行任意底层系统命令。**该漏洞影响目标版本下的所有部署场景，哪怕设备运行在纯开箱默认配置下亦无法幸免**。
* **CVE-2026-88772（CVSS v4: 9.5）：**

  内存缓冲区边界限制缺陷（Buffer Overflow）。当网关启用了 DTLS（数据报传输层安全协议）时可被触发，导致远程代码执行（RCE）或整机服务拒绝（DoS）。而在绝大多数生产环境的 VPN 虚拟服务中，DTLS 处于默认开启状态。

```
# CVE-2026-88772 典型受影响配置特征（VPN 虚拟服务默认开启 DTLS）: add vpn vserver vpn1 SSL 10.0.0.0 443 -Listenpolicy NONE # 检查状态: 若绑定了 DTLS 监听且对外暴露，即进入高危可利用面
```

## 🔍 攻击路径复盘：未认证流量如何穿透系统权限

在真实受害案例中，攻击者通常将 NetScaler 设备作为进入企业内网的跳板：

```
[阶段1: 暴露面探测] 扫描目标 443 / DTLS 端口，识别 NetScaler 固件版本指纹 [阶段2: 绕过鉴权请求] 发送畸形输入参数/超长报文，绕过预认证过滤链 [阶段3: 内存覆写/指令注入] 触发 CVE-2026-88771 或 CVE-2026-88772 取得 Shell 权限 [阶段4: 凭据收割] 导出网关内存中残留的活动会话 Cookie、企业域凭据与证书 [阶段5: 内部横向展开] 依托网关作为中继跳板，向内网域控与核心集群推进
```

## 🛡️ 官方修复版本清单与紧急排障指南

Citrix 官方已于安全通报 CTX697096 中发布安全补丁，以下固件版本已包含对该两处零日漏洞的完整修复：

* **Citrix NetScaler ADC / Gateway 14.1：**

  升至 `14.1-73.37` 及更高版本；
* **Citrix NetScaler ADC / Gateway 13.1：**

  升至 `13.1-64.23` 及更高版本；
* **FIPS 硬件加密版：**`14.1-73.37 FIPS`

  及 `13.1.37.279 FIPS/NDcPP`。

## ⚙️ 疑似失陷环境的应急处置六步法

由于漏洞已被在途武器化利用，Citrix 强烈建议凡是对外暴露网关的企业安全团队，在升级固件前后严格执行以下取证与排查步骤：

1. **保全现场证据：**

   为受影响的 NetScaler ADC VPX 虚拟机实例制作全量内存与磁盘镜像快照；
2. **断网隔离：**

   将涉事设备从生产网络中隔离，暂停外网 DNS 解析与路由指向；
3. **全面撤销凭证：**

   吊销设备管理账户凭据，强制注销所有在线用户的活动会话会话令牌；
4. **横向审计内网：**

   全面排查网关下游所连接的 LDAP/AD 域控、Web 应用集群与数据库访问日志，确认黑客是否已借助网关向内渗透；
5. **重构与版本更新：**

   重新安装最新已修复固件版本，禁止从未经安全审计的配置备份中直接无损还原；
6. **轮换密钥系统：**

   更新所有本地账户密码、密钥加密密钥（KEK），并重新签署或替换所有 SSL/TLS 证书。

***END***

阅读推荐

[【安全圈】OpenAI 研究代理曾将用户图片传到第三方图床，已发现 53 次](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079129&idx=1&sn=7df0283a6c5d51694b17203ac0b35c59&scene=21#wechat_redirect)

[【安全圈】两个恶意 GitHub Actions 曾重新上线，旧工作流需排查](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079129&idx=2&sn=df0e0e05d2843681315bf1ebf88e985d&scene=21#wechat_redirect)

[【安全圈】SharePoint 代码注入漏洞出现实际攻击，已发布补丁仍需核对](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079129&idx=3&sn=8eab1210d63abf0b373ad59028f7c1ad&scene=21#wechat_redirect)

[【安全圈】暴露的 Docker 接口成攻击入口，Carbonato 借 AI 代理控制主机](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079118&idx=1&sn=c15dc9fe4166f047f1ddffafc639e2e0&scene=21#wechat_redirect)

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
在看
，轻点两下取消在看
分享
留言
收藏
听过