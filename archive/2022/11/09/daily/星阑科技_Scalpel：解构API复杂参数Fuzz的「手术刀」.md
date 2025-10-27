---
title: Scalpel：解构API复杂参数Fuzz的「手术刀」
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496361&idx=1&sn=bb87f87d991f05c9220965491f7e2047&chksm=c0075f35f770d6230e37330a3d6c7c2b3c26f9b2d26c431cddc2a50499f3a5b9883702466173&scene=58&subscene=0#rd
source: 星阑科技
date: 2022-11-09
fetch_date: 2025-10-03T22:06:23.849398
---

# Scalpel：解构API复杂参数Fuzz的「手术刀」

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3o9IibBAeVOl4IAfRP9SzJxfxBUBXaKvNyDibmPzTNwfWYmicnjmPGp5Qjg/0?wx_fmt=jpeg)

# Scalpel：解构API复杂参数Fuzz的「手术刀」

星阑科技

以下文章来源于星阑实验室
，作者PortalLab

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7I2gqBRVgAVpkPNqBsibrgE0DM5mTmZIRYzgFUNPjF59g/0)

**星阑实验室**
.

聚焦API安全最新资讯，分享API安全研究成果

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOeiaFHTFtiatmEIxZQcXOHfyr6GOBM88IeMm28ybjSAHEJKicuQxPxN5L5NFZ5mza2NOnuokf9ant2fUQ/640?wx_fmt=gif)

**Scalpel 简介**

Scalpel是一款自动化Web/API漏洞Fuzz引擎，该工具采用被动扫描的方式，通过流量中解析Web/API参数结构，对参数编码进行自动识别与解码，并基于树结构灵活控制注入位点，让漏洞Fuzz向量能够应对复杂的编码与数据结构，实现深度漏洞挖掘。

* 详细技术原理可参考KCon 2022议题：[《自动化API漏洞Fuzz实战》](http://mp.weixin.qq.com/s?__biz=Mzg3NDcwMDk3OA==&mid=2247484068&idx=1&sn=89ea1b1be48a0cb7f93a4750765719d1&chksm=cecd8b79f9ba026f7fbf52771e41272d684fc3af5175587f768082f8dbaee12d6d33bb892ceb&scene=21#wechat_redirect)
* 目前我们的Fuzz引擎端已打包为一个小工具，内置100+漏洞POC，供大家试用：

  https://github.com/StarCrossPortal/scalpel

**深度参数注入原理**

随着Web应用复杂度的提升与API接口的广泛使用，在HTTP应用漏洞Fuzz过程中，**传统的「Form表单明文传参的模式」已经逐渐变为「复杂、嵌套编码的参数传递」。**在此情况下，直接对参数内容进行注入或替换，无法深入底层的漏洞触发点。

漏洞Fuzz过程中需要对这些「结构体、编码」进行抽离，找到真正的注入点位，方可进行自动化漏洞测试。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3okBmrhxW4YnlKqWviazicNJGibFKXQzEb7DHCaF0ViafK0WumjCAXSzicKBg/640?wx_fmt=png)

**Scalpel拥有一个强大的数据解析和变异算法，它可以将常见的数据格式（json, xml, form等）解析为树结构，然后根据poc中的规则，对树进行变异，包括对叶子节点和树结构的变异。变异完成之后，将树结构还原为原始的数据格式。**

Scalpel主体结构分为被动代理、Fuzz向量生成与验证、结果输出三个阶段：

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oOUh8A30TrVAqa7TkSu6L1Wmk8DiaibZOTNAnibsHoyTLGicjIBMBKVvQFA/640?wx_fmt=png)

漏洞检测部分，采用解析算法，深度解析流量请求中的参数，通过POC中设定的注入点和变异方式生成测试请求，发送请求之后，再通过POC中的验证规则进行成功性判断，最终输出Fuzz结果。

以下面这个JSON请求包为例，解析算法会将其转换为右边所示的树结构，无论其嵌套的层次有多深，解析算法会将其中的所有键值对都解析为一个树结构。然后可以对树中的叶子节点进行变异，也可以对树的整体结构上进行变异。在树上进行变异之后，将树按照原始的数据格式再还原回去，填充到请求报文中，形成变异的请求报文之后再发送出去。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oP73skviaIYhHSibNCb1LuZHjicg4H7BsYu5xkoQaicqNmVQ2lOQSsxa38A/640?wx_fmt=png)

