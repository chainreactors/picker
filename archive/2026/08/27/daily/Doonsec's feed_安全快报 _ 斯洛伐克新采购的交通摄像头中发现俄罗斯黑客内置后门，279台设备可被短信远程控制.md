---
title: 安全快报 | 斯洛伐克新采购的交通摄像头中发现俄罗斯黑客内置后门，279台设备可被短信远程控制
url: https://mp.weixin.qq.com/s/4KrX8gl2atxf4S-3wQ9ubg
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:35:28.310115
---

# 安全快报 | 斯洛伐克新采购的交通摄像头中发现俄罗斯黑客内置后门，279台设备可被短信远程控制

# 安全快报 | 斯洛伐克新采购的交通摄像头中发现俄罗斯黑客内置后门，279台设备可被短信远程控制

天懋信息

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**本周安全事件速览**

**08月20日-08月26日**

**01**

**斯洛伐克新采购的交通摄像头中发现俄罗斯黑客内置后门，279台设备可被短信远程控制**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibTwLR0aV9Lzq0fWM0QNPNh0gyenXsu5EPLstH7OicciaMiaWXVsia4Zy8AB9KMe18IctUPfz8icN6jTezpBC0JtKSOQjultXyocd6m0/640?from=appmsg)

**简要介绍**

斯洛伐克国家安全局在该国新购置的279台NERO R-ONE高速摄像头中发现内置后门。这些摄像头通过欧盟支持的3000万欧元现代化基金采购，其模块中预置了12个俄罗斯关联电话号码。任意一个号码发送的短信即可激活后门，使攻击者无需IP地址或密码即可获取摄像头的实时画面并实现完全控制。斯洛伐克国家安全局发布了一份技术报告，介绍了NERO摄像头中发现的额外安全缺陷以及设备的实际来源。调查发现，这些设备的安全启动功能被禁用，Web管理门户和通信接口也存在多个漏洞。斯洛伐克媒体指出，摄像头实际为俄制CORDON PRO.M的贴牌版本，由一家塞浦路斯空壳公司通过无竞标合同向政府出售。类似设备据报已在克罗地亚和东欧多国部署。

**文章来源：****Bank Info Security**

**02**

**挪威数字政府基础设施遭DDoS攻击导致公共服务大面积中断**

![](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibSDMYLlK7Cx9OicJSbpdKfGywxZ2BKaicdR4CwDuSjptM5ybcvqHouasfdvpXcKL9YhMxWYYgIB2LjjRMyeQENNd44vumf0RNq1s/640?from=appmsg)

**简要介绍**

挪威共享数字政府基础设施再次遭遇分布式拒绝服务（DDoS）攻击，这已是短期内第三次发生此类事件。本次攻击于8月24日凌晨3时38分开始，目标是由挪威数字管理局（Digdir）及其服务商Vivicta运营的基础设施。攻击导致多项共享公共服务出现短时完全不可用，其他服务则出现连接失败、响应缓慢及登录时间延长等问题。Digdir负责运营ID-porten、MinID、Maskinporten等多项挪威公共部门共享基础设施。当共享认证服务中断时，影响会扩散至其他依赖它们的系统，Altinn平台及依赖ID-porten的公共服务均受到了波及。此前6月和8月3日已发生过两次类似攻击。Digdir强调此次事件仅涉及服务可用性问题，无证据表明系统遭入侵或个人信息泄露。Digdir表示服务已大体恢复稳定，但部分系统仍存在限制。

**文章来****源****：Security Affairs**

**03**

**缅甸政府与IT部门遭网络间谍组织诱骗攻击**

![](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibRic0YGXOlvaylV81Doia5GibibEqydlxgLapHRkKfUEtJPiaKD56Akgezia032KyLF8berrt8YtGrzA7mjmet4NJsQXqnmqP9b4gXjw/640?from=appmsg)

**简要介绍**

代号为“Operation QUICSILVER”的网络间谍活动以缅甸政府及信息技术部门为目标，该攻击诱饵伪造缅甸公共假期日历，后续攻击则使用虚拟硬盘文件触发感染链，内含伪装成PDF文档的Windows快捷方式。受害者打开后，会显示一份用缅甸语撰写的毕业典礼邀请函作为诱饵，同时快捷方式利用合法的Windows ftp.exe程序秘密执行恶意脚本。脚本随后将隐藏目录中的两个文档文件合并，重构出下一阶段的载荷。该载荷是基于Golang编写的后门程序QUICAgent，具备沙箱规避能力，通过随机延迟和大量SHA-256哈希运算来逃避检测。后门通过Cloudflare Workers域名动态获取C2服务器地址，并使用QUIC协议通过UDP 443端口与服务器通信。QUICAgent支持执行命令、传输文件、浏览目录等五项功能，并通过在Windows启动文件夹中创建LNK文件实现持久化。

