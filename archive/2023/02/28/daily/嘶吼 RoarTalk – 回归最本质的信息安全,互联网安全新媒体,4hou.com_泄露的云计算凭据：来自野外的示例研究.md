---
title: 泄露的云计算凭据：来自野外的示例研究
url: https://www.4hou.com/posts/QLD0
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-28
fetch_date: 2025-10-04T08:14:06.537486
---

# 泄露的云计算凭据：来自野外的示例研究

泄露的云计算凭据：来自野外的示例研究 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 泄露的云计算凭据：来自野外的示例研究

lucywang
[技术](https://www.4hou.com/category/technology)
2023-02-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)124091

收藏

导语：本文重点介绍了两个云计算凭据被攻击的示例。

![Cloud-21-illustration_orange.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230119/1674101820800381.png "1674101021111474.png")

云泄露通常源于配置错误的存储服务或暴露的凭据，越来越多的攻击专门针对云计算服务，以窃取相关凭据并非法访问云基础设施。这些攻击的目的就是使目标组织付出经济或其他方面的代价。

本文重点介绍了两个云计算凭据被攻击的示例。虽然初始访问阶段很重要，但我们将重点关注攻击期间执行的攻击后操作，并分享这两种针对云基础设施的攻击流程。攻击流程显示了攻击者如何滥用窃取的计算凭据来寻找各种攻击方法(如加密挖掘、数据窃取等)，并以意想不到的方式滥用云服务。

为了检测下面描述的攻击，由Amazon Web Services (AWS)和Google cloud概述的云日志记录和监控最佳实践是必不可少的，因为它们提供了对云基础设施级别活动的可见性。这强调了遵循Amazon Web Services和Google Cloud日志记录和监控最佳实践的重要性。

Palo Alto Networks通过Cortex XDR for cloud和Prisma cloud帮助组织解决云安全问题，Cortex XDR for cloud可检测云计算凭据被盗等云攻击，Prisma cloud以最少的权限管理身份授权。

**云工作的关键原则**

在深入研究之前，我们应该了解在云计算中工作的一个非常基本和重要的规则。实体(无论是人还是计算工作负载)都需要合法和相关的凭据才能在基础设施级访问云环境。凭据用于身份验证(验证实体的标识)和授权(验证实体被允许做什么)。

作为一种最佳实践，当计算工作负载在云中执行API调用(例如，查询存储服务)时，工作负载的相关凭据应该仅专用于它。它们还应该仅供该工作负载或人员使用，而不能供其他任何人使用。

正如我们将在这两个示例中看到的，有助于降低云计算凭据攻击风险的一个重要安全原则是最低权限访问。特别是，这意味着与这些凭据相关联的权限应该缩小到使用它们的代码实际所需的最小权限集。这限制了攻击者在计算凭据被盗用时可以采取的行动。

**攻击示例1：AWS Lambda凭据受攻击导致网络钓鱼攻击**

攻击者可以通过窃取Lambda的凭据来执行代表Lambda函数的API调用，这允许攻击者可以在云环境中执行多个API调用并枚举不同的服务，如下图所示。虽然由于缺乏权限，大多数API调用都不被允许，但该攻击导致了由攻击者创建的AWS简单电子邮件服务（SES）发起的网络钓鱼攻击。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230119/1674101821958486.png "1674101039411963.png")

攻击者使用受攻击的Lambda函数的凭据枚举云环境

这种网络钓鱼攻击不仅给组织带来了意想不到的成本，也使其他组织面临额外的风险。

在本示例中，受害者没有活跃的SES，如果有，攻击者可能会滥用它来对受害者的组织发起攻击，或者他们甚至可以使用合法的电子邮件帐户进行网络钓鱼攻击。

由于组织使用的云服务种类繁多，因此很难预测云攻击将在何处结束。从云计算到网络钓鱼并不是只有一个实现方法。

**攻击流**

攻击者能够窃取Lambda的环境变量并将它们导出到攻击设备(AWS\_ACCESS\_KEY\_ID, AWS\_SECRET\_ACCESS\_KEY, AWS\_SESSION\_TOKEN)。

当凭据被窃取后，攻击者通过以下步骤发起攻击：

**WHOAMI - 2022-05-20T20:35:49 UTC**

攻击从GetCallerIdentity命令开始，该命令相当于whoami，因为它提供了与凭据相关联的实体的信息。从响应中，攻击者可以获得其他信息，例如被盗的帐户ID和凭据类型。但是，它们不能确定与身份相关联的任何权限。

**IAM枚举- 2022-05-20T20:35:55 UTC**

