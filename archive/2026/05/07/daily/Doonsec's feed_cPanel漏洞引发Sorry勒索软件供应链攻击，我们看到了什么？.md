---
title: cPanel漏洞引发Sorry勒索软件供应链攻击，我们看到了什么？
url: https://mp.weixin.qq.com/s/odYzQtIw0mtcm5GNo00U-Q
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:52:25.967728
---

# cPanel漏洞引发Sorry勒索软件供应链攻击，我们看到了什么？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AwziaxUyibcNjvibQBUuPaNehkLr21icibuvoe6vyzu7ZS5cb7SCeibRNcHVvsgydPZaia1LdBY8pBd8D0dxBVKDVpksNp163icO2DsyTS28wTGAz9c/0?wx_fmt=jpeg)

# cPanel漏洞引发Sorry勒索软件供应链攻击，我们看到了什么？

原创

千里
千里

东方隐侠安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

各位少侠好，我是千里。

过去两周，一场利用cPanel认证绕过漏洞（CVE-2026-41940）的大规模攻击正在全球范围内蔓延。攻击者无需任何凭据，只需要发送几个特制的HTTP请求，就能获得root级别的WHM管理权限。

![コントロールパネルcPanelとは（初心者向け徹底解説）](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNjxNpoXlsyNjR8lOszPROEyyJmC1oYMLObpibyB2JVHwIVqeAlOofqTwDEz3ibjqb8oebwBFrLiazsgzNzzJG7ZV49lPuv65nxsfk/640?wx_fmt=png&from=appmsg)

截至5月7日，Shadowserver Foundation监测到超过44,000个独立IP从事扫描和利用活动，全球至少40,000台服务器已被攻陷。Censys的数据显示，其中8,859台主机上出现了".sorry"勒索软件文件标记，7,135台确认为cPanel/WHM服务器。

多家安全厂商确认，该漏洞在cPanel官方于4月28日发布补丁之前至少30天就已经在野利用。5月1日，CISA将该漏洞纳入已知被利用漏洞（KEV）目录。但目前来看，仍有大量服务器未完成修补。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNgxdwg6fZJXEjiaV6xK6iawj52kiaQALX5Y3ickOkz4ApAAXyicdCCG9icZ9BZTdqba6TibY3kWGsY00wDO668wxjicvcnBnRph2ibqwYuE/640?wx_fmt=png&from=appmsg)

这场攻击涉及的不仅仅是一个漏洞，而是一整套攻击链条。Sorry勒索软件、Mirai僵尸网络、国家背景APT攻击……多种威胁同时在cPanel这个脆弱的入口上叠加。

我在知识星球「隐侠技术客栈」同步更新了事件进展。这里先拆解一下漏洞本身的技术细节。

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNiaPUxibTmcRMASLzCu9Dp28ZFgLBYQC4uf4UqKoCrebM5q89l8awzo54SBJicm90mwcLYDFGiaWknm8DdG4AFnaVrqGbceQSzM6uo/640?wx_fmt=png&from=appmsg)

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

三个环节组成的认证绕过

01

CVE-2026-41940不是单点漏洞，而是由三个逻辑缺陷链式组合形成的认证绕过。

第一环：Session文件写入与CRLF注入

cPanel的session以文件形式存储在/var/cpanel/sessions/raw/:<id>。格式是扁平的key=value列表，每行一条记录。文件中存储的内容包括user、pass、hasroot、tfa\_verified等字段。

当session加载器读到successful\_internal\_auth\_with\_timestamp这个字段时，会将会话标记为已认证。攻击者要做的，就是把这个字段写进session文件。

问题出在Cpanel::Session::saveSession()函数——它在写入session文件之前，没有调用filter\_sessiondata()进行CRLF过滤。对比来看，另一个函数Cpanel::Session::create()则会正常调用filter\_sessiondata()。

