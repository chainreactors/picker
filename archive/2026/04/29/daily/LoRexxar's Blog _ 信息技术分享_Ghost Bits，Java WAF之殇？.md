---
title: Ghost Bits，Java WAF之殇？
url: https://lorexxar.cn/2026/04/29/java-ghost-bits/
source: LoRexxar's Blog | 信息技术分享
date: 2026-04-29
fetch_date: 2026-04-30T05:23:51.506948
---

# Ghost Bits，Java WAF之殇？



[LoRexxar's Blog | 信息技术分享](/)

[LoRexxar's Blog | 信息技术分享](/)

Ghost Bits，Java WAF之殇？



# Ghost Bits，Java WAF之殇？

java
ghostbits


2026/04/29




Share

* 
* 
* 
* 
* 

![](/assets/loading.svg)

在前两天的BlacksetHat Asia 2026上，@浅蓝和@1ue分享一个非常有趣的议题，Java中的GhostBits漏洞

* <https://i.blackhat.com/Asia-26/Presentations/Asia-26-Bai-Cast-Attack-Ghost-Bits-4.23.pdf>

探究深度非常深，影响范围非常之广，内容非常有意思

# 什么是Ghost Bits？

Ghost Bits这个概念的来源太久很难深究，甚至在软件领域之前就已经有类似的概念。**Ghost Bits主要是指那些在莫名其妙的位置影响到软件运行的位，所以形容像幽灵一样。**

在这个议题中，**Ghost Bits主要指的是在某些类型转换过程中被不小心丢掉的高位，导致原字符串内容变化。**

最经典的场景就是**char类型和byte类型的转换**，也是Java的经典场景。

**char类型是16位（2字节），byte类型是8位（1字节）**，如果发生char强制转换为byte就会丢弃高8位，**只保留低8位**。其中的8位就像幽灵一样消失了。

![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202604291810719.png)

在Java中，**有4种非常常见的写法**都会有该问题

* `(byte) ch`：显式的byte强制类型转化
* `ch & 0xFF`：位掩码，保留低8位
* `OutputStream.write(int)`：写入流时被截断
* `DataOutputStream.writeBytes()`：官方JDK方法，在文档中明确写明会丢弃高8位

![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202604291810211.png)

而在unicode中，会有大量的高位内容，经过处理和转换之后就会被截断变成对应的字符
![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202604291810631.png)

要注意的是，这个问题本质上**在源代码层面表现一致，不能单独算作是一个漏洞**，所以在80%的场景下，该问题主要影响的是**和源代码不在同一层的软件，其中最经典的就是waf**！
![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202604291810119.png)

# 具体怎么回事？

基础的原理刚才都理解了，其实就是利用高位无效的机制问题，使得**输入的内容在waf和实际源代码处理的时候遇到的是不同的内容**。

比如说中文字阮，经过处理之后源代码获得的就是.

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` 字符 '阮' = U+962E = 0x962E (byte) 0x962E = 0x2E = '.' ``` |

那你就可以用这种方式绕过WAF的限制

比如说我输入`\u丰丰耳失`，**waf收到这个输入的时候认为没有任何敏感词**，则放行到后端jackson，后端将其转为byte，最终拼接成sql注入语句

![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202604291810219.png)

最神奇的是，这种逻辑的泛用性极强，首先本身高位被抛弃意味着高位可以塞入任意值，那么对于poc就是多对1的转化关系。

以下两种都可以直接转为对应的`../../`，这对于waf来讲就是极强的考验，即便只针对byte的转化关系，waf也非常难处理

![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202604291810259.png)
![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202604291810235.png)

# 继续拓展？

刚才提到了，在java本身的代码中，char类型和byte类型的转化是非常常用的写法，其带来的问题往往并不能直白的影响到源代码层面，**但对于安全来讲，似乎小概率事件会导致大概率问题**？！

# CVE-2025-41242 Spring框架因Jetty URI解析不一致导致的路径穿越漏洞

刚才我们讨论的是泛用性非常强的waf场景，那么**在Spring框架下**，本身会有一个非常大的问题，就是Spring框架中`StringUtils.uriDecode`和Jetty`URIUtil.encodePathSafeEncoding`的处理方式不一致，导致了底层的路径穿越问题。

* <https://github.com/advisories/GHSA-r936-gwx5-v52f>
* <https://github.com/spring-projects/spring-framework/commit/24e66b63>

对于Spring框架的`StringUtils.uriDecode`方法

![](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202604291810384.png)

遇到%时会做专门的处理，并调用`ByteArrayOutputStream.write`导致了高位bit丢失，出现Ghost Bits漏洞。

`阮严灵丰丰甲来`会被转为`.%u002e`

这个输入在Spring层面，不但可以通过`isInvalidPath/isInvalidEncodedPath`的路径检查，还不会被识别为正常的%u编码，全部放行

传递到Jetty中，`URIUtil.encodePathSafeEncoding`却会将`%u002e`做unicode解码转为`.`，最终构造成为`../`
![image-20260429181104521](https://lorexxar-blog.oss-cn-shanghai.aliyuncs.com/blog/202604291811773.png)

## Openfire CVE-2023-32315 — 认证绕过

转为Byte丢失高位的方案大家都知道，还有一些更邪门的其他漏洞，其实本质上也是类似的问题。

一个很有趣的例子就是**Openfire CVE-2023-32315**，这个漏洞本质上是一个基础的路径穿越漏洞

* CVE-2008-6508，最早的漏洞只需要..就可以实现路径穿越
* CVE-2023-32315，发现可以用%u002e，也就是UTF-16来替代%2e实现路径穿越，因为AuthCheckFilter并没有校验对应的输入，但Jetty支持%u解码，导致了漏洞的绕过

poc就是这样的

|  |  |
| --- | --- |
| ``` 1 ``` | ``` /setup/setup-a/%u002e%u002e/%u002e%u002e/log.jsp ``` |

很多WAF都加入了%u002e%u002e作为关键字之一，那么你可以使用这个poc来绕过

|  |  |
| --- | --- |
| ``` 1 ``` | ``` /setup/setup-a/%2>%2>/%2>%2>/log.jsp ``` |

这里有个比较邪门的点在于，对于大部分框架来说，**他们不会把`%2>`当做url编码去处理，因为`>`并不是合法的url编码**。

但是对于Jetty来说，他会一视同仁，把`>`传入到`convertHexDigit`做处理

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` public static byte convertHexDigit(byte c) {     byte b = (byte)((c & 0x1f) + ((c >> 6) * 0x19) - 0x10);     if (b < 0 || b > 15)         throw new NumberFormatException("!hex " + c);     return b; } ``` |

也就是说即便是符号`>`依旧会经过这一套算法，最终获得结果是14，对应`E`

那么这样一来，**waf收到的请求是`%2>`不合法的url编码不做处理，jetty把他处理转为了`%2E`成功输入`.`绕过waf**。

# 写在最后

其实类似的场景同样非常多，因为许多大型框架中，除了显式的Java类型转化，还会有隐式的框架中的处理导致同样的问题，在原议题中分享了不同框架下涉及到不同漏洞的很多种问题，他们无一都是开发者无意中触发了Ghost bits问题，设计者并没有提前考虑好类型强制转化的额外影响。

正如演讲结尾所说：**“We have only scratched the surface”** — 这才刚刚开始。

原文作者：[LoRexxar](https://lorexxar.cn)

原文链接：<https://lorexxar.cn/2026/04/29/java-ghost-bits/>

发表日期：[April 29th 2026, 6:09:32 pm](https://lorexxar.cn/2026/04/29/java-ghost-bits/)

更新日期：[April 30th 2026, 9:50:44 am](https://lorexxar.cn/2026/04/29/java-ghost-bits/)

版权声明：本文采用[知识共享署名-非商业性使用 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc/4.0/)进行许可

* Previous Post

  [AI.Re.(3) - AI到底变了什么？为什么突然井喷？](/2026/04/07/reai3/ "AI.Re.(3) - AI到底变了什么？为什么突然井喷？")

Powered by [Hexo](https://hexo.io/)theme [Archer](https://github.com/fi3ework/hexo-theme-archer)

[京ICP备2021004652号-1](https://beian.miit.gov.cn/)

PV:  :)

CATALOG

1. [1. 什么是Ghost Bits？](#什么是Ghost-Bits？)
2. [2. 具体怎么回事？](#具体怎么回事？)
3. [3. 继续拓展？](#继续拓展？)
4. [4. CVE-2025-41242 Spring框架因Jetty URI解析不一致导致的路径穿越漏洞](#CVE-2025-41242-Spring框架因Jetty-URI解析不一致导致的路径穿越漏洞)
   1. [4.1. Openfire CVE-2023-32315 — 认证绕过](#Openfire-CVE-2023-32315-—-认证绕过)
5. [5. 写在最后](#写在最后)

* Archive
* Tag
* Cate

Total : 211

2026

* 04/29
  [Ghost Bits，Java WAF之殇？](/2026/04/29/java-ghost-bits/)
* 04/07
  [AI.Re.(3) - AI到底变了什么？为什么突然井喷？](/2026/04/07/reai3/)
* 03/11
  [AI.Re.(2) - OpenClaw到底为什么爆火？](/2026/03/11/reai2/)
* 03/10
  [AI.Re.(1) - AI变革的时代来了吗？](/2026/03/10/reai1/)

2025

* 12/31
  [不容错过的2025年度漏洞：React2Shell（CVE-2025-55182）分析](/2025/12/31/react2shell/)

2024

* 06/11
  [PHP CGI Windows平台远程代码执行漏洞（CVE-2024-4577）分析与复现](/2024/06/11/phpcgi-rce/)

2023

* 12/18
  [人与代码的桥梁-聊聊SAST](/2023/12/18/sast2024/)
* 11/21
  [Joern In RealWorld (3) - 致远OA A8 SSRF2RCE](/2023/11/21/joernrw3/)
* 10/26
  [Joern In RealWorld (2) - Jumpserver随机数种子泄露导致账户劫持漏洞（CVE-2023-42820）](/2023/10/26/joerninrw2/)
* 10/20
  [深入浅出Joern（四）不常用语法大全](/2023/10/20/joern4/)
* 08/31
  [Joern In RealWorld (1) - Acutators + CVE-2022-21724](/2023/08/31/joerninrw/)
* 08/24
  [深入浅出Joern（三）Joern和Neo4j常用语法大全](/2023/08/24/joern3/)
* 08/22
  [深入浅出Joern（二）CPG与图数据库](/2023/08/22/joern2/)
* 08/21
  [深入浅出Joern（一）Joern与CPG是什么？](/2023/08/21/joern-and-cpg/)
* 07/19
  [打造自己的AIGC应用（一）入门篇](/2023/07/19/aigc1/)
* 06/21
  [赛博偶像速成指南（三）- Midjourney](/2023/06/21/cybergirl3/)
* 06/02
  [赛博偶像速成指南（二）- SD进阶篇](/2023/06/02/cyber-girl2/)
* 05/25
  [从0到1的ChatGPT - 进阶篇（五）- Embeddings](/2023/05/25/chatgpt5/)
* 05/19
  [从0到1的ChatGPT - 进阶篇（四）- 训练自己的ChatGPT](/2023/05/19/chatgpt4/)
* 05/08
  [看上去不起眼的微信机器人以及公众号爬虫](/2023/05/08/wechat-robot/)
* 04/28
  [从0到1的ChatGPT - 进阶篇（三）- ChatGPT+？](/2023/04/28/chatgpt-3/)
* 04/26
  [从0到1的ChatGPT - 入门篇（二） - 如何与ChatGPT对话？](/2023/04/26/chatgpt2/)
* 04/14
  [从0到1的ChatGPT - 入门篇](/2023/04/14/chatgpt1/)
* 02/21
  [赛博偶像速成指南](/2023/02/21/cyber-girl/)

2022

* 11/02
  [CS Xss2Rce CVE-2022-39197分析与复现](/2022/11/02/cs-xss2rce/)
* 04/14
  [SCA的困境和出路](/2022/04/14/sca/)
* 03/21
  [人生的第二个可能~](/2022/03/21/vblog/)

2021

* 12/10
  [log4j2 JNDI注入漏洞速通~](/2021/12/10/log4j2-jndi/)
* 08/17
  [从0开始入门Chrome Ext安全（三） -- 你所未知的角落 - Chrome Ext安全](/2021/08/17/chrome-ext-4/)
* 08/17
  [DevSecOps 究竟需要怎样的白盒？](/2021/08/17/devsecops/)
* 08/06
  [区块链安全罪与罚 -- 浅谈区块链与安全发展史](/2021/08/06/blaockchain-dev/)
* 05/19
  [创宇四年](/2021/05/19/lifesuibi/)
* 04/16
  [反制Webdriver - 从Bot到RCE进发](/2021/04/16/chrome-webdriver-attack/)
* 03/09
  [通达OA代码审计篇二 - 11.8 后台Getshell](/2021/03/09/tongda11-8/)
* 03/03
  [通达OA代码审计篇 - 11.7 有条件的任意命令执行](/2021/03/03/tongda11-7rce/)
* 02/05
  [如何自动化挖掘php反序列化链 - phpunserializechain诞生记](/2021/02/05/kunlun-m-phpser/)
* 01/28
  [为被动扫描器量身打造一款爬虫-LSpider](/2021/01/28/lspider-design/)

2020

* 10/30
  [构造一个CodeDB来探索全新的白盒静态扫描方案](/2020/10/30/whitebox-2/)
* 09/21
  [从0开始聊聊自动化静态代码审计工具](/2020/09/21/whiteboxaudit/)
* 07/14
  [Geekpwn 2020云端挑战赛 Noxss & umsg](/2020/07/14/geekpwn2020-noxss/)
* 07/08
  [从反序列化到类型混淆漏洞 -- 记一次ecshop实例利用](/2020/07/08/ecshop-unser-1/)
* 06/10
  [Roundcube mail 3 Xss](/2020/06/10/roundcube-mail-xss/)
* 05/29
  [Roundcube mail代码审计笔记](/2020/05/29/roundcube-mail-1-4-4/)
* 05/11
  [空指针-Base on windows Writeup -- 最新版DZ3.4实战渗透](/2020/05/11/dz-3-4-windows/)
...