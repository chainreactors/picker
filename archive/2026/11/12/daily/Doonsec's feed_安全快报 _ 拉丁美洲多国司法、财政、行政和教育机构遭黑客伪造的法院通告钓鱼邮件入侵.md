---
title: 安全快报 | 拉丁美洲多国司法、财政、行政和教育机构遭黑客伪造的法院通告钓鱼邮件入侵
url: https://mp.weixin.qq.com/s/so7d1Hbd58IKm3O81jyw_Q
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:04:00.357860
---

# 安全快报 | 拉丁美洲多国司法、财政、行政和教育机构遭黑客伪造的法院通告钓鱼邮件入侵

# 安全快报 | 拉丁美洲多国司法、财政、行政和教育机构遭黑客伪造的法院通告钓鱼邮件入侵

天懋信息

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**本周安全事件速览**

**11月05日-11月11日**

**01**

**拉丁美洲多国司法、财政、行政和教育机构遭黑客伪造的法院通告钓鱼邮件入侵**

![](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibTqYibe6pdNcbwSPjH3qRrmcGuTbVhmicj8oOvfSYVtxkMn5csiciaDn6GARiaicVVUdLko7KZlibx1icOOG300BkZItW2Z8Pa3wAdFaBM/640?from=appmsg)

**简要介绍**

黑客组织APT-C-36（又称Blind Eagle）近期发起新一轮网络攻击，主要针对拉丁美洲的司法、财政、行政及教育机构，使用葡萄牙语和西班牙语书写的法院通知、检察院通告及行政文件等钓鱼诱饵投递远程访问木马。攻击链始于钓鱼邮件：一封包含哥伦比亚司法主题XHTML文件的邮件内嵌武器化SVG图像，渲染出仿冒哥伦比亚国家总检察院的网页，并利用HTML走私技术在浏览器本地组装ZIP压缩包以绕过邮件安全检测。ZIP内的JavaScript释放器伪装成“网络配置审计器2.7.298”，执行环境侦察后启动VBScript，绕过AMSI与ETW，同时展示虚假刑事传票页面作掩护，并删除原始XHTML、清除MotW元数据、在启动文件夹建立持久化，最终通过PowerShell在内存中解码并启动AsyncRAT与DCRat谱系的RAT载荷。哥伦比亚因关键基础设施安全成熟度不均而持续成为重点目标。

**文章来源****：Infosecurity-Magazine**

**02**

**俄罗斯黑客劫持Microsoft Exchange邮件服务器，针对北约与欧盟开展间谍活动**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibTm4bnjn5JPOj5XZKXnGzLrRymlCqBdg0fISPALYY9jETiclnhrugcCvd7sg1uCLWjgTiaFeLH9OFickmLZAicVbtDvnSZUlpIViaBA/640?from=appmsg)

**简要介绍**

安全公司ESET披露，与俄罗斯联邦安全局（FSB）关联的国家支持组织Turla将Microsoft Exchange邮件服务器改造为攻击者控制的基础设施，用于监视涉及北约和欧盟的通信。该行动使用了一套工具集Cereal——一种模块化.NET恶意软件，可在Exchange服务器上运行、接收命令、在内存中执行、映射受害组织并收集特定邮件。2025年底，Cereal在哈萨克斯坦一个政府组织中被发现，用于静默监控外发邮件并转发关注的信息。一个月后，在罗马尼亚政府中又发现了同一工具集，其配置被调整为转发与北约和欧盟相关的邮件。该工具集最显著的特点是摒弃了外部命令与控制基础设施，直接将被攻陷的Exchange服务器用作C2中枢，使攻击者无需专门的基础设施即可操作，且操作者IP地址难以通过网络追踪识别。

**文章来****源****：****Bank Info Security**

**03**

**美国监管部门警告称医院制冷系统正成为网络攻击目标，或危及血液与药品安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibQ8fLAT6YSt8GDDIibh0hzQ4z2ys31cjmHfqwQlrobHXLKtHOZAtfrI9knm48Q3E8r2BpAxEQSGSMMMb8kKR9iaycsgxbicKBfcvA/640?from=appmsg)

**简要介绍**

