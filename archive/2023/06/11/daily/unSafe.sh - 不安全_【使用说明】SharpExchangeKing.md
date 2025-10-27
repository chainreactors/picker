---
title: 【使用说明】SharpExchangeKing
url: https://buaq.net/go-168143.html
source: unSafe.sh - 不安全
date: 2023-06-11
fetch_date: 2025-10-04T11:44:45.670688
---

# 【使用说明】SharpExchangeKing

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

![](https://8aqnet.cdn.bcebos.com/796b27b99cf8d0636f761f8dc2e24a47.jpg)

【使用说明】SharpExchangeKing

*2023-6-10 16:33:21
Author: [rcoil.me(查看原文)](/jump-168143.htm)
阅读量:132
收藏*

---

* [分类](https://rcoil.me/categories)
* [标签](https://rcoil.me/tags)
* [归档](https://rcoil.me/archives)
* [关于](https://rcoil.me/about)
* 搜索

发表于

2023-06-10

|

分类于

[编程之道](https://rcoil.me/categories/%E7%BC%96%E7%A8%8B%E4%B9%8B%E9%81%93/)

|

热度

℃

摘要：针对本地 Windows Exchange Server 的 SharpExchangeKing 版本已经编写完成。

## 0x00 前言

针对本地 Windows Exchange Server 的 SharpExchangeKing 版本已经编写完成。

主界面如下所示：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/22287830/1685697500983-4ef482a8-875f-4832-b3a1-154a6bc4ee64.png#averageHue=%2350504f&clientId=ubf52d702-cd21-4&from=paste&height=414&id=u8531017f&originHeight=414&originWidth=845&originalType=binary&ratio=1&rotation=0&showTitle=false&size=30077&status=done&style=none&taskId=u934092d6-1130-4918-8a65-f18da0e327d&title=&width=845)

SharpExchangeKing 的功能依次如下所示：

1. 基本信息收集
2. 邮箱账户枚举
3. 邮箱账号密码暴力破解
4. 一些在获取邮箱账号后的操作，主要是针对邮箱文件夹的设置，比如委派
5. 检测委派
6. 根据搜索条件对邮件进行下载
7. 浏览共享

特别提醒：要想使用以上功能，在输入 Target 后，必须选择点击 GoGoGo，并且是通过获取基本信息后，才能正常使用，否则无法使用。在 Target 有更改时，也必须重新点击 GoGoGo。

PS：我也不清楚为什么 Defender 会将 SharpExchangeKing 标记为特洛伊木马。并且使用 DefenderCheck 检测是正常的。

## 0x01 Info 模块

该模块主要是获取以下信息：

1. 服务器所在内网域的域名及 Windows Server 版本，是根据之前编写的 NTLMSSP 解析工具。
2. 获取 Exchange 发行版本信息，包含了发行时间。
3. 尝试获取 Exchange 服务器内网 IP。
4. 从 SSL 证书中获取一些数据，这个数据可以辅助判断该目标是否是我们要打的。
5. 根据发行时间跟漏洞修补时间对比得出可能存在的漏洞。

效果如下所示：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/22287830/1685609848015-b73beccc-130d-493b-a6fc-c95aa4319f4f.png#averageHue=%23292420&clientId=u5135a97f-65aa-4&from=paste&height=648&id=u66ba3037&originHeight=648&originWidth=845&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63005&status=done&style=none&taskId=ue120138f-968b-4d0b-a352-dcad1f2ca61&title=&width=845)

当在本地 ExchangeReleaseVersion.data 文件中找不到版本数据时，会前往微软官网获取 Exchange 的版本数据。因此，此时确保当前网络可访问 <https://learn.microsoft.com/en-us/exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019>。

## 0x02 Mailbox 模块

模块说明：该模块主要是验证输入的邮箱用户是否存在。当前，该模块提供了 3 个可选择的方法，它们分别是：

| 方法 | 描述 | 缺点 |
| --- | --- | --- |
| **SMTP** |

* 对输入的用户名有要求，需要提供完整的邮箱名，比如 [[email protected]](https://rcoil.me/cdn-cgi/l/email-protection#ddafbeb2b4b19dafb2aaa9b8bcb0f3b1bcbf)
* 狗都不用
  |
* 如果目标邮服配置了 `Catch-all` 邮箱，则 **SMTP** 无法使用。
* 不支持多线程
  |
  | **OWADate** |
* 支持 [[email protected]](https://rcoil.me/cdn-cgi/l/email-protection#c8baaba7a1a488baa7bfbcada9a5e6a4a9aa) 用户名格式
* 仅输入用户名 rcoil，则在请求时默认是 rowteam\rcoil
* 成功验证写入 owadate\_success.txt
  |
* OWA 接口存在 MFA 时，则 **OWADate** 无法使用。
* 对网络条件要求，得多尝试几次
* 有些环境仅支持单种格式，两种格式需要反复尝试
  |
  | **EASDate** |
* 支持 [[email protected]](https://rcoil.me/cdn-cgi/l/email-protection#0270616d6b6e42706d757667636f2c6e6360) 用户名格式
* 仅输入用户名 rcoil，则在请求时默认是 rowteam\rcoil
* 成功验证写入 easdate\_success.txt
  |
* 对网络条件要求，得多尝试几次
* 有些环境仅支持单种格式，两种格式需要反复尝试
  |

以上三种方法都支持批量，将需要检测的用户写入文件即可。以下是使用 EASData 的测试结果：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/22287830/1685611490495-06acba24-79d5-4335-8499-cb21b0c04001.png#averageHue=%23474645&clientId=u1555a1fa-6053-4&from=paste&height=463&id=u54ffe8d9&originHeight=463&originWidth=847&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23667&status=done&style=none&taskId=u773a4dca-d0a5-434f-b0ab-6f8b8b3a382&title=&width=847)

## 0x03 Pwd Brute 模块

模块说明：该模块为密码爆破，目前仅支持 EWS 接口的验证，且该接口支持 NLTM 验证，成功验证写入 brute\_success.txt。

账号密码混杂组合支持 5 种模式：

| 模式 | 写入说明 |
| --- | --- |
| 单个账号单个密码 | UserName 和 PassWord 分别填写账号密码即可。 |
| 单个账号多个密码 | UserName 填写账号，PassWord 填写包含密码的本地文本路径。 |
| 多个账号单个密码 | UserName 填写包含账号的本地文本路径，PassWord 填写密码。 |
| 多个账号多个密码 | UserName 填写包含账号的本地文本路径，PassWord 填写包含密码的本地文本路径。 |
| 批量验证账号密码 | UserName 填写包含账号密码的本地文本路径，格式必须为“用户名:密码”。 |

PS：如果以上的密码是 NTLM 格式，则勾选 NTLM，不支持明文和 NTLM 同时使用。

![image.png](https://cdn.nlark.com/yuque/0/2023/png/22287830/1685695202003-11af0546-f91c-4855-9e6e-d48369028b73.png#averageHue=%2352504e&clientId=ubf52d702-cd21-4&from=paste&height=548&id=u369f5a7f&originHeight=548&originWidth=847&originalType=binary&ratio=1&rotation=0&showTitle=false&size=55905&status=done&style=none&taskId=u8c387744-6c96-493d-812f-6a6ee05c913&title=&width=847)

## 0x04 Setting 模块

模块说明：粗略的充当一个权限维持的作用。主要是对当前邮箱的收信箱做转发及委派访问权限。

界面大致如下所示：
![image.png](https://cdn.nlark.com/yuque/0/2023/png/22287830/1685695844457-103c583e-2bba-4163-a2ae-01b7e6798f2e.png#averageHue=%23989796&clientId=ubf52d702-cd21-4&from=paste&height=284&id=u6fc0a223&originHeight=284&originWidth=840&originalType=binary&ratio=1&rotation=0&showTitle=false&size=25551&status=done&style=none&taskId=u4a4d8f67-e2ca-4027-aa4c-5b1dc4858aa&title=&width=840)

使用说明：

* Auto：必须为 “username:password” 格式。该字段支持批量、
* Value1：根据 Funtion 选择。必须是 username 的邮箱名，比如当前登陆的是 rcoil，它的用户邮箱名为 [[email protected]](https://rcoil.me/cdn-cgi/l/email-protection#4537262a2c2905372a32312024286b2820)。
* Value2：根据 Funtion 选择对应值。

这个模块当前支持 8 个函数功能，它们分别是：

| 方法 | 描述 |
| --- | --- |
| GetMailLists | 从全局地址簿获取邮箱账号数据，成功则输出到 MaiLists.txt 文件 |
| GetInboxRules | 读取用户 Value1 规则信息，从返回结果中能够获得规则对应的 RuleID。 |
| AddForwardToRecipients | 创建用户 Value1 转发邮件至用户 Value2 的规则。 |
| DelForwardToRecipients | 根据 RuleID 删除用户 Value1 的指定转发规则。 |
| GetInboxPermissions | 查看用户 Value1 收件箱的访问权限。 |
| AddDelegateEditorToInboxPermissions | 添加用户 Value2 对用户 Value1 收件箱的完全访问权限。 |
| RemoveDelegateEditorToInboxPermissions | 移除用户 Value2 对用户 Value1 收件箱的访问权限。 |
| UpdateFolderDefaultToPermissions | 设置所有用户都可以访问 username 的所有邮件。 |

它们都是只能作用自身，无法为他人设置转发及委派。

## 0x05 CheckDelegate 模块

模块说明：主要是针对 UpdateFolderDefaultToPermissions 方法中的设置进行一个检测。如果成功检测出，那么就可以在 MailStore 模块中读取相应邮件文件夹的邮件。

* Query 支持单个/多个邮箱用户

![image.png](https://cdn.nlark.com/yuque/0/2023/png/22287830/1685697126620-83649996-e8cb-42a5-a531-7e2f2e16f478.png#averageHue=%237a7978&clientId=ubf52d702-cd21-4&from=paste&height=284&id=ud3f97445&originHeight=284&originWidth=822&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19934&status=done&style=none&taskId=u9bae10d1-6eed-449d-a543-99dc6618629&title=&width=822)

* Query 支持文件

  ![image.png](https://cdn.nlark.com/yuque/0/2023/png/22287830/1685696704817-b5f9da4b-a977-4737-a660-d8a774fca9c1.png#averageHue=%23a2a1a1&clientId=ubf52d702-cd21-4&from=paste&height=417&id=u246e8be9&originHeight=417&originWidth=1129&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52055&status=done&style=none&taskId=u313e911b-f79f-49f7-9be7-b874b758448&title=&width=1129)

检测出来什么文件夹可访问，那么就可以读取相对应的文件夹。如果检测出 `msgfolderroot`，那么，可访问所有邮件。

在输入正确的邮箱，有些环境可能会提示 `The SMTP address has no mailbox associated with it.`也就是 `SMTP 地址没有与其关联的邮箱`，具体原因未明。这个问题在 MailStore 同意存在。

## 0x06 MailStore 模块

模块说明：可读取当前用户的所有邮件，也可读取受委派的邮箱的邮件。

Value 输入框支持两种模式：

* 基于时间区间：格式为 `2020/05/26-2023/06/02`
* 基于关键字：格式为 `VPN,密码`，多个关键字以逗号隔开

Delegete 输入框支持两种格式：

* 直接输入单个或多个邮箱名称，多个邮箱以逗号隔开
* 支持文件列表

![image.png](https://cdn.nlark.com/yuque/0/2023/png/22287830/1685697597916-f0649c09-eca3-4db3-b23d-75863c481849.png#averageHue=%23696867&clientId=ubf52d702-cd21-4&from=paste&height=371&id=u1334fabf&originHeight=371&originWidth=838&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26072&status=done&style=none&taskId=ud002688d-1491-4b51-bf48-2edb7444cde&title=&width=838)

* 仅下载附件

![image.png](https://cdn.nlark.com/yuque/0/2023/png/22287830/1685698023967-52153ed7-2277-46d8-84a0-ba755a856ec8.png#averageHue=%235c5b5a&clientId=ubf52d702-cd21-4&from=paste&height=309&id=u0e638a5f&originHeight=309&originWidth=836&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19268&status=done&style=none&taskId=u17ec9b37-cdb3-4409-9870-78e82bf0687&title=&width=836)

* 读取委派用户的邮箱

![image.png](https://cdn.nlark.com/yuque/0/202...