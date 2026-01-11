---
title: 深入理解JavaScript 来挖洞
url: https://mp.weixin.qq.com/s/36zZn3SrfZPL6G9U3avKow
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:40:44.299273
---

# 深入理解JavaScript 来挖洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4fyZMZ9pLj8Cibs8uxWbBKSibQicbAPEYra7icCuk99M9SybybbiaQFjuA05RGn6xelUlqtu2hibNNaFYA/0?wx_fmt=jpeg)

# 深入理解JavaScript 来挖洞

迪哥讲事

![]()

在小说阅读器中沉浸阅读

以下文章来源于骨哥说事
，作者骨哥说事

![](http://wx.qlogo.cn/mmhead/Tjnia6K0WAwzfic3VPt0EfMjicnGXzicDLoHEqtz1cP3Iozxf1tSyMxCFNG9Aya8SziaVKhVw7ia6QugE/0)

**骨哥说事**
.

一个喜爱鼓捣的技术宅

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg)

许多漏洞猎人都掌握侦察技巧：搜集子域名、收集 URL、下载 JavaScript 文件。但随后往往陷入僵局：找不到漏洞、没有实际影响、拿不到赏金。究其根本，是因为侦察并非最终目标。

侦察只能帮你勾勒出攻击面。真正的漏洞，藏匿于你对应用程序实际运行逻辑的理解之中。

本文重点讲解侦察完成后该做什么，以及如何利用 Burp Suite，将海量的 JavaScript 文件转化为真实、可提交报告的安全漏洞。

这不是纸上谈兵，而是在实际渗透测试中使用的确切工作流。

#### 步骤 1：侦察完成后，先转变思维方式

请停止这样想： “我拿到了URL列表，现在该丢什么攻击载荷（ payload ）进去？”

开始这样思考：

> **这个应用究竟是如何做决策的？**

JavaScript 不只是前端代码，它更是一扇暴露了应用内部逻辑的窗口。

现代 Web 应用经常通过 JS 泄漏关键信息：

* **内部 API** 接口
* **隐藏参数**
* **功能开关**（ feature flags ）
* **基于角色的访问控制逻辑**
* **仅限管理员的访问路径**
* **已弃用或遗留的接口端点**
* **在客户端做出的（本应在服务端完成的）安全决策**

一旦你学会正确阅读 JavaScript，感觉就像在查阅一份本不该公开的**后端架构说明文档**。

#### 步骤 2：如何正确阅读 JavaScript 代码

别一上来就盲目搜索 `alert(1)` 或 `eval`。

**首先，理解代码结构。**

打开一个 JS 文件后，重点关注：

* **API 的基础路径**（ 例如 `/api/v1/` ）
* **带版本标识的端点**（ 如 `/v1/`, `/v2/`, `/internal/` ）
* **身份验证**相关的请求头信息
* **功能开关**的标识
* **角色检查**相关的代码段
* **错误处理**逻辑

即使代码被压缩混淆（ Minified ）看着头疼，但其核心逻辑必然存在。

在分析前，建议先用浏览器开发者工具（ DevTools ）的“美化”（ Pretty-Print ）功能，或者使用外部工具将其格式化，让代码结构清晰可读。

#### 步骤 3：那些能指引你发现漏洞的“高价值”关键词

在所有 JavaScript 文件中全局搜索以下关键词：

```
admin      （管理员）
internal   （内部）
debug      （调试）
test       （测试）
staging    （预发布环境）
beta       （ Beta 版）
role       （角色）
permission （权限）
access     （访问）
feature    （功能）
flag       （标志）
enabled    （启用）
disabled   （禁用）
isAdmin    （是管理员）
isStaff    （是员工）
token      （令牌）
key        （密钥）
secret     （密钥/机密）
config     （配置）
```

这些词汇常常指向潜在的漏洞区域，例如：

* **访问控制缺陷**（ Broken Access Control ）
* **隐藏的管理员功能**
* **未受保护的内部 API**
* **业务逻辑缺陷**

来看个例子：

```
if (user.role === "admin") {
  enableExport()
}
```

此时，你需要提出一个关键问题：

* **这个判断是仅在前端 JavaScript 中执行，还是后端也同步进行了严格校验？**很多时候，后端过度信任了前端传来的数据。

#### 步骤 4：从 JavaScript 代码中提取隐藏接口端点

JavaScript 文件里常常直接暴露原始 API 路径，比如：

```
/api/user/profile
/api/admin/export
/internal/reports
/graphql
 （ GraphQL 接口）
```

这些接口端点可能在正常浏览网页时根本不会出现。

你的任务是：

1. **复制**这些端点路径。
2. 将它们粘贴到 **Burp Repeater** 模块中。
3. 进行**手动测试**。

**切勿**仅仅因为网页界面上看不到某个功能，就默认认为它需要身份认证或授权。

#### 步骤 5：在 Burp Suite 中测试这些提取出的端点

一旦识别出潜在端点，Burp Suite 就该登场，成为你的主力武器了。

> **核心原则：手动测试 > 自动化扫描**

自动化工具擅长于**发现**，而手动测试才能**深入挖掘**真正的漏洞。请务必先对每个端点进行手动测试。

#### 步骤 6：Burp Suite 手动测试标准流程

将目标请求发送到 **Burp Repeater**，然后按以下步骤进行测试：

**1. 身份验证检查**

* **移除**`Authorization` 请求头。
* 将令牌替换成**另一个低权限用户**的令牌。
* 尝试使用**已过期**或**格式错误**的令牌。

如果端点在这些情况下依然响应，可能意味着你发现了：

