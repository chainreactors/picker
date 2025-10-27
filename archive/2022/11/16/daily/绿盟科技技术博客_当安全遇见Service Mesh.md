---
title: 当安全遇见Service Mesh
url: http://blog.nsfocus.net/service-mesh/
source: 绿盟科技技术博客
date: 2022-11-16
fetch_date: 2025-10-03T22:53:13.650450
---

# 当安全遇见Service Mesh

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

# 当安全遇见Service Mesh

### 当安全遇见Service Mesh

[2022-11-15](https://blog.nsfocus.net/service-mesh/ "当安全遇见Service Mesh")[李睿捷](https://blog.nsfocus.net/author/liruijie/ "View all posts by 李睿捷")

阅读： 1,165

根据《2022年银行业云原生技术发展实践与展望》显示，国内多家大型金融机构，如华夏银行、中国银行等，通过以Istio为代表的开源Service Mesh服务治理框架帮助企业敏捷地构建云原生应用。

另外，NIST在今年2月发布了SP800-204C (利用服务网格为基于微服务的应用程序实施DevSecOps)。Service Mesh（服务网格）首次以合规文件标题的形式出现在大众视野里面。

接下来，我们将揭开Service Mesh神秘面纱，看看它在云原生生态中扮演着什么样的角色、可以为云原生业务带来哪些价值以及探索它与安全之间的关系。

在开始之前，我们需要了解两个和K8S相关的基本概念：Service：一组具有相同Label Pod集合的抽象。K8S为一组Pod提供相同的DNS名，通过Service可以在它们之间进行负载均衡Endpoints：K8S集群中的一个资源对象，存储在K8S MasterNode的etcd中，用来记录一个Service对应的所有pod的访问地址

![](https://wework.qpic.cn/wwpic/676670_nhte-UXBQ0i4D-J_1668485209/0)

图：通过Service来为相同Label的Pod动态分配访问流量

## 一、**微服务架构业务面临的挑战**

随着云原生理念的普及，更多的组织开始使用容器技术来重构业务系统—从传统单体式（Monolithic）应用转向微服务架构（Microservices）应用。微服务通过对复杂系统进行拆分，使其变成多个易于开发和维护的小的服务单元，每个服务保持自身的开发和部署节奏，从而实现业务的敏捷性。然而，单体式应用拆分成微服务后以后也随之带来诸多挑战，主要包括：

* 服务发现与路由更复杂

我们设想一个利用微服务架构搭建的网上购物业务， 每一个不同的服务都对应属于自己的业务逻辑，比如购物车服务负责添加商品、 Webserver服务负责处理UI请求、数据库服务负责存储数据等，这些不同服务之间需要相互通信。 某一个服务需要知道如何与其他服务进行通信，比如需要将与通信的其他所有服务的Endpoints在Webserver服务上进行配置。当我们添加一个服务的时候，我们需要随之添加所有与之进行通信服务的Endpoints，这些将作为应用部署代码的一部分而存在，这必然会给本应专注于业务逻辑本身的服务带来额外的负担。

![](https://wework.qpic.cn/wwpic/385519_es7VN_StQnaDu8g_1668485209/0)

图：微服务架构应用示意图

* 东西向流量难以防护

组织通常将防火墙部署在K8S集群的边界，一旦攻击者入侵到集群内部，集群内部的通信将处于安全威胁当中。默认状态下，微服务之间的通过Http或者其他不安全的协议进行通信；另外集群中的任何服务之间都可以不受限地进行通信。从安全角度看，对于包含敏感数据的容器化业务，如包含个人信息的电子银行应用，K8S集群内部东西向防护的缺失无疑给组织带来较高的风险。此时，每个服务就需要考虑如何安全地与集群内其他服务进行通信。

![](https://wework.qpic.cn/wwpic/418175_fwXS6RlZQx6Cbyh_1668485209/640)

图：需关注集群内部服务之间的东西向网络安全

* 监控与可跟踪性差

另外，我们还需要在每个微服务中加入尝试重连的逻辑来使得整个应用更为健壮；对于服务来讲还有指标(metrics)，组织的运维人员需要关注各个微服务的性能表现如何，比如微服务在一段时间内接收或发送了多少请求、这些请求耗时多久以便找到应用的瓶颈所在，这时开发团队又会在服务中添加监控（如Prometheus）以及跟踪（如zipkin）机制。

![](https://wework.qpic.cn/wwpic/453982_1WVXnSuETtG7odv_1668485209/0)

图：非业务逻辑繁多，压得服务喘不过气了

这时我们看到，微服务的开发团队需要把上述逻辑全部加入到服务中，这就意味着开发团队无法将精力完全集中在业务逻辑本身，而不得不照顾每一个微服务的网络通信和安全等逻辑（上图中灰色部分），最终导致微服务变得十分复杂且不再轻量化。

## 二、**Service Mesh：通过边车模式给微服务做“减负”**

为了解决上述问题，我们尝试将刚才提到的非业务相关逻辑全部塞进一个名为边车(Sidecar)的容器当中。边车可以理解为一个微型的代理，这个代理是个第三方的应用，集群的运维人员通过简单的API就可以对其进行配置，这样我们便可以充分解放开发人员双手，让他们可以更加专注于业务逻辑上面。更重要的是，组织无需考虑将这些代理的配置信息添加到用于微服务部署的yaml文件当中，因为Service Mesh有一个统一的管理平面，它可以自动地将这些代理置入到每个服务对应的Pod当中，此时微服务之间的通信完全可以通过这些代理来执行了，我们将服务与服务之间通信的网络层+统一的管理平面+所有代理的组合，简单地称之为“Service Mesh”

![](https://wework.qpic.cn/wwpic/416010_hkUmDohITmmmlhP_1668485209/0)

图：Service Mesh示意图

Service Mesh专门针对云原生应用，是处理微服务之间通信的基础设施，最大的作用是将Service之间的网络通信和管理从业务中完全剥离，同时实现微服务架构下网络流量的统一管理。Service Mesh具备三大特点：可观察性、流量控制与安全；其中安全相关的能力主要体现在服务的认证、服务间通讯的加密、安全相关策略的强制执行等方面。

![](https://wework.qpic.cn/wwpic/513838_-oNFpnmwRUaaCYi_1668485209/0)

图：通过Service Mesh，让服务化繁为简

目前很多企业还是采用Dubbo、Spring Cloud等基于 SDK 的传统微服务框架进行服务治理来，然而它们大多很难跨语言，比如Spring Cloud主要是支持Java语言的，这违背了微服务可以使用任意语言开发的初衷。更重要的是，这些微服务框架都带有侵入性，在应用开发的时候就需要在代码中嵌入和工具相关的内容，为后续应用的迁移、改造和升级制造了诸多困难。在这个背景下，作为下一代微务治理框架的Service Mesh（服务网格）应运而生。

使用Service Mesh使得开发者无需关心服务之间的那些原本通过服务框架实现的事情，比如Spring Cloud和其他中间件等，现在只管交给Service Mesh就可以了。一言以蔽之：Service Mesh是微服务时代的 TCP/IP 协议，负责服务之间的网络调用、限流、熔断和监控（p.s. We don’t have to be protocol aware）

## 三、**Istio：让Service Mesh模式落地**

Service Mesh是一种架构，而Istio作为践行Service Mesh理念的代表，使其更好地执行。我们刚才提到的代理，在Istio中名为Envoy proxy（以下简称“Envoy”），即数据平面；而管理平面则称为Istiod，负责管理在每个微服务对应Pod中所部署的Envoy，所有对Istio组件的配置全部在Istiod中完成，无需对部署微服务的K8S yaml文件做任何的调整。需要注意的是，我们对所有Envoy的设置全部在Istiod中完成，Istiod会将其自动推送至每一个代理上，一旦配置完成Envoy就可以在不依赖于管理平面情况下来相互通信。

![](https://wework.qpic.cn/wwpic/720349_FGg5Dc51TTqP3OA_1668485209/0)

图：Istio整体架构

* 动态的服务发现

在Istiod中有个中央仓库，里面记录了所有正在运行的Service，当新的微服务上线时会自动的在中央仓库中进行注册，Istio帮助我们自动检测K8S集群中的Service和Endpoints。使用中央仓库，Envoy代理可以查询(query）Endpoints，并将流量发送至相关的服务。

* 安全—证书管理

Istio在容器化网络中扮演着CA的角色，可以为集群中所有的微服务创建证书，并使得在微服务的Envoy代理之间通过TLS安全协议进行通信成为可能。举个例子：比如Web服务器Service想要访问数据库Service，Istio的管理平面Istiod的中央仓库会把Service的证书和Service互访的规则分发到边缘处，据此Web服务器Service和数据库Service会互相证明彼此的身份，同时建立一个Mutual TLS，然后在两者之间会建立一个隧道，两个服务之间所有通信的流量都是加密的。这也是零信任体系在云原生环境中的体现，即我们始终不相信Service之间通信的网络，从而坚持使用基于身份的访问控制和加密来维护微服务业务东西向网络的安全性。

![](https://wework.qpic.cn/wwpic/517429_xuX72ikTThaWav9_1668485209/0)

图：Istio安全架构（橘色星型图标代表证书）

* 良好的可观测性

可观测性通常包括Metrics (指标)、Tracing (追踪)、Logging (日志)三部分。Istio 为网格内所有的服务通信生成详细的遥测数据。这种遥测技术让 Isito 提供了服务行为的可观察性，使运维人员能够排查故障、维护和优化应用程序，而不会给服务的开发人员带来任何额外的负担。

![](https://wework.qpic.cn/wwpic/785782_VcJ2g98bQcWnWAc_1668485209/0)

图：Envoy收集所有指标和追踪数据并传递至管理平面

## 四、**当安全与Service Mesh相遇**

由于应用架构变革，云原生应用遵循面向微服务化的设计方式，从而导致服务数量激增、配置复杂等问题；与此同时，微服务应用也为API安全防护带来了新的挑战：1. 随着服务更细颗粒度的划分，API接口的数量激增及调用关系的复杂，API管理将变得更加困难；2. 服务间调用的不断增多使得利用API漏洞进行横向攻击的风险也不断增加，微服务间产生的东西向流量无法通过基于边界的防护方式去检测。综上，我们需要一种适用于微服务环境下的全流量的API防护方法。

![](https://wework.qpic.cn/wwpic/801348_EsAWrPYiTmqk6_P_1668485209/0)

图：夸张的服务数量和服务间调用关系

为此，**绿盟基于Service Mesh（服务网格）开发了云原生API安全方案**，其中云原生WAF结合Service Mesh运行模式，采用轻量级的方式，无感知地接入至每个微服务应用中，无论是南北向还是东西向流量，都配备专有地轻量级WAF容器进行防护。根据业务的不同，可采用不同的WAF安全模块进行精准防护。得益于Envoy接管了进出微服务的所有的流量以及Envoy的过滤器的机制，只需要在Envoy的过滤器中实现API安全防护的能力，我们就得到了一个微服务环境下的全流量的安全防护体系。

![](https://wework.qpic.cn/wwpic/644831_xIZzIbwWTLmefRO_1668485209/0)

图：Service Mesh数据平面流量走向示意图

①  请求发送至Pod, Envoy截获此请求；②  请求经过Envoy事先定义的过滤器（API安全网关）；③  过滤器对请求流量进行检测，判断是否是恶意流量，对非法行为直接阻拦，合法行为放行转发到业务容器；④  业务容器接受到正常请求处理完，返回响应报文；⑤  过滤器对响应流量进行检测，判断是否是恶意流量，对非法行为直接阻拦，合法行为放行响应给请求方。

配合Istio的微服务治理，可快速将WAF容器注入至每个微服务应用中，同时收集每个WAF容器的运行数据进行管里面地统一分析。与传统部署在网络边界处相对笨重的WAF相比，更加适配微服务的云原生WAF，可伴随业务生命周期地变化而变化，从而真正应对未来在云上运行数千个容器的场景，同时提供云原生安全能力的支撑及高效、批量的运维管理。

![](https://wework.qpic.cn/wwpic/739504_ykwayZRNSHGD5EK_1668485209/0)

图：绿盟云原生API防护架构

综上，Service Mesh框架在覆盖流量管理、可观测性的同时，有效地提高微服务的安全性能。针对包括防止中间人攻击、灵活的访问控制、审计工具和使用安全协议进行通信等在内的安全需求，以Istio为代表的开源服务网格可以提供证书管理、透明的TLS加密，以及身份验证和授权工具来保护微服务业务。另外，我们还可以利用Service Mesh架构，将WAF容器注入至每个微服务应用中，以自适应的方式补充微服务环境下API的安全能力，从而保证云原生业务的安全性。

参考文献：

[1] https://jimmysong.io/blog/what-is-a-service-mesh/?from\_wecom=1 什么是Service Mesh（服务网格)

[2] https://zhuanlan.zhihu.com/p/111244353?from\_wecom=1 kubernetes service 原理解析

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/weeklyreport46/)

[Next](https://blog.nsfocus.net/dynamorio-9/)

### Meet The Author

李睿捷

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)