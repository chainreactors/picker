---
title: HR软件成了攻击入口？看“Jasper Sleet”如何混成远程IT员工
url: https://mp.weixin.qq.com/s/jWEXYE9qRrDOcl55gVebcg
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:35:36.316005
---

# HR软件成了攻击入口？看“Jasper Sleet”如何混成远程IT员工

![cover_image](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibcgx9iap18efkhjzlOE6libpTSYZdGSBXP7QkYradRjMcOgbve2SvR479lRxZyiaHyDQjbHiaq4cUHpRLN7micfRkSj020I8l2Ptx8c/0?wx_fmt=png&from=appmsg)

# HR软件成了攻击入口？看“Jasper Sleet”如何混成远程IT员工

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 一个与朝鲜有关的威胁组织“Jasper Sleet”，正在利用远程招聘流程的漏洞，伪装成合格的IT求职者潜入目标公司。他们渗透过程覆盖了从投递简历到入职后的全链条。本文将拆解其攻击路径，并基于真实数据给出具体、可操作的检测与防护建议。

## 一场精心编排的“入职”攻击

疫情后远程办公普及，企业招募流程也全面线上化。认证靠网络，入职靠邮件，这在提升效率的同时，也撕开了一道新口子。

一个被称为“Jasper Sleet”的威胁组织就盯上了这个空档。他们把传统的人力资源（HR）SaaS平台，变成了网络攻击的跳板。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibcgx9iap18efkhjzlOE6libpTSYZdGSBXP7QkYradRjMcOgbve2SvR479lRxZyiaHyDQjbHiaq4cUHpRLN7micfRkSj020I8l2Ptx8c/640?wx_fmt=png&from=appmsg)

▲ “Jasper Sleet”利用招聘流程的攻击链概览。

他们的剧本是这样的：先是伪造或盗用身份，伪装成技术娴熟的远程IT工作者。然后在目标公司的招聘网站上，像“海投”一样，针对特定技术岗位批量投递简历。他们甚至会用生成式AI去分析职位描述，让自己的求职信和简历完美匹配对方要求，以此大幅提升通过筛选的概率。

一旦被成功录用，他们就“名正言顺”地完成线上入职流程，设置工资账户。至此，一个带有合法员工身份的账号到手。接下来的戏码大家可能猜到了：登录内部系统，访问公司数据，为后续的窃密或勒索铺路。

这套攻击模式的狡猾之处在于，它每一步都踩在合法业务流程的节点上。单独看任何一个环节——求职者访问招聘网站、填写申请、入职办理手续——都看似正常。但连起来看，就是一场有预谋的渗透。

## 攻击链深度解析与检测点

微软的观测与分析将攻击流程分成了三个阶段：招聘前、招聘中、入职后。每个阶段都有其特殊的行为和可供追溯的信号。

### 招聘前：API调用的异常“踩点”

在寻找目标阶段，“Jasper Sleet”会通过目标公司对外公开的招聘网站，调用Workday等HR平台的招聘API接口。

他们会访问诸如`hrrecruiting/jobApplicationPackages/*`、`hrrecruiting/resumes/*`这类端点，来获取职位详情、提交申请。问题是，这些调用本身并非恶意，任何申请者都会这么做。

但狐狸尾巴藏不住。真正的求职者往往用少数几个账号。而“Jasper Sleet”则会用大量外部账号，以固定、重复的模式，对同一组API进行访问。这种“广撒网”式的踩点行为，与个人求职逻辑不符。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibc6eLiapoTGsGJswEewZSkFb0VajFSb6Zjiak6pfia0tJ84xLIPNzaFwmTP4MfnzXwwmyXQNC192jTYScsVVFLGmpUgTicicXbVIibGU/640?wx_fmt=webp&from=appmsg)

▲ 来自可疑外部账号对招聘API的批量访问记录。

**检测建议：**利用Microsoft Defender for Cloud Apps的Workday连接器，监控所有连接到`/hrrecruiting`端点的API活动。重点追查“外部用户”账号，并将其访问的IP地址、时间规律与已知的“Jasper Sleet”威胁情报进行比对。发现得越早，止损成本越低。

### 招聘中：沟通工具里的蛛丝马迹

进入面试环节后，战场会转移到沟通工具。

威胁组织会使用电子邮件、Microsoft Teams、Zoom或Cisco Webex等平台与招聘团队联系，安排面试。这为检测提供了额外的机会。

**检测建议：**

* **邮件与Teams：**

  在Microsoft Defender XDR中，可以通过高级搜寻查询，追踪来自可疑IP地址或邮箱的外联系人发起的、包含“面试”等关键词的邮件或聊天记录。
* **Zoom/Webex：**

  启用Defender for Cloud Apps对应的连接器，监控面试会议中是否有来自恶意基础设施的外部账号参与。
* **文件签署：**

  启用DocuSign连接器。Offer Letter（录用通知书）的签署是一个关键节点。监控来自可疑源头的合同签署活动，能有效拦截恶意入职。

### 入职后：新员工的“不可能旅行”

攻击者成功入职，拿到了内部账号，这才是他们真正行动的开始。

我们观察到，在入职初期，这些“新员工”的账户会立即出现可疑活动。例如，在短时间内从地理位置相距甚远的不同IP登录，触发“不可能旅行”警报。

