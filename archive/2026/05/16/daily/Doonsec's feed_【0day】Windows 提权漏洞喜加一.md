---
title: 【0day】Windows 提权漏洞喜加一
url: https://mp.weixin.qq.com/s/7ndZ8YzLCEd08ixveIGzbw
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:44:42.099244
---

# 【0day】Windows 提权漏洞喜加一

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAju5UuLiagMibdupeRs0pCuHMHS4ua353p3GGIJ9N0q31n1woRD0FIGEmoEbz8dJx6cLw74IzSXphAHoe4MaGqTl3lWSUBpbVjE8/0?wx_fmt=jpeg)

# 【0day】Windows 提权漏洞喜加一

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAiaiclC18C9aqnetCNa7tpicZu6CbOfoicbNvvbeQppdicVsCQNIW4du6nWxCHyyWvcicIfPMb8uMQhZlQ6oMwg663znYYVM0QicKibzbA/640?wx_fmt=jpeg&from=appmsg)

## 长话短说

GitHub 账号 Nightmare-Eclipse 在 MiniPlasma 仓库中声称，Windows Cloud Files Mini Filter Driver 中与 CVE-2020-17103 相关的问题仍然存在，甚至表示原始问题可能从未被正确修复，或补丁在某个时间点被回滚；仓库 README 还称其将 PoC 改造成可弹出 SYSTEM shell 的形式，但同时承认这是竞态条件，成功率可能随环境变化。

攻击者博客进一步声称，该 PoC 已在「全补丁 Windows 11 与 Windows Server 2025」上测试，并能稳定获得 SYSTEM shell。这个说法如果属实，影响很大。

## CVE-2020-17103 是什么

CVE-2020-17103 是 Windows Cloud Files Mini Filter Driver 权限提升漏洞。NVD 当前描述为「Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability」，并说明该编号不同于 CVE-2020-17134 与 CVE-2020-17136。

从评分看，它属于本地攻击面。Tenable 收录的 CVSS v3 向量为 AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H，基础分 7.8，等级 High；NVD 记录中也能看到 Microsoft 后续加入的 CVSS v3.1 向量为 AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H。也就是说，该漏洞不适合作为互联网入口，但一旦攻击者已有低权限上下文，成功利用后的影响可以覆盖机密性、完整性与可用性。

## MiniPlasma 新在哪里

MiniPlasma 的新意不在于 CVE 编号，而在于它提出了一个更危险的指控：**这个 2020 年漏洞可能仍然存在，或者补丁效果在后续系统版本中失效。**

仓库 README 的叙述链条大致是：作者重新调查 GreenPlasma 中用到的技术时，认为 `cldflt!HsmOsBlockPlaceholderAccess` 仍受到六年前报告给微软的问题影响；作者还称该问题最初由 Google Project Zero 的 James Forshaw 发现并报告，后来被归入 CVE-2020-17103；随后作者又声称原始 PoC 无需修改即可工作，并把它改造成 SYSTEM shell 形式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cBGhzWwhSAhO1yJ2Dp3twVJGASK2fxLT4IhOFsWW0spoObicNOJzjujzTRHtzMAiaI0b8wnP3w3eWaMgTydjwcZVSb08jyYiaQiawCu0A6GvDYY/640?wx_fmt=png&from=appmsg)

攻击者博客的表述称 CVE-2020-17103 的补丁「根本不在那里」，并声称新 PoC 在全补丁 Windows 11 与 Windows Server 2025 上能够弹出 SYSTEM shell。**攻击者声称：全补丁 Windows 11 与 Server 2025 可提权。**

## 核心研判

**研判一：MiniPlasma 是「旧 CVE 被重新武器化」，不是一个已经坐实的新 0day。置信度：高。**

依据是 CVE-2020-17103 本身是 2020 年漏洞，漏洞库和补丁记录都能回溯到当时；MiniPlasma 新增的是「补丁可能不存在 / 可能回滚 / 原始 PoC 仍可工作」这一主张，而不是新 CVE 分配或微软新公告。

**研判二：对企业而言，最合理动作不是「全网应急」，而是「补丁基线核查 + Cloud Files 行为监控 + 升级触发条件」。置信度：中。**

原因很直接：即使 MiniPlasma 属实，它也是本地提权，不是远程入口。它放大的是已失陷主机的损害上限，而不是单独制造初始入侵。因此，应急动作要围绕「谁可能被低权限执行」「哪些资产使用 Cloud Files / OneDrive 按需文件」「是否存在异常 SYSTEM 进程生成」来展开。

> 参考：https://github.com/Nightmare-Eclipse/MiniPlasma

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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