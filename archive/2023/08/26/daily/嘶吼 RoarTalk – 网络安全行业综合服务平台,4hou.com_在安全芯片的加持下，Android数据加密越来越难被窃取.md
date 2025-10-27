---
title: 在安全芯片的加持下，Android数据加密越来越难被窃取
url: https://www.4hou.com/posts/gDK3
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-26
fetch_date: 2025-10-04T11:58:50.205729
---

# 在安全芯片的加持下，Android数据加密越来越难被窃取

在安全芯片的加持下，Android数据加密越来越难被窃取 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 在安全芯片的加持下，Android数据加密越来越难被窃取

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-08-25 11:30:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)121874

收藏

导语：我们将在本文介绍分析静态数据加密。

![cool-picture.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230823/1692777936135557.png "1692777936135557.png")

**Android FBE的背景**

我们将在本文介绍分析静态数据加密。Android FBE是Android Full Disk Encryption的简称,是一种安全机制,用于对Android设备的所有数据进行加密,保护用户的个人隐私和敏感数据。

简而言之，此功能允许永远不以明文形式存储文件，以防止攻击者通过简单地提取存储设备来读取它们。相反，文件在加载到内存中时（例如，通过文本编辑器）会自动解密，并在写回磁盘时再次加密。这要归功于操作系统的支持，Android历来使用两种方法：全磁盘加密（FDE）和基于文件的加密（FBE）。顾名思义，基于文件的加密在文件级工作。也就是说，每个文件都有自己的密钥，并且可以独立于其他文件进行解密。Android依赖于Linux内核特性fscrypt来实现这一点，该特性在Ext4和F2FS等各种文件系统中都得到支持。在为目录树获得主密钥之后，系统将为文件、目录和符号链接检索单独的密钥。

由于采用了文件级方法，FBE实现非常精确。Android利用这一点将文件划分为两个加密级：

设备加密（DE）：文件在启动后立即可用；

凭证加密（CE）：文件只有在用户进行身份验证后才可用（这是用户数据的选择级别）。

在启动设备时自动派生DE密钥，考虑到这一点以及它所保护的数据类型，从攻击者的角度来看，它并不是特别有趣。然而，值得注意的是，这是直接启动功能的基础，允许在用户进行身份验证之前解锁设备的某些功能，比如警报。

尽管如此，由于攻击者的目标可能是检索私有数据，因此本文主要关注CE密钥。派生它的步骤相当复杂，过程从系统拥有的一些DE保护文件（在/data/system\_DE//spblob中）开始。最终密钥的原始字节实际上是从凭证的原始字节派生出来的。尽管过程复杂，但这意味着无论攻击者可以利用多少漏洞，他们仍然需要暴力破解凭证以将其提供给密钥派生过程。

**使用TrustZone派生CE密钥**

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230823/1692777948114244.png "1692777948114244.png")

上图显示了派生CE密钥所需的不同组件是如何链接在一起的。如上所述，这是一个相当复杂的过程，所以我们建议在一个单独的选项卡中打开图片。对于没有配备安全芯片的设备，密钥派生来自两个不同的受保护组件：

特权用户（system或root）拥有的文件：普通用户无法访问；

TEE保护密钥：这些密钥只能在TEE内部由Keymaster应用程序使用。这些密钥也是与身份验证绑定的，因此只有在用户成功通过身份验证时才能使用它们。

这意味着攻击者应该能够提升权限并篡改可信执行环境，以便提取密钥或能够在身份验证之前使用密钥。为此，我们有必要了解Gatekeeper如何进行身份验证。

**使用Gatekeeper进行身份验证**

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230823/1692778027944337.png "1692778027944337.png")

Gatekeeper是TEE中经常出现的可信应用程序（TA）之一，通过与相应的Android守护进程以及硬件抽象层通信，它在验证用户的身份验证凭证方面发挥着关键作用。请注意，Gatekeeper仅通过PIN/密码/模式参与身份验证，而其他TA用于支持生物识别。尽管如此，当用户在启动设备时首次进行身份验证时，他们无法使用生物识别技术，原因恰恰与数据加密有关。

Gatekeeper实现了两个概念上简单的命令：Enroll和Verify。通常在用户首次设置身份验证因素或更改身份验证因素时调用Enroll。该命令接受一个所谓的密码（pwd） blob，对其进行签名，然后返回，将其转换为密码句柄。密码blob是从凭证创建的，凭证首先使用scrypt进行扩展，然后与哈希字符串组合。用于签名所提供的密码的密钥是Gatekeeper的内部密钥，用于验证凭证。这样的功能是通过Verify命令实现的，而在用户尝试进行身份验证时调用该命令。顾名思义，它验证当前身份验证尝试的密码blob是否有效。它通过计算其HMAC并将其与原始密码句柄进行比较来实现这一点，原始密码句柄也与命令一起发送。

