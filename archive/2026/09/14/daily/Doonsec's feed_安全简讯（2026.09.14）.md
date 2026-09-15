---
title: 安全简讯（2026.09.14）
url: https://mp.weixin.qq.com/s/nmTZaQPE7kzd5_-F3b8cDA
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T06:57:33.205898
---

# 安全简讯（2026.09.14）

# 安全简讯（2026.09.14）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**1. LiteLLM服务器暴露，AI网关成安全重灾区**

9月10日，数千台LiteLLM服务器已在网上暴露，其中数百台接受默认密码或无需身份验证，黑客可轻易窃取敏感令牌甚至劫持基础设施。LiteLLM是开源AI网关，可同时访问OpenAI、Anthropic、Gemini等多个LLM提供商，其Docker容器被拉取超2.4亿次，今年早些时候还曾遭大规模供应链攻击。谷歌旗下Wiz扫描发现超85,000个LiteLLM实例，检查的3074台服务器中有294台完全无需验证或接受默认主密钥“sk-1234”，且三分之一的云环境运行着LiteLLM部署。一旦暴露，不仅API密钥泄露，流经实例的提示、响应及MCP连接的外部工具都会暴露。攻击者可利用其进行API调用增加成本，还可将其作为跳板获取进一步访问权限，因其涉及代码执行，可运行服务器端Python并将请求路由到任意内部URL。Wiz指出，未配置身份验证时所有用户都会被授予管理员权限；未修补版本存在授权后可执行根级代码的漏洞（CVE-2026-59821），MCP端点身份验证缺陷允许无凭据登录并访问连接工具（CVE-2026-59822），进而查询数据库、读取GitHub代码库或读写文件系统。

https://cybernews.com/security/litellm-servers-exposed-require-no-password/

**2. Revolut因伪造政府请求泄露客户数据**

9月12日，Revolut证实因收到来自政府机构域名基础设施内电子邮件地址发送的欺诈性信息请求，该公司将敏感客户数据泄露给了未经授权的第三方。通知指出，该邮件包含有效的域名身份验证凭证，通过了旨在确认邮件来自政府机构的验证。Revolut表示，基于合理理由相信这是真实请求并予以满足。泄露数据包括客户身份和联系方式（出生日期、邮寄地址、电子邮件、电话号码）、护照和驾照复印件、验证自拍照、账户对账单及交易记录，其中交易记录涵盖比特币。这并非技术漏洞：没有系统被入侵，没有恶意软件，服务器未被外部访问。攻击者要么在政府机构域名下创建恶意账户，要么入侵现有账户，然后提交看似合法的数据请求，Revolut工作人员处理了该请求，事后核实才发现是欺诈。Revolut称事件仅影响部分客户，已立即联系，但未透露具体范围和涉事政府机构名称，也未说明是否影响特定国家或市场。

https://securityaffairs.com/198922/data-breach/revolut-exposed-kyc-data-after-fraudulent-government-email-passed-security-checks.html

**3. 佛州车管局确认驾驶员数据库遭泄露**

9月11日，佛罗里达州公路安全和机动车辆管理局（FLHSMV）已证实，其DAVID驾驶员数据库在ShinyHunters勒索团伙声称入侵后遭遇数据泄露。此前，ShinyHunters声称窃取超过20万条驾驶员记录。FLHSMV声明称，9月4日获悉一个国际网络犯罪组织实施了数据泄露，事件已迅速得到控制，目前无进一步泄露。调查确定，攻击者使用了属于普兰特城警察局一名用户的被盗凭证，这些凭证被不当存储在该员工的个人电子设备上。该机构已通知佛州总检察长办公室，并正与州数字服务局和执法部门合作应对，称因属正在进行的刑事调查，更多信息将在适当时机公布。然而，FLHSMV的调查结果与ShinyHunters的说法不同。黑客声称利用密码重置漏洞获取了多个DAVID账户访问权限，包括DMV员工和FBI特工账户，随后从9月3日起遍历记录ID并下载相关HTML页面和图像。为证明入侵，攻击者分享了属于杰弗里·爱泼斯坦的DAVID记录截图，含敏感个人信息和车辆信息。

