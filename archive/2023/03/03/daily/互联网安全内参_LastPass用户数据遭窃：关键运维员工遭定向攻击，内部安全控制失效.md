---
title: LastPass用户数据遭窃：关键运维员工遭定向攻击，内部安全控制失效
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507965&idx=1&sn=a4b22a739e9331e63cebebcbb09b7b10&chksm=ebfa98dddc8d11cbba84fd3bb96f37b06f35954a4e01bc49f4352ec3da109a4b00fc66f58573&scene=58&subscene=0#rd
source: 互联网安全内参
date: 2023-03-03
fetch_date: 2025-10-04T08:32:29.396797
---

# LastPass用户数据遭窃：关键运维员工遭定向攻击，内部安全控制失效

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7vy7JJsaokicEdCmnjK9iaBawyS4Jk6TibM2WtzicUfbicz8IQJic9SXXdDG2kVTIe7gQibuciaiaCRQEPavOQ/0?wx_fmt=jpeg)

# LastPass用户数据遭窃：关键运维员工遭定向攻击，内部安全控制失效

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7vy7JJsaokicEdCmnjK9iaBawYZLZb8JvQSj9BNMicWHxaEh3fML5zkGibMYZt6vUIIFd1THM9LIuuKVA/640?wx_fmt=jpeg)

**由于恶意黑客窃取并使用了有效的访问凭证，LastPass的安全人员难以检测到对手活动，导致其从LastPass的云存储服务器处访问并窃取到大量数据，持续驻留达两个月以上。**

前情回顾·**我怎么被黑的？**

