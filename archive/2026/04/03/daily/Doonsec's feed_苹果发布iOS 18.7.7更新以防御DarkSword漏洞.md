---
title: 苹果发布iOS 18.7.7更新以防御DarkSword漏洞
url: https://mp.weixin.qq.com/s/hseKSGXo2ZfqwM3eY6IX3Q
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:12:32.886467
---

# 苹果发布iOS 18.7.7更新以防御DarkSword漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnuOLxq62SAtICnAHecialIBOCBiaGLuwqRSfSkX9xM10KHicVZFmHRIOTZwqpqOY9SNPsMPTuWy1KIJTMZxpsloUZbufLSNgfG8qc/0?wx_fmt=jpeg)

# 苹果发布iOS 18.7.7更新以防御DarkSword漏洞

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnsJXVAGhYwZ5zjfrOEV30aoiaDSKkxh2vfLrWVCHpenos8Lvfqb4zy8JfzDic0RbSakleGFqH6AJfEMh5FIIPZ4ln9szBZnpibrgI/640?wx_fmt=png&from=appmsg)

苹果正式扩大了iOS 18.7.7和iPadOS 18.7.7的推送范围，以保护用户免受一种被称为DarkSword漏洞的关键性基于网络的威胁。

该更新最初于2026年3月24日发布，苹果于4月1日通过自动更新向更多设备积极推送，以确保广泛且即时的保护。

**DarkSword威胁**
虽然针对DarkSword漏洞的基础修复程序最早于2025年发布，但此次最新更新为所有受支持的设备带来了强制性的网络攻击防护。

由于DarkSword依赖恶意网络内容来入侵系统，确保所有活跃用户都拥有这些最新的安全定义至关重要。

此次更新覆盖了广泛的硬件范围，支持从iPhone XR到最新iPhone 16系列的各种设备，以及多代iPad产品。

**修复的关键漏洞**

除了DarkSword防护措施外，iOS 18.7.7还解决了超过15个重大安全漏洞。

这些补丁修复了关键漏洞，这些漏洞可能允许威胁行为者访问敏感数据、跟踪用户行为或执行未经授权的代码。

以下是此次版本中解决的最严重漏洞的详细说明：

| 组件 | CVE标识符 | 影响 | 描述 |
| --- | --- | --- | --- |
| 内核 | CVE-2026-20687 | 系统崩溃或未经授权的内核内存写入 | 解决了一个严重的释放后使用内存问题 |
| WebKit | CVE-2026-20643 | 通过网络攻击绕过同源策略 | 修复了导航API中的跨源逻辑问题 |
| 安全 | CVE-2026-28864 | 本地攻击者获取Keychain项目访问权限 | 改进了权限检查以锁定凭证 |
| 剪贴板 | CVE-2026-28866 | 应用程序秘密访问用户复制的敏感数据 | 增强了符号链接验证以防止未经授权的访问 |
| 网络 | CVE-2026-28865 | 从特权位置拦截网络流量 | 修复了802.1X认证状态管理问题 |

苹果在此补丁周期中也高度重视用户隐私。一个值得注意的WebKit漏洞（CVE-2025-43376）已得到解决，该漏洞此前允许远程攻击者即使在启用iCloud私人中继的情况下也能查看泄露的DNS查询。

此外，苹果还修复了iCloud和崩溃报告器中的权限问题（CVE-2026-28880和CVE-2026-28878），这些问题曾允许恶意应用程序秘密扫描和枚举用户设备上安装的其他应用程序。

鉴于DarkSword网络攻击的严重性以及底层内核级漏洞，强烈建议所有苹果用户立即更新其设备。

如果设备尚未自动应用此补丁，用户可以前往"设置" > "通用" > "软件更新"手动触发安装。

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