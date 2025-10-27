---
title: SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据的黑客活动
url: https://www.4hou.com/posts/r7PK
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-02
fetch_date: 2025-10-04T08:23:56.176387
---

# SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据的黑客活动

SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据的黑客活动 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据的黑客活动

布加迪
[新闻](https://www.4hou.com/category/news)
2023-03-01 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)176200

收藏

导语：Sysdig威胁研究团队最近在客户环境中发现了一起导致专有数据被盗的复杂云活动：SCARLETEEL。攻击者利用容器化的工作负载将特权升级到AWS帐户，以便盗取专有软件和凭据。

Sysdig威胁研究团队最近在客户环境中发现了一起导致专有数据被盗的复杂云活动：SCARLETEEL。攻击者利用容器化的工作负载将特权升级到AWS帐户，以便盗取专有软件和凭据。他们还企图使用Terraform状态文件转而攻击其他连接的AWS帐户，以便在整个组织中横向移动。

这次攻击比大多数攻击来得复杂，原因是它从受攻击的Kubernetes容器开始传播到受害者的AWS帐户。攻击者还了解AWS云机制，比如弹性计算云（EC2）角色、Lambda无服务器函数和Terraform。最终结果不是一起典型的加密货币劫持攻击。攻击者还有其他更阴险的动机：盗取专有软件。

在去年，云端网络攻击猛增了56%。最常见的动机是在云端获得持久性、窃取敏感数据以及创建用于挖掘加密货币的EC2实例等新资源。这些资源可能会对组织的云账单产生严重影响。但更多侧重间谍活动的动机也依然存在。实际上，攻击者可以利用云资源从事挖掘加密货币之外的勾当。

我们看到的这起复杂攻击涉及多方面，这表明了保护基于云的基础设施的复杂性。单凭漏洞管理解决不了所有问题。有许多工具可以降低来自高级威胁的风险，包括虚拟机、云安全态势管理（CSPM）、云基础设施授权管理（CIEM）、运行时威胁检测和密文管理。

**概述**

这张信息图显示了杀伤链的主要步骤。不妨先显示攻击的概貌，然后更详细地介绍每个步骤。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230301/1677631644155914.png "1677631644155914.png")

图1

第1步：攻击者利用托管在AWS云帐户内的自管理Kubernetes集群中面向公众的服务获得初始访问权。

第2步：一旦攻击者获得了pod的访问权，恶意软件就能够在执行过程中执行两个初始操作：

启动加密货币挖掘软件，以便牟利或分散注意力。

通过实例元数据服务（IMDS）v1中worker的临时凭据获得凭据访问权，使用集群角色权限代表worker枚举和收集信息。由于授予的权限过大，攻击者能够：

1）枚举AWS资源。

2）找到其他身份和访问管理（IAM）用户的凭据，它们被设置为Lambda环境变量，并以明文形式推送到亚马逊S3存储桶中。

第3步：攻击者使用前一步中发现的凭据来横向移动。他们直接联系AWS API，进一步枚举帐户，进而收集信息和泄露数据。他们在这一步中能够：

1）禁用CloudTrail日志以逃避检测。

2）盗取专有软件。

3）通过发现S3存储桶中的Terrraform状态文件，找到与不同AWS帐户相关的IAM用户的凭据。

第4步：攻击者使用新的凭据再次横向移动，从他们发现的其他AWS帐户重复攻击和杀伤链。幸好他们无法枚举资源，因为他们尝试的所有AWS API请求都因缺乏权限而失败。

**技术分析**

**初始访问——容器受攻击**

攻击者发现并利用了一项暴露在互联网面前的服务，它部署在Kubernetes集群中。一旦他们访问了容器，开始执行不同的操作以发动攻击。

第一个操作是下载和启动挖币软件，以窃取一些内存周期。这是自动化容器威胁的常见伎俩。攻击者启动了脚本miner.sh，以便运行一个XMRig可执行文件以及挖币软件配置文件config\_background.json。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230301/1677631679143073.png "1677631679143073.png")

图2

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230301/1677631689202702.png "1677631689202702.png")

图3

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230301/1677631701156459.png "1677631701156459.png")

图4

