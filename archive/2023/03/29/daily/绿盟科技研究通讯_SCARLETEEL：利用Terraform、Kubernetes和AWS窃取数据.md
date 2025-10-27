---
title: SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据
url: https://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247494911&idx=1&sn=fcb96c62dded4e1814c433f7f13805cd&chksm=e84c4a20df3bc33610cbc9a27e52fe94fb2ec3dd160140c392f713f7dd80c0470ca7f922e771&scene=58&subscene=0#rd
source: 绿盟科技研究通讯
date: 2023-03-29
fetch_date: 2025-10-04T11:01:19.309756
---

# SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUaw9KZMW48Xb3Gj4WC9lnkshYo5rMVxk5YJcQW7Z3oEttlJibeA9ZAbneDXBuLn0SXgMTbnLo4icF6Q/0?wx_fmt=jpeg)

# SCARLETEEL：利用Terraform、Kubernetes和AWS窃取数据

原创

创新研究院

绿盟科技研究通讯

![](https://mmbiz.qpic.cn/mmbiz_gif/hiayDdhDbxUaw9KZMW48Xb3Gj4WC9lnksh9C9DHg4p75icemAZ6WqP3iaHgOv3oO66NlMibLhh3v6Q4aH5c0YD34OA/640?wx_fmt=gif)

一、 引言

根据Sophos安全公司在《The Reality of SMB Cloud Security in 2022》[1]中指出，在过去的2022一年里，发生在云上的网络攻击增加了56%。在云端获得持久性、窃取敏感数据和创建资源进行恶意挖矿是几个最常见的动机。这些攻击活动不仅是利用云服务资源进行获利，还包括一些间谍活动。

本文主要解读了由Sysdig威胁研究团队公开的一起云上攻击活动[2]，由于攻击过程复杂且较为典型，希望能够分享其中的技术细节，带大家了解真实的云上攻击事件。

文中涉及到的技术仅供教学、研究使用，禁止用于非法用途。

二、 攻击链概述

该攻击活动发生在Sysdig的一个客户环境，被取名为SCARLETEEL。攻击者利用一个容器化的工作负载获得初始访问权限，通过一些手段进行权限提升和横向移动，使得影响扩大至客户的AWS账户，大致攻击链如图1所示：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaw9KZMW48Xb3Gj4WC9lnksPiatEibBqtukyrwrWrzevtYWmNLBcf0azDz1hVLpPDUtCV9b1fbficP0A/640?wx_fmt=png)

图1 SCARLETEEL攻击链

步骤1：攻击者利用托管在AWS云账户中的Kubernetes集群获得初始访问权限

步骤2：获得集群Pod的访问权限后，攻击者可以进行以下两种操作：

a. 启动一个加密货币挖掘软件，以谋取利益

b. 利用实例元数据服务获取临时凭证权限，利用集群角色权限收集信息。由于授予的权限过大，导致攻击者可以：

a) 枚举AWS资源

b) 从Lambda和S3服务中获取其他IAM用户的凭证

步骤3：利用步骤2中获取的凭证进行横向移动，可通过AWS API获取更多账户相关信息：

a. 停用CloudTrail日志以绕过检测

b. 窃取专利数据

c. 通过S3存储桶中的Terraform状态文件，寻找其他IAM用户凭证

步骤4：利用新的凭证重复步骤3中的横向移动行为，但因缺乏权限而尝试失败

三、 技术分析

3.1

初始访问——攻击容器应用

攻击者利用暴露在公网上的服务获得初始访问权限，发现该业务运行在Kubernetes集群中。容器作为一个受限的隔离环境，并非攻击者的最终目的，攻击者在容器环境中进行了两个攻击操作：

1. 在当前环境中下载和启动挖币软件。但是挖币只是攻击者的最初目标或者作为窃取数据行为的“障眼法”，一旦可以继续扩大战果，攻击的目标也就随之改变。

