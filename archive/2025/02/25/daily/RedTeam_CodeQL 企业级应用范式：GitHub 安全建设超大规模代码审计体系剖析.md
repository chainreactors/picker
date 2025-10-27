---
title: CodeQL 企业级应用范式：GitHub 安全建设超大规模代码审计体系剖析
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjAxNjc5OQ==&mid=2247484244&idx=1&sn=68012180bdabe8fb5aeb77cb030cfa3f&chksm=c006cba4f77142b2883250c6c62c6e2d56248b340d3fa854b8b5351226d64b1bbf0128ab85b3&scene=58&subscene=0#rd
source: RedTeam
date: 2025-02-25
fetch_date: 2025-10-06T20:38:42.080686
---

# CodeQL 企业级应用范式：GitHub 安全建设超大规模代码审计体系剖析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6USuqjXjYk4a0icgBChRCsrHe1sqOCYE7iaMicrib3iahTr68ibLicrG8mKolM42BYutfM7vazgfY0DSVPdURG1mV0zlA/0?wx_fmt=jpeg)

# CodeQL 企业级应用范式：GitHub 安全建设超大规模代码审计体系剖析

原创

tonghuaroot

RedTeam

**GitHub 通过 CodeQL 实现大规模安全防护，结合自定义查询包、自动化变种分析与提示性告警，构建高效漏洞检测体系，为开发者提供企业级代码安全实践范本。**

## 前言

GitHub 的产品安全工程团队编写代码并实现工具，帮助确保 GitHub 背后的代码的安全。我们使用 GitHub GHAS 来发现、跟踪和修复漏洞，并在大规模上执行安全编程标准。我们大量依赖的工具之一是CodeQL，它用于分析我们的代码。

CodeQL 是 GitHub 的静态分析引擎，支持自动化安全分析。您可以像查询数据库一样查询代码，它提供了一种比传统的代码库文本搜索更强大的分析方式，可以揭示代码中的问题。

以下内容将详细介绍我们如何使用 CodeQL 来保持 GitHub 的安全性，并且您可以学习如何将这些经验应用到您自己的组织中。您将了解我们为何以及如何使用：

* 自定义查询包（以及我们如何创建和管理它们）。
* 自定义查询。
* 变种分析，以揭示潜在的不安全编程实践。

## 大规模启用 CodeQL

在 GitHub，我们以多种方式使用 CodeQL。

1. **默认设置**：使用默认安全扫描组件默认安全扫描组件满足了我们超过 10,000 个仓库的需求。通过这些设置，PR会自动获得 CodeQL 的安全扫描。
2. **高级设置**：使用自定义查询包 一些仓库，比如我们庞大的 Ruby 单体应用，需要投入更多的资源，因此我们使用高级设置，配合包含自定义查询的查询包进行更精细的定制。
3. **多仓库变种分析（MRVA）**：我们使用 MRVA 进行变种分析和快速审计。同时，我们也编写自定义 CodeQL 查询来检测特定于 GitHub 代码库的代码模式，或者是我们希望安全工程师手动代码审计的模式。

我们在单体应用上使用的自定义 Actions 工作流步骤非常简单，示例如下：

```
- name: Initialize CodeQL
    uses: github/codeql-action/init@v3
    with:
      languages: ${{ matrix.language }}
      config-file: ./.github/codeql/${{ matrix.language }}/codeql-config.yml
```

我们的 Ruby 配置比较标准，但高级设置提供了多种配置选项，使用自定义配置文件。其中一个有趣的部分是 `packs` 选项，这是我们在 CodeQL 分析中启用自定义查询包的方式。这个包包含了我们为 Ruby 编写的 CodeQL 查询，专门用于 GitHub 的代码库。

接下来，我们将深入探讨我们为什么这么做，以及如何实现！

## 发布的 CodeQL 查询包

最初，我们将 CodeQL 查询文件直接发布到 GitHub 单体仓库中，但由于以下几个原因，我们放弃了这种方法：