**文章来****源：****The Hacker News**

**04**

**中亚多国政府遭网络间谍组织利用多款远控工具入侵**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibS5NM8KbVZ3m1EB7W3UxzRauBuoMTEFYl7xtTIfic3hEKoR87wSyLjDgVo6JvIBibOyOah5z2qBhkc8V5OQqAVGYNxTNh00Df3WI/640?from=appmsg)

**简要介绍**

安全公司Bitdefender披露了一项代号为“SilkParasite”的网络间谍行动，该行动持续针对中亚地区政府机构发动网络攻击。攻击者使用了七款远程访问工具（RAT），其中DriveSilkRAT、CookiETagRAT、NomadRAT、GoginRAT和NodeEdgeRAT五款为首次被发现。该行动攻击链通常以附有密码的RAR压缩包开始，内藏恶意Office文档，通过鱼叉式钓鱼邮件投递。诱饵文件针对乌兹别克斯坦、土库曼斯坦等国政府定制，甚至冒充特定部委。攻击链中的宏代码会启动DLL侧加载，释放第一阶段载荷。值得注意的是，恶意宏会主动检查卡巴斯基杀毒软件是否运行，以规避检测。五款新型RAT功能各异，覆盖.NET、C++、Go和JavaScript四种语言。其中，DriveSilkRAT利用Google Drive作为命令与控制（C2）服务器；CookiETagRAT则通过HTTP Cookie/ETag响应头接收指令。所有工具均采用插件化架构，便于扩展且保持低检测率。

**文章来****源：****The Hacker News**

**05**

**伊朗关联黑客首次成功入侵英国一发电厂**致使设施关闭**停运四天**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibRPEBSyo3y8UEl32sltlWfexnsP3ntiaaakv3nI88AnQswFvsd7JmzhvIMp0vb9CNkvSYEqeRVLib4Qc7pDAy02ZY9orb2jQBu9A/640?from=appmsg)

**简要介绍**

2026年7月，伊朗黑客成功入侵英国一座小型燃气发电厂，导致该设施关闭长达四天。这是伊朗关联黑客首次成功使英国发电设施瘫痪的案例，也是同类网络攻击中最为成功的一次。出于安全考虑，英国官员未公布电厂名称。该电厂规模较小，停运未影响英国整体电力供应。此次攻击被报告给隶属于GCHQ的国家网络安全中心（NCSC），该中心负责保护英国的关键基础设施。此次攻击与同期席卷美国12个州、数十家污水处理厂的网络攻击同步发生。FBI将美国事件归咎于“恶意网络行为者”，美国政府消息人士随后确认威胁很可能源自德黑兰。分析认为，此次攻击的目的并非伤害平民，而是展示与伊朗伊斯兰革命卫队关联的黑客能够渗透并致使英国敏感基础设施瘫痪。

**文章来****源：****Security Affairs**

**06**

**美国警告AI生成脚本正用于攻击西门子PLC关键基础设施安全漏洞**

![](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibSwrQYK9yc10ticKZcnEZk97b9WoWia5kjhTyMsGvQTlTdicJJdjAUcX5YZKk2MAtQ8y1CZBcf7ZIg9lib1hZ9GIuwMdeicX0Ax5eqI/640?from=appmsg)

**简要介绍**

美国国家安全局（NSA）、网络安全与基础设施安全局（CISA）、联邦调查局（FBI）等多家机构联合发布警告，称美国关键基础设施正面临利用人工智能生成漏洞利用脚本的活跃威胁。攻击目标为西门子S7系列可编程逻辑控制器（PLC），涉及制造、能源、水务、化工等多个关键行业。攻击者利用Censys、ZoomEye等互联网扫描服务，查找暴露在互联网上且运行过时软件或防护不足的PLC设备。借助AI辅助，攻击者基于公开信息生成针对S7系列PLC的漏洞利用脚本，以实现初始访问、凭据窃取和拒绝服务等目的。其部署的自定义Python脚本集成了snap7等开源工控库，伪装成合法监控工具，通过S7comm协议对PLC内存进行读写操作。联合机构建议运营者确保系统更新、隔离互联网访问、加强访问控制并部署安全监控。

