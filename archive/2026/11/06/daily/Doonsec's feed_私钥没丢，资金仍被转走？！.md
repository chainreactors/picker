---
title: 私钥没丢，资金仍被转走？！
url: https://mp.weixin.qq.com/s/sF1ExD6RCWSN1Q2T83qqew
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:58:11.177308
---

# 私钥没丢，资金仍被转走？！

# 私钥没丢，资金仍被转走？！

原创

BlockSec
BlockSec

BlockSec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ibKZs4HxyqtTUJibmiaaDgadp610m0ahHpndAtK8Y4B9dAlMY539eDia191DN7avhWFrMQOav9ny1Miaic7wEibdzWibq3Jjev4oz6kds90U3A4sicM/640?wx_fmt=gif&from=appmsg)

一笔付款，身份核验通过了，审批完成了，签名也有效。资金就一定安全吗？

未必。

从去年 BigONE 失窃约 2700 万美元、Bybit 遭遇约 15 亿美元攻击，再到今年 Binance 约 63 亿美元资产遭到非法转移，这些事件共同揭示了一个问题：攻击者未必需要直接窃取私钥，也能转走资金。

所以，机构需要追问的不只是“私钥有没有保管好”，更要问：这笔付款为什么成立？实际签署了什么？谁能改变签名规则？执行后，系统又如何判断付款是否完成？

BlockSec 将沿着一笔付款从发起到结算的路径，结合公开案例梳理容易被忽视的授权风险。

后续还会更新技术系列文章 《Beyond Secure Storage》 将进一步讨论两条攻击路径：一类是无需取得私钥，也能滥用系统的签名能力；另一类是通过密码学实现缺陷预测或恢复密钥，从而进行攻击。

**一笔付款可能在哪些环节被劫持？**

通过钱包执行一笔付款，通常涉及四个环节：付款依据与授权、交易构造与核验、签名授权与密钥使用，以及执行与结算。

