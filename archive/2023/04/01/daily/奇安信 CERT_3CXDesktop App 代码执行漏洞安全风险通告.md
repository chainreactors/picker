---
title: 3CXDesktop App 代码执行漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247498142&idx=1&sn=dcfa11ee9419d2d7b56fe90c9d70ab10&chksm=fe79dd06c90e541077b0c8b16c8f4e7b76fc11fedf89babca2205d25bb9bf42e64f40fcaf3d4&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2023-04-01
fetch_date: 2025-10-04T11:22:44.522767
---

# 3CXDesktop App 代码执行漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs489X0JHJj8aibS5abrVuLLAtDP5amAic3DHTPZnymSKCeibGyqiabzMY8VR29TSbVXV49LJPASbbOCWLA/0?wx_fmt=jpeg)

# 3CXDesktop App 代码执行漏洞安全风险通告

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

**安全通告**

3CXDesktop App 是一款跨平台桌面电话应用程序，适用于Linux、MacOS 和 Windows。3CXDesktop 允许用户通过聊天、消息、视频和语音进行交互。3CX在全球190多个国家和地区提供服务，拥有超过1200万日活用户和60万以上的客户群体。其网站上列出的客户包括汽车、航空航天、金融、食品饮料、政府、酒店和制造等多个行业的知名企业。

近日，奇安信CERT监测到**3****CXDesktop App代码执行漏洞(CVE-2023-29059)**，3CXDesktop App 部分版本在构建安装程序时，内嵌了攻击者特制的恶意代码，在程序安装时会执行恶意代码，并进一步下载恶意负载到目标环境中执行。**鉴于该产品用量较多，建议客户尽快做好自查及防护。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | 3CXDesktop App 代码执行漏洞 | | |
| **公开时间** | 2023-03-30 | **更新时间** | 2023-03-31 |
| **CVE****编号** | CVE-2023-29059 | **其他编号** | QVD-2023-7890 |
| **威胁类型** | 代码执行 | **技术类型** | 内嵌的恶意代码 |
| **厂商** | 3CX | **产品** | 3CXDesktop App |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | **已发现** | 未公开 |
| **漏洞描述** | 3CXDesktop App 部分版本在构建安装程序时，内嵌了攻击者特制的恶意代码，程序安装时会执行恶意代码，并进一步下载恶意负载到目标环境中执行。 | | |
| **影响版本** | Electron Mac 3CXDesktop App = 18.11.1213  Electron Mac 3CXDesktop App = 18.12.402  Electron Mac 3CXDesktop App = 18.12.407  Electron Mac 3CXDesktop App = 18.12.416  Electron Windows 3CXDesktop App shipped in Update 7 =   18.12.407  Electron Windows 3CXDesktop App shipped in Update 7 =   18.12.416 | | |
| **其他受影响组件** | 无 | | |

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | 3CXDesktop App 代码执行漏洞 | | | |
| **CVE****编号** | CVE-2023-29059 | **其他编号** | | QVD-2023-7890 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | **9.6** |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **用户认证（****Au****）** | | **用户交互（****UI****）** | |
| 无 | | 需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 低 | |
| **危害描述** | 在程序安装时会执行恶意代码，并进一步下载恶意负载到目标环境中执行。 | | | |

处置建议

**官方暂未发布修复程序，受影响用户可以使用下面的缓解方案来缓解此漏洞。**

**缓解方案：**

使用PWA App，PWA App的安装方法可以参考下面链接：

https://www.3cx.com/user-manual/web-client/

**入侵检测指标(IOC)：**

akamaicontainer[.]com

akamaitechcloudservices[.]com

azuredeploystore[.]com

azureonlinecloud[.]com

azureonlinestorage[.]com

dunamistrd[.]com

glcloudservice[.]com

journalide[.]org

msedgepackageinfo[.]com

msstorageazure[.]com

msstorageboxes[.]com

officeaddons[.]com

officestoragebox[.]com

pbxcloudeservices[.]com

pbxphonenetwork[.]com

pbxsources[.]com

qwepoi123098[.]com

sbmsa[.]wiki

sourceslabs[.]com

visualstudiofactory[.]com

zacharryblogs[.]com

akamaicontainer[.]com

akamaitechcloudservices[.]com

azuredeploystore[.]com

azureonlinecloud[.]com

azureonlinestorage.com

convieneonline[.]com

dunamistrd[.]com

glcloudservice[.]com

journalide[.]org

msedgepackageinfo[.]com

msstorageazure[.]com

msstorageboxes[.]com

officeaddons[.]com

officestoragebox[.]com

pbxcloudeservices[.]com

pbxphonenetwork[.]com

pbxsources[.]com

qwepoi123098[.]com

Soyoungjun[.]com

aa124a4b4df12b34e74ee7f6c683b2ebec4ce9a8edcf9be345823b4fdcf5d868

59e1edf4d82fae4978e97512b0331b7eb21dd4b838b850ba46794d9c7a2c0983

92005051ae314d61074ed94a52e76b1c3e21e7f0e8c1d1fdd497a006ce45fa61

5407cda7d3a75e7b1e030b1f33337a56f293578ffa8b3ae19c671051ed314290

b86c695822013483fa4e2dfdf712c5ee777d7b99cbad8c2fa2274b133481eadb

e6bbc33815b9f20b0cf832d7401dd893fbc467c800728b5891336706da0dbcec

11be1803e2e307b647a8a7e02d128335c448ff741bf06bf52b332e0bbf423b03

7986bbaee8940da11ce089383521ab420c443ab7b15ed42aed91fd31ce833896

c485674ee63ec8d4e8fde9800788175a8b02d3f9416d0e763360fff7f8eb4e02

B5E318240401010E4453E146E3E67464DD625CFEF9CD51C5015D68550EE8CC09

AA4E398B3BD8645016D8090FFC77D15F926A8E69258642191DEB4E68688FF973

参考资料

[1]https://www.3cx.com/blog/news/desktopapp-security-alert/

[2]https://www.3cx.com/user-manual/web-client/

时间线

2023年3月31日，奇安信 CERT发布安全风险通告。

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