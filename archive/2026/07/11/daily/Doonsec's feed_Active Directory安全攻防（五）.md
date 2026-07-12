---
title: Active Directory安全攻防（五）
url: https://mp.weixin.qq.com/s/jtTUocQeb57jc4JBWGEVbQ
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:09:27.090272
---

# Active Directory安全攻防（五）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/pcNneYiaOMFFEGibQkr0oTuia9bExVNO5xEx8eANllLibUe46KebVq9EPCJdsBsJTvCh6PV2w0Vb6vFiaw5xgyIOzaQ/0?wx_fmt=jpeg)

# Active Directory安全攻防（五）

原创

寰宇秘阁
寰宇秘阁

寰宇密阁

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在前几篇文章中，我们深入探讨了 Active Directory 的访问控制列表（ACL）机制、SDProp 安全描述符传播器以及 AdminSDHolder 容器的保护原理。我们了解到，AD 中对象的权限来源是多层次的——既有通过组织单位（OU）委派的权限，也有 SDProp 机制为高权限账户强制设定的权限。

然而，还有一个常被忽视但同样重要的权限来源：**Schema（架构）中定义的默认权限**。

每当 Active Directory 创建一个新对象（如用户、计算机、组等），系统并不是从零开始构建其安全描述符的。相反，AD 会从 Schema 中读取该对象类预定义的**默认安全描述符**，作为新对象的初始权限模板。这些默认权限使用一种名为 **SDDL（Security Descriptor Definition Language，安全描述符定义语言）** 的专用字符串格式进行定义。

理解 Schema 默认权限和 SDDL 语法，对于安全审计、权限分析以及攻防研究都至关重要。本文将详细解析这一机制。

---

## 一、AD 对象权限的三大来源

在深入 Schema 默认权限之前，让我们先回顾一下 Active Directory 中对象权限的完整来源体系：

| 权限来源 | 描述 | 适用范围 |
| --- | --- | --- |
| **Schema 默认权限** | 在对象创建时，从 Schema 中该对象类的 `defaultSecurityDescriptor` 属性读取并应用 | 所有新创建的 AD 对象 |
| **OU 级别的委派权限** | 通过在组织单位上配置 ACL 实现权限继承，子对象继承父容器的权限 | OU 内的对象（通过继承） |
| **SDProp 强制权限** | AdminSDHolder 容器上的 ACL 模板，由 SDProp 进程周期性地强制覆盖到受保护账户 | 受保护安全组的成员（`adminCount=1`） |

这三层权限共同构成了 AD 对象最终的有效权限。其中，Schema 默认权限是最基础的一层——它决定了对象"出生"时的权限状态。

---

## 二、Schema 中的默认安全描述符

### 2.1 什么是 Schema？

Active Directory Schema（架构）定义了目录数据库中可以存储的所有对象类型（类）和属性。可以将 Schema 理解为 AD 的"数据字典"或"蓝图"——它规定了：

* **类（Class）**

  ：可以创建哪些类型的对象（如 `user`、`computer`、`group`、`organizationalUnit` 等）
* **属性（Attribute）**

  ：每种对象可以拥有哪些属性（如 `sAMAccountName`、`mail`、`memberOf` 等）
* **默认安全描述符**

  ：每种对象在创建时应具有的初始权限

### 2.2 查看 Schema 中的默认权限

要查看某个对象类的默认安全描述符，可以通过以下两种方式：

**方式一：使用 Schema 管理单元（Schema Snap-in）**

1. 运行 `regsvr32 schmmgmt.dll` 注册 Schema 管理单元
2. 打开 MMC 控制台，添加"Active Directory 架构"管理单元
3. 展开"类"节点，找到目标类（如 `user`）
4. 右键点击 → 属性 → 切换到 **“默认安全性（Default Security）”** 选项卡

在这个选项卡中，你可以看到以图形化方式展示的默认权限配置。

**方式二：使用 ADSI 编辑器（adsiedit.msc）**

1. 打开 ADSI 编辑器
2. 连接到 **Schema** 命名上下文
3. 找到目标类对象（如 `CN=User,CN=Schema,CN=Configuration,DC=...`）
4. 查看其 `defaultSecurityDescriptor` 属性

该属性的值是一个 **SDDL 格式的字符串**，这就是我们接下来要重点解析的内容。

### 2.3 defaultSecurityDescriptor 属性

`defaultSecurityDescriptor` 是 Schema 中每个类对象上的一个属性，它以 SDDL 字符串的形式存储了该类对象的默认权限模板。

例如，`user` 类的 `defaultSecurityDescriptor` 可能类似如下：

```
D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;AO)(A;;RPLCLORC;;;PS)(OA;;CR;ab721a53-1e2f-11d0-9819-00aa0040529b;;PS)...
```

这段看起来像"天书"的字符串，实际上是一种高度结构化的权限描述语言。让我们来逐步解析它。

---

## 三、SDDL 安全描述符定义语言详解

### 3.1 SDDL 概述

