---
title: CertPotato｜从WebShell到System权限
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247490498&idx=1&sn=7446586ab5519330937242a304838375&chksm=c187dbd3f6f052c5153395600db308692f8455a685f461e24daa7e10e88fe5c9339f66fdc8e3&scene=58&subscene=0#rd
source: M01NTeam
date: 2023-01-05
fetch_date: 2025-10-04T03:04:43.675469
---

# CertPotato｜从WebShell到System权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwYctSsa5QibPJnFmnic62smUvmq2YibVtjTMcvsqgjpClVTcWCHbD8a0d8Eq4hKAwAbOaI7j1JGupjFQ/0?wx_fmt=jpeg)

# CertPotato｜从WebShell到System权限

原创

天元实验室

M01N Team

**01** 简介

本文所介绍的CertPotato是一种能够在AD域环境中从WebShell的服务账户权限提升到本地System权限的技术。虽然名字包含Potato但是并没有利用NTLM中继攻击，其实现主要依赖于ADCS和TGT委派。成功的关键需要以下几个条件：

1. 当前WebShell是以服务账户运行的
2. 存在AD域环境且配置了ADCS服务
3. CA包含可以注册且包含可进行身份验证EKU的证书模板

**02**实现过程

一般情况下Windows服务在服务账户上下文中运行，服务账户大部分都不属于域账户，这样CertPotato中关键的一环申请ADCS证书就无法完成，因此第一步是需要获取一个有效的域账户用于申请证书。Windows中常用的服务账户包含以下六种：

|  |  |  |
| --- | --- | --- |
| 账户类型 | 本地管理员  权限 | 认证账户（域内） |
| LocalSystem | 有 | 机器账户 |
| NetworkService | 无 | 机器账户 |
| LocalService | 无 | 匿名 |
| sMSA | 无 | 自身 |
| gMSA | 无 | 自身 |
| 虚拟账户 | 无 | 机器账户 |

分析以上账户，LocalSystem和LocalService可以忽略，其他账户申请ADCS证书需要自身或机器账户的认证材料，认证材料可以是Hash或TGT票证。其中gMSA（组托管服务账户）和sMSA（独立托管服务账户）都是域账户需要本身的账户认证材料。NetworkService和虚拟账户在AD域内无法进行身份认证，需要借助所在主机的域机器账户进行身份认证。CertPotato提权方式所针对的就是NetworkService和虚拟账户的Webshell提权。

如果当前获取了IIS服务的WebShell，默认情况下IIS中进程所运行的账户为IIS程序池虚拟账户defaultapppool。下图为在IIS中上传执行命令的WebShell后运行whoami命令的结果。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYctSsa5QibPJnFmnic62smUv01r9YCkWXd6q9X9o2j182Auhq90aJ7sPicFvrMt5J7MZ2ohVWoZxIog/640?wx_fmt=png)

但是由于defaultapppool是虚拟账户不属于AD域。因此IIS中的进程在AD域中进行认证时，所使用的账户是所在主机的机器账户。下图是使用impacket开启SMB服务器并使用IIS中的Webshell访问SMB共享的结果，可以看到认证的账户是机器账户。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYctSsa5QibPJnFmnic62smUveTQGr0KrA7ibCbxB3zzxXWyDm705gzWSPAib8VMahLFhLTUiaG4QD7vBw/640?wx_fmt=png)

此时可以借助TGT委派技巧获取IIS所在主机的机器账户TGT。在使用非约束委派时，AP-REQ中的Authenticator使用与TGS-REP中TGS相同的服务会话密钥加密，在TGS-REP中包含一个委派TGT，该TGT具有与想要使用无约束委托访问服务的用户相关联的密钥。使用SSPI/GSS-API的函数，特别是InitializeSecurityContext()函数并提供目标SPN，可以获得一个SSPI SecBuffer结构恢复AP-REQ。加密Authenticator的会话密钥可以从本地Kerberos缓存中检索，解密通过解密Authenticator可以获得委派TGT。TGT委派的优点是不论当前账户是否被授予委派权限都能获得委派TGT。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYctSsa5QibPJnFmnic62smUvibxCibicAhKhbic8ibFWoBvunDsmq7tic3d8b10IicRM27PrIcLBFfOCdM7Wg/640?wx_fmt=png)

