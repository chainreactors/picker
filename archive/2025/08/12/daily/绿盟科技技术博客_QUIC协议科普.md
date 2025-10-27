---
title: QUIC协议科普
url: https://blog.nsfocus.net/quic%e5%8d%8f%e8%ae%ae%e7%a7%91%e6%99%ae/
source: 绿盟科技技术博客
date: 2025-08-12
fetch_date: 2025-10-07T00:48:24.226704
---

# QUIC协议科普

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

# QUIC协议科普

### QUIC协议科普

[2025-08-11](https://blog.nsfocus.net/quic%E5%8D%8F%E8%AE%AE%E7%A7%91%E6%99%AE/ "QUIC协议科普")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 433

标题: QUIC协议科普

创建: 2025-08-01 13:16

————————————————————————–

目录:

☆ QUIC协议基本概念
☆ 测试QUIC协议
1) quic.nginx.org
2) Chrome使用QUIC的大致流程
3) 若干支持QUIC的测试站点
☆ 检查DNS HTTPS RR
1) dig
2) nslookup
3) dns.google
☆ 检查目标服务器是否支持QUIC
1) http3check.net
2) domsignal.com
☆ 浏览器对QUIC的支持
1) Firefox
2) Chrome
2.1) Chrome的ZeroOmega扩展不能代理QUIC流量
3) Edge
☆ 从沿线设备看QUIC

————————————————————————–

☆ QUIC协议基本概念

QUIC是”Quick UDP Internet Connections”的缩写。QUIC协议最初由Google开发，后
由IETF于2021年5月标准化为RFC 9000。参看:

————————————————————————–
QUIC A UDP-Based Multiplexed and Secure Transport
https://www.rfc-editor.org/rfc/rfc9000
https://datatracker.ietf.org/doc/html/rfc9000

Using TLS to Secure QUIC
https://www.rfc-editor.org/rfc/rfc9001
————————————————————————–

QUIC地位类似于TLS，但QUIC的下层协议是UDP，相比之下TLS的下层协议是TCP。QUIC
主要用于支持HTTP/3。

QUIC在高延迟或丢包的网络中表现更好，但某些网络设备会阻止UDP流量，导致QUIC
不可用。若使用代理，因大多数代理不支持UDP，QUIC将不可用。

☆ 测试QUIC协议

1) quic.nginx.org

用浏览器访问如下URL，并点击Run

https://quic.nginx.org/quic.html

会图形化显示测试结果。缺省同时测试HTTP、QUIC，可以只测QUIC。

用浏览器以无痕模式访问如下URL

https://quic.nginx.org/

提前打开F12 Network面板，启用Protocol列，该列默认未启用。可同步Wireshark抓
包，过滤规则”udp port 443″。

在F12 Network中看到，浏览器先用HTTP/2发起请求，响应报文中有

alt-svc: h3=”:443″; ma=86400

h3表示HTTP/3，443是QUIC服务运行的端口，ma=86400表示该声明的有效期为86400秒
(1天)。浏览器收到此头部后，会尝试使用QUIC连接指定端口。

在Network中看到，前面几个请求Protocol列都是h2，后面开始出现h3。Wireshark中
已抓到443/UDP报文。

2) Chrome使用QUIC的大致流程

现在Chrome支持并默认启用QUIC。

当Chrome访问目标网站时，检查DNS HTTPS RR或响应报文Alt-Svc头部判断服务器是
否支持QUIC。若服务器未明确声明支持QUIC，Chrome将使用TLS。若服务器声明支持
QUIC，Chrome后续会尝试QUIC，同时尝试TLS。若QUIC连接更快且稳定，Chrome优先
使用QUIC(HTTP/3)。若TLS连接更快或QUIC连接失败，Chrome回退到HTTP/2或1.1。

Chrome会基于Alt-Svc头部的有效期缓存服务器的QUIC支持信息。若之前成功使用
QUIC连接到目标服务器，Chrome在后续请求中优先尝试QUIC。若QUIC连接多次失败，
Chrome暂时判定目标服务器不支持QUIC。

3) 若干支持QUIC的测试站点

www.google.com
quic.nginx.org
cloudflare-quic.com
http3.is

