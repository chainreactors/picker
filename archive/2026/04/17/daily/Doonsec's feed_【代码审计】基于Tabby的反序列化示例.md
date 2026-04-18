---
title: 【代码审计】基于Tabby的反序列化示例
url: https://mp.weixin.qq.com/s/R7tBno-m5o2QGN6uZJ5Plg
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:28:33.470746
---

# 【代码审计】基于Tabby的反序列化示例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ocg1gpicEs1tZw6fWPKUAuHTo0GShH1wmJpb6oHyWuojKoZ6UrB2JN7rL1VhoCxd6SRyR2Fa2sEmTicpHBTdD0Nwaa0MtKbwATI19Zvvc6lJ0/0?wx_fmt=jpeg)

# 【代码审计】基于Tabby的反序列化示例

原创

十月的进阶之路
十月的进阶之路

十月的进阶之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 千里之行，始于足下

## 0. 先建立分析方法论

本文依旧使用webgoat作为示例，做反序列化分析时，脑子里永远只放三件事（至少在这个靶场如此）：

**Source**：数据从哪里进入对象恢复流程。

**Taint**：这些数据是否能被攻击者控制。

**Sink**：这些数据最后会不会走到危险函数。

反序列化漏洞的判断逻辑不是“有没有 `readObject`”，而是：

```
入口方法
→ 对象字段被恢复
→ 字段被后续逻辑使用
→ 进入危险函数
```

后面所有查询，本质上都是在回答这三个问题。

## 1. 第一步：确认图数据已经导入成功

### 目的

先确认 `Neo4j`里确实有 `Tabby` 导入的代码图，否则后面所有查询都没有意义。

### 命令

```
match (m:Method) return count(m)
```

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1shpH3NzMZyenJlGCdPiafZZGcfP2C6fB7DIkOicXGeOqIDl7QibJglrlPyqEmPgnn3iaMcYprkGnrmEiamibVLFRILagLI176d9Q8ro/640?wx_fmt=png&from=appmsg)

### 这个命令在做什么

统计 `Method` 节点数量。 你现在查到 `288846`，说明图数据是完整的，依赖库、项目代码、`JDK` 类都在图里。

### 为什么先做这个

因为反序列化分析依赖大量方法节点、调用边和污点标记。没有图，就谈不上路径分析。

### 下一步做什么

开始缩小范围，不再看全图，只看自己的包。

## 2. 第二步：把搜索范围缩到项目包

### 目的

图里有 `JDK`、`Spring`、`Jackson`、`WireMock`、各种依赖库。 如果不先过滤包名，结果会被依赖库淹没。

### 命令

