---
title: 每周网安态势概览【20260712】028期
url: https://mp.weixin.qq.com/s/ZZtLUi2hlOtya0qFKLpduQ
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:30:05.582740
---

# 每周网安态势概览【20260712】028期

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icUibSUtGFNrp4165U71lPF0WiboFxOe3GdZqPZRl6KEvzsskcIAOOAk70JtnFQO3rkfynSAvwbMHSNg/0?wx_fmt=jpeg)

# 每周网安态势概览【20260712】028期

原创

网空闲话
网空闲话

网空闲话plus

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者按

2026年7月6日至7月12日，网空闲话关注并分享的国际网安领域的热点事件，以及每日国际网络安全态势一览。

![](https://mmbiz.qpic.cn/mmbiz_jpg/0KRmt3K30icUibSUtGFNrp4165U71lPF0WUhVsnWZx85lRod0hxfOAG1ECP6jBOBe3D9Jw1JpDfOfbApuWKZkYqg/640?wx_fmt=jpeg&from=appmsg)

一、威胁行为体

本周威胁行为体活动呈现国家APT持续扩张、勒索软件生态专业化、司法追责跨国化三大特征。国家层面，中国关联APT UAT-7810利用新LongLeash后门扩充武器库，持续构建ORB网络；朝鲜黑客PolinRider通过恶意npm包和Go模块攻击开发者供应链；伊朗Cavern Manticore使用模块化Cavern平台攻击以色列政府与IT公司，Handala和Ababil of Minab瞄准医疗和物流行业。影响力行动方面，NewsGuard发现Threads上294个虚假女性账号瞄准台湾男性，疑似XX影响力行动；亲俄黑客组织NoName057(16)和Z-pentest持续活跃。勒索软件专业化显著，Gentlemen勒索软件配备定制EDR/AV杀手加速全球攻击，The Gentlemen利用21种远程执行技术加密整个网络，GodDamn利用微软签名驱动攻击美国企业。Armored Likho使用BusySnake窃密木马持续攻击俄罗斯、哈萨克斯坦和巴西政府及能源部门。司法层面，Ryuk成员Vardanyan在美国认罪面临15年监禁，俄罗斯黑客Obrezko从泰国引渡至美国，西班牙逮捕多名亲俄黑客组织成员，FBI提供关键线索。

**二、战术技术与程序（TTPs）**

本周战术技术呈现EDR对抗白热化、无文件攻击深化、AI驱动钓鱼升级三大趋势。EDR绕过成为核心战场：The Gentlemen利用ktapi.sys漏洞禁用EDR并读写Windows内核内存，配备定制EDR/AV杀手加速攻击；GodDamn使用PoisonX微软签名驱动禁用防御；SindriKit 1.3.0滥用调用栈欺骗绕过EDR检测；SilverFox将ValleyRAT升级为八阶段恶意软件链，最终植入内核级Rootkit。无文件与隐蔽技术持续进化：APT-C-20将Shellcode隐藏在PNG图片中启动无文件C#后门；Fancy Bear利用LSB隐写术和反射加载部署木马；Turla的Kazuar后门利用DLL侧加载和PowerShell加载器实现隐蔽执行；进程参数投毒技术利用Windows启动数据隐藏Shellcode。AI驱动攻击方面，Forg365钓鱼平台结合AI与AiTM技术窃取Microsoft 365账户，威胁行为者冒充30余品牌招聘面试窃取Google凭证。破坏性后门GigaWiper集成磁盘擦除、虚假勒索和间谍功能，具备破坏与加密双重能力。RedHook安卓木马滥用ADB无线调试获取Shell级访问权限，新型Linux后门libjson\_script.so.0针对iKuai路由器且VirusTotal零检测。Mandiant发现通过机器DPAPI可恢复活跃ADFS签名密钥，标志凭证保护面临新挑战。

**三、漏洞与代码**

本周漏洞态势高危密集，零日利用加速、供应链漏洞频发、AI框架风险凸显三大特征交织。零日利用方面，Adobe ColdFusion CVE-2026-48282细节公开2小时内遭利用，补丁发布不到两小时即被攻破；Citrix Bleed系漏洞CVE-2026-8451公开24小时内遭利用，CISA将SharePoint CVE-2026-45659等四个漏洞加入KEV目录。AI框架与开发工具风险：IBM发现Langflow 6个严重漏洞含未认证RCE及API密钥跨租户滥用，Google Dialogflow CX漏洞允许攻击者劫持AI会话，Cursor AI编辑器存在操作系统级远程代码执行漏洞。基础设施层面，U-Boot六个新漏洞可让恶意镜像在启动时运行代码，15年历史的GhostLock Linux内核漏洞可提权至root，Januscape漏洞致Linux KVM客户机可崩溃物理服务器。网络设备漏洞严峻：Ubiquiti披露UniFi生态系统25个安全漏洞含多个CVSS 9.9+缺陷，Tenda路由器固件存在隐藏管理员后门，Gitea严重漏洞仅需有效用户名即可绕过认证。此外，Attested TLS漏洞致WhatsApp等应用加密通道遭中间人攻击，Opera GX零点击漏洞允许恶意网站窃取用户数据，多个ModSecurity漏洞可绕过防火墙规则。OpenSSH 10.4发布多项安全修复与后量子密码支持。

**四、安全事件与态势**

本周安全事件呈现医疗行业攻击激增、数据泄露透明度困境、AI赋能攻击加速三大特征。医疗行业成为重灾区：网络犯罪分子涌向医疗保健企业致攻击数量翻倍，AI威胁使第三方医疗供应商成主要目标，半数数据泄露涉及关联企业，Atrium Health支付180万美元和解网络追踪器诉讼。数据泄露方面，埃森哲确认遭威胁行为者888窃取35GB源代码及数据并出售，法国政府通信平台Tchap遭入侵致7.3万用户信息暴露，荷兰Odido电信网络攻击疑有本地同伙参与。日本安全事件密集：住友重工海外集团服务器遭非法访问，KDDI ISP邮件系统遭非法访问，电商Askul因勒索软件攻击全年净亏221亿日元，15岁高中生利用ChatGPT开发恶意程序攻击动漫流媒体服务被捕。AI赋能攻击凸显，单人攻击者利用AI在72小时内攻破某全球企业AWS云环境。执法与行业动态方面，国际刑警组织Operation First Light逮捕5800名网络犯罪嫌疑人，越南逮捕HiAnime动漫盗版服务7名嫌疑人。FortiBleed认证窃取活动被指与INC和Lynx勒索软件团伙关联，The Gentlemen成为6月最活跃勒索软件团伙。工业自动化系统恶意软件拦截率降至三年最低，Qilin、Stormous、World Leaks等团伙在6月攻击多家日本企业及机构。

**五、网络犯罪与暗网市场**

本周网络犯罪与暗网市场呈现数据泄露规模下降、勒索软件持续活跃、执法行动密集三大趋势。数据泄露方面，2026上半年仅1.14亿行记录泄露，同比减43%，但数据泄露透明度仍是网络安全中最棘手的问题之一，多数安全专业人员被施压隐瞒泄露。勒索软件生态活跃，DeadLock勒索软件组织新增11名受害者，The Gentlemen成为6月最活跃勒索软件团伙，Kairos仅凭威胁窃取2TB数据致美国政府部门支付100万美元赎金。执法行动取得重大战果：全球反欺诈行动逮捕5811人，拦截2.93亿美元非法资产；国际刑警组织Operation First Light逮捕5800名网络犯罪嫌疑人；越南警方逮捕7名HiAnime运营者，该站曾是全球最大动漫盗版网站，涉嫌盗播26000部动画获利20.8亿日元。暗网交易方面，FortiBleed窃取英国外交部等机构凭证并出售，威胁行为者888窃取埃森哲35GB源代码及数据出售。犯罪手法创新，卡巴斯基揭露围绕GTA VI的五种诈骗手法包括钓鱼网站、恶意下载与加密货币陷阱。值得注意的是，第三名美国安全专家因帮助Ran被判入狱，凸显内部威胁与犯罪勾结风险。

**六、网络空间政策与标准**

本周政策与标准领域围绕AI治理、隐私保护、网络主权与合规监管四大主线推进。AI治理方面，英国外交大臣称AI风险堪比核武呼吁提前制定安全规则，联合国秘书长呼吁禁止自主武器系统，俄罗斯数字发展部获20项新职能成为人工智能主要监管机构，但美国雇佣黑客提案引发强烈批评。隐私保护争议激烈，欧盟Chat Control监控法案复活投票未达门槛但反对方票数更多仍失败，杜罗夫抨击其为香蕉共和国伎俩；欧洲恢复法律允许大型科技公司扫描CSAM，日本改正个人信息保护法成立但AI开发可免同意提供病历等敏感信息。网络主权与合规方面，欧盟委员会起诉四国未落实NIS2指令，欧盟拟统一年龄限制或致数百万欧洲儿童无法访问社交网络，多国跟进社交媒体年龄禁令合规挑战凸显；俄罗斯政府放弃对外国互联网流量收费计划，但反欺诈包拟恢复短信确认重要操作。军事与网络安全层面，五角大楼网络注册学徒计划开放申请，国际奥委会解除对俄罗斯奥委会禁令，墨西哥新网络安全计划面临世界杯首次真正考验。CISA BOD 26-04重新定义安全领导者漏洞管理指标，OMB M-26-14要求联邦机构优先解决资产可见性，Cloudflare加入英国政府网络弹性承诺计划。

**七、云安全 / 网络资产与基础设施 / AI安全**

本周云安全、网络资产与AI安全领域呈现云原生威胁深化、AI赋能攻击加速、深度可观测性需求凸显三大趋势。云安全威胁方面，LiteLLM代理连接亚马逊Bedrock遭劫持用于门罗币挖矿，CAI云蠕虫感染Kubernetes服务器窃取凭证挖矿并清除竞争对手，单人攻击者利用AI在72小时内攻破某全球企业AWS云环境，标志云原生攻击进入自动化与智能化阶段。AI框架风险持续，Google Dialogflow CX漏洞允许攻击者劫持AI会话并窃取数据，Rogue Agent漏洞可让攻击者劫持聊天机器人，IBM发现Langflow 6个严重漏洞含API密钥跨租户滥用。网络资产与基础设施层面，研究揭示281款免费安卓VPN应用存在流量泄露、明文数据和追踪行为，警报VPN应隐藏流量但多数未能做到。Gigamon强调AI时代需通过深度可观测性填补东西向、加密和云原生流量盲点。工业自动化系统恶意软件拦截率降至三年最低，Q1 2026威胁态势显示防御效能下滑。日本15岁高中生利用ChatGPT开发恶意程序攻击动漫流媒体服务被捕，标志AI工具民主化带来的新型威胁。网络犯罪分子涌向医疗保健企业致攻击数量翻倍，AI威胁使第三方医疗供应商成为主要攻击目标。

![](https://mmbiz.qpic.cn/mmbiz_gif/cdpEKcgoS1BicLZgU8jmicyg91xn76bzlpQheJKKianlFtD313WQNw3uOiadF1ds97PWDvXmQeaW6DnPTDQlnQU32A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0KRmt3K30icVGnSe4zPGUZ2ibceYmDIib04vz21so50Ycia1QhibUCGKKecTyBl99eoCibzVwOANCyosia05JyYzyJdMQ/0?wx_fmt=png)

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