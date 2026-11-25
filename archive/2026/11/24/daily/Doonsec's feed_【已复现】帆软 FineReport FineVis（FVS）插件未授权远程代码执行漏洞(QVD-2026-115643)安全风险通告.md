---
title: 【已复现】帆软 FineReport FineVis（FVS）插件未授权远程代码执行漏洞(QVD-2026-115643)安全风险通告
url: https://mp.weixin.qq.com/s/4DXlPVgT6C-jXpjSI8HGUQ
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:44:34.203715
---

# 【已复现】帆软 FineReport FineVis（FVS）插件未授权远程代码执行漏洞(QVD-2026-115643)安全风险通告

# 【已复现】帆软 FineReport FineVis（FVS）插件未授权远程代码执行漏洞(QVD-2026-115643)安全风险通告

奇安信 CERT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

● 点击↑蓝字关注我们，获取更多安全风险通告

---

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞概述** | | | |
| **漏洞名称** | 帆软 FineReport FineVis（FVS）插件未授权远程代码执行漏洞 | | |
| **漏洞编号** | QVD-2026-115643 | | |
| ****公开时间**** | 2026-11-21 | ****使用量级**** | 万级 |
| **奇安信评级** | **高危** | **CVSS 3.1分数** | **9.8** |
| **威胁类型** | 代码执行 | **利用可能性** | ****高**** |
| **POC状态** | **未公开** | **在野利用状态** | 未发现 |
| **EXP状态** | **未公开** | **技术细节状态** | **未公开** |
| **危害描述：**攻击者可利用空模板路径绕过登录校验，未授权上传并应用恶意 FVS 复用包，向 WEB-INF 写入可执行内容，以应用进程权限执行任意系统命令，可能导致服务器被完全控制、报表业务数据与数据库连接凭据泄露，并可作为跳板进一步渗透内网。 | | | |

**0****1**

**漏洞详情**

**>****>****>****>**

**影响组件**

帆软 FineReport 是企业级报表与数据决策平台，FineVis（FVS）是其可视化大屏插件，支持复用包（.mfvs，用于打包模板及其依赖资源）的在线导入与应用，常用于经营分析、指挥调度与数据看板，在金融、制造、政企等行业的报表系统中部署广泛。

**>****>****>****>**

**漏洞描述**

近日，奇安信CERT监测到官方修复帆软 FineReport FineVis（FVS）插件未授权远程代码执行漏洞(QVD-2026-115643)，该漏洞源于 FVS 插件复用包导入与应用接口的模板鉴权缺陷：当请求携带的模板路径被归一化为空值时，相关请求被判定为“无需登录的模板访问”，从而绕过登录状态校验；攻击者无需任何账号或凭据，即可上传并应用构造的 .mfvs 复用包。在复用包应用阶段，导入组件未对附件写入位置实施业务白名单限制，可向应用 WEB-INF 目录写入可执行内容，容器检测到配置或类文件变更后重载，最终以应用进程权限执行任意系统命令。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**>****>****>****>**

**利用条件**

目标启用 FineVis（FVS）插件且服务网络可达，无需任何凭据。

**02**

**影响范围**

**>****>****>****>**

**影响版本**

FineReport < 11.5.16

FineVis（FVS）插件 < 4.15.0

**03**

**复现情况**

目前，奇安信CERT已成功复现帆软 FineReport FineVis（FVS）插件未授权远程代码执行漏洞(QVD-2026-115643)，截图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/RwAbCjh555sVS9VpCAKaoHU2iaekXO2nnvRboAC1yWt9eficFSCZtHKW7YjiaOaRsDUkBLu4cxLC8kkCMseKyIanbQediaNO7PqlUrwb8AsXLNQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RwAbCjh555tHyicibFCCg95kJ7PgVSeUSMuAicOxzETwex4AAYmhQdSVqbP58zYR76P8IJiaK18CicxVtWEIrwohDKPia0j8DNYQCpY3q0yHs9KC0/640?wx_fmt=png&from=appmsg)

**04**

**受影响资产情况**

