---
title: 安全简讯（2026.04.23）
url: https://mp.weixin.qq.com/s/U5Y7hXEcX3mVkF1MI9B4JA
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:55:17.624641
---

# 安全简讯（2026.04.23）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4S21m309ZrxFThjkVnWWGyQ4BSppcOSsp5ZEPRpgwCpVFicT7HzvcXfyEZ5NxwicicDlNWbTmibCntLeWVKYF8j6UtIJr4Jp89IJicnltoLiaU02Y/0?wx_fmt=jpeg)

# 安全简讯（2026.04.23）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. Kyber勒索软件双平台攻击，号称后量子加密**

4月22日，网络安全公司Rapid7在2026年3月的一次安全事件响应中，发现并分析了一种名为Kyber的新型勒索软件。该勒索软件同时具备针对Windows系统和VMware ESXi虚拟化平台的两个不同变种，且由同一个勒索软件关联组织部署在同一网络中，意图通过同步加密所有服务器以最大化破坏效果。两个变种共享相同的活动ID和基于Tor的勒索基础设施。其中，ESXi变种专门针对VMware环境构建，能够枚举所有虚拟机、加密数据存储文件，并用勒索信篡改ESXi管理界面，引导受害者完成赎金支付流程。该变种声称采用了Kyber1024后量子加密技术，但Rapid7分析发现这一说法并不属实，ESXi变种实际使用ChaCha8进行文件加密，并使用RSA-4096进行密钥封装。相比之下，Windows变种用Rust编写，技术实现更为成熟。它确实实现了Kyber1024和X25519密钥保护机制，与勒索信中的声明一致。具体而言，Kyber1024用于保护对称密钥材料，而AES-CTR则负责批量数据加密。

https://www.bleepingcomputer.com/news/security/kyber-ransomware-gang-toys-with-post-quantum-encryption-on-windows/

**2. Harvester用GoGra后门滥用微软云API实施攻击**

4月22日，威胁行为者Harvester被指使用了新版Linux版本的GoGra后门，研究人员在VirusTotal平台上发现了来自印度和阿富汗的恶意软件样本，表明这两个国家可能是间谍活动的目标。最新发现表明，Harvester正在继续扩展其工具集，使其不再局限于Windows系统，而是利用同一后门程序的新变种感染Linux系统。攻击利用社会工程学手段诱骗受害者打开伪装成PDF文档的ELF二进制文件。攻击者随后会显示诱饵文档，同时悄悄运行后门程序。与Windows版本类似，Linux版GoGra也滥用微软的云基础设施，使用开放数据协议查询，每两秒钟向一个名为“Zomato Pizza”的特定Outlook邮箱文件夹发送一次请求。该后门程序会扫描收件箱，查找主题行以“Input”开头的电子邮件。一旦收到符合条件的邮件，程序会解密Base64编码的邮件正文，并使用“/bin/bash”将其作为shell命令执行。执行结果会以主题为“Output”的电子邮件形式发送给操作员。数据窃取完成后，植入程序会清除原始任务邮件以掩盖痕迹。

https://thehackernews.com/2026/04/harvester-deploys-linux-gogra-backdoor.html

**3. Rituals遭黑客攻击，超4100万会员数据泄露**

4月22日，总部位于荷兰的化妆品巨头Rituals近日证实，黑客从其会员数据库中窃取了大量数据，导致客户个人信息泄露。Rituals表示，他们在4月份发现了一起“未经授权下载”会员数据的事件，被窃信息包括客户的全名、出生日期、性别、邮政地址、电子邮件地址、电话号码，以及他们偏好的Rituals商店和账户类型。Rituals发言人Eline van Malssen确认，黑客窃取的是欧洲和英国客户的会员数据，同时部分美国客户也受到影响。截至目前，Rituals尚未描述此次网络攻击的具体性质，也未说明数据泄露发生的具体方式，同时拒绝就公司是否收到黑客的任何信息、更精确的事件时间线或受影响会员的确切人数发表评论，理由为“安全原因”。据其官网显示，Rituals的会员数据库拥有超过4100万客户，这家零售巨头在2025年的收入达到24亿欧元（约28亿美元）。

