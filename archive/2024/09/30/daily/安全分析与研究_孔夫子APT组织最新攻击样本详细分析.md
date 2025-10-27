---
title: 孔夫子APT组织最新攻击样本详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247488966&idx=1&sn=896c8b93ebaf490a335a756e530fa1e8&chksm=902fbaeea75833f820a27bcb79b501d3451be6f2b45d9640a69897ef241a6b652fa1524d3284&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-09-30
fetch_date: 2025-10-06T18:25:05.948356
---

# 孔夫子APT组织最新攻击样本详细分析

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGI5KlCSIDeolmyzSg1EWXBA3iamahibVfQ78dgeOHbz6jr2lGYOqDacFaw/0?wx_fmt=jpeg)

# 孔夫子APT组织最新攻击样本详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/15703

先知社区 作者：熊猫正正

Confucius是一个印度背景的APT组织，该组织在恶意代码和基础设施上与Patchwork存在重叠，但目标侧重有所不同，该组织自2013年起开始活跃同时也被国内安全厂商称为摩罗桫或者孔夫子，与许多其他南亚 APT 组织团伙一样主要对中国和巴基斯坦等国的关键基础设施部门发起网络攻击，其中包括政府机构、军工企业、核工业等。

该组织使用了多种攻击手法，包括但不限于邮件结合钓鱼网站、邮件结合木马附件、单一投放木马等，其除了使用自身的特种木马外，疑似还使用了一些商业、开源木马，其投递样本基本都使用rar或者zip进行压缩。

笔者最近跟踪到该组织最新的攻击样本，对该批样本进行了详细分析，分享出来供大家参考学习。

详细分析

1.初始样本是一个压缩包，解压缩之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGI3qRuQIAUGDqPtU5gV9ECgHBUsK8y0kVLrmAy6eYyXASJVicSEFf6JSg/640?wx_fmt=png)

2.LNK文件命令行信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGI8SGDeXw4AfylCiczfricg0gLoatBg9uFxgKAaBJVbUzX6okR5G9QXWKw/640?wx_fmt=png)

3.提取里面包含的PowerShell恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGIXnE2FC6QUZYGsy8LjVOF8yteYz28uQVibDEf3ADe8jHmAonU70ZGp4w/640?wx_fmt=png)

4.恶意脚本在指定的目录下生成恶意模块，恶意模块为NET程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGIh0Ny1hXWeU4zmdiaibVY1UE5nAibwp3jI1HSDadGzsxia5BB2E5dbRdn6w/640?wx_fmt=png)

5.恶意脚本在指定的目录下生成欺骗PDF文档并打开，PDF文档内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGIXFCPBIkAmnmrzY6icjMaDlqLNFWpgNPIBdeM8uNricld3qpdeeD8nj0g/640?wx_fmt=png)

6.通过白+黑的方式加载恶意模块，NET程序中包含很多垃圾无用代码，获取远程服务器恶意模块URL链接，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGINySspia42iblH52UWOS0fQicrDN9A7hjfQz4N7ONlDnTCfRSjPbicABwicg/640?wx_fmt=png)

7.获取第二个(备用)远程服务器恶意模块URL链接，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGINIq5NwVGeWm1PM2HBIpiaa65vvHh4ibqUuRMiaiadPED5SNMvCJ7BQGNUA/640?wx_fmt=png)

8.从远程服务器上下载恶意模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGIxCp8Mfbkoqh77aKK3EnSBlENa5mm5CkCia2UfE7k39rj2zIthfzibzBw/640?wx_fmt=png)

9.最后加载执行下载的恶意模块Bsdfwiyersdkfh函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGIyX7ajnic3ianicVZK6YibjF9WoRxvzLDQSgZqfhqw1pdKibZWHW8JWX7yNw/640?wx_fmt=png)

10.下载的恶意模块，也是NET程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGIU40tibLaofWrlb0wl2obuhDQHd9PufSRiamW03NDO4MOU4K6vS5h06uQ/640?wx_fmt=png)

11.恶意模块Bsdfwiyersdkfh函数，也包含大量的无用垃圾代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGIibQFkZYqbr371ictVZsUGD86kHxd3gBxmyibdZDxdsMm6bJ2KLpqF677Q/640?wx_fmt=png)

12.可以手动去除垃圾代码方便进行静态分析，恶意模块会获取设置硬盘的卷标号，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGI7BeComibWfP9pQPhXVbH5JUO2O16VNG3Fysy7ve5AGozxoUDCiaflw1A/640?wx_fmt=png)

13.获取主机名、用户名，然后请求远程服务器，下载已上传文件的MD5文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGIamrwayG8qmK4raVyAoXiaib8ctDD0sYfebeFFP124avBChnt6ickIrkbg/640?wx_fmt=png)

14.遍历获取磁盘指定后缀的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGIm8pLsKQB2JghfsmU38FiabxVJbe3HsTiaD7JnmENa3XiavWqh4P7eElLA/640?wx_fmt=png)

15.将指定的文件和数据上传到黑客远程服务器上，该木马为了避免重复上传文件，会在上传文件的时候，向C2服务器回传文件的MD5值，上传文件的时候，会判断当前文件的MD5值是否存在已上传文件MD5列表中，来避免文件被重复上传，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGIscDTC4of3z12cUNM3XeO1uft26u0DyXDYgiaZvUDkvN6KQ4gJN0wmbA/640?wx_fmt=png)

通过对样本进行逆向分析，该样本与孔夫子APT组织此前的攻击样本非常相似，可以确定该攻击样本为孔夫子APT组织的最新攻击样本。

16.笔者通过威胁情报平台查询黑客的域名服务器，发现这些域名已经被标记为孔夫子APT组织，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGInxQDYq4yjSNXzpVKNZdoyrnnYsNtnKh7Sza5F56ibD5RAM6wWcoHYng/640?wx_fmt=png)

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmXgKqNMmnLTG8XpTOErUZGIY2cScVnNgx6gT95liaNGKxN7AREbYb0ziaBFc7gQ4fRNZX7jKBZxLywA/640?wx_fmt=png)

总结结尾

黑客组织利用各种恶意软件进行的攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，而且非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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