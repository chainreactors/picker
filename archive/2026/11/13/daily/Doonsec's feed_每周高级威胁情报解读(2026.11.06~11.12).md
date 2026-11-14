---
title: 每周高级威胁情报解读(2026.11.06~11.12)
url: https://mp.weixin.qq.com/s/47VDiSAO3YLTemsicTRzQA
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:14:56.587846
---

# 每周高级威胁情报解读(2026.11.06~11.12)

# 每周高级威胁情报解读(2026.11.06~11.12)

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026.11.06~11.12

**攻击团伙情报**

* 失控：曝光 Silent Lynx 服务器内幕
* Turla 新工具集 Cereal：劫持 Exchange 邮件流水线
* 肚脑虫组织使用节日主题诱饵对巴基斯坦的攻击活动分析

**攻击行动或事件情报**

* 关于“银狐”木马“金钩（G03）”团伙攻击态势深入分析报告
* 威胁行为者利用 GSocket 打造隐蔽的 C2 通道
* 黑客利用AntiFox人工智能代理发起AWS凭证窃取攻击
* 范德堡大学遭遇 BYOD 勒索团伙攻击
* 多款国产小型软件更新供应链攻击行动披露

**恶意代码情报**

* Falcon C2 利用浏览器规避检测
* GhostFrame：一款与 Settra 勒索软件相关联的新型 ESXi 植入程序
* Armorsteal 揭秘：剖析一款窃取数据和挖掘加密货币的 Python 恶意软件工具包
* Citrus 勒索软件：VLESS 承载通信、Sn00py 负责加密，大语言模型助纣为虐

**漏洞情报**

* 微软补丁日通告：2026年11月版
* 谷歌修复 Chrome 今年第八个野外零日漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq8uSBMN9OXcNP5ZTlqHZB4rUtWKibbsToibIIgnsmPZCMZ7gXngEdkCSlvCobhGSrCJgwYNoibhDopOxb1icUpww9b17Gm2eScemSw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqibtZicQfWYpY2bDgdyY7767Jq03pxnqMYiaibOfhGmQoNVOLZpb0pIeaeTY22vCeKFlFlMv8mpYdzkXjoHpdKNesO3l2LhEbjhmpE/640?wx_fmt=gif&from=appmsg)

**攻击团伙情报**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOq969RauKA3O9IHSmTk2eqK3ZvLXlIgpW0HGNfyicMpxDnMiaROaCGKBYo8Wll9Njpyz7FzlZIcB4icY4jjiaMvXVjZPCHPf6Ir14lI/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqicXdfwhqF9HmI9ibuOQLsn7m374O5Kxpp2iccKZ0iaSdcRvMUefSDBibrAD8AicYhkdjgDfaqCTf4Z80HTAryiaRhkpnx0z1ljUiaNy30/640?wx_fmt=gif&from=appmsg)

**01**

**失控：曝光 Silent Lynx 服务器内幕**

**披露时间：**2026年11月11日

**情报来源：**https://www.cloudsek.com/blog/off-the-rails-inside-an-exposed-silent-lynx-server

**相关信息：**

CloudSEK于2026年11月11日披露，一个暴露的Silent Lynx服务器开放目录提供了该中亚间谍集群2026年4月至10月的工具、入侵数据和AI代理对话。高置信度将其归属Silent Lynx，中置信度显示哈萨克斯坦关联。操作者长期控制塔吉克斯坦铁路网络，借单一员工账户从政府电子公文平台批量获取国防等敏感文件；通过WAR、webshell和PostgreSQL超级用户权限攻入乌兹别克斯坦Smart Forestry并取得主机执行；还制作土库曼斯坦铁路和地方行政钓鱼诱饵，预示新行动。植入匹配Laplas和Chvost并出现新服务安装器及AMSI绕过。自托管Hermes代理使用DeepSeek承担侦察、收集和日志清理，破坏性命令获预授权，Telegram用于控制。操作者经Tor登录，测试流量来自哈萨克斯坦住宅连接，多项OPSEC失误导致暴露。

