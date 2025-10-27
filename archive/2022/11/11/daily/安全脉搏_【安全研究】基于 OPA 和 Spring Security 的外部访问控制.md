---
title: 【安全研究】基于 OPA 和 Spring Security 的外部访问控制
url: https://www.secpulse.com/archives/190847.html
source: 安全脉搏
date: 2022-11-11
fetch_date: 2025-10-03T22:21:33.668207
---

# 【安全研究】基于 OPA 和 Spring Security 的外部访问控制

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 【安全研究】基于 OPA 和 Spring Security 的外部访问控制

[安全管理](https://www.secpulse.com/archives/category/construction/securityissue)

[安全狗](https://www.secpulse.com/newpage/author?author_id=32873)

2022-11-10

20,523

↑ 点击上方 关注我们

**译者导读**

CNCF的毕业项目Open Policy Agent（OPA）, 为策略决策需求提供了一个统一的框架与服务。它将策略决策从软件业务逻辑中解耦剥离，将策略定义、决策过程抽象为通用模型，实现为一个通用策略引擎，可适用于广泛的业务场景，比如：判断某用户可以访问哪些资源、允许哪些子网对外访问、工作负载应该部署在哪个集群、容器能执行哪些操作系统功能、系统能在什么时间被访问。需要注意的是，OPA 本身是将策略决策和策略施行解耦，OPA 负责相应策略规则的评估，即决策过程，业务应用服务需要根据相应的策略评估结果执行后续操作，策略的施行是业务强相关，仍旧由业务应用来实现[1]。

这篇译文是笔者对博文《EXTERNALIZED AUTHORIZATION USING OPA AND SPRING SECURITY》的汉化[2]。博文主要介绍基于 OPA 和 Spring Security 对Java WEB应用进行外部访问控制的技术实践（在这里对博文的背景做一定的补充介绍：无论是云原生应用还是传统单体应用，都面临着**“失效的访问控制”**以及**“失效身份认证”**这两类漏洞的严峻风险。这两类漏洞均“跻身”OWASP TOP10 2017以及OWASP TOP10 2021榜单，可谓“老大难”问题；并且，云原生应用带来了API应用接口爆发式增长、对策略设置的灵活性要求提高的挑战；面对这样的风险与挑战，**OPA可发挥其在业务场景“判断某用户可以访问哪些资源”的优势**，帮客户缓解该问题）。

下面将进入译文部分。若读者朋友能够在阅读之后能收获对OPA技术思路的初步认识，甚至对OPA相似业务场景下能力和服务的研发有所助益，笔者将不胜荣幸。文中若有错漏之处，恳请读者朋友能帮忙指正。

**前言**

虽然OAuth2和OIDC已经成为访问控制的事实标准，流行度很广，但现有的访问控制标准（如XACML、UMA）难以落地甚至使用。因此开发人员继续推出自己的解决方案，但实现起来常常费时费力，增加了维护成本。

在本教程中，我们将探究****如何通过使用********Open Policy Agent********和********Spring Security********将决策外部化********以********简化访问控制********模块****。

**一、目标**

通常，任何公开 API 的服务都需要“身份认证”（authentication）和“访问控制”（authorization）。虽然这两个术语听起来很相似，但二者在安全的作用方面有着根本的不同。“身份认证”是确定身份的过程，“访问控制”是确定权限的过程。二者都是非常关键的主题，因为对它们的关注不足可致最常见的漏洞产生（参考OWASP Top10），今天我们将****重点关注********“访问控制”****。

“访问控制”大致可以分为两类：粗粒度（如RBAC（Role-Based Access Control，基于角色的访问控制））和细粒度（如ABAC（Attribute-Based Access Control，基于属性的访问控制），也称为PBAC（Policy-Based Access Control，基于策略的访问控制））。

通常，在区域边界实施粗粒度访问控制策略，但更细粒度的访问控制策略是需要在服务级别实现和实施的。这导致服务的安全性难以被构建，并且安全策略与业务逻辑的紧密耦合，因此对开发人员的生产力产生负面影响。我们的目标是将访问控制外部化，这允许开发人员简单地实现核心业务功能并重用公共模块进行访问控制，同时访问策略变得集中，因此在更改策略时不需要更改单个服务的代码。

**二、开放策略代理**

开放策略代理（OPA） 是一个开源策略引擎，它提供了一个简单的 API 便于用户将策略决策委托给它。当服务需要做出策略决策时，它会查询 OPA 并提供结构化数据作为输入。OPA 根据策略和数据评估输入并生成输出，输出也可以是任意数据结构，不限于简单allow/deny响应。OPA 策略用称为 Rego 的高级声明性语言表示。更多关于 OPA 和 Rego 的信息可以在官方文档中找到。

**1****运行**

若要做演示，只需从GitHub 版本[3]下载 OPA 二进制文件并将其作为服务器运行即可：

|  |
| --- |
| ./opa run --server |

或者使用官方的 OPA Docker镜像运行：

|  |
| --- |
| docker run -p 8181:8181 openpolicyagent/opa run --server |

**2****策略**

让我们创建一个名为policy.rego的文件并在其中编写一个简单的策略来拒绝所有请求：

|  |
| --- |
| package authz  default allow = false |

我们将使用 Policy API 来创建和更新策略：

|  |
| --- |
| curl -X PUT --data-binary @policy.rego localhost:8181/v1/policies/authz |

**3****数据**

通常，OPA 策略需要一些数据来做出决策，可以使用各种方法将这些数据加载到 OPA 中。使用哪种方法通常取决于数据的大小和更新的频率。此外，加载数据的方式决定了在编写策略时访问它的方式。通过策略决策请求发送的数据可通过输入变量进行访问。异步加载的数据始终通过数据变量进行访问。

对于我们的示例，我们将使用其中的两种方法。其中一部分数据作为输入，另一部分数据包含组织中用户的层次结构（如图1所示），我们将使用其 Data API 推送到 OPA。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190847-1668063375.png)图 1 组织架构图

为此，我们创建一个名为data.json的文件，其内容如下：

|  |
| --- |
| [    {"name": "alice", "subordinates": ["bob", "john"]},    {"name": "bob", "subordinates": ["carol", "david"]},    {"name": "carol", "subordinates": []},    {"name": "david", "subordinates": []},    {"name": "john", "subordinates": []}  ] |

并将其加载到 OPA 中：

|  |
| --- |
| curl -X PUT -H "Content-Type: application/json" -d @data.json localhost:8181/v1/data/users |

##

**三、应用程序**

现在我们需要构建一个服务，我们将为其进行访问控制。它将是一个简单的基于 Spring Boot 的 Web 应用程序，提供用于访问两种资源的 API：salaries（薪水）和documents（文档）。

**1****依赖项**

首先，我们添加必要的依赖项：

|  |
| --- |
| <dependency>      <groupId>org.springframework.boot</groupId>      <artifactId>spring-boot-starter-web</artifactId>  </dependency>  <dependency>      <groupId>org.springframework.boot</groupId>      <artifactId>spring-boot-starter-security</artifactId>  </dependency>  <dependency>      <groupId>org.springframework.boot</groupId>      <artifactId>spring-boot-starter-data-jpa</artifactId>  </dependency>  <dependency>      <groupId>com.h2database</groupId>      <artifactId>h2</artifactId>      <scope>runtime</scope>  </dependency> |

**2****Salary组件**

接下来，我们创建一个实体类和标准的分层架构组件来表示Salary：

|  |
| --- |
| @Entity  public class Salary {        @Id      @GeneratedValue(strategy = GenerationType.IDENTITY)      private Long id;        @Column(unique = true)      private String username;      private double amount;        // getters, setters and overriden methods from UserDetails  } |

|  |
| --- |
| @Repository  interface SalaryRepository extends CrudRepository<Salary, Long> {      Optional<Salary> findByUsername(String username);  } |

|  |
| --- |
| @Service  public class SalaryService {        private final SalaryRepository repository;        public SalaryService(SalaryRepository repository) {          this.repository = repository;      }        public Salary getSalaryByUsername(String username) {          return repository.findByUsername(username)                  .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT\_FOUND));      }  } |

|  |
| --- |
| @RestController  @RequestMapping("/salary")  public class SalaryController {        private final SalaryService service;        public SalaryController(SalaryService service) {          this.service = service;      }        @GetMapping("/{username}")      public Salary getSalary(@PathVariable String username) {          return service.getSalaryByUsername(username);      }  } |

**3****Document组件**

然后我们创建相同类型的类来表示Document：

|  |
| --- |
| @Entity  public class Document {        @Id      @GeneratedValue(strategy = GenerationType.IDENTITY)      private Long id;      private String content;      private String owner;            // getters and setters  } |

|  |
| --- |
| @Repository  interface DocumentRepository extends CrudRepository<Document, Long> {  } |

|  |
| --- |
| @Service  public class DocumentService {        private final DocumentRepository repository;        public DocumentService(DocumentRepository repository) {          this.repository = repository;...