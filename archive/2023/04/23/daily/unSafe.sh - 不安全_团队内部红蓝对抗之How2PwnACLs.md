---
title: 团队内部红蓝对抗之How2PwnACLs
url: https://buaq.net/go-160017.html
source: unSafe.sh - 不安全
date: 2023-04-23
fetch_date: 2025-10-04T11:31:31.189912
---

# 团队内部红蓝对抗之How2PwnACLs

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

![](https://8aqnet.cdn.bcebos.com/8ea778843d502a7009e02a2aa5733fec.jpg)

团队内部红蓝对抗之How2PwnACLs

序言ACL在域里算比较复杂的知识，笔者原本熟悉程度也比较一般。但作为内网基础知识，还是有必要掌握的。以下是笔者学习的一些笔记并配套了对应的实战环境，目前环境作为私
*2023-4-22 20:7:0
Author: [xz.aliyun.com(查看原文)](/jump-160017.htm)
阅读量:51
收藏*

---

## 序言

ACL在域里算比较复杂的知识，笔者原本熟悉程度也比较一般。但作为内网基础知识，还是有必要掌握的。以下是笔者学习的一些笔记并配套了对应的实战环境，目前环境作为私有挑战已上线xbitsplatform靶场平台。

该挑战需要在已有一个域凭据的情况下，全程通过远程操作完成一些ACL滥用相关的利用。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422191901-7bd16550-e0ff-1.png)

## ACL概念

访问控制列表 (ACL) 是访问控制条目 (ACE) 的列表。ACL 中的每个 ACE 都标识一个受托者，并为该受托者指定允许、拒绝或审计的访问权限。安全对象的安全描述符可以包含两种类型的 ACL：DACL 和 SACL。

使用ADSI edit连接域后，可以看到某个域Object的acl，如下图。列表中的每一条即为ACE。代表以用户bob为主体，描述哪些对象对bob有什么样的权限。

![](http://152.136.31.37/uploads/upload_3275751beb17fcd84fe208363ae4d3b5.png)

具体打开一条ace，看到域管组对用户bob有一系列的权限：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422191918-85ddd29a-e0ff-1.png)

## 如何查看ACL

刚才我们通过图形化界面查看了域对象的ACL，在渗透测试中往往使用命令行操作更加方便。我们将做个实验来比较几个工具的优劣:

我们手动增加了用户Apache对bob的完全访问权限:

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422191927-8b5b4a0e-e0ff-1.png)

### Active Directory Module

安装：

```
import-module ActiveDirectory
```

使用:

```
(Get-Acl -Path "AD:CN=bob,CN=Users,DC=cia,DC=gov").access
```

可以看到Apache用户对bob有GenericAll权限

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422191938-91d4ae70-e0ff-1.png)

### Powerview

```
Get-ObjectAcl -samAccountName bob -ResolveGUIDs | ? {$_.ActiveDirectoryRights -eq "GenericAll"}
```

和Active Directory Module相比多了一些字段，但少了IdentityReference，导致看起来不直观：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422191949-983a09d6-e0ff-1.png)

不知道是不是版本问题，和其他人的工具会不一样。不过可以根据SecurityIdentifier指向的sid知道是谁作用于bob。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192105-c588ff1e-e0ff-1.png)

### dsacls.exe

```
dsacls "CN=bob,CN=Users,DC=cia,DC=gov"
```

结果比较明了，直接就是FULL CONTROL。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192113-ca8a6d36-e0ff-1.png)

## 特殊ACEs

但如果我们给的权限只是列表中的一小点，那么看到的结果需要解读，比如我们看到：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192123-d03ad5e0-e0ff-1.png)

表示CIA\Exchange Trusted Subsystem对bob用户的GUID为bf967a06-0de6-11d0-a285-00aa003049e2的属性有WriteProperty权限。

我们可以通过脚本转换GUID：

```
$ObjectTypeGUID = @{}

[email protected]{
    SearchBase=(Get-ADRootDSE).SchemaNamingContext
    LDAPFilter='(SchemaIDGUID=*)'
    [email protected]("Name", "SchemaIDGUID")
}

$SchGUID=Get-ADObject @GetADObjectParameter
    Foreach ($SchemaItem in $SchGUID){
    $ObjectTypeGUID.Add([GUID]$SchemaItem.SchemaIDGUID,$SchemaItem.Name)
}

[email protected]{
    SearchBase="CN=Extended-Rights,$((Get-ADRootDSE).ConfigurationNamingContext)"
    LDAPFilter='(ObjectClass=ControlAccessRight)'
    [email protected]("Name", "RightsGUID")
}

$SchExtGUID=Get-ADObject @ADObjExtPar
    ForEach($SchExtItem in $SchExtGUID){
    $ObjectTypeGUID.Add([GUID]$SchExtItem.RightsGUID,$SchExtItem.Name)
}

$ObjectTypeGUID | Format-Table -AutoSize

$ObjectTypeGUID[[GUID]'bf967961-0de6-11d0-a285-00aa003049e2']
```

结果：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192134-d6fdf02e-e0ff-1.png)

即：

powerview也可以针对具体某一条查询：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192146-de07351a-e0ff-1.png)

dsacls.exe结果比较简单，只能查询基础ACL，如GenericAll、WriteDAcl等，但胜在能远程查询，其他工具需要在域的上下文中使用：

```
dsacls.exe "\\10.0.0.50\CN=bob,CN=Users,DC=cia,DC=gov"
```

## 如何赋权

可以使用dsacls进行普通赋权，如WriteACL、GenericAll等。特殊权限可以使用图形化的ADSI远程登录进行修改。