在原始参数结构解析之后，我们可以基于树结构来设定我们的测试向量注入方式：

对节点的变异方式有：

1. 按数据类型注入payload

2. 注入通用型payload

3. 畸形数据替换

4. 类型转换

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3obibECLBAv4EeK8Pq4ibzf7etZJo0iczE9ib5wv6Vcy8QVuapRcibNP83IiaA/640?wx_fmt=png)

对树结构的变异方式有：

1. 替换object类型结构

2. 插入节点

3. 删除节点

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oEIUTo7XWad3a5CJia8MP7G4X03laKqVtVMpQkG1DBibrcSibHpGcYcuCA/640?wx_fmt=png)

**Scapel 功能介绍**

Scalpel扫描器支持以下漏洞检测或者挖掘场景：

1、检测目标已知安全的漏洞，包括CVE漏洞，热门框架、组件、中间件安全漏洞。

2、通用安全漏洞，包括但不限于SQL注入、XSS漏洞、文件上传、命令执行、文件读取等。

3、未知0day漏洞或者安全问题

同时支持多个参数位置的变异，包括：path、query、header、body等部分，具体可以参考Scalpel

漏洞POC编写指南（https://github.com/StarCrossPortal/scalpel/wiki/POC%E7%BC%96%E5%86%99%E6%8C%87%E5%8D%97）

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oRYEJdnp0gyCoBvTbLgWicrAquiarXUmhy6o3o4YALsib4tBzLzQKsDpoA/640?wx_fmt=png)

**案例1：CVE-2022-1388F5 BIG-IP** **API** **Unauthenticated RCE漏洞的检测**

简单了解下漏洞，具体可以参考之前[分析文章](https://mp.weixin.qq.com/s?__biz=Mzg3NDcwMDk3OA==&mid=2247483735&idx=1&sn=0b6ffbf45338fdac74d644bd4895c2c7&scene=21#wechat_redirect)（[【技术干货】F5 BIG-IP API Unauthenticated RCE(CVE-2022-1388)分析](http://mp.weixin.qq.com/s?__biz=Mzg3NDcwMDk3OA==&mid=2247483735&idx=1&sn=0b6ffbf45338fdac74d644bd4895c2c7&chksm=cecd888af9ba019ce1bd8c218d821874e275aa77287966087ad045c99b8ff27419b92836db2b&scene=21#wechat_redirect)），我们要实现RCE，需要构造如下特殊的请求：

1、访问路径为/mgmt/tm/util/bash

2、Host为localhost或者127.0.0.1时，绕过验证赋予用户身份

3、Connection头加上X-F5-Auth-Token

4、body部分添加json形式的执行命令

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oZibu68ibWE5LaKDFYlS74VYraw8tgHHLVKeU2dicooBULwlo7sFyeUWCA/640?wx_fmt=png)

为了检测到CVE-2022-1388漏洞是否存在，我们需要在发送构造的特殊请求后，识别响应中是否进行了命令执行。了解到整个检测的步骤后，开始编写漏洞POC

一一对应，在URL部分变异，变异方式为替换，变异值为/mgmt/tm/util/bash

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oicePVtaiaJGVwXOqg0qHdX00XIN23LWJc4qNAZmMZeTCKCL1PEibibZFzg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oJ75qGkyM2hyxUiarlvp0gczibhECWwgMRORZtQTpUH3XFRtajicsXWb5w/640?wx_fmt=png)

在Host部分变异，变异方式为替换，变异值为localhost

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3o8ViayfOjbD2ic2LQyI1S6LYdmGuZaPAAibVLGNqV8gCIuICPXfP5Iwlvw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oPQaKcicnhh6c96S4CsV9blHcVfJeWXuyTZgmV7wZfbMJ85umnIHMD2A/640?wx_fmt=png)

对Heder部分的变异，变异方式为替换，变异值为Keep-Alive,X-F5-Auth-Token

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oQpC1MhHlyFx2icTzPX9ice2XhZ2eYSuql2nLibAqH0jicdgsdOFThibr1ZQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oPTtXIukUBUoCwUSOicTxWlsN7icKrWahX5pbYbzjS37J3IXphrhpmZtw/640?wx_fmt=png)

对body部分的变异，变异方式为替换，变异值为我们需要执行的命令，这里执行id命令。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3ofvJiamcsWyyYrfNHTA7rZYOd8udiaZCd4dKX7hxIZCSIoJibE2BmLIkvg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oHyIH0LTkRTicj4v7MuOdon4D9q8ronDl0ojDTyNNm6yU4S6CXGOEhWg/640?wx_fmt=png)

