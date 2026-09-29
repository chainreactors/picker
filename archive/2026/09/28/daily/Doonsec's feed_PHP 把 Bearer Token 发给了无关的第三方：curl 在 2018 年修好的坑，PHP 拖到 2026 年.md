---
title: PHP 把 Bearer Token 发给了无关的第三方：curl 在 2018 年修好的坑，PHP 拖到 2026 年
url: https://mp.weixin.qq.com/s/aRDyDFpvUeUJxOe8JI39BQ
source: Doonsec's feed
date: 2026-09-28
fetch_date: 2026-09-29T07:38:24.216445
---

# PHP 把 Bearer Token 发给了无关的第三方：curl 在 2018 年修好的坑，PHP 拖到 2026 年

# PHP 把 Bearer Token 发给了无关的第三方：curl 在 2018 年修好的坑，PHP 拖到 2026 年

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> PHP 的 file\_get\_contents() 在跟随重定向时会把手写的 Authorization、Cookie、Proxy-Authorization 头原封不动发到新主机，哪怕是换成别的端口、甚至从 HTTPS 掉到 HTTP 明文。curl 在 2018 年（CVE-2018-1000007）和 2022 年（CVE-2022-27776）分两步修完了同类问题，PHP 的 stream wrapper 两个都没修，直到 8.2.34 / 8.3.35 / 8.4.26 / 8.5.11（CVE-2026-91766，CVSS 5.9）。本文拆解这个洞的成因、修复方案，以及顺带挖出来的 strip\_header() 老 bug。

## 一句话说清楚

你的 PHP 代码用 file\_get\_contents() 调一个 API，请求头里带了 `Authorization: Bearer xxx`。API 返回 302，Location 指向另一台主机。PHP 会把你的 token 一起发过去。

Cookie 和 Proxy-Authorization 同理。更细思极恐的是，重定向只是换了端口，或者从 HTTPS 降到 HTTP，也算——token 就这么明文落在网络上。

受影响的版本：8.2.34、8.3.35、8.4.26、8.5.11 之前的所有 PHP。同一个 bug，curl 在 2018 年 1 月就修掉了。

## 重定向的时候，头到底去哪了

PHP 里 file\_get\_contents() 和 fopen() 接受一个 URL，http:// 或 https:// 的会走到 `ext/standard/http_fopen_wrapper.c` 里的 C wrapper。

额外的请求头来自 stream context，也就是你用 stream\_context\_create() 拼的那个 options 数组。`follow_location` 默认是开的。官方公告里的 PoC 和你写过的任何一次 API 调用长得一模一样：

<?php
$ctx = stream\_context\_create(['http' => [
    'header' => "Authorization: Bearer SECRET\r\nCookie: sid=abc",
    'follow\_location' => 1,
]]);
file\_get\_contents('https://example.com/api', false, $ctx);

example.com 要是回一个 302 Found，Location 指向别的主机，那台主机就同时收到了这两个头。修复前的 C 侧代码大概是这样（有删减）：

/\* 第一个请求跑一遍，之后每一跳重定向都再跑一遍 \*/
if (!header\_init && !redirect\_keep\_method) {
    /\* 重定向时剥掉 POST 相关的头 \*/
    strip\_header(user\_headers, t, "content-length:");
    strip\_header(user\_headers, t, "content-type:");
}
/\* <- Authorization、Cookie、Proxy-Authorization 原样通过 \*/

/\* ... 稍后，读到 Location 头之后 ... \*/
php\_url\_free(resource);                   /\* <- 当前 URL 被扔掉 \*/
if ((resource = php\_url\_parse(new\_path)) == NULL) { ... }
int new\_flags = HTTP\_WRAPPER\_REDIRECTED;  /\* <- 这里没有任何东西说明凭据属于谁 \*/
if (response\_code == 307 || response\_code == 308) {
    new\_flags |= HTTP\_WRAPPER\_KEEP\_METHOD;
}

关键在于：重定向是一次递归调用，同一个 context 传下去，于是它读到同一份 header option，为新 URL 重新拼出同一个头集合。wrapper 只删 Content-Length 和 Content-Type，别的都不动，而且还只在 POST 变 GET 的时候删。

另一个细节更致命——wrapper 先释放当前 URL，再去解析下一个。等到它构造递归调用的时候，手上已经没有任何东西能拿来跟新主机做比对了。

## 这段历史比你以为的长

