---
title: CTF之Misc-zip压缩包分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458483850&idx=1&sn=b2a624f6753f81072ce9b78419dbc865&chksm=b18e4c0086f9c516e126950fb9fb5d2bcdbd31b147374c693b37dcbb1fff6e5dfaaca4396605&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-11-17
fetch_date: 2025-10-03T23:01:01.572449
---

# CTF之Misc-zip压缩包分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G4J8y2ialKZLnZHkaLKOsmUGbzo5rbcicBLo4RmZUPREoiaIGNdAM4tLhhsrdI8tbUiaTP0XiaAIJrwQg/0?wx_fmt=jpeg)

# CTF之Misc-zip压缩包分析

wx\_酸菜鱼

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G4J8y2ialKZLnZHkaLKOsmU9zlrXibJJs0c2nLlPDyp9dHYcOeonRmIHNsdvKJ7SFiaeh3xJfzyLyHg/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：wx\_酸菜鱼

本人打ctf总结的一点思路，如有错漏之处，敬请指正。

##

## **zip文件格式**

一个zip文件由三部分组成：压缩源文件数据区+压缩源文件目录区+压缩源文件目录结束标志。

###

### **1、压缩源文件数据区**

在这个数据区中每一个压缩的源文件/目录都是一条记录，记录的格式如下：
[文件头+ 文件数据 + 数据描述符]

```
文件头结构、、、、、组成    　                长度文件头标记                   4 bytes  (0x04034b50)解压文件所需 pkware 版本      2 bytes全局方式位标记                2 bytes压缩方式                     2 bytes最后修改文件时间              2 bytes最后修改文件日期              2 bytesCRC-32校验                   4 bytes压缩后尺寸                   4 bytes未压缩尺寸                   4 bytes文件名长度                   2 bytes扩展记录长度                  2 bytes文件名                      （不定长度）扩展字段                    （不定长度）文件数据、、、、、数据描述符、、、、、CRC-32校验                  4 bytes压缩后尺寸                   4 bytes未压缩尺寸                   4 bytes
```

这个数据描述符只在全局方式位标记的第３位设为１时才存在，紧接在压缩数据的最后一个字节后。这个数据描述符只用在不能对输出的 ZIP 文件进行检索时使用。例如：在一个不能检索的驱动器（如：磁带机上）上的 ZIP 文件中。如果是磁盘上的ZIP文件一般没有这个数据描述符。

50 4B 03 04：这是头文件标记（0x04034b50）
14 00：解压文件所需 pkware 版本
00 00：全局方式位标记（有无加密） 头文件标记后2bytes
08 00：压缩方式

###

### **2、压缩源文件目录区**

在这个数据区中每一条纪录对应在压缩源文件数据区中的一条数据。

```
组成               　            长度目录中文件文件头标记             4 bytes  (0x02014b50)压缩使用的　pkware 版本          2 bytes解压文件所需 pkware 版本         2 bytes全局方式位标记                   2 bytes压缩方式                        2 bytes最后修改文件时间                 2 bytes最后修改文件日期                 2 bytesＣＲＣ－３２校验                 4 bytes压缩后尺寸                      4 bytes未压缩尺寸                      4 bytes文件名长度                      2 bytes扩展字段长度                    2 bytes文件注释长度                    2 bytes磁盘开始号                      2 bytes内部文件属性                    2 bytes外部文件属性                    4 bytes局部头部偏移量                  4 bytes文件名                       （不定长度）扩展字段                     （不定长度）文件注释                     （不定长度）
```

50 4B 01 02：目录中文件文件头标记(0x02014b50)
3F 00：压缩使用的 pkware 版本
14 00：解压文件所需 pkware 版本
00 00：全局方式位标记（有无加密，伪加密的关键） 目录文件标记后4bytes
08 00：压缩方式

###

### **3、压缩源文件目录结束标志**

###

```
组成               　          长度目录结束标记                    4 bytes  (0x02014b50)当前磁盘编号                    2 bytes目录区开始磁盘编号               2 bytes本磁盘上纪录总数                 2 bytes目录区中纪录总数                 2 bytes目录区尺寸大小                   4 bytes目录区对第一张磁盘的偏移量        4 bytesZIP 文件注释长度                 2 bytesZIP 文件注释                   （不定长度）
```

###

### 50 4B 05 06：目录结束标记

00 00：当前磁盘编号
00 00：目录区开始磁盘编号

暴力破解
暴力破解就是爆破压缩包的密码。

windows下可以使用ARCHPR这款工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtTibibydia9JfPolkIcZ1f13RT4rsokCic53zR5xicm73z7ziccKB8WJViawOA/640?wx_fmt=png)

linux下可以使用frackzip命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtzGetSUs1zlibE4Dgl23pgznFptjKrEtYTnJn4hCicNveqf2EeUrH9kJw/640?wx_fmt=png)

```
fcrackzip -b -l 6-6 -c 1 -p 000000 passwd.zip-b 暴力破解-c 1 限制密码是数字-l 6-6 限制密码长度为6-p 000000 初始化破解起点
```

伪加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtClnV91FuVBBQsvZBlnu8Zjfk2gD0rKhQ7kbQm3lK3KqLONtiaZ7o1NA/640?wx_fmt=png)

这里是504B01021400000008，将1400XX0008改成单数就形成了伪加密。将这里改成0009再来看一下再改回去就破解了伪加密。

例题 强网杯2020 miscstudy level5
伪加密，处理后解压出leve5

明文攻击
大致原理，一个需要解密的ZIP而且不知道密码，但幸运的是有ZIP包里一个已知文件，将已知文件进行ZIP加密后和待解密的ZIP里已知文件进行hex对比，两者的区别就是ZIP加密的三个key。
需要查看压缩算法是否一致，CRC校验值是否相同。

