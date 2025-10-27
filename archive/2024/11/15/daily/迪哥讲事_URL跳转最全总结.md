---
title: URL跳转最全总结
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496342&idx=1&sn=dde08fd0ba84961143d4c6cdfa36af66&chksm=e8a5f8f5dfd271e3bc7eb86630737c80c35406741d1036450f225196e6d8e964999bae4bd229&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-11-15
fetch_date: 2025-10-06T19:21:57.447879
---

# URL跳转最全总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L6MCxPWAoPlAOgOlgHPDBTska177N5aYYgv9UCLdWjiahXp96ia572bAAYzNAvejlwY79Bd9uVPkHhz6kSpFBWmw/0?wx_fmt=jpeg)

# URL跳转最全总结

迪哥讲事

以下文章来源于呼啦啦安全
，作者hulala14

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM4oAWT053vepz0zA6SJjJj1pgicxskIpqK4MHaiaFkl0raw/0)

**呼啦啦安全**
.

分享下个人安全经验

# URL跳转最全总结

> 在互联网的迷宫中，**URL跳转漏洞**是一道隐藏的暗门，它诱导不知情的网民步入风险的深渊。体积越是庞大的企业,只会越加重视**url跳转漏洞**

## 引言

**URL跳转漏洞**是一种常见的安全漏洞，许多网站在接收到用户提交的URL并进行跳转时，未对URL进行充分验证，导致攻击者可以通过构造特殊的URL绕过验证并进行跳转。攻击者利用这一漏洞可以进行钓鱼攻击、恶意重定向等恶意行为，从而对用户的隐私和安全造成威胁。