**SDDL（Security Descriptor Definition Language）** 是 Microsoft 定义的一种文本格式，用于描述安全描述符。它将复杂的二进制安全描述符转换为人类可读（虽然不太友好）的字符串表示。

SDDL 字符串的基本结构如下：

```
O:<所有者SID>G:<主组SID>D:<DACL>S:<SACL>
```

| 组成部分 | 含义 |
| --- | --- |
| `O:` | Owner（所有者）——对象的所有者 SID |
| `G:` | Group（主组）——对象的主组 SID |
| `D:` | DACL（自主访问控制列表）——定义谁可以访问对象 |
| `S:` | SACL（系统访问控制列表）——定义审计规则 |

在 Schema 的 `defaultSecurityDescriptor` 中，最常见的是 `D:` 部分（DACL），它定义了对象的默认访问权限。

### 3.2 ACE 条目的格式

DACL 部分由一系列 **ACE（访问控制条目）** 组成，每个 ACE 用括号包裹，格式如下：

```
(ACE_Type;ACE_Flags;Rights;Object_GUID;Inherit_Object_GUID;Account_SID)
```

各字段的含义：

| 字段 | 含义 | 示例 |
| --- | --- | --- |
| **ACE\_Type** | ACE 类型 | `A` = 允许（Access Allowed），`D` = 拒绝（Access Denied），`OA` = 对象特定的允许 |
| **ACE\_Flags** | 继承标志 | `CI` = 容器继承，`OI` = 对象继承 |
| **Rights** | 权限代码 | `RP` = 读取属性，`WP` = 写入属性，`CC` = 创建子对象等 |
| **Object\_GUID** | 对象 GUID（仅对象特定 ACE） | 控制权限适用于哪个属性或扩展权限 |
| **Inherit\_Object\_GUID** | 继承对象 GUID | 控制继承适用于哪种子对象类型 |
| **Account\_SID** | 安全主体 | `DA` = Domain Admins，`SY` = System 等 |

### 3.3 权限代码详解

SDDL 中的权限使用两字母缩写表示，以下是常见的权限代码：

| 代码 | 全称 | 含义 |
| --- | --- | --- |
| `RP` | Read Property | 读取属性 |
| `WP` | Write Property | 写入属性 |
| `CR` | Control Access / Extended Right | 控制访问权 / 扩展权限 |
| `CC` | Create Child | 创建子对象 |
| `DC` | Delete Child | 删除子对象 |
| `LC` | List Children | 列出子对象 |
| `LO` | List Object | 列出对象 |
| `RC` | Read Control | 读取安全描述符（DACL） |
| `WO` | Write Owner | 修改所有者 |
| `WD` | Write DACL | 修改 DACL |
| `SD` | Standard Delete | 标准删除 |
| `DT` | Delete Tree | 删除子树 |
| `SW` | Self Write | 自写（如将自己添加到组中） |
| `GA` | Generic All | 完全控制 |
| `GR` | Generic Read | 通用读取 |
| `GW` | Generic Write | 通用写入 |
| `GX` | Generic Execute | 通用执行 |

### 3.4 安全主体代码

SDDL 使用简短的代码来表示常见的安全主体，避免使用冗长的 SID 字符串：

| 代码 | 安全主体 | 说明 |
| --- | --- | --- |
| `DA` | Domain Admins | 域管理员组 |
| `SY` | System | 本地系统账户 |
| `AO` | Account Operators | 账户操作员组 |
| `PS` | Personal Self（Self） | 对象自身（用户可以修改自己的某些属性） |
| `RS` | RAS and IAS Servers | RAS 和 IAS 服务器组 |
| `AU` | Authenticated Users | 已认证用户 |
| `WD` | Everyone | 所有人 |
| `CA` | Certificate Publishers | 证书发布者 |
| `BA` | Built-in Administrators | 内置管理员组 |
| `EA` | Enterprise Admins | 企业管理员组 |
| `SA` | Schema Admins | 架构管理员组 |
| `CO` | Creator Owner | 创建者/所有者 |

此外，对于没有预定义代码的安全主体，SDDL 直接使用完整的 SID 字符串表示：

| SID | 安全主体 |
| --- | --- |
| `S-1-5-32-560` | Windows Authorization Access Group（Windows 授权访问组） |
| `S-1-5-32-561` | Terminal Server License Servers（终端服务器许可证服务器） |

---

## 四、实战解析 SDDL 字符串

### 4.1 逐条解析示例

让我们以 `user` 类的默认安全描述符为例，逐条解析其中的 ACE：

**第一条 ACE：**

```
(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)
```

拆解：

| 字段 | 值 | 含义 |
| --- | --- | --- |
| ACE\_Type | `A` | Access Allowed（允许访问） |
| ACE\_Flags | （空） | 无继承标志 |
| Rights | `RPWPCRCCDCLCLORCWOWDSDDTSW` | 多项权限的组合 |
| Object\_GUID | （空） | 适用于所有属性 |
| Inherit\_Object\_GUID | （空） | 无继承限制 |
| Account\_SID | `DA` | Domain Admins（域管理员） |

