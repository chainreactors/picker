---
title: cPanel EmailTrack 再现致命 SQL 注入——一次低权限提权如何撬动共享托管信任
url: https://mp.weixin.qq.com/s/ejhxyH4UNEF-aMTxiaBYbg
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:47:25.808439
---

# cPanel EmailTrack 再现致命 SQL 注入——一次低权限提权如何撬动共享托管信任

# cPanel EmailTrack 再现致命 SQL 注入——一次低权限提权如何撬动共享托管信任

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OsD6dqdtzc8GtllaIlmyMqpVicPdv5AGhzEz4XX9Hic3iaHnDM656hlEEPSkxiaGIbWDdXibyfhOM8YQAuIPAUHjtLLTMTKnkK2iagU/640?from=appmsg)
> **导语**：9 月 8 日，全球装机量最大的虚拟主机控制面板 cPanel 发布紧急安全公告，确认其 EmailTrack 功能存在 SQL 注入漏洞 CVE-2026-67401，CVSS 评分高达 9.9 分。一个仅拥有邮件权限的认证账户，即可在服务器任意位置写入文件并以 root 身份执行命令——所有受支持版本均在影响之列。

---

## 一、事件回顾：一次邮件权限，零成本拿走整台服务器

根据 cPanel 官方公告与多家安全研究机构的复现报告，这条攻击链并不复杂。攻击者首先需要一个已认证的 cPanel 账户，并且该账户被授予了邮件相关权限——这是绝大多数 cPanel 共享托管方案的默认配置，几乎人人都有。接下来，攻击者向 EmailTrack 接口提交一段精心构造的 SQL 语句触发注入，再借助 SQL 的 INTO OUTFILE 能力把 Webshell 或可执行文件落到服务器的任意目录。由于 EmailTrack 在执行链路中以高权限上下文运行，落地的文件随即获得执行路径，最终以 root 身份被加载——账户背后的攻击者便完成了从"邮箱小喽啰"到"整台服务器主宰者"的身份跃迁。

![从邮件权限到 root 的提权链路](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NzHIjlP3Wia2m4hWQgwic4B1B42fAzA0ldxbTYHE8j6BibcoJjOAK69a9peIF2iaYB8C6y8ZULxrOVw1icOtM2PbGlZdR1mKvyroko/640?from=appmsg "从邮件权限到 root 的提权链路")

cPanel 在公告里写得很克制但分量极重："every supported version was affected（每个受支持版本均受影响）"。考虑到 cPanel 在全球虚拟主机市场的装机量——数百万台服务器、覆盖海量中小企业官网、电商独立站与个人站点——这一漏洞的潜在爆炸半径远超一般的 Web 应用 CVE。

---

## 二、行业信号：2026 年，cPanel 第三次因为"低权限直达 root"翻车

把视角拉远，2026 年并非 cPanel 第一次因"低权限到 root"的提权链被推上风口浪尖。1 月，CVE-2026-65643 让拥有域名控制权限的认证账户同样可以以 root 身份执行代码；5 月，CISA 将 CVE-2026-48172（LiteSpeed cPanel 插件的权限提升漏洞）加入已知被利用漏洞目录（KEV），强调其可被任意 cPanel 用户以 root 身份执行任意脚本；9 月，本次 CVE-2026-67401 再一次把"邮件权限"这一几乎人手一份的低门槛权限，变成 root 的入口。

三次漏洞，三个完全不同的功能模块，踩进的是同一类陷阱：**共享托管架构里那条"账户—服务器"的信任边界，从来都没有真正被认真设计过**。EmailTrack、域名控制、LiteSpeed 插件——它们每一次成为漏洞的载体，都是因为控制面板在向某个子功能授权时，沿用了过高的执行上下文。一旦 SQL 注入、命令注入、反序列化这些"古典"漏洞嵌入这一上下文，root 便不再遥远。

从商业角度看，这种"邻居即攻击者"（neighbor-as-attacker）的威胁模型，正在成为共享托管行业的结构性风险。对托管服务商而言，每一次这样的 CVE 都是一次客户信任的扣分；对采购方而言，再"物美价廉"的共享托管方案，都需要重新计算一次真实的安全边际成本。

---

## 三、对中小企业的冲击：便宜的代价

对把网站、邮件、小型 SaaS 业务部署在共享 cPanel 主机上的中小企业来说，本次漏洞有几个特殊属性。

