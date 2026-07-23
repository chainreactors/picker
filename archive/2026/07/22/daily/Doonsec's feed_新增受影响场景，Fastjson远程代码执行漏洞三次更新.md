---
title: 新增受影响场景，Fastjson远程代码执行漏洞三次更新
url: https://mp.weixin.qq.com/s/VORXbD0VvNio7ETVhiGr9w
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:08:43.020799
---

# 新增受影响场景，Fastjson远程代码执行漏洞三次更新

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T4OSm0sXdEMJkjcePF4uHFNMEBj9a7fITQruPtP807vkAK89qKL4SupBAbr7xZt29n9E21G8f3U2HeTefzt4cweeHib3ic3nJsoJ9tb22cGWs/0?wx_fmt=jpeg)

# 新增受影响场景，Fastjson远程代码执行漏洞三次更新

微步情报局
微步情报局

微步在线研究响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

漏洞概况

Fastjson 是 Alibaba 开源的一款基于 Java 的快速 JSON 解析器/生成器，广泛用于 Java 应用的 JSON 序列化与反序列化。

近日，微步情报局监测到互联网披露了Fastjson 远程代码执行漏洞。经分析，Fastjson 存在远程代码执行漏洞，远程攻击者通过向使用受影响版本 Fastjson 的应用发送特制的恶意 JSON 数据，无需依赖任何第三方类库，即可在目标服务器上执行任意代码。

此漏洞无须用户权限，攻击者成功利用此漏洞可远程攻击者可在未启用安全模式的目标服务器上执行任意代码，直接威胁系统机密性、完整性与可用性，可导致服务器被完全控制。建议受影响用户尽快修复。

漏洞处置优先级(VPT)

**综合处置优先级：**高风险

|  |  |  |
| --- | --- | --- |
| 基本信息 | 微步编号 | XVE-2026-39684 |
| CVE编号 | 无 |
| 漏洞类型 | RCE(远程代码执行) |
| 利用条件评估 | 利用漏洞的网络条件 | 网络可达 |
| 是否需要绕过安全机制 | 否 |
| 对被攻击系统的要求 | 未启用 Fastjson 安全模式(SafeMode) |
| 利用漏洞的权限要求 | 无须用户权限 |
| 是否需要受害者配合 | 否 |
| 利用情报 | POC是否公开 | 是 |
| 已知利用行为 | 微步威胁感知平台TDP已捕获在野利用行为 |

漏洞影响范围

|  |  |
| --- | --- |
| 产品名称 | Fastjson |
| 官方通告影响范围 | 1.2.68<=version<=1.2.83 |
| 微步验证实际影响范围 | 1.2.66/1.2.67 jar:file也能复现。而且fastjson更低版本有其他安全问题，建议漏洞管控时按照version<=1.2.83 排查。 |

漏洞复现

jar:http 远程拉取在 Spring Boot FatJar 场景中可作为第一阶段资源获取。在 Linux/macOS 下，可进一步借助 /proc/self/fd 或 /dev/fd 转为 jar:file，形成二阶段 fd bridge RCE。

最新验证结论为：

1、Spring Boot 常见内嵌容器 Tomcat、Jetty、Undertow 均受影响（说明：这里指fd bridge 链路已验证，不等价于所有容器都支持单发直接 jar:http RCE。）

2、Linux/macOS：JDK8/17/21/25 等已验证可 RCE。

3、Windows：JDK8 可触发。Windows 缺少 /proc/self/fd 或 /dev/fd 同形态路径，高 JDK 不受影响。

4、1.2.83\_noneautotype不是“关闭 autoType 但仍可绕过”的普通配置状态，而是 artifact 行为发生变化，safeMode 在危险路径前直接终止，因此在当前已知利用链路下不受此漏洞影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEN6OGx2ccQxicoHtV4lmptpv5rxyFKYIgTEClM2zbYlTZuDkX6LNictEK6vZMhgCxkyVIgQFD0cuQNKRjsiaic8YJPicstSIIcvicsxc/640?wx_fmt=png&from=appmsg)

###

修复方案

### 临时缓解措施

1、官方暂未发布该漏洞补丁及修复版本,鉴于 fastjson 1.x 系列已停更，建议迁移至 Fastjson 2.x 版本

2、可通过以下任意一种方式启用 Fastjson 的安全模式(SafeMode):

* 代码启用： ParserConfig.getGlobalInstance().setSafeMode(true)
* JVM 启动参数启用： -Dfastjson.parser.safeMode=true
* 配置文件启用： fastjson.parser.safeMode=true

3、使用防护类设备拦截带有如下内容的POST、JSON请求：

·@type":"jar:file:.

·@type":"jar:http:..

4、可切换到 noneautotype 版本，Maven 坐标示例：

com.alibaba:fastjson:1.2.83\_noneautotype

微步产品支撑

1、微步漏洞情报于2026-07-20收录该漏洞。

2、微步下一代威胁情报平台NGTIP及X情报中心已向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。

3、微步威胁感知平台TDP已于2026-07-20支持检测，检测ID：**S3100181015**，模型/规则高于：**20260720000000** 可检出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEPSCIkLibPf0zSYFNAOz9uND2ia2sozDVW9FyfgVOUknCohC53UsMoib4VqgOIfZcQDYvOd63H3825KJic7pESk5O7D0gvoTvTFcics/640?wx_fmt=png&from=appmsg)

**4、微步威胁防御系统OneSIG已支持防护，规则ID：3100181015。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T4OSm0sXdEPOxxfhFH6h6mcdjyy9ksJC8ibgicQUcCHTpV3nsvGqOvlmrgr29ZknD4xdlKHKNSaHNIY6JllBLtJibXHlU2fKqrB6z0WB1aF7Vk/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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