美国网络安全和基础设施安全局、FBI及卫生与公众服务部、农业部、交通部联合发布警告，要求医院等关键基础设施运营者紧急加强互联网联网制冷系统的防护。此前，欧洲自10月中旬起发生一波制冷设施网络攻击。随后攻击范围扩大，法国血液机构的一家制冷供应商也遭入侵，所幸值班技术人员及时发现冷藏设施温度上升，血液制品未受影响。美国机构警告，攻击者利用未修补或联网的电子温控器漏洞，可远程篡改设置、强制设备进入持续加热或化霜循环，破坏温度敏感物资并干扰监测系统。美国医院协会建议医院审视联网OT设备是否确需联网，并在可行时断开连接，同时强化身份认证、更新设备、隔离OT网络。

**文章来****源：****Bank Info Security**

**04**

**法国互助信贷银行遭供应链攻击，银行账户被欺诈转走1亿欧元**

![](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibSJzJAQBzoiauRyxb6wSOckCib8OrvPTepicUGeaySIOic7BFIoftddbQYteqoaQBND5Aet9exb0qMLgVIrxae05HSIIIwTjevF9E4/640?from=appmsg)

**简要介绍**

法国合作银行互助信贷阿凯亚（Crédit Mutuel Arkéa）确认，攻击者通过其一家第三方服务商的平台入侵银行系统，利用银行自有账户向其他机构发起欺诈转账，造成约1亿欧元（约1.12亿美元）损失。被盗资金随后通过专业平台兑换为加密货币，区块链调查员指出攻击者将USDC稳定币大量兑换为以太坊并在多条链上洗钱。银行强调这是一起外部供应链攻击，客户资产和银行自身稳定性未受威胁，攻击“已得到控制”，目前正配合司法与警方追查来源并尝试追回资金。该案是欧洲银行史上规模空前的盗窃事件之一，也是法国近期接连发生的网络攻击中的最新一起。

**文章来****源：****Bank Info Security**

**05**

**300家美国银行客户遭黑客以伪造登录页面手段窃取凭证**

![](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibRRC7XHtQKN6EFdSh84mKxZaLtwoOwZAVCibdvIeIoqYfmRvnDub4kra3Zz5T88KTd66Id6F8vY8vxrbAcgBy9t6ZiaERxUQiarSI/640?from=appmsg)

**简要介绍**

威胁情报公司Kela报告称自5月以来，一场单一钓鱼活动持续针对约300家美国银行（多为中型及区域性机构）的客户，同时波及全球加密货币交易所及美国财政部服务用户。攻击者通过伪造银行登录页面窃取凭证，并使用重复访问伪装技术--同一IP二次访问时显示“账户已暂停”等假象，以躲避安全扫描器和下架团队。截至10月25日，仍有248个仿冒189家金融机构的域名在线，命名多采用secure、disable等关键词与银行名拼接。攻击基础设施与英国、荷兰、澳大利亚、新西兰等地的银行、加密交易所及政府服务钓鱼活动共享，指向单一运营者或钓鱼即服务平台。据悉，10月11日至20日期间，攻击者通过英国住宅宽带IP连接跳板服务器，并使用VPN与Tor出口节点，疑似定期检查管理面板。

**文章来****源****：Bank Info Security**

**06**

**范德堡大学遭网络攻击后紧急下线系统，BYOD勒索团伙声称已窃取超百万条身份信息**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibRJOhjye2sdibdl0xXhyarVJ6ef9Yyn2K3Z3dRgxh35UZaPrlARplS1aezicGYCN7Z16rrkvpkgDA3ibyc8rv5V7aXl9OYmj9GAYY/640?from=appmsg)

**简要介绍**

美国范德堡大学于2026年11月9日确认其遭受网络安全事件，可能影响大学设备、系统和云服务（包括OneDrive与Box），随即要求全校师生关闭大学设备、断开校园WiFi，并警惕异常弹窗、文件权限变更或可疑认证请求。校方IT团队与政府机构合作调查并遏制事态，课程与学生服务于次日恢复正常，校园WiFi及Okta、Outlook、Zoom等部分系统重新开放，但多数系统访问仍受限。勒索软件团伙BYOD在数据泄露网站宣称对攻击负责，声称锁定了大学数据库、获取研究数据及逾100万份社会安全号、姓名、邮箱、电话和学生与员工记录，并称完全控制了域控制器。校方未确认数据是否实际泄露，也未点名攻击方。BYOD勒索软件团伙自2026年9月出现以来持续针对学术与医疗机构发起网络攻击。

**文章来****源****：****Info Security-Magazine**

