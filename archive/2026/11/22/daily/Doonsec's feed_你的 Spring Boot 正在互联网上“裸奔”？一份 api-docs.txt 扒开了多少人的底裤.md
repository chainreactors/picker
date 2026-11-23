---
title: 你的 Spring Boot 正在互联网上“裸奔”？一份 api-docs.txt 扒开了多少人的底裤
url: https://mp.weixin.qq.com/s/-QGarB-SEnYR9odGUUXUyw
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:01:32.881746
---

# 你的 Spring Boot 正在互联网上“裸奔”？一份 api-docs.txt 扒开了多少人的底裤

# 你的 Spring Boot 正在互联网上“裸奔”？一份 api-docs.txt 扒开了多少人的底裤

原创

网络安全民工
网络安全民工

网络安全民工

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 先别急着关页面。
> 如果你的项目里出现过 `actuator/env`、`actuator/heapdump`、`druid/websession.json`、`swagger-ui.html`，请花 3 分钟看完。
> 因为攻击者的字典里，这些路径一个都不少。

---

## 一、一张“敏感端点清单”，看得人后背发凉

最近拿到一份 `api-docs.txt`，打开一看，好家伙——密密麻麻全是 Spring Boot 项目里最不该随便暴露的路径：

```
actuator/envactuator/heapdumpactuator/jolokiaactuator/logfileactuator/mappingsactuator/metricsactuator/threaddumpgateway/actuator/envgateway/routesdruid/websession.jsondruid/sql.htmlswagger-ui.htmlv2/api-docsv3/api-docs...
```

这还只是冰山一角。
`actuator/env` 能吐配置，`heapdump` 能拖内存，`jolokia` 配置不当可能直接 RCE，`gateway/routes` 能把网关路由看个精光，Druid 监控页面的 `websession.json` 甚至能把会话信息摆上桌。

很多开发同学觉得：“我这是内网服务，没事。”
但现实是：**资产测绘一搜，一大把 Spring Boot 应用正把 Actuator 端点明晃晃挂在公网上。**
网络空间测绘：FOFA语法 `body="Whitelabel Error Page"`、ZoomEye 语法 `app:"Spring Framework"`，搜出来的结果足够让安全同学睡不着觉。

更扎心的是——这些路径不是 0day，也不是什么高深技巧。
它们就安安静静躺在攻击者的 `Dir.txt` 字典里，等着被批量扫。

---

## 二、别等被拖了 heapdump 才想起关端点

Spring Boot 好用，Actuator 好用，Swagger 好用，Druid 也好用。
但“好用”和“裸奔”之间，往往只差一个 `management.endpoints.web.exposure.include=*`。

一旦端点暴露，可能发生什么？

* `actuator/env` 泄露数据库账号、Redis 密码、第三方 Key；
* `actuator/heapdump` 被下载，内存里的 token、密码、业务数据一起打包带走；
* Spring Cloud Gateway 的 SpEL、环境属性修改等历史漏洞被批量验证；
* Swagger 文档把内部接口、参数、鉴权方式全部交底；
* Druid 监控页面把 SQL、Session、URI 统计暴露得明明白白。

你以为只是“信息泄露”，攻击者眼里却是**从信息收集到横向移动的跳板**。
更何况，Spring 生态的“核弹级”漏洞从来就没断过。

看看下面这些让人头皮发麻的 **CVE 标签**，你的系统躲过了几个？

* `CVE-2022-22965` (大名鼎鼎的 Spring Core RCE / Spring4Shell)
* `CVE-2022-22947` (Spring Cloud Gateway SpEL RCE)
* `CVE-2022-22963` (Spring Cloud Function SpEL RCE)
* `CVE-2021-21234` (任意文件读取)
* `CVE-2021-21344` (Eureka Xstream 反序列化)
* `CVE-2024-37084` (Spring Cloud Data Flow RCE)
* `CVE-2025-24813` (Apache Tomcat partial PUT 文件写入/RCE)
* `CVE-2025-22235` (Spring Boot EndpointRequest 鉴权绕过)
* `CVE-2025-41243` (Spring Cloud Gateway 环境属性修改)
* `CVE-2026-47884` (Spring Framework XsltView SSRF/RCE)
* `CVE-2026-59378` (Spring Boot Actuator 默认安全配置鉴权绕过)

面对如此密集的 `spring-vulnerability` 火力网，光靠手动排查？根本防不住！

---

## 三、安全自查，不需要从零造轮子

问题来了：知道有风险，怎么快速发现？