```
match (m:Method)
where m.CLASSNAME contains "org.dummy.insecure"
return m.CLASSNAME, m.NAME, m.SIGNATURE
limit 50
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1uxTIVLCJDcRdkeebDMZQ7b93GSVeEIHWfLWBuIrO6Cg2u4Ev3HgPsxUyWVdfU7YeooKlthwD0p1oSz0JBTwf8t8jicBKFuicB84/640?wx_fmt=png&from=appmsg)

### 参数意义

* `m.CLASSNAME contains "org.dummy.insecure"`：只看自己的代码
* `limit 50`：避免一次性返回太多结果，先观察结构

### 为什么这样做

漏洞分析最怕“看到了很多结果，但都不是自己的代码”。 先限定包名，能快速判断项目里到底有哪些类、方法、入口。

### 下一步做什么

在自己的包里找候选`source`。

## 3. 第三步：找“候选反序列化入口”

### 目的

先找出项目里是否存在 `readObject` / `readExternal` 这种入口方法。

### 命令

```
match (m:Method)
where m.CLASSNAME contains "org.dummy.insecure"
and m.NAME in ["readObject","readExternal"]
return m.CLASSNAME, m.NAME, m.SIGNATURE
```

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1ud0Zp8dH1IoP0ZQJKO2qYKiavlRtr3FiakzdB29WZwaHtrGPTZggJtJJolm1KS3kHlvKTXkSnRvS9YTPHTo37UOgDmlAfXGFttU/640?wx_fmt=png&from=appmsg)

### 这个命令在做什么

它是在问： “我自己的代码里，有没有显式定义反序列化回调方法？”

### 为什么这一步很重要

因为 `Java` 原生反序列化漏洞里，`readObject` 往往就是 `source`。 它不是普通业务方法，而是 `JVM` 在反序列化时自动触发的特殊入口。

### 你现在的结果意味着什么

已经查到了 `org.dummy.insecure.framework.VulnerableTaskHolder` 的 `readObject`，这说明：

* 项目里确实存在原生反序列化入口
* 这不是依赖库里的 `gadget`，而是自己的代码

### 一个关键理解

`readObject` 通常**不会**通过普通 `CALL` 边被别的方法调用。 它是 JVM 隐式触发的，所以你用“谁调用了 `readObject`”去查，常常会查不到。

### 下一步做什么

确认这个入口是否真的能走到危险函数，也就是找 `sink`。

## 4. 第四步：理解 sink 不是“普通危险方法”，而是 Tabby 标记过的危险点

### 目的

不是所有 `exec`、`lookup`、`invoke` 都能直接拿来做路径分析。 `Tabby` 的 `procedure` 需要的是它识别过的 `sink` 节点。

### 命令

```
match (sink:Method {IS_SINK:true})
return sink.NAME, sink.CLASSNAME, sink.VUL
limit 20
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1t9EKaIhQUsQxxE7P1p6Eafe4nEMQmk9Rk7dibhSreA1NrhDfOyNzeR9ricnMh1IjBSBbStnLzGEG1kAmURqXHjvTdsgoCeI0KTY/640?wx_fmt=png&from=appmsg)

### 参数意义

* `IS_SINK:true`：只查 `Tabby` 标记的危险方法
* `VUL`：漏洞类型，比如 `EXEC`、`JNDI`、`REFLECTION`

### 为什么一定要加 `IS_SINK:true`

如果只写 `where sink.NAME in ["exec","invoke","lookup"]`，查出来的可能是普通方法，不一定是 `Tabby sink`，`procedure` 内部就会报错。

### 当前结果意味着什么

已经看到：

* `java.lang.Runtime.exec` → `EXEC`
* `javax.naming.InitialContext.lookup` → `JNDI`
* `java.lang.reflect.Method.invoke` → `REFLECTION`

这表示图里确实已经有可分析的危险点。

### 下一步做什么

把 `source` 和 `sink` 连起来，开始做路径查找。

## 5. 第五步：用 Tabby 的路径搜索去连 source 和 sink

### 目的

确认“反序列化入口”是否能把污染数据送到危险函数。

### 命令

```
match (source:Method)
where source.CLASSNAME contains "org.dummy.insecure"
and source.NAME = "readObject"

match (sink:Method)
where sink.IS_SINK = true
and sink.NAME = "exec"
and sink.CLASSNAME = "java.lang.Runtime"

call tabby.algo.findPath(source, ">", sink, 5, false)
yield path
return path
limit 3
```

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uQ0gXRhw4Y9Fq5sv0ej5sKXW8BmgK8gEac5KPaYCwPPVSelQdlmia1TPv0ibKyFeQLOM76NweeVpbCTHHlkRG1vtHUI98yxAkRc/640?wx_fmt=png&from=appmsg)

### 每个参数是什么意思

* `source`：起点，也就是反序列化入口
* `" > "`：前向搜索，从 `source` 往后找
* `sink`：终点，也就是危险函数
* `5`：最大路径长度，先用小一点，便于聚焦
* `false`：不是深度优先，先用默认策略更稳定

### 为什么用前向搜索

因为现在已经明确知道 `source` 在哪里。 `source` 少、`sink` 多的时候，前向查找通常更自然。

### 为什么先把 `sink.NAME` 收窄到 `exec`

因为现在的目标是验证一个典型反序列化 `RCE` 链。 先把范围缩小，容易看懂结果，确认这一条后，再扩展到其他 `sink`。

### 下一步做什么

看结果路径，判断它是不是“真的从 `source` 到 `sink`”。

