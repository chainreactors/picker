---
title: RBAC 和 Keto（Go RBAC 框架）
url: https://www.anquanke.com/post/id/289298
source: 安全客-有思想的安全新媒体
date: 2023-06-17
fetch_date: 2025-10-04T11:44:14.048803
---

# RBAC 和 Keto（Go RBAC 框架）

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# RBAC 和 Keto（Go RBAC 框架）

阅读量**703190**

发布时间 : 2023-06-16 17:57:09

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

1. RBAC
   RBAC（Role-Based Access Control）是最通用的权限访问控制系统。其思想是，不直接授予具体用户各种权限，而是在用户集合和权限集合之间建立角色集合。每种角色对应一组相应的权限，一旦用户被分配适当的角色，他就拥有此角色的所有权限。这样做的好处是，不必在每次创建用户时都分配权限，只要给用户分配相应的角色即可，并且角色的权限变更比用户的权限变更要少得多，这将简化用户的权限管理，减少系统开销。
   RBAC 有三种模型。
   1.1. RBAC0
   它是其它 RBAC 模型的基础。在该模型中，用户和角色之间是多对多的关系，每个角色至少有一个权限。
   [图片]
   1.2. RBAC1
   在 RBAC0 的基础上，引入角色间的继承关系，即角色有上下级的区别。角色间的继承关系可分为一般继承关系和受限继承关系。一般继承关系要求角色继承关系是绝对偏序关系，允许角色间的多继承。而受限继承关系则进一步要求角色继承关系是树状结构，实现角色间的单继承。
   [图片]
   1.3. RBAC2
   在 RBAC0 的基础上，引入角色的访问控制。该模型有以下两种约束：

* 静态职责分离
  + 互斥角色：互斥角色是指各自权限可以互相制约的角色。对于这类角色，用户在某次活动中只能被分配其中的一个角色，不能同时获得多个角色的使用权。比如在审计活动中，一个用户不能被同时分配会计角色和审计员角色
  + 基数约束：一个角色被分配的用户数量受限；一个用户可拥有的角色数量受限；一个角色对应的访问权限数目也受限，以控制高级权限的分配。比如公司的管理层是有限的
  + 先决条件角色：要想获得较高的权限，首先要拥有低一级的权限
* 动态职责分离
  + 运行时互斥：动态地约束用户拥有的角色，比如一个用户可以拥有两个角色，但是运行时只能激活其中一个
    [图片]

---

1. Keto 介绍
   2.1. 介绍
   Ory Permissions（基于开源的 Ory Keto Permission Server）是第一个、唯一的“Zanzibar：Google 的一致的、全球的授权系统”的开源实现。
   如果你需要知道是否允许一个用户做某些事情 – Ory Permissions 非常适合你。
   Ory Permission 实现基本的 API 契约，用于使用 HTTP 和 gRPC API 管理和检查关系（“权限”）。未来的版本将包含用户集重写（比如 RBAC 风格的角色-权限模型）、Zookies 等特性。
   2.2. 安装
   Ory 软件可以运行在任何操作系统（FreeBSD、macOS、Linux、Windows、…）上，支持所有主要 CPU（ARM64、ARMv7、x86\_64、x86、…）平台。
   Ory 提供预构建的二进制、Docker 镜像，支持多种包管理器。
   详情请参考：<https://www.ory.sh/docs/keto/install>
   2.3. 性能
   本文档解释 Ory Keto 的时间复杂度（time complexity）。稍后将分析和添加主内存复杂度。我们只检查评估引擎（检查和展开 API），因为其它部分主要由依赖决定，比如你选择的数据库、消息的解/编码。为清晰起见，给定的示例忽略命名空间（namespace）。
   2.3.1. 检查引擎
   本质上，检查引擎（check-engine）假设关系元组（relation tuple）和它们的间接组合成一个无环有向图，被称为关系图（the graph of relations）。
   思考下面的示例：
   file#access@(file#owner) // probably defined via subjectset rewrites
   file#access[@user1](https://github.com/user1 "@user1") // access was granted directly
   file#owner[@user2](https://github.com/user2 "@user2") // file owner record; indirectly gets access
   被解释为下图：
   [图片]
   通过从 object 开始搜索图，经过 relation，尝试到达 user 的方式，计算object#relation[@user](https://github.com/user "@user") 形式的检查请求。如果存在这样的路径，那么允许请求。
   Ory Keto 使用的图遍历算法是广度优先搜索。在最坏的情况下，时间复杂度是 O(n+e)，其中 n 是从节点 object#relation 通过 e 条边可到达的节点数。重排列，时间和空间复杂度都是 o(b^d)，其中 b 是从搜索根见到的最大宽度，d 是最大深度。
   这意味着复杂性很大程度上取决于图的结构。如果图包含深度嵌套的间接（indirection），需要多次递归调用解析这些间接。类似地，如果有广度嵌套的间接，Ory Keto 必须能解析所有间接。目标是以只需解析少许间接的方式，设计 ACL 元组。了解更多关于 ACL 设计的最佳实践。
   因此，我们认为常规的基准测试不会产生任何有意义的结果。因此，我们将在稍后添加与其它类似项目的比较。
   2.3.2. 扩展引擎
   与检查引擎遍历关系元组（relation tuple）图的方式类似，扩展引擎构建它遇到的所有集合操作的树。它解析从请求的主体集合（subjectset）开始到指定深度的所有间接（indirection）。因为它也是用广度优先搜索，时间和空间复杂度线性依赖于从请求的主体集合可到达的节点。同样的性能考虑也适用于这里，需要特别注意的是，请求较低的深度将进一步限制操作的复杂度。如果关系元组是深嵌套和/或广泛嵌套的，那么返回的树也可能很快超过合理的大小限制。
   2.3.3. 参考

