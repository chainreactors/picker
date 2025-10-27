---
title: 从云上攻防态势分析展望云服务安全架构设计框架发展
url: https://buaq.net/go-166070.html
source: unSafe.sh - 不安全
date: 2023-05-29
fetch_date: 2025-10-04T11:37:02.724615
---

# 从云上攻防态势分析展望云服务安全架构设计框架发展

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/9ccd0ed5875da70f2399c413b1880611.jpg)

从云上攻防态势分析展望云服务安全架构设计框架发展

本文主要是记录笔者基于近期对云上攻防态势的分析思考和展望云服务安全架构设计框架的未来发展趋势，观点仅代表个人。近期，笔者详细分析了近几年所有公开的云厂商漏洞报告[1
*2023-5-28 12:53:38
Author: [avfisher.win(查看原文)](/jump-166070.htm)
阅读量:43
收藏*

---

本文主要是记录笔者基于近期对云上攻防态势的分析思考和展望云服务安全架构设计框架的未来发展趋势，观点仅代表个人。

近期，笔者详细分析了近几年所有公开的云厂商漏洞报告[1]发现，头部云厂商的云服务都存在不少漏洞，其中AWS、GCP、Azure被公开披露的云服务漏洞最多。

其中最易受攻击的云服务类型主要集中以下几种类型：
[![02](http://avfisher.win/wp-content/uploads/2023/05/02.png)](http://avfisher.win/wp-content/uploads/2023/05/02.png)

* **k8s/容器**：AWS CloudShell, AWS ECR Public, AWS ECS, AWS EKS, Azure ACI, Azure Function Apps, Azure Service Fabric, Azure CloudShell, GCP Anthos Service Mesh, GCP Cloud Shell, GCP GKE
* **数据库**：AWS RDS, Azure Cosmos DB, Azure Database for PostgreSQL, GCP Cloud SQL, IBM Cloud Database for PostgreSQL, Aliyun ApsaraDB RDS for PostgreSQL, Aliyun AnalyticDB for PostgreSQL
* **数据管理**：AWS AppSync, AWS Glue, Azure Cognitive Search, Azure Synapse Analytics, Azure Data Factory, GCP Dataflow
* **CI/CD**：AWS CodeStar, Azure DevOps, Azure Service Fabric Explorer, GCP CloudBuild
* **计算**：Azure Red Hat Update Appliance, GCP GCE, GCP GCD, GCP OS Login
* **IAM**：AWS IAM, Azure AD, Azure ADFS, GCP IAM

由此可见，**大量基于k8s/容器等新技术构建的云服务是攻击者/安全研究者最青睐的攻击/研究对象，其次就是近年来针对基于开源数据库软件构建的云数据库和数据管理服务的攻击趋势明显上升，此外针对CI/CD云服务的供应链攻击也在显著增多，还有针对最常见的云上IAM服务的攻击依然普遍存在。**

进一步分析发现云服务面临的主要攻击类型如下：
[![03](http://avfisher.win/wp-content/uploads/2023/05/03.png)](http://avfisher.win/wp-content/uploads/2023/05/03.png)

* **越权攻击**:
  + Azure  Cosmos DB Notebook的forwardingId存在越权问题可导致RCE漏洞（CosMiss）
  + GoldenSAML攻击主要针对联邦认证机制中使用的SAML  Response的伪造
  + 利用assume  role提权至Glue服务账号再结合其内部API的不安全配置获得其他使用了Glue服务的租户账号权限
  + 利用AWS  AppSync服务的confused deputy问题实现跨租户资源访问
  + 利用AWS  ECR Public服务的未公开API跨租户越权修改容器镜像
  + 利用Azure  PostgreSQL权限配置不当实现本地提权及通过数据库备份功能证书校验逻辑不严实现跨账号数据库认证绕过
  + 利用GCP  CloudBuild服务的Service Account账号的token（metatdata  API中获取）实现IAM的提权，即利用云服务的默认过多的IAM权限实现IAM的低权限提升
  + 利用GCP的各种服务特性实现IAM权限提升，即间接提权方式
  + 利用云服务的跨账号默认IAM权限配置不当，如允许修改资源arn，实现跨租户资源获取
  + 在Azure  Synapse Spark功能中利用filesharemount.sh脚本的条件竞争问题对任意文件执行chown操作从而实现本地提权
* **注⼊攻击**:
  + AWS  SageMaker Jupyter Notebook Instance  Takeover（利用XSS->CSRF->安全恶意扩展->访问Metadata->获取AWS认证token）
  + Azure  Synapse pipelines and Azure Data Factory默认使用的第三方适配Amazon  Redshift的ODBC连接器驱动存在命令注入漏洞（CVE-2022-29972）导致RCE可获取Azure服务敏感信息和跨租户数据
  + Google  Cloud Shell – Command Injection
  + 利用AWS  PostgreSQL的log\_fdw扩展的路径穿越漏洞实现任意本地文件读取泄露RDS服务的内部认证凭据
  + 利用CSTI和存储型XSS获得Azure  Service Fabric Explorer服务的用户管理员权限（CVE-2022-35829）
  + 利用Google  Cloud Shell校验逻辑不当借助Theia IDE实现Cloud Shell命令注入可绕过安全校验直接访问Cloud  Shell底层VM实例的metadata
  + 利用Kudo提供的SCM面板的CSRF攻击多个Azure  Web服务
  + 通过commit  message修改Azure DevOps流水线执行过程中的环境变量可导致软件供应链攻击
  + 通过SSH公钥注入获取GCE访问权限
* **云原⽣攻击**:
  + Azure  Container Instances (ACI)服务跨账号容器接管
  + PostgreSQL服务帐户可以访问其他 RDS（MySQL、SQL Server 等）的 Docker 映像
  + 利用AWS的ECS服务的Task  Definition新建容器并通过EC2的metadata API获取临时AK/SK提权
  + 利用Azure  Serverless Function容器中本地进程提权实现容器逃逸
  + 利用Google-managed  Anthos Service Mesh的Istio控制面支持多集群部署通过新建恶意的GKE集群并部署Google-managed  ASM导致RCE可直接访问Google-managed ASM底层VM实例的metadata
  + 利用k8s  TLS Bootstapping机制进行提权
  + 利用具有CAP\_NET\_RAW  Linux  capability和hostNetwork=true的容器通过中间人劫持K8S集群的云宿主机node节点上的Metadata服务实现本地提权或者容器逃逸
  + 通过AWS  ECS Task Definition可以获取敏感信息（Task Definition类似于k8s的kubeconfig文件）
  + 阿里云PostgreSQL服务因不安全配置导致容器逃逸可造成跨租户数据库的未授权访问
* **信息泄露**:
  + AWS:  Lightsail object storage access keys logged
  + GCP:  Exfiltrate data via the logs of GCP Org policy
  + NotLegit:  Azure App Service vulnerability exposed hundreds of source code repositories
  + S3漏洞利用（计算资源中列权限、过度依赖IAM防止数据泄露、非公开的桶中包含公开的存储对象）
  + 滥用AWS  VPC服务的TrafficMirror特性获取东西向流量中的敏感信息
* **开源组件攻击**:
  + AWS  CloudShell Terminal（Cloud9）命令注入漏洞（CVE-2019-0542）
  + AWS:  In-band key negotiation issue in the AWS S3 Crypto SDK for golang  (CVE-2020-8912 and CVE-2020-8911)
  + Azure:  Cloudshell terminal escape (CVE-2019-0542)
  + Dataflow服务的JMX  RMI端口未授权访问导致RCE并借助使用host网络的容器可直接访问GCE的metadata
* **防御绕过**:
  + 利用AWS  API Gateway服务可以绕过IP黑名单的限制
  + 利用未公开的私有API绕过CloudTrail的日志记录

通过分析以上针对云服务的攻击类型可以总结出云服务面临的主要威胁类型（STRIDE）如下所示：

[![04](http://avfisher.win/wp-content/uploads/2023/05/04.png)](http://avfisher.win/wp-content/uploads/2023/05/04.png)

根据识别出来的云服务面临的主要威胁，站在云服务安全架构设计的角度来看导致这些安全威胁的根因应该包括以下几个方面：

* **网络连接：突破云服务所在的网络隔离直接攻击云服务**
  + 传统的网络隔离边界：防火墙、路由器、交换机、VPN
  + VPC：peering、endpoint、traffic mirror
  + 云专线：混合云、多云网络
  + 安全组
* **部署模式：利用云服务部署架构的特性打破租户隔离实现跨租户资源获取**
  + 物理多租：单租户独享
  + 逻辑多租：多租户共享
* **资源负载：利用部署云服务的资源负载的逃逸漏洞突破资源隔离**
  + k8s/容器逃逸
  + 虚拟机逃逸
  + 物理机CPU/芯片侧信道攻击
* **权限配置：利用云服务的权限策略配置问题突破权限隔离**
  + IAM账号：AWS Landing Zone
  + IAM策略：ABAC
  + 委托代理：Confused Deputy
  + 联邦认证：AWS STS security tokens、SAML
* **服务功能：利用云服务自身功能特性和漏洞造成资源滥用、权限提升、信息泄漏**
  + 传统的Web漏洞：SSRF、XXE、XSS、CSRF、CSTI
  + 云服务功能滥用：API Gateway、CloudShell Terminal、云函数、云WAF、云CDN、云存储桶
  + 未公开API滥用
* **应用数据：不安全的应用数据保护导致信息泄漏**
  + 云日志服务：CloudTrail
  + 数字证书不当传输与保存：Azure AD、Cloud SQL Auth Proxy
  + 数据明文传输与保存：VPC TrafficMirror

云安全公司Wiz近期发布了一个专门针对云服务租户隔离框架PEACH，结合其在云安全领域的研究成果系统地提出了云服务安全架构设计方法论[3]。

Wiz认为典型的云服务漏洞引发的跨租户攻击模式如下：

[![05](http://avfisher.win/wp-content/uploads/2023/05/05.png)](http://avfisher.win/wp-content/uploads/2023/05/05.png)

应用PEACH框架构建安全的云服务架构的核心原则包括：

* **减少云服务应用接口的复杂性**
* **增强租户间资源访问的隔离性**
* **提高租户间资源的冗余度**

具体分两步走：

**第一步，对云服务应用进行威胁建模**

[![06](http://avfisher.win/wp-content/uploads/2023/05/06.png)](http://avfisher.win/wp-content/uploads/2023/05/06.png)

1) 首先找出云服务应用的所有外部接口。

2) 然后对每个接口执行以下分析：
[![07](http://avfisher.win/wp-content/uploads/2023/05/07.png)](http://avfisher.win/wp-content/uploads/2023/05/07.png)

2.1) 确定输入类型（即输入的不受信任的数据）和接口的各个组件。

2.2) 绘制接口的设计图，包括以下元素：

[![08](http://avfisher.win/wp-content/uploads/2023/05/08.png)](http://avfisher.win/wp-content/uploads/2023/05/08.png)

* 注意用户输入类型，可能会变形以滥用接口。
* 跟踪数据从用户输入经过的每个存储或处理它的组件的流程。
* 区分共享和复制组件。
* 添加安全边界，将每个复制组件与其他租户分开。

2.3) 评估每个组件的复杂度级别。

2.4) 根据以下准则确定接口的隔离级别：

* 使用了哪些安全边界类型？
  + 资源隔离
  + 数据隔离
  + 网络隔离
  + 身份隔离
* 它们彼此独立吗？
  + 共享组件
  + 复制组件
* 它们如何加固？（参见第二步）
  + 权限加固
  + 加密加固
  + 认证加固
  + 网络加固
  + 环境清理

2.5) 在实施表中总结发现的威胁。

[![09](http://avfisher.win/wp-content/uploads/2023/05/09.png)](http://avfisher.win/wp-content/uploads/2023/05/09.png)

2.6) 通过询问来确定数据流的每个阶段可能出现的潜在漏洞：

* 组件的攻击面是什么？
* 什么样的恶意用户输入可能导致滥用？

2.7) 如果隔离级别在复杂性和情境因素（包括合规性、数据敏感度和预算考虑）方面被确定为不足，则根据需要修改设计，通过减少复杂性，增强隔离性，增加资源冗余度来提高隔离级别。

**第二步，基于P.E.A.C.H.五个方面实施云服务安全加固**

* **权限加固（Privilege hardening）：**
  + 在服务环境中，租户和主机通常具有最小的权限，遵循最小特权原则。
  + 特别地，除非经过租户明确批准，否则每个租户不得读取或写入其他租户的数据，每个主机也不能读取或写入其他主机的数据
  + 在执行操作之前，需要验证权限。
* **加密加固（Encryption hardening）：**
  + 属于每个租户的数据（静态数据和传输数据）都使用唯一于该租户的密钥进行加密，而不管架构如何。
  + 与每个租户的活动相关的日志由租户和控制平面之间共享的秘密进行加密。
* **认证加固（Authentication hardening）：**
  + 每个租户与控制平面之间的通信（双向）使用唯一于每个租户的密钥或证书进行身份验证。
  + 验证身份、验证密钥，并阻止使用自签名密钥。
* **网络加固（Connectivity hardening）：**
  + 默认情况下，除非经过租户明确批准（例如便于数据库复制），否则阻止所有主机之间的互联互通；主机不能连接服务环境中的其他主机，除了控制平面使用的主机（即集线器和分支配置）。
  + 除非经过租户明确批准，否则主机不接受来自其他主机的传入连接请求，除了控制平面使用的主机（以防攻击者设法克服自己受损主机上的连接限制）。
  + 租户不能随意访问任何外部资源（服务环境内部和Internet上的资源），只能与租户预先批准或明确批准的资源进行通信。
* **环境清理（Hygiene）：**环境中的不必要的数据或者信息可能为攻击者提供线索或快速收益，特别是那些已经成功攻破一个或多个安全边界的攻击者，这会进一步促进侦察和横向移动。因此，供应商可以在设计阶段消除以下类型的数据，并定期扫描部署环境中遗忘的数据或者信息：
  + 机密信息：接口和数据存储（以及虚拟化或容器化情况下的底层主机）不包含任何密钥或凭据，这些凭据将允许对其他租户环境进行身份验证或解密其他租户的后端通信或日志。
  + 软件：主机实例和数据存储（以及底层主机）不包含任何内置软件或源代码，这些软件或源代码可能会促进侦察或横向移动。
  + 日志：每个租户的日志对其他租户隐藏并不可访问；每个租户可访问的日志不包含与其他租户活动有关的任何信息。

应该说PEACH框架是一个不错的云服务安全架构设计框架，但是细究下来也存在一些不足：

* **过度隔离**：为了提高资源冗余度添加太多重复组件和安全边界也可能会导致云服务环境整体复杂度的增加，从而可能引入新的漏洞。
* **过度依赖人的分析经验**：云服务安全架构师需要具备丰富的攻防经验，了解各种云服务接口类型和相应的加固方案，过度依赖架构师的经验会导致不同能力的架构师对于风险消减的最终效果差异较大。

因此，结合云上攻防态势分析的结果和PEACH框架的核心思...