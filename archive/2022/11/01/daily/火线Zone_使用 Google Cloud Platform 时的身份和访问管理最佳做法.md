---
title: 使用 Google Cloud Platform 时的身份和访问管理最佳做法
url: https://mp.weixin.qq.com/s?__biz=MzI2NDQ5NTQzOQ==&mid=2247497073&idx=1&sn=50aad5714650aee728530bc6d65887c8&chksm=eaa97d51dddef4478ec568408ec644e7f45e9af3a251613a4c7848058ea0fd2c77d55cdb839d&scene=58&subscene=0#rd
source: 火线Zone
date: 2022-11-01
fetch_date: 2025-10-03T21:26:35.287074
---

# 使用 Google Cloud Platform 时的身份和访问管理最佳做法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0Z0LqMyVGaRroicL1WvO1tdrTaMkftU7bKhoThia56c0ncmg1TYOgETtibvzHK6jsqib7uRtcbmmcibn3rXEfiaPEeCg/0?wx_fmt=jpeg)

# 使用 Google Cloud Platform 时的身份和访问管理最佳做法

火线小助手

火线Zone

‍

**本文为翻译文章，原文链接****：https://www.praetorian.com/blog/iam-best-practices-gcp/**

*在 Praetorian，我们的首要任务之一是检查每个客户的身份和访问管理 (IAM) 结构。我们的一些大客户使用谷歌云平台 (GCP)，它是三大云提供商之一，拥有约 8% 的云服务市场份额。在与 GCP 合作期间，我们注意到随着组织的发展，额外的部门和项目会显着增加 IAM 权限的复杂性。*

*这篇博文旨在提供工具和方法，帮助大型组织思考如何最好地组织他们的 IAM 模型。我们将介绍核心 IAM 概念并讨论在 GCP 的层次结构链中逻辑组织资源组的方法，以利用从父资源继承的 IAM 策略。最后，我们将讨论 GCP 中示例组织结构中的三个场景，并使用我们内置的层次结构创建简单的访问条件语句，以便于验证和验证。*

从基础开始

IAM 策略描述了**谁**可以对**哪些资源采取**什么行动。这看起来很简单，但随着组织试图扩展其政策以伴随增长，它可能会变得异常复杂。无论组织规模如何，了解这三个概念中的每一个以及它们如何相互作用对于有效的 IAM 都是必不可少的。

IAM 的第一个构建块是**principal**，它描述了我们定义中的**who**。IAM 策略可以应用于多个 GCP 主体，包括服务帐户、google 帐户、google 组和 google 工作区。

IAM 的第二个构建块是**什么操作。**角色是确定委托人可以执行**什么操作的权限的集合。**以下是三种类型的角色：

* **基本角色：**这些角色包括所有者、编辑者和查看者角色。这些角色具有广泛的权限，Google 和 Praetorian 都不建议使用它们。
* **预定义角色**：这些是 Google 创建的具有细粒度访问控制的角色。
* **自定义角色**：这些是组织创建的角色。自定义角色可以授予用户一组最低权限。

IAM 的第三个构建块是**哪个资源，**它规定了委托人可以在云层次结构中的哪个位置执行其允许的操作。IAM 策略定义了哪些资源具有哪些权限以及哪些组织负责，并将一个或多个委托人与一个或多个角色绑定。图 1 概述了 GCP 的资源层次结构：

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaRroicL1WvO1tdrTaMkftU7bj4z9rJ76uDOWfWrNVKOtaATicicuxOdlNichAibSxJmGT3xe0kB90e6iatA/640?wx_fmt=png)

   *图 1：GCP 中的资源层次结构。*

GCP 用户在组合三个 IAM 构建块时需要牢记 IAM 继承策略。组织可以在任何级别（组织、文件夹、项目和资源）设置 IAM 策略，并且资源将从父资源继承所有策略。生成的权限将是所有策略的联合。

### **拒绝策略和条件语句**

