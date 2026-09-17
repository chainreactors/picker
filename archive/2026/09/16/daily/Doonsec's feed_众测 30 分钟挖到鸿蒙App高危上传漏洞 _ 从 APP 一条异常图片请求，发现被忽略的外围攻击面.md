---
title: 众测 30 分钟挖到鸿蒙App高危上传漏洞 | 从 APP 一条异常图片请求，发现被忽略的外围攻击面
url: https://mp.weixin.qq.com/s/g7C_-SkNwavzz5K3kODpsg
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:54:27.927613
---

# 众测 30 分钟挖到鸿蒙App高危上传漏洞 | 从 APP 一条异常图片请求，发现被忽略的外围攻击面

# 众测 30 分钟挖到鸿蒙App高危上传漏洞 | 从 APP 一条异常图片请求，发现被忽略的外围攻击面

w4nk3r
w4nk3r

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**0x01 简介**

本次众测 Web 主站防护严密，没有找到突破口，于是切换思路，借助 Yakit 代理抓取鸿蒙 APP 流量。在众多请求中发现一条异常图片请求，目标直接访问裸 IP。顺着该 IP 追踪，发现一台独立外围服务器，其上文件上传接口仅依靠后缀做校验，存在绕过漏洞。漏洞验证成功后，核查资产边界，但不属于众测授权核心资产范围，当即停止深入利用。文章复盘完整挖掘链路，探讨 APP 流量挖掘隐藏攻击面与渗透测试的资产边界问题。

本文内容仅用于网络安全技术学习与交流，所有操作均在授权测试环境下完成。严禁将文中技术用于未授权检测与非法攻击，违者责任自负。

原文地址：https://xz.aliyun.com/news/92800

****0x02 正文详情****

这次众测一开始其实并不顺利。

按照正常的测试流程，我先从目标暴露在公网的 Web 资产入手，对主要业务系统进行了信息收集和常规漏洞探测。

但这一轮下来，几个主要 Web 应用的防护都比较完善，并没有发现特别有价值的突破口。

眼看着时间一点点过去，我开始考虑换一个方向。

**Web 面没有明显突破口，并不意味着目标没有问题，也可能只是当前看到的攻击面还不够完整。**

既然如此，不如换一个观察角度

于是，我把测试重点转向了目标的 APP

而这次真正让我找到突破口的，并不是什么复杂的漏洞利用，而是一条看起来非常普通的图片资源请求

**从 Web 面转向 APP**

在实际众测过程中，我比较习惯把目标理解成“一组业务资产”，而不是单独的一个域名。

一个目标除了主站 Web 应用之外，往往还可能存在：

* APP
* 小程序
* H5
* API
* 图片/文件服务
* 对象存储
* 后台管理系统
* 第三方业务系统
* 历史遗留服务

这些系统虽然表面上属于同一个业务体系，但背后的服务器、域名、开发团队，甚至安全策略，都可能完全不同。

因此，当 Web 主站没有明显突破口时，与其继续盯着同一个入口反复测试，不如换一个观察角度。

这也是我这次转向 APP 流量分析的原因。

**APP 流量分析**

这次测试使用的是华为鸿蒙手机。

由于设备无法 Root，我没有继续折腾模拟器，而是直接使用 Yakit 作为中间代理，通过手机 Wi-Fi 代理将 APP 的 HTTP/HTTPS 流量转发到测试机。

Yakit 监听地址设置为：

```
0.0.0.0
```

随后在手机 Wi-Fi 中配置对应的代理地址和端口。

配置完成后，打开 APP 并进行正常操作，就可以在 Yakit 的 MITM 模块中看到 APP 发出的请求。

代理抓包本身属于比较基础的操作，这里不再展开

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAU74q0IeUrNI38TWPFSO99rECDkicIInic5pukweYYpV7t3EElVhQHex5JX91J4zPhfxoFJZpKP9JXQPxv47zvGZn058bKiahrBAQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVKBfxxhwzjvI3aaSZsUgMsrWvVq6JFxrQuYtZXicGEL83pyDoWB29tMe71g8Sv0dXODiaS55VR0EsrqRu5PiadKeGPL5GcibkU0Ug/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

