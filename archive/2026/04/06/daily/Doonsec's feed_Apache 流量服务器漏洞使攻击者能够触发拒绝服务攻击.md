---
title: Apache 流量服务器漏洞使攻击者能够触发拒绝服务攻击
url: https://mp.weixin.qq.com/s/toUWdwleS-4MT-LMKnM9og
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:27:00.251684
---

# Apache 流量服务器漏洞使攻击者能够触发拒绝服务攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnuLjGT9RWHibJhSZ8IUW3QxD6bdrXNZQ3k1OicEcYOeTzdES0cSXjNTCmUGBIfF3CaUteMzSUM6Fic5vTUpoy415icbWDvbXfULicicw/0?wx_fmt=jpeg)

# Apache 流量服务器漏洞使攻击者能够触发拒绝服务攻击

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJns0JpsWf478loaFicWzsKIXAASQ8l1e3ENQbNIhpgWUFruQjDUOcSmEjLj9niaDOm6hV1yxXgsEClibJoqJ6wvvsaUS3ZrzzVdcrE/640?wx_fmt=png&from=appmsg)

The Apache Software Foundation 已发布关键安全更新，以修复 Apache Traffic Server（ATS）中的两个漏洞。

这些漏洞于 2026 年 4 月 2 日披露，可能被远程威胁行为者利用来触发拒绝服务（DoS）攻击，或实施 HTTP 请求走私攻击。

漏洞源于服务器在处理包含请求体数据的 HTTP 请求时的方式存在缺陷。

漏洞分析

安全研究人员 Masakazu Kitajo 和 Katsutoshi Ikenoya 发现了两个影响 ATS 处理 Web 流量方式的独立问题。

第一个漏洞（CVE-2025-58136）

攻击者仅需发送一个合法的 POST 请求即可使服务器崩溃。

由于无需任何特殊身份验证，该漏洞对拒绝服务攻击构成严重风险。攻击者可以轻松利用该漏洞干扰企业网络并使应用下线。

第二个漏洞（CVE-2025-65114）

这是一个 HTTP 请求走私漏洞，由对格式错误的分块（chunked）消息体处理不当引起。

请求走私是一种极具危险性的攻击技术，允许攻击者干扰不同服务器对 HTTP 请求边界的解析方式。

这可能导致攻击者绕过安全控制、污染 Web 缓存，或窃取同一服务器上其他用户的敏感数据。

Apache Traffic Server 是一款流行的高性能 Web 代理与缓存服务器，因此这些漏洞对企业环境构成了重大威胁。

管理员应立即检查其部署情况。受影响版本包括：

ATS 9.x 分支（9.0.0 至 9.2.12）

ATS 10.x 分支（10.0.0 至 10.1.1）

缓解措施与解决方案

为保障基础设施安全，网络管理员必须尽快升级 ATS：

使用 9.x 分支的用户应升级至 9.1.13 或更高版本

使用 10.x 分支的用户应升级至 10.1.2 或更高版本

如果无法立即打补丁，对于拒绝服务漏洞（CVE-2025-58136）可采取临时缓解措施：

通过设置配置参数 proxy.config.http.request\_buffer\_enabled 为 0，可防止服务器崩溃（该值在标准配置中通常为默认值）

对于请求走私漏洞（CVE-2025-65114），不存在配置层面的缓解方案。

升级软件仍然是唯一彻底的安全防护手段。

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