使用Rubeus中的tgtdeleg功能可以获得委派TGT。需要注意的是，经过测试仅当在Server版本的Windows系统中能够直接获得TGT，在非Server版本的系统中需要提权到本地管理员才能成功执行。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYctSsa5QibPJnFmnic62smUvbGlTAcEJmmSmbNLabngeAxNe3M7iaadlBmDRmic1ImKrSUl8GKCC2fBQ/640?wx_fmt=png)

在获得TGT后，可以使用TGT申请AD CS证书，使用前需要转换为ccache格式才能写入环境变量。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYctSsa5QibPJnFmnic62smUv3suqN0HrHJc3TgvPd8bdwhaWaVlKTw3cVHT4D8fLOfvSp8FTyM2RcA/640?wx_fmt=png)

在Linux系统中将票据写入环境变量KRB5CCNAME中即可用于身份认证，使用klist命令可以查看缓存中的票据。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYctSsa5QibPJnFmnic62smUv56GygyWoRj4YMwHXRwb2BBMnkMo9zDiaOiaPRegMTFpuSW10iaR1OfmdQ/640?wx_fmt=png)

在成功将票据写入缓存中后，可以使用Certipy工具申请票据。此时注意需要为主机配置DNS信息防止无法根据名称找到CA服务器。此处申请了一个与主机名相同的pfx证书。申请的票据模板需要包含以下5个EKU之一，票据才能用于后续的身份验证：

1. 客户端认证
2. PKINIT 客户端认证
3. 智能卡登录
4. 任何目的
5. SubCA

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYctSsa5QibPJnFmnic62smUvzzbu4zRmntmhxOhe6NYcB14cibccbzWLQMkBHdoWxoHCeUhZyicECoMg/640?wx_fmt=png)

在获得证书后，利用PKINIT身份验证和U2U扩展，可以获得机器帐户的哈希值。实际上到这一步提权的过程基本完成，获取的账户本身就拥有DC的CIFS服务的委派权限。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYctSsa5QibPJnFmnic62smUv9ibpG6SKtDtvvIUlKm5CicKwNPbNTffm5A4VJVFrVkqBrOSIEdDscOzg/640?wx_fmt=png)

在成功获取Hash后，就可以制作DC中CIFS服务的白银票据，其中还需要域的SID和CIFS服务的SPN，这些信息都比较容易获取就不再赘述，最后需要指定一个任意的用户名。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYctSsa5QibPJnFmnic62smUv21iaCHvdBAXwCVxXLFwia5aGibBOv9Y5diaFTnPfCrCEQvNmuRYCoghqOA/640?wx_fmt=png)

再次将生成的白银票据写入缓存，并使用psexec进行横向。票据可用则会返回一个CMD的Shell，执行whoami命令发现当前为nt authority/system，此时已经成功将虚拟服务区权限提升到本地System权限。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYctSsa5QibPJnFmnic62smUvs0MEibfMJfYYAlPQSgyibSDET4Wx5OlicfOTwIdgJ4B2K640RuBY1NC1Q/640?wx_fmt=png)

最后，回顾CertPotato整个利用过程并总结如下：

1. 使用WebShell上传Rubeus进行TGT委派，获取机器账户的委派TGT
2. 将TGT写入环境变量
3. 使用TGT认证向CA申请证书
4. 使用证书获取机器账户Hash
5. 使用Hash和并搜集其他制作白银票据所需参数，申请DC CIFS服务的服务票据
6. 将白银票据写入环境变量，进行psexec获取System权限的Shell

**03**总结

这是一种非常有趣的本地提权方式，主要是利用了TGT委派和AD CS认证，其中最关键的一环就是使用TGT委派技巧获得了有效的TGT。获得机器账户后的TGT之后还可以通过Shadow Credentials技术获得NT Hash。因为攻击是多步骤的，因此可以通过中断攻击链的方式阻断攻击，如限制账户可申请证书模板，使攻击者无法获得能够认证的证书。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYctSsa5QibPJnFmnic62smUvS0qaEv0vT4AQMwic8epfJa8X5CjZogECLgKJJGX9A0Ck9iax6WICuh8A/640?wx_fmt=png)

**绿盟科技天元实验室**专注于新型攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwYctSsa5QibPJnFmnic62smUvHHhI4oibGXEUaibzeC6Y9Mz4SyvIwPmDTkd85heoqhjuslUJNibKsHsJg/640?wx_fmt=jpeg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwYctSsa5QibPJnFmnic62smUvUguOMRCfzEibpTPx0yQkZico59OMYhpH7pUhk9ZVcRpicEEn1arfXIHkg/640?wx_fmt=jpeg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

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