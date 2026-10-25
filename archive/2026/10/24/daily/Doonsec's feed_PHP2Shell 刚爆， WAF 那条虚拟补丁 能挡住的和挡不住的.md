---
title: PHP2Shell 刚爆， WAF 那条虚拟补丁 能挡住的和挡不住的
url: https://mp.weixin.qq.com/s/XjwHTFcuOpiyh2fOkr0bng
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:07:38.569985
---

# PHP2Shell 刚爆， WAF 那条虚拟补丁 能挡住的和挡不住的

# PHP2Shell 刚爆， WAF 那条虚拟补丁 能挡住的和挡不住的

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导语：** 你好，我是网络安全老宋。安全攻防干货准时送达！

网络安全老宋// 漏洞快讯 · WAF 防护

// 漏洞快讯 · WAF 防护

# PHP2Shell 刚爆， WAF 那条虚拟补丁 能挡住的和挡不住的

往源码里钻一层，看清这条规则防什么不防什么

CVE-2026-109618CVSS 9.2源码级分析

目录 · Table of Contents

01往源码里看一层：longjmp 怎么把状态搞乱的

02109619 不是一个洞，是四个

03拆规则：这两组条件在防什么

04所以现在到底该做什么

05怎么查：你有没有被打过

06检测规则：四种格式，可以直接抄

07三层阻断：边缘、WAF、主机

●**一句话精华**
一条好规则会主动告诉你它防不住什么。雷池这条 PHP2Shell 规则，难得地把边界写在了明面上。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl9suO9cWh4B40l2MapsAIibLfydfPhabctTm1En8gicMKD2ZYZ7R2MvWpVDicrcItUx7Kf2U403gXic4X7j0BR5y3LY4XX4ZeFbk9w/640?wx_fmt=png&from=appmsg)

▲ WAF 规则卡在请求特征层，漏洞出在运行时内存层：中间隔着一道断层

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl8evibuSSPLs4pIxL5Mn4SOJed4N0icdpC2v9k3pCXu15oic6ZkQ48dI0hicb5AUhjN3iawTibxAIJkEjE0hUy8Re8KjDgkYy0kPGGjg/640?wx_fmt=png&from=appmsg)

▲ 左边是 WAF 能看见的请求特征，右边是漏洞真正发生的内存层，中间是断层

10 月 21 日下午，PHP 官方一次性放出两个 RCE：CVE-2026-109618 和 CVE-2026-109619，代号 php2shell，CVSS v4.0 打 9.2。48 小时后，香港网络安全事故协调中心定性为"极高度风险"，说正在被广泛利用；英国预算责任办公室、芬兰政府公共服务、荷兰一些机构官网相继临时下线。

就在这两天，长亭雷池的规则广场上更新了一条针对这两个 CVE 的自定义规则，附带一句很实在的说明：这是虚拟补丁，不是根治方案，对变种不能承诺 100%，完整修复需要升级 PHP。

这句话在这类场景里是稀缺的。大部分厂商发规则恨不得写成"已完美防护"，这条规则反而主动列出了自己防不住什么、哪些攻击路径看不到。

这篇就围着这条"自曝短板"的规则展开：往源码里钻一层看清漏洞怎么发生的，规则和阻断策略给你能直接抄的版本。

漏洞躺在 PHP 解释器核心里，所有跑 PHP 的东西都躲不掉：WordPress、Drupal、Joomla、Magento、Nextcloud、phpMyAdmin、Laravel 等。W3Tech 的数据是公开网站里约 69.3% 用 PHP，HKCERT 引用的 VirusTotal 估算则是全球联网的 PHP 主机超过 510 万台、约 380 万台至少开着一个端口。

**CVE-2026-109618 是内存耗尽之后的记忆混乱。** PHP 分配内存失败时用 longjmp 中断执行，可中断那一刻请求数据可能只初始化了一半，后续清理流程会把半成品当有效数据处理。

**CVE-2026-109619 是 worker 里残留的过期全局状态。** 某些错误处理、会话管理操作让全局状态指向已释放的内存，下一个请求若在状态被重置前用到它，就是一次 use-after-free。

