---
title: 4月全球网络安全焦点事件TOP10
url: https://mp.weixin.qq.com/s/pJm7ZQ6Il8Rnq27pvLSxWw
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:27:10.767186
---

# 4月全球网络安全焦点事件TOP10

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pYZtDTxxdanTtk1wd2IgqH6o07qegBQibB3UlbFcKOJNTgU7LBfDkvmjrT9m23IO7qicjiaTbV76ReUnzGtWS425O0huibtyhV6u101wnfvdKc/0?wx_fmt=jpeg)

# 4月全球网络安全焦点事件TOP10

原创

Cismag
Cismag

信息安全与通信保密杂志社

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**前言**

![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdbITUWKPYovMia1pBo6s2ZznxNQ9b7cOPdJFEZylQqiaL2hK5Tg4iaicfzHNnNCS3o6VLP2qMEOCpzibgOIIdibrbMV80CcuDpsDtkFw/640?wx_fmt=png&from=appmsg)

4月以来，全球网络安全威胁急剧升温。AI工具违规使用致涉密信息泄露，供应链投毒事件波及大量AI应用，FBI内部系统遭入侵，欧盟委员会超300GB数据失窃。伊朗系黑客发起大规模网络攻势，量子软件供应链暴露出547个漏洞。攻防并进，美军大幅加码网络战力，北约完成4000余人规模年度网络防御演习，抗量子加密无人机也首度试验成功。以下是梳理出的4月份全球网安十大事件，带你了解全球最新网络安全威胁态势。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pYZtDTxxdaAuVdc8x2z9ibjuztEs8CT9qgTwZSA9vpyGfwzgDKujr6LkrQ0icFIuVGbfSajvrIBeZOFCkHzmcYTucemdk5HQX86hTgP6icX2E/640?wx_fmt=png&from=appmsg)

**01**

**国家安全机关通报AI工具使用导致涉密信息泄露事件**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pYZtDTxxdb6zXn0ia16KTnXNbKFMMSTAic4qyOxjSJ9KOKhUfaMWp10jeayoxG26HwibPSqWlpje31HbF5TFwtBAhtwyG1E5nVogO4xk87RcI/640?wx_fmt=jpeg)

4月，国家安全机关通报了多起因违规使用AI工具导致的失泄密案例。其中，某科研机构研究人员使用AI应用软件擅自上传核心数据及实验成果，导致该研究领域涉密信息泄露。另一案例中，某机关工作人员违规使用互联网扫描软件扫描涉密会议纪要，文件被自动备份至网盘，其后网盘账号密码遭暴力破解，攻击者获取了其在3年间扫描的127份涉密文件，经境外社交媒体传播造成严重后果。通报指出，AI工具通常会自动收集用户输入信息用于自主学习，各环节均面临泄露风险，必须牢记“涉密不上网、上网不涉密”的基本原则。（相关阅读：1.[专题•特别策划｜全球人工智能治理：多元主体结构与互动机制](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247604529&idx=1&sn=2f6b996e6038bb67569e09f5e3f10f06&scene=21#wechat_redirect)；2.[专题·人工智能｜生成式人工智能对网络安全监管的挑战及应对](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247600022&idx=1&sn=af738d3f3b91240b1649d611b3e50967&scene=21#wechat_redirect)）

**02**

**多起供应链投毒事件安全风险分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pYZtDTxxdZQdWHbcCs4WBCbibtqwPBtrVk5vHUWzeMcUgWja6uGeBK18NFVLhxf0RxpdXC9oN01OF8SIXPia1vOugoGWrvcNlu8xtIJvEfXY/640?wx_fmt=jpeg)

4月，国家网络安全通报中心监测发现，近期集中爆发多起供应链投毒攻击，目标包括API工具Apifox、Python库LiteLLM及HTTP库Axios。其中Axios投毒因OpenClaw等大量AI应用依赖该库，风险沿依赖链蔓延。三起事件呈隐蔽性强、范围广、危害高、传播快等特点，可致凭据窃取、远程代码执行和数据泄露。风险分析：攻击聚焦高权限开发人员；路径隐蔽（账号劫持、上游污染等），无需交互即可扩散；单次投毒可引发横向移动与二次投毒；恶意代码采用混淆、反调试等手段，检测阻断难度大。防护建议：仅从官方渠道下载安装，核对校验信息；为不同项目搭建独立环境，避免暴露开发运维环境，不随意执行未知命令；关注安全预警，及时打补丁或回退稳定版本，并清理本地缓存。

