---
title: 【已复现】GitLab 远程代码执行漏洞安全风险通告第二次更新
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247497301&idx=2&sn=b6e6e17cabcd53962b115f1120005bf4&chksm=fe79d2cdc90e5bdb639eb6d373369c202a7e96782a4d995033744406d6369fe079aaa37d1a21&scene=58&subscene=0#rd
source: 奇安信CERT
date: 2023-01-10
fetch_date: 2025-10-04T03:25:55.633452
---

# 【已复现】GitLab 远程代码执行漏洞安全风险通告第二次更新

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs488LXldqsXfILb7U6snyRZF01RIvO51icvgRG7xaC1540KIV9y4xdUuHc7NY6D23h9jdRUX6d5tNzA/0?wx_fmt=jpeg)

# 【已复现】GitLab 远程代码执行漏洞安全风险通告第二次更新

原创

QAX CERT

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供安全风险**通告**和**有效**解决方案。

**安全通告**

Gitlab是目前被广泛使用的基于git的开源代码管理平台, 基于Ruby on Rails构建, 主要针对软件开发过程中产生的代码和文档进行管理，同时可以搭建Web服务。

近日，奇安信CERT监测到GitLab官方发布**GitLab远程代码执行漏洞(CVE-2022-2992)**通告，该漏洞存在是由于未对GitHub中导入的API端点请求数据进行校验。经过身份认证的远程攻击者可通过发送特制的请求包最终在目标机器上执行任意代码。**鉴于此漏洞影响范围较大，建议客户尽快做好自查及防护。**

本次更新内容：

新增GitLab远程代码执行漏洞(CVE-2022-2992)复现截图；

更新技术类型及参考链接，新增CNNVD编号；

新增奇安信产品解决方案。

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **GitLab** **远程代码执行漏洞** | | |
| **公开时间** | 2022-08-30 | **更新时间** | 2023-01-09 |
| **CVE****编号** | CVE-2022-2992 | **其他编号** | QVD-2022-13943  CNNVD-202208-4486 |
| **威胁类型** | 代码执行 | **技术类型** | 命令注入 |
| **厂商** | GitLab | **产品** | GitLab CE、GitLab EE |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| **已公开** | 未发现 | 未发现 | **已公开** |
| **漏洞描述** | GitLab社区版（CE）和企业版（EE）存在远程代码执行漏洞。经过身份验证的攻击者可以通过 GitHub API 端点导入功能执行任意代码，最终控制服务器。 | | |
| **影响版本** | 11.10 <= GitLab CE/EE < 15.1.6 GitLab CE/EE 15.2.x < 15.2.4 GitLab CE/EE 15.3.x < 15.3.2 | | |
| **不受影响版本** | GitLab CE/EE >= 15.1.6  GitLab CE/EE >= 15.2.4  GitLab CE/EE >= 15.3.2 | | |
| **其他受影响组件** | 无 | | |

奇安信CERT已成功复现**GitLab远程代码执行漏洞(CVE-2022-2992)**，复现截图如下:

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs488LXldqsXfILb7U6snyRZFBQbW8iau7Ztxx2aebImdahIDdTWbibm8p8utxibibZK2bTiavY1lMoORoKg/640?wx_fmt=png)

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | **GitLab** **远程代码执行漏洞** | | | |
| **CVE****编号** | CVE-2022-2992 | **其他编号** | | QVD-2022-13943  CNNVD-202208-4486 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 9.9 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 低权限 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 经过身份认证的远程攻击者可通过GitHub API 端点导入功能实现远程代码执行。 | | | |

处置建议

**1.目前官方已发布安全版本修复该漏洞，建议受影响用户：**

GitLab CE/EE 15.1.x及更低版本升级至15.1.6或更高版本；

GitLab CE/EE 15.2.x升级至15.2.4或更高版本；

GitLab CE/EE 15.3.x升级至15.3.2或更高版本。

**下载地址：**

https://about.gitlab.com/update/

**2.若无法立即升级，可以通过禁用 GitHub 导入来缓解此漏洞：**

使用管理员帐户登录到GitLab 执行以下操作：

(1）点击“菜单”->“管理”

(2）点击“设置”->“常规”

(3） 展开“可见性和访问控制”选项卡

(4） 在“导入源”下禁用“GitHub”选项

(5）点击“保存更改”

产品解决方案

**奇安信网站应用安全云防护系统已更新防护特征库**

奇安信网神网站应用安全云防护系统已全局更新所有云端防护节点的防护规则，支持对GitLab 远程代码执行漏洞(CVE-2022-2992)的防护。

**奇安信开源卫士已支持**

奇安信开源卫士20230109.140版本已支持对Gitlab 远程命令执行漏洞（CVE-2022-2992）的检测。

**奇安信自动化渗透测试系统产品解决方案**

奇安信自动化渗透测试系统在第一时间加入了该漏洞的插件规则和指纹规则，请将插件版本和指纹版本升级到20230109182100版本。规则名称：Gitlab CVE-2022-2992 远程命令执行漏洞，插件版本：20230109182100，指纹版本：20230109182100。奇安信自动化渗透测试系统升级方法：系统管理->升级管理->插件升级（指纹升级），选择“网络升级”或“本地升级”。

**奇安信网神网络数据传感器系统产品检测方案**

奇安信网神网络数据传感器（NDS5000/7000/9000系列）产品，已具备该漏洞的检测能力。规则ID为：7696 ，建议用户尽快升级检测规则库至2301091300以上。

参考资料

[1]https://about.gitlab.com/releases/2022/08/30/critical-security-release-gitlab-15-3-2-released/

[2]https://gitlab.com/gitlab-org/gitlab/-/issues/371884

时间线

2022年8月31日，奇安信 CERT发布安全风险通告；

2023年1月9日，奇安信 CERT发布安全风险通告第二次更新。

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