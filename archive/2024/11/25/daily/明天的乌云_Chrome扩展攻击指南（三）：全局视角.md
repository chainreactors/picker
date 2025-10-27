---
title: Chrome扩展攻击指南（三）：全局视角
url: https://blog.xlab.app/p/4db211d3/
source: 明天的乌云
date: 2024-11-25
fetch_date: 2025-10-06T19:14:49.573099
---

# Chrome扩展攻击指南（三）：全局视角

[明天的乌云](/)

透明人博客

* [首页](/)
* [分类](/categories/)
* [归档](/archives/)
* [日报专栏](https://daily.xlab.app/)
* [我的推荐](/links/)
* [友情链接](/friends/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [1. 用户量](#%E7%94%A8%E6%88%B7%E9%87%8F)
2. [2. 基础扫描](#%E5%9F%BA%E7%A1%80%E6%89%AB%E6%8F%8F)
   1. [2.1. Content scripts注入](#Content-scripts%E6%B3%A8%E5%85%A5)
      1. [2.1.1. all\_urls注入](#all-urls%E6%B3%A8%E5%85%A5)
      2. [2.1.2. iframe注入](#iframe%E6%B3%A8%E5%85%A5)
   2. [2.2. Background](#Background)
      1. [2.2.1. WAR文件](#WAR%E6%96%87%E4%BB%B6)
      2. [2.2.2. Externally connectable](#Externally-connectable)
      3. [2.2.3. 权限申请](#%E6%9D%83%E9%99%90%E7%94%B3%E8%AF%B7)
         1. [2.2.3.1. all\_urls权限](#all-urls%E6%9D%83%E9%99%90)
         2. [2.2.3.2. 敏感数据API权限](#%E6%95%8F%E6%84%9F%E6%95%B0%E6%8D%AEAPI%E6%9D%83%E9%99%90)
   3. [2.3. CSP Bypass](#CSP-Bypass)
3. [3. 漏洞扫描](#%E6%BC%8F%E6%B4%9E%E6%89%AB%E6%8F%8F)
4. [4. 结语](#%E7%BB%93%E8%AF%AD)
5. 5. 相关文章

![透明人](/images/logo.png)

透明人

Tmr Blog

[197
日志](/archives/)

[33
分类](/categories/)

[159
标签](/tags/)

0%

链接

* [透明日报](https://daily.xlab.app/ "https://daily.xlab.app")

# Chrome扩展攻击指南（三）：全局视角

发表于
2024-11-24

分类于

[安全](/categories/%E5%AE%89%E5%85%A8/)
，
[漏洞挖掘](/categories/%E5%AE%89%E5%85%A8/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98/)

阅读次数：

本文字数：
1.4k

阅读时长 ≈
1 分钟

对商店的全量扩展进行扫描分析，统计风险和漏洞情况

> 注意：本文写于2023.5，数据可能和当下不同

## 用户量

从攻击角度看，用户量大的影响面大，漏洞价值就越高，一共`12W+`扩展，仅有不到`2W`个扩展超过1000用户，非常的“二八原则“

![](/p/4db211d5/stat_num.png)

## 基础扫描

什么漏洞可能会常见？什么漏洞是高价值的？

1. 哪些网页会被注入Content scripts
2. 哪些网页有externally\_connectable权限
3. 是否有WAR
4. CSP Bypass
5. 域权限
6. 敏感Chrome API权限，如geolocation，cookies，scripting等

### Content scripts注入

#### all\_urls注入

all\_urls注入意味着所有网页都会注入，能增加攻击目标网站的攻击面

![](/p/4db211d5/stat_content_all_urls.png)

#### iframe注入

iframe注入意味着可以通过iframe进行攻击，更加隐蔽，不过也会受SameSite cookies的影响

![](/p/4db211d5/stat_content_iframe.png)

### Background

#### WAR文件

存在WAR文件意味着可探测，同时也能极大增加`Background`的攻击面

整体上有20%左右存在`WAR`，随着用户数量增加，存在`WAR`的扩展占比也在增加，在超过10W用户的扩展中，半数以上存在WAR文件

![](/p/4db211d5/stat_war.png)

#### Externally connectable

`externally_connectable`允许直接与`Background`通信，极大增加`Background`的攻击面

好在这个配置非常少见，但也存在用户量多占比高的趋势

![](/p/4db211d5/stat_ext_conn.png)

#### 权限申请

权限意味着在`Background`中能做什么事，同时也决定了在`Background`中的漏洞价值

##### all\_urls权限

all\_urls权限意味着在Background中可以无视同源策略访问任意网站，极大提高在`Background`中`CSRF`漏洞价值

同样也出现在用户量大的扩展中有更多的扩展申请这个权限

![](/p/4db211d5/stat_perm_all_urls.png)

##### 敏感数据API权限

这里将获取网页/历史/书签/cookies等数据，管理/配置等功能都视为可以获取敏感数据，也是`Background`漏洞的价值来源

![](/p/4db211d5/stat_perm_api.png)

### CSP Bypass

Manifest中可以自定义CSP

Manifest V2默认的CSP并不禁止eval和inline，基本可以认为可以绕过

而Manifest V3又过于严格，基本无法绕过

用[csp-evaluator](https://github.com/google/csp-evaluator)扫描检查，有中危视为可Bypass

在各用户分布下存在CSP Bypass的占比都在70%左右，相比Manifest V2大概占比75%差别不大

CSP Bypass的问题基本可以忽略，等价于V2可绕，V3不可绕

## 漏洞扫描

粗糙的扫描了用户量top300的扩展，人工审查后挖到大大小小20来个漏洞，有几个UXSS的高危漏洞，但大多数可能只有开关标签页的垃圾漏洞

考虑到自动化扫描会漏报，用户量大的漏洞可能也多，估计有漏洞的扩展大概占比3%左右？

## 结语

从研究者的角度来说：洞多，好挖，速来！

但从用户来说：安装一个浏览器扩展时，信任的是什么？

一般来说我们运行一个程序时，信任的是背后的厂商/开发者，又或者代码开源不作恶，甚至是靠杀软，但对于浏览器扩展来说，好像什么都没有

在研究过程中也确实发现了一些恶意扩展，包括网上也能看到很多恶意扩展报告，目前还是靠主动向Google举报，但从举报到删除至少有两个月左右的时间差，可以参考[披露一个恶意Chrome扩展程序](https://blog.xlab.app/p/1e632d6d/)

也发现了一些以及所谓“开源”扩展在商店中“货不对板”的情况，虽然深究后没有发现恶意行为，但心理不适

## 相关文章

* [Chrome扩展攻击指南（二）：漏洞分析](https://blog.xlab.app/p/4db211d2/)
* [Chrome扩展攻击指南（一）：基础知识](https://blog.xlab.app/p/4db211d1/)
* [让”低成本-高交互-定制化“的蜜罐成为可能](https://blog.xlab.app/p/4f53b9f3/)
* [蜜罐反制的现状与未来](https://blog.xlab.app/p/2b5e681a/)
* [获取真实的操作系统与浏览器的类型及版本](https://blog.xlab.app/p/18ce46b3/)

欢迎关注我的其它发布渠道

[Twitter](https://twitter.com/tmr11235)

[Telegram](https://t.me/tm_daily)

[RSS](/atom.xml)

[安全](/tags/%E5%AE%89%E5%85%A8/)
 [安全研究](/tags/%E5%AE%89%E5%85%A8%E7%A0%94%E7%A9%B6/)
 [漏洞挖掘](/tags/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98/)
 [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/)
 [Chrome扩展](/tags/Chrome%E6%89%A9%E5%B1%95/)

[Chrome扩展攻击指南（二）：漏洞分析](/p/4db211d2/ "Chrome扩展攻击指南（二）：漏洞分析")

[苦中作乐，路在脚下](/p/e53e3a7d/ "苦中作乐，路在脚下")

[地球ICP备42号](https://beian.miit.gov.cn/)

© 2016 –
2025

透明人

站点总字数：
343k

Theme NexT works best with JavaScript enabled