最后对响应的匹配，使用正则识别id命令之后的结果。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oZrDYwTkGoVKNVSnYAj1KqG64lO2qvDGYu6qS9mqvsWr7WLxaAb0Jxg/640?wx_fmt=png)

在编辑好漏洞POC之后，运行扫描器进行检查。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oUEHVREbhaSx28HzQLThnpYyw9DoTD6Bicq1t3lrLNib6Dfk43pYbyA0g/640?wx_fmt=png)

在被动扫描的过程，实际获取到的数据包如下：

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oET0vnDIQ5HIcarD6lcTvHIydzpnJ9s2YC8H84eyFEGhxDibEemm3Wsg/640?wx_fmt=png)

如果存在漏洞，将会以html文件的形式记录存在漏洞的信息，查看此次扫描结果。

成功扫描出CVE-2022-1388F5 BIG-IP API Unauthenticated RCE漏洞，漏洞的请求也变异无误，最后的响应中也是执行了id命令。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oMbK5GDnPejRCunmQ6lshxKhgiaSpSmdpPRspQjlOomVBjI0IyFoSfiaQ/640?wx_fmt=png)

**案例二：利用Scalpel工具挖掘多个0day漏洞**

Scalpel工具使用较为灵活，通过对检测目标变异响应的check，可以发现检测目标中未知的安全问题。

例如为发现某些API接口是否存在账号密码的泄露，可以在check部分利用正则表达式匹配具体的泄露数据。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oytwNG4jKVojFIecKW31ZZlSOeTxv4bicRqFuxZrOBXPVibQy7S4ZMUVA/640?wx_fmt=png)

为发现目标是否存在文件读取漏洞，可以在多个变异位置插入或者替换payload

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3owZcnWpJJFdmwibS1rIfxic58Y6XEkdq48P7283GN1ibnlysn1D1uq5DDw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oOblwxgtTnS7VQIU108QROliaTp83up03Y87EDAjgx5MYuIaghvvekhg/640?wx_fmt=png)

为发现SQL注入漏洞，可以在query、Heder、body中的参数插入' and 1=1类似的payload

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oqz0icSA7vE1MIE0DAOYPyAB7d887VDKwamZia1e3hFVNSudXqSNwm3cA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oaYl9AGXJeaoCicq4FTaibH0owsjLxibiaJfKjn1EoeiauSzuj8hiaxemgpPg/640?wx_fmt=png)

星阑实验室成员利用如上的类似通用检测规则，挖掘多个0day漏洞，已提交给CNVD国家信息安全共享平台并被收录。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oFRbBzYTCC3W5YuLJeYPPlJffdibGKsRPftrWYLewBRutZJkxFp3tJyw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3o9eC1feSTiaqEy11xuQCkh6lQEjOJYlMnNAeOQPBaTf9bVBtLCQMsXyA/640?wx_fmt=png)

同时发现某Apache开源项目的CVE漏洞，报告被该团队接受并正在修复，尚未披露。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3ogia7VQE1J8jick0shYXaEyX7yDIc9GKxnvMnvcCTtxWFJufKg2pO4WiaA/640?wx_fmt=png)

**工具地址**

**GitHub地址下载地址：**https://github.com/StarCrossPortal/scalpel

目前已支持100+常见漏洞Fuzz向量与POC，持续维护中。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oeFaoWiblIZAIqrTiaDPBFkIunVWBsXfiaSrMUnibib6hSgrxRvnPibspdkQA/640?wx_fmt=png)

Scalpel支持多个平台，请根据您的平台或者需求下载相应的版本。

![](https://mmbiz.qpic.cn/mmbiz_png/wfFYMXc5G1NIptsJbgzwsk7KUrw8Yl3oAblMyKXQia1qgibJFrO5jCWMdR2fj8wz4NmznFibyaZZFP5RYzwic8lWibw/640?wx_fmt=png)

**关于Portal Lab**

星阑科技 Portal Lab 致力于前沿安全技术研究及能力工具化。主要研究方向为API 安全、应用安全、攻防对抗等领域。实验室成员研究成果曾发表于BlackHat、HITB、BlueHat、KCon、XCon等国内外知名安全会议，并多次发布开源安全工具。未来，Portal Lab将继续以开放创新的态度积极投入各类安全技术研究，持续为安全社区及企业级客户提供高质量技术输出。

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUK...