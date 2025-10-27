---
title: 加密SOCKS5信道中防DNS泄露
url: http://blog.nsfocus.net/socks5dns/
source: 绿盟科技技术博客
date: 2023-02-28
fetch_date: 2025-10-04T08:15:11.814878
---

# 加密SOCKS5信道中防DNS泄露

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

# 加密SOCKS5信道中防DNS泄露

### 加密SOCKS5信道中防DNS泄露

[2023-02-27](https://blog.nsfocus.net/socks5dns/ "加密SOCKS5信道中防DNS泄露")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")[DNS](https://blog.nsfocus.net/tag/dns/)

阅读： 1,464

本文从纯粹的技术原理角度简介加密SOCKS5信道中防DNS泄露的问题，不涉及其它。

初代SOCKS5协议本身不包含加密机制，但现实世界中有许多加密SOCKS5实现。现代浏览器及相应Proxy插件普遍支持远程DNS解析，DNS泄露得到相当程度的阻止。但是，这样不足以彻底阻止DNS泄露。比较理想的状态是本机所有DNS解析请求都走加密SOCKS5信道，对此至少有两种现成的开源实现，Tor-DNS与DNS2SOCKS，自行放狗。

缺省情况下，Tor-DNS侦听53/UDP，收到DNS请求后做某种处理再发送到Tor SOCKS5 Proxy侦听的9050/TCP，由后者设法进行加密后的远程DNS解析，以此对付DNS泄露。

Tor-DNS用Go语言编写，第一次看Go代码，语法都不了解，全凭其他语言经验瞎猜。起初不想猜，让ChatGPT给我翻译成Python，未能如愿，后来硬着头皮看Go代码，大致看明白了。注意answer函数实现，里面有这么一段

————————————————————————–
buf[0] = 5 // VER: 5
if q.opcode == 0 // QUERY
{
var dn []byte
if q.typ == 12 // PTR
{
buf[1] = 0xF1 // CMD: RESOLVE\_PTR
dn = []byte( ptr2ip( q.name ) )
}
else // Any other record type
{
buf[1] = 0xF0 // CMD: RESOLVE
dn = []byte( q.name )
}
num := len(dn)
buf[2] = 0 // RSV
buf[3] = 3 // ATYP: DOMAINNAME
buf[4] = byte( num )
for i, v := range dn
{
buf[5+i] = v
}
buf[5+num] = 0 // DST.PORT
buf[6+num] = 0 // DST.PORT
————————————————————————–

没看过Tor的源码及文档，仅凭上述代码判断这是一种私有”Tor SOCKS5 DNS”协议，域名解析请求报文格式如下

+————+
| DST.ADDR |
+—-+——+——-+——+—–+——+———-+
|VER | CMD | RSV | ATYP | LEN | FQDN | DST.PORT |
+—-+——+——-+——+—–+——+———-+
| 5 | 0xF0 | 0 | 3 | X | ANY | 0 |
+—-+——+——-+——+—–+——+———-+

参看

《RFC 1928意译版(非直译版)》
https://scz.617.cn/network/200503311423.txt

CMD为非标0xF0，Tor SOCKS5 Proxy对此类请求报文做了扩展处理，此时DST.ADDR格式是”len+str”，其余字段如上图所示。下面是对www.youtube.com进行A记录查询时的请求报文

————————————————————————–
05 // +0x0 VER
f0 // +0x1 CMD
00 // +0x2 RSV
03 // +0x3 ATYP 3表示DST.ADDR字段对应FQDN(全称域名)
0f // +0x4 LEN
77 77 77 2e 79 6f 75 74 // +0x5 FQDN www.youtube.com
75 62 65 2e 63 6f 6d
00 00 // +0x14 DST.PORT
————————————————————————–

相应的响应报文

+—-+—–+——-+——+———-+———-+
|VER | REP | RSV | ATYP | BND.ADDR | BND.PORT |
+—-+—–+——-+——+———-+———-+
| 5 | 0 | 0 | 1 | Variable | 0 |
+—-+—–+——-+——+———-+———-+

————————————————————————–
05 // +0x0 VER
00 // +0x1 REP 0表示成功，其余非0值对应不同的失败情形
00 // +0x2 RSV
01 // +0x3 ATYP 1表示BND.ADDR字段对应IPv4地址
ac d9 0e 6e // +0x4 BND.ADDR 网络字节序 172.217.14.110
00 00 // +0x8 BND.PORT
————————————————————————–

Tor-DNS收到上述响应报文后再组织一个符合DNS协议的A记录查询响应报文，发送给DNS Client。

目前stunnel不支持UDP转发，但Tor-DNS可与stunnel配合，只有一种合理解释，stunnel也支持私有”Tor SOCKS5 DNS”协议，我找到了相应代码。

————————————————————————–
/\*
\* stunnel-5.68\src\protocol.c
\*/
NOEXPORT void socks5\_server ( CLI \*c )
{
if ( socks.req.ver != 0x05 )
{
…
}
// CONNECT
else if ( socks.req.cmd == 0x01 )
{
…
}
/\*
\* Line 488
\* RESOLVE (a TOR extension)
\*/
else if ( socks.req.cmd == 0xf0 )
{
s\_ssl\_read( c, &host\_len, sizeof host\_len );
host\_name = str\_alloc( (size\_t)host\_len+1 );
s\_ssl\_read( c, host\_name, host\_len );
host\_name[host\_len]
=’\0′;
s\_ssl\_read( c, &port\_number, 2 );
port\_name = str\_printf( “%u”, ntohs( port\_number ) );
if ( hostport2addr( &addr, host\_name, port\_name, 0 ) )
{
————————————————————————–

stunnel只检查了socks.req.cmd是否为0xf0，未检查socks.req.atyp是否为3，并且不支持socks.req.cmd为0xf1；换句话说，stunnel部分支持私有”Tor SOCKS5 DNS”协议，但对于防DNS泄露，stunnel足矣。

Go可以跨平台交叉编译，Tor-DNS可以编译成PE。

DNS2SOCKS不同于Tor-DNS，前者是一种更通用的防DNS泄露方案，不必与Tor SOCKS5 Proxy或stunnel相配合，可与任意加密SOCKS5 Proxy相配合，DNS2SOCKS要求指定一个支持TCP DNS的DNS Server。其技术原理是，侦听53/UDP，收到UDP DNS请求报文后将之转换成TCP DNS请求报文，通过SOCKS5发送TCP DNS请求；通过SOCKS5收TCP DNS响应，将之转换成UDP DNS响应返回给DNS Client。所有的SOCKS5 Proxy都支持TCP转发，但不见得支持UDP转发，后者实现起来比较复杂。DNS2SOCKS可与Tor、stunnel配合，但未使用私有”Tor SOCKS5 DNS”协议。DNS2SOCKS不利之处在于TCP DNS效率不如UDP DNS，容易超时。若与Tor、stunnel配合，建议用Tor-DNS，后者效率高得多。

Windows版可用Visual C++ 2015 Express Edition编译，作者提供了预编译的PE；同一份源码可用GCC编译Linux版。

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/sidecopyphishinganalysis/)

[Next](https://blog.nsfocus.net/node-jscve-2023-23918/)

### Meet The Author

scz

C/ASM程序员

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)