https://techcrunch.com/2026/04/22/cosmetics-giant-rituals-confirms-data-breach-of-customer-membership-records/

**4. 西班牙捣毁最大西语漫画盗版平台Tu Manga Online**

4月22日，西班牙警方近日捣毁了他们所称的规模最大的西班牙语漫画盗版平台。该平台自2014年开始运营，每月为全球数百万用户提供服务，通过免费提供受版权保护的作品，并利用产生的网络流量获取广告收入。警方公告中未明确提及平台名称，但据TorrentFreak报道，该平台正是知名的西班牙语漫画网站Tu Manga Online（TMO）。在包括韩国知识产权持有者在内的法律压力下，该平台已被迫下线。警方于2025年6月展开调查，发现该平台通过铺天盖地的弹窗广告牟利超过470万美元。其中大部分广告为色情内容，鉴于该网站许多访问者为未成年人，这一情况令人担忧。用户在网站上进行的每个操作包括选择内容、阅读描述或浏览目录都会触发弹窗，从而最大化广告曝光率。警方公告称，自2014年以来，该组织一直系统地、免费且未经授权地提供大量受知识产权保护的作品的访问权限。该门户网站已成为西班牙语漫画盗版的主要参考点，每月访问量达数百万，具有显著的国际影响力，对版权所有者、出版商、翻译人员及整个文化产业造成了严重损害。

https://www.bleepingcomputer.com/news/security/spain-dismantles-major-47m-manga-piracy-platform-arrests-four/

**5. Mirai僵尸网络瞄准已停产D-Link路由器**

4月22日，Akamai最新报告指出，Mirai僵尸网络正在攻击已停产的D-Link路由器，利用的是一年前披露的命令注入漏洞CVE-2025-29635。该漏洞存在于D-Link DIR-823X系列路由器中，影响固件版本240126和24082。漏洞成因是攻击者可控制的函数值在未经验证的情况下被复制，并且可以通过精心构造的POST请求加以利用。Akamai解释称，路由器从请求正文中提取最终进入命令缓冲区的值，而不检查它来自哪个表单字段。观察到的攻击尝试针对的是相同的代码，并触发了相同的系统调用，这与去年在GitHub上发布后已被删除的概念验证漏洞利用程序完全一致。作为执行路径的一部分，攻击者加载了一个shell脚本来下载并运行有效载荷，该载荷具有许多Mirai特征，包括XOR编码、硬编码的控制台执行字符串和硬编码的下载器IP。受影响的D-Link DIR-823X系列路由器已于去年停产，且不再从供应商处获得软件更新。D-Link早在9月份就已发出警告，强烈建议用户停用该产品，并指出继续使用可能会对连接到该设备的其他设备造成风险。

https://www.securityweek.com/mirai-botnet-targets-flaw-in-discontinued-d-link-routers/

**6. npm蠕虫攻击：16个Namastex包遭投毒窃取凭证**

4月22日，一种针对npm生态系统的新型供应链攻击正在窃取开发者凭证，并通过从被盗账户发布的恶意软件包进行类似蠕虫的传播。该威胁由Socket和StepSecurity的研究人员在Namastex Labs的多个软件包中发现。截至发稿时，已确认被攻破的Namastex软件包共有16个。这些软件包主要用于AI代理工具和数据库操作，因此攻击目标为高价值终端，而非大规模感染。注入的恶意代码会收集与各类机密相关的敏感数据，包括令牌、API密钥、SSH密钥、云服务凭证、CI/CD系统凭证、注册表及LLM平台凭证，以及Kubernetes/Docker配置。此外，它还会尝试提取Chrome和Firefox浏览器中存储的敏感数据，涵盖MetaMask、Exodus、Atomic Wallet和Phantom等加密货币钱包。StepSecurity指出，该恶意软件本质上是一种“供应链蠕虫”。它能够寻找用于npm发布的令牌，并将自身注入到该令牌有权发布的每一个软件包中，从而实现进一步传播。

https://www.bleepingcomputer.com/news/security/new-npm-supply-chain-attack-self-spreads-to-steal-auth-tokens/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

启明星辰安全简讯

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

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