* 每次新查询或更新查询时，都需要经过生产部署流程。
* 不包含在查询包中的查询没有预编译，会导致 CI 中的 CodeQL 分析变慢。
* 我们的CodeQL查询测试套件作为单体应用的 CI 任务运行。当发布新版本的 CodeQL CLI 时，有时会因为查询输出的变化导致查询测试失败，即使PR中的代码没有变化。这常常会引起工程师的困惑和沮丧，因为测试失败与他们的PR没有关系。

通过将查询包发布到GitHub 容器注册表(GCR)，我们简化了流程，并消除了许多问题，使得发布和维护 CodeQL 查询变得更加容易。所以，虽然可以将自定义 CodeQL 查询文件直接部署到仓库中，我们推荐将 CodeQL 查询作为查询包发布到 GCR，以便更轻松地部署并加速迭代。

## 创建我们的查询包

在设置自定义查询包时，我们面临了几个考虑因素，特别是在管理依赖项，比如`ruby-all`包时。

为了确保我们的自定义查询保持可维护性和简洁性，我们扩展了默认查询套件中的类，例如`ruby-all`库。这样我们就能利用现有的功能，而不是重新发明轮子，从而保持查询的简洁性和可维护性。然而，CodeQL 库 API 的变化可能会引入 breakchange，可能会使我们的查询过时或导致报错。由于 CodeQL 作为我们 CI 的一部分运行，我们希望最大限度地减少这种情况发生的可能性，因为这可能会导致工程师的沮丧和让开发者对安全团队丧失信任。

我们针对最新版本的`ruby-all`包开发查询，确保我们始终在使用最新的功能。为了减轻 breakchange 影响 CI 的风险，我们在准备发布时会固定`ruby-all`的版本，并将其锁定在`codeql-pack.lock.yml`文件中，这确保了在部署查询时，我们使用的是经过测试的特定版本，从而避免了由于意外更新而出现问题。

这里是我们如何管理这个设置的：

* 在我们的 qlpack.yml 文件中，我们设置了依赖关系，使用`ruby-all`的最新版本
* 在开发过程中，这个配置在运行`codeql pack init`时会拉取最新版本，确保我们始终保持更新。

```
// Ourcustomquerypack'sqlpack.yml

library:false
name:github/internal-ruby-codeql
version:0.2.3
extractor:'ruby'
dependencies:
codeql/ruby-all:"*"
tests:'test'
description:"Ruby CodeQL queries used internally at GitHub"
```

*在发布之前，我们会在`codeql-pack.lock.yml`文件中锁定版本，指定精确版本，以确保稳定性，并防止在 CI 中出现问题。*

```
// Ourcustomquerypack'scodeql-pack.lock.yml

lockVersion:1.0.0
dependencies:
...
codeql/ruby-all:
   version:1.0.6
```

这种方法让我们能够在利用`ruby-all`包的最新功能的同时，确保发布时的稳定性。

我们还有一组CodeQL单元测试，通过它们我们可以快速判断是否会在发布查询包之前导致报错c。这些测试用例作为我们查询包仓库中的 CI 流程的一部分运行，为我们提供了早期问题检测的功能。我们强烈推荐为您的自定义 CodeQL 查询编写单元测试，以确保稳定性和可靠性。

总的来说，发布新 CodeQL 查询的基本流程如下：

* 提交包含新查询的 PR。
* 为新查询编写单元测试。
* 合并 PR。
* 在新 PR 中递增查询包版本。
* 运行`codeql pack init`以解析依赖项。
* 根据需要修正单元测试。
* 将查询包发布到 GitHub 容器注册表(GCR)。
* 配置了查询包的仓库将开始使用更新后的查询。

我们发现这个流程在确保发布查询包的稳定性的同时，也平衡了团队的开发体验。

## 配置我们的仓库使用自定义查询包

