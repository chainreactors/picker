---
title: 2026攻防演练必修高危漏洞集合（2.0版）
url: https://mp.weixin.qq.com/s/IdViLpiWmrSNgSSabjGI6A
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:21:51.561030
---

# 2026攻防演练必修高危漏洞集合（2.0版）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8U6kERPHGZzgc8L7ktFVE1UiaWS4t2ww2hWCkzXYPeqVBKF1iaojfEicRXlmaPNiau12cwrOPeDeh02aicJkrHy6fxF4ZxOLcI9GZRPKpD8fwzQ/0?wx_fmt=jpeg)

# 2026攻防演练必修高危漏洞集合（2.0版）

漏洞盒子VulBox

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

高危风险漏洞一直是国内护网期间企业网络安全防护的重点风险面。随着政企单位业务系统、办公协同、ERP、CRM、运维安全、视频安防、MES、指挥调度等系统逐步国产化，红队打点目标也会更多转向国内常见应用和行业场景系统。

HW攻防演练在即，斗象XVI扩展漏洞情报结合近期漏洞情报、公开验证情况和国内护网常见资产类型，整理形成**《2026HW必修高危漏洞集合（2.0版）》**。本版重点覆盖国产化环境下更常见的业务系统、协同办公、运维管理和行业应用，便于企业补充第一版之外的自查清单。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/TianBfDibsTJFp7QBa7GKQ0oQVU6euSyZ3PQkNzqoXE0Hv5F6c2VBHE18vGGXoTXYia61TJ7ySKOhnZvC3niaDTtw5RicXlIF8QXvIbW4ibsJsOCk/640?wx_fmt=png&from=appmsg)

本期报告整理收录了2026年公开披露且适合HW排查的高危漏洞，包含漏洞基础信息、影响范围、风险研判、检测思路和修复建议。企业可结合自身资产暴露面、系统重要性和可访问范围开展针对性排查。

**1**

**漏洞数据汇总**

以下数据针对2026年公开披露且适合HW排查的高危漏洞进行系统梳理，具体汇总如下：

* **SQL注入**

漏洞数量：11个

涉及厂商：Fortinet、用友、泛微、金和、任我行、东胜物流、易宇通、云连、深科特/LVS、九佳易

* **任意文件读取/目录访问**

漏洞数量：6 个

涉及厂商：畅捷通、Supermap、天地伟业、孚盟云、LVS、友数聚

* **远程代码执行（RCE）/ 命令注入**

漏洞数量：6 个

涉及厂商：VMware、Palo Alto Networks、Fortinet、深信服、青龙面板

* **任意文件上传**

漏洞数量：4 个

涉及厂商：九麒科技、智慧校园系统、可视化融合指挥调度平台、博硕BGM

* **其他**

漏洞数量：11

漏洞类型：反序列化、认证绕过、内存破坏/代码执行、代码注入/提权、信息泄露、配置不当、失效的身份认证、路径遍历

涉及厂商：Oracle、Apache、Cisco、Ivanti、深信服、用友、天锐绿盾、九麒科技、fnOS等

**2**

