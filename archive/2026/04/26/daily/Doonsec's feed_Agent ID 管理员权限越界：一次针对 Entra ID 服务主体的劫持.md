---
title: Agent ID 管理员权限越界：一次针对 Entra ID 服务主体的劫持
url: https://mp.weixin.qq.com/s/XgXpQW2W6F8iKqrO6XuoKQ
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:04:42.047384
---

# Agent ID 管理员权限越界：一次针对 Entra ID 服务主体的劫持

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibed0eZ5YZzKC0SanZaibwatuLjJlgogwibgDwPUhrVXpYwDicZg4fS1fuosA6D8dUjL9lOuM3FEdcgyn2caCJSHZfOu6ZhJ0xto0s/0?wx_fmt=png&from=appmsg)

# Agent ID 管理员权限越界：一次针对 Entra ID 服务主体的劫持

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 微软为管理AI而设计的Agent ID管理员角色，理论上只应管理“智能体身份”。我们却发现，拥有此权限的攻击者，竟能接管租户内任意一个服务主体，包括那些拥有特权的高价值服务账号。权限设计的边界是如何被轻易打破的？

## 一句话说清楚

微软的智能体身份平台（预览版）为AI智能体在Entra ID中创建了独立的身份对象。为了管理这些新对象，微软引入了Agent ID Administrator角色。按文档描述，这个角色应该只管理那些跟“智能体”相关的对象。

但我们发现，仅仅拥有Agent ID管理员权限的账户，可以直接把自己添加为**任意服务主体**的“所有者”。之后，他就能给这些服务主体添加凭证，并以该身份完成认证。这等于完全控制了那个服务主体。

在那些已经部署了高权限服务主体的租户里，这是条极好的权限提升路径。

虽然这个角色的应用还不广泛，但绝大多数租户都至少有一个特权服务主体。我们也看到，不少租户已经在大量使用“智能体身份”。可以预见，随着Agent ID管理员角色的普及，这个权限范围上的漏洞会逐渐成为显著的安全风险。

我们已经把这个情况报告给了微软安全响应中心，并且在所有云环境中都完成了修复。现在，Agent ID管理员已经不能再去管理非智能体服务主体的所有者了。

如果你已经了解上述概念，可以直接跳到“边界如何被打破”部分。

## Agent ID 管理员权限漏洞

### 你需要知道的背景知识

**Entra ID 中的应用程序与服务主体**

在微软Entra ID（之前的Azure AD）中注册一个应用时，会在应用的“主租户”里创建两个相互关联的对象：一个应用程序对象（Application Object），一个服务主体（Service Principal）。

* **应用程序对象**

  ：这是应用的全局定义，描述了它的配置。
* **服务主体**

  ：这代表了应用在特定租户内的身份。负责认证、被分配角色和权限、访问资源的，都是这个服务主体。如果一个应用配置为多租户，那它在不同租户中使用时，都会基于同一个应用程序对象，创建各自的服务主体。

Entra ID里有很多种服务主体，比如应用程序服务主体、托管身份等。本文我们只聚焦于“应用程序服务主体”，因为后面说的行为，正是针对这一类型的。

**微软Entra Agent ID**

简单说，这个平台让你能把AI智能体当作是Entra ID中的“一等公民。这意味着，你可以对租户内的AI智能体实施条件访问、生命周期管理等策略。其底层基于微软智能体身份平台，这是为AI智能体设计的一个身份与授权框架。

它引入了几个新对象类型：

* **蓝图**

  ：定义和创建智能体身份的模板。
* **蓝图主体**

  ：蓝图被添加到某个租户时的租户特定实例。
* **智能体身份**

  ：供AI智能体向API和服务进行身份验证的特殊服务主体。
* **智能体用户**

  ：这些是可选的对象，为那些需要UPN或电子邮件的智能体提供用户类对象，用于“模拟”（On-Behalf-Of）认证流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibed0eZ5YZzKC0SanZaibwatuLjJlgogwibgDwPUhrVXpYwDicZg4fS1fuosA6D8dUjL9lOuM3FEdcgyn2caCJSHZfOu6ZhJ0xto0s/640?wx_fmt=png&from=appmsg)

关键在于，智能体身份是在我们熟悉的目录原语（应用程序、服务主体、用户）之上构建的。而我们的发现，就藏在这个“共享的基础”里。

**Agent ID Administrator 角色**

微软新增这个角色的本意，是管理新型“智能体身份”控制平面。查阅官方文档，它的权限范围是这样的：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibevV9mqXLKwIv4IrwXHiapvWTWcCVwWF3dsY5M9XEYEPz7PI9SViaIO54xV3eo8gxGib9LwSEwSZGfG0W6icDicb4zzwNJic2m4DYm9o/640?wx_fmt=png&from=appmsg)

直白翻译：只管“智能体”那摊事，不管所有服务主体。这个区分很重要，因为服务主体背后是自动化流程、CI/CD、安全工具，以及那些带有特权的集成。控制它们，就等于控制了环境的一大块。

