---
title: GoTrim：基于Go语言的僵尸网络会重点攻击WordPress网站
url: https://www.4hou.com/posts/4KO7
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-27
fetch_date: 2025-10-04T02:32:10.197955
---

# GoTrim：基于Go语言的僵尸网络会重点攻击WordPress网站

GoTrim：基于Go语言的僵尸网络会重点攻击WordPress网站 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# GoTrim：基于Go语言的僵尸网络会重点攻击WordPress网站

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-12-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)992963

收藏

导语：本文详细介绍了这个僵尸网络如何使用WordPress和OpenCart扫描和破坏网站。

FortiGuard实验室最近遇到了一个以前没有报道过的内容管理系统(CMS)扫描器和用Go编程语言(通常也称为Golang)编写的攻击破解器。在几个在线论坛上，它被描述为安装在受感染的WordPress网站上，但没有公开的分析报告。

受影响平台：Linux；

影响用户：任何组织；

影响：远程攻击者可以控制易受攻击的系统；

严重级别：严重；

Golang攻击破解器并不新鲜。例如，我们之前报道过2019年的StealthWorker活动。这个新的攻击破解器是我们命名为GoTrim的新活动的一部分，因为它是用Go编写的，并使用 “:::trim:::” 来区分与C2服务器通信的数据。

与StealthWorker类似，GoTrim也利用网络执行传播式攻击攻击。我们发现最早的样本是在2022年9月。在撰写本文时，该活动仍在进行中。

本文详细介绍了这个僵尸网络如何使用WordPress和OpenCart扫描和破坏网站。

**攻击链**

![picture1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221215/1671068353157428.png "1671068353157428.png")

GoTrim攻击链

GoTrim使用木马网络对其目标执行传播式攻击攻击。每个木马都会获得一组凭据，用来尝试登录一长串的网站目标。成功登录后，木马客户端将被安装到新感染的系统中。然后，它等待来自攻击者的进一步命令，从而扩展木马网络。

GoTrim仅在攻击尝试成功后向C2服务器报告凭据。我们没有在GoTrim中观察到任何用于传播自身或部署其他恶意软件的代码。然而，我们确实找到了下载和执行GoTrim bot客户端的PHP脚本。攻击者似乎在某种程度上滥用泄露的凭据来部署PHP脚本以感染GoTrim系统。

![picture2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221215/1671068364178149.png "1671068364178149.png")

PHP下载脚本

通常，每个脚本都将GoTrim恶意软件从硬编码的URL下载到与脚本本身相同的目录中的文件并执行它。为了掩盖其踪迹，下载器脚本和GoTrim攻击程序都从受感染的系统中删除。它不会在受感染的系统中保持持久性。

**静态分析**

除非另有说明，本文中详细的分析是基于具有SHA-256哈希c33e50c3be111c1401037cb42a0596a123347d5700cee8c42b2bd30cdf6b3be3的示例。

GoTrim是用Go 1.18版本构建的。与所有Go应用程序一样，代码中使用的所有第三方库都静态链接到恶意软件，导致可执行二进制文件相对较大。但是这样做的好处是不依赖任何外部文件来正确执行。为了解决大小问题，恶意软件使用UPX打包，将文件从6 MB减少到1.9 MB。

使用Go的另一个优点是，相同的源代码可以交叉编译，以支持不同的体系结构和操作系统。根据示例中的源代码路径，在开发GoTrim时使用了Windows。但是，我们只观察到针对64位Linux的示例。

**C2通信**

GoTrim可以通过两种方式与命令和控制（C2）服务器通信：客户端模式，它向命令和控制服务器（C2服务器）发送HTTP POST请求，或服务器模式，它启动HTTP服务器以侦听传入的POST请求。与C2交换的所有数据都使用Galois计数器模式下的高级加密标准（AES-GCM）进行加密，密钥来自嵌入恶意软件二进制文件中的口令。

默认情况下，如果受感染的恶意软件直接连接到internet(即受害者的出站或本地IP地址是非私有的)，GoTrim将尝试在服务器模式下运行。否则，将切换到客户端模式。

执行后，GoTrim创建一个MD5哈希，表示受感染设备的唯一标识(木马ID)。它由以下字符串生成，包含由“：”字符分隔的几条信息：

VICTIM\_EXTERNAL\_IP:HTTP\_SERVER\_PORT:1:OUTBOUND\_IP:AES\_PASSPHRASE

VICTIM\_EXTERNAL\_IP：设备的外部/公共IP；

HTTP\_SERVER\_PORT：HTTP服务器端口。这是在服务器模式下为HTTP服务器随机生成的介于4000到8000之间的数字。对于客户端模式，始终为0；

