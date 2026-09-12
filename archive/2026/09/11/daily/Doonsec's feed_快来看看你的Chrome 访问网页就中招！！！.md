---
title: 快来看看你的Chrome 访问网页就中招！！！
url: https://mp.weixin.qq.com/s/S7pgbwc4hCGrMOmptH8AxA
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:47:18.283727
---

# 快来看看你的Chrome 访问网页就中招！！！

# 快来看看你的Chrome 访问网页就中招！！！

零日手记
零日手记

随笔漫记安全路

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

9月4日，CISA将CVE-2026-85046加入KEV目录（已知 exploited漏洞），修复截止日期9月18日。

9月5日，Google又发布了新一批Chrome更新，修复了另一个V8在野利用漏洞CVE-2026-87491。

两周内两个V8 0day在野利用。这是今年Google修复的第七和第八个Chrome活跃利用0day。

---

**CVE-2026-85046：V8类型混淆（CVSS 8.8）**

* **类型**：V8 JavaScript引擎类型混淆
* **影响**：Chrome < 152.0.7977.82
* **攻击方式**：构造恶意HTML页面，远程攻击者在沙箱内执行任意代码
* **在野利用**：Google确认已知悉在野利用（9月3日）
* **CISA KEV**：9月4日加入，FCEB机构9月18日前必须修复
* **修复版本**：152.0.7977.82

类型混淆是V8引擎的经典漏洞类型。V8的JIT编译器在优化代码时会做类型推断——假设某个对象一直是某种类型，据此生成优化后的机器码。如果攻击者构造的场景让对象的实际类型与JIT的假设不一致，优化后的代码就会按错误的类型操作对象——读写错误的内存偏移，最终实现任意代码执行。

访问一个恶意网页就够了。不需要点击下载，不需要安装任何东西，页面加载时V8执行恶意JavaScript就触发。

---

**CVE-2026-87491：V8越界写入**

* **类型**：V8越界写入
* **影响**：Chrome < 153.0.8010.36
* **攻击方式**：同样通过构造恶意HTML页面，沙箱内远程代码执行
* **在野利用**：Google确认已知悉在野利用
* **发现者**：首尔大学Compsec Lab的Jihyeon Jeong（8月6日报告，奖金$2,500）
* **修复版本**：153.0.8010.36（Windows/macOS）/ 153.0.8010.36（Linux）

这批更新一共修了230个漏洞，其中195个由Google自己报告。还包括5个WebGL和Cast组件的严重漏洞。一个WebPackaging的use-after-free（CVE-2026-87639）由OpenAI Codex Security发现——AI找漏洞。

---

**2026年Chrome在野利用0day清单**

截至9月，Google今年已修复8个在野利用的Chrome 0day：

| CVE | 类型 | 修复版本 |
| --- | --- | --- |
| CVE-2026-2441 | — | — |
| CVE-2026-3909 | — | — |
| CVE-2026-3910 | — | — |
| CVE-2026-5281 | — | — |
| CVE-2026-11645 | — | — |
| CVE-2026-85046 | V8类型混淆 | 152.0.7977.82 |
| CVE-2026-87491 | V8越界写入 | 153.0.8010.36 |

8个0day里至少2个是V8引擎漏洞。V8是Chrome最复杂的组件，也是攻击者最常打的目标——JavaScript引擎需要在性能和安全之间做大量权衡，JIT优化的类型推断天然容易引入类型混淆类漏洞。

---

**沙箱不是万能的**

两个漏洞的描述都是"execute arbitrary code inside the sandbox"——在沙箱内执行代码。Chrome沙箱限制了渲染进程的权限，即使V8被攻破，攻击者也"只是"在沙箱内执行代码，不能直接读写文件系统或执行系统命令。

但实际攻击中，攻击者通常会组合使用两个漏洞：一个V8漏洞突破沙箱内的代码执行，一个沙箱逃逸漏洞获得操作系统级权限。Chrome的安全模型依赖深度防御——V8漏洞是第一层被突破，但不应该是最后一层。

---

**修复建议**

1. **立即升级Chrome到153.0.8010.36+**

* Chrome菜单 > 帮助 > 关于Google Chrome > 重新启动

2. 所有基于Chromium的浏览器都需要升级：Microsoft Edge、Brave、Opera、Vivaldi
3. 企业环境通过组策略/MDM强制推送更新
4. 注意：部分Linux发行版的Chromium包更新可能滞后——Arch Linux的stable mirror在8月25日就冻结了，导致默认Chromium停留在151版本。检查你的实际版本
5. 如果无法立即升级，临时缓解：禁用JavaScript，或使用不基于Chromium的浏览器处理不受信任的网页

办公电脑、浏览器终端——所有使用Chrome的设备都需要排查版本号。这不是"建议更新"，是在野利用。

---

**参考链接**

* Google Chrome安全通告：chromereleases.googleblog.com
* CISA KEV：cisa.gov/known-exploited-vulnerabilities-catalog（CVE-2026-85046）
* The Hacker News：thehackernews.com/2026/09/chrome-v8-zero-day-exploited-in-wild.html
* NVD：nvd.nist.gov/vuln/detail/CVE-2026-85046

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/euBEasB1QK1mSyV63n51RYwjUnANgONCBIoG7rlnVw75VBa0K8ZtSh9RmNQBsX1ibHXx1Gw8emQgIjJAeNmdJGg/0?wx_fmt=png)

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