wrapper 把 header option 当成"这次请求"的一部分，所以"跟随重定向"自然就变成了"换个地方发同样的请求"。这个设计从 2003 年 4 月就定下了，Sara Golemon 在那次提交里加了 header、method、content 三个 context option，随 PHP 5.0.0 首发。那个提交里的重定向代码，已经在递归传同一个 context。两个特性从一开始就绑在一起。

2011 年，Dmitry Stogov 给 HTTPS over proxy 加了 basic auth 支持，而它读的正是同一个 header option 里的 Proxy-Authorization。到这一步，这个 option 携带凭据已经是"按设计"的事了。

真正让人有点无语的是，确实有两个人想过"头能不能活过重定向"。2005 年 Ilia Alshanetsky 让被重定向的 POST 转成 GET，理由是"follow browsers and cURL"，顺路剥掉 Content-Length 和 Content-Type。2013 年 Michael Wallner 把这段剥离逻辑搬进 strip\_header()（bug #61548）。

两人回答的都是同一个问题：POST 变成 GET 之后，某个头还有没有意义。没有一个人问：这个请求是不是还发给同一台服务器。

Michael 当年加的回归测试 bug61548.phpt，从那天起就在断言一个小缺陷——重定向后的 GET，期望输出里有两个空行而不是一个。原因是 strip\_header() 删掉了最后一个头，却留下了它前面的换行，然后 wrapper 又追加了自己的换行。在一个带 `Connection: close` 的 GET 上这无害，于是测试把它记了下来。我修这个洞的时候又撞上了它。

## curl 花四年、两个 CVE 才走完这段路

curl 犯过完全一样的错，代价是两次安全公告。

Craig de Stigter 报 CVE-2018-1000007 之后，Daniel Stenberg 在 curl 7.58.0 里改成：自定义的 Authorization 头只保留在原始 URL 的主机上，除非应用主动打开 CURLOPT\_UNRESTRICTED\_AUTH。2018 年 1 月 24 日发布。

但这个检查只比主机名。同一台主机换个端口、或者换个协议，Authorization 和 Cookie 照样发出去。Harry Sintonen 把这个缺口报成 CVE-2022-27776，curl 7.83.0 在 2022 年 4 月堵上。

PHP 的 wrapper 这两个 bug 全有——2018 那个和 2022 那个——一直到这次发布才一起清掉。也就是说，PHP 落后了 8 年。

## Jakub 和我改了什么

改动本身不复杂，思路就一句：先解析新 URL，再释放旧的，这样在决定发什么之前，两边都还在手上。然后比较 scheme、host、port（端口缺省时补上 443 或 80），把一个 sticky flag 带进递归调用。

