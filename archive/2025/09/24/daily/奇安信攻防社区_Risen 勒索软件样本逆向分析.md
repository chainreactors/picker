---
title: Risen 勒索软件样本逆向分析
url: https://forum.butian.net/share/4562
source: 奇安信攻防社区
date: 2025-09-24
fetch_date: 2025-10-02T20:33:41.023355
---

# Risen 勒索软件样本逆向分析

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### Risen 勒索软件样本逆向分析

* [漏洞分析](https://forum.butian.net/topic/48)

Risen 勒索软件是一种加密型恶意软件，它侵入受害者系统后，会加密并重命名文件（通常在原扩展名后添加电子邮件地址与用户 ID，如 “.Default@firemail.de].E86EQNTPTT”），同时在桌面和登录前屏幕显示勒索信息，然后留下两个勒索信文件（“Risen\_Note.txt” 和 “Risen\_Guide.hta”），要求受害者联系攻击者（通过提供的邮箱地址）并在三天内合作，否则威胁泄露或出售网络中的数据。

勒索软件简介
======
Risen 勒索软件是一种加密型恶意软件，它侵入受害者系统后，会加密并重命名文件（通常在原扩展名后添加电子邮件地址与用户 ID，如 “.Default@firemail.de\].E86EQNTPTT”），同时在桌面和登录前屏幕显示勒索信息，然后留下两个勒索信文件（“Risen\\_Note.txt” 和 “Risen\\_Guide.hta”），要求受害者联系攻击者（通过提供的邮箱地址）并在三天内合作，否则威胁泄露或出售网络中的数据。
![Pasted image 20250902145535.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-b8bfbbd2b51d25733b1f9dc28cd82133846071ad.png)
修改桌面如下：
![Pasted image 20250902145815.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-1789d4a3986cb18f99c7189fbc1b7c14f8cf792b.png)
勒索信息样例如下：
```php
RisenNote :
Read this text file carefully.
We have penetrated your whole network due some critical security issues.
We have encrypted all of your files on each host in the network within strong algorithm.
We have also Took your critical data such as docs, images, engineering data, accounting data, customers and ...
And trust me, we exactly know what should we collect in case of NO corporation until the end of the deadline we WILL leak or sell your data,
the only way to stop this process is successful corporation.
We have monitored your Backup plans for a whileand they are completely out of access(encrypted)
The only situation for recovering your files is our decryptor,
there are many middle man services out there whom will contact us for your caseand add an amount of money on the FIXED price that we gave to them,
so be aware of them.
Remember, you can send Upto 3 test files for decrypting, before making payment,
we highly recommend to get test files to prevent possible scams.
In order to contact us you can either use following email :
Email address : [Default@firemail.de](mailto:Default@firemail.de)
Or If you weren't able to contact us whitin 24 hours please Email : [default1@tutamail.com](mailto:default1@tutamail.com)
Leave subject as your machine id : R9HMWW0M9J
If you didn't get any respond within 72 hours use our blog to contact us,
therefore we can create another way for you to contact your cryptor as soon as possible.
TOR BLOG : [http://o6pi3u67zyag73ligtsupin5r ... pfttxqu7lsuyd.onion](http://o6pi3u67zyag73ligtsupin5rjkxpfrbofwoxnhimpgpfttxqu7lsuyd.onion/)
```
逆向分析
====
基础信息
----
样本文件
![Pasted image 20250902150908.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-8956d4ba59e20d9f0bb05ae6a838aad22211778c.png)
我们先用die看一下软件样本的基础信息
![Pasted image 20250902151245.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-00217db29c31412462a9c25aeab6dfa5098dbf69.png)
抗检测技术
-----
用ida pro打开样本进行逆向分析。与许多精心设计的恶意软件一样，Risen 的首要行动都是为了生存并确保其能够不受干扰地运行。首先，它创建一个名为 RISEN\\_MUTEX 的\*\*互斥锁\*\*，以确保在同一时间只有一个程序实例可以在系统上运行。这可以防止多个实例尝试加密相同的文件，这可能会导致文件损坏或触发安全警报，造成勒索失败。
![Pasted image 20250902152511.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-7f66a6a7e476c5e8eea1da081d05345b873e7d33.png)
接下来，它执行了一个巧妙的自我保护行为：\*\*地理围栏\*\*。恶意软件调用 GetSystemDefaultUILanguage API 来检查计算机的默认语言，这是 Windows 系统提供的 Win32 API 函数，用于获取操作系统默认用户界面语言（即安装时的界面语言）的语言标识符（LANGID）。然后，它将结果与五种语言代码的硬编码列表进行比较。如果系统的语言与其“不攻击”列表中的语言匹配，勒索软件将立即终止。这是攻击者用来避免攻击本国或特定国家而设置的黑名单，避免被这些国家的执法机构溯源和追踪。
![Pasted image 20250902152759.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-f4f8e3eab20419d8395670f94e122b38c55cbc87.png)
在此设置过程中，它还会创建一个名为 Risenlogs.txt 的日志文件，该文件可能是其开发阶段的残余文件，用于调试目的。
![Pasted image 20250902152815.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-3cd6140a54f64c682dc58c27a7d1da5bbbdcd712.png)
持久化
---
Risen 完成系统环境检测后，它的下一个优先事项是确保它能够在系统重新启动后幸存下来。
为了实现这一点，它通过创建计划任务来建立持久性。它使用 Windows schtasks.exe 命令行程序，设置一个名为 \*\*SystemDefense\*\* 的任务。该名称是精心选择的，听起来像一个合法的系统进程，使其能够逃避用户或管理员的检查。此任务可确保在加密完成之前重新启动系统时，勒索软件也会自动再次运行。
![Pasted image 20250902153430.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-099e84c1f46da96ecd8d944d51290619ff8ff83f.png)
![Pasted image 20250902154225.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-2005acfc9ad22b2b0f1ce9fab8aa459f5566d851.png)
在确保自身持久驻留之后，恶意软件开始侦察系统环境，识别适合加密的目标。它通过遍历所有驱动器，并调用 \*\*GetDriveTypeW\*\* API 来判断哪些卷是本地硬盘（如 C: 或 D:）。接着，它参考位于 `off\_44CB08` 的内部配置数组，只选择高价值的本地文件进行加密，同时避开网络驱动和移动设备，以降低风险。
![Pasted image 20250902154252.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-c017194e8ee0a6bfbcd6897a168703e78c6b13bf.png)
勒索过程分析
------
在确认目标驱动器后，Risen 勒索软件进入其核心阶段：加密受害者的文件。它会递归遍历目录，并运用加密算法锁定数据，使其彻底无法访问。
加密完成后，它会告知受害者发生了什么以及如何付款。在其中发现了一个硬编码的字符串，其中包含威胁方的联系方式：Telegram 用户名 \*\*@tokyosupp\*\*。这成为受害者与攻击者沟通、协商支付并获取解密密钥的渠道。与使用 Tor 隐藏服务的更成熟操作不同，这种依赖公开平台的方式表明，虽然攻击者资源有限，但仍极具危险性。
![Pasted image 20250902155020.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-a461cb24a72df2c8e09b05fe53f390cdb165dffd.png)
设置桌面图片
![Pasted image 20250902181650.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-297a856608770ea1d13cea42b0e075f1cf7acef0.png)
创建勒索信息文本文件Risen\\_Note.txt和 Risen\\_Guide.hta
![Pasted image 20250902181941.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-b702b89abb0371b0f9de854b37a7916121b68d0b.png)
加密算法分析
------
ida pro反编译勒索软件总是失败，于是换成了Ghidra来反编译并分析加密的过程。
先用搜索功能定位一下加密的函数：
![58b590b67a4a061000077be1b69e67b9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-9e6770c3159f542aa49b8b814030eabf540dd664.png)
加密的主流程在FUN\\_00401760函数中：
首先是\*\*加密函数初始化部分\*\*，主要是文件操作和加密准备，并在文件尾部或缓冲区写入了 `"RISE"` 标记，用来识别文件状态。
![9f4553fea8ca1b5f39b79d3bf9ab1e68.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-f1e4452dd11e439860086dd8230bd6693266902c.png)
然后调用FUN\\_00401150生成密钥
![d92901b629fde1a6bed38b2a53a1e474.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-c1488a92caf387053b27ebad3866cf9a8c1f5b09.png)
跟进FUN\\_00401150查看一下密钥生成方法，代码很长，只截取了一部分，总结一下就是，本地随机生成一个 256-bit 会话密钥和 nonce，用它们初始化加密函数，对文件进行流加密；然后再用攻击者内置的 \*\*RSA 公钥\*\*加密这个会话密钥，并把结果写到文件头，最后清理内存中的明文密钥。
![40f9a9bd49be6f0be792ee9384a28cb8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-5cc32e8990a0b1cd72b9ceb63316a2df950ca485.png)
![16519875b88327d234066be2ef4e41cb.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-b4c0d1910c9eb8f45ffe48992b96e93ac741f1e2.png)
![4529e56237764909f3c1df93ea5c5a82.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-3492402c42a3994d956fad9dc01150d2fa915b6f.png)
我们继续回到加密主流程函数FUN\\_00401760，获取到密钥后开始加密环节，这段代码是勒索软件里常见的\*\*文件加密逻辑\*\*，即：\*\*分块读取 → 算法加密 → 覆盖写回\*\* 的分段选择性加密，具体的加密调用了FUN\\_00402050函数
![40495c5f71e605fe4b77914ea0a8accf.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-c43cd469b0c20fafb7d8c56a87a950098adc1a1a.png)
![747e0363ae64dbc87cc856f7c2ebdf82.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-b569b4a996701a4919e38eeb24b98d2c594c7043.png)
我们再跟进FUN\\_00402050函数查看一下具体是什么算法,根据代码可以看出是流密码的加密方式，使用 \*\*ChaCha20算法\*\*生成 keystream，把文件数据和 keystream 逐字节 XOR，加密结果写回原文件。
![0a40482566fa7914918317ab5fd9f2f4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-ff01abf576631de6a96f8a4df939541293c276d3.png)
这是FUN\\_00401760的结尾部分代码，这里在执行替换文件名的操作，即在原扩展名后添加电子邮件地址与用户 ID，如 “.Default@firemail.de\].E86E...