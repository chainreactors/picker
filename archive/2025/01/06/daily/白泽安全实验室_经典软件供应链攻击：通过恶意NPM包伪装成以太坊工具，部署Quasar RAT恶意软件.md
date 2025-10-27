---
title: 经典软件供应链攻击：通过恶意NPM包伪装成以太坊工具，部署Quasar RAT恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzI0MTE4ODY3Nw==&mid=2247492510&idx=1&sn=3a4bc5eed2d26a5edadc0ec882d9abba&chksm=e90dc9b4de7a40a263a3ff8938aa563bee6b3bff0fdc40752d96a210fd2f6ebad9495ed46236&scene=58&subscene=0#rd
source: 白泽安全实验室
date: 2025-01-06
fetch_date: 2025-10-06T20:20:15.242351
---

# 经典软件供应链攻击：通过恶意NPM包伪装成以太坊工具，部署Quasar RAT恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NpPydsaAMIO544JSnpfZmIP1kA3oSNWBwv5Pg9s4o0qib1dcrDa9ZxowI95xuFxpic78yMxbTiagEKV4b8GPUJkFA/0?wx_fmt=jpeg)

# 经典软件供应链攻击：通过恶意NPM包伪装成以太坊工具，部署Quasar RAT恶意软件

BaizeSec

白泽安全实验室

### **一、事件背景**

随着区块链技术的快速发展，以太坊作为其中的代表性平台，其智能合约的安全性受到了广泛关注。许多开发者和企业都在寻求有效的工具来检测和修复智能合约中的漏洞，以保障资产安全和业务稳定运行。然而，这也为不法分子提供了可乘之机，他们开始利用开发者对安全工具的信任，通过伪装成合法的漏洞扫描工具来实施攻击。近日，网络安全研究人员在NPM（Node Package Manager）平台上发现了一个名为“ethereumvulncontracthandler”的恶意包，该包伪装成一个用于检测以太坊智能合约漏洞的合法工具，但实际上会秘密安装Quasar RAT（远程访问木马）恶意软件到开发者系统中。此次事件再次凸显了软件供应链攻击的严重性和隐蔽性，提醒开发者和组织必须加强第三方代码的审查和安全防护措施。

### **二、事件过程**

* **恶意包发布：**

2024年12月18日，一个使用“solidit-dev-416”假名的攻击者在NPM平台上发布了名为“ethereumvulncontracthandler”的恶意包。该包声称能够检测以太坊智能合约中的漏洞，吸引了众多开发者的关注和下载。

* **隐蔽安装恶意软件：**

当开发者安装并运行该包时，它会利用复杂的混淆技术，如Base64和XOR编码，来逃避安全检测。随后，该包会从远程服务器下载一个恶意脚本，并在后台静默执行，从而将Quasar RAT部署到Windows系统中。

* **确保恶意软件持久性：**

为了使Quasar RAT能够长期驻留在系统中，攻击者还采取了多种欺骗手段。初始的npm包充当加载器，从远程服务器检索并执行Quasar RAT。一旦执行，恶意脚本会运行隐藏的PowerShell命令，并安装Quasar RAT。此外，它还会修改Windows注册表，以确保恶意软件的持久性。

* **与远程控制服务器通信：**

感染的机器会与位于captchacdncom:7000 的命令与控制服务器建立通信，使攻击者能够保持对系统的控制，并有可能进一步传播感染。

### **三、攻击技术细节分析**

* **混淆技术：**

恶意包使用了Base64和XOR编码等混淆技术，将恶意代码隐藏在看似正常的代码中，增加了检测和分析的难度。Base64编码是一种将二进制数据转换为ASCII字符串的方法，常用于隐藏数据内容；而XOR编码是一种简单的加密算法，通过将数据与密钥进行异或运算，使数据在传输过程中难以被识别。

* **恶意脚本下载与执行：**

恶意包在安装后，会从远程服务器下载一个恶意脚本。这个脚本包含了Quasar RAT的核心代码，负责实现远程访问和控制功能。下载完成后，脚本会在后台静默执行，不引起用户的注意。

* **隐藏PowerShell命令：**

为了进一步隐藏恶意行为，攻击者使用了隐藏的PowerShell命令来执行恶意操作。PowerShell是Windows系统中一个强大的脚本工具，具有广泛的系统访问权限，攻击者可以利用它来执行各种恶意命令，如下载文件、修改注册表、启动服务等。

* **注册表修改：**

通过修改Windows注册表，攻击者可以实现恶意软件的自启动和持久性。注册表是Windows系统中用于存储系统配置和应用程序设置的数据库，攻击者可以在其中添加或修改特定的键值，使恶意软件在系统启动时自动运行，从而长期控制用户系统。

### **四、恶意软件风险**

Quasar RAT是一种危险的恶意软件，具有广泛的功能，包括键盘记录、截图捕获、凭据窃取等。它能够记录用户的键盘输入，获取用户的敏感信息，如密码、信用卡号等；还可以截取用户的屏幕图像，监视用户的操作行为；此外，它还能窃取用户的登录凭据，使攻击者能够非法访问用户的账户和数据。对于处理敏感以太坊项目的开发者来说，Quasar RAT的存在将严重威胁他们的资产安全和项目机密性。

参考链接：

https://hackread.com/npm-package-disguised-ethereum-tool-quasar-rat/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

白泽安全实验室

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NpPydsaAMIN7MdZNibeGNoAT8tqwpL0jiaadMrz99YH3koiadd3bCWZXicyNqlId4PnibcJCj8JabAOvibc5uBn4G7Ow/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过