---
title: 记一次2022某地HVV中的逆向分析
url: https://www.freebuf.com/articles/network/354424.html
source: FreeBuf网络安全行业门户
date: 2023-01-06
fetch_date: 2025-10-04T03:10:26.031464
---

# 记一次2022某地HVV中的逆向分析

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

记一次2022某地HVV中的逆向分析

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

记一次2022某地HVV中的逆向分析

2023-01-05 19:28:27

所属地 湖南省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 前言

事情是这样的，国庆前期某地HVV，所以接到了客户通知他们收到了钓鱼邮件想要溯源。

![image-20230104172700286](https://image.3001.net/images/20230105/1672918107_63b6b45bcb9367039771a.png!small)

直接下载文件逆向分析一波。钓鱼邮件，图标什么的做的还是挺逼真的，还真的挺容易中招的，但是这里的bug也明显，丹尼斯没有客户端，百度一下能够辨别这是钓鱼的。

## 逆向分析

查壳工具`DIE`看是否加壳。

![image-20230103141604176](https://image.3001.net/images/20230105/1672918109_63b6b45d4b150bace57ec.png!small)

当然其他查壳工具也可以exeinfope等，看到的东西不一样。

![image-20230103142926987](https://image.3001.net/images/20230105/1672918110_63b6b45e645533e04b723.png!small)

可以看到是64位的应用，无壳，IDA静态分析。

![image-20230103154754832](https://image.3001.net/images/20230105/1672918111_63b6b45fb03bec3366af4.png!small)

直接进入主函数，直接F5逆向main函数c代码。

![image-20230103154954253](https://image.3001.net/images/20230105/1672918112_63b6b460ed9f55fe60a8d.png!small)

主函数中使用的函数比较少：

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
HRSRC ResourceW; // rbx
HGLOBAL Resource; // rbp
signed int v5; // eax
size_t v6; // rsi
size_t v7; // rcx
void *v8; // rdi
​
ResourceW = FindResourceW(0i64, (LPCWSTR)0x66, L"DATA");
Resource = LoadResource(0i64, ResourceW);
v5 = SizeofResource(0i64, ResourceW);
v6 = v5;
v7 = (unsigned int)(v5 + 1);
if ( v5 == -1 )
v7 = -1i64;
v8 = malloc(v7);
memset(v8, 0, (int)v6 + 1);
memcpy(v8, Resource, v6);
sub_140001070(v8);
return 0;
}
```

简单来看就是先查找资源，DATA应该为加密的`shellcode`，加载资源赋给`Resource`,计算资源空间大小，`malloc`分配空间大小，`memset`将申请的内存初始化为0，`memcpy`函数的功能是从源内存地址的起始位置开始拷贝若干个字节到目标内存地址中,跟进`sub_140001070`。

![image-20230103173426982](https://image.3001.net/images/20230105/1672918114_63b6b462119d41c2b909d.png!small)

可以看到反汇编之后在第52行创建进程，在56行分配虚拟内存，60行写入内存，61行创建线程，这里创建的线程即为恶意进程。这里使用动态调试x96dbg验证我们的分析另外，需要分析一下外联的地址以及注入的进程是什么，64位的应用使用x64dbg，依次下断点。

简单计算一下地址，IDA的起始地址为`00000001400015C4`。

![image-20230104105921636](https://image.3001.net/images/20230105/1672918115_63b6b4633605181502c8b.png!small)

`FindResourcew`地址为`00000001400015C4`。

![image-20230104110146017](https://image.3001.net/images/20230105/1672918116_63b6b4642bf8e0b4ef11d.png!small)

在x64dbg中找到起始地址`00007FF638B915C4`。

![image-20230104110245628](https://image.3001.net/images/20230105/1672918117_63b6b46525118304593cf.png!small)

根据偏移量跳转下断点。

![image-20230104110537142](https://image.3001.net/images/20230105/1672918118_63b6b46631c2ab6bf7ac1.png!small)

![image-20230103180338368](https://image.3001.net/images/20230105/1672918119_63b6b4672fac26eb20b3e.png!small)

F7按步调试。

![image-20230104113546489](https://image.3001.net/images/20230105/1672918120_63b6b4681f52cf88b1285.png!small)

在`loadResource`函数中追踪内存。

![image-20230104113636171](https://image.3001.net/images/20230105/1672918121_63b6b4697f44dacab0520.png!small)

这里加载的是`DATA`的内容，即为加密的`shellcode`,我们直接用`Resouce hacker`直接查看一下恶意进程`dennis.exe`的DATA内容。

![image-20230103175035753](https://image.3001.net/images/20230105/1672918122_63b6b46a9458b13c2ff6f.png!small)

说明我们的分析没有问题，继续向下调试。

![image-20230104132427466](https://image.3001.net/images/20230105/1672918123_63b6b46be91eed4cf8f53.png!small)

因为这个应用比较小，所以代码量也不大，f5反编译之后可以直接找到函数下断点，这里不需要计算偏移量了，计算方法跟上面差不多。

![image-20230104134458824](https://image.3001.net/images/20230105/1672918125_63b6b46d01dfbd2733934.png!small)

调试走到这里，可以发现走的是循环。

![image-20230104161509292](https://image.3001.net/images/20230105/1672918126_63b6b46e1913ecb46c044.png!small)

可以明显的看到有`xor`异或指令，这里对shellcode即DATA的内容做异或，异或的对象为`byte ptr`指向的地址，内存数据为`key`,那么key的内容为。

![image-20230104162423546](https://image.3001.net/images/20230105/1672918127_63b6b46f11d71522dfc3f.png!small)

因为是按字节异或所以这里异或的内存应该为78，整个循环异或的key应该为`12345678`，shellcode加密的时候应该用的key为12345678加密的，所以这里解密使用key去解密，跳出循环RIP一下，到断点`CreateProcessW`。

![image-20230104163015456](https://image.3001.net/images/20230105/1672918128_63b6b4703a6e74a3f2fa7.png!small)

可以清晰的看到注入的进程为`C:\\windwos\\system32\\svchost.exe`，向下调试。

![image-20230104163319151](https://image.3001.net/images/20230105/1672918129_63b6b471559bc67ec548f.png!small)

申请虚拟空间内存，然后向下为写入内存。

![image-20230104163411764](https://image.3001.net/images/20230105/1672918130_63b6b4723c0662f3fb5db.png!small)

解密完成后写入内存，所以在这里是可以看到外联的ip地址或者说是域名的，这里使用的是ip，查询之后发现是`腾讯云`的服务器。

![image-20230104163924966](https://image.3001.net/images/20230105/1672918131_63b6b473524f7729450a0.png!small)

在向下就是创建进程起服务`svchost.exe`了。

# 小结

钓鱼使用的服务器ip地址是某云，怕是可以溯源到本人身份了吧，毕竟现在国内运营商都需要实名，如果用的国内域名也都是实名的不管是否有CDN，不过这种级别的HVV也没必要。第一次逆向分析，多亏了大佬指点，步履维艰，如有错误欢迎指出。

# 钓鱼邮件 # 攻击溯源 # HVV

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

前言

逆向分析

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)