恶意软件初始化标志：在计算木马 ID时始终设置为1；

OUTBOUND\_IP：目标设备的出站/本地IP地址；

AES\_PASSPHRASE：嵌入每个样本的硬编码字符串。该恶意软件后来使用该字符串的SHA256哈希作为AES-GCM密钥，用于加密其与C2服务器的通信。我们观察到的所有样本都共享相同的AES密码。

在生成bot ID之后，GoTrim创建一个异步Go例程(类似于多线程)，该例程在客户端和服务器模式下向C2服务器发送信标请求。

C2请求URL在不同版本之间发生变化，如本文稍后部分所述。对于此特定示例，信标请求URL为“/selects？dram=1”。

在这个信标请求中，一些受害者和木马信息被发送到C2服务器，如下图所示。

![picture3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221215/1671068376705301.png "1671068376705301.png")

发送到C2服务器的数据截图

信标请求中发送的一些有趣的字段包括：

1. Bot ID：木马的唯一ID；

2.外部IP：受害设备的公共IP地址；

3.HTTP服务器端口：为HTTP服务器随机生成的端口（客户端模式为0）；

4.恶意软件初始化标志：发出此请求时始终设置为1；

5.出站IP：受害目标设备的本地IP地址；

6.状态消息：“GOOD”消息被其他字符串替换，这些字符串在后续信标请求期间报告任何正在运行的CMS检测或强制执行任务的状态；

7.状态标志：这些标志指示恶意软件当前是否有C2服务器分配的任何处理任务以及这些任务的ID；

8.MD5校验和：该值由上述请求的部分和硬编码的AES密码生成，它用作消息完整性校验和。

这些字段通过：：：trim：：：字符串连接在一起，因此为这个活动选择了这个名称。然后使用AES-256-GCM密钥加密数据，这是前面提到的密码的SHA-256哈希。

服务器通常以“OK”、“404 page not found”或“BC”响应，所有这些都使用相同的AES-GCM密钥加密。当收到“BC”时，GoTrim将重新生成其bot ID并从服务器模式切换到客户端模式。

第一个信标请求是向木马网络注册一个新的木马。

每次信标请求后，GoTrim会休眠几秒到几分钟，这取决于C2服务器的响应，以及恶意软件在发送下一个请求之前是否正在处理C2分配的任务。恶意软件定期执行此信标请求，以更新C2服务器有关木马状态的信息，包括成功的凭据，如本文的攻击攻击部分所述。如果GoTrim在100次重试后未能从C2服务器接收到有效响应，它将自行终止。

当信标请求被异步发送以更新C2服务器的状态时，GoTrim要么向C2服务器发送请求以接收命令（客户端模式），要么设置HTTP服务器以侦听传入的任务请求（服务器模式）。

**客户端模式**

在客户端模式下，恶意软件发送一个POST请求到“/selects?”bilert=1 "接收来自C2服务器的命令。

C2服务器响应使用相同AES-GCM密钥加密的命令。在下图中可以看到一个解密命令的示例。

![picture4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221215/1671068388126461.png "1671068388126461.png")

包含命令及其选项的响应截图

通过“：：：trim：：：”字符串分割数据后，可以识别7个字段，如下所示。

1. MD5校验和：用于校验消息的完整性。如：83217f8b39dccc2f9f2a0157f0236c4f；

2. 命令ID：表示当前任务的命令；

3.并发级别：这会影响每个任务执行的goroutine的数量；

4. 命令选项：包含命令的选项，以7E 6A 71 6D 70 C2 A9 (~jqmp©)字节分隔。根据命令的不同，它们的解释也不同：

a.目标列表：这是GZIP压缩数据，解压缩后，包含将作为登录尝试目标的域列表。

b.命令选项1（已修订）：此选项包含身份验证命令的用户名。C2服务器可以指定一系列字节（如C2 A9 64）来使用域作为用户名，而不是为每个域使用相同的用户名。

c.命令选项2(修改后)：对于认证命令，该选项包含密码；

d.命令选项3：WordPress认证的未知选项；

e.命令选项4：WordPress身份验证选项，在提交凭据时使用POST请求或XML-RPC。

5. 内部值：恶意软件本身不使用的数值(例如，42和255)，可能代表当前命令的内部任务ID。

恶意软件支持以下命令：

1：验证WordPress域提供的凭据；

2：验证对Joomla!域提供的凭据(目前尚未实现)；

3：根据OpenCart域验证所提供的凭据；

4：根据Data Life Engine域验证所提供的凭据(目前尚未实现)；