**03**

**美国能源部太平洋西北国家实验室部署MERU智能化网络防御系统**

![](https://mmbiz.qpic.cn/mmbiz_jpg/1pYZtDTxxdaW4smAoy4VSuMUMvBm3mKQ8hOvgZDTyn4TPH0mrG7LeYQF8MyVA6jTef4ictFibwWy0wKO7m8AjKEk8LnlxjwyGgUaKGGibXibiahM/640?wx_fmt=jpeg)

4月，美国能源部太平洋西北国家实验室成功部署基于AI的“多模态实体关系统一”（MERU）网络防御系统。该系统融合图论与多源威胁情报，将包括漏洞数据库、攻击模式库及MITRE ATT&CK在内的数据进行统一分析，构建动态风险视图。该系统可将海量情报转化为可执行防御策略，帮助安全团队提前识别高优先级威胁并应对零日攻击。初步应用表明，该系统显著提升了威胁识别效率与前置防御能力，推动网络安全向智能化、预测性防御演进。（相关阅读：[数智驱动的网络安全主动防御体系能力生成和策略研究](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247603456&idx=2&sn=0162af5b2e003d248a6badba99a6a6d3&scene=21#wechat_redirect)）

**04**

**FBI监控系统遭入侵，被定为重大网络安全事件**

![](https://mmbiz.qpic.cn/mmbiz_jpg/1pYZtDTxxdbJ0pITMtPhwePkxXadnLicKicbxlQ0Q6XNmGibObpwuZ5k4v8P4PqPPXYMX4BEBVic4icXcCG8BJMZ1XA7rdcU5GayJ81jTBQCticHk/640?wx_fmt=jpeg&from=appmsg)

4月，FBI宣布其内部监控管理系统遭网络入侵，依据联邦信息安全现代化法将事件定为最高级别的重大网络安全事件。通过该事件发现，黑客侵入非密内部网络，获取通话元数据、监控记录及涉案人员个人信息，涉及FISA授权监控相关的DCS—3000系统，虽未截获通话内容，但可能暴露卧底身份与调查线索。黑客利用商用ISP供应商基础设施绕过边界防御，美方称攻击手法与所谓“Salt Typhoon”组织相似。（相关阅读：[基于标识密码的视频监控系统安全加固方案](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247588229&idx=1&sn=db9804cb07fb73a68306ea150d44b8bb&scene=21#wechat_redirect)）

**05**

英国与捷克公司合作推出全球首款抗量子加密无人机

![](https://mmbiz.qpic.cn/mmbiz_jpg/1pYZtDTxxdZRvVY9FTO5hB6sT7Q0e27sPic4CH7mXVTQjnhqmyp9WRvXb9ZgaMpJCZMa0c067jiaBGuquAxDtSOdHGxRzQeibJia62w1ibn2EIUo/640?wx_fmt=jpeg)

4月，英国网络安全公司Post-Quantum与捷克STV集团合作完成了“全球首批抗量子安全无人机”试验。该型无人机将STV集团经过实战检验的无人机平台与Post-Quantum公司的专利加密及无线电技术相结合，并采用了已有数十年历史的Classic McEliece加密算法。在过去将近五十年间，Classic McEliece算法从未被攻破，但由于其密钥尺寸过大，过去认为会压垮无人机弱信号链路，因此此前无人将该算法部署到无人机上。对此，Post-Quantum和STV公司合作开发了一种新架构，使Classic McEliece算法能在低带宽条件下正常运行，从而为飞行过程中的视频馈送、图像及任务数据提供安全保护。这两家公司表示，未来将把该型无人机的抗量子安全标准配置扩展至其他地面及海上军用系统。（相关阅读：[无人机安全通信协议研究综述](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247589197&idx=4&sn=8176931260645902054373cc8c5c0223&scene=21#wechat_redirect)）

**06**

**欧盟委员会发生大规模数据泄露**

![](https://mmbiz.qpic.cn/mmbiz_jpg/1pYZtDTxxdbCyQnXyPyInxtZxVTESR5JztqrCicjo33aqdpwZvjiaCQCw4WdiauY0BJhM9STyZe0qq9OGKlupsicxalTorAa630sC9vk41zCyuU/640?wx_fmt=jpeg)

4月，欧盟计算机应急响应小组（CERT-EU）确认，欧盟委员会用于托管Europa.eu公共网站平台的亚马逊网络服务（AWS）云账户后端环境于3月24日遭黑客入侵，超过300 GB的数据被窃取。黑客组织TeamPCP于3月19日对Aqua Security公司的Trivy漏洞扫描器实施供应链攻击，在正常软件更新渠道中植入恶意版本，导致欧盟委员会下载了受感染版本的Trivy软件，从而泄露了AWS应用程序编程接口（API）密钥。TeamPCP组织利用该密钥创建并附加新访问密钥，由此获取了其他关联AWS账户的控制权，并使用TruffleHog工具扫描更多保密信息并验证AWS凭证，以实现横向移动。被盗数据涉及Europa托管服务下71家客户，包括42个欧盟委员会内部机构及至少29个其他欧盟实体，内容包含姓名、电子邮件地址、用户名等个人信息，以及包含用户原始提交内容的自动退信通知等。被盗数据已于3月28日被公布，欧盟委员会随后立即撤销了受损账户权限、停用并轮换相关凭证，通知相关数据保护机构，并强调此次事件未影响其内部系统。（相关阅读：[基于行为分析的内网数据防泄露场景研究与技术实现](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247586063&idx=1&sn=1a4c017cd467963c4633a545fb495242&scene=21#wechat_redirect)）

**07**

**伊朗系黑客针对以色列、阿联酋、美国发动大规模网络攻势**

![](https://mmbiz.qpic.cn/mmbiz_png/1pYZtDTxxdZ2ibUUZ32X3OKuxr4gEqBzWFXdVZdqIlKFtVChIA267ykwLUdaFWjDnL6QVsicq0OBU1g7ssPgfLy7H0JIIMJQgicLW4MImiaq998/640?wx_fmt=png&from=appmsg)

4月，中东冲突背景下，伊朗关联威胁行为者正持续针对以色列、阿联酋发动Microsoft 365密码喷洒攻击。Check Point报告显示，攻击分三波进行，已致以色列300多个、阿联酋超25个组织云环境受损，目标涵盖政府、能源、科技等领域。攻击通过Tor节点实施，手法与伊朗Gray Sandstorm组织高度吻合。同期，伊朗勒索软件团伙Pay2Key于2026年2月底重启行动，攻击美国医疗机构。该团伙升级攻击技术，利用远程工具入侵、禁用防御、部署勒索软件并清除痕迹。此外，亲伊朗的BQTlock也持续针对美、以为目标。网络安全机构指出，伊朗正将勒索软件用于网络报复，模糊网络犯罪与国家支持破坏的界限。建议相关机构启用MFA、强化日志审计与地理访问限制以防御。（相关阅读：[两场局部冲突中黑客群落行为与动因研究](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247591771&idx=2&sn=d22d4f4089b593d0c38db3aacf7b57df&scene=21#wechat_redirect)）

**08**

**量子模拟器惊现547个漏洞，量子软件供应链安全拉响警报**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pYZtDTxxdYUYiciae1dczTCsOq9xyR3b3uZRs7seNcjviaZJPT2Gf0CK11CbicL7OrpPuwnQ7gTGD5Copyic3Mv4dBuOo4WnBUp5TQjQNHWnLe0/640?wx_fmt=jpeg)

4月，橡树岭国家实验室团队完成对45个开源量子计算模拟器的全面安全审计，共发现547个安全漏洞，暴露出量子软件底层经典代码的严重安全隐患。本次审计覆盖22家机构的主流框架，借助COBALT QAI与Z3求解器开展静态分析，确认40个严重漏洞、492个高危漏洞、15个中危漏洞，包含QASM注入这一新型量子专用攻击向量，可被用于操控量子电路。审计发现，9个框架获满分安全评级，而Qiskit Aer、Cirq等知名框架评分为零，安全水平差异悬殊。研究首次证实漏洞可跨平台传播：IBM Qiskit Aer的缺陷通过集成代码，转移至橡树岭国家实验室的XACC模拟器，凸显量子软件供应链高风险特征。同时确定32量子比特为关键阈值，超出后漏洞链显著增多，系统越界、崩溃风险剧增。此次审计揭示量子计算领域长期忽视经典软件安全的短板，研究团队呼吁全行业强化代码审查、漏洞扫描与渗透测试，尽快建立统一安全标准，防范供应链风险传导至国家关键基础设施。

**09**

**美国国防部加码网络与AI战力建设**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pYZtDTxxdZjHmTiaXZwGGjNTN4MjJRjKOVwfmWIqwTygqXlJwRqhqevMjtL5Nic7923bL1k9kOCSboa7THe79nupgmicR8l5cATv5T3VErdek/640?wx_fmt=jpeg)

4月，美国国防部高层在国会听证会上表态，全力支持白宫1.5万亿美元年度国防预算申请，将网络部队改革、全域数字作战能力升级作为核心支出重点。五角大楼官员指出，全球网络威胁已从数据窃取转向破坏性前置部署，大国攻击性网络军力持续提升，美军网络作战频次同比增长25%。本次预算单列205亿美元专项网络经费，用于军用网络防护、境外网络对抗、全军零信任架构升级，同时配套585亿美元AI及联合作战指挥项目，联动无人装备、信息战技术，深度融合网络作战与常规军事行动。该预算大幅加码国防网络安全，与民用网络预算缩减形成反差。美军同步推进网络司令部2.0重组改革，理顺岗位体系、强化军种协同。国会质疑现有架构权责交叉、高端网络人才流失严重，政府人员薪资不及私企。美方表示将打通部门壁垒、统筹威胁情报与攻防部署，依托AI弥补人力缺口，扩充文职队伍、深化产学研合作，全面适配大国对抗下现代化网络威慑与实战战备需求。（相关阅读：1.[海外研究 | 欧盟《人工智能法案》解读及建议](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247603293&idx=1&sn=e416bbc3bd3ed77de73d97b98a8f4392&scene=21#wechat_redirect)；2.[东盟国家人工智能发展战略特点及其治理框架分析—基于信息安全治理视角](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247601028&idx=1&sn=afb54529a10811b581f2ca39e2788dca&scene=21#wechat_redirect)）

**10**

**北约举行全球最大规模年度网络防御演习“锁定盾牌”**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pYZtDTxxdaY9ibJjEm8TicxqIdyUl8lhiahxvBuPBibulFrc1z290d6Zk3T0q4Pr0icm2nArzic8eQopQia9uUUp6eibmstYTQG2MNePFRRqwPn9nI/640?wx_fmt=jpeg)

4月，北约网络防御合作卓越中心（CCDCOE）在爱沙尼亚首都塔林启动了2026年度“锁定盾牌”（Locked Shields）网络防御演习。此次演习汇集了来自41个国家的4000余名网络防御人员，旨在强化各国国家系统和关键基础设施抵御复杂网络威胁的能力。此次演习以大规模网络冲突为背景，16支参演队伍扮演多国快速反应团队，协助虚构盟国Berylia应对持续网络攻击。在为期两天的演习中，参演方需防御约8000次针对电网、5G网络、卫星及作战管理系统等模拟国家基础设施的实时网络攻击。除技术防御外，此次演习还纳入了战略传播、国际法、数字取证及国家层级决策等非技术挑战，并首次引入了为选举系统提供网络防御的场景。西门子、Mattermost和Bitdefender等100多家企业为此次演习提供了支持，包括提供关键技术能力以及搭建和运行复杂的演习环境等。

**相关阅读**

**[1月全球网络安全焦点事件TOP10](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247603847&idx=1&sn=19b8baa19df674524daac468c2501ba3&scene=21#wechat_redirect)**

[2月全球网络安全焦点事件TOP10](https://mp.weixin.qq.com/s?__biz=MzkwMTMyMDQ3Mw==&mid=2247604289&idx=1&sn=3b19a8425fbdccb0e93cfae2f2ff94fd&...