2. 因此攻击者尝试利用IMDS（Instance Metadata Service）服务进行权限提升。

IMDS即实例元数据服务，它是AWS实例上的组件，在实例上进行编码，用于安全访问实例元数据。利用元数据服务获取临时凭据是一种常见的攻击思路，不同的云厂商所对应的元数据服务地址不同，其中AWS的元数据服务接口如下：

// 获取IAM信息

http://169.254.169.254/latest/meta-data/iam/info

// 获取IAM凭证信息，包括AccessKeyId、SecretAccessKey和临时令牌

http://169.254.169.254/latest/meta-data/iam/security-credentials/<rolename>

在获取凭证信息之后，可以使用aws-cli工具控制aws云服务资源。但是利用AWS API的调用请求会在AWS CloudTrail服务上留下日志。AWS CloudTrail是一项安全服务，能够记录、持续监控和保留与整个AWS网络服务基础设施的行为有关的账户活动，包括AWS管理控制台、AWS SDK、命令行工具和其他AWS网络服务服务采取的行动。如图2所示，Sysdig通过查看CloudTrail日志可了解攻击者的攻击操作：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaw9KZMW48Xb3Gj4WC9lnks9VBntlRrupA2h7zH9Q3sFWjRfHQYML8aQa3nF6KTvqQU69V4iaoica2g/640?wx_fmt=png)

图2 CloudTrail日志

由图可知，由于IAM角色权限有限，类似“CreateGroup“、”CreateUser“等敏感操作都被拒绝。AWS的IAM权限模型采用的是ABAC，即基于属性的访问控制（ABAC），它基于属性来定义权限。在实际操作中，这些属性也叫做标签，通过在权限策略中的添加标签字段，实现对资源的动态权限管理。但不论是AWS的ABAC，还是Azure的RBAC，一般云厂商的权限逻辑都认为拒绝操作优先于允许操作，因此合理分配IAM角色权限，可以很大程度地减小实例沦陷后的危害。

但不幸的是，此次事件中由于IAM角色配置不当，攻击者可以获取较多的信息。

3.2

发现——AWS

常见AWS云服务资源的信息收集思路，主要包括以下几种方式：

1. 在Lambda函数代码和环境变量中收集信息：函数代码和环境变量中可能包含其他IAM角色的凭证信息，使得攻击者获取更高权限。

2. 在ECS Task Definition中收集信息：ECS Task Definition中包含容器在启动时运行的命令信息、租户运行任务时使用的 IAM 角色信息等。

3. 在S3存储桶中收集信息：S3是 AWS的对象存储服务，从过去发生的一些S3存储桶数据泄露事件中可知，用户可能会利用S3存储一些敏感信息，包括敏感凭证、日志文件等，都可能为攻击者提供辅助。

主要思路是在一切可存储数据、可查看配置的云服务资源中获取信息。

此次事件中攻击者利用了Lambda函数和S3存储桶服务。通过已有权限查看Lambda函数列表、下载函数代码，最终窃取了客户的专有软件代码以及专有密钥，造成了知识产权的损失。

针对S3存储桶需要说明的是：CloudTrail并不记录存储在S3存储桶中的对象的数据事件，除非明确开启此类功能。在此次攻击事件中，该功能并没有开启，因此并没有记录下查看特定对象的请求信息，仅有列举存储桶列表的日志记录，如图3所示：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaw9KZMW48Xb3Gj4WC9lnksck0gt8dtkLxcmKHOicuIUN72XvWnGHHBNojyd9z1y11MWat7lyy4g2g/640?wx_fmt=png)

图3 CloudTrail日志中列出存储桶操作记录

但Sysdig断定攻击者遍历了存储桶用以寻找敏感数据，因为该存储桶中的Terraform相关文件信息在后续攻击步骤中被利用。

3.3

防御绕过——禁用CloudTrail日志