https://www.bleepingcomputer.com/news/security/florida-confirms-dmv-database-breached-via-stolen-police-account/

**4. JFrog Artifactory曝严重漏洞遭利用**

9月11日，威胁行为者正利用JFrog Artifactory中的严重和高危漏洞绕过身份验证、获取管理权限，并在自托管服务器上部署Rust后门。云安全公司Wiz报告证实，该漏洞已在多个环境中被利用，包括结合CVE-2026-42018和CVE-2026-42016的利用链。第三个漏洞CVE-2026-82329是严重身份验证绕过漏洞，watchTowr本月初观察到有人利用其铸造管理员令牌。攻击者先利用CVE-2026-42018获取内部匿名用户的JWT，即使匿名访问被禁用且权限较低；随后利用CVE-2026-42016将权限提升至管理员级别。8月15日至9月8日期间，多个威胁行为者利用这两个漏洞，某些情况下创建管理员账户仅用不到五分钟。攻击者创建管理员账户并生成长期访问令牌后，安装恶意Groovy插件执行任意命令，并通过部署基于Rust的后门建立持久性。Wiz表示，在多个案例中发现具有C2功能的定制Rust后门程序。下一阶段，攻击者下载额外载荷，上传webshell，窃取Artifactory配置数据和集群加入密钥，枚举存储库、令牌和用户，并将SSH密钥添加到新创建账户中。

https://www.bleepingcomputer.com/news/security/artifactory-flaws-chained-in-attacks-deploying-backdoor-malware/

**5. GitLab曝最高危漏洞，用户被敦促立即修补**

9月11日，GitLab周四敦促用户立即修补其服务器，以应对编号为CVE-2026-85706的最高严重性路径遍历漏洞。该漏洞由安全研究员“s3ntago”通过GitLab的HackerOne漏洞赏金计划报告，源于存储库提交API中路径限制不当和身份验证强制执行缺失。未经身份验证的攻击者可在“某些条件下”利用该漏洞从易受攻击的服务器读取任意数据，例如凭据、密钥和敏感信息。虽然GitLab尚未将此漏洞标记为已被利用，但一天后，网络安全公司watchTowr报告称，攻击者已开始搜索未针对CVE-2026-85706打补丁的暴露在互联网上的GitLab服务器。watchTowr警告称，已观察到针对该漏洞的野外探测，该漏洞允许攻击者通过单个HTTP请求读取任意文件，并指出根据近期GitLab漏洞情况，大规模利用可能不远，防御者应检查日志文件，查找包含“file.path”参数的HTTP POST请求以识别潜在攻击尝试。

https://www.bleepingcomputer.com/news/security/gitlab-urges-users-to-patch-max-severity-path-traversal-flaw/

**6. Cl0p声称入侵哈雷戴维森窃取270GB数据**

9月12日，Cl0p团伙声称入侵哈雷戴维森内部网络，数据量达270GB，并在暗网泄露网站标注“通过种子文件、磁力链接发布”，称该公司是四家“没有联系我们”的企业之一。哈雷戴维森发言人周五表示已注意到相关说法，但拒绝进一步置评。审查磁力目录后，此次泄露可能与Cl0p近期针对使用Windchill PLM软件的制造公司的勒索活动有关。Windchill由PTC开发，是全球主要制造商广泛使用的产品生命周期管理平台。公开目录显示了PTC Windchill 13服务包、WC12应用程序组件、Windchill管理员主目录、Solr服务器、Vaultlist文件及PublishModeLog等环境指标，涉及服务器日志、系统配置、备份信息及数据保险库引用，但尚不清楚各文件具体内容。PLM平台处理产品数据及工程师、制造商、供应商之间的实时工作流程，敏感数据泄露后果可能极为严重。Cl0p至少自2019年起活动，曾利用MOVEit、Fortra GoAnywhere和Cleo漏洞。6月，该团伙转向利用影响PTC Windchill PLM的零日漏洞CVE-2026-12569。

https://cybernews.com/news/harley-davidson-clop-data-breach-windchill-270gb/

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