这里还有个细节：文档里说这个角色是“特权角色”，但在Entra UI（基于Beta版目录角色定义）里，它却**没被打上这个标签**。这可能导致管理员在分配这个角色时，不会像对待其他特权角色那样小心。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfTAPItHyXsOeKbFTuycw36rAfbJWE15XbbXjVpq0QgZRVHPA97YibLQlgKXvibcfb2hsxbPMgSLa0AHqU5a6rHJZnOibh4wW4ykk/640?wx_fmt=png&from=appmsg)

微软已经确认，会修复这个UI和文档间的不一致。

## 边界如何被打破

我们观察到的过程是这样的：一个被分配了Agent ID管理员角色的用户，可以把自己添加为**任意服务主体**的所有者，哪怕这个服务主体跟智能体身份毫无关系。之后，他就能直接凭证并以此身份通过认证。

**步骤一：添加“所有者”**

这一步对非智能体的服务主体也能成功。你可以加自己，也能加其他主体。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibc0D9hFVmawpRbOPaYWJ8kiabZQnxUwgjMZPkGdc5R5oib43wFOgU5IapsOVepPcBR5AKt3VFibbokHWP2QUYbE4KsLoREb0zwGRI/640?wx_fmt=png&from=appmsg)

**步骤二：添加凭证**

这一步只有在成为所有者之后才能操作。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfK92dY5ENjzpGibVHiauMILR1jPOiaHvMS7fgoRiahvo2E1HaDhCRnSm8DG3tLSusH3uN35OWzZqmYAvGuAU7URJ9diczz3sJVG49c/640?wx_fmt=png&from=appmsg)

说白了，“所有权”就是一种接管手段。成为所有者后，加个密钥就能以那个服务主体的身份登录了。

这个角色本意是管智能体身份，但在实际操作中，它能改**任何**服务主体的所有者。

**为什么会这样？**

我们推测的逻辑很简单。有些智能体身份底层的实现就是服务主体（及相关的类型）。这个角色有诸如“microsoft.directory/agentIdentities/owners/update”这样的操作权限，允许管理员管理智能体对象的所有者。

如果相应的权限检查没有严格限定在“智能体支撑的服务主体”上，那么权限就会“溢出”到普通的服务主体层面。

这有点像经典的设计漏洞：一个对象类型继承自另一个类型时，权限作用域没把牢。

我们测试了应用程序对象，添加自己为应用所有者的操作被拒绝了。所以，这个问题似乎特定地出现在“服务主体”这个层面。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibeSSJ9KgZFWkAyhux7MwC3vFVvcV4bb8suDicX18WibfqglrLbf3GxZsDDohMcahfkBUicz9wy1VsxicCNx3hSpvic7JRoSH0WTh1rA/640?wx_fmt=png&from=appmsg)

修复之后，再用Agent ID管理员角色尝试给非智能体服务主体分配所有权，操作会被阻断，并返回下述错误。

## 潜在影响：服务主体劫持

获取一个服务主体的所有权，相当于在攻击链上拿到了一个强力支点。一旦攻击者成为所有者，他就能添加凭证，以该服务主体的身份登录，并行使它既有的所有权限，比如访问特定API、使用目录角色、调用集成接口。

实际的影响大小，取决于被盯上的服务主体本身拥有的权限级别。在那些广泛使用服务主体或服务主体拥有高权限的环境里，这就是一条权限提升的捷径。

修复前，Agent ID管理员角色允许任意分配服务主体的所有权，这实际上让它拥有了类似“应用程序管理员”角色的能力，但其权限定义范围却没被严格限定在智能体用例上。

**当目标是特权“服务账号”时**

权限升级的逻辑很直接：如果一个服务主体本身就拥有高权限（比如目录角色、高影响力的Microsoft Graph权限），接管它就等于拿到了这些权限。很多公司都有这样的服务主体。

攻击者可以先去发现哪些服务主体是“特权”的，然后瞄准它们。实际操作中，这意味着两种检查：

1. **拥有特权目录角色的服务主体**

   ：利用Microsoft Graph API去查看哪些服务主体被分配了管理员级别的目录角色。
2. **拥有高影响力Graph权限的服务主体**

   ：查询应用角色对Microsoft Graph的分配情况，看是否包含敏感权限。

### 枚举特权服务主体

你可以用下面的脚本（登录az后使用）来寻找目标。这些脚本不专门过滤非智能体服务主体。