修复版本是 8.5.12、8.4.27、8.3.36、8.2.35。8.1 及更早版本官方已不更新，得找发行版或 LTS 供应商拿回移植补丁。

## 0101 往源码里看一层：longjmp 怎么把状态搞乱的

这是整件事里最值得搞明白的一段。

修复前管内存分配失败的 `zend_mm_safe_error()`（`Zend/zend_alloc.c` 371 行起）：

⏰ PHP Core · 源码机制

heap->overflow = 1;

zend\_try {

zend\_error\_noreturn(E\_ERROR, ...);

} zend\_catch {

} zend\_end\_try();

heap->overflow = 0;

zend\_bailout();      // 就是这里，控制权直接被扔出去

exit(1);

关键在 `zend_try` 和 `zend_bailout` 这对宏。翻 `Zend/zend.h` 能看到，`zend_try` 展开后是 PHP 自己包装的一套 setjmp：

⏰ PHP Core · 源码机制

#define zend\_try                      \

JMP\_BUF \*\_\_orig\_bailout = EG(bailout);  \

JMP\_BUF \_\_bailout;                    \

if (SETJMP(\_\_bailout)==0) {

`zend_catch` 展开后则是 `LONGJMP(*EG(bailout), FAILURE)`（`Zend/zend.c` 第 1188 行）。

看懂这三个宏，漏洞就通了：**`setjmp` 记住一个位置，`longjmp` 一跳回去，中间所有 C 函数的清理逻辑全被跳过。** 那些函数不是"没来得及释放内存"，是根本没执行到清理那行。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flibN5V4ibNDRaZPLWeH7fXicQlerf6q2dAJfvY7WkH6VibQ8olJzYL5VYFzTzxE8l4hO8BG6Sne1rFX178hzkUqAibcy6SXY8HPY1w0/640?wx_fmt=png&from=appmsg)

▲ 内存耗尽触发中断，中间 C 函数的清理逻辑被跳过，状态就这样残留了下来

所以链条是这样的：一个 C 函数在 `emalloc()` 过程中被判定失败，它已把自己的指针写进了某个全局位置，但指向的结构体还没建完。这时候 `zend_bailout()` 一跳，整个请求栈被瞬间抽走，等请求清理流程遍历时读到的就是半成品。

顺带一提，PHP 源码里搜 `longjmp` 是搜不到的，它藏在 `zend_catch` 宏里。

**为什么 mod\_php 最危险。** 因为在 mod\_php 下这段触发逻辑发生在任何应用代码运行之前。请求启动阶段就要解析 POST body，而 mod\_php 无论启动是否完成都会调用 `php_request_shutdown()`，于是 shutdown 去遍历一个没人建完的状态。官方明确写了：mod\_php 默认配置下已演示出完整的未认证利用链；PHP-FPM 源码分析支持同样结论，但没演示出完整链。

**触发 OOM 的三种方式都跟 multipart 有关：** 没有可用 Content-Length 的 body、单个 part 携带大量 header、空的 file input。第二条是精髓，header 字节数很小但 PHP 为它建的数据结构远大于此，"只限 body 大小"没用。

**补丁动了近 400 个文件。** 因为旧假设是"OOM 会直接跳走，所以函数中途不用担心状态一致性"，而这个假设被整个代码库隐式依赖着。修的不是一处判断，是把一个前提整个换掉：删掉 `zend_bailout()` 那一行，`memory_limit` 从"硬性中止"变"软限制"，越过它只记录待处理错误，C 函数带着完整结构走完；新增的硬限制越界直接结束进程，因为 cleanup 本身正是可能读取陈旧状态的危险路径。

**这个补丁没有消除什么。** 打过补丁的 PHP 仍会杀掉耗尽内存的 worker，只是没有那个内存破坏。拒绝服务还在，得在边缘层限流。

## 0202 109619 不是一个洞，是四个