这意味着攻击者可以在Basic认证头的password字段中嵌入\r\n字符，向session文件中注入额外的key=value行：

```
Authorization: Basic base64("任意内容\nuser=root\nhasroot=1\ntfa_verified=1\nsuccessful_internal_auth_with_timestamp=1746000000")
```

```
每一行被写入session文件后，都会成为独立的记录。
```

第二环：ob段的加密绕过

cPanel登录后会下发一个whostmgrsession cookie，格式为whostmgrsession=<base>,<obhex>。<obhex>是一个32字符的十六进制串，用作per-session编码密钥。当ob段存在时，cPanel会对pass字段进行对称加密。

然而，如果攻击者构造一个不带ob段的cookie（只有whostmgrsession=<base>，没有逗号及后面的内容），cpsrvd会跳过加密流程，直接将Basic认证头的密码原样写入session文件。

这被称为一段"bypassing the encryption process"，由Github安全研究员Ryan Emmons（Rapid7）发现并披露。

第三环：Cache晋升机制

session文件写入了还不够，cPanel还有一个缓存机制。攻击者需要通过/scripts2/listaccts等无需cp\_security\_token的端点，触发session加载器读取磁盘上的session文件，将恶意字段晋升到活跃缓存中。这个过程在内部称为cache promotion。

至此，攻击者完成了一次完整的认证绕过——不需要知道任何真实凭据，不需要绕过双因素认证，因为在注入阶段已经写入了tfa\_verified=1。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

从漏洞到勒索：四阶段的攻击链路

02

综合多方分析，攻击链条如下：

