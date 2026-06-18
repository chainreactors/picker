---
title: Google紧急发布Chrome安全更新，修复可致任意代码执行的关键漏洞
url: https://mp.weixin.qq.com/s/kxS_P0elGBsZtXYGnf4qKQ
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:48:16.132090
---

# Google紧急发布Chrome安全更新，修复可致任意代码执行的关键漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnu8ztjXdQFjIHqAEgREVNRalu8g11PWy8lUvyYMPC7kiacmrYpXVbGFhbIGrUibVGavsia82hFKXNetaCibGwooHmaXYE9oLhHeT0M/0?wx_fmt=jpeg)

# Google紧急发布Chrome安全更新，修复可致任意代码执行的关键漏洞

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnupJ0MIiaBlCpjNwOo3ckgAS7832nuTTtOQ8IRoF6lxibgU15Y0lsNTeRx7RTxuxRQNSprb6j6SKaIzxeEibhbv91YKpUpicpdMncI/640?wx_fmt=png&from=appmsg)

Google已向全球用户推送Chrome紧急安全更新，修复多个关键漏洞。此次更新将Windows/macOS版Chrome升级至149.0.7827.155/.156，Linux版升级至149.0.7827.155。鉴于漏洞的高危性与可利用性，安全研究人员及企业防护团队必须立即应用补丁。

一、漏洞核心风险

1. 高危漏洞集中爆发

本次更新共修复33个安全漏洞，其中7个被标记为"关键"级别。

主要风险类型为内存安全漏洞（如释放后重用），攻击者可借此实现远程代码执行（RCE）。

受影响组件覆盖浏览器核心功能：

WebShare（网页内容共享）

WebView（嵌入式网页渲染）

Digital Credentials（数字凭证）

密码管理与Web认证模块

攻击面显著扩大，恶意网页可直接触发漏洞执行任意代码。

2. 漏洞利用链威胁

释放后重用（Use-after-free）漏洞因内存管理缺陷，使攻击者能操控已释放的内存区域。

结合Chrome的高市场占有率，成功利用可能导致：

大规模系统沦陷

用户凭证窃取

间谍软件或勒索软件投递

二、关键漏洞详情

1. 7个关键漏洞（CVSS评分均≥7.8）

| CVE编号 | 漏洞位置 | 报告时间 | 风险本质 |
| --- | --- | --- | --- |
| CVE-2026-12437 | WebShare | 2026-05-25 | **释放后重用**，可执行任意代码 |
| CVE-2026-12438 | WebView | 2026-05-27 | 实现逻辑缺陷，绕过安全策略 |
| CVE-2026-12439 | Digital Credentials | 2026-06-03 | 释放后重用，突破凭证隔离机制 |
| CVE-2026-12440 | Digital Credentials | 2026-06-03 | 释放后重用，关联凭证数据泄露 |
| CVE-2026-12441 | File Input | 2026-06-05 | 释放后重用，操控文件上传流程 |
| CVE-2026-12442 | 密码管理模块 | 2026-06-09 | 释放后重用，窃取加密存储的密码 |
| CVE-2026-12443 | Web认证 | 2026-06-11 | 释放后重用，劫持身份验证流程 |

2. 其他高危风险组件

远程访问与扩展生态：

Chromoting（远程桌面）及扩展程序存在多个释放后重用漏洞（CVE-2026-12444等），诱导用户安装恶意扩展即可触发攻击。

实时通信功能：

WebRTC与媒体模块的堆缓冲区溢出（CVE-2026-12447等）可通过特制音视频流量触发，导致系统崩溃或信息泄露。

输入验证缺陷：

密码管理、文件系统访问等模块存在策略执行不足问题（CVE-2026-12460等），攻击者可绕过安全限制。

三、修复与应对建议

1. 紧急处置措施

立即升级至最新版本：

通过 设置 → 关于Chrome 手动触发更新，或等待自动推送完成。

企业环境优先级：

验证终端设备的Chrome版本合规性

监控异常浏览器活动（如非预期进程创建）

限制非必要扩展安装权限，防范恶意扩展链攻击

2. 漏洞防御背景

Google未公开技术细节以避免漏洞被武器化，但内存破坏类漏洞高度可能被组合利用。

攻击者通常将此类漏洞与沙箱逃逸技术结合，实现系统级控制。

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