真正值得关注的，是大量正常请求中突然出现的一条异常请求

**一条“不太正常”的图片请求**

在浏览 APP 正常功能时，我看到了一批图片、接口等请求。

大部分请求都很普通，基本符合：

业务域名 → API → JSON / 图片 / 其他资源

但其中一个图片资源请求引起了我的注意。

**APP 在请求图片资源时，并没有使用业务域名，而是直接请求了一个裸 IP 地址**

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUErUGDsZeJjQz1gibfrhApM0qaM0G7cuibN5To8sJK4ib5jq9qWQgoMXN31fmLiaBOalEgv3uCU1S9GyLnJemwGYiaaKbib5Wzuun04/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

当时我的第一反应并不是：“这里肯定有漏洞”，

而是：**“这个 IP 到底是谁？”**

它可能只是正常的图片服务器，也可能是 CDN 节点。

但还有一种可能：

**这是一个没有出现在前期 Web 资产视野中的独立服务器**

如果是后一种情况，那么这条看似普通的图片请求，就不再只是一张图片，而更像是 APP 无意中暴露出的一个新攻击面

这里还有一个值得注意的地方：**这个 IP 并不是通过扫描器枚举得到的，而是 APP 在正常业务流程中主动请求到的通信地址**

这意味着，接下来与其继续围绕主域名做测试，不如顺着这个 IP 看看它到底承担着什么业务

**从一个 IP 继续往下追**

拿到这个 IP 后，我先进行了基础验证

这里我并没有直接把它当成漏洞，而是先确认它到底是什么角色。

如果它只是普通 CDN 节点，那么继续深入测试的价值有限；

如果它对应的是一台独立业务服务器，那么就意味着 APP 暴露出了一个新的业务入口。

实际访问后发现，这个地址并不是简单返回图片资源，而是可以直接访问，并且背后运行着一个独立的 Web 服务

也就是说:APP->图片请求->裸 IP->独立 Web 服务->新的业务入口

到这里，测试思路发生了一次变化

这个 IP 本身未必意味着漏洞

但**IP 背后的服务，可能意味着新的攻击面**

对于众测来说，这种发现往往比单纯拿到一个 IP 更有价值

**意外发现文件上传功能**

继续观察这个 Web 服务后，我发现其中存在文件上传功能

到这里，我开始重点关注它的上传逻辑

首先确认正常文件能否上传，然后进一步观察服务端对于文件类型、文件名以及后缀的处理方式

测试过程中发现：

**服务端主要依赖文件名后缀进行限制，存在校验不足的问题，可以通过修改文件名后缀上传自定义后缀文件**

原本预期的业务逻辑应该更接近：

用户上传文件->服务端校验文件类型->严格限制允许的文件类型->保存文件

但实际观察到的处理逻辑存在明显的限制缺失。

因此，这里不能简单地把它理解成一个普通的“文件上传接口”。

真正值得关注的是：

**攻击者能够影响最终上传文件的类型。**

当然，文件上传漏洞最终能够造成多大的影响，还需要结合上传目录、文件访问方式、服务器解析机制以及权限控制等因素进行判断。

**文件上传漏洞验证**

发现上传功能后，我没有停留在“这里存在一个上传点”这一层，而是继续对其实际处理逻辑进行了验证

对于文件上传类问题来说，上传接口本身并不能直接等同于高危漏洞。真正需要确认的是：**攻击者能否控制最终写入服务器的文件，以及这个文件落地后能够产生什么影响**

因此，我按照实际请求链路继续进行了测试

