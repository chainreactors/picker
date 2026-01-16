---
title: Microsoft SQL Server 存在允许攻击者通过网络提升权限漏洞
url: https://mp.weixin.qq.com/s/UCWuVh9FyPK4UuHDSnQyTw
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:27:20.574301
---

# Microsoft SQL Server 存在允许攻击者通过网络提升权限漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo4tv2I8icIGyC9JYH01gxjPlGHuOYusJcCDe369e9iaiaEJsJLyak4oyRjOMib1PYBwGDUPbzqbnMX4mg/0?wx_fmt=jpeg)

# Microsoft SQL Server 存在允许攻击者通过网络提升权限漏洞

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo4tv2I8icIGyC9JYH01gxjPlnGj5LEUpN0QMUayYo53qFuz9vYdiachkyC9wjE1IIpsDYkKSSib10dgQ/640?wx_fmt=jpeg&from=appmsg)

微软于2026年1月13日发布安全更新，修复SQL Server中的一个关键权限提升漏洞。该漏洞允许已授权的攻击者绕过身份验证控制，远程获取更高的系统权限。

该漏洞被追踪为CVE-2026-20803，其根本原因是数据库引擎关键功能缺少身份验证机制。漏洞影响多个SQL Server版本，包括SQL Server 2022和最新发布的SQL Server 2025。该漏洞CVSS评分为7.2，微软将其严重等级定为"Important"。

攻击需具备高权限账户和网络访问权限，但一旦利用成功，攻击者可获得内存转储、调试访问等高危能力，可能进一步导致系统被完全控制。

| CVE编号 | 严重等级 | CVSS评分 | 攻击向量 |
| --- | --- | --- | --- |
| CVE-2026-20803 | Important | 7.2 | 网络 |

漏洞细节与影响

CVE-2026-20803利用了CWE-306（关键功能缺失身份验证）漏洞，允许具备高权限的认证用户突破权限边界。攻击者可借此获取调试权限、转储敏感内存内容，甚至访问加密数据或内存中的数据库凭证。

漏洞发布时被评估为"较低可能性"被利用，因其需要特定前置条件，短期内大规模利用的可能性较低。微软目前未收到在野利用报告或公开披露尝试。

微软通过常规分发版（GDR）和累积更新（CU）路径为受影响的SQL Server版本提供安全更新。运行SQL Server 2022的组织应安装CU22（版本16.0.4230.2）或RTM GDR（版本16.0.1165.1）。SQL Server 2025用户需安装2026年1月GDR更新（版本17.0.1050.2）。

建议优先修补面向公网的系统或处理敏感数据的系统。微软建议审查部署架构并限制管理员访问权限，以在更新窗口期间降低利用风险。

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