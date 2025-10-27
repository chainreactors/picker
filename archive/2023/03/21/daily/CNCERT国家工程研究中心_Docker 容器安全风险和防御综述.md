---
title: Docker 容器安全风险和防御综述
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535607&idx=2&sn=8c8bae38cbd79456d8d829d61c7208ab&chksm=fa93fd36cde47420b981f6effbc7d3c37ca5264b3ca59367e8e2ae5bfd2cac0c200caad15440&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-21
fetch_date: 2025-10-04T10:09:40.107870
---

# Docker 容器安全风险和防御综述

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kJ7HP1LZv5F3FThiaAYqQOztdgw9eHc8TdPeGroUd2icmPPVM7MHgTRxrC94Am9NELPQEC3YAedmqQ/0?wx_fmt=jpeg)

# Docker 容器安全风险和防御综述

网络安全应急技术国家工程中心

以下文章来源于信息安全与通信保密杂志社
，作者Cismag

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM57SpaEcnib8NMGibzYLk6p0uOuGZThgJsy6XBtuoV6SmKQ/0)

**信息安全与通信保密杂志社**
.

网络强国建设的思想库、安全产业发展的情报站、创新企业腾飞的动力源

**摘要：**Docker是目前最具代表性的容器平台之一，它的安全问题引起了产业界和学术界的广泛关注。首先，对Docker架构以及基本安全特性进行介绍，分析了Docker面临的安全威胁。其次，对Docker增强、安全检测、瘦身等方面的安全技术进行了分析梳理。最后，对Docker安全的未来发展进行总结和展望，帮助和激励研究人员开始对Docker领域的研究。

Docker是一种轻量级的虚拟化方式，将应用程序和运行环境打包成容器镜像，使得应用程序能够直接在容器中独立地运行。由于Docker拥有轻量化、高效率和易部署的特点，目前已被广泛应用于云计算和微服务架构中。

根据国家安全漏洞库统计，Docker自2013年正式发布以来，截至2022年8月，累计发现124个相关漏洞，其中高危以上漏洞占71%，这对应用生态安全和用户信心都带来了不利影响。因此，Docker的安全性得到了产业界和学术界的广泛关注，许多研究思路和方法被不断提出。本文对Docker安全相关的研究思路、方法和工具进行比较和分析，并指出未来可能的研究方向。

# **1、背景知识**

**1.1　Docker架构**

图1为Docker架构图。容器在宿主机上工作，并和其他容器共享宿主机内核。其中Docker客户端和Docker守护进程通过REST API进行通信，发送拉取镜像之类的命令行请求；Docker守护进程用来处理Docker客户端发送的请求；Docker引擎是Docker架构中的运行引擎；Docker 容器是容器服务的交付实体。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBwBfSa05Bbw4a7yhB3RuoIxaAfibKG9n3FEiaicib32WXwia3jdHhIapXMfymhIwRxfQ8xjbHCoyArC01A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图 1　Docker 架构

**1.2　Docker安全机制**

Docker采用了多种Linux内核安全机制来约束容器内的进程，如表1所示。

Docker利用Linux的命名空间(Namespaces)为容器提供独立的工作空间，与其他容器进行资源隔离；Docker利用Cgroups机制，限制每个容器可以访问哪些资源，确保多容器环境下能正常使用系统资源；Capabilities定义了CAP\_CHOWN、CAP\_KILL等多种权限(不同版本略有不同，5.16-rc6版本中定义了40个权限)，将超级用户权限进行细分，容器默认只有其中的14种权限；Docker基于Seccomp机制，限制容器内系统调用；SElinux和AppArmor属于强制访问控制，限制可执行程序的访问控制权限，如读写功能；内容信任机制通过发布者签名和使用者校验的方式确认镜像的完整性。

表 1　Docker 安全机制

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBwBfSa05Bbw4a7yhB3RuoIxIcJHJDCbfW4NjF8pMtdGgCe6o01dLsQX7lfROoQYZrib8sWoCmOphmQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

# **2、容器 Docker 安全风险**

狴犴安全团队将Docker安全问题分为镜像安全风险、容器虚拟化安全风险和容器网络安全风险3个方面，本文在此基础上对Docker安全问题进一步补充分析，为后续Docker安全增强提供研究方向。

**2.1　镜像安全风险**