由于CloudTrail服务会记录下大部分AWS账户日志，因此在攻击AWS时攻击者往往会考虑绕过该服务的检测。在考虑如何规避CloudTrail时，需要先了解清楚该服务的运行详情。

通过查看AWS官方文档了解到，CloudTrail服务是默认启用的，AWS用户可以免费查看最近90天的事件记录。通过以下命令可以查看CloudTrail的监视范围，结果如图4所示：

aws cloudtrail describe-trails

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaw9KZMW48Xb3Gj4WC9lnkslkfjqpUIwFfibAnwHicyL2zJMXicojTjQ2reU28r4N9iafpYwnBwBggPRQ/640?wx_fmt=png)

图4 CloudTrail监控配置

其中“IsMultiRegionTrail”字段代表是否将监视所有区域，true代表是，false代表仅监视单区域；“S3BucketName”代表将CloudTrail日志写入S3存储桶。

然后了解到常见的绕过方式主要有以下几种[3]：

一、 中止CloudTrail服务

使用以下命令中止日志记录：

aws cloudtrail stop-logging --name awscloudtrail-example

当完成攻击后，重新启动日志服务：

aws cloudtrail start-logging --name awscloudtrail-example

二、 删除CloudTrail服务

删除trails或者删除存储日志的存储桶

aws cloudtrail delete-trail --name awscloudtrail-example

但是此种方法较为“高调”，会使CloudTrail服务处于宕机状态，同时删除存储桶后在管理控制台弹窗提示，如图5所示：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaw9KZMW48Xb3Gj4WC9lnksXetUNrfjrxh1S3PrIhH89SUcGR6ptXYm6duHapFBoODCoYmkKd6ibhA/640?wx_fmt=png)

图5 CloudTrail控制台弹窗

同时AWS的另一个监控服务GuardDuty也会对CloudTrail服务的异常状态发出警报，因此并非攻击者的首选。

三、区域绕过

当CloudTrail服务仅监视个别区域时，可以在监视区外的区域对实例进行操作，绕过监控；或者利用include-global-service-events标签关闭全球服务，命令如下：

aws cloudtrail update-trail --name my-trail --no-include-global-service-events

此次攻击活动中，攻击者采用了第一种方案进行规避，为调查取证提供了阻碍。在实际给应用程序分配IAM角色时，禁用或删除安全日志的权限对于程序来说不必要的，因此说明了合理分配权限与权限审查的重要性。

3.4

凭据访问——Terraform状态文件

Terraform是一个开源的基础设施即代码（IaC）工具，用于部署、改变或创建云环境中的基础设施。

为了让Terraform知道哪些资源在其控制之下，以及何时更新和销毁它们，它默认使用一个名为terraform.tfstate的状态文件。当Terraform在持续集成/持续交付（CI/CD）管道中被集成和自动化时，该状态文件需要以适当的权限被访问。特别是，运行管道的服务主体需要能够访问保存状态文件的存储账户容器。这使得像AWS S3这样的共享存储成为保存状态文件的完美候选。

然而，Terraform状态文件中可能包含凭证信息。

在上述攻击步骤中，攻击者有权限列出可用的存储桶并检索所有的数据。在事件调查期间，Sysdig尝试用不同的工具来检索数据，验证了在S3存储桶内的terraform.tfstate文件中可以找到明文IAM用户凭证信息，如图6所示：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaw9KZMW48Xb3Gj4WC9lnksBucib1Vv64kLIfyYN4HORwfM3MTictoyNrP6M9RjmEXDwbUFw8RZzyrQ/640?wx_fmt=png)

图6 S3存储桶中的terraform.tfstate文件

3.5

横向移动——AWS帐户

通过上述手段获得新凭证后，攻击者重复信息收集和横向移动操作，尝试以新凭证权限获得额外的资源。但后续的操作并没有主动规避CloudTrail服务的意识，导致CloudTrail记录了新凭证对应的可疑活动，如图7所示：