CVE-2026-109619 在安全通告里被归成一个 CVE，但 Wiz 拆出了四条独立 bug，PHP 团队确认它们同源。

|  |  |
| --- | --- |
| 原语 | 机制与后果 |
| **远程进程内存泄露** | upload-progress 在请求启动阶段于 `PS(id)` 发布 session id，OOM 后 `PS(id)` 可能指向已释放的分配；后续 multipart 请求在 Session 重置前走到清理路径，PHP 把重新占用的堆内容 URL 编码进响应的 `PHPSESSID` Cookie。**不需要 RCE 就能读主机内存**，Wiz 演示读出密码、token、API key |
| fatal error backtrace UAF | PHP 把最近一次 fatal error 的调用栈保留在 `EG(last_fatal_error_backtrace)`，致命 OOM 摧毁请求堆却没置空。跨请求 UAF，Wiz 对 Drupal 演示未认证 RCE |
| OPcache 类型混淆 | `zend_accel_script_persist()` 推进进程本地的 `CG(map_ptr_last)` 前沿，但只有持久化完成后才发布共享前沿；中间分配失败则本地已推进、共享状态还以为槽位空着。跨 worker 类型混淆，Wiz 对 WordPress 演示未认证 RCE |

（另有一条 upload-progress 反序列化器 UAF：记账数据存在 `BG(unserialize)`，致命分配失败摧毁请求堆后这个全局没跟着失效，下一个同 worker 的请求可能把攻击者重新占用的内存当成活的记账数据，可链成 RCE。）

**一个必须单独拎出来的反直觉结论：第二条内存泄露即使应用没调用过 session 也能工作。** 所以"我不用 session，那个开关跟我无关"是错的，也正因为它跟 session 配置无关，把 `session.upload_progress` 关掉就不可能是通用解法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93flicSv6rSAlN0ynwoI2sia1gqoKSBhbfYpTVaAfbsz0msgpABJqTibzickf1W7iaVRFbrNOLek8hZxzaKsKTNGvjhLALGs7Kd1F9I40s/640?wx_fmt=png&from=appmsg)

▲ 四条独立链路，同一个根因，最终归并为两个 CVE

四个 bug 两种影响，根子是同一个：PHP 在不该 OOM 的时机 OOM，释放了请求内存，却把内部指针留下。

## 0303 拆规则：这两组条件在防什么

雷池这条规则的 JSON 不长，两组条件用 OR 连起来、组内是 AND：一组抓 session upload progress 路径（`PHP_SESSION_UPLOAD_PROGRESS` 参数 + 像 session id 的 `PHPSESSID` + `multipart/form-data`），另一组抓 multipart 请求体里的空字节注入（`Content-Disposition` 头部后 32 字节内出现 `\x00`）。完整规则见 06 节。

**动作选"黑名单"，但同时勾了"启用观察模式"。** 雷池 9.4.3 加的这功能是发现攻击后只记录不拦截。新漏洞刚出来、PoC 已在网上传开时，谁也不知道这规则会不会误伤正常业务。规则元数据里有一项要留意：**`log` 是 false**，意味着默认不落详细日志，日志采集不到位观察模式就是哑炮。

**规则自己承认的三条边界。** 原文那段"详细的漏洞和 WAF 匹配说明"讲得很清楚：

- **WAF 和漏洞根本不在同一层。** 原文一句话点透："WAF 匹配的是 HTTP 请求特征，PHP 漏洞发生在运行时内存管理，两者不在同一层。"WAF 能看见请求头、参数名、正则匹不匹配得上；看不见 PHP 进程内部的内存状态、longjmp 之后那些半初始化的数据结构、worker 里那块被释放又还被引用的内存。这就像小区门口装了监控，能拍到谁进了门，但住户家里进了贼、东西被翻了监控就帮不上忙。 - **109618 的核心特征，当前规则没覆盖。** 原文紧跟一句："当前规则没有覆盖这些核心特征。"翻译一下：规则抓的是"利用链的输入指纹"不是"漏洞的成因"。攻击者换一种方式把内存耗干，比如不送 Content-Length、或者塞一个带一百个 header 的 part，这条规则就看不见了。 - **109619 只覆盖了 session 这一条路径。** 官方列的 producer/consumer 路径还有 INI 诊断、fatal backtrace、其他 extension/object 状态，规则一条没管。