镜像安全决定了生成容器的安全性，一直 是学术界关注的热点。表 2 是近几年研究镜像 包含漏洞的情况。随着时间的推移，镜像中的 漏洞数并没有明显减少，说明镜像仓库中的镜像安全问题一直没有得到很好的解决。

表 2　Docker 镜像漏洞对比

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBwBfSa05Bbw4a7yhB3RuoIxQH4YbOvFmPCc5GYvgr0m4p4MqWEAicvqcfHu7ibECIoicSuLkkyGeqBIA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

(1)镜像安全威胁模型如图2所示，Docker Hub平台用户面临两种不同的威胁：一是攻击者可以发布包含恶意执行命令的镜像，一旦用户下载运行镜像，就可能遭受攻击；二是开发者发布包含漏洞的镜像，攻击者有可能利用漏洞对使用镜像的用户进行攻击。

(2)镜像仓库安全风险。主要包含两个方面的风险：一是如果私有镜像仓库的配置不当，攻击者可利用漏洞直接通过公网访问私有仓库并随意篡改仓库镜像；二是用户以明文形式下载镜像，容易遭遇中间人攻击，攻击者能够篡改镜像内容或者冒名发布恶意镜像。

(3)构建镜像安全风险。两种Docker镜像的构建方式：一是使用Docker commit命令行方式构建，直接提交容器并生成镜像；二是编写Dockerfile指令，按照指令构建一个新镜像。文献[5]研究表明，Docker Hub平台上的Dockerfiles文件存在两个问题：一是构建过程违背Dockerfile最佳实践，如未明确标记镜像版本等；二是Dockerfiles文件包含恶意代码脚本，导致存在主机文件泄露等安全问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBwBfSa05Bbw4a7yhB3RuoIxRSZ6qjGDJZpbMEkLmEd74vdA7UTOsUXGrOmxX2MnQKlVy2jrT3wUicg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图 2　Docker 镜像安全威胁模型

**2.2　容器虚拟化安全风险**

容器是一种轻量级的虚拟化方式，且不拥有独立的资源配置，没有做到系统内核层面的隔离。

(1)容器隔离安全风险。与虚拟机相比，Docker缺少虚拟化层，在文件隔离方面并不完善，如容器仍然可以访问主机系统的/proc和/sys目录，攻击者可以获取/proc/kallsyms中的内核符号来构建针对内核漏洞的攻击。针对存储资源，Cgroups未对主机存储资源进行限制。若容器不断向存储空间写入数据直至耗尽，将造成主机或容器的拒绝服务。

(2)容器逃逸攻击。容器逃逸是指容器“逃出”自身权限，能够对宿主机和其他容器进行非法访问。容器逃逸的方式有很多种：一是利用容器的配置不当，如Docker高危启动参数等；二是利用Docker软件本身存在的安全漏洞，如容器逃逸著名案例Shocker攻击通过调用open\_by\_handle\_at函数来获取宿主机的资源；三是利用内核漏洞进行容器逃逸，如通过内核漏洞非法进入内核上下文，获取当前进程的有关数据，切换当前命名空间来获取root shell，实现容器逃逸。

**2.3　容器网络安全风险**

Docker网络驱动包含桥接网络、MacVLAN和Overlay这3种模式，如图3所示。Docker默认的网络驱动是桥接网络。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBwBfSa05Bbw4a7yhB3RuoIxz5Cficn9BcRpMgziaWJXFDcMtXdOUpUz7sPm4wq0MKUowLNziaVeo0lGg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图 3　Docker 网络驱动

桥接网络的容器之间共用未过滤的Docker0网桥来进行通信；MacVLAN与主机的网络接口连接，容器之间没有访问权限限制；Overlay主要利用虚拟扩展局域网(Virtual eXtensible Local Area Network，VXLAN)技术，在主机之间的网络上构建出新的虚拟网络，但未实现流量加密。3种组网模式都存在一定的安全风险，容器易遭受地址解析协议(Address Resolution Protocol，ARP)欺骗、嗅探、广播风暴和拒绝服务等攻击，造成敏感信息泄露和网络服务功能受限等危害。

容器之间的网络流量控制主要利用Iptables命令进行基于IP的访问控制。但是容器的IP是动态的，创建或重新启动容器会分配一个新IP，Iptables命令都需要调整。因此，从性能和安全性两方面为容器指定安全策略是一个挑战，因为每当重新创建容器时，必须更新这些策略，并且在策略更新期间也应锁定Iptables的策略表。此外，Iptables的限制范围有限，容器网络仍然容易受到数据链路层攻击，如ARP欺骗等。每个容器需要不同的网络策略，策略的总数将随着容器数量的增加而增加，容易产生网络策略爆炸，容器生态系统的性能和安全性都将受到影响。

