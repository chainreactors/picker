---
title: 微软Edge浏览器启动时将所有保存的密码以明文形式存入进程内存
url: https://mp.weixin.qq.com/s/xnYkmRGqBMcIumvmG8aU2w
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:25:21.524824
---

# 微软Edge浏览器启动时将所有保存的密码以明文形式存入进程内存

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJntqnrU31hFcupsvrcsibZ466icJVqbaicl7NE0nsNeiavQNyhoMKDzJMibBibzQR63vc2CpfYz8yEISHIDIgfo64vZ5X9BARU3LxpYbc/0?wx_fmt=jpeg)

# 微软Edge浏览器启动时将所有保存的密码以明文形式存入进程内存

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnsBwIB3fMRxl9I5ASW7UQmXAuOWibMTcvvggEDlyeUbpk1vZ9vEFn0GZicibicoqkg4BCmwH9BQyNj8J4iaokK07ibWp3pbE6pAOMSeg/640?wx_fmt=png&from=appmsg)

安全研究人员发现，Microsoft Edge在浏览器启动的瞬间便会将所有已保存密码解密至进程内存，并以明文形式持续驻留，无论用户是否访问过相关网站。

该发现由PaloAltoNtwks Norway于4月29日在BigBiteOfTech平台披露，研究员@L1v1ng0ffTh3L4N系统测试了所有主流基于Chromium的浏览器凭证内存处理行为后确认。

Edge是唯一表现出此行为的浏览器，它在启动时即加载全部密码保险库至明文进程内存，并在整个会话期间持续保留。

与Google Chrome的对比尤为鲜明。Chrome采用按需解密机制，即凭证仅在自动填充过程中或用户主动查看已保存密码时才会解密。

Chrome进一步通过应用绑定加密（App-Bound Encryption）强化防护，将解密密钥加密绑定至经过身份验证的Chrome进程，阻止其他进程复用密钥访问凭证。

Edge未提供任何此类保护。从浏览器启动伊始，用户保险库中所有网站的已保存凭证即以明文形式存在于浏览器进程内存中。这为任何能够读取该进程内存的攻击者创造了持续且广泛的凭证提取目标。

使该发现尤为矛盾的是Edge自身的UI行为。浏览器在密码管理器界面显示密码前仍会要求用户重新认证，但浏览器进程早已以明文形式持有所有凭证，任何能查询进程内存的实体均可直接访问。

因此，重新认证验证仅提供了访问控制的假象，对基于内存的凭证提取攻击毫无实际防护作用。

在远程桌面服务（RDS）或终端服务器等共享或多用户环境中，此问题的严重性显著升级。

具备系统管理员权限的攻击者可同时读取所有已登录用户进程的内存。

在披露时发布的概念验证视频中，攻击者通过已沦陷的管理员账户成功从另外两名已登录用户的Edge浏览器进程内存中提取了存储凭证，包括会话已断开但仍处于活跃状态的用户。

这将单次管理员级入侵直接转化为对整个多用户环境的完整凭证收割，与MITRE ATT&CK框架中的T1555.003（从Web浏览器获取凭证）直接对应。

当研究人员向微软进行负责任披露时，该公司的官方回应称此行为属于"设计使然"。

微软现有公开文档承认，在本地攻击条件下浏览器内存中的凭证可能被访问，并将此类场景归类为超出浏览器威胁模型的范畴。

4月29日在BigBiteOfTech发布的披露内容包含一个小型教育性验证工具，允许用户确认其Edge浏览器是否在进程内存中保留明文凭证。该工具旨在提高风险意识并鼓励用户独立验证此行为。

部署了Edge的Windows环境管理团队，尤其是运营终端服务器、VDI环境或任何共享访问系统的团队，应将此视为高优先级配置风险，并考虑迁移至支持按需解密和应用绑定加密的浏览器，直至微软调整此设计决策。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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