首先测试正常文件上传，确认服务端能够接收并处理上传请求；随后进一步观察服务端对上传文件名称、后缀以及文件类型的处理方式

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVjweQ4DOyOEeXTjAQCPvyPWVEvseKxVyCSK0g70ty6jJwJb5zvSGKHbzrWVMIBBxjRESiasKjKmibkyficF6J47s4qfr7DrQskEo/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

测试过程中发现，服务端对上传文件的限制并不严格，上传文件的后缀存在可控空间。通过调整上传文件的文件名及相关参数，我成功绕过了原有的文件类型限制，使服务端接受了原本不应被允许上传的文件

到这里，问题已经不再是简单的“存在一个上传接口”，而是**攻击者已经能够影响服务器最终接收并保存的文件类型**。

随后我进一步确认了文件的实际落地情况，并验证上传后的文件能够被正常访问。

也就是说，这条攻击链已经实际走通：上传接口->上传限制校验->绕过文件类型限制->文件成功上传->文件实际落地->上传文件可被访问

至此，文件上传漏洞已经完成了实际验证。

这里需要特别说明的是，我没有继续尝试利用该文件上传点进一步获取服务器权限或扩大影响。

原因并不是漏洞无法继续利用，而是在后续核实过程中发现，当前服务器虽然与目标业务存在关联，但并不属于本次众测约定的核心业务资产范围。

因此，在确认漏洞真实存在并保留必要验证证据后，我停止了进一步利用，并将该问题及资产归属情况一并反馈给了甲方，甲方给出的说法与我想的一致，并且给出口头嘉奖

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAWof0DsRpohE1RJqN2kIicfTDyQwUOZhtUOfcLugjQa3407AkY5kyqG3IsTPEAzgFq2bIInSRl0eawIZVIcHia5hm3EEShnCU4Gc/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

这次测试给我的一个比较深的体会是：

**漏洞验证和漏洞利用，是两个不同的阶段；能够继续利用，不代表就应该继续利用。**

在真实的安全测试中，技术上“能不能打进去”和授权范围内“应不应该继续打”，是两件完全不同的事情

**一个有意思的问题：我好像“打偏了”**

到这里，其实已经可以确认：

**漏洞本身是真实存在的**

后续进行资产归属核验时，却发现了一个比较有意思的情况。

这个上传点所在的服务器，属于目标单位的外围附属资产，但**不在本次众测约定的核心业务资产范围之内**。

也就是说，从技术路径来看，我确实找到了漏洞；

但从众测规则和资产边界来看，却相当于：

**“漏洞是真的，但打偏了。”**

这个结果反而让我觉得很有代表性。

因为在实际众测中，我们经常会把注意力集中在：

```
主域名核心业务核心 API后台系统
```

但一个真实单位的互联网暴露面，往往远比这些复杂

可能存在:核心业务,APP,API,图片服务,文件服务，历史系统，独立服务器，第三方/外围系统

这些系统虽然可能服务于同一个业务体系，但安全建设水平并不一定一致。

因此：

**发现漏洞、确认资产归属、判断业务影响，其实是三个不同的问题。**

这次测试也让我更加意识到，漏洞验证不能只关注技术层面的“能不能打”，还需要确认：

* 资产到底属于谁；

* 是否属于授权范围；

* 是否属于核心业务；

* 漏洞实际影响是什么。

确认该资产不在本次众测约定的核心范围后，我没有继续对该服务器进行进一步利用，而是保留必要的验证证据并结束了后续测试

**为什么 APP 流量值得关注？**

回头看整个过程，真正让我觉得有价值的，其实不是最后那个上传点。

而是：

**如果我没有去分析 APP 流量，这个服务器很可能根本不会进入我的测试视野。**

传统 Web 资产发现的思路通常是：

```
主域名 ↓子域名 ↓IP ↓端口 ↓Web 服务 ↓漏洞
```

而 APP 给了我另一条路径：

```
APP ↓API / 图片 / 文件请求 ↓通信地址 ↓新的 IP / 域名 ↓独立 Web 服务 ↓新的功能 ↓漏洞
```

