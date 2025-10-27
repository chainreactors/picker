---
title: 【已复现】Fortinet FortiNAC 远程代码执行漏洞安全风险通告第二次更新
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247497814&idx=2&sn=751cd6f30cd0a6aafa9a54fea4689dc4&chksm=fe79dccec90e55d86be9e601f65c1d6ea5e30388ecb286de5b61bf86d06ffe48e07c9003b0c1&scene=58&subscene=0#rd
source: 奇安信CERT
date: 2023-02-23
fetch_date: 2025-10-04T07:52:13.055578
---

# 【已复现】Fortinet FortiNAC 远程代码执行漏洞安全风险通告第二次更新

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs48L70WLibyq7VpLjb6QRAy8icb2zFqgVNyPexeIia14Gvq8UG9XVgQmgka5nVqHrFl1YrCjR2xbFtn3g/0?wx_fmt=jpeg)

# 【已复现】Fortinet FortiNAC 远程代码执行漏洞安全风险通告第二次更新

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供安全风险**通告**和**有效**解决方案。

**安全通告**

FortiNAC(Network Access Control) 是Fortinet的一种零信任网络访问控制解决方案，可增强用户对企业网络上的物联网 (IoT) 设备的监控。NAC 是零信任网络访问安全模型的重要组成部分，在该模型中，IT 团队可以轻松了解正在访问网络的人员和设备，以及如何保护网络内外的公司资产。NAC 可提供全面的网络可视性，有效控制设备和用户，包括自动化动态响应。

近日，奇安信CERT监测到Fortinet官方发布安全更新，其中包含**Fortinet FortiNAC 远程代码执行漏洞(CVE-2022-39952)**。FortiNAC keyUpload 脚本中存在任意文件写入漏洞，未经身份认证的远程攻击者可利用此漏洞向目标系统写入任意内容，最终可在目标系统上以 Root 权限执行任意命令，**目前该漏洞细节及PoC已公开，奇安信CERT已成功复现该漏洞。****鉴于此漏洞影响较大，建议客户尽快更新至最新版本。**

**本次更新内容：**

**修改漏洞信息；**

**新增复现截图；**

**新增产品解决方案；**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **Fortinet FortiNAC** **远程代码执行漏洞** | | |
| **公开时间** | 2023-02-20 | **更新时间** | 2023-02-20 |
| **CVE****编号** | CVE-2022-39952 | **其他编号** | QVD-2023-4737  CNNVD-202302-1434 |
| **威胁类型** | 代码执行 | **技术类型** | 文件名或路径的外部可控制 |
| **厂商** | Fortinet | **产品** | FortiNAC |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| **已公开** | 未发现 | 未发现 | **已公开** |
| **漏洞描述** | FortiNAC keyUpload 脚本中存在任意文件写入漏洞，未经身份认证的远程攻击者可利用此漏洞向目标系统写入任意内容，最终可在目标系统上以 Root 权限执行任意命令 | | |
| **影响版本** | FortiNAC 9.4.0  FortiNAC 9.2.x <= 9.2.5  FortiNAC 9.1.x <= 9.1.7  FortiNAC 8.8.x  FortiNAC 8.7.x  FortiNAC 8.6.x  FortiNAC 8.5.x  FortiNAC 8.3.x | | |
| **不受影响版本** | FortiNAC 9.4.x >= 9.4.1  FortiNAC 9.2.x >= 9.2.6  FortiNAC 9.1.x >= 9.1.8  FortiNAC 7.2.x >= 7.2.0 | | |
| **其他受影响组件** | 无 | | |

目前奇安信CERT已成功复现该漏洞，截图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs48L70WLibyq7VpLjb6QRAy8ic25KUUt7xAYLxtKKUOsJ1WHu2BKxYV4YJZibUW9goXW9IfRDAHrSJtsA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs48L70WLibyq7VpLjb6QRAy8icFmycic0bcoMhGM7FILiaBoZq3xnVaCWo8tEia8K8O6TZCXIS8DM2DQ9zQ/640?wx_fmt=png)

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | Fortinet FortiNAC 远程代码执行漏洞 | | | |
| **CVE****编号** | CVE-2022-39952 | **其他编号** | | QVD-2023-4737  CNNVD-202302-1434 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 9.8 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 不需要 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 未经身份认证的远程攻击者可利用此漏洞向目标系统写入任意内容，最终可在目标系统上以 Root 权限执行任意代码。 | | | |