攻击的下一个阶段是身份和访问管理(IAM)枚举，IAM被认为是攻击的最佳途径。通过获得对IAM的访问权，攻击者可以提升权限并获得受害者帐户的持久性。

IAM枚举包括两个API调用，由于缺乏权限而被拒绝：

ListAttachedRolePolicies

ListRolePolicies

可以假设，攻击者注意到缺少权限，因此仅在两个命令后终止IAM枚举（可能是为了避免产生不必要的噪音）。

**通用枚举2022-05-20T20:39:59 UTC**

在枚举IAM失败后，攻击者开始对不同区域的不同服务进行枚举。这种技术的噪音很大，因为攻击者试图了解目标帐户的体系结构，更重要的是，获得可能存在于云帐户中的敏感信息的访问权。

执行的一些主要服务和API调用包括：

存储枚举

```
ListBucketsGetBucketCorsGetBucketInventoryConfigurationGetBucketPublicAccessBlockGetBucketMetricsConfigurationGetBucketPolicyGetBucketTagging
```

EC2枚举

```
GetConsoleScreenshotGetLaunchTemplateDataDescribeInstanceTypesDescribeBundleTasksDescribeInstanceAttributeDescribeReplaceRootVolumeTasks
```

网络枚举

```
DescribeCarrierGatewaysDescribeVpcEndpointConnectionNotificationsDescribeTransitGatewayMulticastDomainsDescribeClientVpnRoutesDescribeDhcpOptionsGetTransitGatewayRouteTableAssociations
```

日志记录枚举

```
GetQueryResultsGetBucketLoggingGetLogRecordGetFlowLogsIntegrationTemplateDescribeLogGroupsDescribeLogStreamsDescribeFlowLogsDescribeSubscriptionFiltersListTagsLogGroup
```

备份枚举

```
GetPasswordDataGetEbsEncryptionByDefaultGetEbsDefaultKmsKeyIdGetBucketReplicationDescribeVolumesDescribeVolumesModificationsDescribeSnapshotAttributeDescribeSnapshotTierStatusDescribeImages
```

SES枚举

```
GetAccountListIdentities
```

通用枚举

```
DescribeRegionsDescribeAvailabilityZonesDescribeAccountAttributes
```

**后门2022-05-20T20:43:22 UTC**

在枚举IAM失败时，攻击者试图通过执行CreateUser命令创建一个新用户(未成功)。

**从云计算到网络钓鱼攻击2022-05-20T20:44:40 UTC**

由于枚举期间的大多数API调用导致权限被拒绝，因此攻击者能够成功枚举SES。因此，攻击者通过滥用云电子邮件服务发起了钓鱼攻击，其中包括执行VerifyEmailIdentity和UpdateAccountSendingEnabled等命令。

**逃避检测2022-05-20T23:07:06 UTC**

最后，攻击者试图通过执行DeleteIdentity命令删除SES标识来隐藏他的一些活动。

**其他情况分析**

此攻击的一个非常重要的攻击指标（IoC）是IP地址50.82.94[.]112。

来自Lambda函数的API调用通常使用为Lambda生成的凭据（包括AccessKeyId）从其IP执行。因此，具有该AccessKeyId的每个API调用都被认为是Lambda函数。然而，在攻击过程中，攻击者能够窃取Lambda的凭据，从而允许攻击者冒充Lambda。

因此，IP是关键的IoC，因为它是检测冒充Lambda的方法。攻击者使用窃取的凭据来模拟和执行代表Lambda函数的API调用，但是他们是从一个未连接到Lambda的IP地址执行的，该IP地址也不属于云环境。

**攻击示例2：部署加密挖矿的Google Cloud应用程序引擎服务帐户受攻击**

攻击者能够窃取Google Cloud应用程序引擎服务帐户(SA)的凭据，攻击者有许多方法可以实现这一点，这些方法不一定与云服务提供商中的任何漏洞有关。例如，在许多示例中，用户将凭据存储在不安全的位置，或者使用容易猜到或强行设置的密码。

在本示例中，被盗窃的SA是默认SA，它具有高权限的角色(项目编辑器)。这允许攻击者发起攻击，最终创建了多个用于加密挖掘的核心CPU虚拟机（VM），如下图所示。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230119/1674101822166930.png "1674101634131586.png")

攻击者滥用受攻击的App Engine SA来分配多个云示例进行窃取攻击

当攻击者在受害者的环境中启动数千个虚拟机时，将显著增加其预期成本。即使有人在短时间内注意到在他们的环境中发生了这样的攻击，它仍然会产生严重的攻击后果。