![](https://mmbiz.qpic.cn/mmbiz_png/AwziaxUyibcNiatrNibZ4cYUFpHGiaW18YOO1q54Jb2Kj9dH8ldDINQoUiaibXsY9HUzjmkNx2sofoHQmOVpYuLZibtEF2jxtdoXcXFR73k5ZnlIa84/640?wx_fmt=png&from=appmsg)

1. 阶段1：Session预创建— 向目标2087端口发送带有无效凭据的登录请求，获取 cookie。
2. 阶段2：CRLF载荷注入— 去掉cookie中的ob段，构造含CRLF序列的Basic Authorization头重放请求。注入whostmgrsession、user=root、hasroot=1、tfa\_verified=1、successful\_internal\_auth\_with\_timestamp、/scripts2/listaccts等字段。
3. 阶段3：Cache晋升— 请求 端点，触发session加载器从磁盘读取raw session文件，将所有注入字段加载到缓存。
4. 阶段4：权限获取与横向移动— 通过WHM界面执行命令、修改root密码、安装后门。cPanelSniper工具在这一阶段提供交互式Shell访问，支持批量操作。

补丁发布后72小时内，安全研究员Mitsec公开了名为"cPanelSniper"的武器化PoC。这是一个纯Python 3.8+实现的零依赖工具，支持批量扫描、Subfinder/Shodan管道集成、交互式WHM Shell访问。

随着PoC公开，攻击活动迅速扩散。攻击者IP为95.111.250[.]175，使用公开PoC对全球目标进行批量扫描。攻击目标集中在菲律宾军方（.mil.ph）、老挝政府门户（.gov.la）、印尼国防训练门户，以及多个国家的托管服务提供商（MSP）。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

根因思考：为什么一个"老漏洞"能瘫痪全球4万台服务器

03

站在技术和事件之外，有几个更值得思考的问题。

第一，代码路径分化是安全漏洞的温床。

saveSession()和create()两个函数处理着本质上相同的逻辑——将session数据写入文件。但一个调用了filter\_sessiondata()，另一个没有。cPanel是一个运行了二十多年的成熟软件，session模块经过了无数次迭代，不同开发者在不同时期为该模块贡献了不同的代码路径。当新代码路径加强了安全过滤，旧路径却未被同步修改时，漏洞就埋下了。

这种情况在很多长期维护的大型项目中都存在。一个函数加了安全检查，另一个功能相似的函数却因为"没人记得"而遗漏了。

第二，CRLF注入——一类已经存在了30年的漏洞，依然能在最核心的认证模块中打出致命伤害。

这种攻击手法在上世纪90年代末的HTTP规范讨论中就已经被广泛认识。但在2026年，它仍然是cPanel认证绕过的关键环节。安全行业在"发现新漏洞"上投入了大量精力，但基础类型漏洞的防御还没有真正覆盖到每一行代码。

第三，供应链攻击的规模化效应。

攻击者选择MSP作为切入点是典型的供应链策略。一家托管服务商被攻陷，可能意味着成百上千的下游客户同时暴露。HIBP的数据显示，Game社区Reborn Gaming已有约126个账户因此次攻击被泄露。这还只是直接可见的损失。

对于使用了托管服务的企业来说，自身的防护能力再强，也受制于上游服务商的安全水位。CISO需要的不只是内部安全策略，还需要对供应商安全做实际的审查。

第四，从补丁到大规模利用的时间窗口正在缩短。

cPanel在4月28日发布补丁，5月1日cPanelSniper PoC公开，5月3日大规模自动化扫描开始。72小时内，从补丁发布到自动化利用完成周转。这不是最快的，但趋势很明显——攻击者的自动化程度和响应速度都在提升。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

防御建议

04

如果你的服务器还在用cPanel：

* 立即升级至11.86.0.41及以上版本

* 限制WHM端口（2087）的入站流量，仅允许可信IP访问

* 排查 目录下是否存在包含异常字段的session文件/var/cpanel/sessions/raw/

* 检查access日志中是否存在大量无 的 请求cp\_security\_token的/scripts2/listaccts

* 使用cPanel官方的IOC检测脚本 进行检查ioc\_checksessions\_files.sh

如果你在安全团队，建议关注以下信号：.sorry文件扩展名、异常的cPanel/WHM登录日志、以及大量发往2087端口的畸形的HTTP请求。

关于这次事件的更详细技术分析，包括完整的session文件格式解析、whostmgrsession cookie的各个字段含义、绕过背后的代码分析，已经发布在知识星球「隐侠技术客栈」。

此次事件的IoC列表、检测脚本的详细使用方法，也会在星球内持续更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AwziaxUyibcNhvia0xYaSlEqiboc2r3madpib329upZ0jlVWdtmwofSFYxI0SpBq8Xfm5ONwc4L8ZickkMKDTicqdMaQxsJLCdgiacVcguWLqqerUT8/640?wx_fmt=jpeg&from=appmsg)![]()

加入我们，和众多安全从业者一起追踪前沿威胁。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

参考资讯

05

* https://www.securityweek.com/over-40000-servers-compromised-in-ongoing-cpanel-exploitation/
* https://thehackernews.com/2026/05/critical-cpanel-vulnerability.html

* https://www.bleepingcomputer.com/news/security/critical-cpanel-flaw-mass-exploited-in-sorry-ransomware-attacks/
* https://www.picussecurity.com/resource/blog/cve-2026-41940-explained-cpanel-whm-authentication-bypass-hit-1-5m-servers
* https://www.helpnetsecurity.com/2026/05/05/cve-2026-41940-cpanel-exploited/
* https://nvd.nist.gov/vuln/detail/CVE-2026-41940
* https://github.com/ynsmroztas/cPanelSniper

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icqGYtiaRQqH60REFUK5n2iaTH2Ifziba6pa3aNz9ofOyXMqhhszN46Jl2IWB3mBT41SS9kywiaJN52zxTqxvLfn0UA/0?wx_fmt=png)

东方隐侠安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icqGYtiaRQqH60REFUK5n2iaTH2Ifziba6pa3aNz9ofOyXMqhhszN46Jl2IWB3mBT41SS9kywiaJN52zxTqxvLfn0UA/0?wx_fmt=png)

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