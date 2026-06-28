---
title: Cisco CUCM 任意文件写入到RCE：一条被低估的攻击链
url: https://mp.weixin.qq.com/s/bGi5a_ZLKNMmrNaIwmDAFQ
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:11:42.025849
---

# Cisco CUCM 任意文件写入到RCE：一条被低估的攻击链

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdKyXe33Tiap35HFiaQyZFfMa5k3r5ZaQv9HHmF2JF5Zzbrk2fHpd7icTd9B4WiaG1MwP8QkqfRcGwTQWS1ibpSWhbnNsee9j41baTU/0?wx_fmt=png&from=appmsg)

# Cisco CUCM 任意文件写入到RCE：一条被低估的攻击链

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 思科统一通信管理器（CUCM）曝出认证绕过漏洞，允许攻击者通过组合SSRF与路径穿越写入任意文件，最终植入Webshell实现远程代码执行。整条利用链值得关注的点在于：它没有依赖什么新技术，而是把几个老问题精巧地串在了一起。

## 这事有多严重

Cisco Unified Communications Manager（CUCM）是企业电话系统的核心，调度着数以万计的IP电话、视频终端。一旦这玩意儿被拿下，企业通讯基本就裸奔了。编号 CVE-2026-20230 的漏洞，影响版本 15.0.1.13901-2，思科已经发了补丁：https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW 。但补丁归补丁，部署进度永远慢于攻击者的扫描速度。

## 根因：一个未认证接口引发的血案

翻开 `jakarta-tomcat\webapps\cmplatform\WEB-INF\web.xml`，有个端点直接暴露在外：`/installClusterStatusExecute`。没有任何认证拦着。对应的 Servlet 是 `com.cisco.ccm.cmplatform.servlets.ClusterInstallStatusServlet`，当 `action` 参数等于 `clusterNodeInstallStatus` 时，代码流程会一路往下走到 `NodeInstallStageClient#getInstallStage`，这里面发起了一个 HTTPS 请求。问题出在：请求的目标地址，是攻击者通过 `hostname` 参数传进去的。

这就是一个典型的 SSRF 入口。只不过思科做了主机名校验，127.0.0.1 和 localhost 这些常规的内网地址直接被 ban 了。校验逻辑在 `InjectionFilter#hostHeaderValidation`。绕过它的办法比想象中简单——

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfeOicqwVAXPYnImvnQU82pQ9bGp3P1eTuicZY1IdpicJCWWmCcurbKuGFE0IZxppKlWg6j2uAOBYkbXVf8rJEGiaO6tPl3iczzxmTQ/640?wx_fmt=png&from=appmsg)

我们只需要拿到服务器的真实主机名。恰好，有个未认证的接口可以返回这个信息：`/webdialer/Version.jws?wsdl`。访问它，返回的 WSDL 里就写着主机名。拿到这个名字之后，SSRF 的校验就形同虚设。

## 从 SSRF 到任意文件写入

整个攻击的精髓在于 `hostname` 参数怎么被利用。它本来该传一个集群节点的主机名，比如 `cu-cm-pub-01`。但攻击者往里塞的是一整条 URI，经过 URL 编码后长这样：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdKyXe33Tiap35HFiaQyZFfMa5k3r5ZaQv9HHmF2JF5Zzbrk2fHpd7icTd9B4WiaG1MwP8QkqfRcGwTQWS1ibpSWhbnNsee9j41baTU/640?wx_fmt=png&from=appmsg)

解码后能看到，实际请求的路径是本地的一个 Axis 服务端点，末尾的 `?method=!` 加上一段 XML，利用了类似 CVE-2019-0227（Axis 1.4 经典洞）的手法：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeMkGG6qXTibx3uBT9ZBu0C1jPXgOXUlKCoqL24SG4XcZ7LpVBBbtia2Uibl2K3Iyysa4FW2weSPgMm9Uo8p09s6CuKWCNxNU3bWk/640?wx_fmt=png&from=appmsg)

服务器收到这个精心构造的请求后，调用 `JerseyClient#doGet` 发起内部 HTTPS 请求，目标变成了本地的 Axis 服务，而 Axis 服务忠实地把请求参数里的内容写进了日志——`LogHandler` 被配置成把日志写到任意路径。路径穿越符 `../` 一路跳到了 `tomcat/webapps/platform-services/axis2-web/aaa.jsp`。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibcYPXp5sFLPaqZ7aia86nbpaNtFpkXMSwfb2eVKxsKf2lvq3V7QCuaX2PxscU039QQa6T4HJGIOdaqfpLfbYy95ZibwScIy81HPw/640?wx_fmt=png&from=appmsg)

也就是说，攻击者现在有了一个自己控制内容的 JSP 文件。

## Webshell 落地与命令执行

文件写进去了，但这个 `aaa.jsp` 的内容只是 Axis 接口吐出的日志，不是什么 Webshell 代码。真正把恶意代码塞进去的，是这个 JSP 文件本身的一个“功能”——它接受 `f` 参数（目标路径）和 `t` 参数（要写入的内容），可以再次写入任意文件。攻击者访问:
`/platform-services/axis2-web/aaa.jsp?f=../../../../../../../common/log/taos-log-a/tomcat/webapps/platform-services/axis2-web/c.jsp`
同时传递 `t` 参数，值为一句话木马：一个带密码保护、能执行系统命令的 JSP 代码片段。

到这一步，攻击者打开浏览器访问：
`https://目标IP/platform-services/axis2-web/c.jsp?pwd=123&i=id`
服务器就乖乖执行 `id` 命令。至此，CUCM 彻底沦陷。

## 几个值得琢磨的点

这台戏唱完，有几个地方让我觉得设计上欠考虑。第一，集群安装状态查询为什么要暴露给未认证用户？这种接口显然只该给集群内部节点相互调用，要么加认证，要么只监听本地回环地址。第二，SSRF 的目标地址校验只过滤 IP 不过滤真实主机名，这种“修半边”的做法等于没修。第三，一个老旧的 Axis 框架一直没升级或替换，历史漏洞 CVE-2019-0227 的利用手法在 2026 年还能复现，这说明组件的依赖管理根本没当回事。

从利用难度看，这条链不需要任何前置权限，拿到主机名只需要一次请求，整个攻击过程干净利落。真实的攻防场景中，这种漏洞一旦被写进攻击框架，内网横向移动就是分分钟的事。

思科给的修复在链接里，但如果你负责维护 CUCM，别只打补丁——检查一下 `web.xml` 里还有没有别的未认证端点，检查 Axis 组件的版本，顺便把日志到底写在哪里也看一眼。

---

### 参考资料

[1] https://ssd-disclosure.com/cisco-unified-communications-manager-arbitrary-file-write-to-rce/

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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