* [网络巨头思科遭数据勒索：VPN访问权限被窃取，2.8GB数据泄露](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247505152&idx=1&sn=5ffff5ec24e52fb82408e0abd7f2c50f&chksm=ebfa9220dc8d1b36f288c38ff8b5e8a9ca9dd2d704405128b938f852bb3e3d35403f3f1b6355&scene=21#wechat_redirect)
* [微软被指旗下产品遭滥用攻击客户，一家美国顶级安全公司险些被黑](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247494128&idx=1&sn=80d776608f4f3726e8018bdc1ad2757a&chksm=ebfaaed0dc8d27c647f9bbd566d3093b7a74b3e69ca96fd798c037caa7d867906e5f5cd7fb6c&scene=21#wechat_redirect)
* [我看见你在黑我了！乌克兰国安公开警告俄罗斯APT组织](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247500103&idx=1&sn=dfc5a38f30008162ec81fa29bb834d42&chksm=ebfa8667dc8d0f710823d17805b6a23e06182a6665d8b5d2db4bed701e73fa80db850028bae7&scene=21#wechat_redirect)

安全内参3月2日消息，密码管理供应商LastPass日前公布了去年遭受[“二次协同攻击”事件](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247507318&idx=2&sn=54d6830e1f55a4f9eeb9d8cbf8859fbb&chksm=ebfa9a56dc8d1340d6132f624f8f2bc66c0acaf8ffa4d292a8cabf0e9c785ac2965c2aae7bd0&scene=21#wechat_redirect)的更多信息，发现**恶意黑客潜伏在其内网长达两个月的时间内，持续访问并窃取了亚马逊AWS云存储中的数据**。

据安全内参了解，“二次协同攻击”事件，是指LastPass在2022年8月、12月先后披露的两起违规事件，这两起事件的攻击链有关联。

**关键运维员工遭定向攻击**

LastPass在去年12月透露，恶意黑客窃取到部分加密的密码保险库数据和客户信息。现在，该公司进一步解释了恶意黑客的攻击实施方法，称**对方使用到了去年8月首次入侵时窃取的信息**，还**利用一个远程代码执行漏洞，在一名高级DevOps工程师的计算机上安装了键盘记录器**。

LastPass表示，二次协同攻击利用到了首轮违规中外泄的数据，并访问了该公司经过加密的Amazon S3存储桶。

LastPass公司只有4位DevOps工程师有权访问这些解密密钥，因此恶意黑客将矛头指向了其中一名工程师。最终，**黑客利用第三方媒体软件包中的远程代码执行漏洞，在该员工的设备上成功安装了键盘记录器**。

“恶意黑客成功获取了员工在完成多因素身份验证（MFA）后输入的主密码（master password），借此**获得了该DevOps工程师对LastPass企业密码保险库的访问权**。”LastPass日前发布的最新安全警告称。

“恶意黑客随后导出了共享文件夹中的本地企业密码保险库条目和内容，其中包括能够访问LastPass AWS S3生产备份、其他云存储资源以及部分相关重要数据库备份的安全注释和加密密钥。”

**由于恶意黑客窃取并使用了有效的访问凭证，LastPass的调查人员很难检测到对方活动，导致其顺利从LastPass的云存储服务器处访问并窃取到大量数据**。恶意黑客甚至持续驻留达两个月以上，从2022年8月12日一直到2022年10月26日。

直到恶意黑客尝试用云身份和访问管理（IAM）角色执行未授权操作时，**LastPass才最终通过AWS GuardDuty警报检测到这些异常行为**。

该公司表示，他们已经更新了安全机制，包括对敏感凭证及身份验证密钥/令牌进行轮换、撤销证书、添加其他记录与警报，以及执行更严格的安全策略等。

**大量数据已被访问**

作为此次披露的一部分，LastPass还发布了关于攻击中哪些客户信息遭到窃取的具体说明。

根据特定客户的不同，**失窃数据的范围很广且内容多样，包括多因素身份验证****（MFA）****种子值、MFA API集成secreet，以及为联合企业客户提供的Split Knowledge组件（K2）密钥**。

以下是被盗数据内容的基本概括，更详细的失窃信息说明请参阅LastPass支持页面*（https://support.lastpass.com/help/what-data-was-accessed）*。

**事件1中被访问的数据汇总**

**云端按需开发和源代码仓库**——包括全部200个软件代码仓库中的14个。

**来自各代码仓库的内部脚本**——其中包含LastPass secrets和证书。

**内部文档**——描述开发环境运作方式的技术信息。

**事件2中被访问的数据汇总**

**DevOps secrets**——用于访问我们云端备份存储的受保护secrets。

**云备份存储**——包含配置数据API secrets、第三方集成secrets客户元数据，以及所有客户保险库数据的备份。除URL、用于安装LastPass Windows/macOS版软件以及涉及邮件地址的特定用例之外，全部敏感客户保险库数据均通过“零知识架构”进行加密，且只能通过各用户主密码提供的唯一加密密钥实现解密。请注意，LastPass永远不会获取最终用户的主密码，也不会存储或持有主密码——因此，泄露数据中不涉及任何主密码。

**LastPass MFA/联邦数据库备份**——包含LastPass Authenticator的种子值副本，作为MFA备份选项（如果启用）的电话号码，以及供LastPass联邦数据库（如果启用）使用的Split Knowledge组件（即K2「密钥」）。该数据库经过加密，但在第二次违规事件中，恶意黑客窃取了单独存储的解密密钥。

本次发布的支持公告还相当“隐蔽”，由于LastPass公司在公告页面的HTML标签添加了*<meta name="robots" content="noindex">*，因此该页面无法通过搜索引擎直接检索。

LastPass还发布一份题为“安全事件更新与建议操作”的PDF文档，其中包含关于违规和失窃数据的更多信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FzZb53e8g7vy7JJsaokicEdCmnjK9iaBawRhVicISKHOFxOB4XbJWljuLVCYibvm4LPIaBgicx78D7mmwCkoMmWjNJQ/640?wx_fmt=png)

该公司也整理了支持文件，面向免费、付费和家庭客户以及LastPass Business管理员提供应对建议。

通过公告中的建议操作，应可进一步保障您的LastPass账户与相关集成。

**参考资料：bleepingcomputer.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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