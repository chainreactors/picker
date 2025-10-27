---
title: 样本分析：CyberVolk勒索软件浅析
url: https://forum.butian.net/share/3940
source: 奇安信攻防社区
date: 2024-12-24
fetch_date: 2025-10-06T19:33:55.512662
---

# 样本分析：CyberVolk勒索软件浅析

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

### 样本分析：CyberVolk勒索软件浅析

样本
该样本是CyberVolk黑客组织使用的，该组织是一个印度网络犯罪组织，成立于2024 年 3 月 28 日，最初名为 GLORIAMIST India，后来更名为 Cybervolk。
该勒索样本原本同大多数勒索软件一样，...

样本
==
该样本是CyberVolk黑客组织使用的，该组织是一个印度网络犯罪组织，成立于2024 年 3 月 28 日，最初名为 GLORIAMIST India，后来更名为 Cybervolk。
该勒索样本原本同大多数勒索软件一样，使用AES加密算法，SHA512哈希算法用于AES密钥生成。在经过多次泄露之后进行了更新，现如今 AES 加密算法已被 ChaCha20-Poly1305 + AES + RSA + 量子抗性算法所取代。据称它是 FUD（完全不可检测）。
它可以在不需要 C2（指挥和控制）服务器的情况下进行加密和解密（离线勒索软件）。如果输入错误的密钥，加密文件的内容将被删除，如果没有数据备份，则将永远丢失。
基本情况
----
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-f827658f3256d14deddad370e2b38d94198b31b3.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-bd13f11301b8e9020e49005b0d7f1722a03d1279.png)
运行后
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-81f6feca3a0e277c7bb8a3a29072bfd51f3c2a7d.png)
CyberVolk 勒索软件运行后，立即显示支付界面，同时限制用户在系统中的操作并开始加密所有文件。
它通过阻止任务管理器等工具的打开来防止进程被中断，并在短时间内完成加密。
勒索软件为用户提供了 \*\*5 小时\*\*的支付窗口，并在系统中创建一个名为 \*\*Readme.txt\*\* 的文件。
- 在 Readme.txt 文件中，用户被要求支付 \*\*1,000 美元\*\*。如果未在 5 小时内支付，系统中的数据将被删除。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-9414f53ef5bf04dcc9c41fa7065a737be7d79830.png)
动态分析
----
### 启动流程
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ca43cd4a01ee556d6d185a6cbd9db53d9a68a013.png)
CyberVolk 勒索软件通过将一个 \*\*BMP 文件\*\*写入 `$HOME\AppData\Temp` 目录启动其进程，然后将 BMP 文件设置为桌面背景。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-8cf57380f555fd866c49e764ff7f1b5674768190.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-d269d6102f81a70d9d23e3bbdfa4246b0df68ab1.png)
`CreateThread`创建了一个线程执行了个无限循环的对话窗的创建。`DialogFunc`如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7cd059c2b3056c72e4f8cd6b246368d778c12488.png)
然后它将“time.dat”文件打印到系统中，并启动 GUI。“time.dat”中指定了 5 小时的时间，并根据那里写入的数据在 GUI 上设置了一个计时器。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1d6dcb30d35a8fdebb70f13b94d93d1cc8a8dafb.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-ffd2d156d764656a47b53ab1a11949df15928fd9.png)
在创建 time.dat 文件后，它从$HOME 目录的第一个目录开始加密。首先，它创建一个带有.CyberVolk 扩展名的文件，然后通过读取文件的内容对其进行加密，然后将加密的数据写入带有.CyberVolk 扩展名的文件中。然后，它从系统中删除未加密的文件。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-b6ac6c4dc4afb24aad0628de1fdb73ef9473731e.png)
在动态分析中监控过程操作时，观察到用于 GUI 支持的控制台 "conhost.exe" 根据主进程启动。未检测到任何额外的潜在有害进程、网络连接、持久性或其他任何方法/技术。
在观察过程中，“SafeBoot”键引起了注意。观察到 CyberVolk 勒索软件正在篡改 Windows 设备的安全模式设置。还观察到它在`$HOME\\AppData\\Roaming`目录中读取 `dec\_key.dat`。该文件未被创建，因为它没有写入。
分析中还发现了一段文字：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-006135cf71e2f826eb490385fcd0c3dca91e3f1f.png)
解密
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-0922af5ce06053a92e8ec2c3a3a8b11524bb92d7.png)
在解密过程中，详细检查了与原始密钥的对比情况，但没有发现这样的比较。CyberVolk 勒索软件不会将提供的解密密钥与原始解密密钥进行比较。
相反，在从 dec\\_key.dat 文件中获取密钥后，它使用 WriteFile API 创建一个空文件，文件名为 .CyberVolk 扩展文件的实际名称。例如，对于文件 file.txt.CyberVolk，它在磁盘上写入一个名为 file.txt 的空文件。然后，使用 NtWriteFile API，它处理解密密钥，并将加密文件的解密内容写入 file.txt。然而，在此过程中，缓冲区内存没有被检查。如果提供的密钥不正确，它不会将损坏的数据写入文件，而是写入 0 字节的数据。但如果提供的密钥是正确的，由于生成的数据不会损坏，它会正确地写入解密的文件内容。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-6f04eb5ebd24ca6d72ddea9a8d9435604f836bb8.png)
该函数针对字符串“解密密钥不正确”进行了分析，因为它可能与加密密钥有关。发现它并不检查实际的加密密钥。相反，它计算一个 36 个字符的值。如果输入的值不是正好 36 个字符，它会显示“解密密钥不正确”的消息并返回 0。然而，如果字符串是 36 个字符，它会在不验证实际加密密钥的情况下继续进行解密过程。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a9bd80cb70cc2fd253fa47ffbb5d07ccf080f5e2.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-1a35bc70901da2ba94ea14a13d4f0e3430c9e8bd.png)
当它检测到一个 36 位的值时，观察到它开始解密过程。同时，在\\_fopen 代码结构中执行写操作。在这里，从用户接收到的 36 字节值被打印在 dec\\_key.dat 上，该值在动态分析中显示。
静态分析
----
### 反调试
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-fc589ea1d6fb6a6d31fa35947ef2b225ccf6d86c.png)
CyberVolk 使用 `IsDebuggerPresent` 检测调试器，并在检测到调试器时终止运行。如果未检测到调试器，则继续执行 `resetGlobalVariable()` 函数。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-c2aeeaf13873eb8a7b68de4f8f19055e64b1b1d3.png)
"IsProcessorFeaturePresent" API 确定特定处理器功能是否受到其运行的计算环境的支持。
还观察到勒索软件访问与 CPU 相关的信息。使用 CPUID 指令来区分虚拟环境和物理环境。CPUID 查询处理器的属性并检查虚拟化指标，以确定环境是否为虚拟机。
- 使用 `CPUID` 指令获取处理器属性，判断运行环境是否为虚拟机。
- 通过 `IsProcessorFeaturePresent` 检查处理器的支持功能。
### 蠕虫式传播功能
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-a28e62c66f6a5ee1379342fb9a2c32ac636982e1.png)
CyberVolk 勒索软件被发现包含类似蠕虫病毒的活动。它扫描所有驱动器字母，从 "a" 到 "z"。如果这些驱动器是可以传播自身的类型（可移动、硬盘、网络），它会在这些驱动器上创建一个多线程进行执行。这个结构具有像蠕虫一样的自动传播功能。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-dedc2f07b0efa709fc9e9e886ee0c282c75c085f.png)
CyberVolk 勒索软件通过在一个不同的线程中以无限循环等待 1 秒，持续搜索名为 "TaskManagerWindow" 的窗口，使用 "FindWindowA" API。当找到该窗口时，它通过 PostMessageW API 发送 0x0010 (WM\\_CLOSE) 来关闭窗口。这防止用户通过任务管理器终止 cybervolk 勒索软件进程。
当解密过程完成后，程序使用\\_exit(1);函数自行终止。然而，由于它不涉及任何持久性、不将自身写入进程或使用任何其他技术/方法，因此在自清理阶段，它除了自行终止外不执行其他任何操作
漏洞
--
与大多数勒索软件不同，CyberVolk 勒索软件首先启动图形用户界面，然后开始使用多重威胁加密系统。在此期间，发现任务管理器被阻止以防止进程被中断，但 PowerShell 没有被阻止。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-64a0cc34bcee84c94d795119ab5dc79e5d4d5ead.png)
一旦图形用户界面启动并在 PowerShell 中给出必要的命令以终止该进程，加密过程就会被中断。
由于其结构中不包含任何持久性特征，Cybervolk 勒索软件在设备重启时不会重新激活或尝试重新加密文件。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/11/attach-7ea890d5fd2935abcf1350fd198cff8cc7944ab5.png)
此外，CyberVolk 勒索软件通过从 18,000 秒持续倒计时来运行，如 time.dat 文件中所写。可以通过修改 time.dat 文件手动调整计时器，这允许倒计时无限延长。这一能力可以为逆向工程、取证和恶意软件分析团队提供更多的分析时间。

* 发表于 2024-12-23 10:00:02
* 阅读 ( 2966 )
* 分类：[二进制](https://forum.butian.net/community/erjinzhi)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![Sciurdae](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bc2f26335b817b6b3b3f133f3743e19ccb490ef.png)](https://forum.butian.net/people/32432)

[Sciurdae](https://forum.butian.net/people/32432)

16 篇文章

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

#### ![Sciurdae](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bc2f26335b817b6b3b3f133f3743e19ccb490ef.png)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![](https://shs3.b.qianxin.com/attack_forum/2024/06/qrcode-eccadc95f36c47595ba2d71981950ceab25ebfe3.jpg)

---