# 3、Docker安全增强技术

Docker安全增强技术主要包括利用Linux内核安全机制、可信计算的单容器安全增强，以及基于访问控制策略容器间运行安全控制等。

(1)基于命名空间和内核模块(Linux Kernel Module，LKM)来缓解容器隔离安全风险。Jian等人通过动态检查主机命名空间的方式，实现了对异常进程的有效检测，防止逃逸行为。陈莉君等人提出了基于LKM的Docker资源信息隔离方法，利用系统调用劫持技术来覆写进程文件内容，建立有效的资源隔离机制。

(2)基于AppArmor机制增强容器安全，缓解了容器逃逸和特权提升等攻击。在AppArmor的默认配置文件中并没有限制网络和capability规则，攻击者可以通过受损容器危害宿主机。Loukidisandreou等人提出Docker-Sec方法，通过静态分析容器执行参数和动态监测运行状态来生成AppArmor配置文件，但该方法无法防御用户空间攻击。Mattetti等人提出了LiCShield框架，利用SystemTap方法跟踪系统内核操作并生成包含5种规则的AppArmor配置文件，但LiCShield生成的文件作用范围只在Docker守护进程。Zhu等人提出的Lic-Sec将Docker-Sec与LiCShield相结合，动态分析生成AppArmor配置文件。其能够提供更高级别的保护，防止所有的特权提升攻击，包括Docker-Sec无法防御的用户空间攻击。Lic-Sec的流程如图4所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBwBfSa05Bbw4a7yhB3RuoIxxVmmPUTLcYat6OetVmYVh7nnz8fjJvkllbBlico1VnCcr0he5iaSRIMw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图 4　Lic-Sec 流程

(3)基于Seccomp机制增强容器安全。在Linux的300多个可用系统调用中，Seccomp默认会在配置文件中阻止其中44个系统调用，但剩余的系统调用仍有可能被滥用从而对系统造成安全威胁。Lei等人提出了分阶段执行应用程序容器SPEAKER，将容器分成启动阶段和运行阶段，使用strace工具对系统调用进行跟踪并生成Seccomp配置文件，但是动态分析无法覆盖容器全部的系统调用。Wan等人提出了一种基于自动测试的沙箱容器挖掘方案(Mining Sandboxes)，使用测试套件对容器进行测试并跟踪系统调用，分析日志生成Seccomp配置文件，同样动态分析无法覆盖容器全部的系统调用。Ghavamnia等人提出Confine工具，使用静态和动态分析来检测出容器内的应用程序及其所有依赖项，识别容器正确操作所需的系统调用，并生成Seccomp配置文件。基于AppArmor机制和Seccomp机制的6种方法的具体比较如表3所示。

(4)基于可信计算增强容器安全。2015年，Intel推出指令集扩展(Software Guard Extensions，SGX)，可用于保护不受信任主机上运行的容器和其他应用程序。Arnautov等人提出了基于SGX机制增强Linux容器安全(Secure Linux Containers with Intel SGX，SCONE)来保护容器免受外部攻击，但是该方法对于硬件设备的限制过高，无法进行大范围推广。王鹃等人 利 用可信计算技术，提出了 Docker 安全增强系统DockerGuard，构造了一条从底层硬件到容器的信任链，增强运行过程的安全。但该方案牺牲 了 Docker 容器原有的便捷、快速部署的特性，并且难以根据Docker版本的更新进行实时更新。

表 3　基于 Linux 内核安全机制的加固方法

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBwBfSa05Bbw4a7yhB3RuoIxDz4udzSaoyqDlbVuf5f3BdsRopoROswDfI9LOia6YMxgOicdpy8EOOLQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

(5)微服务环境中的容器间访问控制。云服务应用程序通常由许多微服务组成，而73%的微服务部署在容器当中。为了防止正常的微服务被其他恶意的微服务随意访问，需要有细粒度的访问控制策略来支撑。Li等人提出了自动增强访问控制工具AUTOARMOR，具有以下特点：一是利用基于静态分析的请求提取机制，从微服务源码中自动获取微服务间的调用逻辑；二是利用基于图形的策略管理机制，通过权限图来实现策略的更新。实验表明，AUTOARMOR能够以较小的开销有效地生成微服务间的访问控制策略，成功阻止了访问未经授权的微服务、访问未经授权的资源和执行未经授权的操作3种未经授权请求攻击，缓解了容器网络安全风险。但该方法仍存在以下问题：