我们在此不会提供通用的配置建议，因为最终配置取决于您的组织如何部署代码。我们没有在CodeQL配置文件中锁定我们的包版本（如上所示）。相反，我们选择通过将 CodeQL 包发布到 GCR 来管理版本控制。这使得 GitHub 单体应用检索到查询包的最新发布版本。要回滚更改，我们只需重新发布包。在之前的案例中，我们发布了一个查询，发现它产生了很多误报，我们能够在不到 15 分钟的时间内发布一个新版本的包，删除了那个查询。这比我们通过合并 PR 回滚 CodeQL 配置文件中的版本所需的时间要快。

发布查询包到 GCR 时遇到的一个问题是，如何轻松地让该包可供多个仓库访问。我们探索了几种方法。

* **为各个仓库授予访问权限**。在包管理页面，您可以为各个仓库授予访问包的权限。对于我们来说，这不是一个好的解决方案，因为我们有太多仓库，手动操作不可行，且目前没有通过 API 配置的方式。
* **为 CodeQL 操作运行器生成个人访问令牌**。我们可以生成一个个人访问令牌(PAT)，该令牌具有读取我们组织所有包的权限，并将其添加到 CodeQL 操作运行器中。然而，这会要求我们管理一个新的令牌，并且看起来权限过于宽泛，因为它可以读取我们所有的私有包，而不是我们明确允许它访问的包。
* **通过关联的仓库提供访问权限**。我们最终实施了我们探索的第三种解决方案。我们将仓库与包关联，并允许包继承关联仓库的访问权限。

## 自定义 CodeQL 查询包

我们编写了各种自定义查询，以便在我们的环境中使用。这些查询涵盖了 GitHub 特定的代码模式，这些模式在默认的 CodeQL 查询包中没有包含。这样，我们就能根据公司和代码库的特定模式和偏好定制分析。通过我们的自定义查询包，我们会针对如下内容进行告警：

* 特定于 GitHub 代码的高风险 API，如果接收到未经过滤的用户输入，可能会导致安全问题。
* 使用特定的 Rails 内建方法，我们有更安全的自定义方法或函数。
* 在 REST API 端点定义和 GraphQL 对象/突变定义中未使用必要的授权方法。
* 需要工程师定义访问控制方法的 REST API 端点和 GraphQL 突变。（特别是查询检测到缺少此方法定义，以确保这些端点正在检查访问者的权限。）
* 使用签名令牌时，提醒工程师在使用时将产品安全部门作为审查者。

自定义查询更多是用于教育目的，而不是阻止代码的发布。例如，我们希望在工程师使用ActiveRecord::decrypt方法时发出警告。该方法通常不应在生产代码中使用，因为它会导致加密列被解密。我们使用查询元数据中的推荐严重性级别，使这些告警更像是信息性告警。这意味着它可能会在 PR 中触发告警，但不会导致 CodeQL CI jobs 执行失败。我们使用这种较低的严重性级别，让工程师在不立即被阻断的情况下评估新查询的影响。此外，这个告警级别不会通过我们的基础设施项目进行追踪，这意味着它不需要立即处理，反映了查询随着我们继续改进其相关性和风险评估而不断完善的成熟度。

```
/**
 * @id rb/github/use-of-activerecord-decrypt
 * @description Do not use the .decrypt method on AR models, this will decrypt all encrypted attributes and save
 * them unencrypted, effectively undoing encryption and possibly making the attributes inaccessible.
 * If you need to access the unencrypted value of any attribute, you can do so by calling my_model.attribute_name.
 * @kind problem
 * @severity recommendation
 * @name Use of ActiveRecord decrypt method
 * @tags security
 *      github-internal
 */

import ruby
import DataFlow
import codeql.ruby.DataFlow
import codeql.ruby.frameworks.ActiveRecord

/** Match against .decrypt method calls where the receiver may be an ActiveRecord object */
class ActiveRecordDecryptMethodCall extends ActiveRecordInstanceMethodCall {
ActiveRecordDecryptMethodCall() { this.getMethodName() = "decrypt" }
}

from ActiveRecordDecryptMethodCall call
select call,
  "Do not use the .decrypt method on AR models, this will decrypt all encrypted attributes and save them unencrypted.
```

