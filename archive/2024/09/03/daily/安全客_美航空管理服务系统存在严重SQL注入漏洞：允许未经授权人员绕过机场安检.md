---
title: 美航空管理服务系统存在严重SQL注入漏洞：允许未经授权人员绕过机场安检
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649786826&idx=1&sn=5836a828206db72a5c4643bca67de664&chksm=8893b9a5bfe430b386427669dfc669d65e16f9ebfb2388771f56ff7a703089c1471750fbf486&scene=58&subscene=0#rd
source: 安全客
date: 2024-09-03
fetch_date: 2025-10-06T18:26:02.507976
---

# 美航空管理服务系统存在严重SQL注入漏洞：允许未经授权人员绕过机场安检

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb4bytOXkg840r0zhMmUOIzoJOiclCvRK8qTFAibJtPJiboq5I1AdfydrkpXibChDTOsKuPRiaSLJpicx4Rg/0?wx_fmt=jpeg)

# 美航空管理服务系统存在严重SQL注入漏洞：允许未经授权人员绕过机场安检

安全客

最近，一项研究揭示了航空运输安全系统中的一个严重漏洞，该漏洞允许未经授权的人员绕过机场安检。Known Crewmember（KCM）和Cockpit Access Security System（CASS）是两个允许飞行员、空乘人员及其他航空公司员工绕过传统安检并进入机舱座位的系统。这些系统通过验证员工在航空公司的在职状态来决定是否授权其跳过安检或访问机舱。验证过程包括出示身份证明，然后TSA（美国运输安全管理局）工作人员使用笔记本电脑验证员工状态。

研究人员伊恩·卡罗尔（Ian Carroll）和萨姆·库里（Sam Curry）对这些系统的验证过程进行了研究，发现不同航空公司可能使用不同的系统来管理员工数据。

ARINC（柯林斯航空系统的子公司）为TSA管理KCM系统，通过API在不同航空公司之间路由授权请求。大航空公司可能有自己的系统，而小航空公司则往往依赖像FlyCASS这样的第三方服务。FlyCASS提供了一个基于Web的界面，供KCM和CASS系统参与者使用。研究人员发现FlyCASS中存在一个严重的漏洞：在登录系统中发现了SQL注入漏洞。这一缺陷使得研究人员能够获得Air Transport International的管理员访问权限，从而在该航空公司的KCM和CASS列表中添加或管理飞行员和空乘人员，而无需进一步认证。

卡罗尔表示：“为了测试是否可以添加新员工，我们创建了一个名为Test TestOnly的测试员工，并用我们选择的测试照片进行了授权，允许其使用KCM和CASS。然后，我们使用查询功能检查我们的新员工是否获得了授权。不幸的是，我们的测试用户现在被批准使用KCM和CASS。”他进一步指出：“我们意识到我们发现了一个非常严重的问题。任何具有基本SQL注入知识的人都可以登录此网站，并将任何人添加到KCM和CASS列表中，从而绕过安检并访问商用飞机的机舱。我们发现了更多严重问题，但在发现第一个问题后立即开始了披露过程。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4bytOXkg840r0zhMmUOIzoILibrMkdLwV50aiaiax1R5VRO8X1pH7CiaOJJneYia0tbfiatkrpa5RJKLPA/640?wx_fmt=png&from=appmsg)

研究人员于4月23日首次向国土安全部（DHS）披露了这一问题，随后FlyCASS在KCM/CASS系统中被禁用以解决此问题。研究人员解释说，当他们尝试协调安全的公开披露时，DHS停止了回应，而TSA则发表了误导性的声明，轻描淡写了该问题。

TSA错误地声称该漏洞无法用于访问KCM检查点，声称在发放KCM条形码之前需要进行审核过程。“不幸的是，国土安全部没有与我们合作，而TSA新闻办公室则发表了危险的错误声明，否认了我们发现的问题。”卡罗尔补充道：“TSA新闻办公室在声明中说，这个漏洞不能用于访问KCM检查点，因为TSA在发放KCM条形码之前会进行审核过程。然而，KCM条形码并不是使用KCM检查点所必需的，因为TSA工作人员可以手动输入航空公司员工ID。”

研究人员指出，由于TSA工作人员可以手动输入航空公司员工ID，因此KCM条形码并不是必需的。随后，TSA从其网站上删除了相关信息，但没有解决研究人员的更正问题。攻击者可能会利用该漏洞进行其他攻击，例如编辑现有KCM成员的详细信息，从而绕过新成员的审核过程。此外，未注册的KCM条形码可能会通过KCM网站与员工ID关联。

文章来源：

https://securityaffairs.com/167862/hacking/air-transport-security-systems-critical-flaw.html

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4bytOXkg840r0zhMmUOIzoEAZ2BqwY4vKHc4UcMDKjU9BukfL9XyOZbc4OTNHCiccP0Fb2VOxxj3w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb4bytOXkg840r0zhMmUOIzobWjbM9bb8whmJfYV8q8Bic8RqWeKkh8rUEHFpC4nr8Oox6G01DkMPSA/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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