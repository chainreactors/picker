---
title: 云端Wireshark
url: https://blog.nsfocus.net/%e4%ba%91%e7%ab%afwireshark/
source: 绿盟科技技术博客
date: 2026-06-05
fetch_date: 2026-06-06T05:49:41.245035
---

# 云端Wireshark

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

# 云端Wireshark

### 云端Wireshark

[2026-06-05](https://blog.nsfocus.net/%E4%BA%91%E7%AB%AFwireshark/ "云端Wireshark")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 55

https://wireshark.cloud/

此网站相当于远程解析pcap文件。传个pcap上去，它通过网页展示报文解析结果。怎么说呢，借助现代浏览器和js的NB，把Wireshark的GUI在网页里实现了。

那个界面很逼真、传神，不认真用，真以为是个本地GUI。使用场景可能是，手头只有别人抓的pcap，没有本地Wireshark，或者手头有tcpdump抓了包，但没有GUI工具查看。只是应个急，看一下报文解析，还成。报文解析界面中右键复制什么的，不要想，只会触发浏览器自身的右键菜单，而非Wireshark的右键菜单。

由于只是解析pcap，并不要求本机装有winpcap驱动，不存在云端抓了本机报文的隐私泄露问题。当然，你上传的pcap本身含有敏感数据时，另说。这与将pcap发给任一不可信第三方，风险级别是一样的。

工具栏第二个图标是”Start live remote capture”，点击后弹出对话框，给出客户端(本机)操作指南。

需在本机安装websocat，不同OS有不同的安装方式。

macOS   brew install websocat

FreeBSD pkg install websocat

Others  https://github.com/vi/websocat/releases

我是Ubuntu，去github下载

https://github.com/vi/websocat/releases/download/v4.0.0-alpha3/websocat.x86\_64-unknown-linux-musl

这是静态链接的单ELF，绿色版，”chmod +x”即可执行。

前述对话框的第二格给出客户端命令，比如

sudo tcpdump -i <interface> -U -w – \

‘not host relay.wireshark.cloud’ \

| websocat -b wss://relay.wireshark.cloud/<uuid>/send

相当于tcpdump实时抓包生成pcap并上传，不存在想象中的”远程抓包”，只有”本地抓包+远程解析”。可调整tcpdump的Capture Filter。命令中uuid与当前网页相关，刷新网页后会变，需同步调整命令中的uuid。

下面是一次实验记录。

在Windows Edge中访问

https://wireshark.cloud/

点击”Start live remote capture”，查看uuid，点击OK，启动WebSocket Server。之后工具栏第二个图标变成”Stop live remote capture”，图标左下角出现红叉，显式提示WebSocket Server已启动。

在Ubuntu中执行

sudo tcpdump -i ens33 -U -w – ‘icmp’ \

| ./websocat -b wss://relay.wireshark.cloud/6b716b71-1c31-4500-9ede-96d1f8ab8900/send

用ifconfig查看网络接口名，本例是ens33。只抓ICMP报文，方便测试。websocat带相对路径，也可

cp websocat /usr/local/bin/

在另一个bash中执行

ping www.microsoft.com

正常的话，Windows Edge中已实时看到Icmp Echo Request/Reply。

WebSocket Server不是很稳定，不行就刷新网页重新来过。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/ai%E6%94%BB%E9%98%B2%E8%A7%86%E7%95%8C%EF%BC%9A%E4%BB%8Emythos%E7%A0%B4%E5%B1%80%E7%9C%8B%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98%E7%9A%84%E5%B7%A5%E7%A8%8B%E5%8C%96%E8%B7%83%E8%BF%81/)

[Next](https://blog.nsfocus.net/%E4%BC%81%E4%B8%9A%E6%96%87%E6%A1%A3%E5%AE%89%E5%85%A8%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%EF%BC%88%E4%B8%80%EF%BC%89%EF%BC%9A%E5%91%8A%E5%88%AB%E6%B7%B7%E4%B9%B1%EF%BC%8C%E4%BB%8E%E5%88%86/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)