☆ 检查DNS HTTPS RR

以www.google.com为目标FQDN

1) dig

$ dig @8.8.8.8 www.google.com HTTPS +short
1 . alpn=”h2,h3″

$ dig @1.1.1.1 www.google.com HTTPS +noall +answer
www.google.com. 9240 IN HTTPS 1 . alpn=”h2,h3″

alpn=”h2,h3″表示服务器支持TLS(HTTP/2)和QUIC(HTTP/3)。若后面有”port=443″，
表示TLS在443/TCP、QUIC在443/UDP，这是默认值。

2) nslookup

$ nslookup -type=HTTPS www.google.com 8.8.8.8 | grep alpn
www.google.com rdata\_65 = 1 . alpn=”h2,h3″

rdata\_65表示DNS HTTPS RR，其DNS RR Type是65。

3) dns.google

https://dns.google/
https://dns.google/query?name=www.google.com&rr\_type=HTTPS
https://dns.google/resolve?name=www.google.com&type=HTTPS

能看到”alpn=h2,h3″

☆ 检查目标服务器是否支持QUIC

可在F12 Network中查看Protocol列，可查询DNS HTTPS RR，可用Wireshark抓443/
UDP的包，还可用一些在线网站检查目标服务器是否支持QUIC。

1) http3check.net

https://http3check.net/
https://http3check.net/?host=www.google.com

若目标服务器支持QUIC，会看到绿色字体显示:

QUIC is supported
HTTP/3 is supported

HTTP Header中有:

alt-svc: h3=”:443″; ma=2592000,h3-29=”:443″; ma=2592000

2) domsignal.com

https://domsignal.com/http3-test

输入目标FQDN，点击”Check HTTP/3″。若目标服务器支持QUIC，会看到

HTTP/3 is enabled. It supports the following protocol version.

domsignal.com判定quic.nginx.org不支持QUIC，而http3check.net能正确判定
quic.nginx.org。鉴于此，应优先使用http3check.net。

☆ 浏览器对QUIC的支持

1) Firefox

about:config
network.http.http3.enabled

2) Chrome

————————————————————————–
chrome://flags/
Experimental QUIC protocol
Default
Enabled
Disabled

或

chrome://flags/#enable-quic
————————————————————————–

此处说明如下

Enable experimental QUIC protocol support. – Mac, Windows, Linux, ChromeOS, Android

默认相当于启用状态

2.1) Chrome的ZeroOmega扩展不能代理QUIC流量

Chrome的ZeroOmega扩展不能代理QUIC流量，它不支持UDP，只支持TCP，只支持HTTP、
SOCKS。

启用ZeroOmega扩展，访问quic.nginx.org，F12 Network Protocol只看到h2，再无
h3；尽管第一个响应报文中有Alt-Svc头部，Chrome后续并未尝试h3。Wireshark同步
抓取443/UDP，无QUIC通信发生。初步判断，启用ZeroOmega扩展后，Chrome不存在
QUIC流量泄露，相当于强制TLS。

3) Edge

————————————————————————–
edge://flags/
Experimental QUIC protocol
Default
Enabled
Disabled

或

edge://flags/#enable-quic
————————————————————————–

此处说明如下

Enable experimental QUIC protocol support. – Mac, Windows, Linux, Android

默认相当于启用状态

☆ 从沿线设备看QUIC

发往443/UDP的QUIC Client Initial包，大致包裹结构如下

IP
UDP
QUIC
TLS Client Hello
明文SNI (比如google.com)

沿线设备可通过解密看到明文SNI。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/%E8%8E%B7%E5%8F%96windbgx%E7%A6%BB%E7%BA%BF%E5%AE%89%E8%A3%85%E5%8C%85/)

[Next](https://blog.nsfocus.net/angr%E7%AC%A6%E5%8F%B7%E6%89%A7%E8%A1%8C%E7%BB%83%E4%B9%A0-%E5%AF%B9%E4%BB%98ollvm-control-flow-flattening-%E6%8E%A7%E5%88%B6%E6%B5%81%E5%B9%B3%E5%9D%A6%E5%8C%96/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)