**攻击流**

谷歌应用引擎是Google Cloud完全管理的无服务器平台，服务账户是令牌。当用户创建一个App Engine示例时，云提供商创建一个默认SA，并将其附加到创建的App Engine上。

此应用程序引擎默认SA在项目中具有编辑功能。编辑器具有很高权限，这是攻击者能够发起攻击的关键，编辑器允许执行高权限的API调用，例如：

启动计算工作负载；

FW (Firewall)规则修改；

创建SA密钥；

**权限升级2022-06-16T12:21:17.624 UTC**

这次攻击一开始是为了升级权限。如上所述，默认情况下，应用程序引擎的SA对项目具有编辑权限。凭借这些权限，攻击者试图通过将以下对象添加到IAM策略中来添加计算/管理功能：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230119/1674101823158109.png "1674101172149196.png")

正如我们所看到的，SA域前缀中的appspot表示该SA属于App Engine服务。

**允许任何2022-06-16T12:21:29.406 UTC**

接下来，攻击者修改了项目级别的FW规则。首先，攻击者试图创建一个子网（名为default）。然后，攻击者将以下规则添加到该子网中：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230119/1674101824146609.png "1674101184124888.png")

此操作进一步推进了攻击者挖掘加密货币的目标，为了实现无限制的加密货币挖掘，攻击者删除了对网络级别的任何限制。

注意优先级字段是很重要的。通过将其设置为零，攻击者的规则被设置为最高优先级，这意味着它将按照现有FW规则的顺序首先生效。

**挖矿攻击2022-06-16T12:21:38.916 UTC**

安装完成后，攻击的主要阶段就开始了，在多个区域启动虚拟机。

虽然攻击者可以创建高CPU设备，但在本示例中，攻击者反而创建了一个配备了四个高性能GPU(例如nvidia-tesla-p100)的标准虚拟机(例如n1-standard-2)：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230119/1674101825425387.png "1674101197885807.png")

总的来说，在这次攻击中创建了超过1600个虚拟机。

**后门2022-06-16T13:25:56.037 UTC**

攻击者假设用于攻击的SA密钥会被检测到并被删除，因此通过执行google.iam.admin.v1.CreateServiceAccountKey API调用创建了多个SA密钥供以后使用。

**其他情况分析**

就像我们讨论的第一个示例一样，IP是一个重要的IoC。在这种情况下，攻击是从多个IP（总共九个不同的IP）发起的，其中一些是活动的Tor出口节点。

同样，我们希望从云环境中的IP使用App Engine的SA，它绝对不应该从Tor出口节点使用。

修改防火墙规则是此类攻击中常用的技术，许多组织强制执行拒绝访问活动挖矿池的网络流量规则，因此攻击者必须修改防火墙规则来实现他们的目标。

最后，通过编辑名为default的网络，攻击者试图逃避检测。除非禁用此选项，否则默认情况下，将使用默认网络创建每个新项目。攻击者似乎试图利用这一点，从而避免创建自己的网络。

**总结：窃取计算令牌是一个日益严重的威胁**

窃取计算工作负载的令牌是上述两个攻击示例的共同点，虽然上述两个示例都涉及无服务器服务，但此攻击向量与所有计算服务都相关。

需要强调的是，这种类型的攻击可能来自不同的攻击路径，包括应用程序漏洞或零日漏洞(如Log4Shell)，而不仅仅来自错误配置或糟糕的云安全态势管理(CSPM)。

为了处理此类攻击，云审计日志对于检测和调查与响应(IR)都至关重要。对于无法安装代理的无服务器工作负载，云审计监控更为关键，因此更难阻止此类攻击。

AWS和Google Cloud提供的日志记录和监控最佳实践为如何防止此类情况提供了明确的指导。AWS GuardDuty服务还可以帮助检测和警告类似的攻击，例如从另一个AWS帐户使用的EC2示例凭据。另一种预防方法是为Lambda配置接口端点策略，限制Lambda仅在VPC内使用。

**Palo Alto Networks的用户可以通过以下方式免受计算令牌盗窃**

Cortex XDR for cloud，通过将来自云主机、云流量和审计日志的活动与端点和网络数据集成，为安全团队还原完整事件过程。

Prisma Cloud帮助组织管理身份授权，解决了在云环境中管理IAM的安全挑战。Prisma Cloud IAM安全功能自动计算跨云服务提供商的有效权限，检测过度许可的访问，并建议奖权限降到最低。

了解如何使用Unit 42云事件响应服务(用于调查和响应攻击)和网络风险管理服务(用...