用户可以创建阻止权限的拒绝策略。在显式拒绝中，拒绝策略将始终覆盖允许的权限。这意味着，如果委托人对该关联权限具有拒绝 IAM 策略，即使他们也具有包含该权限的角色，他们也将无法执行操作。相反，隐式拒绝发生在没有任何拒绝或允许许可的策略的情况下。当委托人没有拒绝或允许权限的 IAM 策略时，GCP 默认拒绝它。

条件语句是有效 IAM 策略的重要组成部分，它仅在满足条件时才应用 IAM 策略（即资源具有标签）。这允许通过 GCP 的 IAM 策略继承不适用于子资源的 IAM 策略。虽然我们将在本文中使用标签和条件语句来创建安全的 IAM 模型，但我们也知道条件语句可能会无意中引入 IAM 缺陷。我们将尝试减少示例中的条件语句，以降低复杂性并使它们更易于审计和扩展。

组织架构划分

创建一个经过深思熟虑的组织结构将有助于我们将 IAM 策略置于正确的位置并降低复杂性。在 Praetorian 在多个 GCP 环境中的工作过程中，我们看到了以下按从大到小的划分。请注意，并非所有部门都可能存在或需要。

### **按业务单位划分**

组织经常试图按业务单位安排最高级别的组织结构。对于大型公司，业务部门可以是 Gmail 和 Google 搜索等资源的部门。对于小公司，业务部门可以更具体，如应用程序前端和应用程序后端。

按业务部门划分使公司的计费更加容易。这样做还会在委托人与其业务部门之间建立一对一的关系，因为通常员工不会属于多个业务部门。在 GCP 中，业务部门通常直接映射到组织或文件夹。请注意，业务部门也可以根据公司的需要在以下分组之间切换。

### **按环境类型划分**

在中层，组织倾向于按照生产、测试和质量保证等环境类型来区分 GCP 环境。这通常涉及一对多映射，因为每个员工可能需要访问多个环境来完成其工作职能。环境分离允许公司在接近生产时制定更严格的规则（即，更少的人应该有权进行生产）。在 GCP 中，环境类型通常映射到组织或文件夹。

### **按项目名称/团队名称划分**

较低级别的组织结构通常将 GCP 环境与当前正在开发的项目分开。这通常是一对多的映射，因为员工可以是多个团队和项目的一部分。GCP 环境还允许包含跨所有项目或项目集合的共享资源的共享项目。

图 2 显示了我们的工程师经常遇到的组织结构的示例图片，我们将使用它作为基点来创建一些易于审计和扩展的示例 IAM 策略。

*图 2：我们将从中创建 IAM 策略场景的通用组织结构。*

请注意，这只是 GCP 中一种潜在的组织结构。组织会发现，每种结构化方法都有其自身的成本和收益。

场景

我们现在将讨论公司在设置 GCP 环境时可能经常遇到的三种情况。我们将遍历每个场景并尝试将 IAM 策略置于适当的级别，以使其更具可扩展性和可验证性。

### **要求一：一个用户跨多个业务部门的一个预定义角色**

第一个场景的要求是创建一个 IAM 策略，为我们的 CFO 阅读器提供适用于不同业务部门的*Billing Account Costs Manager预定义角色 (roles/billing.costsManager)。*这将使首席财务官对公司将钱花在哪里有一个很好的了解。规则应该去哪里？

#### **解决方案：尽可能高的组织级别**

满足此要求的一种简单方法是将 IAM 策略附加到不同的业务部门，如附录的文件 1 所示。然而，这是低效的，因为新创建的业务单位也必须具有此 IAM 策略。此外，此解决方案在审核 IAM 策略时引入了冗余，因为这些策略是相同的。

更好的方法是利用 IAM 策略从父资源继承的事实。我们可以将此 IAM 策略置于组织级别。然后，每个业务部门将从组织继承 IAM 策略，如附录的文件 2 所示。

从这个场景中，我们学会了在最高级别插入 IAM 策略，以利用 GCP 的 IAM 策略继承。

### **要求二：一个用户跨多种环境类型的多个预定义角色**

第二种情况的要求是授予我们的 Praetorian Cloud Manager 以下内容：