**本次高危漏洞自查列表**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **漏洞编号** | **类型** | **资产类别** |
| Oracle WebLogic Server 反序列化漏洞 | CVE-2026-35300 | 反序列化 | 中间件/WebLogic |
| Apache HTTP Server 配置中正则表达式缓冲区下写漏洞 | CVE-2026-44631 | 内存破坏/代码执行风险 | Web服务器/Apache HTTP Server |
| VMware Aria Operations 命令注入漏洞 | CVE-2026-22719 | 命令注入/RCE | 虚拟化运维平台 |
| Cisco Catalyst SD-WAN Controller 认证绕过漏洞 | CVE-2026-20182 | 认证绕过/管理员权限 | 网络控制器/SD-WAN |
| Palo Alto Networks PAN-OS Captive   Portal 远程代码执行漏洞 | CVE-2026-0300 | 内存破坏/RCE | 边界设备/防火墙 |
| Fortinet FortiClient EMS SQL 注入远程命令执行漏洞 | CVE-2026-21643 | SQL注入/命令执行 | 终端管理/FortiClient EMS |
| Ivanti Sentry OS 命令注入漏洞 | CVE-2026-10520 | 命令注入/RCE | 移动接入/安全网关 |
| Cisco Unified Communications 多产品代码注入漏洞 | CVE-2026-20045 | 代码注入/提权 | 统一通信/语音平台 |
| 深信服运维安全管理系统 save\_SNMP 远程代码执行漏洞 | TVD-2026-08916 | 远程代码执行 | 运维安全/堡垒机 |
| 深信服运维安全管理系统 search\_login 信息泄露漏洞 | TVD-2026-08538 | 信息泄露 | 运维安全/堡垒机 |
| 用友NC ServletForESBAdaptor 反序列化漏洞 | TVD-2026-10155 | 不安全的反序列化 | 国产ERP |
| 用友U8Cloud openapi SQL注入漏洞 | TVD-2026-04479 | SQL注入 | 国产ERP |
| 用友U8 CRM changebgflag.php SQL注入漏洞 | TVD-2026-04361 | SQL注入 | 国产CRM/ERP |
| 泛微云桥 e-Bridge sendWxMsg SQL注入漏洞 | TVD-2026-08730 | SQL注入 | 国产OA/云桥 |
| 金和OA VouchUpdate.aspx SQL注入漏洞 | TVD-2026-05617 | SQL注入 | 国产OA |
| 畅捷通T+ DownLoadBlockFile 任意文件读取漏洞 | TVD-2026-10503 | 任意文件或目录访问 | 财务/ERP |
| Supermap iServer output 任意文件读取漏洞 | TVD-2026-05859 | 任意文件或目录访问 | GIS/地理信息平台 |
| 天地伟业Easy7综合管理平台 downloadNote 任意文件读取漏洞 | TVD-2026-05372 | 任意文件或目录访问 | 视频安防/综合管理平台 |
| 青龙定时任务管理面板 command-run 远程代码执行漏洞 | TVD-2026-08555 | 远程代码执行 | 任务调度/运维平台 |
| 青龙定时任务管理面板 dependencies 远程代码执行漏洞 | TVD-2026-08739 | 远程代码执行 | 任务调度/运维平台 |
| 悟空CRM queryUserList 登陆绕过漏洞 | TVD-2026-10475 | 配置不当 | WEB应用 |
| 任我行协同CRM普及版 viewaccountBase SQL注入漏洞 | TVD-2026-07626 | SQL注入 | 国产CRM |
| 孚盟云 TfrmProject 任意文件读取漏洞 | TVD-2026-08938 | 任意文件或目录访问 | 国产CRM/外贸管理系统 |
| 天锐绿盾审批系统 updateFilePrintParamsD.do fastjson 反序列化漏洞 | TVD-2026-07625 | 不安全的反序列化 | 数据防泄漏/审批系统 |
| 九麒科技 BigAnt 即时通讯系统 upload\_file 任意文件上传漏洞 | TVD-2026-05020 | 任意上传 | 即时通讯/协同办公 |
| 九麒科技 BigAnt 即时通讯系统 loginByToken 登录绕过漏洞 | TVD-2026-05034 | 失效的身份认证 | 即时通讯/协同办公 |
| fnOS app-center-static 目录遍历漏洞 | TVD-2026-04379 | 路径遍历 | 私有云/NAS |
| 智慧校园(安校易)管理系统 FileUpload.ashx 任意文件上传漏洞 | TVD-2026-10809 | 任意上传 | 智慧校园平台 |
| 可视化融合指挥调度平台 upload 任意文件上传漏洞 | TVD-2026-08343 | 任意上传 | 指挥调度平台 |
| 东胜物流软件 CrmProxyMailListGridSource.aspx SQL注入漏洞 | TVD-2026-07472 | SQL注入 | 物流管理系统 |
| 易宇通KingTrans物流管理系统 getAccountTypeByNumber SQL注入漏洞 | TVD-2026-08724 | SQL注入 | 物流管理系统 |
| 云连POS-ERP管理系统 getClsItem.action SQL注入漏洞 | TVD-2026-11167 | SQL注入 | POS/ERP |
| 深科特 LEAN MES系统 UploadPortraits.ashx 任意文件上传漏洞 | TVD-2026-11937 | 任意上传 | MES/生产管理系统 |
| LVS精益价值管理系统 WebSer.asmx SQL注入漏洞 | TVD-2026-09884 | SQL注入 | MES/精益管理系统 |
| LVS精益价值管理系统 LoginVaild.aspx 任意文件读取漏洞 | TVD-2026-09864 | 任意文件或目录访问 | MES/精益管理系统 |
| 友数聚 CPAS审计管理系统 doDownLoadPicFile 任意文件读取漏洞 | TVD-2026-11493 | 任意文件或目录访问 | 审计管理系统 |
| 博硕BGM Upload.ashx 任意文件上传漏洞 | TVD-2026-04901 | 任意上传 | 业务管理系统 |
| 九佳易管理系统 PrivilegedCodeDestroy.asmx SQL注入漏洞 | TVD-2026-08336 | SQL注入 | 业务管理系统 |

**斗象漏****洞情报中心****从漏洞描述、影响范围、风险研判、检测规则和修复方案**五个方面，对上述38个漏洞进行了详细解读，由于篇幅原因，本文不做详细展示，感兴趣的读者可以**扫描下方图片的二维码**，关注“**斗象科技**”公众号，后台回复**“2026HW必修高危漏洞集合2.0”**，即可获得完整版报告。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/TianBfDibsTJE1iaSibEibTKplhqvq42RH0QnKibxJZhPBs5JlDQaoNBWgep10V2VU5pQdz6ictUKyAMlsUZMsaIJjeYdwKIIxhiaKSnY8vCY9tpJcE/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jBzzLZqveIcwb2BPjSmvzKvZDIbvicctgd3jz9EQjBqtiba5Y2D3f0fFj913L7oPJaSBxefiaTW0iajuN272LSqoEw/0?wx_fmt=png)

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