服务应用程序通常由许多微服务组成，而73%的微服务部署在容器当中。为了防止正常的微服务被其他恶意的微服务随意访问，需要有细粒度的访问控制策略来支撑。Li等人提出了自动增强访问控制工具AUTOARMOR，具有以下特点：一是利用基于静态分析的请求提取机制，从微服务源码中自动获取微服务间的调用逻辑；二是利用基于图形的策略管理机制，通过权限图来实现策略的更新。实验表明，AUTOARMOR能够以较小的开销有效地生成微服务间的访问控制策略，成功阻止了访问未经授权的微服务、访问未经授权的资源和执行未经授权的操作3种未经授权请求攻击，缓解了容器网络安全风险。但该方法仍存在以下问题：一是请求识别依赖于服务间通信库的建立和语义模型，当通信库的建模不完整时，会导致请求不被识别；二是即使通信库建模是正确的，无用代码也会带来误报。

# **4、Docker安全检测**

**4.1　检测容器安全工具**

镜像安全风险一直是学术界的研究热点。目前的镜像安全检测工具主要分为开源工具和商用工具。本文对代表性的开源工具进行性能对比，如表4所示。

Javed等人使用Clair、Anchore和Microscanner这3种扫描工具对59个承载Java应用程序的容器进行扫描，发现现有的工具准确性普遍不高，准确率最高的Anchore漏掉了34%的漏洞，原因是只有Anchore能够扫描非系统包，同时准确率依赖于现有的漏洞数据库和漏洞检测方式。Zheng等人介绍了一种基于继承图的安全检测系统ZeroDVS，通过2 000个镜像的rootfs配置信息，建立有镜像继承关系的图形数据库，并预先存储父镜像信息。在扫描镜像漏洞时，与数据库匹配批量识别父镜像源的漏洞，此时只需扫描未匹配的子镜像层的安全漏洞，提高了安全扫描效率。

表 4　检测容器安全工具

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBwBfSa05Bbw4a7yhB3RuoIxLtdf4LafEiak35Y8Hua9icw2b3wotsNsbGbAc67d99s5f7HhsBc5QYRg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**4.2　基于机器学习的容器安全检测**

容器安全检测工具大多是针对镜像进行静态扫描检测。基于机器学习的检测技术主要是对容器运行时的状态(系统调用、文件输入/输出、网络输入/输出、调度程序和内存等)进行特征提取，然后使用分类器进行训练检测。检测技术分为无监督学习检测方法和有监督学习检测方法。

(1)无监督学习检测方法。Tunde-onadele等人发现仅对容器进行静态漏洞扫描是不够的，于是提出了4种无监督机器学习方法，包括K近邻法(K-Nearest Neighbor，KNN)、主成分分析(Principal Component Analysis，PCA)结合KNN、K均值(K-Means)、自组织映射算法(Self-Organizing Map，SOM)，把系统调用频率作为特征向量，通过实验比较，SOM的检测准确率最好，达到78.57%，但都没有达到较高的准确率。Srinivasan等人提出了一种实时入侵检测系统模型，利用N-grams系统调用计算概率，然后使用最大似然估计器和简单良好的图灵平滑技术来处理跟踪，检测异常的准确率可达到87%~97%。

(2)有监督学习检测方法。Abed等人将系统调用包(Bag of System Calls，BoSC)与滑动窗口技术结合，只跟踪当前窗口中系统调用的频率，把规定窗口内不同的系统调用的频率映射成序号，并作为特征向量来进行判别训练。该方法具有较高的检测率，真阳性率达到100%，但该方法对训练要求高。Tien等人提出KubAnomaly系统，使用4层全连接层构造神经网络，利用系统调用作为特征向量来创建分类模型，实现了高达96%的检测准确率，并成功识别了4次真实环境下的攻击。但应用该系统需要在客户机上安装代理软件，可能会面临通过代理软件进行攻击的威胁。季一木等人利用基于系统调用序列和系统调用频率的入侵检测方法，结合滑动窗口与优化后的词的逆文档频率(Term Frequency–Inve...