---
title: SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据
url: http://blog.nsfocus.net/scarleteelterraformkubernetes/
source: 绿盟科技技术博客
date: 2023-05-06
fetch_date: 2025-10-04T11:40:40.310398
---

# SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据

### SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据

[2023-05-05](https://blog.nsfocus.net/scarleteelterraformkubernetes/ "SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据")[李来冰](https://blog.nsfocus.net/author/lilaibing/ "View all posts by 李来冰")[AWS](https://blog.nsfocus.net/tag/aws/), [云服务利用](https://blog.nsfocus.net/tag/%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%88%A9%E7%94%A8/), [公有云攻防](https://blog.nsfocus.net/tag/%E5%85%AC%E6%9C%89%E4%BA%91%E6%94%BB%E9%98%B2/)

阅读： 1,330

## **一、******引言****

根据Sophos安全公司在《The Reality of SMB Cloud Security in 2022》[1]中指出，在过去的2022一年里，发生在云上的网络攻击增加了56%。在云端获得持久性、窃取敏感数据和创建资源进行恶意挖矿是几个最常见的动机。这些攻击活动不仅是利用云服务资源进行获利，还包括一些间谍活动。

本文主要解读了由Sysdig威胁研究团队公开的一起云上攻击活动[2]，由于攻击过程复杂且较为典型，希望能够分享其中的技术细节，带大家了解真实的云上攻击事件。

文中涉及到的技术仅供教学、研究使用，禁止用于非法用途。

## **二、******攻击链概述****

该攻击活动发生在Sysdig的一个客户环境，被取名为SCARLETEEL。攻击者利用一个容器化的工作负载获得初始访问权限，通过一些手段进行权限提升和横向移动，使得影响扩大至客户的AWS账户，大致攻击链如图1所示：

![](https://blog.nsfocus.net/wp-content/uploads/2023/05/wps_doc_0-1-300x113.png)

图1 SCARLETEEL攻击链

步骤1：攻击者利用托管在AWS云账户中的Kubernetes集群获得初始访问权限

步骤2：获得集群Pod的访问权限后，攻击者可以进行以下两种操作：

1. 启动一个加密货币挖掘软件，以谋取利益
2. 利用实例元数据服务获取临时凭证权限，利用集群角色权限收集信息。由于授予的权限过大，导致攻击者可以：
   * 枚举AWS资源
   * 从Lambda和S3服务中获取其他IAM用户的凭证

步骤3：利用步骤2中获取的凭证进行横向移动，可通过AWS API获取更多账户相关信息：

1. 停用CloudTrail日志以绕过检测
2. 窃取专利数据
3. 通过S3存储桶中的Terraform状态文件，寻找其他IAM用户凭证

步骤4：利用新的凭证重复步骤3中的横向移动行为，但因缺乏权限而尝试失败

## **三、******技术分析****

### ****初始访问——攻击容器应用****

攻击者利用暴露在公网上的服务获得初始访问权限，发现该业务运行在Kubernetes集群中。容器作为一个受限的隔离环境，并非攻击者的最终目的，攻击者容器环境中进行了两个攻击操作：

1. 在当前环境中下载和启动挖币软件。但是挖币只是攻击者的最初目标或者作为窃取数据行为的“障眼法”，一旦可以继续扩大战果，攻击的目标也就随之改变。
2. 因此攻击者尝试利用IMDS（Instance Metadata Service）服务进行权限提升。

IMDS即实例元数据服务，它是AWS实例上的组件，在实例上进行编码，用于安全访问实例元数据。利用元数据服务获取临时凭据是一种常见的攻击思路，不同的云厂商所对应的元数据服务地址不同，其中AWS的元数据服务接口如下：

// 获取IAM信息

<http://169.254.169.254/latest/meta-data/iam/info>

// 获取IAM凭证信息，包括AccessKeyId、SecretAccessKey和临时令牌

[http://169.254.169.254/latest/meta-data/iam/security-credentials/<rolename](http://169.254.169.254/latest/meta-data/iam/security-credentials/%3Crolename)>

在获取凭证信息之后，可以使用aws-cli工具控制aws云服务资源。但是利用AWS API的调用请求会在AWS CloudTrail服务上留下日志。AWS CloudTrail是一项安全服务，能够记录、持续监控和保留与整个AWS网络服务基础设施的行为有关的账户活动，包括AWS管理控制台、AWS SDK、命令行工具和其他AWS网络服务服务采取的行动。如图2所示，Sysdig通过查看CloudTrail日志可了解攻击者的攻击操作：

![](https://blog.nsfocus.net/wp-content/uploads/2023/05/wps_doc_1-1-300x153.png)

图2 CloudTrail日志

由图可知，由于IAM角色权限有限，类似“CreateGroup“、”CreateUser“等敏感操作都被拒绝。AWS的IAM权限模型采用的是ABAC，即基于属性的访问控制（ABAC），它基于属性来定义权限。在实际操作中，这些属性也叫做标签，通过在权限策略中的添加标签字段，实现对资源的动态权限管理。但不论是AWS的ABAC，还是Azure的RBAC，一般云厂商的权限逻辑都认为拒绝操作优先于允许操作，因此合理分配IAM角色权限，可以很大程度地减小实例沦陷后的危害。

但不幸的是，此次事件中由于IAM角色配置不当，攻击者可以获取较多的信息。

### ****发现——********AWS****

常见AWS云服务资源的信息收集思路，主要包括以下几种方式：

1. 在Lambda函数代码和环境变量中收集信息：函数代码和环境变量中可能包含其他IAM角色的凭证信息，使得攻击者获取更高权限。
2. 在ECS Task Definitions中收集信息：ECS Task Definition中包含容器在启动时运行的命令信息、租户运行任务时使用的IAM 角色信息等。
3. 在S3存储桶中收集信息：S3是 AWS的对象存储服务，从过去发生的一些S3存储桶数据泄露事件中可知，用户可能会利用S3存储一些敏感信息，包括敏感凭证、日志文件等，都可能为攻击者提供辅助。

主要思路是在一切可存储数据、可查看配置的云服务资源中获取信息。

此次事件中攻击者利用了Lambda函数和S3存储桶服务。通过已有权限查看Lambda函数列表、下载函数代码，最终窃取了客户的专有软件代码以及专有密钥，造成了知识产权的损失。

针对S3存储桶需要说明的是：CloudTrail并不记录存储在S3存储桶中的对象的数据事件，除非明确开启此类功能。在此次攻击事件中，该功能并没有开启，因此并没有记录下查看特定对象的请求信息，仅有列举存储桶列表的日志记录，如图3所示：

![](https://blog.nsfocus.net/wp-content/uploads/2023/05/wps_doc_2-1-300x57.png)

图3 CloudTrail日志中列出存储桶操作记录

但Sysdig断定攻击者遍历了存储桶用以寻找敏感数据，因为该存储桶中的Terraform相关文件信息在后续攻击步骤中被利用。

### ****防御绕过——禁用Cloud********Trail********日志****

由于CloudTrail服务会记录下大部分AWS账户日志，因此在攻击AWS时攻击者往往会考虑绕过该服务的检测。在考虑如何规避CloudTrail时，需要先了解清楚该服务的运行详情。

通过查看AWS官方文档了解到，CloudTrail服务是默认启用的，AWS用户可以免费查看最近90天的事件记录。通过以下命令可以查看CloudTrail的监视范围，结果如图4所示：

aws cloudtrail describe-trails

![](https://blog.nsfocus.net/wp-content/uploads/2023/05/wps_doc_3-1-300x149.png)

图4 CloudTrail监控配置

其中“IsMultiRegionTrail”字段代表是否将监视所有区域，true代表是，false代表仅监视单区域；“S3BucketName”代表将CloudTrail日志写入S3存储桶。

然后了解到常见的绕过方式主要有以下几种[3]：

* 中止CloudTrail服务

使用以下命令中止日志记录：

aws cloudtrail stop-logging –name awscloudtrail-example

当完成攻击后，重新启动日志服务：

aws cloudtrail start-logging –name awscloudtrail-example

* 删除CloudTrail服务

删除trails或者删除存储日志的存储桶

aws cloudtrail delete-trail –name awscloudtrail-example

但是此种方法较为“高调”，会使CloudTrail服务处于宕机状态，同时删除存储桶后在管理控制台弹窗提示，如图5所示：

![](https://blog.nsfocus.net/wp-content/uploads/2023/05/wps_doc_4-1-300x101.png)

图5 CloudTrail控制台弹窗

同时AWS的另一个监控服务GuardDuty也会对CloudTrail服务的异常状态发出警报，因此并非攻击者的首选。

* 区域绕过

当CloudTrail服务仅监视个别区域时，可以在监视区外的区域对实例进行操作，绕过监控；或者利用include-global-service-events标签关闭全球服务，命令如下：

aws cloudtrail update-trail –name my-trail –no-include-global-service-events

此次攻击活动中，攻击者采用了第一种方案进行规避，为调查取证提供了阻碍。在实际给应用程序分配IAM角色时，禁用或删除安全日志的权限对于程序来说不必要的，因此说明了合理分配权限与权限审查的重要性。

### ****凭据访问——********Terraform状态文件****

Terraform是一个开源的基础设施即代码（IaC）工具，用于部署、改变或创建云环境中的基础设施。

为了让Terraform知道哪些资源在其控制之下，以及何时更新和销毁它们，它默认使用一个名为terraform.tfstate的状态文件。当Terraform在持续集成/持续交付（CI/CD）管道中被集成和自动化时，该状态文件需要以适当的权限被访问。特别是，运行管道的服务主体需要能够访问保存状态文件的存储账户容器。这使得像AWS S3这样的共享存储成为保存状态文件的完美候选。

然而，Terraform状态文件中可能包含凭证信息。

在上述攻击步骤中，攻击者有权限列出可用的存储桶并检索所有的数据。在事件调查期间，Sysdig尝试用不同的工具来检索数据，验证了在S3存储桶内的terraform.tfstate文件中可以找到明文IAM用户凭证信息，如图6所示：

![](https://blog.nsfocus.net/wp-content/uploads/2023/05/wps_doc_5-1-300x68.png)

图6 S3存储桶中的terraform.tfstate文件

### ****横向移动——********AWS帐户****

通过上述手段获得新凭证后，攻击者重复信息收集和横向移动操作，尝试以新凭证权限获得额外的资源。但后续的操作并没有主动规避CloudTrail服务的意识，导致CloudTrail记录了新凭证对应的可疑活动，如图7所示：

![](https://blog.nsfocus.net/wp-content/uploads/2023/05/wps_doc_6-1-300x153.png)

图7 CloudTrail记录了新凭证的攻击行为

由图可知，攻击者尝试了“ListGroups”、“ListUsers”、“AttachUserPolicy”等操作，但都因缺乏权限而失败。

## ****五、总结与思考****

SCARLETEEL事件始于一个易受攻击的Pod，攻击者通过信息收集获取到了AWS IAM用户凭证信息，从而横向移动至Lambda服务、S3存储桶服务，最终窃取了客户的专有软件。

从Sysdig调查分析的攻击行为来看，此次事件涉及的云上攻击者的攻击思路较为灵活，基本包括了常见的攻击技术并能够应用至攻击活动中，但在过程中也难免会“存在疏忽”导致留下更多痕迹。

该攻击活动真实地说明了，网络安全是一项复杂的系统工程，每个环节都应做到最佳防护，防止出现“牵一发而动全身”的影响。尤其是此次攻击活动中最为突出的两个问题：最小权限原则和威胁检测机制。若在分配角色权限过程中能够遵循最小化原则并定期进行权限审查，攻击者难以横跨至云服务资源中从而获取更多信息，也难以绕过日志监控系统，可能会留下更多的攻击痕迹。而强大的威胁检测机制则可以在攻击者进一步深入之前给出警报信息，帮助客户及时止损。

## ****参考文献****

1. https://news.sophos.com/en-us/2022/11/29/the-reality-of-smb-cloud-security-in-2022/
2. <https://sysdig.com/blog/cloud-breach-terraform-data-theft/>
3. https://rzepsky.medium.com/playing-with-cloudgoat-part-2-fooling-cloudtrail-and-getting-persistence-access-6a1257bb3f7c

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/api/)

[Next](https://blog.nsfocus.net/linux-overlayfscve-2023-0386/)

### Meet The Author

李来冰

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)