Scrypt是一个密钥派生函数，在这种情况下，它通过需要大量内存来减缓自定义硬件攻击。它的参数与凭证的盐值一起存储在一个文件中。这意味着每次身份验证尝试的延迟可以忽略不计，但却让需要多次进行身份验证的攻击者减慢了速度。

如果身份验证成功，Gatekeeper将创建一个身份验证（auth）令牌。这是一个标准格式的签名令牌（如AOSP中指定的），旨在防止重放攻击。此令牌证明用户已通过身份验证，需要发送给Keymaster TA以解锁绑定身份验证的密钥。如果身份验证尝试失败，Gatekeeper的节流机制就会启动，使暴力破解变得不可能。这是与实现相关的，但通常TA存储有关每个失败请求的时间的信息，并在此类失败请求的频率变得可疑时开始返回错误。当用户再次成功进行身份验证时，计数器将重置。

**合成密码**

用户通过身份验证后，系统就有了一个有效的applicationId。在真正成为CE密钥之前，还需要经过几个步骤。对我们来说，第一个也是更有趣的是合成密码的推导过程。检索到这些信息后，还有许多一些操作，但是这些步骤不需要用户或某些受信任的组件提供任何信息。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230823/1692778040798205.png "1692778040798205.png")

合成密码存储在Android文件系统中，必须用两个不同的密钥解密。第一个是存储在Android Keystore中的常规密钥，该密钥受TEE保护并绑定身份验证。由于这些密钥永远不会离开TEE，因此它们以加密形式存储，并且需要在Keymaster TA中进行解密。除此之外，如上所述，只有当命令还包含先前由Gatekeeper生成的验证令牌并且仍然有效时，才能使用它们。一旦在TEE中完成了第一次解密，就使用哈希的applicationId作为密钥再次解密中间缓冲区。注意，这里的AES是使用GCM模式完成的，如果密钥出现问题，则由于标记不匹配而导致操作失败。

此时，攻击者基本上需要完成三件事才能恢复CE密钥。首先，他们需要能够检索特权用户拥有的文件，这很可能是利用了一个包含多个漏洞的内核漏洞。然后，他们还必须篡改TEE，要么从Keymaster泄露所需的密钥，要么攻击Gatekeeper中的凭证验证和认证令牌生成。最后，他们需要对获得的信息执行暴力破解。

**用于Gatekeeper的PoC**

研究人员在三星A22设备（更准确地说是在A226B和A225F）上实现了PoC，这些设备使用来自Mediatek 的两个易受攻击的SoC： MT6769V和MT6833V，可以使用MTKClient利用。该工具与下载模式（类似于高通soc上的EDL模式）交互，该模式暴露了一个USB接口，该接口最初用于在其上执行支持操作（例如刷新固件）。要触发该漏洞，就必须物理访问，并且在某些设备（如A225F）上，必须在设备PCB上短路两个引脚才能进入下载模式。一旦设备以正确的模式启动，该工具利用Boot ROM漏洞，然后修改BL2（在Mediatek 启动模式中称为preloader）以禁用下一个安全启动检查，最后将其加载到设备上并在其上启动。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230823/1692778054169884.png "1692778054169884.png")

但要实现攻击，就需要修复以下组件：

1.BL3，它被称为小内核（简称为LK），禁用Android验证启动检查，因为我们想要启动修改的Android映像；

2.Android系统（在本示例中为启动镜像），授予我们root访问权限，并修改供应商分区中存在的Gatekeeper Trusted应用程序；

3.TEE操作系统（称为TEEGRIS）禁用对受信任应用程序的验证。

获得Android系统最高权限（Android Rooting）

为了实现Android Rooting，我们使用了Magisk。用修复的Gatekeeper TA替换它，我们只需要在SPU分区中创建一个新文件，然后Magisk的init程序在启动时将其安装在现有文件的位置。这种方法的优点是，它可以简单地替换任何文件，因为我们只需要将它放在复制目录树的SPU分区中。

一旦完成，我们就可以对设备进行root访问，然后使用它来访问CE密钥派生中涉及的文件。

**修复TEEGRIS**

