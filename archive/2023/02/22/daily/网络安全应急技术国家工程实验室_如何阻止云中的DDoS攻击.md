---
title: 如何阻止云中的DDoS攻击
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247534681&idx=3&sn=8be639f0bab5f7236d3f8fec537e7e02&chksm=fa93fe98cde4778e34416166a47a845d1bc1afc4255f91d6cca12c6e301e22a0a95da8100f35&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2023-02-22
fetch_date: 2025-10-04T07:44:08.101815
---

# 如何阻止云中的DDoS攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176l4JlPzcial8zaT7ic4bSI3wCFfhOgwXnaqAK6MUiciaMyu5F4jPEiaq4DhZJGRkkIzSa0MfAaLJwic5o1w/0?wx_fmt=jpeg)

# 如何阻止云中的DDoS攻击

网络安全应急技术国家工程中心

从2022年1月到7月，Sysdig威胁研究团队实施了一个全球蜜网系统，通过多个攻击载体捕获了大量漏洞。Sysdig在《2022年云原生威胁报告》中指出，相较2021年，2022年的攻击类型已经从加密挖矿明显转向分布式拒绝服务（DDoS）活动。

如果组织希望通过检测与此威胁相关的早期迹象，来了解如何在云环境中预防DDoS攻击，那么本文将介绍保护云基础设施所需的大多数最佳实践。

# **云中DoS攻击的技术和方法**

在OSI（Open Systems Interconnection）模型中，DDoS攻击的模式和行为可以划分为不同的层。

例如，应用层攻击是HTTP/s级别的任何攻击。这是第7层，OSI模型的顶部。用DNS查询或HTTP GET请求充斥HTTP/s应用程序是实现这一点的简单方法，因为我们可以检测到Killnet网络攻击。

攻击者还可以在TCP（第4层）或通过UDP/ICMP活动（第3层）发起DOS活动。这些活动会淹没网络和服务器，直到它们无法处理任何合法的网络流量。攻击者的目标是饱和目标服务器的网络连通性。

最后，不仅攻击者可以造成这种破坏。您可能希望测试基础设施的健壮性，使用工具或服务来增加流量，并查看检测工具的行为。

在这篇文章中，我们的目标是使用CNCF Project Falco来检测导致云中的DoS攻击的妥协指标（IoC）。为了实现这一点，Falco必须插入各种云提供商的审计日志服务。值得庆幸的是，Falco为每个云数据源提供了一个专用插件。

通过长期监控预期的网络流量/行为，我们可以设计Falco规则来检测运行时的异常网络行为。

# **如何防范暴力破解DDoS攻击**

首先，确保Web服务器免受暴力攻击是很重要的。攻击者的目标是访问服务器或暂时使其失去响应。暴力破解包括尝试数千甚至数百万个密码，直到找到正确的密码。

一方面，终端用户在生成强密码时必须遵循安全策略，这样这种类型的攻击才不会成功。另一方面，大多数云提供商（例如微软、谷歌、亚马逊、IBM等）提供了诸如速率限制之类的工具来防止暴力攻击。

### **检测账户接管欺诈**

主要的威胁检测解决方案之一是监视应用程序的登录页面，以防止使用受损凭证对用户帐户进行未经授权的访问。账户接管是一种在线非法活动，攻击者在未经授权的情况下访问用户的账户。

就AWS的WAF技术而言，它具有帐户接管预防（ATP）功能，可以检测潜在的未经授权的访问，这是可能导致DoS攻击的最明显的IoC。

攻击者可以通过多种方式访问最终用户的帐户，例如使用被盗的凭据或通过一系列尝试猜测受害者的密码。由于Falco插入了每个云提供商（包括GCP、AWS和Azure）的云审计日志服务，我们可以创建Falco规则来检测来自不寻常IP的AWS帐户登录，例如：

```
```
- rule: Console Login Success From Untrusted IP desc: Detect a console login success from an untrusted IP address condition: >-   aws.eventName="ConsoleLogin" and   jevt.value[/responseElements/ConsoleLogin]="Success" and not aws.sourceIP in   (trusted_ip_addresses) output: >- Detected a console login success from an untrusted IP address (requesting user=%aws.user, requesting IP=%aws.sourceIP, AWS region=%aws.region, arn=%jevt.value[/userIdentity/arn], user agent=%jevt.value[/userAgent]) priority: info source: aws_cloudtrail
```

（向右滑动，查看更多）
```

