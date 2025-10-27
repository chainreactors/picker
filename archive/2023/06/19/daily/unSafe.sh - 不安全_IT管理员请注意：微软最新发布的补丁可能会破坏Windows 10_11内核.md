---
title: IT管理员请注意：微软最新发布的补丁可能会破坏Windows 10/11内核
url: https://buaq.net/go-169263.html
source: unSafe.sh - 不安全
date: 2023-06-19
fetch_date: 2025-10-04T11:44:44.551749
---

# IT管理员请注意：微软最新发布的补丁可能会破坏Windows 10/11内核

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

![](https://8aqnet.cdn.bcebos.com/84be9e5812bf2cf9e710b88c84c74caa.jpg)

IT管理员请注意：微软最新发布的补丁可能会破坏Windows 10/11内核

本周微软向Windows 10/11以及服务器版发布例行安全更新，此次安全更新涉及CVE-2023-32019号漏洞。根据说明此次安全更新为修复内核中的信息泄露漏洞，但不幸的是修复代码
*2023-6-18 21:37:28
Author: [www.landiannews.com(查看原文)](/jump-169263.htm)
阅读量:35
收藏*

---

[本周微软向Windows 10/11以及服务器版发布例行安全更新](https://www.landiannews.com/download/99158.html)，此次安全更新涉及**CVE-2023-32019**号漏洞。

根据说明此次安全更新为修复内核中的信息泄露漏洞，但不幸的是修复代码似乎存在问题会导致某些新问题。

有鉴于此微软已经修改策略，在默认情况下禁用内核相关的更改，企业可以在环境中验证确认没问题再启用。

![](https://img.lancdn.com/landian/public/thumb/insider-yellow.png)

**CVE-2023-32019：**

经过身份验证的用户包括攻击者可能导致内核信息泄露，此漏洞不需要管理员权限或通过其他方式权限提升。

成功利用此漏洞的攻击者可以在服务器上运行的特权进程中查看堆内存，还可以配合其他漏洞进行权限提升。

要解决此漏洞需安装2023-06月例行更新，默认情况下此解决方案已经被禁用，企业可以按需自行启用方案。

**为什么默认禁用：**

微软没有明确说明关于内核的代码修改具体会导致哪些问题，但微软强调部署该方案可能会导致某些新问题。

因此微软在默认情况下禁用相关更改，微软推荐企业在环境中对修复方案进行验证，没问题后再启用该方案。

后续这个修复方案会被默认启用，所以如果企业不提前安装进行测试的话，后面默认启用后可能会造成破坏。

**如何手动启用缓解方案：**

在测试机上安装最新安全更新，安装并在重启确认安装完成后，转到注册表编辑器的以下路径并按提示操作。

```
#注册表编辑器路径
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Policies\Microsoft\FeatureManagement\Overrides
# 新建DWORD32并命名为
4237806220 #Windows 11 22H2
4204251788 #Windows 11 21H2
4103588492 #Windows 10 20H2/21H2/22H2
4137142924 #Windows Server 2022
# 新建后将其键值修改为
1 #启用策略
0 #禁用策略
# 其他系统的对应名称
LazyRetryOnCommitFailure #Windows 10 v1809 / Server 2019
LazyRetryOnCommitFailure #Windows 10 v1607 / Server 2016
# 将其键值修改为
0
```

具体帮助文档访问微软官方网站：[How to manage the vulnerability associated with CVE-2023-32019](https://support.microsoft.com/en-us/topic/kb5028407-how-to-manage-the-vulnerability-associated-with-cve-2023-32019-bd6ed35f-48b1-41f6-bd19-d2d97270f080)

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/99174.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/99174.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)