**02**

**Turla 新工具集 Cereal：劫持 Exchange 邮件流水线**

**披露时间：**2026年11月10日

**情报来源：**https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/

**相关信息：**

ESET在哈萨克斯坦政府Exchange服务器发现此前未记录的Turla模块化.NET工具集Cereal，一个月后在罗马尼亚政府组织发现同一工具集，后者配置收集与北约和欧盟相关邮件。该工具集无外部C2，由受害Exchange服务器充当控制点；CerealNeuron被动监听伪装成OWA、Autodiscover和ActiveSync的路径，CerealHermit可从磁盘读取加密命令备用。命令以独立编译的.NET程序由CerealRunner投递执行，CerealLoader利用VTable Fixups和非托管入口在.NET运行时前执行原生代码，并滥用.NET原生映像缓存和合法Windows组件侧载。CerealBox注入EdgeTransport.exe并包装现有传输代理，筛选含doc、docx或pdf附件且匹配硬编码列表的邮件，压缩加密暂存后外泄。ESET高置信度归因Turla，显示其将Exchange作为长期收集与执行枢纽。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOq8qbJIgqdnn9w5fibfiaOEeMqGbEZnbw9M1q3iaz7zRiaqfmsWia5bGBD4o7xrvIXw8smwKrz6WJo0Hsy7SmEXKYUjicTECH2rWX7oXo/640?wx_fmt=png&from=appmsg)

**03**

**肚脑虫组织使用节日主题诱饵对巴基斯坦的攻击活动分析**

**披露时间：**2026年11月11日

**情报来源：**https://mp.weixin.qq.com/s/YXkLFwzXwQUjMygy1oR2OQ

**相关信息：**

360高级威胁研究院在日常狩猎中捕获APT-C-35肚脑虫组织针对巴基斯坦的钓鱼攻击活动，该组织长期围绕巴基斯坦及南亚目标开展情报窃取。本轮攻击以宰牲节开斋邀请函为诱饵，向受害者发送带恶意宏的Excel文档，宏代码加密保护并内嵌32位与64位两段Shellcode，根据系统版本选择执行。一阶段Shellcode经取反加异或解密出下载地址，获取后续载荷，再经二次解密得到二阶段Shellcode，后者检测Bitdefender、卡巴斯基、ESET、QuickHeal和360等安全软件驱动以决定行为，未检测到则下载伪装成音频文件的DLL，修复PE头后通过创建计划任务经rundll32加载实现持久化。该DLL收集用户名、计算机名及已安装软件信息，经AES加密上传至C2，攻击者根据目标校验结果有选择地下发MpuoAgent等后续功能模块。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOqib3GvGd1Eib2SWAKycmEbQk1vJ85Xia1bBEsaWBDXW6p0b82PfkHT1z6fQMIVEs42ibCsenGbafpHACetTcGkdj096pJtljBWicatg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqicgn5nYRnNLE9co5bGwrKvTtNA8JGpAmkibvVLciaKSfM3dNYEXTwPicnROUibtPgGONyMG6Rj3A5EWfBC45Jn4zvoiaiadXAliaFrU28/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq9boASorJ7fcwwmuq3SppcWKYxiaKCnwR9zvibFgUHFau2pYJkibhueZcyOtWQaNwghNUKzuNiabsg1icDfP5TPplfPq1VoDiao6cicvw/640?wx_fmt=gif&from=appmsg)

**攻击行动或事件情报**

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq83QVl4fkhr5u4YVJHbo6VT7yaiaRlmOCfy1oZTkSD2GkicybTucCfQl29iacgP258Vj02wonL3ZtpUIiced3lEKIWnucI9fUicJnCY/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq8EsQPBQ41sQ6eJPd4brIyj80FJkhCHW1wEkQ12FIia9LsK6Wg9LgpJ3Nv6tJRyFUgFGwNfPWJiajYUiaKguAjicGPPsuMcGliaIibibs/640?wx_fmt=gif&from=appmsg)

