---
title: 初探 MedusaLocker 勒索软件
url: https://forum.butian.net/share/3939
source: 奇安信攻防社区
date: 2024-12-18
fetch_date: 2025-10-06T19:36:17.435519
---

# 初探 MedusaLocker 勒索软件

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

### 初探 MedusaLocker 勒索软件

前言
MedusaLocker是一种自2019年9月开始活跃的勒索软件，主要针对Windows系统。该恶意软件通过加密受害者的文件，要求支付赎金以恢复访问权限。
样本分析
IOC
一个32位的可执行文件。
WinMain...

前言
==
MedusaLocker是一种自2019年9月开始活跃的勒索软件，主要针对Windows系统。该恶意软件通过加密受害者的文件，要求支付赎金以恢复访问权限。
样本分析
====
IOC
---
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f1c42e42e1fe7f17a6663c70fc46ae93eab88f36.png)
一个32位的可执行文件。
WinMain
-------
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ea9a4cf967f49251a178605222d55f81a35646c7.png)
### 创建互斥体
在开头，可以看到恶意软件最常用的一个技术之一，创建互斥体，确保单一实例的运行。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-0db22b3d094dbd6cb64f8373bb3782889e898e98.png)
一个函数是一个简单的打印子程序，上面写着"\[LOCKER\] Is running\\n"。不过，打印功能被禁用了。第二个函数是字符串格式化函数，用于格式化唯一的互斥体，然后将其传递给创建互斥体的函数。
创建互斥体的函数是`sub\_405630`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-5b1c2040196c4a3a7d013a2179674c3a522824e9.png)
### 权限提升
勒索软件要想进行任何操作，都需要先提升权限。往下进入else分支：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-2e4afc0823b556204622dbeffe7de35c77964ecd.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-76929e126258787fdae08fe8d5a20b02bb7a8a90.png)
`sub\_420AE0`函数的一个逻辑如下：
```plaintext
Start
↓
获取当前进程句柄
↓
尝试打开进程访问令牌 (OpenProcessToken)
↓
┌──────────────┬─────────────┐
│失败 │成功 │
│返回false ↓ │
│ 查询令牌提升状态(GetTokenInformation)
│ ↓
│ 是否提升(TokenInformation != 0)?
│ ↓
│ 是 否
│ 返回true 返回false
```
如果这里没有提升权限成功，返回了false，就会进入下面的`sub\_420C80`中，如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d208ac9f5337eaedef21352a582ea3de30f8721e.png)
这里涉及权限提升的关键组件（`Elevation:Administrator!new:`），它通过滥用 COM 对象来绕过 UAC（用户账户控制）这一内置安全措施。CMSTPLUA COM 接口存在一个已知的 UAC 旁路。
具体来说它通过初始化COM (CoInitialize)，获取了相应的CLSID和IID，通过这个来构造一个Elevation字符串路径，尝试获取管理员权限的COM对象。构造的 `Elevation:Administrator!new:` 表明目标是提升当前进程的权限为管理员权限。
### 禁用UAC
接着向下分析，在提权后的下个函数`sub\_420BB0`中，勒索软件对注册表进行了某些操作，如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-6ac2cb1ab771cd0c7de8b3ce742a659d6f80e6f3.png)
一开始以外是通过注册表实现持久化，实际发现这里再禁用UAC，它修改了系统与 UAC（用户账户控制）相关的注册表项。
操作如下：
- 打开注册表路径 `HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`。
- 修改以下两个值：
- \*\*`EnableLUA`\*\*：
- 该值控制 UAC 的全局开关。设为 `0` 会完全禁用 UAC。
- \*\*`ConsentPromptBehaviorAdmin`\*\*：
- 该值控制管理员账户的 UAC 提示行为。设为 `0` 表示禁用所有提示。
### 持久化
向下，函数`sub\_405680`内。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d04817cedc5b921f85be590d8036b40f624b65ab.png)
注册表键值的路径是 "HKEY\\_CURRENT\\_USER/SOFTWARE MDSLK/Self"。MDSLK 的缩写可能是 medusa locker。这里的操作是该勒索软件的一个独特行为，即它会在注册表中添加一个标记键值，用于表示系统已被感染。
勒索软件使用不同的方式，即无限期地调度重复15分钟的任务来实现持久性。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-66f649d92d11fa21a4cce879ac559a153024a26f.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-96aa123d7d53cca571ea307c2defc23d41c7ee61.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f274d5ecb14b696498f00b58501fe9cc1e400297.png)
恶意软件会在系统的 %APPDATA% 中创建一个名称为 "svhost.exe "的自身副本，并在任务调度程序中注册，每隔 15 分钟无限期执行一次。这时就需要使用互斥，当再次执行时，它会首先检查系统中是否已经运行了另一个实例。如果有，恶意软件就会退出，让前一个实例继续运行。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7d1caa2aff3fcab89b4a1a8d84ba1a827e29d250.png)
### 删除进程
它会停止并删除一组预定义的服务和进程，以避免其加密过程受到任何干扰。通过对二进制文件中的字符串进行简单的静态分析，就能发现这些服务集。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7b109d33037ec2752a0f6c4733913c97d7e50a18.png)
上面函数通过服务管理器控制指定的服务，尝试停止运行中的服务并监控服务状态的变化。
- 调用 `OpenSCManagerW` 以获取服务控制管理器的句柄 `hSCManager`。权限标志 `0xF003F` 表示请求所有访问权限（读、写、启动、停止等）。
- 使用 `sub\_407A40` 从 `a1` 获取服务名称（`v2`）,调用 `OpenServiceW` 以打开指定的服务句柄，权限标志 `0x2C` 包含查询状态和控制服务的权限。
- 调用 `QueryServiceStatusEx` 获取服务的当前状态
- 调用 `ControlService` 尝试停止服务
而要关闭的服务被硬编码进内存中，可以在ida中直接观察到：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-11d97ec446e1bb2b79713aee530ccc9ae5d0c46d.png)
### 禁用系统恢复
与大多数勒索软件一样，MedusaLocker也试图删除受害者系统中的数据恢复方式。不过，与大多数勒索软件不同的是，它是通过删除多个恢复选项来实现这一目的的，而不仅仅是删除卷影副本。
它使用`vssadmin`和`wbadmin`从系统中删除卷影副本。它还使用`bcdedit.exe`删除其他恢复选项，以防止系统重新启动进入恢复模式。作为额外步骤，它还会清空回收站以确保万无一失。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-08636793e34651dbc148698389bc726bc2538035.png)
上面列出的每一条命令都是由`CreateProcessW`执行的，它将第一个空格作为进程名称的指示符，其余部分作为该进程的参数。`sub\_41E9A0`的子程序创建这些进程的过程如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7a25b925b3b24ab2dbbea957d6e781b589623eee.png)
总的来说，它启动外部进程并等待其结束。
### 加密
勒索软件也使用对称加密来对文件进行加密，它使用AES-256算法。不过，又不同于一般的AES，它在过程中添加了RSA算法，加密密钥使用嵌入恶意软件的预定义公钥加密，只有使用攻击者的私钥才能解密。恶意软件作者在编写代码时，会使用随机生成的 AES 密钥对每个文件进行加密，然后再使用 RSA 公钥进行加密，并与多份赎金说明一起保存在系统中。
公钥经过base64编码后也是硬编码进了内存，
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-3394359c931e25e96b7273be3e6f751f1d396f12.png)
使用`CryptStringToBinaryA`应用程序接口将 base64 编码的密钥转换为二进制格式，以便在加密函数中使用，如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-75eae7af90611f5635f13297ece1ce22fa5ffc24.png)
最后，使用`CryptGenKey`生成对称密钥，使用公钥对其进行加密，并保存在html赎金说明中。之后，加密器启动，加密过程中会跳过重要的文件夹和扩展名，如提取的字符串，如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9367a6153ea0bcbb9f7fbc3d87bd0d65e0947c36.png)
### 横向移动
勒索软件还具有一个网络模块：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-6268dc721a46aa27dc79ca2048d3f70c50f0e1fe.png)
`sub\_41DB40` 是一个用于执行 ICMP echo 请求（即 ping 操作）的函数。它通过发送 ICMP 请求并等待响应来检查目标主机的可达性。函数内部使用了 `IcmpCreateFile` 和 `IcmpSendEcho` 来执行 ICMP 请求，并返回响应结果。
通过这个函数，它能够与本地网络中的远程系统建立连接，并扫描SMB共享。第一步是按顺序向每个系统发送 ICMP "Ping"，并验证是否收到响应。之后，恶意软件会继续检查系统中是否有任何打开的 SMB 共享，但不包括名称中带有 " "的共享，这表示隐藏共享。然后，恶意软件会将剩余的共享累加到一个列表中，并在稍后阶段进行加密。

* 发表于 2024-12-17 09:00:01
* 阅读 ( 3038 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![友人Aaaaaaaaaa](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/36845)

[友人Aaaaaaaaaa](https://forum.butian.net/people/36845)

5 篇文章

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

#### ![友人Aaaaaaaaaa](https://forum.butian.net/static/images/default_avatar.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---