如果知道用户“应该”从哪个IP地址登录，就可以将这些IP地址添加到trusted\_ip\_addresses列表中。这样，如果潜在的恶意用户获得了对最终用户凭据的访问权，并试图访问云环境，我们就会收到他们从未知IP访问环境的通知。

我们可以利用这些实时警报来采取主动行动，例如对帐户执行MFA或暂时关停帐户，直到我们知道用户是否合法访问它。如果用户在没有MFA的情况下成功登录，我们将触发以下规则：

```
```
- rule: Console Login Without MFA  desc: Detects a console login without MFA.  condition: >-    aws.eventName="ConsoleLogin" and not aws.errorCode exists and    jevt.value[/userIdentity/type]!="AssumedRole" and    jevt.value[/responseElements/ConsoleLogin]="Success" and    jevt.value[/additionalEventData/MFAUsed]="No"  output: >-    Detected a console login without MFA (requesting user=%aws.user, requesting    IP=%aws.sourceIP, AWS region=%aws.region)  priority: critical  source: aws_cloudtrail
```

（向右滑动，查看更多）
```

如果组织中已经实施了MFA，那无疑是最正确的决定。

然而，内部威胁或通过MFA垃圾邮件获得访问权限的高级威胁行为者，可能会考虑在创建具有完全权限的新IAM用户时禁用MFA以逃避检测。检测何时禁用或删除IAM组的MFA，将帮助平台团队防止对云提供商的不安全登录。

```
```
- rule: Azure Deactivate MFA for User Access  desc: >    Multi-factor authentication requires an individual to present a minimum of    two separate forms of authentication before access is granted. Multi-factor    authentication provides additional assurance that the individual attempting    to gain access is who they claim to be. With multi-factor authentication, an    attacker would need to compromise at least two different authentication    mechanisms, increasing the difficulty of compromise and thus reducing the risk.  condition: >-    jevt.value[/operationName]="Disable Strong Authentication" and    jevt.value[/properties/result]="success"  output: >-    Multi-factor authentication configuration has been disabled for a user    (requesting user=%jevt.value[/properties/initiatedBy/user/userPrincipalName],    requesting IP=%jevt.value[/properties/initiatedBy/user/ipAddress],    target user=%jevt.value[/properties/targetResources/0/userPrincipalName])priority: warning  source: azure_platformlogs
```

（向右滑动，查看更多）

# 检测访问控制列表的“过度许可”
```

所有云提供商都有一个类似于访问控制列表（ACL）的特性。ACL在子网级（OSI的第3层和第4层）允许或拒绝特定的入/出流量。组织可以为VPC创建一个自定义的网络ACL，其规则与安全组的规则相似，以便为VPC添加额外的安全层。

不幸的是，一些组织向公共互联网开放了这些ACL。因此，这些过度许可的ACL允许外部攻击者探测云环境。气隙/物理隔离（Air Gapping）云环境将阻止外部实体探测组织的云环境，然而，许多应用程序需要向公共互联网开放。这就是使用Falco来检测何时创建具有公共访问权限的ACL至关重要的原因所在：

```
```
- rule: Create a Network ACL Entry Allowing Ingress Open to the World  desc: >-    Detects Access Control List creation allowing ingress open to the world  condition: |    aws.eventName="CreateNetworkAclEntry" and not aws.errorCode exists and (      not (        jevt.value[/requestParameters/portRange/from]=80 and        jevt.value[/requestParameters/portRange/to]=80      ) and      not (        jevt.value[/requestParameters/portRange/from]=443 and        jevt.value[/requestParameters/portRange/to]=443      ) and      (        jevt.value[/requestParameters/cidrBlock]="0.0.0.0/0" or        jevt.value[/requestParameters/ipv6CidrBlock]="::/0"      ) and      jevt.value[/requestParameters/egress]="false" and      jevt.value[/requestParameters/ruleAction]="allow"    )  output: >-    Detected creation of ACL entry allowing ingress open to the world    (requesting user=%aws.user, requesting IP=%aws.sourceIP, AWS    region=%aws.region, arn=%jevt.value[/userIdentity/arn], network acl    id=%jevt.value[/requestParameters/networkAclId], rule    number=%jevt.value[/requestParameters/ruleNumber], from    port=%jevt.value[/requestParameters/portRange/from], to    port=%jevt.value[/requestParameters/portRange/to])  priority: error  source: aws_cloudtrail
```

（向右滑动，查看更多）
```