盲区清单值得单独拎出来：**WAF 看不到 PHP 进程内部状态，也看不到不经过它的内网流量、源站直连、CLI，以及所有非 HTTP 攻击面。** 还有一句核心判断："WAF 规则/虚拟补丁都是在为修复工作争取更多的时间。"

## 0404 所以现在到底该做什么

**第一优先级永远是升级 PHP。** 升到对应版本，重启服务，验证版本确实变了。官方原话："There are no complete mitigations, updating is the only safe choice"。

⏰ PHP Core · 源码机制

# 阻断级:multipart 表单字段里注入 PHPSESSID

# 这是 Chain A 和 Chain C 的共同根因:MULTIPART\_EVENT\_FORMDATA

# 会把 POST 里的值直接抄进 session id,不做 use\_only\_cookies 检查。

# 正常客户端不会把 session id 放在表单字段里,它走 Cookie 头。

alert http any any -> any any (msg:"php2shell - session ID in multipart form field (tier 2)"; flow:established,to\_server; http.content\_type; content:"multipart/form-data"; startswith; nocase; http.request\_body; pcre:"/(?i)(?:^|\r\n)Content-Disposition\s\*:[^\r\n]{0,500}?\bname[ \t]\*=[ \t]\*[\x22\x27]?[ \t]\*PHPSESSID[ \t]\*[\x22\x27]?[ \t]\*[\x3b\r\n]/"; classtype:web-application-attack; sid:1001201; rev:2; metadata:created\_at 2026\_10\_21, tag php2shell;)

# 阻断级:multipart 文件名里带 PHP 开标签

# Chain A 的载荷载体:FILE\_START 会把文件名原样存进 session 文件,不做净化。

# 只匹配 <?php 和 <?=,裸 <? 和 <?xml 不匹配,避免 XML 类文件名误报。

alert http any any -> any any (msg:"php2shell - PHP open tag in multipart filename (tier 2)"; flow:established,to\_server; http.content\_type; content:"multipart/form-data"; startswith; nocase; http.request\_body; pcre:"/(?i)(?:^|\r\n)Content-Disposition\s\*:[^\r\n]{0,500}?filename[ \t]\*=[ \t]\*[\x22\x27]?[^\r\n]{0,2000}?<\?(?:php\b|=)/"; classtype:web-application-attack; sid:1001202; rev:2; metadata:created\_at 2026\_10\_21, tag php2shell;)

# 阻断级:multipart 文件名里带序列化对象语法

# Chain C 的写入原语:gadget 文件名 x|O:8:"stdClass":0:{}

# O:/a:/s: 是序列化形式,R: 是反向引用,| 是 PHP handler 分隔符。

alert http any any -> any any (msg:"php2shell - serialized object syntax in multipart filename (tier 2)"; flow:established,to\_server; http.content\_type; content:"multipart/form-data"; startswith; nocase; http.request\_body; pcre:"/(?i)(?:^|\r\n)Content-Disposition\s\*:[^\r\n]{0,500}?filename[ \t]\*=[ \t]\*[\x22\x27]?[^\r\n]{0,2000}?(?:[oO]\s\*:\s\*\d{1,10}\s\*:\s\*[\x22\x27]|[aA]\s\*:\s\*\d{1,10}\s\*:\s\*\{|[sS]\s\*:\s\*\d{1,10}\s\*:\s\*[\x22\x27]|[rR]\s\*:\s\*\d{1,10}\s\*\x3b|\|\s\*[oO]\s\*:\s\*\d{1,10})/"; classtype:web-application-attack; sid:1001203; rev:2; metadata:created\_at 2026\_10\_21, tag php2shell;)

# 关联级:出现 PHP\_SESSION\_UPLOAD\_PRO...