然而，攻击的目的绝不单单是挖币。挖币是攻击者的最初目标，一旦他们访问了受害者的环境，目标就随之改变，或者挖币被用作逃避数据泄露检测的手段。在安装挖币软件期间，我们观察到容器上同时运行一个bash脚本，以枚举和提取环境中的额外信息，比如凭据。

为了找到凭据，攻击者直接访问IMDS。IMDS v1是在AWS中创建自管理集群或EC2实例的旧版本时默认使用的版本，它用于配置和管理机器。

从IMDS v1检索绑定到EC2实例角色的AWS临时安全凭据是一种很常见的做法。攻击者可能发现IAM角色绑定到运行以下代码的worker实例：

role\_name=$(curl http://169.254.169.254/latest/meta-data/iam/security-credentials/)

然后获取AccessKeyId、SecretAccessKey和临时令牌：

metadata\_content=$(curl http://169.254.169.254/latest/meta-data/iam/security-credentials/$role\_name)

查看对IMDS v1的恶意请求，我们还发现了对一个不太为人所知的内部端点（“仅限内部使用”）的请求，AWS文档有解释（https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instancedata-data-categories.html）。

metadata\_content=$(curl http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance)

下面屏幕截图显示了攻击者如何攻击实例元数据端点以及恶意脚本执行了哪些命令来grep和检索IAM角色密钥。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230301/1677631734185428.png "1677631734185428.png")

图5

一旦收集完毕，就可以在短时间内使用这些凭据，以便代表被冒充的IAM角色运行操作，直接调用AWS API。使用CloudTrail日志，你可以看到来自使用集群角色的攻击者的第一个API调用：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230301/1677631752122828.png "1677631752122828.png")

图6

攻击者运行一些AWS操作在AWS平台上获得持久性，试图创建新的用户/组，并将新的访问密钥绑定到现有IAM用户。幸好，由于攻击者使用的帐户缺乏权限，所有这些执行都被拒绝了。

不幸的是，AWS集群角色错误配置，拥有过大的读取权限。本意是允许读取特定的S3存储桶，但权限允许角色读取帐户中的一切，这使攻击者得以进一步了解AWS帐户，包括Lambda。

**发现——AWS云**

一旦攻击者获得对云帐户的初始访问权，就开始收集关于部署在AWS帐户中的资源的信息。下表中报告的活动只是AWS帐户中记录的部分API请求。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230301/1677631768846477.png "1677631768846477.png")

图7

在这些收集活动期间，攻击者将目光放在最常用的AWS服务上：无服务器Lambda函数和S3存储桶。

**Lambda函数枚举——盗取专有代码和软件**

Lambda函数及其他无服务器函数常用于执行自定义代码，无需担心底层基础设施，这给了最终用户很大的灵活性。

受影响的AWS帐户中有不同的Lambda函数，主要与帐户自动化有关。

攻击者开始使用适当的API调用枚举和检索位于AWS帐户中特定区域的所有Lambda函数。比如说，你可以使用以下的AWS命令列出函数。说白了，它就是REST API调用，因此有许多方法来完成这个任务。

**aws lambda list-functions**

在获得函数列表后，攻击者试图通过下载Lambda代码来深入挖掘。他们调用下面的AWS API，获得了代码位置，从而可以下载组成Lambda的代码。在本例中，Lambda函数拥有专有软件及执行软件所需的密钥。

aws lambda get-function --function-name $function\_name --query 'Code.Location'

使用curl或wget命令，攻击者成功盗取了Lambda代码，并从Lambda函数盗取了专有代码和软件。还有证据表明攻击者执行了盗取的软件。

攻击者花时间查看Lambda函数的环境变量，使用类似以下的命令，找到了同一帐户中与IAM用户相关的其他AWS凭据：

aws lambda list-versions-by-function --function-name $function\_name

正如你在攻击下几步中看到的那样，攻击者使用这里找到的凭据对新用户重试枚举，希望有新的发现或评估帐户内部可能的特权升级。

**S3存储桶枚举**

亚马逊S3是一种非常流行的存储服务，允许用户存储和检索数据。

攻击者常常攻击存储在S3存储桶中的资源和文件，以提取信息和凭据。在过去，许多攻击利用了配置错误的S3存储桶或没有密码或安全措施就向公众敞开的S3存储桶。在这次攻击中，攻击者能够检索和读取超过1Tb的信息，包括客户脚本、故障排除工具和日志文件。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230301/1677631807153871.png "1677631807153871.png")