10：检测在域中安装WordPress, Joomla!, OpenCar或Data Life Engine CMS；

11：终止恶意软件；

我们观察到一个目标列表在一个WordPress认证命令中包含多达30000个域。此外，我们观察到，身份验证命令只提供一个密码来测试列表中的所有域。如上所述，攻击可能是通过命令受感染设备网络测试不同的域和凭据来传播的。

恶意软件完成处理命令后，在发送另一个POST请求以接收来自C2服务器的新任务之前，它会休眠一段时间。

**服务器模式**

在服务器模式下，GoTrim在4000到7999之间的随机端口上启动服务器，以响应攻击者发送的传入POST请求。这种模式为攻击者提供了一种与木马通信的更灵敏的方式。例如，攻击者可以检查木马的状态，而无需等待后续的信标请求，只需向木马的HTTP服务器处理的特定URL发送POST请求。

为了向目标设备发出命令，攻击者向“/BOT\_ID?”ert=1 "发送POST请求，正文包含AES-256-GCM加密的命令数据，类似于C2服务器在客户端请求命令时的响应。服务器模式支持与客户端模式相同的命令。

攻击者还可以发送带有参数“/BOT\_ID？intval=1”的请求，以查看当前正在运行的任务的状态以及分配的任务是否已完成。

当CPU利用率低于某个水平(75%或90%，取决于当前任务使用的并发工作者的数量)时，将生成一个单独的goroutine来处理每个域。

**僵尸网络命令**

**检测CMS**

GoTrim试图确定目标网站上是否使用了四个CMS（WordPress、Joomla！、OpenCart或DataLife Engine）中的一个。它通过检查网页内容中的特定字符串来实现这一点。

有趣的是，它只通过检查“WordPress.com”的Referer HTTP标头来针对自托管的WordPress网站。由于托管的WordPress主机提供商，例如wordpress.com，通常会实施更多的安全措施来监控、检测和阻止攻击尝试。

用于确定已安装CMS的字符串如下所示：

![微信截图_20221215094401.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221215/1671068654313125.png "1671068654313125.png")

虽然GoTrim可以使用上述四种cms检测网站，但它目前只支持针对WordPress和OpenCart网站的身份验证。这表明该僵尸网络仍在开发中。

**验证WordPress凭据**

除了C2服务器提供的用户名之外，它还试图通过向“/wp-json/wp/v2/users”发送GET请求来收集更多的用户名。

之后，它尝试使用C2命令中提供的用户名列表和密码登录WordPress网站，通过发送POST请求到“/wp-login.php”。下图显示了登录的POST请求示例。

![picture5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221215/1671068403136887.png "1671068403136887.png")

WordPress身份验证请求

这个请求导致在成功登录后重定向到WordPress网站的管理页面(即/wp-admin)。为了确认登录和重定向成功，它检查响应是否包含“id=\”adminmenumain\”。

C2服务器还可以通过WordPress XML- rpc特性指定要执行的身份验证，这是用户使用XML以编程方式与CMS远程交互的另一种方式。通过直接与web服务器的后端通信，可以绕过通常在访问网站页面时有效的反木马机制（如captchas）。

成功登录后，以下信息(以“|”分隔)将被更新为全局状态消息，并与以下请求一起发送到C2(客户端模式)或作为传入请求的响应(服务器模式)：

目标URL；

用户名；

密码；

命令ID(1用于WordPress, 3用于OpenCart等)；

攻击状态(“0GOOD”表示成功)；

**验证OpenCart凭据**

GoTrim还可以强力破解运行开源电子商务平台OpenCart的网站。

它向目标的“/admin/index.php”发送一个GET请求，并收集登录请求所需的与身份验证相关的令牌和标头。然后，它通过向相同的URL发送POST请求以及包含用户名和密码的表单编码数据来执行实际的身份验证。

为了验证登录请求是否成功，它会通过搜索“/dashboard&user\_token=”来检查网站是否返回了OpenCart用户令牌，并确保接收到的数据中的“redirect”值不为空。

一个有效的身份验证响应应该如下所示：

```
{"redirect":"https://example.com/opencart/admin/index.php?route=common/dashboard&user_token=USER_TOKEN_HASH"}
```

成功登录后，全局状态消息将更新为针对WordPress的攻击状态。

**反木马检查**

GoTrim可以检测到网络托管提供商和CDN(如Cloudflare和SiteGround)使用的反木马技术，并规避一些更简单的检查。

它试图通过使用浏览器发送的相同HTTP标头并支持相同的内容编码算法(gzip、deflate和Brotli)来模拟来自64位Windows上Mozilla Fire...