![](https://mmbiz.qpic.cn/mmbiz_png/2ibKZs4HxyquQvCrzsibMAQe92GwmciavBtLqdSDyWXOtXK5X8UuFM44BibSoVVXiaQIZYLKN6APdJ3Rrpdf1AaGqMP8sX7sicwhcVo72e4NKiaEgE/640?wx_fmt=png&from=appmsg)

图 1：付款全流程示意图

**1. 付款依据与授权**

这笔钱，本来就该付吗？

如果是客户发起提现，那么平台需要确认用户的身份、账户的可用余额，以及交易是否符合业务规则。

如果是机构内部调拨，也需要相应的资金管理批准。

也就是说，无论是外部提现还是内部调拨，都需要先校验付款的真实性，再进行签名。

但如果攻击者改写了账户记录或风控逻辑，系统也可能“按流程”批准一笔本不该发生的付款。

例如，2025 年 7 月 16 日 BigONE 披露了未经授权的热钱包资产移动，公布估计损失约为 2700 万美元。这一事件中，攻击者就是通过篡改账户和风控系统的运行逻辑，从而在私钥未泄漏的情况下转出资金。

这里的关键是：签名之前，用于判断“该不该付款”的依据已经被改变了。

那么，对支付机构而言，仅确认请求来自某个内部服务还不够。每笔付款都应能追溯到独立可核验的客户指令或资金管理决策；还需要检查，同一个失陷身份能否同时伪造请求、修改记录，并改变批准规则。

**2. 交易构造与核验**

你看到的，就是你本来要签署的吗？

一笔付款获批后，系统还需要将收款地址、金额等业务信息转换成可供钱包签署的交易数据。

如果这一过程被篡改，界面显示的可能是“转账”，实际送去签名的却是“变更钱包控制权”。

那么，你的签名就可能在你不知情的情况下，授权攻击者接管钱包，而你以为自己只是批准了一笔转账。

例如，2025 年 Bybit 遭遇的约 15 亿美元攻击，就暴露了这一风险。

Bybit 原本计划将 ETH 从冷钱包转入温钱包，但攻击者通过失陷的 Safe 界面误导签名者，使他们以为自己在确认正常转账，实际却签署了一笔会改变钱包控制逻辑的恶意交易。

攻击者凭有效签名完成了钱包实现的替换，随后利用新的控制逻辑转移资产，无需为后续每笔提款重新取得原所有者批准。具体链上过程可参见[《Bybit被盗事件深度解析》](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247488651&idx=1&sn=c0fa63c0cfdf25d2a5d303acbd48b144&scene=21#wechat_redirect)。

这个案例说明：

签名前的核验必须针对实际送去签名的完整交易及其执行效果，不能只依赖操作界面的展示。即使有多位签名者，如果他们都依赖同一个失陷视图，也未必能够发现问题。

另外，资金调拨、钱包升级和提款权限变更，也应设置各自的授权要求，避免一次普通转账的审批被用于改变钱包控制权。

**3. 签名授权与密钥使用**

谁能签名，谁又能改变签名规则？

一个身份即使不能直接签名，也可能通过修改策略或替换运行代码获得同等能力。

因此，保护资产密钥的管理权限同样需要审查。

2026 年 3 月，Resolv 发生安全事件，根据其官方复盘指出，攻击者多次尝试获取签名能力受阻后，利用高权限角色修改密钥访问策略，取得签名权限。随后，攻击者通过两笔非法交易铸造了 8000 万枚 USR。

再例如， 2026 年 10 月 Binance 遭受 63 亿美元未经授权转移事件中，攻击者通过失陷员工设备和内部 AI 工具进入钱包工程师的设备，随后利用窃取的容器部署令牌执行恶意操作，取得内部钱包签名服务的未授权访问，绕过正常提现流程发起交易。

这两个案例虽然入口不同，却指向同一个问题：

保护密钥不仅要控制谁能够直接使用密钥，更要控制谁能够改变密钥的访问策略、签名服务的运行环境，以及授予其他身份签名权限。

那么支付机构则需要同时核验：

谁能调用签名接口，谁能授予调用权限，谁能部署或修改签名服务。

另外，业务批准、密钥使用与管理变更之间的分离，还必须经得起高权限身份失陷的考验。

**4. 执行与结算**

签完以后，风险就结束了吗？

不一定，签名完成后，交易何时执行、能否撤销，仍然关系到资金安全。

风险点一：已签交易的执行能力可能被保留

交易签好了，却还没有执行。这份签名以后还能用吗？

在某些机制下，可以。业务请求被取消，也不代表已经签署的交易会自动失效。

2026 年 4 月 1 日 Drift Protocol 事件中，攻击者利用 Solana 的 durable nonce 机制，使预先签署的交易不受普通交易短期有效窗口的限制，在相关 nonce 尚未被消耗或推进的情况下，保留了后续提交执行的能力。

具体可见[《Drift Protocol 事件详细复盘》](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247491717&idx=1&sn=c9de74c09dd131b135f9d4198b351a3e&scene=21#wechat_redirect)。

所以，机构需要明确的是，当业务请求被取消或发现异常后，系统通过什么机制使尚未执行的已签交易失效，以及谁有权执行这些操作。

风险点二：内部资金异动被误读，触发额外退款

2026 年 9 月，Chainflip 在 Tron 网络上发生安全事件。攻击者提交平台已经签署的内部资金归集操作，并附上恶意构造的交易备注（memo）。

于是，系统错误地将其识别为一笔新的客户兑换，与攻击者正常获得的流动性提供者（LP）提款叠加，造成约 73.64 万 USDT 的重复支出。

这个案例说明，链上确实发生了一笔转账，并不意味着它就对应一笔新的客户付款，更不意味着平台应据此发起退款。在支付或退款前，系统还需要核实资金来源、业务类型，以及是否已经履行过相应的付款义务。

**你的支付系统，真的足够可靠吗？**

回看这些案例，资金损失可能发生在签名前，也可能发生在签名后。有效签名本身，无法替机构回答付款是否有业务依据、操作是否符合审批意图，以及付款是否已经完成。

因此，对支付机构而言，有价值的安全评估应给出具体答案：

* 一笔付款能否追溯到独立可核验的业务依据？
* 审批与实际签署的完整操作是否一致，包括权限变更和附加交易？
* 某个运行或管理身份失陷后，是否仍有独立控制阻止或限制支出？
* 暂停提现后，已有签名和链上授权是否仍可使用，如何确认遏制已经生效？

这些问题也不能只靠一次配置检查解决。

一方面，软件更新、权限调整和业务变化后，可能会改变原有的安全边界，那么就需要重新检查安全措施是否仍然有效。

另一方面，AI 工具的使用还可能引入新的攻击面，那么机构就需要通过持续监控和应急演练，检验能否及时发现异常，并在关键身份或生产环境失陷后限制资金继续流出。

那么围绕上述问题，BlockSec 将举办 「AI 时代的资金保卫战」线上研讨会。会上将结合近期交易所与支付企业的安全事件，讨论攻击者如何通过人员、工具和生产环境触及资金操作，以及机构如何改进威胁发现、授权核验与应急处置。

邀请嘉宾：

* 周亚金：香港中文大学副教授，BlockSec 联合创始人兼 CEO
* 吴磊：浙江大学副教授，BlockSec 联合创始人兼 CTO
* 姜木慧：BlockSec CSO

活动时间：2026 年 11 月 11 日（周三）19:00

活动形式：线上研讨会（腾讯会议）

参会福利：现场将选出 2 家参会机构，赠送免费初步安全体检。

不要等到资金损失发生，才重新审视安全防线。提前发现风险，才能真正守住每一笔资金。

欢迎支付机构的管理者、安全负责人及技术团队参与，共同审视资金流转中的安全盲区。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4HxyquYBN26jZc2IRSibCQhPA27ibmJkRvlrg3tCibwJZsichgnexYQVdOAqDQa8oXian1PxibvAEVshZ0YW6iawrLQyFHNZz9BdB0Wibia97MI/640?wx_fmt=png&from=appmsg)

图 2：线上研讨会报名二维码

---

关于BlockSec

BlockSec 是全球领先的区块链安全和合规公司，于 2021 年由多位业内知名专家联合创立，致力于将前沿安全研究转化为产品与服务，构建安全、易用的 Web3 世界。

BlockSec 面向 Web3 企业、金融机构，及支付机构，提供一站式安全与合规解决方案。服务涵盖智能合约、区块链及钱包安全审计、端到端支付安全评估、渗透测试、攻防演练与应急响应演练，以及持续监控与响应，帮助客户保障资金与数据安全、提升业务韧性。

旗下产品涵盖实时威胁监测与攻击阻断平台 Phalcon Security、加密资产反洗钱与反恐怖融资（AML/CFT）合规平台 Phalcon Compliance、非法资金流入监测与预警平台 Phalcon Network、链上资金追踪与调查平台 MetaSleuth，以及区块链交易分析工具 Phalcon Explorer 等，覆盖风险预防、实时防护、合规风控与事后调查等关键环节。

目前，BlockSec 已累计服务全球逾 1000 家客户，包括 RedotPay、Interlace 等支付机构，Coinbase、Cobo、Uniswap Foundation、Compound、MetaMask、Bybit、Mantle、Puffer、FBTC、Manta、PancakeSwap 等 Web3 知名企业与项目，以及联合国、香港证监会（SFC）、PwC、FTI Consulting 等国际组织、监管机构及专业服务机构。

官网：https://blocksec.com/

领英：https://www.linkedin.com/company/blocksec

Twitter：https://twitter.com/BlockSecTeam

推荐阅读 👇

[![]()](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247493089&idx=1&sn=265eec25baf3191bffec2e89a45f5a62&scene=21#wechat_redirect)[![](https://mmbiz.qpic.cn/mmbiz_jpg/icl4OTbk4icTJKnQAjhicg47N8sLY3SKzqlEcnuEf3pYzPTIqpar2ibkeSeCvjqQsKrLwZwWyTcAXIazKXLQIXEchQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247490504&idx=1&sn=ed76941ba8ee144bdd12cb0ddb7df70c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ibKZs4Hxyqsiamt2u3ialgcibWKibaAIbWnO0MSdKWBTsPDXDricS6OXDo9zojTxUgN7Go5prd4vamicVsLWjrI7njG3f6EK5wkTJzlInZQmzOHIU/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyMzI2NzIyMw==&mid=2247493089&idx=1&sn=265eec25baf3191bffec2e89a45f5a62&scene=21#wechat_redirect)

#BlockSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icl4OTbk4icTKWV4NZYNjUicibdl9UQ4HibVfGa4a6ypSMKArRmWBI3Nibibicuo7YJbQibOC8XKvSMJXYGRFWIz3hsvvfA/0?wx_fmt=png)

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