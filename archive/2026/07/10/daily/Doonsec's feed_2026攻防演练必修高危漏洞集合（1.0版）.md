---
title: 2026攻防演练必修高危漏洞集合（1.0版）
url: https://mp.weixin.qq.com/s/uirqC0lz2lQDIYiLHAjz8Q
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:02:21.756270
---

# 2026攻防演练必修高危漏洞集合（1.0版）

![cover_image](http://mmecoa.qpic.cn/sz_mmecoa_jpg/jpCFCFfaGRHibzYiajiaWaygufOqwnvz1pnZUwauF0GcWgcne38ibMtPQJ2NfCPJO8mZzz4fZkibtGTR8CqNzpTlIoSwBg0Ut2nBfCdwsUI6SvbA/0?wx_fmt=jpeg)

# 2026攻防演练必修高危漏洞集合（1.0版）

斗象科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

高危风险漏洞一直是企业网络安全防护体系中的薄弱环节，更是HW攻防演练期间红队实现突破的关键切入点。每逢HW期间，大量高危漏洞被红队作为突破口集中利用，成为撕开企业网络边界防线的利器。不少企业正是由于未能及时修复此类漏洞，导致整体防御体系被轻易击穿，甚至靶标失守，最终遗憾出局。

2026HW攻防演练在即，斗象XVI扩展漏洞情报深度整合了漏洞盒子的实时海量数据、白帽社区的一手情报以及FreeBuf安全门户的安全资讯，发布《2026HW必修高危漏洞集合（1.0版）》。旨在协助企业在HW攻防演练前期开展精准的风险自查，最大程度消除已知高危隐患，加固网络边界防线。

![](https://mmecoa.qpic.cn/sz_mmecoa_jpg/TianBfDibsTJE62OPeQYadYt1gMuxHhteU2ZbkHp8kz7JvZqKGicrucvE6icS3El8ibmc6RvuzZ0tPARiaq16wgKndiaCfFXJgJH59picV8fjRk28fs/640?wx_fmt=jpeg)

本期报告整理收录了2025年10月至2026年6月在攻防演练中被红队利用最频繁且对企业危害较高的漏洞，包含了详细的漏洞基础信息、检测规则和修复方案，企业可根据自身资产信息进行针对性的排查、配置封堵策略和漏洞修复相关工作。

**1**

**漏洞数据汇总**

以下数据针对2025年10月至2026年6月期间，攻防演练中红队利用率较高的漏洞进行系统梳理，具体汇总如下：

* **远程代码执行**

漏洞数量：13个

涉及厂商：Oracle、Apache ActiveMQ、Veeam、Microsoft、React、Fortra、HPE、Samba、Ivanti、Fortinet、Apache Tomcat、Kubernetes、泛微

* **认证/授权绕过**

漏洞数量：3 个

涉及厂商：Check Point、Palo Alto Networks、Next.js

* **SQL 注入漏洞**

漏洞数量：3 个

涉及厂商：Drupal、用友时空、孚盟云

* **内存破坏/RCE风险**

漏洞数量：2 个

涉及厂商：7-Zip、Google

* **其他**

漏洞数量：13

漏洞类型：命令注入/提权、反序列化、路径遍历/文件读取、反序列化绕过、本地提权、访问控制错误、任意文件下载

涉及厂商：Cisco、用友、XWiki、Apache、Linux Kernel、通达OA

**2**

**本次高危漏洞自查列表**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **漏洞编号** | **类型** | **资产类别** |
| Check Point Remote Access VPN 认证绕过漏洞 | CVE-2026-50751 | 认证绕过 | 边界设备/VPN |
| Oracle PeopleSoft 远程代码执行漏洞 | CVE-2026-35273 | 远程代码执行 | 企业应用/ERP |
| Palo Alto Networks PAN-OS GlobalProtect 认证绕过漏洞 | CVE-2026-0257 | 认证绕过 | 边界设备/VPN |
| Cisco Catalyst SD-WAN Manager 命令注入提权漏洞 | CVE-2026-20245 | 命令注入/提权 | 网络管理/SD-WAN |
| Drupal   Core SQL 注入漏洞 | CVE-2026-9082 | SQL注入 | CMS/门户 |
| Apache ActiveMQ Jolokia 远程代码执行漏洞 | CVE-2026-34197 | 远程代码执行 | 中间件/消息队列 |
| OpenTelemetry Java Agent RMI 反序列化远程代码执行漏洞 | CVE-2026-33701 | 反序列化RCE | Java组件/可观测性 |
| Veeam Service Provider Console 远程代码执行漏洞 | CVE-2026-32998 | 远程代码执行 | 备份/运维平台 |
| Microsoft SharePoint ToolShell 远程代码执行漏洞 | CVE-2025-53770 | 反序列化RCE | 协同办公/门户 |
| React Server Components React2Shell 远程代码执行漏洞 | CVE-2025-55182 | 远程代码执行 | Web框架/前端服务端渲染 |
| Fortra GoAnywhere MFT 反序列化命令注入漏洞 | CVE-2025-10035 | 反序列化/命令注入 | 文件传输/MFT |
| HPE OneView 远程代码执行漏洞 | CVE-2025-37164 | 远程代码执行 | 数据中心管理 |
| Citrix NetScaler ADC/Gateway 高危漏洞 | CVE-2026-3055 | 敏感信息泄露/认证风险 | 边界设备/应用交付 |
| 7-Zip NTFS 解析堆缓冲区溢出漏洞 | CVE-2026-48095 | 内存破坏/RCE风险 | 终端/文件处理 |
| Google Chrome V8 零日漏洞 | CVE-2026-11645 | 内存破坏/RCE风险 | 浏览器/终端 |
| WP Maps Pro WordPress 插件未授权管理员创建漏洞 | CVE-2026-8732 | 权限提升 | CMS插件/WordPress |
| Kirki   WordPress 插件未授权账户接管漏洞 | CVE-2026-8206 | 账户接管 | CMS插件/WordPress |
| XWiki 路径遍历漏洞 | CVE-2026-23734 | 路径遍历/文件读取 | 知识库/协同平台 |
| Apache PyFory 反序列化策略绕过漏洞 | CVE-2026-48207 | 反序列化绕过 | 开发组件/序列化 |
| Samba 打印子系统远程代码执行漏洞 | CVE-2026-4480 | 远程代码执行 | 文件共享/域环境 |
| Linux Kernel Copy Fail 本地权限提升漏洞 | CVE-2026-31431 | 本地提权 | 操作系统/内核 |
| Linux Kernel Fragnesia 本地权限提升漏洞 | CVE-2026-46300 | 本地提权 | 操作系统/内核 |
| Cisco Secure Workload 访问控制错误漏洞 | CVE-2026-20223 | 访问控制错误 | 安全管理平台 |
| Ivanti Connect Secure 栈溢出远程代码执行漏洞 | CVE-2025-0282 | 远程代码执行 | 边界设备/VPN |
| Fortinet FortiVoice 远程代码执行漏洞 | CVE-2025-32756 | 远程代码执行 | 边界/通信设备 |
| Apache Tomcat 远程代码执行漏洞 | CVE-2025-24813 | 远程代码执行/文件写入 | Web中间件 |
| Next.js Middleware 授权绕过漏洞 | CVE-2025-29927 | 认证/授权绕过 | Web框架 |
| Kubernetes ingress-nginx 远程代码执行漏洞 | CVE-2025-1974 | 远程代码执行 | 云原生/入口控制器 |
| Erlang/OTP SSH 远程代码执行漏洞 | CVE-2025-32433 | 远程代码执行 | 开发组件/服务端 |
| 用友时空KSOA save\_folder 存在sql注入漏洞 | TVD-2026-17959 | SQL注入 | 国产ERP |
| (CVE-2026-22679)   泛微 E-cology 10 Dubbo 调试接口远程代码执行漏洞 | CVE-2026-22679 | 远程代码执行 | 国产OA |
| 孚盟云 PriceList.ashx SQL注入漏洞 | TVD-2026-15690 | SQL注入 | 国产CRM/外贸管理系统 |
| 用友NC ResourceManagerServlet   反序列化漏洞 | TVD-2026-15337 | 反序列化 | 国产ERP |
| 通达OA video\_file.php 任意文件下载漏洞 | TVD-2026-15329 | 任意文件下载 | 国产OA |

**斗象漏洞情报中心从漏洞描述、影响范围、风险研判、检测规则和修复方案**五个方面，对上述34个漏洞进行了详细解读，由于篇幅原因，本文不做详细展示，感兴趣的读者可以**扫描下方图片的二维码**，关注“**斗象科技**”公众号，后台回复**“2026HW必修高危漏洞集合”**，即可获得完整版报告。

![](https://mmecoa.qpic.cn/mmecoa_png/TianBfDibsTJFmS2UwruF6ZGpAlMNKjLecQu88DxGsgic8eQLxZL5mXzcq4eMby8NZQkib70SCmMLBKAJscdd05CibC5hbeBy1LcZy2Hv2HiapLfs/640?wx_fmt=png&from=appmsg)

此外，斗象科技已支持详细检测规则，如需要协助，可以拨打**400-156-9866**，与斗象安全专家1V1线上交流。

**·END·**

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/TianBfDibsTJGMZ2SfIMU8PyL3kXDpLdvmvBk2VicxtyRTxVnP70q47GFckibuBw2ZhUHcQ8uYH22Bnk3lZ9TaGUb2TiaO5KhfWBnvRt3HaGEnMw/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmecoa.qpic.cn/sz_mmecoa_png/hrWzJ3hmo1YdmB1twOvgtSeH0uVJ3Y2qIQQia82Nrnfb8NOSmmibE1Hp5HgELnmgM8XwzdlosdffWRgvlvD2V1sQ/0?wx_fmt=png)

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