![](https://mmbiz.qpic.cn/mmbiz_png/L6MCxPWAoPlAOgOlgHPDBTska177N5aYLA4n0BAbx0My9W0m747GtfsuGkibMFSGgKSzOOiashaPnA1HjwibQMiaTg/640?wx_fmt=png&from=appmsg "null")

20231212233202

## URL跳转漏洞的威胁与原理

URL跳转漏洞的存在给用户和网站带来了许多威胁。攻击者可以通过URL跳转漏洞进行包括并且不限于以下恶意行为：

* • 钓鱼攻击：攻击者可以将用户重定向到一个伪造的网站，模仿合法网站的外观，诱使用户输入敏感信息，如用户名、密码、信用卡信息等。
* • 恶意重定向：攻击者可以将用户重定向到一个包含恶意代码的网站，进而感染用户设备或盗取用户信息。
* • 传播恶意软件：攻击者可以将用户重定向到一个携带恶意软件的网站，通过下载和安装恶意软件来攻击用户设备和系统。

URL跳转漏洞的原理在于网站在进行URL跳转时，未对URL进行有效的验证和过滤，使得攻击者可以构造恶意URL来绕过验证，从而实现恶意跳转。

## URL跳转漏洞的攻击及绕过

### 1.基本手法

直接修改URL参数：攻击者可以直接修改URL中的跳转参数，将其修改为恶意网站的URL。

https://vulinbox.yaklang.io:8787/ssrf-in-get?url=http://www.baidu.com/

![](https://mmbiz.qpic.cn/mmbiz_png/L6MCxPWAoPlAOgOlgHPDBTska177N5aYWfCtg0MDfYolqepfamoZibyAACzNURdZO7tqf9ILF1YAQ9wYnVa8wTw/640?wx_fmt=png&from=appmsg "null")

20231215172012

我们可以看到上面的链接中url参数控制着访问的地址,如果本来是一个正常的地址,但是我们通过修改url参数的值将其修改为百度地址,也能成功访问

### 2.防御绕过方法

#### 2.1 进制绕过

进制绕过:攻击者可以将恶意网址进行十进制，然后将编码后的字符串作为跳转参数

![](https://mmbiz.qpic.cn/mmbiz_png/L6MCxPWAoPlAOgOlgHPDBTska177N5aYdg0l5XVqNcgdIgf6jFzbexyokAaKBZggoQGOGnzz6ic9VkDUI8kB5qw/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/mmbiz_png/L6MCxPWAoPlAOgOlgHPDBTska177N5aYnYiaIib2pVXdBqvqicve0iaSibiad1vyiaKwuKUIjXSpvdicia8Dx3tv9jfQCjg/640?wx_fmt=png&from=appmsg "null")

我们对http://3232235777进行访问,可以看到,浏览器自动转换编码成了http://192.168.0.1

原理:

在URL中，当指定的协议为http://时，浏览器会尝试解析后续的内容作为域名或IP地址。在这种情况下，3232235777被解析为一个IP地址。这个特定的数字是一个十进制形式的IP地址，而我们平时见到的IP地址是点分十进制表示的。

点分十进制IP地址是由四个八位字节组成的，每个字节的取值范围是0到255，用.来分隔。例如，192.168.0.1实际上代表的是四个字节的集合,要将点分十进制转换为十进制，可以使用以下方法：

(第一个八位字节的值 \* 256^3) + (第二个八位字节的值 \* 256^2) + (第三个八位字节的值 \* 256) + 第四个八位字节的值

对于192.168.0.1，转换过程如下：

(192 \* 256^3) + (168 \* 256^2) + (0 \* 256) + (1) = 3232235777

因此，当你输入http://3232235777时，浏览器或操作系统将这个十进制的数解析为一个点分十进制的IP地址，也就是http://192.168.0.1。这是为什么输入一个十进制数值可以被解析并跳转到相应的IP地址。

#### 2.2 利用特殊编码字符绕过

利用特殊编码字符绕过:攻击者可以利用特殊编码字符绕过URL跳转验证(比如:'@','?','#','/','')

![](https://mmbiz.qpic.cn/mmbiz_png/L6MCxPWAoPlAOgOlgHPDBTska177N5aY2Nj9TXphwzUBqMHeAkWoBM3UrxMJGUFcknNLMJ8ec1bibPOeD4F6PcA/640?wx_fmt=png&from=appmsg "null")

20231215180113

我们访问https://vulinbox.yaklang.io:8787/ssrf-in-get?url=http://www.baidu.com@evil.com/链接,发现最后却跳转到了evil.com的地址

'@'符号原理:

输入的 URL http://www.baidu.com@evil.com/ 中包含了一个 '@' 符号，这个符号在 URI（Uniform Resource Identifier）中通常用于指示认证信息的开始，紧随其后的是用于认证的用户名，有时还可能包括密码。然而，在这种情况下，它被用来进行一种简单的欺骗。

在这里，www.baidu.com被视为用户名，而 evil.com 被解析为实际要访问的主机名。这种格式可以让浏览器误以为用户尝试在 evil.com 网站上进行用户 www.baidu.com 的身份验证。但由于在大多数情况下，HTTP 认证不会使用 URL 中的用户名来进行处理，于是浏览器会忽略 @ 符号之前的所有内容，并将网络请求直接发送到 evil.com。

这个技巧常被钓鱼攻击用来混淆目标网站的真实域名。用户在快速浏览或不仔细查看的情况下可能会认为他们正在访问 www.baidu.com，但实际上他们的浏览器被重定向到了 evil.com。这就是为什么输入那个 URL 会导致浏览器跳转到 evil.com 的原因。

![](https://mmbiz.qpic.cn/mmbiz_png/L6MCxPWAoPlAOgOlgHPDBTska177N5aYERmrVZ1DZLy5nqOibLfIf3zLoXtnibjLtlF8c2k4eceLu0iakAmRXCwiaA/640?wx_fmt=png&from=appmsg "null")

20231215180534

我们访问https://vulinbox.yaklang.io:8787/ssrf-in-get?url=http://www.evil.com?.baidu.com,发现最后跳转到了evil.com的地址

'?'符号原理:

URL的一般结构是这样的：protocol://domain/path?query\_string#fragment\_id

* • protocol 是通信协议，比如 http 或 https。
* • domain 是域名，指向您想要访问的服务器的地址。
* • path 指定服务器上的特定资源。
* • query\_string（以问号 '?' 开始）通常用于提供额外的参数给服务器。
* • fragment\_id（以井号 '#' 开始）用于指向网页内部的某个部分。

URL http://www.evil.com?.baidu.com 中，www.evil.com是实际的域名。问号 '?' 后面的内容被视为查询字符串，对于服务器来说，它是可选的，并且在这种情况下，不会改变正在请求的服务器的域名。务器会忽略问号后面的内容，除非服务器的代码特别编写以处理这些参数。

#### 2.3 嵌套跳转

嵌套跳转:利用网站的多重跳转机制，间接到达目的地址。

![](https://mmbiz.qpic.cn/mmbiz_png/L6MCxPWAoPlAOgOlgHPDBTska177N5aYOicdESVdepX8z5dYvS9QSG5QawIIXz1QyKbg4UzVD4waNwZpEefBYtA/640?wx_fmt=png&from=appmsg "null")

20231215181159

我们访问https://vulinbox.yaklang.io:8787/ssrf-in-get?url=https://vulinbox.yaklang.io:8787/ssrf-in-get?url=http://www.evil.com,发现最后跳转到了evil.com的地址

原理:在有些代码防御中规定了你能跳转的网站白名单,如果白名单中有网站能够进行url跳转,那么就能进行嵌套跳转

#### 2.4 使用特定子域名绕过

使用特定子域名绕过：通过构造看似合法的子域名来欺骗验证系统。

![](https://mmbiz.qpic.cn/mmbiz_png/L6MCxPWAoPlAOgOlgHPDBTska177N5aYzDDhib0yYa3XQ6QKcKCrcz7z6qvmbtiaOFBAd28fljI1XX0MFA9Xo1Ag/640?wx_fmt=png&from=appmsg "null")

20231215181446

我们访问https://vulinbox.yaklang.io:8787/ssrf-in-get?url=http://www.baidu.com.evil.com,发现最后跳转到了evil.com的地址

原理:

在这个 URL http://www.baidu.com.evil.com 中，evil.com 是实际的顶级域名，而 www.baidu.com是作为 evil.com 域下的一个子域来处理的。因为域名解析是从右向左进行的，所以 evil.com 被认为是最终的顶级域。

详细的分解：

* • .com 是顶级域（TLD）。
* • evil 是二级域名，它直接注册在 .com 顶级域之下。
* • com.evil 是在 .com 顶级域下，evil 这个注册域名下的子域。
* • baidu 和 www 是更深层次的子域名，都是 com.evil 这个子域下的进一步细分。

当你访问这个 URL 时，浏览器会寻找 evil.com 域下的 www.baidu.com子域。如果 evil.com 的拥有者已经设置了这个子域，并且这个子域指向一个有效的服务器，那么浏览器便会显示由该服务器提供的内容。

正因为这种方式，这个 URL 实际上会指向一个属于 evil.com 的页面，而不是 baidu.com。这也是一种网络钓鱼攻击者常用的技巧，使用看似合法的域名来欺骗用户，因为用户可能会忽略 URL 的最后部分，错误地认为他们访问的是他们信任的域名。

#### 2.5 绕过对于点号（.）的检测

绕过对于点号（.）的检测：使用URL编码来隐藏点号，绕过安全措施。

![](https://mmbiz.qpic.cn/mmbiz_png/L6MCxPWAoPlZPViaFb0MZo05Z3JLHoxMgUNdKEwGTJic9MD25fBiadwbxicjsw0CdYdWPkvUu9QQiaogvAJcaKMNvVQ/640?wx_fmt=png&from=appmsg)

20231215182600

这是一个正常的跳转功能

但是我们修改loginUrl参数的地址为dnslog的地址https://sevtex.dnslog.cn,发送数据包,发现跳转失败

![](https://mmbiz.qpic.cn/mmbiz_png/L6MCxPWAoPlZPViaFb0MZo05Z3JLHoxMgtWcxu5fafsUqDMaajEkSaD2VfMtrnhgCYuoUKQ6O2tC6icQEgmSPLBw/640?wx_fmt=png&from=appmsg)

20231215182729

我们对跳转地址进行绕过,绕过对于白名单和.符号的限制加上%E3%80%82%40,将地址修改为

https://sevtex.dnslog.cn%E3%80%82%40.xxx.com

发现进行了跳转,查看dnslog的记录,已经访问成功

![](https://mmbiz.qpic.cn/mmbiz_png/L6MCxPWAoPlZPViaFb0MZo05Z3JLHoxMgpf9fxSukY5Uuodcmo1icCwqbS2tkVyMVsevcYTujgwEta75GZSeCDIQ/640?wx_fmt=png&from=appmsg)

20231215183304

## 防御URL跳转漏洞的方法

为防止URL跳转攻击，以下方法应被考虑实施：

* • 对所有跳转的URL进行严格的输入验证和过滤，以确保跳转的目的地是安全的。
* • 实施白名单策略，仅允许向预定义的可信网站进行跳转。
* • 对URL参数进行安全编码，确保验证机制不被简单绕过。

## 结论

URL跳转漏洞是一种不容忽视的网络安全风险。攻击者可以通过多种方法利用该漏洞进行恶意跳转。因此，开发者和网站管理员必须采取切实可行的安全措施，以确保网站和用户的安全不受到这类漏洞的威胁。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effde...