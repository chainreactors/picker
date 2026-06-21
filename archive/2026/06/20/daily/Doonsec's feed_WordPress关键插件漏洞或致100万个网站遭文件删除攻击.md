---
title: WordPress关键插件漏洞或致100万个网站遭文件删除攻击
url: https://mp.weixin.qq.com/s/uu5K1UMDvRHO2B15oVI1Rg
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:46:05.708887
---

# WordPress关键插件漏洞或致100万个网站遭文件删除攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJntNT22iaVPZU3oB6qj6ZNL66tru093TBIXUaoZxeaU1BzMIIlia0pDE56UDpPKRGSeVLtY4dOgHVsY0icoZmzDNcNgickdQ6ZZwKkA/0?wx_fmt=jpeg)

# WordPress关键插件漏洞或致100万个网站遭文件删除攻击

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnuh7U5fYk3fU8anmFvzK8iaXOkredoUcB6CRLrzeLtfO135hPBJNTIjSNicRUV0WFibGWPwQgEOicSL6G0NpUUWTIaGhtFAzhTib2bI/640?wx_fmt=png&from=appmsg)

广泛使用的 Avada (Fusion) Builder WordPress 插件中发现了一个严重的安全漏洞。该缺陷可能使未经身份验证的攻击者能够删除任意文件，并可能危及超过一百万个安装站点上的整个网站。

该漏洞被标识为 CVE-2026-8713，CVSS 评分为 9.1，影响该插件的所有版本（最高至 3.15.3）。该问题已在 3.15.4 版本中得到解决。安全研究员“daroo”发现了此问题，并通过 Wordfence 漏洞赏金计划进行了报告，获得了 3,600 美元的奖励。

严重的 WordPress 插件漏洞

该漏洞源于插件的 Fusion\_Form\_DB\_Entries 类中 maybe\_delete\_files() 函数内的文件路径验证不足。Avada Builder 包含一个表单功能，该功能将用户提交的内容存储在数据库中，随后使用隐私清理机制对其进行处理。

此清理例程旨在在定义的过期时间段后删除或匿名化存储的条目。然而，由于不正确的清理和缺乏路径规范化，该函数无法验证文件路径是否保留在预期的上传目录内。

攻击者可以利用此弱点，通过提交包含路径遍历序列的特制表单输入。由于插件没有使用像 realpath() 这样的函数来强制目录边界，恶意路径（例如对上传目录外敏感文件的引用）会被保留下来。

当清理过程执行时，它会将攻击者控制的 URL 转换为文件系统路径，并将其传递给 WordPress 的 wp\_delete\_file() 函数，该函数会删除服务器上的任意文件。

利用该漏洞需要一个配置为将条目存储在数据库中的、公开可访问的 Avada 表单。未经身份验证的攻击者可以向 wp\_ajax\_nopriv\_fusion\_form\_submit\_ajax 端点发送请求，将恶意负载注入表单数据中，同时操纵 fusion\_privacy\_expiration\_interval 和 privacy\_expiration\_action 等参数以触发立即删除。然后，清理例程会通过关闭钩子（shutdown hook）自动处理该条目，无需管理员交互。

一个特别危险的结果是攻击者删除关键文件，如 wp-config.php。删除此文件会迫使 WordPress 进入其安装状态，允许攻击者使用恶意数据库重新配置站点，并最终通过插件或主题部署任意 PHP 代码。这可能导致完全的远程代码执行和整个站点被接管。

Wordfence 证实，其防火墙通过检测并阻止提交的表单数据中的路径遍历尝试，从而针对该漏洞利用提供保护。

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