另一个教育性查询是上面提到的，当我们检测到定义REST API端点的类中缺少`control_access`方法时。如果PR中引入了一个没有`control_access`的端点，PR中将出现一个评论，表示未找到`control_access`方法，而这是REST API端点的必需项。这将通知审查员潜在的问题，并提示开发人员进行修复。

```
/**
 * @id rb/github/use-of-activerecord-decrypt
 * @description Do not use the .decrypt method on AR models, this will decrypt all encrypted attributes and save
 * them unencrypted, effectively undoing encryption and possibly making the attributes inaccessible.
 * If you need to access the unencrypted value of any attribute, you can do so by calling my_model.attribute_name.
 * @kind problem
 * @severity recommendation
 * @name Use of ActiveRecord decrypt method
 * @tags security
 *      github-internal
 */

import ruby
import DataFlow
import codeql.ruby.DataFlow
import codeql.ruby.frameworks.ActiveRecord

/** Match against .decrypt method calls where the receiver may be an ActiveRecord object */
class ActiveRecordDecryptMethodCall extends ActiveRecordInstanceMethodCall {
ActiveRecordDecryptMethodCall() { this.getMethodName() = "decrypt" }
}

from ActiveRecordDecryptMethodCall call
select call,
  "Do not use the .decrypt method on AR models, this will decrypt all encrypted attributes and save them unencrypted.
```

## 变种分析

变种分析（VA）是指查找安全漏洞的变种的过程。在我们响应 Bug Bounty或安全事件时，这非常有用。我们使用多种工具来执行此操作，包括 GitHub 的代码搜索功能、自定义脚本和 CodeQL。我们通常会先使用代码搜索，查找在多个仓库中与某个漏洞相关的模式。有时这并不够好，因为代码搜索没有语义意识，无法确定给定的变量是否是 Active Record 对象，或者它是否在`if`表达式中使用。要解决这些问题，我们会使用CodeQL。

当我们编写 CodeQL 查询进行变种分析时，我们并不太关心误报，因为目标是为安全工程师提供分析的结果。代码质量的要求也不是特别高，因为这些查询仅在 VA 过程中使用。我们使用 CodeQL 进行变种分析的一些示例如下：

* 我们在哪些地方使用 SHA1 哈希？
* 根据最近的漏洞赏金报告，我们的一个内部 API 端点容易受到 SQL 注入攻击。我们在哪里向该 API 端点传递用户输入？
* Ruby 中某些 HTTP 请求库处理代理设置的方式有问题。我们能否查看在何处实例化了带有代理设置的 HTTP 请求库？

最近的一个例子涉及 Rails 中的一个微妙漏洞。我们想检测代码中是否存在以下条件：

* 使用一个参数查找一个 Active Record 对象。
* 在查找该对象之后，稍后再次使用该参数。

这个条件可能导致不安全的直接对象引用（IDOR）漏洞（国内一般叫越权漏洞），因为 Active Record 查找方法可以接受一个数组。如果代码在一次调用中查找 Active Record 对象，来确定某个实体是否有权访问某个资源，但稍后使用数组中的其他元素来查找对象引用，这可能导致 IDOR 漏洞。编写查询来检测所有这种模式的漏洞是困难的，但我们能够编写一个查询，找出潜在漏洞，并生成一个代码路径清单，供我们手动分析。我们通过 CodeQL 的 MRVA 在大量 Ruby 代码库中运行了这个查询。

查询代码如下：

```
/**
 * @name wip array query
 * @description an array is passed to an AR finder object
 */

import ruby
import codeql.ruby.AST
import codeql.ruby.ApiGraphs
import codeql.ruby.frameworks.Rails
import codeql.ruby.frameworks.ActiveRecord
import codeql.ruby.frameworks.ActionController
import codeql.ruby.DataFlow
import codeql.ruby.Frameworks
import codeql.ruby.TaintTrack...