他们的账户也会尝试大量访问内部SaaS应用，如Teams、SharePoint、OneDrive，进行搜索和下载。对于一个刚入职、理论上还在适应期的新人来说，这种行为显得过于急切了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibd796WYCs7iaibibcCyDgQJUHnVhuDjzsHac9VoMxbKAfVR3iaVl0H2KUbQ2HfXcsTNYjeyTFpeKgrKAcC66OoyOibpTezrkDMzFDtk/640?wx_fmt=webp&from=appmsg)

▲ 新入职账号对工资账户信息进行异常修改的样本事件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibedAk75EoFCFUZrF7wAhSNumrJiaa6Cmsb5GrIIhwibze3bZQKicImrw7lRTR0Ln7Xmao10ic656VBShpyHBSITG4Llkfc3HzWqbvQ/640?wx_fmt=webp&from=appmsg)

▲ 某新员工入职头两个月内频繁触发的“不可能旅行”警报。

**检测建议：**对所有新创建的员工账号，特别是远程IT职位，提高监控等级。警惕任何与数据访问、多地理位点登录、匿名代理使用相关的警报。入职初期的异常行为往往最密集，是揪出他们的黄金窗口。

## 微软的实战防护工具箱

讲完攻击手法，说说怎么防。微软基于这套攻击链条，在Defender产品线提供了相应的检测覆盖。

| 攻击战术 | 观察到的主要活动 | Microsoft Defender 覆盖项 |
| --- | --- | --- |
| 资源开发 | 访问对外Workday网站，研究职位并提交申请 | Microsoft Defender for Cloud Apps – 检测Workday招聘服务中的可疑活动 |
| 资源开发 | 入职后登录新Workday账号，从已知恶意IP更新工资信息 | Microsoft Defender for Cloud Apps – 检测Workday中可疑的薪资财务活动 |
| 初始访问 | 新入职威胁角色进行异常登录，访问内部资源 | Microsoft Defender XDR – 不可能旅行告警；由疑似“Jasper Sleet”发起的登录活动 |

这套组合拳的核心思路，是**打破数据孤岛**。把HR系统的员工入职事件、身份系统的登录日志、端点的访问行为、云应用的操作记录全部关联起来，才能看清跨系统、多阶段的完整攻击图景。

对于安全团队来说，给出几个可以直接上手的建议：

1. **启用并配置好连接器。**

   别再让HR系统成为监控盲区。将Workday、DocuSign、Zoom等业务平台接入Defender for Cloud Apps，让外部用户的动作变得可见。
2. **新员工账号是高风险资产。**

   建立对新创账号（尤其是远程权限高的账号）的特殊监控策略，头30天是重点观察期。
3. **培训你的HR和用人部门。**

   让他们成为第一道防线。教会招聘人员在面试和背调中识别反常迹象，比如过度完美的简历、对薪资细节异常模糊、催促快速入职等。

> 这类攻击的隐蔽性极强，因为它披着“合法业务”的外衣。传统的防火墙、杀毒软件对此几乎无效。防御的关键在于将安全左移，从招聘阶段就开始介入，并依靠行为分析和威胁情报来发现那些“完美”伪装下的异常模式。

## 几条实用的高级搜寻查询

最后，附上几条可以直接在Microsoft Defender XDR中运行的高级搜寻查询（KQL）。这些查询能帮你主动发现环境中可能存在的类似威胁活动。

**查询1：外部用户对Workday招聘API的访问**

let api\_endpoint\_regex = 'hrrecruiting/\*';
CloudAppEvents
| where Application == 'Workday'
| where IsExternalUser
| where ActionType matches regex api\_endpoint\_regex
| where IPAddress in (<suspiciousips>) or AccountId in (<suspicious\_emailids>);
| summarize make\_set(ActionType) by AccountId, IPAddress, bin(Timestamp, 1d)

**查询2：与面试相关的可疑邮件与Teams通信**

//Email communications
EmailEvents
| where SenderMailFromAddress == "<suspicious\_emailids>" or RecipientEmailAddress == "<suspicious\_emailids>"
| where Subject has "Interview"
| project Timestamp, SenderMailFromAddress, SenderDisplayName, SenderIPv4, SenderIPv6, RecipientEmailAddress, Subject, DeliveryAction, DeliveryLocation

**查询3：新员工入职后源自已知恶意IP的薪资操作**

CloudAppEvents
| where Application == "Workday"
| where AccountId == "<NewHireWorkdayId>"
| where ActionType has\_any ("Add", "Change", "Assign", "Create", "Modify") and ActionType has\_any ("Account", "Bank", "Payment", "Tax")
| where IPAddress in ("<suspiciousIPs>")
| summarize make\_set(ActionType) by IPAddress, bin(Timestamp, 1d)

攻击者在进化，他们开始把AI用在社工钓鱼，把招聘网站当作情报搜集点。我们不能再把人力资源流程仅仅看作是“业务”，它同样是攻击面的一部分。这件事说难也难，因为它需要安全与业务部门的深度协作；说简单也简单，关键在于你是否愿意在“正常”的流程中，多花功夫去寻找那些细微的“不正常”。

---

### 参考资料

[1] https://www.microsoft.com/en-us/security/blog/2026/04/21/detection-strategies-cloud-identities-against-infiltrating-it-workers/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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