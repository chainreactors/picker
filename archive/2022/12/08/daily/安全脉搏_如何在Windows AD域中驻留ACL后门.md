---
title: 如何在Windows AD域中驻留ACL后门
url: https://www.secpulse.com/archives/193028.html
source: 安全脉搏
date: 2022-12-08
fetch_date: 2025-10-04T00:50:45.915847
---

# 如何在Windows AD域中驻留ACL后门

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

# 如何在Windows AD域中驻留ACL后门

[系统安全](https://www.secpulse.com/archives/category/articles/system)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-12-07

39,906

# 前言

当拿下域控权限时，为了维持权限，常常需要驻留一些后门，从而达到长期控制的目的。Windows AD域后门五花八门，除了常规的的添加隐藏用户、启动项、计划任务、抓取登录时的密码，还有一些基于`ACL`的后门。

# ACL介绍

ACL是一个访问控制列表，是整个访问控制模型（ACM）的实现的总称。常说的ACL主要分为两类，分别为特定对象安全描述符的自由访问控制列表 (DACL) 和系统访问控制列表 (SACL)。对象的 DACL 和 SACL 都是访问控制条目 (ACE) 的集合，ACE控制着对象指定允许、拒绝或审计的访问权限，其中Deny拒绝优先于Allow允许。

安全描述符包含与安全对象关联的安全信息。安全描述符由 SECURITY\_DESCRIPTOR 结构和关联的安全信息组成。安全描述符可以包含以下安全信息：：

* • 对象所有者和主组的安全标识符 (SID) 。
* • 指定允许或拒绝特定用户或组的访问权限的 DACL 。
* • 一个 SACL ，指定为对象生成审核记录的访问尝试的类型。
* • 一组控制位，用于限定安全描述符或其单个成员的含义。

# 隐藏安全描述符

当可控一个用户时，不想该用户被轻易发现，可以对其进行隐藏。首先查看该用户所用者，默认是域管组：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391253.jpeg "null")

可以在GUI上对所有者进行修改，也可以使用`powerview`进行修改：

```
Set-DomainObjectOwner -identity jumbo -OwnerIdentity jumbo
```

修改完成后：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-16703912531.jpeg "null")

a7f0c51c-abca-4b0b-b288-2218e633e8da

因为是权限维持，所以当前权限是域管，先尝试给域管添加一个对`jumbo`用户`Deny`所有权限的ACL，但是发现`powerview`的`Add-DomainObjectAcl`方法并没有设置`Deny`权限的操作，只有`Allow`：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391254.png "null")

image-20221203165731119

当然，你可以使用`New-ADObjectAccessControlEntry`来完成手动ACL的添加，他的原理如下图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-16703912541.png "null")

image-20221203165922392

上图看出还要手动做最后的ACL保存。既然`Add-DomainObjectAcl`已经完成了自动化的`CommitChanges`，直接把`Allow`默认可变的参数不就行了？首先手动在`Add-DomainObjectAcl`添加一个`AccessControlType`参数：

```
.PARAMETER AccessControlType

Specifies the type of ACE (allow or deny)
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391255.png "null")

image-20221203170302148

设置参数定义：

```
[Parameter(Mandatory = $True, ParameterSetName='AccessRuleType')]
[ValidateSet('Allow', 'Deny')]
[String[]]
$AccessControlType,
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391256.png "null")

image-20221203170313999

删除之前的默认的`Allow`：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-16703912561.png "null")

image-20221203170641601

最后把`AccessControlType`参数替换之前的`ControlType`：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391257.png "null")

image-20221203170738348

现在就可以在使用`AccessControlType`参数来给对象添加`Allow`或者`Deny`的权限了。

当尝试域管添加一个对`jumbo`用户`Deny`所有权限的ACL后：

```
Add-DomainObjectAcl -TargetIdentity jumbo -PrincipalIdentity S-1-5-21-12312321-1231312-123123-500 -AccessControlType Deny
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391257.jpeg "null")

871e59ae-a6bb-4e4a-83c9-bd01800bba33

当然，把`SID`改成`SamAccountName`也是可以的：

```
Add-DomainObjectAcl -TargetIdentity jumbo -PrincipalIdentity administrator -AccessControlType Deny
```

可以发现域管也没权限查看`jumbo`用户的属性了：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391258.jpeg "null")

WKtY1zjGss

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-16703912581.jpeg "null")

J3Qsrfsyl0

当使用`system`用户查看`jumbo`用户ACL时，可以看到对应的`Deny`的ACL：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391259.jpeg "null")

cccac477-019c-4600-8678-124461d8fb96

现在域管对`jumbo`用户已经无法操作任何东西了，先用`system`用户删除该`Deny`权限，准备使用`powerview`的`Remove-DomainObjectAcl`方法时，发现也只有的`Allow`，也就是默认只能移除对象的`Allow`权限，老方法，把删除的ACL属性设置为可变参数：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391259.png "null")

image-20221203171520243

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391263.png "null")

image-20221203171530075

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391264.png "null")

image-20221203171559987

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391265.png "null")

image-20221203171546945

进行删除：

```
Remove-DomainObjectAcl -TargetIdentity jumbo -PrincipalIdentity S-1-5-21-12312321-1231312-123123-500 -Rights ALL -AccessControlType Deny
```

当然，把`SID`改成`SamAccountName`也是可以的：

```
Remove-DomainObjectAcl -TargetIdentity jumbo -PrincipalIdentity administrator -Rights ALL -AccessControlType Deny
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391266.jpeg "null")

67ee14b5-46a7-44a7-81ea-57eaed22c0b5

那么同学们可能会想，如果真的有人进行了上面操作，真的没办法查看了吗，实际上并不是，对象的拥有者是有权限修改的，比如把`jumbo`用户的拥有者改成默认的域管组，然后对域管进行设置`Deny`的ACL，但是实际上拥有者依然有权限修改其ACL，这也是为什么在文章开始的时候，要把`jumbo`拥有者设置为`jumbo`的目的：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391266.png "null")

image-20221203172330615

上面尝试了拒绝域管对`jumbo`所有的权限，那为了隐藏，并且为了防止后续还要对`jumbo`用户的一些其他修改，实际上可以对`jumbo`用户设置`everyone`拒绝读取的权限即可：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-1670391268.jpeg "null")

8f23c0b4-e7e9-4f55-9c30-8abbc2a86f09

现在所有用户对其都没有查看权限了：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193028-16703912681.jpeg "null")

WKtY1zjGss

当然，只是设置了拒绝读取权限，实际上当域管去修改其ACL权限时，还是可以的：

![](http...