处置建议

**1、修复建议**

目前 Fortinet 官方已发布安全版本修复该漏洞，建议受影响用户尽快更新至对应的安全版本。

FortiNAC 9.4.x >= 9.4.1

FortiNAC 9.2.x >= 9.2.6

FortiNAC 9.1.x >= 9.1.8

FortiNAC 7.2.x >= 7.2.0

**2、检测规则**

Snort已公开该漏洞检测规则，如下：

```
alert http ( msg:"SERVER-OTHER Fortinet Fortinac keyUpload.jsp remote code execution attempt"; flow:to_server,established; http_uri; content:"/configWizard/keyUpload.jsp",fast_pattern,nocase; http_client_body; content:"name=|22|key|22|",nocase; content:"filename=",nocase; metadata:policy balanced-ips drop,policy max-detect-ips drop,policy security-ips drop; reference:cve,2022-39952; classtype:attempted-admin; gid:1; sid:61392; rev:1; )
```

Emerging Threat已公开该漏洞检测规则，如下：

```
alert tcp any any -> [$HOME_NET,$HTTP_SERVERS] $HTTP_PORTS (msg:"ET EXPLOIT Fortinet FortiNAC - Observed POST .zip with Vulnerable Parameter (CVE-2022-39952)"; flow:to_server,established; content:"POST"; http_method; content:"/configWizard/keyUpload.jsp"; http_uri; fast_pattern:0,20; content:"name=|22|key|22 3b|"; http_client_body; content:"|0d 0a 0d 0a|PK"; http_client_body; reference:cve,2022-39952; classtype:attempted-admin; sid:2044270; rev:1; metadata:attack_target Server, created_at 2023_02_21, cve CVE_2022_39952, deployment Perimeter, deployment Internal, former_category EXPLOIT, signature_severity Major, tag Exploit, updated_at 2023_02_21;)
```

产品解决方案

**奇安信网站应用安全云防护系统已更新防护特征库**

奇安信网神网站应用安全云防护系统已全局更新所有云端防护节点的防护规则，支持对Fortinet FortiNAC 远程代码执行漏洞(CVE-2022-39952)的防护。

**奇安信天眼检测方案**

奇安信天眼新一代安全感知系统已经能够有效检测针对该漏洞的攻击，请将规则版本升级到3.0.0222.13753或以上版本。规则ID及规则名称：0x100214FA，Fortinet FortiNAC 远程代码执行漏洞(CVE-2022-39952)。奇安信天眼流量探针规则升级方法：系统配置->设备升级->规则升级，选择“网络升级”或“本地升级”。

**奇安信网神网络数据传感器系统产品检测方案**

奇安信网神网络数据传感器（NDS5000/7000/9000系列）产品，已具备该漏洞的检测能力。规则ID为：7714，建议用户尽快升级检测规则库至2302221300以上；

**奇安信自动化渗透测试系统检测方案**

奇安信自动化渗透测试系统在第一时间加入了该漏洞的插件规则和指纹规则，请将插件版本和指纹版本升级到20230222120508以上版本。规则名称：Fortinet FortiNAC CVE-2022-39952远程代码执行漏洞，插件版本：20230222120508，指纹版本：20230222120508。奇安信自动化渗透测试系统升级方法：系统管理->升级管理->插件升级（指纹升级），选择“网络升级”或“本地升级”。

参考资料

[1]https://www.fortiguard.com/psirt/FG-IR-22-300

时间线

2023年2月21日，奇安信 CERT发布安全风险通告；

2023年2月22日，奇安信CERT发布安全风险通告第二次更新。

点击**阅读原文**

到奇安信NOX-安全监测平台查询更多漏洞详情

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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
在看
，轻点两下取消在看
分享
留言
收藏
听过