这两条路径最大的区别在于：**第二条路径是从业务行为反推出基础设施**

它不一定每次都能发现漏洞，但有机会发现传统资产收集过程中没有进入主要测试视野的业务入口

所以对于 APP 流量，我现在更关注的并不是“能不能抓到包”，而是：

**APP 到底在和哪些服务器说话？**

**从一次异常请求重新理解攻击面**

这次的情况还有一个值得注意的地方。

如果单纯把：“APP 请求资源时使用了裸 IP”

单独拎出来，并直接定性为信息泄露漏洞，其实并不严谨。

因为：

**一个 IP 地址本身，并不一定构成安全漏洞。**

真正有价值的是后续形成的完整链条：

```
APP 暴露通信信息        ↓发现新的网络入口        ↓确认入口存在独立 Web 服务        ↓发现文件上传功能        ↓发现上传限制存在缺陷        ↓确认真实安全风险        ↓进行资产归属核验
```

所以，这里真正值得记录的并不是：“APP 泄露了 IP。”

而是：

**一个看似普通的客户端通信信息，最终成为了扩大攻击面的入口。**

这也是我认为这次测试最有价值的地方

**如果重新来一次，我还会怎么做？**

如果让我重新测试一次类似目标，我大概还是会遵循几个简单的原则。

### **1. 先看业务入口，再看客户端**

先完成基础 Web 资产收集。

如果主 Web 面没有明显突破口，再转向：

```
APP小程序H5客户端接口
```

不要把 APP 只当成一个业务客户端，也可以把它当成一个观察目标基础设施的入口

**先关注异常，再判断漏洞**

对于客户端流量，我会特别注意：

* IP 地址

* 异常域名

* 非主域名请求

* 图片/文件服务器

* 对象存储

* 特殊接口

* 不常见的通信地址

因为真正值得继续追踪的东西，往往并不会直接告诉你：“这里存在一个漏洞。”

它可能只是表现得：**“这里和其他地方不太一样。”**

### **3. 先确认资产归属，再判断影响**

发现新的 IP 或域名后，不要马上进入漏洞利用。

需要先回答：

它属于谁？

为什么 APP 会访问它？

对应什么业务？

是否属于目标？

是否属于授权范围？

只有把这些问题搞清楚，后续的漏洞验证才有意义

### **4. 先证明问题真实存在，再考虑进一步利用**

对于漏洞验证，我更倾向于：发现->复现->确认->评估影响

而不是为了让漏洞看起来更“高危”，强行把利用链往后延伸

尤其是在真实众测环境中，**测试边界本身也是测试的一部分**

## **建了个**src专项圈子，内容包含**src漏洞知识库**、**src挖掘技巧**、**src视频教程**等，一起学习赚赏金技巧，以及专属微信群一起挖洞 圈子专注于更新src相关： ``` 1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例2、分享src优质视频课程3、分享src挖掘技巧tips4、小群一起挖洞 ``` ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg41LkR0ezBlmjJY4Lwgg8mr1A5efwqe0yGE9KTQwLPJTe9zyv3wgYnhA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0) ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1) ![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2 "null") ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTahgbr35OD8B1WCHW2uGMetuDzTPJiaHibhWhMm8UQ5iboDmNKqrRfjIrXQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5) ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWr5g7s0TNF4tBZqNbdewPNswTDOfvN6PkggCqz8j3mib6Vf3z4ia83asg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6) 图片 ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4Bd1oBmTkA5xlNwZM5fLghYeibMBttWrf57h8sU7xDyTe5udCNicuHo8w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7) ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTaTWxLibDHdqdx6IahjVWr6ficJWskIMjdrbYaLGBIVsbONxbb5ibDS5trQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8) 图片 ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTafQtWhe2qhicQCvx8XaDyp6Kb4eeWBnhZLlGKcAvxKausLKc2YYggykQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11) 图片 ![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7U...