**01**

**关于“银狐”木马“金钩（G03）”团伙攻击态势深入分析报告**

**披露时间：**2026年11月10日

**情报来源：**https://mp.weixin.qq.com/s/y\_2SrPvsW2E5vPfcuvom-g

**相关信息：**

CNCERT与北京观成科技联合发布银狐木马金钩团伙攻击态势报告。该团伙最早可追溯至2025年，主要攻击国内高校、医疗、证券及科技企业，近期搭建高度仿真的同花顺仿冒下载网站并借助SEO投毒提升搜索曝光，诱导用户下载捆绑木马的安装包，其自制图标复用同花顺iFinD视觉设计，多个钓鱼站点呈现布局、命名及路径高度一致性。安装包释放银狐木马加载器与带同花顺公司数字签名的白文件，经四阶段分步解密加载，通过注册表自启动项持久化，具备反沙箱能力，经TCP非标准端口直连境外服务器，具备屏幕截图、键盘记录、远程命令执行及插件下发功能，通信采用每会话独立密钥的XOR加密。监测期间该团伙控制境内肉鸡超2.5万个，单日上线峰值超千个，专项组依据代码加密方式及通信协议同源性证据将其命名为金钩。

**02**

**威胁行为者利用 GSocket 打造隐蔽的 C2 通道**

**披****露时间：**2026年11月11日

**情报来源：**https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/

**相关信息：**

微软披露，多个威胁行为者利用开源远程访问工具GSocket攻陷Linux服务器后维持持久访问，即使初始Web漏洞修复仍可经公共Global Socket Relay Network中继通信，无攻击者自有IP或域名可封堵。Defender遥测显示2026年3月至8月相关检测增长356.2%，87.1%事件集中于Web应用与托管，PHP/cPanel占63.9%，Apache占24.3%，教育研究占30.7%，科技电信占22.9%。攻击链为利用面向互联网应用执行curl下载脚本，按架构选择客户端并暂存/dev/shm，经cron、systemd和shell配置持久化，伪装内核线程名并清除痕迹，部分尝试利用CVE-2026-43284提权。GSocket以共享密钥识别端点，可经Telegram、Discord或webhook传递，重连不依赖固定C2地址。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqib2syibsqMg7EKhaJlEKWunJib9ZGcTQc2W0C2YgFDKncZxK1RrfVVhw5Hibm87icoiaWjic5LoctTvYBl2T3wWhYVOTTumjicKPSvPA8/640?wx_fmt=png&from=appmsg)

**03**

**黑客利用AntiFox人工智能代理发起AWS凭证窃取攻击**

**披露时间：**2026年11月10日

**情报来源：**https://github.com/rtkwlf/wolf-tools/tree/main/pack\_alerts/202611-antifox-alibaba-hosted-platforms-facilitate-web-cloud-intrusions

**相关信息：**

Arctic Wolf Labs于2026年11月10日披露，开源智能体渗透测试平台AntiFox正被用于从阿里云托管基础设施发起入侵。攻击者先攻陷面向互联网的IIS应用，由w3wp.exe创建ASPX网页后门并执行命令，解析web.config获取连接字符串和应用设置，尝试连接内部生产数据库。随后利用有效AWS IAM用户及假定EC2角色，在约半小时内发出数百次跨服务API请求，多数被拒但夹杂成功操作，快速枚举IAM、EC2、S3、Lambda、Secrets Manager、KMS、RDS等，最终成功GetSecretValue获取生产密钥，并进行S3对象读取、复制和删除。建议监控异常托管ASN、单IP多凭据、跨服务List/Get/Describe突发、IIS工作进程派生命令及新增ASPX文件，并启用CloudTrail、S3数据事件和版本控制，轮换泄露凭据、撤销会话、实施最小权限和IMDSv2。

**04**