* **身份验证绕过**（ Authentication Bypass ）
* **不安全的直接对象引用**（ IDOR， Insecure Direct Object Reference ）
* **权限提升**（ Privilege Escalation ）

**2. 参数操控测试**

主动且大胆地修改请求参数：

* **ID 类参数**：尝试替换为其他用户的 ID（ 如 `userId=123` 改为 `userId=456` ）。
* **布尔值**：将 `true` 改为 `false`，或反之。
* **角色字段**：尝试将 `"user"` 改为 `"admin"`。
* **状态字段**：把 `"inactive"` 改成 `"active"`。

如果后端服务器未经任何校验就直接接受了这些修改，这就是一个**安全漏洞**。

**3. 测试 JavaScript 中提示的“隐藏参数”**

JavaScript 代码常常会暴露出一些**前端界面从未发送**的参数。

例如一段 JS 代码可能这样写：

```
fetch("/api/user/update", {
  body: {
    email,
    role,
    isVerified
  }
})
```

但实际网页请求中可能只发送了 `email`。此时，你应该在 Burp 中**手动添加**`role` 或 `isVerified` 参数进行测试。

**隐藏参数往往是发现严重漏洞的富矿。**

#### 步骤 7：通过 JS 分析定位常见漏洞类型

深入的 JavaScript 分析通常会引导你发现以下几类漏洞：

* **访问控制缺陷**：

+ 普通用户可以访问管理员专用的 API。
+ 数据导出、删除等高危功能缺乏权限保护。

* **不安全的直接对象引用（ IDOR ）**：

+ 参数中存在 `userId`、`orderId`、`accountId` 等。
+ 这些 ID 是连续的或易于预测的。

* **业务逻辑缺陷**：

+ 可以跳过业务流程中的某些必需步骤。
+ 能够乱序改变对象的状态（ 如从未支付直接跳至已发货 ）。
+ 简单的请求重放（ Replay Attack ）即可触发非预期行为。

* **信息泄露**：

+ 暴露了调试接口（ debug endpoints ）。
+ 错误消息中返回了详细的内部信息。
+ API 响应过于详尽，包含了敏感数据。

* **过度信任客户端验证**：

+ 某些限制（ 如次数、额度 ）仅在 JS 前端代码中校验。
+ 角色权限检查只在浏览器端进行。

#### 步骤 8：真正能派上用场的 Burp Suite 扩展（ Plugins ）

别一股脑儿装一堆插件，选择精而有效的。

结合 JavaScript 分析，以下几款扩展尤其有用：

* **Logger++**： 帮助你记录与特定操作相关的**所有请求**，对于理清复杂的请求调用链（ request chains ）非常有用。
* **Autorize**： 通过自动使用不同权限等级的令牌重放请求，高效地**检测授权问题**。
* **Param Miner**： 擅长发现**隐藏和未记录的参数**，与 JS 分析发现的线索相得益彰。
* **Turbo Intruder**： 在处理**基于逻辑的竞争条件**（ Race Condition ）攻击，或需要进行高强度、定制化的暴力破解测试时非常强大。

**记住：** 插件是你的辅助工具，永远无法替代你的**主动思考和分析**。

#### 步骤 9：组合拳：JS线索 + Burp 验证 = 高影响漏洞

真正能带来高额赏金的，往往是**多重漏洞的串联利用**。

来看一个经典的组合攻击链：

1. **JavaScript 分析** 发现了一个隐藏的后台管理员接口（ `/api/admin/export` ）。
2. 进一步测试发现，该接口**缺乏有效的后端角色验证**。
3. 使用 **Burp Suite** 发送请求，**以普通用户身份成功访问**该接口。
4. **成功执行了管理员专属的操作**（ 如导出全部用户数据 ）。

这就是一份证据清晰、**影响巨大**的漏洞报告。

#### 步骤 10：需要规避的常见错误

* **盲目“喷洒”攻击载荷**（ Blind payload spraying ），不加以思考。
* 完全**忽略 JavaScript 中蕴含的业务逻辑**。
* **过度依赖自动化扫描器**，放弃手动深入测试。
* **不仔细阅读服务器的响应内容**，错过关键错误信息或线索。
* **跳过手动测试环节**，过于追求自动化。

**大多数严重漏洞是逻辑缺陷，而非简单的注入或跨站脚本（ XSS(跨站脚本) ）。**

#### 结语

* **侦察（ Recon ）** 告诉你**去哪里找**
* **JavaScript 分析**告诉你**目标如何工作**
* **Burp Suite** 告诉你**哪里可以被攻破**

如果你能将这“三部曲”有机地串联起来，发现漏洞将不再是大海捞针，而变得**有迹可循**。

停止盲目的“乱枪打鸟”，开始深入理解应用程序的内在逻辑。**这才是顶尖漏洞赏金猎人能够持续斩获丰厚奖励的核心秘诀。**

感谢阅读 ✨

如果你是一个长期主义者，欢迎加入我的知识星球，本星球日日更新,包含号主大量一线实战,全网独一无二，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

往期回顾

#

# [如何利用ai辅助挖漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497813&idx=1&sn=c778ad6a4bffd7a0a72a900144ea90ca&scene=21#wechat_redirect)

#

# [如何在移动端抓包-下](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497880&idx=1&sn=b9b980464333074216b55ea94c8a743a&scene=21#wechat_redirect)

#

# [如何绕过签名校验](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497491&idx=1&sn=a1b00b9a8a54eb96aa3ba8bf23cb7e28&scene=21#wechat_redirect)

#

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)[‍](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e...