**第一，攻击门槛极低。** 不需要 0day，不需要社工，只需要一个被分配的 cPanel 账户——无论是自己注册、批量购买、还是从数据泄露里拿到——再加上基础的 SQL 注入知识即可。

**第二，被入侵后的取证极其困难。** 共享托管环境下数百个账户共用同一台服务器，攻击者提权到 root 后可以轻易抹除 Web 日志、邮件日志、数据库 binlog，痕迹被淹没在正常流量中。中小企业几乎不具备专业取证能力，往往要等到"网站突然变成博彩页"或"客户收到钓鱼邮件"才后知后觉。

**第三，合规风险被连锁放大。** PCI DSS 4.0 在共享托管环境上有专门的 A.1 条款，要求服务商隔离每个客户的运行环境；GDPR、HIPAA 等法规对个人数据的处理环境同样有隔离要求。当一台共享主机沦陷，所有客户的数据都将被视为"未授权访问"——这意味着一次漏洞利用可能引发连锁的数据泄露通报义务。

---

## 四、对托管巨头的警醒：护城河正被基础错误撕开

对 Bluehost、HostGator、SiteGround 这些大型 cPanel 经销商而言，本次事件再次提醒：分销品牌再响亮，安全责任的最终落点仍是底层控制面板的质量。短期看，业务团队必须主动联系 cPanel 官方确认补丁推送时间表，对自营的每一台服务器执行强制升级检查；同时建议向客户发布临时缓解指南，例如关闭非必要的邮件跟踪功能、限制 cPanel 账户登录的 IP 段、强制开启两步验证。

中长期看，巨头们需要重新审视"基础控制面板 + 增值插件"这条生态链是否健康。LiteSpeed、Imunify360、Softaculous 等第三方插件与 cPanel 核心深度耦合，每一次插件层的漏洞都可能穿透控制面板自身的防御。一个值得投入的方向是引入"最小特权 + 容器化"重写控制面板的子功能，让每个用户态操作都在独立的非特权命名空间内执行，从架构上消除"低权限直达 root"的物理路径。

---

## 五、普通用户能做什么

对使用 cPanel 共享主机的个人站长与中小团队，建议立即执行以下五步：

* 登录 WHM，确认 cPanel 版本已升级至官方公告要求的修复版本，未达标者立即联系服务商；
* 在 EmailTrack 配置中暂时关闭非必需的邮件追踪功能；
* 为所有 cPanel 账户开启两步验证，并绑定手机或硬件密钥；
* 复核全部账户的权限分配，删除已不使用的邮件或域名权限；
* 把网站与数据库备份到异机或对象存储，警惕供应链层面的二次入侵。

---

## 六、写在最后

cPanel 在 2026 年用三次高危漏洞给行业上了一课：**任何把"信任"建立在"账户边界"上的系统，最终都会因为某一处边界的疏忽而整体失守**。对正在选型或续约虚拟主机的企业而言，本次 CVE-2026-67401 不只是"又一个需要打补丁的 CVE"，而是一次重新审视"共享托管是否还匹配你当前业务体量"的契机。当控制面板本身的提权成本低到可以忽略，再厚的安全运营都只是在外围修补。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NiaZe9icuVzqxTGicrzjKHVrZlK8w5xYF7wZzhrjyOdd05coa9dZeIzlIt6ESPCibp313sEbunxiaLnCEj49ETKhApZ8Nj80INT2hY/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6MAibgkXrPokze8ExrCLmscic7VeLNX1zT9Kn7tpWYtMib46c6icj6GTjFzx7b81vbNqVDvLYYHWAQaAicCJgfwD7fbA9eibVZbBewXk/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621144&idx=1&sn=895132b6dea5c5055ac21126293661f9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PWjpgp1l9ia655vzyzWURTicOryckXhyHU6v6WtIKTeS5gy5hqAF0N6YzDth0xMkFuPI5SWPuEIcic4mt256aGORvicrVt16S81K8/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621255&idx=4&sn=75d0f413e300d99d4e5cc631714c96ae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6Mj8Z39s8I3WbuovBA4RjSiaric8JibiaHzbnYuic9hx9luicFZcmkxL9wia3ACE18nibrXUk9fGXicnNy7TFyPmehcAAZCRz5fXlgbib3UU/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621242&idx=1&sn=c7504153dd6aa285da53fc1a4a907f82&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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