**范德堡大学遭遇 BYOD 勒索团伙攻击**

**披露时间：**2026年11月09日

**情报来源：**https://www.bleepingcomputer.com/news/security/vanderbilt-university-hit-in-byod-ransomware-attack-data-theft-claimed/

**相关信息：**

2026年11月9日，范德堡大学确认正应对活跃网络安全事件，可能影响校内设备、系统和云服务，要求师生关闭设备、断开校园Wi-Fi，警惕弹窗、文件或权限异常、文件缺失或被改、陌生应用和异常认证请求，发现异常立即关机并联系IT。BYOD勒索团伙声称加密数据库，窃取逾100万社保号、姓名、邮箱、电话、学生和员工记录及研究数据，并称完全接管域控；还出现README\_BYOD\_31.txt勒索信和播放警告音频的视频，但校方尚未确认团伙参与、设备是否加密及数据是否被窃。BYOD为2026年新团伙，泄露站另列5个组织，上月曾称攻击新墨西哥大学健康科学中心并造成系统中断。

**05**

**多款国产小型软件更新供应链攻击行动披露**

**披露时间：**2026年11月06日

**情报来源：**https://mp.weixin.qq.com/s/CesM6rLUoWb6IKJUUkn6dA

**相关信息：**

奇安信红雨滴团队披露一起针对多款国产小型软件更新渠道的大规模供应链投毒行动。攻击者瞄准更新配置接口使用明文HTTP、不校验更新包签名等系统性缺陷，劫持六个国产软件的更新通道，利用模板化工具生成伪装成正版软件的Inno Setup恶意更新包推送恶意载荷。恶意更新包内含带AMD有效签名的白文件及通过DLL侧载的恶意组件，经纯内存shellcode下载并四层解包，最终在内存中加载插件化的.NET植入体，不落盘。该木马经DoH的TXT记录死信箱获取C2配置，通信全程加密，并以ip-api.com校验受害者地理位置，明确仅针对云南省目标执行，否则退出。所有变体共享命名管道后缀MyControlPipeaaa，成为稳定同源判据。行动处于活跃运营状态，插件具体窃密能力尚待分析。

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqicfgTtFaTbky7l7et1ia583s2CMFPW1gY5aZTDicEqkMNbDwYZoCQHYXCzOm95H8gJUav3yerl0KHuU8C0KMhKiaOnlYAL9E10icaI/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOq9VQX0b7u6YXOaaiaztAl4aC04VS2fBeaCjGCIC2Hbgh7gRxkfLbLhDewCPVkwe65dEOF7V4qS2uF5h0XicY40dibPaDfnWS1XgyY/640?wx_fmt=gif&from=appmsg)

**恶意代码情报**

![](https://mmbiz.qpic.cn/mmbiz_gif/odcL3w4qOqicz0E7wmRypia47a2x6yZjttYg6OwfHyJmgoBvBKPhaiajRm6aW04zBQFxGoO4e6brmtJ9vG3uJvoubX56lzyGZL0FibJNZBRgibhQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/odcL3w4qOqibHtoO2QHgksy7EoTiaIrsIGfROHL1CvJJLW43JnC8dDsO4tibVicLQG8uzQUHVj5RWIDIvqiaVx99ndV8vWoF9a7YLmYj31kcuWn4/640?wx_fmt=gif&from=appmsg)

**01**

**Falcon C2 利用浏览器规避检测**

**披露时间：**2026年11月11日

**情报来源：**https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/

**相关信息：**

Unit 42披露Falcon又称XG的浏览器原生C2框架，攻击者向政府webmail和应用注入恶意JavaScript，控制访客浏览器并侧载伪装PDF阅读器的Chrome扩展，窃取密码、邮件、会话Cookie和通信，还投递以OneDrive为C2的Rust植入Antino。2026年3至5月中东和东南亚多国政府机构受影响。Falcon管理面板需连按三次F9显示登录，受害页面伪装游戏，并与PeckBird...