## 6. 第六步：读懂返回结果，不是只看“查到了没”

### 目的

学会看 `Neo4j` 返回的 `path` 结构，知道它到底证明了什么。

你现在拿到的结果里，最重要的是这几个字段：

* `start`：路径起点
* `end`：路径终点
* `segments`：中间的边
* `LINE_NUM`：命中的源代码行号
* `POLLUTED_POSITION`：污染流向的位置
* `IS_SINK:true`：终点确实是危险函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1tPegex1TMSfKKLVTl3mAk6SVNBmKKEclkNCdSibB1ASrZw0EVKsEicmhU1728DRVmkUNAFsuACdGNdEyrzDkdfPNxNoiaCAIpkSU/640?wx_fmt=png&from=appmsg)

### 当前结果说明了什么

结果已经表明：

```
org.dummy.insecure.framework.VulnerableTaskHolder.readObject
→ java.lang.Runtime.exec
```

而且 `LINE_NUM` 直接指向了代码里调用 `exec` 的位置。

### 为什么这一步比“查到路径”更重要

因为漏洞分析的关键不是“图里有一条边”，而是：

* 这条边是不是源码里的真实语句
* 污点是不是从对象字段传到了危险参数
* 这条路径是不是出现在你自己的包里

这里都满足了。

### 下一步做什么

回到源码，人工确认这条路径对应的逻辑。

## 7. 第七步：回到源码确认语义

### 目的

图分析给“路径”，源码确认“漏洞成立”。

这段代码里，分析重点有两个：

第一段：

```
stream.defaultReadObject();
```

这表示对象字段会从序列化流里恢复出来。 这一步很关键，因为它让 `taskName`、`taskAction` 变成外部可控数据。

第二段：

```
Runtime.getRuntime().exec(taskAction);
```

这表示恢复后的数据直接进入命令执行。

### 为什么这就足够了

因为这里没有必要再找别的复杂 `gadget`，类自己已经把“反序列化输入”送进了 `exec`，这就是完整的危险链。

## 8. 第八步：为什么查不到 `caller -> readObject`

### 目的

当尝试查：

```
match (caller:Method)-[:CALL]->(m:Method)
where caller.CLASSNAME contains "org.dummy.insecure"
and m.NAME = "readObject"
```

这经常没有结果，不是因为没有漏洞，而是因为 `readObject` 是 `JVM` 隐式调用的，不是你代码里显式 `CALL` 出来的。

### 这说明什么

`Neo4j` 图是“程序静态调用关系”的图，不是运行时反射调用日志。 `JVM` 自动触发的回调，不一定表现为普通 `CALL` 边。

### 所以应该怎么想

不要问“谁调用了`readObject`”，而要问：

“这个 `readObject` 里，数据流去了哪里？”

## 9. 第九步：常见坑位

### 坑一：忘记加 `IS_SINK:true`

会导致 `procedure` 报错，或者拿到错误节点。

### 坑二：只看 `CALL`，不看隐式入口

`readObject`、`readExternal`、框架自动反序列化入口经常不是普通调用边。

### 坑三：范围太大

不加包名过滤，最后看见的是依赖库，不是自己的项目。

### 坑四：只看路径长度，不看代码语义

路径再短，也要结合源码判断字段是不是可控、条件是不是可绕过、`sink` 是否真的危险。

## 10. 分析流程总结

给个示例参考顺序：

第一步，确认图是否导入完成。

第二步，限定自己的包名。

第三步，找 `readObject`、`readExternal`、`Web` 入口、`JSON/XML` 入口。

第四步，找 `IS_SINK:true` 的危险方法。

第五步，用 `tabby.algo.findPath` 把 `source` 和 `sink` 连起来。

第六步，回源码确认字段流向和危险调用。

 第七步，记录路径、行号和污点位置，形成结论。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

十月的进阶之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GFPic2iaAJQw9icmAfmmEej0faflh5tB82cUK35MTVuw42wOQtcxfYUV0AXBEgJCSan9OhFhdMXuUpjtyUB8cxwVA/0?wx_fmt=png)

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