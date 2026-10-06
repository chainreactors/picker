---
title: 已完成思考Apache HTTP Server 2.4.69 发布：修复 20 个安全漏洞
url: https://mp.weixin.qq.com/s/LaMCw5vQ8L5VjeWTRFYCyQ
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:13.936271
---

# 已完成思考Apache HTTP Server 2.4.69 发布：修复 20 个安全漏洞

# 已完成思考Apache HTTP Server 2.4.69 发布：修复 20 个安全漏洞

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnvxvtN5IsJw6sM4v0fA9w2iad7wQxYLciczibJgtQWdaAOTLy9YhbbzBgWRTeHgXtibnYomO50peNgg5yJE6B4A45YCuTkVjeibGheA/640?wx_fmt=png&from=appmsg)

Apache 软件基金会于 2026 年 10 月 1 日发布 Apache HTTP Server 2.4.69，修复了一批可能导致代码执行、服务崩溃、数据泄露以及在特定条件下绕过认证的安全缺陷。官方将该版本定为当前最佳可用版本（best available release）。

公告共列出 20 个漏洞：5 个评级为中等（moderate），15 个为低危（low）。绝大多数影响 2.4.0 至 2.4.68 版本，但实际暴露面取决于启用的模块、服务器配置以及攻击者能否触达目标。其中涉及代码执行的漏洞存在明显的前提限制，不能简单理解为“所有 Apache 安装都受影响”。

#### 两个需要重点关注的代码执行类问题

**CVE-2026-63292（mod\_vhost\_alias）**：远程客户端可通过发送超过 8192 字节的 Host 头触发崩溃，甚至可能执行代码。但该漏洞的利用需要同时满足两个条件——`VirtualDocumentRoot` 使用了主机名格式说明符，且 `LimitRequestFieldSize` 被调高至默认值以上。

**CVE-2026-42356（CGI 处理）**：在 CGI 程序触发某些内部重定向后，Apache 可能选错处理器，导致被重定向的文件被当作 CGI 执行。前提是目标文件必须已经存在于已启用 CGI 的目录中，且没有能被 mod\_mime 识别的后缀名。该问题仅影响 2.4.60 至 2.4.68。

这两个前提条件十分关键：默认部署环境下，两者均不构成无限制的代码执行。此前关于 Apache HTTP Server 代码执行的报道，主要关注的是 2.4.67 修复的那个 HTTP/2 double-free 漏洞，与本次不同。

#### 漏洞清单概览

除非另有标注，受影响版本均为 2.4.0–2.4.68；以下修复均已包含在 2.4.69 中。

| CVE | 模块/组件 | 严重等级 | 漏洞或影响 |
| --- | --- | --- | --- |
| CVE-2026-42356 | CGI 处理 | Low | 有限代码执行；仅 2.4.60–2.4.68 |
| CVE-2026-42528 | mod\_dav | Moderate | 共享锁溢出导致子进程崩溃；≤2.4.68 |
| CVE-2026-46729 | mod\_heartmonitor | Low | 单播监听器空指针崩溃 |
| CVE-2026-47360 | mod\_session\_cookie | Low | 内部重定向后会话 Cookie 泄漏至后端 |
| CVE-2026-48005 | mod\_auth\_digest | Low | 伪造头部可强制重新认证 |
| CVE-2026-56153 | mod\_charset\_lite | Low | finish\_partial\_char 堆溢出 |
| CVE-2026-56154 | mod\_rewrite | Low | lookahead 期间释放后重用 |
| CVE-2026-56449 | mod\_proxy\_html | Low | 构造响应触发越界写入 |
| CVE-2026-57941 | mod\_http2 | Moderate | 共享缓冲区释放后重用及内存写入 |
| CVE-2026-58415 | mod\_dav\_fs | Low | WebDAV 属性数据库信息泄露 |
| CVE-2026-59685 | Windows 路径处理 | Moderate | 展开短文件名时越界写入 |
| CVE-2026-59797 | mod\_ssl | Low | SSLRequire 表达式权限处理缺陷 |
| CVE-2026-63045 | mod\_proxy\_ftp | Low | 伪造 PASV 响应劫持数据连接 |
| CVE-2026-63292 | mod\_vhost\_alias | Moderate | 栈溢出；崩溃或可能代码执行 |
| CVE-2026-63686 | mod\_xml2enc | Low | 字符集转换失败导致代理处理崩溃 |
| CVE-2026-63718 | mod\_proxy\_uwsgi | Low | 响应走私；2.4.30–2.4.68 |
| CVE-2026-73636 | mod\_auth\_digest | Low | 截获的认证凭据可被重放 |
| CVE-2026-73637 | mod\_auth\_digest | Low | 并发请求破坏认证状态 |
| CVE-2026-79768 | mod\_userdir | Low | 路径等价导致信息泄露 |
| CVE-2026-93546 | mod\_dav\_fs | Moderate | 命名空间溢出；崩溃与数据库损坏；≤2.4.68 |

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

不喜欢

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