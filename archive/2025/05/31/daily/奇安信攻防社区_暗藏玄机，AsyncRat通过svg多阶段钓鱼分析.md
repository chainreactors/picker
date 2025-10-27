---
title: 暗藏玄机，AsyncRat通过svg多阶段钓鱼分析
url: https://forum.butian.net/share/4354
source: 奇安信攻防社区
date: 2025-05-31
fetch_date: 2025-10-06T22:23:42.350325
---

# 暗藏玄机，AsyncRat通过svg多阶段钓鱼分析

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

### 暗藏玄机，AsyncRat通过svg多阶段钓鱼分析

攻击者通过伪装成司法部门，进行钓鱼攻击。

初始样本
====
初始样本为一个svg文件，在浏览器中显示如下，翻译成中文大致意思为
```php
哥伦比亚共和国司法部门，官方通知的紧急传票。如果在法定期限内不作出回应或出庭，可能会面临财产扣押、资金冻结等强制措施，并且可能产生额外的处罚，包括信用记录受损和强制执行。所有详细信息、证据和法律效力都包含在一个PDF文档中。
```
并提供了一个下载pdf的按钮。
![1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-18bd98514b7fefc82387c00dca9292081e0d5ceb.png)
分析发现，点击任意地方都会下载一个托管在discord服务器中的名为Documentos\\_xxxxx.js的文件。
![2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-845784067d5c92783420a1b1f4237434d9bb86b3.png)
JScript样本
=========
分析Documentos\\_xxxxx.js，发现此文件存在大量垃圾无意义代码。
![3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-764822aff3f47733bb7f7eccd1cf5ed98b8fd04e.png)
仔细多次分析后，发现在文件的靠后位置，出现了实际代码，会在一系列字符串操作后被还原成明文字符串。根据代码，得出结论此文件并非是`JavaScript`，而是`Windows JScript`脚本文件。在Windows系统中，js后缀的文件默认双击后会被`wscript.exe`程序解释并执行。
![4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-ffec923337dfe6168cf99e03195539e8d929a48e.png)
将实际代码提取出来，并用`WScript.Echo`输出最终字符串。
![5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-f35552a245ca24f665858309ec547800ec16103f.png)
也就是说此脚本会执行下方的`powershell`命令
![6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-3a75d1015210c2f2b2944850785e5756a5dbfabf.png)
Powershell样本
============
将被编码的`powershell`代码解码
![7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-39a0d9a4f1cff3421954b0746d882779f627c8d4.png)
继续分析，代码功能为从archive.org服务器中远程下载一个 new\\_image.jpg 文件，并解析其中被base64编码后的.NET程序，然后反射加载并调用。
![8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e57f738799c42229016eb8fcd567ca53efc306b1.png)
new\\_image.jpg 是一个图片文件，在文件尾部追加了一个base64编码后的.NET程序
![9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-38deb0807e1320bcfe347488ca8876d3cecab417.png)
.NET Dll样本
==========
此.NET程序为一个dll文件，有一定的混淆，使用de4dot反混淆后继续分析。
![10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-3785c67116513d5e0d10faad0aa048cf9f4e1d0a.png)
反编译后，发现该dll为在开源项目`dnlib`中新增了恶意代码，攻击者应该是想通过添加白程序代码，来逃避机器学习查杀。
![11.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-af38eecd7042d5a8562bfd0ae63d506f7841287c.png)
在powershell中会调用`dnlib.IO.Home`中的`VAI`方法，由于dnspy不能直接调试dll，这里我使用了 <https://github.com/hexfati/SharpDllLoader> 来主动加载dll。在调试的时候再把参数通过命令行传入即可。参数为
```php
-d "C:\Users\xxxx\dump.dll" -n dnlib.IO -c Home -m VAI -s true --margs "txt.eliFdetrevnoC/xxxx/xxxx/stnemhcatta/moc.ppadrocsid.ndc//:sptth 1 C:\Users\Public\Downloads fluctuous MSBuild js 2 "
```
![12.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-cfe766cf28fe03996c589b626949dc55c9f41bce.png)
代码中`Class237.smethod\_0`的出现频率很高，后续分析出，此方法实际为字符串隐藏，只有在调用的时候才会中hash表中，通过键取出。这里的`Class237.smethod\_0(12359)`会返回字符串`1`。
![12\_1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-9b706dc2bf144f9f54d7ffaa1978eff704897ba5.png)
分析其字符串隐藏原来，会读取名为`hIXS`的资源，里面包含了所有的加密后的字符串。
![12\_2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-fff79c889a010f43fffb6a45a65671e7de4fc16f.png)
在内存中动态创建一个名为`?`的.NET模块，再创建一个名为`?`的静态函数。
![12\_3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-1f9dc2a9813611a32d16bbd8a847483a689ed74d.png)
继续分析刚创建的模块，发现其将所有字符串取出，并存储在hash表中
![12\_4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-2500644790496afdd8c4cd106c185ec91edccfea.png)
读取时，根据键来读出实际字符串。
![13.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-606153cb1ef0f7e83a25e19a27454616f7a7fec1.png)
继续分析其功能代码，包含了虚拟机检测功能
![15.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-7ce117b2679f273afd0e05d9bf959bda652797f0.png)
计划任务进行权限维持
![15\_1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-7df1f53c14eeda6b2f699512d0323b4414947187.png)
通过注册表`HKEY\_CURRENT\_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`进行维权
![15\_2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-66ee500853a014eccf7e86b21e40f3dc24d60b18.png)
通过反射加载存放在资源文件中的`UAC.dll`进行UAC Bypass。
![15\_3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b29999a976fcb13307295cccd7b3f704cd67f09d.png)
`UAC.dll`使用了cmstp实现UAC Bypass。
![14.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-947b362fb46d8734a8388765a71d91f776e2298b.png)
远程下载 `https://cdn.discordapp.com/attachments/xxxx/xxxx/ConvertedFile.txt` 解码后提取出PE文件。然后根据PE文件的`IMAGE\_OPTIONAL\_HEADER`中的`Magic`字段来选择要使用的傀儡进程注入技术。其中32位程序的`Magic`字段为`IMAGE\_NT\_OPTIONAL\_HDR32\_MAGIC (267)`，64位程序则为`IMAGE\_NT\_OPTIONAL\_HDR64\_MAGIC (523)`。
![16.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-a4fe335dff317166c3f87a755195657b15e6ba18.png)
为32位程序时，使用如下傀儡进程注入技术。
![17.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-c3cd47677c8f1f46a1f9f56fa6ef3325f384310f.png)
为64位程序时，使用如下傀儡进程注入技术。
![18.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-1a690432a656350c53882414ee757f29f2a28333.png)
根据传入方法的参数，会将`Documentos\_xxxxx.js`复制到`C:\Users\Public\Downloads\fluctuous.js`并添加注册表自启动。然后从`https://cdn.discordapp.com/attachments/xxxx/xxxx/ConvertedFile.txt`中下载并解码，再创建傀儡进程`MSBuild.exe`并注入payload。
不过由于链接目前已失效，导致无法分析其最终的payload，在`virustotal`搜索了一下，发现有人已经传过了。
![19.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-458da9cf41ed6eadc3fcda340ac47666522b74af.png)
最终注入的应该是一个AsyncRat木马。
![20.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-9ec6fe927b08f7e2396ae785aef2227b47a2258c.png)
总结
==
攻击者实现了一次多阶段的钓鱼攻击，大量使用了合法的网站来托管恶意payload，并使用内存反射加载来逃避查杀。在企业中对陌生邮件一定要警惕，不运行可疑文件，防止成为攻击者的"肉鸡"。

* 发表于 2025-05-30 09:00:00
* 阅读 ( 2405 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![Aris](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/8047)

[Aris](https://forum.butian.net/people/8047)

1 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![Aris](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---