权限代码展开：

| 代码 | 权限 |
| --- | --- |
| `RP` | 读取属性 |
| `WP` | 写入属性 |
| `CR` | 控制访问权 |
| `CC` | 创建子对象 |
| `DC` | 删除子对象 |
| `LC` | 列出子对象 |
| `LO` | 列出对象 |
| `RC` | 读取安全描述符 |
| `WO` | 修改所有者 |
| `WD` | 修改 DACL |
| `SD` | 标准删除 |
| `DT` | 删除子树 |
| `SW` | 自写 |

**解读**：Domain Admins 对该对象拥有几乎所有权限，相当于**完全控制**。

**第二条 ACE：**

```
(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)
```

与第一条结构完全相同，只是安全主体变为 `SY`（System）。这意味着**本地系统账户**也拥有完全控制权限。

**第三条 ACE：**

```
(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;AO)
```

安全主体为 `AO`（Account Operators），同样拥有完全控制权限。这就是为什么 Account Operators 组默认可以管理域中的用户和组对象。

**第四条 ACE：**

```
(A;;RPLCLORC;;;PS)
```

| 字段 | 值 | 含义 |
| --- | --- | --- |
| ACE\_Type | `A` | 允许访问 |
| Rights | `RPLCLORC` | RP（读取属性）+ LC（列出子对象）+ LO（列出对象）+ RC（读取安全描述符） |
| Account\_SID | `PS` | Personal Self（对象自身） |

**解读**：用户对自己的对象拥有**基本的读取权限**——可以读取自己的属性、列出子对象、列出对象以及读取安全描述符。这是一组只读权限，确保用户至少能够查看自己的基本信息。

**第五条 ACE：**

```
(OA;;CR;ab721a53-1e2f-11d0-9819-00aa0040529b;;PS)
```

| 字段 | 值 | 含义 |
| --- | --- | --- |
| ACE\_Type | `OA` | Object-specific Access Allowed（对象特定的允许访问） |
| ACE\_Flags | （空） | 无继承标志 |
| Rights | `CR` | Control Access / Extended Right（扩展权限） |
| Object\_GUID | `ab721a53-1e2f-11d0-9819-00aa0040529b` | 对应 **Change Password**（更改密码）扩展权限 |
| Inherit\_Object\_GUID | （空） | 无继承限制 |
| Account\_SID | `PS` | Personal Self（对象自身） |

**解读**：用户拥有**更改自己密码**的扩展权限。注意这里使用了 `OA` 类型而非普通的 `A`，因为这是一个**对象特定的 ACE**——它通过 Object\_GUID 精确指定了权限适用于哪个扩展权限（Change Password）。

> **知识点**：`OA` 类型的 ACE 是 Active Directory 特有的，它允许将权限精确绑定到特定的属性、属性集或扩展权限。Object\_GUID 字段引用的是 Schema 中定义的 `rightsGuid` 或 `schemaIDGUID`。

### 4.2 常见扩展权限 GUID 对照表

在解析 SDDL 时，经常会遇到 Object\_GUID 字段中的 GUID 值。以下是一些常见的扩展权限及其 GUID：

| GUID | 扩展权限名称 | 说明 |
| --- | --- | --- |
| `ab721a53-1e2f-11d0-9819-00aa0040529b` | Change Password | 更改密码 |
| `00299570-246d-11d0-a768-00aa006e0529` | Reset Password | 重置密码 |
| `ab721a54-1e2f-11d0-9819-00aa0040529b` | Send As | 代理发送 |
| `ab721a56-1e2f-11d0-9819-00aa0040529b` | Receive As | 代理接收 |
| `1131f6aa-9c07-11d1-f79f-00c04fc2dcd2` | DS-Replication-Get-Changes | 目录复制获取变更 |
| `1131f6ad-9c07-11d1-f79f-00c04fc2dcd2` | DS-Replication-Get-Changes-All | 目录复制获取所有变更 |
| `89e95b76-444d-4c62-991a-0facbeda640c` | DS-Replication-Get-Changes-In-Filtered-Set | 目录复制获取过滤集变更 |

> **安全提示**：`DS-Replication-Get-Changes` 和 `DS-Replication-Get-Changes-All` 这两个扩展权限是执行 **DCSync 攻击**的关键前提。如果攻击者能够获得这两个权限，就可以模拟域控制器进行目录复制，从而提取域内所有用户的密码哈希。

### 4.3 完整 SDDL 解析流程

为了帮助读者建立系统化的 SDDL 解析能力，我们总结一个标准的解析流程：

**步骤一：识别整体结构**

```
O:<所有者>G:<主组>D:<DACL标志>(ACE1)(ACE2)...S:<SACL标志>(ACE1)...
```

首先确定字符串中包含哪些部分（O、G、D、S），然后分别处理。

**步骤二：分离 ACE 条目**

在 `D:` 或 `S:` 部分中，每对括号 `()` 包含一个独立的 ACE。将它们逐一提取出来。

**步骤三：解析每个 AC...