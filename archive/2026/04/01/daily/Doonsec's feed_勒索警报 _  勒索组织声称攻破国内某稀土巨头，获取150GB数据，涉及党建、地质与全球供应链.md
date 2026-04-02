---
title: 勒索警报 |  勒索组织声称攻破国内某稀土巨头，获取150GB数据，涉及党建、地质与全球供应链
url: https://mp.weixin.qq.com/s/23U3e_B1OFCb5bn2fIs_yw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:25:53.999803
---

# 勒索警报 |  勒索组织声称攻破国内某稀土巨头，获取150GB数据，涉及党建、地质与全球供应链

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/m7SEcCOKaqZciaAq30ZXDf7rE4mysXbG90DBiaQ6VRDCkf6XVxGtC5y4KFhvDCgLQyRdjpvaSNxpxk8TddvLfwmNEAoDibsdOic43uIjjaxibL1k/0?wx_fmt=jpeg)

# 勒索警报 | 勒索组织声称攻破国内某稀土巨头，获取150GB数据，涉及党建、地质与全球供应链

原创

懒虫零信噪
懒虫零信噪

懒虫零信噪

![]()

在小说阅读器中沉浸阅读

📌 事件摘要

2026年4月1日，懒虫零信噪监测到，某勒索软件组织在暗网发布针对中国某稀土与钨业巨头的攻击声明。该组织宣称已窃取超过150GB的核心业务数据，并以20枚比特币的价格进行勒索。此次泄露的数据不仅涵盖ERP、HR、研发等商业机密，更罕见地包括了党组织记录、地质勘探数据及全球供应链信息。该组织还留下了联系邮箱与Session ID，表明其正在进行谈判或准备公开数据。

![](https://mmbiz.qpic.cn/mmbiz_png/m7SEcCOKaqa5WlWMs5IWI7BZssricRV4SuDSNQRxuCe3M8ibvvLRhcmBpdXD8NuIfsXMfeas2ibQm71MREoBSL1J0SGSibYcF8GEDu41Hp3MdEo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/m7SEcCOKaqZlJCC4v5ia7NbT7SBZCKLibXY3mJV68869AyLjlVRBcdokIy7UagTFYYo6bqib18UtpgFcEdGQdyGZt9hzQIcpbDykGkicozYBQuo/640?wx_fmt=jpeg&from=appmsg)

📡 攻击事件核心情报

该勒索组织在声明中高调宣称对该企业的“全面基础设施入侵”（Full Infrastructure Compromise），并列出了详细的被盗数据清单。数据格式主要为SQL备份文件（.bak），表明攻击者已深入企业核心数据库层。

📉 财务与市场背景

公司估值：约135.6亿美元

数据规模：超过150GB，包含完整访问权限

数据类型：ERP (Dynamics AX)、HR、实验室信息管理系统 (LIMS)、党委会记录、ESG、供应链管理 (SCM)

💰 勒索与联系信息

勒索金额：20 BTC

售卖状态：独家出售

📂 涉密数据深度解析

此次泄露的数据目录详尽到令人咋舌，攻击者将数据分为三大类：高容量战略资产、核心运营与制造数据库、企业政治与基础设施模块。

1. 高容量战略资产 (Over 5GB)

地质与资源数据：包含名为ecology202306091936.bak的文件（38GB），涉及地质调查、矿山测绘及环境资源监测。这是矿业与材料企业的核心命脉。

中央数据仓库：QL\_DataCenter\_backup (15.8GB)，聚合了所有子公司的数据流。

质量控制档案：QcAdmin20240109.bak (15.5GB)，包含所有技术规格和产品测试历史。

核心HR数据库：MCHRDB20260322000000.BAK (14.7GB)，包含全体员工的全量个人身份信息（PII）和薪资信息。

ERP蓝图：11MicrosoftDynamicsAX\_model.bak (9.07GB)，包含业务逻辑和财务结构蓝图。

单点登录（SSO）枢纽：QL\_SSO\_backup (5.38GB)，包含用户凭证和网络访问令牌，这是后续横向移动的关键。

2. 核心运营与制造数据库 (500MB - 5GB)

实验室信息管理：QL.LIMS.JL\_backup (2.14GB)，包含化学配方和合金配比，这是企业的核心技术机密。

生产调度：QL\_Scheduler\_backup (1.46GB)，包含主生产计划和工厂产能规划。

供应链管理：SCM\_DB\_backup (906MB)，包含物流合同和运输路线。

3. 企业、政治与基础设施模块 (Under 500MB)

党组织记录：ql\_party\_yj\_backup (334MB)，包含党委会议记录和政治领导层信息。这是中国大型企业特有的敏感数据，其泄露可能引发严重的合规与政治风险。

数字文档审批：XTC\_WorkFlowTest (330MB)，包含数字文档审批流程和电子签名逻辑。

董事会材料：QL\_Board\_backup (288MB)，包含董事会会议材料和高管决策记录。

⚠️ 风险预警与安全建议

此次事件不仅是对企业的打击，更是对整个高端制造与材料行业的警钟。勒索软件攻击已从单纯的“加密勒索”进化为“数据窃取+双重勒索+政治敏感信息施压”。

供应链风险排查：由于泄露数据包含详细的供应链管理（SCM）和物流信息，上下游合作伙伴应立即排查账户安全，防范冒充高管或合作伙伴的钓鱼攻击。

核心机密保护：涉及化学配方、合金配比及地质数据的文件一旦流入竞争对手手中，将造成不可逆的经济损失。建议企业立即启动技术秘密保护程序。

内部权限审计：攻击者获取了SSO凭证和ERP蓝图，说明内网权限管理可能存在重大漏洞。建议立即重置所有核心系统密码，并启用多因素认证（MFA）。

政治与合规风险：党组织记录和员工敏感信息的泄露可能违反《个人信息保护法》及国家安全相关法规。建议企业立即向网信办及公安部门报备。

免责声明：本文基于暗网及公开渠道监测到的黑客组织声明整理，所涉内容均为单方面宣称，未经证实且不具备法律效力；内容仅作安全趋势分析与风险预警参考，不构成事实认定或政策建议。请勿尝试联系相关组织或参与任何形式的“响应行动”，以免触犯法律或危及人身安全。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vMByMwrmicRJuiblD41h1JXI8fg8OIgE0Doz0GqFMeoGxmZI0q4XfxFmM3YM25Q3mrKy7Up92YOL1XpEI3S3xFgg/0?wx_fmt=png)

懒虫零信噪

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vMByMwrmicRJuiblD41h1JXI8fg8OIgE0Doz0GqFMeoGxmZI0q4XfxFmM3YM25Q3mrKy7Up92YOL1XpEI3S3xFgg/0?wx_fmt=png)

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