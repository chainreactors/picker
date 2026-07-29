---
title: 俄情报部门劫持IP摄像头监视军运：87,000台设备暴露，默认密码是最大漏洞
url: https://mp.weixin.qq.com/s/A3VyGaxmz8SJFjsvryGbLg
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T04:58:23.592319
---

# 俄情报部门劫持IP摄像头监视军运：87,000台设备暴露，默认密码是最大漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fTugLXvN07BmAWZp01BcDBEasWOWpbL0FFiadSRW26rD8tqJK8wd72F78qU81MBXYEcmfAhbH6Q6xhkT77GUTEqztibTjJdial6gzZM3IfhGQc/0?wx_fmt=jpeg)

# 俄情报部门劫持IP摄像头监视军运：87,000台设备暴露，默认密码是最大漏洞

老张
老张

信息安全动态

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![俄情报部门劫持IP摄像头监视军运：87,000台设备暴露，默认密码是最大漏洞](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fTugLXvN07B2NGptszGmOwkhtXRnjxtwT7MFVOlkqmFXGAaZ8JDer5QQEMf2qeFXuvibv4iaCCtBorEooUw2AJ4v4vEfQ7eH1zjkOzjBVET2A/640?from=appmsg)

## 摄像头被武装成情报工具

7月10日，荷兰民事与军事情报机构（AIVD和MIVD）联合发布公告，指控至少一个俄罗斯情报部门正在系统性地劫持欧洲及乌克兰境内的联网安全摄像头，利用实时画面监视军事运输路线、运往基辅的武器以及乌克兰军队的部署位置。在乌克兰境内，摄像头访问权已被用于对乌军人员实施定位和攻击——路边或商店的摄像头成了火力校准器。而在欧盟和北约国家，同样的接入被用来收集与俄乌战争无关的军事情报。

## 入侵手法：不依赖零日，全靠“捡漏”

攻击链出奇地简单。俄方操作者扫描互联网，识别暴露的IP摄像头品牌，然后尝试默认密码、过时固件和用户未修改的出厂设置。一旦进入，图像识别软件自动筛选军用车辆及货物。整个入侵不需要任何零日漏洞。荷兰情报机构强调，这种攻击仍在持续，而“进入”几乎从不构成难题——大部分所谓被黑的摄像头，其实是主人自己敞开了门。

## 暴露面惊人：87,000+台摄像头带已知漏洞

互联网扫描公司Censys受委托分析了暴露面。在欧盟、北约成员国和乌克兰境内，Censys发现超过87,000台联网摄像头运行着含有已知被利用漏洞的服务版本，这还只是下限。其中超过4,000台位于乌克兰。在荷兰，Censys找到45,386台可从公网访问的摄像头，1,992台运行着带已知漏洞的服务。

需要说明的是，这些数字统计的是“运行已知存在漏洞的服务版本”的摄像头，不一定是摄像头本身的软件有漏洞。Censys自己也在报告中打了补丁：如果只算摄像头固件本身的漏洞，荷兰的数字降到541台。但Censys坚持用宽口径——因为攻陷一个服务，往往就能接管整个设备。此外，版本匹配不等于漏洞可被利用。Censys重点提到的两个CVE：CVE-2016-7407（Dropbear SSH本地密钥导入工具中的漏洞，2016年修复）和CVE-2021-39275（Apache越界写入，2021年修复），虽然标记为“在野被利用”，但前者需恶意密钥文件触发，后者被Apache评为低危且无默认模块利用路径。两者均未进入美国CISA的已知被利用漏洞目录。荷兰情报机构更保守：他们在本国实际只发现少量摄像头被入侵，且这些摄像头恰好位于军事物流路线附近，相关组织已被通知并修复。

## 安全负责人的三步行动指南

![原文配图 1](https://mmbiz.qpic.cn/mmbiz_jpg/fTugLXvN07BdEfMibKicHoCdj7Zb3JAiaMo2lOpB2XJj49LKvfpMIa32nHH9tKupofJ5zBBpcZKpCiaIkAPc60fsaHT2wxViamPuH6FnYqrIBYQg/640?from=appmsg)

### 弄清哪些摄像头在“裸奔”

立即排查所有公网可达的IP摄像头。检查是否因端口转发、UPnP映射或厂商云中继导致设备暴露。优先处理那些覆盖运输路线、港口、敏感场所的摄像头。查看日志中是否存在异常访问。记住：摄像头能被公网ping通，不等于被黑，但意味着随时可能被黑。

### 切断视频流的公网通路

关闭不必要的端口转发和UPnP，通过VPN远程访问摄像头。对于不支持多因子认证的低端设备，坚决不准其直接暴露在公网。更换默认密码是基本功，但很多人至今没做。

### 镜头对准什么，就赋予它什么权限

调整摄像头物理角度，故意避开物流路线、装卸区等敏感区域。无法避免的，就用物理遮挡或数字遮罩。持续更新固件和软件，采购时优先选择至少提供3-5年安全支持的厂商。

## 物联网暴露面：新的安全边界

荷兰情报机构表示，暂未观察到在乌克兰以外利用摄像头情报发动军事攻击。但威胁的可怕之处在于其“普通”：入侵通常只需默认密码，价值完全取决于摄像头对准了什么。一个失陷的摄像头等于给对手一份实时物理安全情报：卡车何时移动，何人进出。不需要攻破内网，只需要攻破一个摄像头。每台联网摄像头、打印机、门禁控制器都可能成为情报收集的入口。修复不只是打补丁，更要从网络架构和物理部署上切断暴露路径。建议立即启动物联网资产清查，将摄像头暴露面纳入常规安全监控。如果做不到事事完美，至少优先保护那些“看得见敏感位置”的摄像头——对手的优先级比你高得多。

推荐阅读

01[等保测评服务方案](https://mp.weixin.qq.com/s?__biz=Mzg4NDc0Njk1MQ==&mid=2247488276&idx=1&sn=a389431ac91cd8b5aec4de08f759fb37&scene=21#wechat_redirect)

02[100张等保拓扑图案例方案参考](https://mp.weixin.qq.com/s?__biz=Mzg4NDc0Njk1MQ==&mid=2247488253&idx=1&sn=0a5f108f7d05b7030cdf73d09184faf8&scene=21#wechat_redirect)

03[信息安全等级保护培训](https://mp.weixin.qq.com/s?__biz=Mzg4NDc0Njk1MQ==&mid=2247488670&idx=1&sn=40a63bb06236af24c7fd8e6b80eebfb4&scene=21#wechat_redirect)

公众号所有文档加入下方社群获取！

![信息安全](https://mmbiz.qpic.cn/mmbiz_jpg/fTugLXvN07C4PYyYD2Gr3Lx3gf8ZEm0YbPYKSBoPKKhflyWJqkUwvlaM9ULqviaYxK7IcCwbK0MKibJqeLW9VHQ8WE2ic1VDDppPpwAWKZqRhw/640?from=appmsg)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HPjboWok4teVOic0O8dM4CYg3a98MY5sfRJ2uicwq2VcVNH56GGxoWYpH4g3bq1tqhHOFxtfv0ryDt9vSne5JgnQ/0?wx_fmt=png)

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