ACL有助于防止状态耗尽攻击。在网络层（第3层），攻击者将尝试实现SYN洪水（SYN flood）攻击。SYN flood是一种拒绝服务攻击形式，攻击者在没有结束连接的情况下快速发起到服务器的连接。然后，服务器必须花费大量的资源等待半打开的连接（作为TCP握手工作流的一部分），从而消耗大量的资源，使系统对合法的输入流量没有响应。

SYN洪水将消耗出现在大多数网络/安全设备中的TCP连接状态表，例如路由器、防火墙、入口控制器、负载平衡器，以及像Apache这样的应用服务器。锁定对网络的访问可以防止这类Dyn攻击。

# **改进Web应用防火墙配置**

使用WAF（Web应用程序防火墙）配置应用（第7层，L7）DDoS保护。这既可以通过云提供商提供的WAF技术实现，也可以通过第三方供应商实现。

就AWS云而言，它们提供了专属的WAF特性。它监视转发到L7资源的HTTP和HTTPS请求，并允许组织根据这些请求的特征控制对内容的访问。它利用ACL对来自任何单个IP地址的流量实施基于速率的规则限制。这些是DDoS保护对应用程序的要求。

就像我们在上面ACL部分提到的SYN洪水一样，HTTP/S洪水是导致DoS的一种流行攻击方法。这是由于应用程序层充斥着DNS查询造成的，这些查询由HTTP GET或POST活动组成。目标是消耗过多的应用程序资源，如内存、CPU和带宽。

从攻击者的角度来看，他们需要知道受害者基础设施中的缺陷在哪里。这些请求是否会导致数据库或应用程序处理延迟？

如果是这样，底层Web服务就会受到恶意请求的阻碍，因此无法交付给其他想要使用该服务的用户。与任何L7风格的攻击一样，了解恶意流量和正常预期流量之间的差异对于减轻威胁至关重要。

在此场景中，组织可以在云环境中的VM/EC2实例上安装Falco。基于来自主机的系统调用，我们可以看到应用程序级的流量活动。使用Falco，组织可以选择定义一个可信域名列表（sysdig.com、github.com和google.com）。与这些域名中任何一个都无法解析的IP地址的网络连接将触发该策略。

```
```
- list: trusted_domains  items: [sysdig.com, github.com, google.com]- rule: Unexpected outbound network connection  desc: Detect outbound connections with destinations not on allowed list  condition: >    Outbound    and not (fd.sip.name in (trusted_domains))  output: Unexpected Outbound Connection    (container=%container.name    command=%proc.cmdline    procpname=%proc.pname    connection=%fd.name    servername=%fd.sip.name    serverip=%fd.sip    type=%fd.type    typechar=%fd.typechar    fdlocal=%fd.lip    fdremote=%fd.rip)priority: NOTICE
```

（向右滑动，查看更多）
```

### **过滤网络流量**

创建WAF规则，根据HTTP标头、HTTP正文或客户URI等条件过滤出web请求。

同样地，ACL规则也可以通过IP地址对web流量进行过滤。与使用Falco检测ACL（对公共互联网开放）的不安全配置类似，组织可以使用Falco规则检测到通常与僵尸网络活动相关的C2服务器的连接。

```
```
- list: c2_server_ip_listitems: [1.234.21.73, 100.16.107.117, 100.6.8.7]
- rule: Outbound Connection to C2 Serversdesc: Detect outbound connection to command & control serverscondition: outbound and fd.sip in (c2_server_ip_list)output: Outbound connection to C2 server (command=%proc.cmdline pid=%proc.pid connection=%fd.name user=%user.name user_loginuid=%user.loginuid container_id=%container.id image=%container.image.repository)priority: WARNINGtags: [network]
```

（向右滑动，查看更多）
```

当然，组织可以使用任何想要的威胁信号。我们基于Feodo Tracker C2 IP Blocklist中的前三个IP地址创建了c2\_server\_ip\_list。

Abuse.ch的团队提供了一个简单的UI来过滤这些IP，以更好地了解它们如何用于各种攻击技术，如木马加载程序、勒索软件和拒绝服务。

与检测到C2服务器的可疑出站流量类似，我们还希望检测到云服务的可疑入站流量：

```
```
- rule: AWS Suspicious IP Inbound Request  desc: >-    Detect inbound requests from known suspicious IP sources, such as TOR exit    nodes, to AWS services.  condition: >-    aws.sourceIP in (ti_anon_ips) and not (aws.eventName="ConsoleLogin" and    jevt.v...