TEEGRIS是三星设计的TrustZone操作系统，可以在Exynos和Mediatek 的soc上找到。它的设计和逆向工程已经被介绍了很多次，所以本文只关注我们需要修复的部分来实现我们的目标：执行修改后的TA。在本文的示例中，我们决定修复Gatekeeper，以绕过句柄验证并始终生成有效的验证令牌。

TEEGRIS分为几个镜像：

tee1.img：它包含Arm Trusted Firmware（在监视器模式下以最高权限执行-EL3）、Secure World内核和一个名为userboot.so的二进制文件。最后一个对我们来说非常重要，因为它用于加载和验证TEEGRIS的根文件系统。

tzar.img：这是TEEGRIS的根文件系统，以逆向工程的自定义压缩格式存储。它包含可供其他库使用但也可供TA使用的库，以及二进制文件，其中包括一个名为root\_task的二进制文件，负责验证和运行Android提供的TA。

super.img：它是包含几个逻辑分区的Android主分区。其中之一是供应商分区，包含大多数TA，包括Gatekeeper。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230823/1692778068106499.png "1692778068106499.png")

总而言之，我们需要修复userboot。所以二进制禁用验证的TZAR。然后，我们修复root\_task以禁用TA的验证，这样终于可以修复Gatekeeper了。

**修复Gatekeeper**

Gatekeeper用于验证用户的凭证。验证使用密钥派生函数（KDF）生成一个惟一的值，然后可以将该值与作为参数传递的预期值进行比较。在Trusty TEE实现中，KDF实际上是一个使用内部密钥的HMAC。对于TEEGRIS来说，KDF似乎是一个自定义的，显然是在加密驱动程序中实现的，至少在基于exynos的设备上，它依赖于内部加密处理器。

如果凭证匹配，Gatekeeper生成一个auth\_token并将其发送回Android，以便它可以附加到Keymaster请求。需要注意的是，这是Keymaster解密身份验证绑定密钥所必需的，例如加密的合成密码。这里有几个选项，但我们决定修复两个值之间的比较，以确保接受任何凭证。这是可能的，因为auth\_token生成机制不使用凭证中的任何位。由于进行过修改，每次我们输入一些凭证时，Gatekeeper都会生成令牌并返回成功，使系统相信它可以继续下一步来解锁设备。可以肯定的是，它不能用错误的凭证解密用户数据。但是在尝试之前，Keymaster任务必须执行合成密码的第一次解密（它被加密了两次）。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230823/1692778082754912.png "1692778082754912.png")

我们可以按照这个办法盗取第一个AES解密操作的结果。该设备是根设备，使用Frida，我们可以在SyntheticPasswordCrypto.decryptBlob中暂停请求该操作的system\_server进程。检索到该值后，我们就可以开始强制使用凭据了。

**暴力破解凭证**

暴力破解的代码如下所示：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230823/1692778097340446.png "1692778097340446.png")

从设备加密的文件中检索scrypt的参数。顾名思义，value\_leaked\_from\_keymaster就是我们通过Frida盗取的值。由于此AES\_Decrypt函数背后使用的GCM操作模式，如果密钥是错误的，解密将失败，我们知道我们需要选择另一个密码。如果成功，就意味着我们找到了正确的值。具体视频请[点此](https://www.youtube.com/watch?v=aCDdwoi9jm8?cc_lang_pref=en&cc_load_policy=1)。

就性能而言，暴力执行脚本肯定可以改进。如上所述，即使只是简单地将它移动到一个一般功能的VM上，也有显著的改进。使用专用硬件会有所不同，但这不是我们PoC的重点，我们更愿意把重点放在实现暴力执行所需的过程上。

利用安全芯片派生CE密钥

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230823/1692778173163295.png "1692778173163295.png")

上图显示了使用安全芯片时如何派生CE密钥。该模式与上一部分中介绍的模式非常相似，主要区别在于引入了一个名为Weaver的新组件，并用于生成applicationId。

**使用Weaver进行身份验证**

Weaver是一个依赖于安全芯片来存储密钥和值的服务，每个值被分配到一个唯一的插槽。它公开了一个由三个命令组成的非常简单的API：

Read：在输入中提供插槽编号和密钥，如果密钥正确，则接收相关值；

write：提供要存储的插槽编号、密钥和值；

getConfig：检索Weaver实现的配置信息。

与Gatekeeper类似，Weaver实现了一种节流机制，该机制在多次读取尝试失败后生效。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230823/1692778194126536.png "1692778194126536.png")

当安全芯片可用时，使用scrypt生成的令牌...