![](https://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUaw9KZMW48Xb3Gj4WC9lnksBZIWFbHwnYO68NBzfhfVmKhrib17VxMuyzfc17c8npbH2R2qN848Kvw/640?wx_fmt=png)

图7 CloudTrail记录了新凭证的攻击行为

由图可知，攻击者尝试了“ListGroups”、“ListUsers”、“AttachUserPolicy”等操作，但都因缺乏权限而失败。

五、总结与思考

SCARLETEEL事件始于一个易受攻击的Pod，攻击者通过信息收集获取到了AWS IAM用户凭证信息，从而横向移动至Lambda服务、S3存储桶服务，最终窃取了客户的专有软件。

从Sysdig调查分析的攻击行为来看，此次事件涉及的云上攻击者的攻击思路较为灵活，基本包括了常见的攻击技术并能够应用至攻击活动中，但在过程中也难免会“存在疏忽”导致留下更多痕迹。

该攻击活动真实地说明了，网络安全是一项复杂的系统工程，每个环节都应做到最佳防护，防止出现“牵一发而动全身”的影响。尤其是此次攻击活动中最为突出的两个问题：最小权限原则和威胁检测机制。若在分配角色权限过程中能够遵循最小化原则并定期进行权限审查，攻击者难以横跨至云服务资源中从而获取更多信息，也难以绕过日志监控系统，可能会留下更多的攻击痕迹。而强大的威胁检测机制则可以在攻击者进一步深入之前给出警报信息，帮助客户及时止损。

参考文献

1. https://news.sophos.com/en-us/2022/11/29/the-reality-of-smb-cloud-security-in-2022/

2. https://sysdig.com/blog/cloud-breach-terraform-data-theft/

https://rzepsky.medium.com/playing-with-cloudgoat-part-2-fooling-cloudtrail-and-getting-persistence-access-6a1257bb3f7c

往期回顾：

[公有云攻防系列——云服务利用篇](http://mp.weixin.qq.com/s?__biz=MzIyODYzNTU2OA==&mid=2247493212&idx=1&sn=8c7343b9f52ae4edf642b6f070ed61ec&chksm=e84c4083df3bc995b0ec32b461e63bffa76033654adb46dd42537444bc1b6d93d968955de300&scene=21#wechat_redirect)

内容编辑：创新研究院 李来冰

责任编辑：创新研究院 陈佛忠

本公众号原创文章仅代表作者观点，不代表绿盟科技立场。所有原创内容版权均属绿盟科技研究通讯。未经授权，严禁任何媒体以及微信公众号复制、转载、摘编或以其他方式使用，转载须注明来自绿盟科技研究通讯并附上本文链接。

**关于我们**

绿盟科技研究通讯由绿盟科技创新研究院负责运营，绿盟科技创新研究院是绿盟科技的前沿技术研究部门，包括星云实验室、天枢实验室和孵化中心。团队成员由来自清华、北大、哈工大、中科院、北邮等多所重点院校的博士和硕士组成。

绿盟科技创新研究院作为“中关村科技园区海淀园博士后工作站分站”的重要培养单位之一，与清华大学进行博士后联合培养，科研成果已涵盖各类国家课题项目、国家专利、国家标准、高水平学术论文、出版专业书籍等。

我们持续探索信息安全领域的前沿学术方向，从实践出发，结合公司资源和先进技术，实现概念级的原型系统，进而交付产品线孵化产品并创造巨大的经济价值。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiayDdhDbxUbrbTJxY0Qv9BtgtXZsYVvaVUtlPicCUV6qDBGgZnrxicAMwvibG73JUu0w1UweTicfkuTRIyJyt77C5Q/640.jpeg?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1&retryload=2)

**长按上方二维码，即可关注我**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

绿盟科技研究通讯

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hiayDdhDbxUYc15Dsy8RcPfwerHzBEhBVQk20S88RRtnlBS56ZnUv3JStz1JUyyBicDvreCNoDaJZ8ul5xxtWRmg/0?wx_fmt=png)

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