**07**

**黑客冒充IT人员诱骗美国雇主健康服务提供商Marathon Health登录凭证，近570万人数据泄露**

![](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibT3oILfSmz1jnrFC7z29icibgEbmYbiaCTMauO6u400VahicHqMZz6aiaeyzibR0g5TaRDcVbzc6sASCtUbCkZFEsO6aoZF6Z0icThj0g/640?from=appmsg "undefined")

**简要介绍**

美国雇主健康服务提供商Marathon Health披露，2026年8月24日，黑客冒充公司IT人员，诱骗一名员工交出其凭证，随后利用该凭证访问云端应用并导出后端数据库信息。调查于9月9日确认个人信息被盗，影响人数达5,684,735人。泄露数据因个体而异，包括姓名、出生日期、联系方式和社会安全号，部分州监管文件还提及医疗与健康保险信息。由于Marathon Health为600多家雇主管理健康计划，部分从未使用其服务的人员也可能受影响，例如印第安纳大学已通知参保员工及家属。截至报道时，尚无已知黑客组织声称对此负责，公司也未披露是否收到赎金要求。Marathon Health已开始通知受影响个人，并提供12至24个月的免费信用监控服务。

**文章来****源****：****Bank Info Security**

**08**

**日本家居用品制造商Iris Ohyama云服务器被非法访问，约770万条个人信息或遭泄露**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibSHx7jnqDKAgSwnleNEuqPIMsG8mLBiag6f8zV1sGQdxdlmTGLxwxqWUVyuIegl6Du7v1EGYIZd1ZKWQXx8S5bK6sAsChV6GJ50/640?from=appmsg)

**简要介绍**

日本家居用品制造商Iris Ohyama披露，其在线购物子公司Iris Plaza使用的外部云服务遭未授权访问，约770万条个人信息记录可能已被查看或获取，但该数字指受影响云环境中存储的记录总量，并非已确认被盗数据。潜在受影响者包括约580万名现有及历史会员和约190万名非会员；可能泄露的信息因注册状态而异，涵盖姓名、地址、电话、邮箱、性别、出生日期及密码等，其中部分信息（包括密码）已加密。信用卡信息未存储在该云服务中，公司称未遭泄露。Iris Plaza于2026年10月28日发现可疑文件后立即关停平台并启动调查，确认第三方未授权访问，分别于10月29日和11月5日发布初步通知与更新。截至11月5日，未收到信息被冒用或造成财务损失的报告；公司已向日本警方报告此事。

**文章来****源****：****Security Affairs**

![](https://mmbiz.qpic.cn/mmbiz_gif/RdDBE4xfCCWnp4MYTluo2ib4Pibo5QAoxm2iaJME3yPXPLr1QYibicibCZibDib4185YxjKdxtvrcRspzxXj8BqZlnUhibA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/RdDBE4xfCCXHBrgOytxrXj5Isuu7Wa0bM6XhWyfjejlJia5dbBFcSpxZGvYibRndWGfODicNTYEpBFkXzuvp547cw/640?wx_fmt=gif)

往期回顾：

[![](https://mmbiz.qpic.cn/mmbiz_png/76BUAjRsqibR8Qib7Jq2qmHuhQgrwQpxibtkK2SSF6kL9PnUVeaDkT5EGS2c2ZXnC844zBIUDFP8sLoAPWwLaHmWq92ThibZ2faQT2OTbCTGVsY/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU3MDA0MTE2Mg==&mid=2247494397&idx=1&sn=c76fc424139433925329d9336cbee98c&scene=21#wechat_redirect)[![](https://mmbiz.qpic.cn/sz_mmbiz_png/76BUAjRsqibS37UVWVzbKViaB4ibZgiaQYNNnRic5ibVt3uqgQzD1zttX26qM71dxz76G69P0EoLkCx9okY0gsZtib0RD0BhicFFiakrfpzjRYOOywak/640?from=appmsg "undefined")](https://mp.weixin.qq.com/s?__biz=MzU3MDA0MTE2Mg==&mid=2247494390&idx=1&sn=17cf560cd9b8a80ff349ff02de7d0a9b&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RdDBE4xfCCWxG4sOdBlYYMiavXjD9Mejibc1pluORms2tmtNrSEgTlrWVzT5pFjaE7kMVondCXfpqLEVfB3SLTMA/0?wx_fmt=png)

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