* Wikipedia Breadth-first search
  2.4. 快速入门：猫视频示例
  本示例介绍一个视频共享服务。视频被组织在目录中。每个目录有一个所有者，每个视频的所有者与其父目录相同。所有者有视频文件的特权，无需单独地在 Ory Keto 中建模。在本例中，建模的其它权限只有“视图访问”，每个所有者都有对其对象的视图访问权，也能授予其它用户该权限。视频共享应用程序将特殊的 \* 用户 ID 解释为任何用户，保护匿名用户。注意，Ory Keto 对该主体的解读与其它主体并无不同。它不知道关于目录结构或诱发的所有权的任何事情。
  术语：
  “Keto 客户端”是与 Keto 进行交互的应用程序。在本例中，我们将视频共享服务后端称为 Keto 客户端。
  2.4.1. 开始示例
  首先，安装 Keto。
  现在可以使用 docker-compose 或 bash 脚本启动示例。bash 脚本需要你在 $PATH 中拥有 keto 二进制程序。
  或者，使用 Docker 自动获取所需的镜像。

  # clone the repository if you don’t have it yet

  git clone <https://github.com/ory/keto.git> && cd keto

docker-compose -f contrib/cat-videos-example/docker-compose.yml up

# or

./contrib/cat-videos-example/up.sh

# output: all initially created relation tuples

# NAMESPACE OBJECT RELATION NAME SUBJECT

# videos /cats/1.mp4 owner videos:/cats#owner

# videos /cats/1.mp4 view videos:/cats/1.mp4#owner

# videos /cats/1.mp4 view \*

# videos /cats/2.mp4 owner videos:/cats#owner

# videos /cats/2.mp4 view videos:/cats/2.mp4#owner

# videos /cats owner cat lady

# videos /cats view videos:/cats#owner

2.4.2. 系统状态
在当前状态下，只有一个用户名为 cat lady 的用户添加了视频。两个视频都在 cat lady 拥有的 /cat 目录下。文件 /cats/1.mp4 可被任何人（\*）查看，而 /cats/2.mp4 没有额外的共享选项，因此只能被它的所有者 cat lady 访问。关系元组（relation tuple）的定义位于 contrib/cat-videos-example/relation-tuples 目录。
2.4.3. 模拟视频共享程序
现在可以打开第二个终端来运行查询，就像视频服务客户端所做的那样。在本例中，我们将使用 Keto CLI 客户端。如果想在 Docker 内运行 Keto CLI，在终端会话中，设置别名
alias keto=”docker run -it —network cat-videos-example\_default -e KETO\_READ\_REMOTE=\”keto:4466\” oryd/keto:v0.7.0-alpha.1”
另外需要设置远程端点，以便 Keto CLI 知道连接到哪里（如果使用 Docker，则不需要）：
export KETO\_READ\_REMOTE=”127.0.0.1:4466”
2.4.3.1. 检查传入请求
首先，我们收到一个匿名用户的请求，想要查看 /cats/2.mp4。客户端必须询问 Keto，允许还是拒绝该操作。

# Is “\*” allowed to “view” the object “videos”:”/cats/2.mp4”?

keto check “\*” view videos /cats/2.mp4

# output:

# Denied

我们已经讨论过该请求应该被拒绝，但在实际操作中看到该结果是非常好的。
现在 cat lady 想要改变 /cats/1.mp4 的查看权限。为此，视频服务应用程序必须展示允许查看该视频的所有用户。它使用 Keto 的扩展 API（expand-API）获取这些数据：

# Who is allowed to “view” the object “videos”:”/cats/2.mp4”?

keto expand view videos /cats/1.mp4

# output:

# ∪ videos:/cats/1.mp4#view

# ├─ ∪ videos:/cats/1.mp4#owner