奇安信鹰图资产测绘平台数据显示，帆软 FineReport FineVis（FVS）插件未授权远程代码执行漏洞(QVD-2026-115643)关联的国内风险资产总数为26701个，关联IP总数为1152个。国内风险资产分布情况如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RwAbCjh555uiasPSxbicmkLLIiaO47U11qcHQH7YfhSrcMMrPJsCyaTOwXiaN1TELtLeMA4Y0lwh0wGmP8g8YA0y5SHrGZ66Y1jvbBZic6cWSF6A/640?wx_fmt=png&from=appmsg)

**05**

**处置建议**

**>****>****>****>**

**安全更新**

官方已发布安全补丁，请及时更新至最新版本：

FineReport >= 11.5.16

FineVis（FVS）插件 >= 4.15.0

升级步骤可参考官方产品安全加固指导手册：

https://help.fanruan.com/finereport/doc-view-4658.html

升级前建议与帆软技术支持确认版本适配关系，并在测试环境完成兼容性验证后再实施生产升级。

临时缓解措施：

无法立即升级时，可采取以下应急措施。相关措施均可能影响业务功能，升级完成后应及时移除：

1、通过反向代理、防火墙或 WAF 限制报表服务的访问来源，仅放行可信网络与必要运维地址；

2、对复用包导入、应用类请求（/decision/view/duchamp/reuse/item、/decision/view/duchamp/reuse/apply/\*）实施拦截或额外的身份校验，并评估其对资源迁移等正常业务的影响；

3、不具备上述条件的实例，建议临时停止外网暴露，仅保留内网受控访问；

4、排查 WEB-INF 目录下的异常类文件、配置文件与日志文件，以及 webroot 下的异常回显文件。

**>****>****>****>**

**产品解决方案**

**奇**安信网神网络数据传感器系统产品检测方案****

奇安信网神网络数据传感器（NDS5000/7000/9000系列）产品，已具备该漏洞的检测能力。规则ID为：8533，建议用户尽快升级检测规则库至2611241530或以上。

**奇安信天眼检测方案**

奇安信天眼新一代安全感知系统已经能够有效检测针对该漏洞的攻击，请将规则版本升级到3.0.1124.15190或以上版本。规则ID及规则名称：

0x10022B2F，帆软 FineReport FineVis（FVS）代码执行漏洞(QVD-2026-115643)。奇安信天眼流量探针规则升级方法：系统配置->设备升级->规则升级，选择“网络升级”或“本地升级”。

**奇安信自动化渗透测试系统检测方案**

奇安信自动化渗透测试系统已经能够有效检测针对该漏洞的攻击，请将插件版本和指纹版本升级到202611252329以上版本。规则名称：帆软 FineReport FineVis（FVS）插件未授权远程代码执行漏洞(QVD-2026-115643)。奇安信自动化渗透测试系统规则升级方法：系统管理->升级管理->插件升级（指纹升级），选择“网络升级”或“本地升级”。

**奇安信网站应用安全云防护系统已更新防护特征库**

奇安信网神网站应用安全云防护系统已全局更新所有云端防护节点的防护规则，支持对帆软 FineReport FineVis（FVS）插件未授权远程代码执行漏洞(QVD-2026-115643)的防护。

**06**

**参考资料**

[1]https://www.fanruan.com/

[2]https://help.fanruan.com/finereport/doc-view-4658.html

**07**

**时间线**

2026年11月24日，奇安信 CERT发布安全风险通告。

**08**

**漏洞情报服务**

「奇安信漏洞情报平台」重磅上线，诚邀您来体验：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555uRiaqiccGzEc3LcLP7Pd0MNpPm6WUz0UoibuNibCa3TL4Mqic4FZspBgHx8Fw8YkiaZdMicZtD3XS248cMD2ibKwWDeicprVLB1wzEDND0/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_png/3tG2LbK7WG3tezJEzJsicLSWCGsIggLbcfk4LB5WK7pdSwMksxPOAoHuibjQpBlEId4nyIIw52n2J8N8MowYZcjA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=3)

![图片](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibpFEkqfMZfO3smS6RKd9BYBVaibvBq1vXprZIc191LXKibdiaApA16q3UgmibQDv4yW09qT88J3jRUfA/640?wxfrom=5&wx_lazy=1&wx_co=1&wx_fmt=other&tp=webp#imgIndex=4 "CERT LOGO.png")

**奇安信 CERT**

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

本文已发布于NCC国家网络安全云社区https://nccsec.cn/security-community

点击↓**阅读原文**，到**ALPHA威胁分析平台**订阅更多漏洞信息。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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