* 开发中的*Compute Admin*预定义角色 (roles/compute.admin)
* 暂存中的*计算网络用户*预定义角色 (roles/compute.networkUser)
* 生产中的*计算网络查看器*预定义角色 (roles/compute.networkViewer)

我们的目标是遵循最小权限原则，即随着项目接近生产，用户的访问权限更少。IAM 政策应该去哪里？

#### **解决方案：条件语句**

创建 IAM 策略的最简洁方法是按策略共有的最高资源对其进行拆分，然后引入条件语句。从第一个场景中学习，我们知道 GCP IAM 继承会导致不同的环境类型从业务单元继承权限。将 IAM 策略置于业务单元级别具有将所有策略保存在一个位置的好处，但随着公司规模的扩大，可能会增加复杂性。

对于我们的场景，我们可以将策略放在 Praetorian 云业务单元中，并使用条件语句为我们的 Praetorian Cloud 管理器在开发中提供*Compute Admin* ，在 staging 中提供*Compute Network User ，在生产中提供\*\*Compute Network Viewer*。在环境类型文件夹级别使用 env:cloud-dev 或 env:cloud-staging 等标签标记资源允许我们使用条件表达式，如

```
resource.matchTag('{projectid}/env','cloud-dev')
```

使权限仅适用于环境类型级别。附录的文件 3 显示了完成上述操作的示例 Terraform 文件。

现在想象一个扩展，其中负责在生产中测试应用程序的额外 Praetorian 安全测试人员需要在Praetorian 云环境的生产环境中预定义*安全审查员*(roles/iam.securityReviewer) 角色以进行测试。我们需要向 IAM 策略添加更多条件语句，以便仅在生产环境中授予 Praetorian Security Tester 权限。这将开始使条件语句膨胀，并可能导致不必要的复杂性，从而导致 IAM 漏洞。

#### 经验教训：最高层政策的工作*有共同点*。

在我们的场景及其扩展中，环境类型资源是 IAM 策略共有的最高级别。我们可以轻松地在此级别创建 IAM 策略，以在适当的环境类型中为 Praetorian Cloud Manager 和 Praetorian Security Tester 提供适当的权限，如附录的文件 4 所示。

从这个场景中，我们了解到，虽然 IAM 策略应置于可能的最高级别以利用 GCP 的 IAM 策略继承，但 IAM 策略应仅设置在它们共有的最高级别，以降低条件语句形式的复杂性. 将策略置于更高级别会使从场景一中吸取的教训太过分，并且会导致难以验证或扩展的极其复杂的策略。

### **要求三：一个用户在特定标记资源上的一个预定义角色**

最后一个场景的要求是给我们的 Praetorian Cloud Developer *Compute Network Viewer*预定义角色，只允许在云暂存环境的 Athena 项目中标记为“designation:not-sensitive”的那些资源。我们将如何制定此 IAM 政策？

#### **解决方案：拒绝政策？**

从上述两个练习中，我们知道我们希望将 IAM 策略放在项目级别。即使存在允许 IAM 策略，拒绝策略也可以帮助我们阻止访问。但是，我们必须特别注意任何显式拒绝策略如何跨资源交互。

对于实际的政策，我们知道我们想要一个有条件的政策，比如

```
resource.matchTag('{projectid}/designation','不敏感')
```

*在 staging/athena 项目中将Compute Network Viewer*提供给我们的 Praetorian Cloud 开发人员。现在，虽然 GCP 的隐式拒绝会阻止 Praetorian Cloud Developer 拥有*Compute Network Viewer*，但我们希望确保我们满足要求的**唯一**方面。为此，我们可以使用拒绝 IAM 策略，该策略将具有如下条件语句

```
!resource.matchTag('{projectid}/designation','not-sensitive')
```

这将拒绝访问那些缺少不敏感标签的人。附录的文件 5 包括演示这一点的 Terraform 文件。

#### 经验教训：隐式拒绝有助于避免意外拒绝策略组合。