手动拼路径？一个两个还行，几十个端点、上百个目标，人会麻。
于是，开源项目 **SpringBoot-Scan** 就是为这个场景准备的。

当前版本 **V3.1.1-2026/11/22**，定位很明确：
**专门针对 Spring Boot 的高危漏洞利用集成框架与敏感信息泄露扫描利器。**

它不是那种只会在命令行里 print 一堆红字的玩具。看看它现在已经支持的东西：

* 内置 `Dir.txt` 敏感端点字典，Actuator、Swagger、Druid、Gateway、Jolokia、heapdump 等路径基本收齐；
* **全量 CVE 漏洞库**：完美集成上方列表中的 `exploit` 模块，从信息泄露直接打通到 `vul` 漏洞利用。
* 支持单一 URL 扫描、TXT 批量扫描；
* 支持敏感文件扫描并自动下载，带进度条；
* 支持 HTTP 代理、代理认证、自定义请求头、随机 User-Agent；
* 支持 Fofa / ZoomEye / Hunter 资产测绘导出，扫之前先把资产捞回来；
* 支持多进程/并发，批量扫描速度提升明显。

简单说：**你负责授权，它负责把该看的端点、该验的 `security-tools` 漏洞，快速过一遍。**

---

## 四、用法有多简单？几条命令的事

对单一目标做信息泄露扫描：

```
python3 SpringBoot-Scan.py -u http://example.com/
```

读取 TXT 批量扫：

```
python3 SpringBoot-Scan.py -uf url.txt
```

对单一目标做漏洞扫描（自动匹配上述CVE）：

```
python3 SpringBoot-Scan.py -v http://example.com/
```

批量漏洞验证：

```
python3 SpringBoot-Scan.py -vf url.txt
```

扫描并下载敏感文件（如 heapdump）：

```
python3 SpringBoot-Scan.py -d http://example.com/
```

批量敏感文件扫描：

```
python3 SpringBoot-Scan.py -df url.txt
```

挂代理、带认证、自定义请求头也都有对应参数。
甚至还能对接 ZoomEye、Fofa、Hunter 的 API，把 `spring-boot` 资产先导出来，再批量喂给扫描模块。

对于二级目录部署的 Spring 项目，直接把 `example.com/test/` 这种路径传进去就行；自签名证书报错，换成 `http://` 即可。
作者在 README 里把“使用者体验”四个字算是玩明白了。

---

## 五、工具是刀，关键看谁用、怎么用

必须说清楚：**SpringBoot-Scan 是开源安全测试工具，不是让你拿去乱扫的“大杀器”。**
它适合什么场景？

* 企业安全团队做 Spring Boot 资产自查；
* 渗透测试人员在**授权范围内**做信息收集和漏洞验证；
* 开发团队上线前检查 Actuator / Swagger / Druid 是否误暴露；
* 安全培训与靶场环境演练。

不适合什么场景？
**没有授权，对着互联网一顿乱扫。**
那不是“师傅”，那是给自己找麻烦。

工具项目里也写得很明白：请务必在合法授权前提下使用，非法行为后果自负。
所以，软文归软文，底线归底线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribR7Gy0LAgqHutT57qJqdWXOkOeKFmskicGFyakdav8bteA6g4PITgCvVNQPlSmT5NcQvIdKr6y7OU5qAgSib0NvQwZTfavIEreeM/640?wx_fmt=png&from=appmsg)

---

## 六、最后说句实在话

这份 `api-docs.txt` 里列出的路径，加上那一长串触目惊心的 CVE 编号，攻击者早就背得滚瓜烂熟。
你的 Spring Boot 应用有没有暴露 `actuator/env`？有没有把 `heapdump` 挂在外面？有没有中招 `CVE-2022-22965`？
**别靠猜，扫一遍，关掉该关的，比什么都强。**

如果你正好需要一把顺手的“Spring Boot 安全自查瑞士军刀”，可以去看看这个项目：

* 下载地址：`https://download.csdn.net/download/zhengfei611/93906494`
* 当前版本：`V3.1.1-2026/11/22`

代码是作者一行行敲的，漏洞模块是一个个跟的，字典是一点点补的。
如果它帮你省下了几个小时的端点拼接时间，或者帮你发现了一个本该关掉的 Actuator 端点、阻断了一次潜在的 `exploit`，**去点个 Star，不过分。**

> 毕竟，安全这件事，**早扫一天，少慌一年。**

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4Ln7j9YplYkgXg13os3mdJEN1k241aoU461aOjdLSrQvIscf5u8YrTFoPKmQZF8d26FIsE0wb5pS8Gdadytia6g/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过