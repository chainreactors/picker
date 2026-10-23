---
title: PHP2Shell 紧急预警：两枚 9.2 分 RCE 藏在 PHP 内核，补丁已发布
url: https://mp.weixin.qq.com/s/NgcArHRCC2XMVfnW3kEgGQ
source: Doonsec's feed
date: 2026-10-22
fetch_date: 2026-10-23T06:44:45.106402
---

# PHP2Shell 紧急预警：两枚 9.2 分 RCE 藏在 PHP 内核，补丁已发布

# PHP2Shell 紧急预警：两枚 9.2 分 RCE 藏在 PHP 内核，补丁已发布

原创

asaotomo
asaotomo

Hx0战队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

安全 · 紧急预警

10 月 21 日，PHP 官方发布紧急安全更新，修复两枚可导致未认证远程代码执行的内核漏洞。它们被社区合称为 **PHP2Shell**，CVSS v4.0 均为 9.2。

先说结论

· 受影响的不是某个 CMS 插件，而是 PHP 解释器本身。

· 只要对外提供 PHP 请求，就可能暴露；Apache mod\_php 风险最高。

· 唯一完整修复是升级，并重启所有 PHP worker。

一、两枚漏洞，为什么能拼成一条攻击链

**CVE-2026-109618** 与内存耗尽处理有关。PHP 用 `longjmp()` 中止 OOM 请求；如果此时请求数据尚未完全初始化，清理阶段就可能把无效状态当成有效数据。官方指出，构造 multipart 请求可以在看似没有超限的情况下触发 OOM；在 mod\_php 上，攻击甚至能发生在应用代码执行之前。

**CVE-2026-109619** 则是陈旧全局状态问题。某次请求留下的内部状态，在其底层内存释放后仍被 worker 引用；同一个 worker 处理后续请求时，如果在正常初始化前访问它，就会形成 use-after-free。

Wiz 将两枚漏洞组合成一条利用链：先利用内存泄露降低地址不确定性，再触发状态损坏，最终在 WordPress、Drupal、Joomla 等环境演示了未认证 RCE。即使没有拿到代码执行权限，泄露的 worker 内存也可能包含密码、令牌、API Key 等敏感数据。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNXVfv0SibtDktZQuDefooZELEeBFeSQQeicCGEtDz46Iy0dicUNEdFgqcYM5Wh5hTPSpPoic8wibibwPAVHT3RQUYMkjnfUuYpyxo1OU/640?wx_fmt=png&from=appmsg)

二、影响范围：先查 PHP，不是先查插件

官方列出的受影响版本是：

PHP 8.2：低于 **8.2.35**

PHP 8.3：低于 **8.3.36**

PHP 8.4：低于 **8.4.27**

PHP 8.5：低于 **8.5.12**

PHP-FPM、Apache mod\_php、php-cgi、FrankenPHP、LiteSpeed 都在风险范围内。PHP 8.1 及更早分支已不再获得官方更新；PHP 项目为 7.4、8.0、8.1 提供了最小源码回补，但这不是正式维护版本。

容易被漏掉的地方包括：容器基础镜像、共享主机、控制面板、设备内置 PHP、CI/CD 构建机，以及只在内网但可被横向访问的服务。Wiz 称 PHP 5.4 以来的版本至少受其中一枚影响；这是研究方判断，不是官方支持范围，但足以说明老系统不能再拖。

三、利用态势：有探测，有尝试，别把“没大规模成功”当安全

补丁发布后，watchTowr 等监测方看到大量利用尝试和公开 PoC 扩散；但不少 PoC 不可用，或者只会把目标打崩。CISA 在公告时表示尚未观察到成功利用，两枚 CVE 当时也未进入 KEV 目录。

这不等于可以等。补丁 diff 已经公开，漏洞又位于运行时，利用门槛会随着研究投入快速下降；一旦成功，攻击者获得的是 Web worker 权限，可能直接读取配置、密钥和数据库凭据。

四、现在做什么：一小时内的处置顺序

1. 盘点真实运行时

用 `php -v`、`php-fpm -v` 和 `php -i` 确认实际承载请求的二进制与配置文件。不要只看网站后台显示的 PHP 版本，也不要只看容器标签；包管理器补丁可能以旧版本号回补，需要在 changelog 中搜索 CVE 编号。

2. 升级到修复版本

升级到 PHP 8.5.12、8.4.27、8.3.36 或 8.2.35，或安装发行版/LTS 厂商提供的修复包。升级后核对包变更记录，确认修复确实进入当前运行时。

3. 重启所有 worker

安装新包不等于旧进程已经加载新运行时。重启 PHP-FPM、Apache、LiteSpeed、FrankenPHP 和所有长期运行的 PHP worker，再复查进程实际版本。

4. 暂时无法升级时，降低暴露面

通过 php\_admin\_value、FPM pool 或 Apache 配置设置 `memory_limit=-1`，并确认没有 pool、目录或应用配置把它改回有限值。

不需要上传的应用把 `post_max_size` 降到 8M；需要上传的降到 32M，并让 `upload_max_filesize` 小于它。

设置 `session.upload_progress.enabled=0`，重启所有 worker。

PHP 8.5 额外设置 `fatal_error_backtraces=0`。

不需要 multipart 的应用，在 Web 服务器或代理层直接拦截 multipart 请求。

不要用 RLIMIT\_AS 或 RLIMIT\_DATA 代替 PHP 内存限制，这可能触发漏洞路径。

这些措施只能降低特定攻击路径的暴露，不能把系统变成安全状态。官方原话很直接：唯一完整的缓解方式就是升级。

5. 排查是否已经被打过

重点看：异常 multipart 请求后紧跟内存限制错误或连续 500；异常增大或畸形的 PHPSESSID 响应 Cookie；无法解释的 PHP worker 重启；Web 进程拉起 sh、bash、curl、wget 等子进程。发现可疑迹象时先隔离主机、保留 Web 与 PHP 日志，再轮换 PHP 进程能读到的密钥和凭据。

五、这次真正值得记住的

PHP2Shell 的警示不只是“又一个高危漏洞”。它说明运行时漏洞会直接穿透应用层安全假设：CMS 代码写得再规范，也挡不住解释器自身的内存破坏。Wiz 与 Calif 的发现过程还说明，AI 正在同时降低漏洞发现和利用适配的成本。

对运维团队，最实际的动作仍然是资产盘点、打补丁、重启和验证；对开发者，别再把 PHP 版本当成“环境细节”。

先升级，再重启，再核验。WAF 可以争取时间，但不能替代补丁。

资料来源：PHP 官方安全公告（2026-10-21）、GHSA-w8hw-w9fx-j79w、GHSA-6wmf-4rv5-p3rp、CERT-EU Security Advisory 2026-018、Wiz Research、NCSC-NL php2shell。利用态势部分参考 watchTowr 与 CISA 公开表态。
整理：2026-10-22

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNUNhzfUJs1Jf3od0ia3icPMVEmsicF7dF18gVWuYe9lUPbOaTGcZPSKM7icbKUVFKiaC1znWpicOj4icgQ2V6gzNKCPHibwgJNhBV6FHQE/0?wx_fmt=png)

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