虽然上面是满足我们最后一个要求的有效方式，但它的可扩展性不是很好。考虑一个额外的请求，我们希望**仅授予**Compute Network Viewer\*访问我们的 Praetorian Cloud 开发人员对标记为“designation:isfine”的资源的访问权限。我们还知道，Praetorian Cloud 暂存环境中的所有项目都将具有标记为“designation:isfine”的资源。只有这些项目中的资源才会具有该名称。使用与上述相同的逻辑，我们可以有一个带有条件语句的 IAM 策略

```
resource.matchTag('{projectid}/designation','isfine')
```

以及带有条件语句的拒绝 IAM 政策

```
!resource.matchTag('{projectid}/designation','isfine')。
```

在查看 staging/athena 项目时会出现问题。由于 GCP 中的 IAM 策略继承，staging/athena 项目将继承其父级的拒绝语句。该项目将有两个拒绝 IAM 策略，拒绝任何不具有**“** designation:not-sensitive”和“designation:isfine”标签的资源。这是不可能的，因为“designation”键不能同时具有“not-sensitive”和“isfine”值。这不是任何一条规则的创建者对我们的开发人员的意义。

这种情况及其扩展证明了在使用拒绝语句时要小心的重要性。在大多数情况下，公司应该允许 GCP 的隐式拒绝来限制权限。拒绝语句在特定情况下确实有其用途（即，在组织级别拒绝以执行公司政策，因为只有财务团队才能在组织中拥有计费权限）。这些场景更加细微，需要审计和成熟的安全程序，以确保多个拒绝 IAM 策略的继承不会结合起来阻止超出策略预期的权限。

最佳实践

       我们对 GCP IAM 的高级探索的一些主要收获如下：

* 公司通常按业务单位、环境类型和项目/团队划分其 GCP 组织结构。
* 公司应致力于将条件 IAM 策略置于可能利用继承的最高通用级别，但又不够高，以至于对某些资源来说是不必要的并产生不必要的复杂性。
* 公司将希望专注于仅提供委托人进行日常运营所需的最低权限。拒绝 IAM 策略可能会增加扩展 IAM 模型以包含新要求的难度。

附录：上述场景使用的 Terraform 文件

### （文件 1）三个业务单位文件夹的计费成本管理器：

```
resource "google_folder" "PraetorianCloud" {
  display_name = "PraetorianCloud"
  parent       = "organizations/<Praetorian Org ID>"
}
resource "google_folder_iam_member" "CFO_Cloud_Access" {
  folder = google_folder.PraetorianCloud.id
  role = "roles/billing.costManager"
  member = "user:cfo@praetorian.com"
}
*repeat for Praetorian Webapp and Praetorian redteam folder
```

###

### （文件 2）组织级别的计费成本管理器

```
resource "google_organization_iam_member" "CFO_Org_Access" {
  org_id = "<Praetorian Org ID>"
  role = "roles/billing.costManager"
  member = "user:cfo@praetorian.com"
}
```

### （文件 3）业务单元级别的角色分配

```
resource "google_folder_iam_member" "Cloud_Manager_Dev_Access" {
  folder = google_folder.PraetorianCloud.id
  role = "roles/compute.admin"
  member = "user:cloudmanager@praetorian.com"
  condition {
    title = "Admin for development only"
    description = "Admin for development only"
    expression = "resource.matchTag('{projectid}/env', 'cloud-dev')"
  }
}
resource "google_folder_iam_member" "Cloud_Manager_Stage_Access" {
  folder = google_folder.PraetorianCloud.id
  role = "roles/compute.networkUser"
  member = "user:cloudmanager@praetorian.com"
  condition {
    title = "network user for staging only"
    description = "network user for staging only"
    expression = "resource.matchTag('{projectid}/env', 'cloud-stage')"
  }
}
*repeat for Cloud production
```

### （文件 4）环境级别的角色分配

```
resource "google_folder" "CloudProduction" {
  display_name = "Production"
  parent       = google_folder.PraetorianCloud.id
}
resource "google_folder_iam_member" "Viewer_for_Cloud_manager_in_production" {
  folder = google_folder.CloudProduction.id
  role = "roles/compute.networkViewer"
  member = "user:cloudmanager@praetorian.com"
}
resource "google_folder_ia...