```
dsacls "\\10.0.1.100\CN=Brandi.Khan,CN=Users,DC=pwn,DC=local" /I:T /G "pwn\Amy.Gibson:WD"

dsacls "\\10.0.1.100\CN=Carol.Dean,CN=Users,DC=pwn,DC=local" /I:T /G "pwn\Brandi.Khan:GA"

dsacls "\\10.0.1.100\CN=IT administrators,CN=Users,DC=pwn,DC=local" /I:T /G "pwn\Jane.Ward:GA"
```

## 编程实现

很多国外文章都使用BloodHound检测acl，我们看看如何实现：
<https://github.com/BloodHoundAD/SharpHound3/blob/master/SharpHound3/Tasks/ACLTasks.cs>

首先从ldap信息里得到ntsecuritydescriptor：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192159-e60ae752-e0ff-1.png)

笔者以往导出ldap信息笔者用的最多的是dsquery，并不会导出acl相关的信息。印象中adfind可以导出sddlstring：

```
AdFind -b "OU=Employee,DC=Contoso,DC=Com" -s base nTSecurityDescriptor -sddl++ -resolvesids
```

在<https://social.technet.microsoft.com/wiki/contents/articles/6477.active-directory-how-to-view-or-delete-delegated-permissions.aspx?Sort=MostRecent&PageIndex=1这篇文章中发现了很多可以操作ACL的工具。>

后续很简单，将数据初始化成ActiveDirectorySecurity实例，取需要的字段与对应值即可：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192210-ec6e562e-e0ff-1.png)

经过过滤找出允许GenericAll、Write Dacl、Write Owner的aces，之后对特殊的aces进行过滤，主要包括：

1.对DCSYNC权限相关的权限进行检测：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192220-f241eaca-e0ff-1.png)

目前dcsync的分析比较透彻了，以下是进行dcsync需要的权限：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192232-f93b13ba-e0ff-1.png)

2.对ForceChangePassword的检测

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192245-017f9302-e100-1.png)

3.对ldps进行检查，通过laps可以获取机器本地管理员密码

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192256-07aebc8a-e100-1.png)

4.对操作spn及增加用户检查

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192306-0daeee66-e100-1.png)

这里有几个objectAceType为allguid，是00000000-0000-0000-0000-000000000000即作用于所有权限。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192316-136bfede-e100-1.png)

解释了上文提到的特殊aces和常规aces作用对象的区别。

## 二次开发

sharpHound要在域内机器运行，局限性比较大，简单做个二开，增加了远程认证：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192325-193b02ce-e100-1.png)

工具最后输出对整个域进行安全评估，以下是使用流程：

首先增加到dc的dns解析

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192337-2053d004-e100-1.png)

执行：

```
7bitsPwnACLs.exe "pwn.local\Amy.Gibson" "[email protected]"  > all.txt
```

获得简洁的结果：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192354-2a7c7ee6-e100-1.png)

标红的都属于非系统默认的ACL的账户，看起来就非常异常。查找具体的规则：

![](https://xzfile.aliyuncs.com/media/upload/picture/20230422192408-32a13058-e100-1.png)

可以看到Amy.Gibson对Brandi.Khan的00000000-0000-0000-0000-000000000000(即所有属性)有writeDACL权限。

## 脆弱性利用

### 不安全的配置导致权限提升

需要重点关注的ACE如下：

```
ForceChangePassword：强制改变当下的密码

AddMembers：可以对目标组添加用户（包括自己的账户）

GenericAll：完全控制对象，包括更改密码、注册SPN、添加AD对象到目标组里面

GenericWrite:更改目标写入参数，导致下次用户登录脚本就要执行

WriteOwne：更新目标对象的所有者，可以让自己成为所有者

WriteDACL：更新对面的DACL，将ACL写入对面实体，直接授予我们的账户对对象的完全控制权

AllExtendedRights：能够对目标对象执行与扩展 AD 权限相关的任何操作。例如，这包括强制更改用户密码的能力。
```

这些权限可以帮助我们进行一定程度的提权，但一般我们选择对目标破坏性最小的一些方案。

### 实战案例

我们现在拥有Amy.Gibson的账户密码，可以导出ACL及ldap信息：

Amy.Gibson在ldap方面仅仅是一个普通用户，没有什么可以利用的地方：

```
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Amy.Gibson
distinguishedName: CN=Amy.Gibson,CN=Users,DC=pwn,DC=local
instanceType: 4
whenCreated: 04/16/2023 05:29:00
whenChanged: 04/16/2023 06:05:55
uSNCreated: 12880
uSNChanged: 13096
name: Amy.Gibson
objectGUID: {9C994167-7B22-4979-98A1-712505B8E69B}
userAccountControl: 66048
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 0
lastLogoff: 0
lastLogon: 0
pwdLastSet: 133260965408921060
primaryGroupID: 513
objectSid: S-1-5-21-1540577040-1432127714-718651653-1111
accountExpires: 0
logonCount: 0
sAMAccountName: Amy.Gibson
sAMAccountType: 805306368
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=pwn,DC=local
dSCorePropagationData: 01/01/1601 00:00:00
lastLogonTimestamp: 133260987556163029
ADsPath: LDAP://dc.pwn.local/CN=Amy.Gibson,CN=Users,DC=pwn,DC=local
```

查看整域的acl，可以看到有几个账户都有异常的权限：

```
[+] show WriteDACLoperation

Administrators
Domain Admins
Enterprise Admins
Account Operators
Amy.Gibson
Brandi.Khan
Jane.Ward
```

### writeDACL on users(Amy.Gibson -> Brandi.Khan)

查看完整的acl信息，Amy.Gibson 对 Brandi.Khan 有wr...