**文章来****源：****The Hacker News**

**07**

**美国非营利性医疗系统AnMed遭网络攻击导致公司业务中断数周和患者数据被盗**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/76BUAjRsqibQ0BT22O2dS1YcJYo0sU9X5aVibgsR9WjJ0vUuk5AqWERGaogkt26c27bl8MOYHA4KXbG5bQ6Gm9qAf8Jspr6Hiar2mnSbggbnMc/640?from=appmsg)

**简要介绍**

非营利性医疗系统AnMed证实，在7月发生的一起网络攻击中，犯罪分子窃取了患者信息。此次攻击导致其IT环境和患者服务中断数周。AnMed服务于南卡罗来纳州和佐治亚州东北部地区。勒索软件团伙“The Gentlemen”声称窃取了6TB的公司及患者数据，包括与心理健康、生殖护理、基因检测和癌症相关的记录。攻击发生后，该团伙还入侵了AnMed的Facebook账户并发布威胁信息。AnMed首席执行官表示，这是一起由追求经济利益的团伙精心策划的复杂事件。目前，AnMed正在确定具体泄露内容，并表示不认可犯罪分子的说法，而是完成独立审查后再通知受影响者。AnMed警告患者警惕诈骗，呼吁不要回应可疑通信、点击链接或提供个人信息。目前，电话服务、电子健康记录读写权限及MyChart患者门户已恢复。

**文章来****源：****Bank Info Security**

**08**

**基因检测公司贝勒遗传学遭黑客非法入侵，31万人测试结果与员工数据或遭泄露**

![](https://mmbiz.qpic.cn/mmbiz_jpg/76BUAjRsqibSIxAIXMrn5Ce4guZ6CadeRjEnMDGR43m90AIZycmmIrhES9F8ofKWGEiburyzwOIgX3JygC16zBSVF3HqfTPvQD95sDZZCADj8/640?from=appmsg)

**简要介绍**

基因检测公司贝勒遗传学（Baylor Genetics）正在通报一起发生于6月的网络攻击事件，约31万人受影响。该公司提供基因测序等诊断服务，业务可追溯至1978年。该公司于6月15日在其IT环境的一小部分中发现可疑活动，调查确认攻击者在6月11日至17日期间访问了其网络和存储数据。泄露信息因个人而异，可能包括姓名、出生日期、医疗检测信息、实验室检测结果、健康保险信息，以及部分个人的社会安全号码。现任或前任员工的个人信息，如社会安全号码、政府身份证号和财务账户信息也可能被泄露。贝勒遗传学表示，目前尚未确认有身份盗窃、欺诈或个人信息滥用事件发生。目前尚无网络犯罪团伙宣称对此次事件负责。

**文章来****源：****Bank Info Security**

![](https://mmbiz.qpic.cn/mmbiz_gif/RdDBE4xfCCWnp4MYTluo2ib4Pibo5QAoxm2iaJME3yPXPLr1QYibicibCZibDib4185YxjKdxtvrcRspzxXj8BqZlnUhibA/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_gif/RdDBE4xfCCXHBrgOytxrXj5Isuu7Wa0bM6XhWyfjejlJia5dbBFcSpxZGvYibRndWGfODicNTYEpBFkXzuvp547cw/640?wx_fmt=gif)

往期回顾：

[![](https://mmbiz.qpic.cn/mmbiz_png/76BUAjRsqibTJuz7YUUnNscHlA7fwHiaPVPsRXlce7az2btP81ia9tmhibLoJN4GlnzTR49Znv86mczR6pv7SC3OajgfoV8TAibX77HBUnwPMqicc/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU3MDA0MTE2Mg==&mid=2247494150&idx=1&sn=edcd31c3549b31eb8e9b0637d3747120&scene=21#wechat_redirect)[![](https://mmbiz.qpic.cn/mmbiz_png/76BUAjRsqibSYnrDJdDzhRgiaGZfXvRVzu0KwYliaC0d0Cp1R6VicjRVkLIzvgGiaTl6qgBXJCYkDbVgmNGZl680NB8eFZhfn0ghnKj1ibiciclDEUY/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU3MDA0MTE2Mg==&mid=2247494114&idx=1&sn=d3b9a172f73afc7e0c85abbe537132b7&scene=21#wechat_redirect)

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