CRC爆破
CRC32碰撞用于非常小的文件（6字节以上基本就别试了），就是通过CRC来反推文件内容。
而且CRC32是很容易碰撞的，所以就6字节而言，同一个CRC32可能对应着十几个字符串（纯可视字符）。

例题 强网杯2020 miscstudy level6
level6的压缩包，发现内部有三个长度为454的txt文件，想到crc爆破。

```
import stringimport binascii dic = string.ascii_letters+"_"+'0123456789'crc2=0xEED7E184crc1=0x9AEACC13crc3=0x289585AF def aa(crc):    for i in dic:        for j in dic:            for k in dic:                for p in dic:                    for q in dic:                        st = i+j+k+p+q                        if crc == (binascii.crc32(str(st)) & 0xffffffff):                            print st                            return def bb(crc):    for i in dic:        for j in dic:            for k in dic:                for p in dic:                    st = i+j+k+p                    if crc == (binascii.crc32(str(st)) & 0xffffffff):                        print st                        return aa(crc1)bb(crc2)aa(crc3)
```

例题PT Site bytectf2020
在注册页面看到三张图
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtc72RnOehibWN15j55nHibAqT9LTr87MYVJY3AGKS6f6lnFjdn3TAibk7g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbt1hTSoZC8vn10HRmfxYaOPolBdylTC90ZrGib0LXzgnmkZ8nV9uQYptw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtbYnvdyNP9zngQefibCqmwGyTLBhsXNRpVZaMv1ibKLuoYMvoPBoy5F2w/640?wx_fmt=png)

最后的一张图有用 根据这个，自己输入员工编号，申请编号是日期加后四位随机，去爆破CRC。

```
import binasciiimport stringimport zipfileimport base64import syscrc = int(0xcb0d2242)i = 0aaa="0123456789"for a in aaa:    for b in aaa:        for c in aaa:            for d in aaa:                strings = "亲爱的员工888888，您自助申请的PT邀请服务已受理完成，邀请链接在附件压缩包中，欢迎下次使用。\n\n"+"申请编号：20201025"+a + b + c+ d +"\n"+"ByteCTF Secret PT Server"                strings = strings.encode('utf-8')                print(binascii.crc32(strings))                if crc == ((binascii.crc32(strings))&0xFFFFFFFF):                    print(strings)                    sys.exit(1)                else:                    print(i)                    i = i+1
```

然后去明文攻击，其中有一点是，把数据写到.txt中，会看到数据比压缩包里的密文多三个字节,那是因为linux下的换行符位0A，windows下为0D0A，将0D删去即可。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbticicRLzPs8GricOGd1icJTbIDNUEp0ibxdd1JpauwNFBKDPvhTdfwbL0XMg/640?wx_fmt=png)
得到http://182.92.4.49:30080/signup.php?type=invite&invitenumber=8128e1f98353335c9b935fec58f0be46

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8H0ibic4gXRlRW5F5UmzsxJbtCpche0SgHSYDPmyPglsE7Z3vR9lkRVibwsJW3TzjarbxeAYcibEbQqSg/640?wx_fmt=png)

**看雪ID：wx\_酸菜鱼**

https://bbs.pediy.com/user-home-865065.htm

\*本文由看雪论坛 wx\_酸菜鱼 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EUvNq2rQycZibURG09OtYP0XCHXZ3icZXcMlqrP9xKN6J9cwRouvpXMfRrRxdE0xCpPmeqybJGOPibw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458479751&idx=1&sn=ca684920ebd23cc09080ba6eefb94165&chksm=b18e5c0d86f9d51b3b31b8a99231416b78566b3365abfbe25625aeba78a44b769576548b316f&scene=21#wechat_redirect)

看雪2022KCTF秋季赛官网：https://ctf.pediy.com/game-team\_list-18-29.htm

**#****往期推荐**

1.[CVE-2022-21882提权漏洞学习笔记](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471430&idx=1&sn=6a47d0c5c8f3f6204548e80977ecd059&chksm=b18e7c8c86f9f59a88d9b8e83c8297e0ef65034a73436998ab835531baadaa51f3d630793b95&scene=21#wechat_redirect)

2.[wibu证书 - 初探](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471429&idx=1&sn=a85188de9b9697fd1b9e708bb8bb1fdb&chksm=b18e7c8f86f9f59933d6cbf0040ed796f06e37b23f17f1ae842eb22257de02338e1a8d751f6b&scene=21#wechat_redirect)

3.[win10 1909逆向之APIC中断和实验](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458471421&idx=2&sn=e83cf7220dc1c4c06a2efc78593e30cc&chksm=b18e7b7786f9f2614ecce34e23be7f71a3d3516766aabda8f25ae41c81ef359a2c245503cf86&scene=21#wechat_redirect)

4.[EMET下EAF机制分析以及模拟实现](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468723&idx=2&sn=5a830d04185d80e1b6cfa639dc6c6c15&chksm=b18e71f986f9f8ef5b3c2fec51f69751e63a5d6bdbadf43b49728ba05606fc4ac63fda378c92&scene=21#wechat_redirect)

5.[sql注入学习分享](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468108&idx=1&sn=42c8ec155e13e3882cf4aeb60cdbb982&chksm=b18e0f8686f98690c9792298abb04dd243862ff8effd545dc668c7b1c682aaacf9797d899e97&scene=21#wechat_redirect)

6.[V8 Array.prototype.concat函数出现过的issues和他们的POC们](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458468074&idx=2&sn=06eb27c1649bd4e3a3e43a46a9500add&chksm=b18e0e...