图8

CloudTrail并不记录存储在S3存储桶中的对象的数据事件，除非明确请求此类功能。在本例中，该功能没有开启，因此无法查看有关访问特定对象的信息。但是我们可以肯定攻击者遍历了存储桶、寻找敏感数据。为了在不消耗可用存储的情况下加快搜索速度，他们可能使用了TruffleHog等工具，立即获得新的AWS用户凭据，并继续在集群中横向移动。

1 TB的数据还包括与Terraform相关的日志文件，Terraform在帐户中用于部署部分基础设施。这些Terraform文件将在攻击者试图转移到另一个AWS帐户的后续步骤中发挥重要作用。

**防御逃避——禁用CloudTrail日志**

一旦攻击者访问了云帐户，试图禁用受攻击帐户中的CloudTrail日志。从下面截图中可见，由于前几个步骤中其中一个受攻击的用户被分配了额外权限，攻击者成功禁用了帐户中配置的一些日志。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230301/1677631825100753.png "1677631825100753.png")

图9

由于该操作，我们无法检索另外的攻击证据。在审查帐户权限时，将禁用或删除安全日志的功能留给尽可能少的用户至关重要。

**凭据访问——Terrraform状态文件**

Terraform是一个开源基础设施即代码（IaC）工具，用于在云环境中部署、更改或创建基础设施。

为了让Terraform知道哪些资源归它控制、以及何时更新和销毁资源，它默认使用了名为terraform.tfstate的状态文件。当Terraform在持续集成/持续交付（CI/CD）管道中被集成和自动化时，要有适当的权限才能访问状态文件。尤其是，运行管道的服务主体需要能够访问保存状态文件的存储帐户容器。这使得像亚马逊S3存储桶这样的共享存储成为保存状态文件的理想选择。

然而，Terraform状态文件以明本形式保管所有数据，这可能包含密文。将密文存储在安全位置以外的任何地方不是好主意，绝不应该放在源代码控制系统中！

攻击者能够列出可用的存储桶，并检索所有数据。若在事件调查期间使用不同的工具（比如Pacu和TruffleHog）分析数据，可以在S3存储桶中的terraform.tfstate中同时找到明文IAM用户访问密钥和密文密钥。以下是来自TruffleHog的截图。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230301/1677631848124218.png "1677631848124218.png")

图10

这些IAM凭据属于第二个连接的AWS帐户，从而使攻击者有机会横向移动，在整个组织中传播攻击。

**横向移动——AWS帐户**

获得新凭据后，攻击者重新启动枚举和信息收集过程，以确定是否可以从这个额外的受攻击帐户获得额外的资源。此外，CloudTrail记录了上述的连接AWS帐户中的可疑活动。

攻击者试图对连接云帐户中的不同AWS资源执行枚举。幸好IAM用户被界定了明确范围，所以所有请求因缺乏权限而失败，只留下无害的GetCallerIdentity API，它默认被允许。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230301/1677631860118868.png "1677631860118868.png")

图11

**建议**

本文阐述的攻击清楚地表明威胁分子如何将试图到达云作为主要目的。这一切始于一项受攻击的服务，不过攻击者一旦获得了有效凭据就试图在云端横向移动，找到专有代码等有价值的信息。他们还试图转向其他云帐户以获得更多的信息。

以下是可以帮助你更谨小慎微的几个建议：

对你的应用程序和面向公众的容器运用漏洞管理周期，及时打上补丁。你会意识到暴露了什么，可以按轻重缓急处理修补活动。

使用IMDS v2，而不是IMDS v1。增强版需要面向会话的请求以增强深度防御，以防范未经授权的元数据访问。此外，为了确保只有授权的pod才能在集群中承担特定的IAM角色，尽可能采用最小权限原则，并使用服务帐户IAM角色（IRSA）。IRSA限制了对资源的访问，降低了未授权访问的风险。未授权的pod将坚持使用IMDS设置。

不要低估只读访问的功效。面对特定的AWS资源（比如Lambda函数），即使只读也意味着数据泄露或凭据收集。仅对所需资源设置只读访问范围是保证帐...