# 方法1：查找拥有特权目录角色的服务主体
BASE="https://graph.microsoft.com"
roles="$(az rest -m GET --url "${BASE}/beta/roleManagement/directory/roleDefinitions?\$filter=isPrivileged eq true&\$select=id,displayName" -o json)"
u="${BASE}/beta/roleManagement/directory/roleAssignments?\$expand=principal(\$select=id,displayName)&\$top=999"
{
  echo -e "SP\_NAME\tSP\_ID\tROLE"
  echo -e "--------\t------\t----"
  while :; do
    j="$(az rest -m GET --url "$u" -o json 2>/dev/null)" || break
    jq -r --argjson roles "$roles" '
      ($roles.value | map(select(.displayName|test("Reader";"i")|not) | {key:.id, value:.displayName}) | from\_entries) as $r
      | .value[]
      | select(.principal."@odata.type"=="#microsoft.graph.servicePrincipal")
      | select($r[.roleDefinitionId] != null)
      | [.principal.displayName, (.principal.id // .principalId), $r[.roleDefinitionId]] | @tsv
    ' <<<"$j"
    u="$(jq -r '."@odata.nextLink"//empty' <<<"$j")"
    [[ -z "$u" ]] && break
  done | sort -t$'\t' -k1,1
} | column -t -s $'\t'

# 方法2：查找拥有高影响力Graph应用权限的服务主体
BASE="https://graph.microsoft.com"
PERM\_IDS='["9e3f62cf-ca93-4989-b6ce-bf83c28f9fe8","06b708a9-e830-4db3-a914-8e69da51d44f","1bfefb4e-e0b5-418b-a88f-73c46d2cc8e9","19dbc75e-c2e2-444c-a770-ec69d8559fc7","dd199f4a-f148-40a4-a2ec-f0069cc799ec","50483e42-d915-4231-9639-7fdb7fd190e5","01c0a623-fc9b-48e9-b794-0756f8e8f067","62a82d76-70ea-41e2-9197-370581804d09”，“cc117bb9-00cf-4eb8-b580-ea2a878fe8f7"]'
PERM\_NAMES='{"9e3f62cf-ca93-4989-b6ce-bf83c28f9fe8":"RoleManagement.ReadWrite.Directory","06b708a9-e830-4db3-a914-8e69da51d44f":"AppRoleAssignment.ReadWrite.All","1bfefb4e-e0b5-418b-a88f-73c46d2cc8e9":"Application.ReadWrite.All","19dbc75e-c2e2-444c-a770-ec69d8559fc7":"Directory.ReadWrite.All","dd199f4a-f148-40a4-a2ec-f0069cc799ec":"RoleAssignmentSchedule.ReadWrite.Directory","50483e42-d915-4231-9639-7fdb7fd190e5":"UserAuthenticationMethod.ReadWrite.All","01c0a623-fc9b-48e9-b794-0756f8e8f067":"Policy.ReadWrite.ConditionalAccess","62a82d76-70ea-41e2-9197-370581804d09":"Group.ReadWrite.All","cc117bb9-00cf-4eb8-b580-ea2a878fe8f7":"User-PasswordProfile.ReadWrite.All"}'
GRAPH\_SP\_ID="00000003-0000-0000-c000-000000000000"
az rest --method GET —url "${BASE}/v1.0/servicePrincipals(appId='${GRAPH\_SP\_ID}')/appRoleAssignedTo" -o json 2>/dev/null \
  | jq -r --argjson ids "$PERM\_IDS" —argjson names "$PERM\_NAMES" '
    ["SP\_NAME", "SP\_ID", "PERMISSIONS"], ["--------", "------", "-------------"],
    ([.value[] | select(.appRoleId as $rid | $ids | index($rid))] | group\_by(.principalId)[] |
      [.[0].principalDisplayName, .[0].principalId, ([.[].appRoleId | $names[.]] | join(", "))]) | @tsv
  ' | column -t -s $'\t'

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdJVxVYJuGHquiauaItFkehElyNIsLQZmicRQxemFOwibvtO3gtCn0OoRSJaz2qEqDnyALqpfdvOISq058wToUrwQN1jwWjpNcnsQ/640?wx_fmt=png&from=appmsg)

## 端到端的攻击流程

下图把上述的枚举和接管步骤整合到了一个流程视图里。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibeCTIoK24jCQKGefWgoKNoJtgY9dIBRKHaw1vgxXgrQhIMfFPDWWDgVSGZKfQ6iaeYibIaHzzI73vOmkicyr5VrDABzy4Lpic48yLE/640?wx_fmt=png&from=appmsg)

### 演示记录

这段录像演示完整流程：找一个有特权的服务主体（演示只搜索了目录角色），接管它，然后用新凭证登录。

内容：一个仅拥有Agent ID管理员权限的测试用户，接管了一个拥有全局管理员角色的非智能体服务主体，并用新凭证登录，完成了权限提升。

## 现实世界的一瞥

我们观察了一些客户环境：Agent ID管理员角色尚未被广泛使用，但这种权限提升的土壤早已存在。

大约**99%的租户**至少拥有一个特权服务主体（不一定与智能体相关）。超过半数的租户正在使用智能体身份，而在这些用户中，又有接近一半的租户拥有超过100个智能体身份。

随着越来越多的组织分配这个角色来管理智能体身份，这个作用域上的缝隙就会实实在在地变成安全风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfExPcTRCEROYVXAdyHczozxjl0iavVpZnpN8RnuhIEfHqq26pobiahlZwfygM6dHXjLM6Gfv2hdXdDZzhJHUJxlhBPAoAGxrbuI/640?wx_fmt=png&from=appmsg)

## 我们的观察与建议

微软已经解决了这个问题，但这件事给我们的启示还在：新的身份类型通常构建在现有基础之上，这可能导致角色权限的作用域出现盲区。在这个案例里，结果是获得了比设计意图更广泛的访问权限。认真审视这些潜在风险永远必要。

### 为什么它容易被忽视

* 在服务主...