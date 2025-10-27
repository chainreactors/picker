---
title: 一种网关trustmap清理方法
url: http://blog.nsfocus.net/trustmap/
source: 绿盟科技技术博客
date: 2023-06-09
fetch_date: 2025-10-04T11:48:08.085666
---

# 一种网关trustmap清理方法

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

# 一种网关trustmap清理方法

### 一种网关trustmap清理方法

[2023-06-08](https://blog.nsfocus.net/trustmap/ "一种网关trustmap清理方法")[绿盟科技](https://blog.nsfocus.net/author/nsfocus/ "View all posts by 绿盟科技")

阅读： 660

当前防火墙等网关设备的ALG模块处理方法是，首先从ALG应用的控制通道信令报文的应用层载荷中识别出数据通道的目的IP地址和目的端口号，再将该IP地址和端口号作为键（Key），将与此控制通道相关联的ACL策略和NAT策略等信息作为值（Value），以键值对（Key-Value pair）形式保存到TrustMap（信任映射表）中，TrustMap的Value同时还会记录下当前的系统时间戳和超时时间。

TrustMap键值对Value中的系统时间戳和超时时间用于键值对的定时清理。ALG定时清理任务的每个周期处理将遍历TrustMap所有键值对，对每一个键值进行超时判断，若当前系统时间大于该键值对的超时时间戳（Value中的系统时间戳与超时时间的和），则将此键值对从TrustMap中删除，防止ALG模块对非法的IP报文进行放行和地址转换。

这种方法的优点是TrustMap键值对的查询性能非常高，在使用哈希表作为TrustMap的时候，时间复杂度为O(1)，不会降低数据通道报文传输的时延和带宽；缺点是TrustMap键值对在时间上是无序存放的，定时清理任务需要遍历TrustMap所有键值对才能将已超时的键值对清理完毕，在大量并发ALG应用的场景下，键值对的数量将达到百万级，该处理方法将持续消耗大量的系统计算资源，导致设备性能大幅下降，严重时可能出现设备计算资源耗尽和设备瘫痪。

对于上述问题，可以在ALG数据结构中增加一个AgeQueue（老化队列），并利用队列的先入先出特点和时间戳增长特点来优化ALG定时清理算法。

以FTP数据为例：

首先，网关设备对网卡接收到的FTP应用的PORT报文，首先提取出PORT报文中携带的IP地址（10.1.1.1）和端口号（11021），将此IP地址和端口号作为Key {目的IP地址=10.1.1.1, 目的端口号=11021 }，将与此FTP应用的PORT报文相关联的ACL策略编号（假设为10）和NAT策略编号（假设为20）作为Value，则Value为{ACL策略编号=10，NAT策略编号=20，应用信息=FTP数据，……}，然后将该键值对存入TrustMap，同时将目的IP地址、目的端口号、当前系统时间戳和超时时间添加到AgeQueue队尾，队列元素Item为{目的IP地址=10.1.1.1，目的端口号=11021，系统时间戳=2020年12月12日12时12分12秒，超时时间=15秒 }；

网关设备中的定时清理任务的每个周期处理中，依次对AgeQueue的队首元素进行超时判断，判断依据为当前系统时间是否大于队首元素的超时时间戳（系统时间戳与超时时间的和），若当前系统时间为2020年12月12日12时12分50秒，则队首元素Item1已超时（超时时间戳=2020年12月12日12时12分12秒+15秒=2020年12月12日12时12分27秒），则使用其目的IP地址和目的端口号组合为Key1 {目的IP地址=10.1.1.1, 目的端口号=11021 }，从TrustMap中删除Key1-Value1键值对，并从AgeQueue中删除队首元素Item1，然后继续处理新的队首元素Item2，直到队首元素不超时或者队尾元素已处理完毕，退出当前清理周期，等待下一个清理周期。

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/nacos-raft/)

[Next](https://blog.nsfocus.net/windowsscreen/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)