# │ ├─ ∪ videos:/cats#owner

# │ │ ├─ ☘ cat lady️

# ├─ ☘ \*️

我们可以看到完整的主体集合扩展。第一个分支
videos:/cats/1.mp4#view
表示允许对象的每个所有者查看
videos:/cats/1.mp4#owner
下一步，我们看到对象的所有者是 /cats 的所有者
videos:/cats#owner
我们看到 cat lady 是 /cats 的所有者。
注意，没有直接关系元组（relation tuple）授予 cat lady 对 /cats/1.mp4 的视图访问权限，因为这是通过所有权关系间接定义的。
但是，特殊用户 \* 被直接授予对对象的视图访问权限，因为它是扩展树的第一级叶子。下面的 CLI 命令可以证明这一点：

# Is “\*” allowed to “view” the object “videos”:”/cats/1.mp4”?

keto check “\*” view videos /cats/1.mp4

# output:

# Allowed

## 更新视图权限将在稍后的阶段添加到这里。

1. Keto 概念
   3.1. 关系元组
   关系元组（relation tuple）是 Ory Keto 的访问控制语言的底层数据类型。它编码对象（objects）和主体（subjects）之间的关系。关系元组与定义和配置它的关系的命名空间（namespace）相关联。下面的 BNF 语法（BNF grammar）描述该文档和 Ory Keto 里使用的编码。
   注意：
   为提升可读性，在示例中经常忽略命名空间，但总是严格需要的。
   <relation-tuple> ::= <object>‘#’relation’@’<subject>
   <object> ::= namespace’:’object\_id
   <subject> ::= subject\_id | <subject\_set>
   <subject\_set> ::= <object>‘#’relation
   关系元组
   object#relation[@subject](https://github.com/subject "@subject")
   可被转换为句子“subject 在 object 上有 relation”。
   3.1.1. 关系元组的效果（Effect）
   关系元组的效果是在命名空间配置（namespace configuration）中定义的关系的效果。它可以是并集（布尔 or）、交集（布尔 and）或排除（布尔 not）中的一个。
   3.1.2. 基础示例
   前往 basic full feature example 查看带上下文的示例。
   3.2. 命名空间
   Ory Keto 使用命名空间（namespace）的概念组织关系元组（relation tuples）。命名空间拥有定义关系，以及其它重要值（see reference）的配置。与其它应用程序不同，Ory Keto 不隔离命名空间。主体集合（subject sets）可以从一个命名空间交叉引用到另一命名空间。命名空间的用途是将数据分割成有条理的分区，每个分区有它的相关配置。
   3.2.1. 对象的作用域
   应用程序也可以使用命名空间来限定对象（objects）的范围，因为 Ory Keto 仅比较命名空间内的对象。比如，Ory Keto 知晓下面的关系元组
   // user1 有权限访问目录 foo
   directories:foo#access[@user1](https://github.com/user1 "@user1")
   // user2 有权限访问文件 foo
   files:foo#access[@user2](https://github.com/user2 "@user2")
   下面的检查（check）请求
   // user2 有权限访问目录 foo 吗？
   directories:foo#access[@user2](https://github.com/user2 "@user2")
   // user1 有权限访问文件 foo 吗？
   files:foo#access[@user1](https://github.com/user1 "@user1")
   都计算为 false（即拒绝）。
   反之亦然，所有包含对象的关系元组必须在相同的命名空间中引用相同的 object。
   3.2.2. 命名约定
   命名空间应该以它们描述的对象的类型的复数形式命名（比如 files、chats、organizations）。命名空间中的关系（relation）应该是一个描述主体（subject）到对象（object）之间的关系的词。作为经验之谈，每个关系元组应该转换成类似这样的句子：
   Subject 在 namespace 的一个 object 上有 relation。
   比如：
   // 好示例

files:8f427c01-c295-44f3-b43d-49c3a1042f35#write[@02a3c847](https://github.com/02a3c847 "@02a3c847")-c903-446a-a34f-dae74b4fab86
groups:43784684-103e-44c0-9d6c-db9fb265f617#member[@b8d00059](https://github.com/b8d00059 "@b8d00059")-b803-4123-9d3d-b3613bfe7c1b
directories:803a87e9-0da0-486e-bc08-ef559dd8e034#child@(files:11488ab9-4ede-479f-add4-f1379da4ae43#*)
files:11488ab9-4ede-479f-add4-f1379da4ae43#parent@(directories:803a87e9-0da0-486e-bc08-ef559dd8e034#*)

// 坏示例

// 命名空间未描述对象的同源类型
tenant-1-objects:62237c27-19c3-4bb1-9cbc-a5a67372569b#access[@7a012165](https://github.com/7a012165 "@7a012165")-7b21-495b-b84b-cf4e1a21b484
// relation 描述 ob...