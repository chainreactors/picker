---
title: Windows中监控进程的DNS查询
url: https://blog.nsfocus.net/windows%e4%b8%ad%e7%9b%91%e6%8e%a7%e8%bf%9b%e7%a8%8b%e7%9a%84dns%e6%9f%a5%e8%af%a2/
source: 绿盟科技技术博客
date: 2026-05-22
fetch_date: 2026-05-23T05:39:53.929473
---

# Windows中监控进程的DNS查询

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# Windows中监控进程的DNS查询

### Windows中监控进程的DNS查询

[2026-05-22](https://blog.nsfocus.net/windows%E4%B8%AD%E7%9B%91%E6%8E%A7%E8%BF%9B%E7%A8%8B%E7%9A%84dns%E6%9F%A5%E8%AF%A2/ "Windows中监控进程的DNS查询")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 32

自从Windows有了DNS Client Service (Dnscache)，进程发起DNS查询时，就与此服
务深度藕合。进程试图进行FQDN解析时，底层API实际向Dnscache服务发起RPC请求。
先在Cache里找，无命中时再由Dnscache进行socket通信，FQDN解析结果经RPC响应返
回给原进程，同时存入Cache。下次再碰上同一FQDN，就用Cache响应，不再触发53/
UDP通信。

Win7可停用Dnscache，此时进程试图解析FQDN时由本进程发送53/UDP报文。Win10及
之后版本，无法停用Dnscache，必须走RPC这一套流程，意味着Win10无法用wf.msc阻
断指定进程的DNS查询。

且不说阻断，我们有时需要知道指定进程可能发起哪些DNS查询，有时想用hosts文件
对之劫持，比如解析到127.0.0.1。在逆向工程领域，这是常见需求。用Wireshark捕
捉53/UDP报文，只能看到待解析的FQDN，不能精确对应到发起进程。虽然可从时间上
推断，但不够精准。再就是Cache命中时，没有53/UDP通信，Wireshark抓不到DNS报
文，这种情况观察者不会知道曾经发起过哪些DNS查询。

原始需求可用Event Tracing for Windows(ETW)日志满足。

Windows自带工具logman、tracerpt、eventvwr.msc、wevtutil常用于查看ETW日志，
但操作并不便捷。也可用PowerShell查看ETW日志，可借助AI生成具体命令。自带工
具胜在普适。

https://github.com/asgarciap/etw-dns

github上有个etw-dns，可在控制台实时输出日志，同时在当前目录生成相关日志文
件，从中可看到哪个进程(PID)在解析哪个FQDN。没有GUI，但操作比eventvwr.msc简
便。

https://www.nirsoft.net/utils/dns\_lookup\_view.html

前段时间无意中发现，nirsoft出品过DNSLookupView，一款GUI的DNS ETW工具，完美
解决原始需求。除了使用便捷，它有个其他技术方案所不具备的优势，会实时将PID
转换成进程名，对于那些很快消失的进程，这点很有用，比如ping。即便如此，某些
转瞬即逝的进程名，仍留不下来，只有PID。

简单说几个DNSLookupView操作细节。

————————————————————————–
File
Start DNS Tracing (F5)
Stop DNS Tracing (F6)
Clear All (Ctrl-X)
View
Sort By
Time
Choose Columns
根据个人喜好挑选被显示的列，调整各字段的顺序
Options
Select Another Font
宋体 12
Advanced Options
域名黑、白名单，支持通配符
————————————————————————–

nirsoft另有不少Windows实用工具，下面这些值得一试。

————————————————————————–
DNSQuerySniffer
https://www.nirsoft.net/utils/dns\_query\_sniffer.html

SmartSniff
https://www.nirsoft.net/utils/index.html

DeviceIOView
https://www.nirsoft.net/utils/device\_io\_view.html

SimpleProgramDebugger
https://www.nirsoft.net/utils/simple\_program\_debugger.html

FileActivityWatch
https://www.nirsoft.net/utils/file\_activity\_watch.html

USBDriveLog
https://www.nirsoft.net/utils/usb\_drive\_log.html
————————————————————————–

DNSQuerySniffer，相当于只抓53/UDP的Wireshark，不满足原始需求。

SmartSniff地位类似Wireshark，但高度简化，不做协议解码，会显示报文的关联进
程。

FileActivityWatch地位类似Process Monitor，只聚焦文件操作。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/%E3%80%90%E6%BC%8F%E6%B4%9E%E9%80%9A%E5%91%8A%E3%80%91apache-struts%E5%A4%96%E9%83%A8%E5%AE%9E%E4%BD%93xxe%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9Es2-069%EF%BC%88cve-2025-68493%EF%BC%89/)

[Next](https://blog.nsfocus.net/%E6%8A%A4%E8%88%AA%E6%95%99%E8%82%B2%E6%95%B0%E5%AD%97%E5%8C%96%E6%88%98%E7%95%A5-%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E4%BA%AE%E7%9B%B82026%E5%B9%B4%E6%95%99%E8%82%B2%E7%BD%91%E7%BB%9C%E5%AE%89/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)