-           php\_url\_free(resource);
-           if ((resource = php\_url\_parse(new\_path)) == NULL) { ...
+           php\_url \*new\_resource = php\_url\_parse(new\_path);
+           if (new\_resource == NULL) { ...
+           int default\_port = use\_ssl ? 443 : 80;
+           bool same\_origin = zend\_string\_equals\_ci(resource->scheme, new\_resource->scheme)
+               && zend\_string\_equals\_ci(resource->host, new\_resource->host)
+               && (resource->port ? resource->port : default\_port)
+                   == (new\_resource->port ? new\_resource->port : default\_port);
+
+           php\_url\_free(resource);
+           resource = new\_resource;

-           int new\_flags = HTTP\_WRAPPER\_REDIRECTED;
+           int new\_flags = HTTP\_WRAPPER\_REDIRECTED | (flags & HTTP\_WRAPPER\_STRIP\_AUTH);
+           if (!same\_origin) {
+               new\_flags |= HTTP\_WRAPPER\_STRIP\_AUTH;
+           }

flag 一旦置上，就会一直保留到后续每一跳。也就是说，重定向绕回原始主机，token 也不会回来——这一点跟关掉 CURLOPT\_UNRESTRICTED\_AUTH 的 libcurl 行为一致。这个选择我认为是对的，凭据泄漏的代价远大于便利性。

验证方式：把同一个脚本指向本地服务器，它先重定向到另一台不同端口的服务器，那台再重定向一次到自己。PHP 8.5.10 在第二台服务器收到的 2 次请求里，2 次都带上了 Bearer SECRET；打补丁后的 PHP-8.5 分支，2 次全都是 0。

需要清楚的是，这个修复只剥三个头名字，多一个都不剥。回归测试里专门断言自定义的 X-Custom 头仍然会到达另一个 origin。

> 如果你的凭据放在 X-Api-Key 或任何自研头里，wrapper 不会帮你剥。把 `follow_location` 设成 0，自己检查 Location 指向哪，然后手动跟。

## 顺手挖出来的 strip\_header() 烂摊子

真正麻烦的是 strip\_header()。老版本用 strstr() 找到头名字，只删第一个匹配；而当这个匹配正好是头块的最后一行时，它直接在字符串那里截断，把前面那个换行符留在原地。这就是 bug61548.phpt 里那两个空行的来源。

这还不只是排版问题。当一个 307 或 308 的 POST 保留 body、而末尾的 Authorization 行被剥掉时，头块会提前结束——目标端收到的是一段被截断的头块，紧接着的字节被当成了 body。这种错误在真实系统里会表现得非常诡异。

我为 8.5 分支写的第一版重写了循环，能捕获重复头，但保留了截断行为。Jakub 和我为 8.2 写的版本改成逐行扫描，丢掉前面的换行，同时能处理重复头、折行续行，以及 `Authorization : ...` 这种冒号前带空格的写法。

Jakub 在 9 月 22 日把它移植回 8.5 发布分支，所以我那第一版从没进过正式发布。8.2 的修复和他的移植版本，都删掉了 bug61548.phpt 期望输出里的那两个空行——一个存在了十三年的错误断言，终于归零。

## Go、Python 各自选了不同答案

"什么算同一台服务器"这个问题，各家的答案并不统一，这很值得留意——因为你可能同时用着它们。

| 客户端 | 规则 |
| --- | --- |
| Go net/http | 转发初始请求上的所有头，唯独在重定向到既非完全匹配、也不是子域的域名时丢掉 Authorization、WWW-Authenticate、Cookie。foo.com 跳 sub.foo.com 是保留的 |
| Python requests | should\_strip\_auth() 里主机名变了就剥 Authorization，但标准端口上的 http→https 升级为了向后兼容会保留 |
| curl / PHP（新版） | 要求 scheme、host、port 三者全部一致 |

Go 的规则比 URL 的 origin 概念松（允许子域），Python 的规则比 origin 松（允许协议升级），curl 和 PHP 走的是最严格的路径。三种都对，前提是你知道自己在继承哪一套。如果你在这些客户端外面又包了一层 SDK 或网关，先去确认一下你继承的规则，以及你的密钥所在的那个头有没有被覆盖到。

## 时间线

* 2026 年 6 月 7 日：q2a3z 报告，Ilia Alshanetsky 同为报告者
* 2026 年 8 月 11 日：8.5 分支上第一版修复，提交 8f79b50，作者是我
* 2026 年 9 月 14 日：正式修复提交 5af9465，我与 Jakub Zelenka 共同完成，9 月 18 日至 22 日期间从 PHP-8.2 合并上来。链接：https://github.com/php/php-src/commit/5af9465ca890be679033d5fb0dc89b6ea071326b
* 2026 年 9 月 22 日：后续提交 795440a，Jakub Zelenka 把按行处理的 strip\_header() 移植到 8.5 及以上。链接：https://github.com/php/php-src/commit/795440a704d4c2523c43666aef43c6a0fa193fee
* 2026 年 9 月 24 日：公告发布，CVSS 3.1 评分 5.9
* 2026 年 9 月 24 日：8.2.34、8.3.35、8.4.26、8.5.11 同日发布

## 我的两点判断

先说分数。CVSS 5.9 属于"中等偏上"，容易被运维排在后面。但从实际风险看，这个洞的触发条件太普通了——一个带 Bearer 头的 API 调用，对方返个 302，凭据就出去了。而且泄漏的目标经常是攻击者可控的域名。凡是代码里有这种模式的，不应该等排期，直接升。

再说这个修复本身。curl 从"比主机名"走到"比 origin"用了四年、两个公告，PHP 一步到位把两个层次都补齐了，这点做得比 curl 当年干净。但如果只让我记一件事，我会记那个最小的动作：**在释放当前 URL 之前，先把下一个 URL 解析出来**。代码手上同时握着两边，才有可能做比较。很多安全 bug 的根子不在逻辑写错，而在于信息在需要它的那一刻已经被丢掉了。

至于自定义头——X-Api-Key 这类——没有通用修复。库没法知道哪个头装的是秘密。这事只能你自己管。

---

### 参考资料

[1] https://daubois.dev/blog/cve-2026-91766-php-http-redirect-credential-leak/

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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