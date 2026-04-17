---
title: Codex Security代码审计初体验
url: https://www.leavesongs.com/PENETRATION/try-code-security.html
source: 离别歌
date: 2026-04-16
fetch_date: 2026-04-17T04:42:09.362187
---

# Codex Security代码审计初体验

* [主页](/)
* 返回

Back to top
Share post

# Codex Security代码审计初体验

phithon

Apr 16, 2026, 11:40 PM

阅读：1019

[网络安全](/sort/PENETRATION)

[AI安全](/tag/AI%E5%AE%89%E5%85%A8),
[codex](/tag/codex)

昨天申请并通过了OpenAI的个人认证，加上前段时间以开源贡献者的身份申请了OpenAI和Anthropic的赞助，分别获取了两家的max会员半年，我会写几篇文章，分别分享一下Codex Security的使用体验、Codex和Claude Code的对比、GPT Cyber模型的使用体验等。

[![image-20260416215809229.png](/media/attachment/2026/04/16/a3f39fe7-b440-4cf3-8d2d-dfda7ee56ea0.3d6f27632fd9.png)](/media/attachment/2026/04/16/a3f39fe7-b440-4cf3-8d2d-dfda7ee56ea0.png)

这篇文章先介绍一下Codex Security的使用体验，因为扫描额度有限，我只测试了几个仓库，并以我自己开发的CoNote2进行介绍。事先说明，这篇文章的评测纯属主观，没有严谨的对比测试，仅供参考。

## [AI Agent对安全领域的颠覆性改变](#ai-agent)

在写测试之前，我先说下这半年AI Agent对安全领域的颠覆性改变。去年年中到下半年，当时Opus的版本还是4，Opus 4.5还没有发布，Cursor正是如日中天的时间，但经过测试我发现，如果用此时的大模型来挖洞，挖出来大量是误报的问题，特别是对于大型项目分析起来还是很吃力。

此时我们团队内部其实在做的完全是另一件事——使用AI来处理和运营传统SAST工具生产的漏洞。我对自己的这个决定也沾沾自喜，我的想法是，如果让大模型自己去挖洞，我不太看好；但如果只是让大模型审核我们传统SAST产出的漏洞报告，那就完全不一样了，大模型只需要跟着漏洞报告中说到的数据流进行分析就可以了。

为此，我还专门做了一份PPT给老板们介绍，我想我们做的这个东西即发展了大模型的特长，又规避了大模型的问题（这里的问题主要指的是在长上下文时的注意力问题），结合传统SAST效果确实不错。

不过在介绍这个方案的同时，我还是提出了这个方案的缺点，就是传统SAST无法检测的漏洞，现在的方案仍然无法检测。这个方案解决的是准确率的问题，但无法提升召回率，更好的方案还是让AI Agent完全接管代码审计这个任务，不过我当时对第二个方案十分缺乏信心。

但老板还是鼓励我们去做了，也提供了很多资源，于是去年10月份我们开始做自己的白盒Agent。半年以后再往前看，当时我的想法实在太过保守，Agent的工作模式对于传统SAST是颠覆式的改变——我们在只使用Gemini Flash模型的情况下，Agent就已经可以挖掘出大量高危及严重的漏洞了，现在已经逐渐成为漏洞贡献的主力军。

言归正传，Codex Security也是GPT推出的一个云端代码审计Agent，我们今天就来体验一下。

## [用户界面](#_1)

Codex Security是一个完全云端的Agent，在本地的Codex App里没有这个功能，必须登录网页端才能看到。

界面设计的挺难用的，我一度找不到怎么创建任务，因为他的主页显示的是漏洞列表……但是我还没有创建任务，怎么会有漏洞呢，所以登录进去看到的将是一篇空白。

点击左侧侧边栏第二个Scans标签页以后，才能看到任务列表和创建任务的按钮。创建任务只能选择自己的Github中的代码仓库，所以如果想扫描私有项目，需要先将代码上传到自己的仓库里才能开启扫描。

我选择扫描了一下我以前写的CoNote2：

[![image-20260416224147020.png](/media/attachment/2026/04/16/3924a21a-dc6e-4cb9-b233-cc09a1a8544d.b2f6be94121d.png)](/media/attachment/2026/04/16/3924a21a-dc6e-4cb9-b233-cc09a1a8544d.png)

创建任务的时候可以填写我比较关注的漏洞类型、AI应该着重分析哪些部分以及这个项目的一些介绍。我全部留空了，因为我这个项目是一个完整的包含了前后端的项目，理论上我不应该人工定义任何内容。在实际企业场景下，安全工程师创建任务的时候也不会给每个仓库都设置一个自定义的prompt，所以就按照默认的来就可以了。

创建任务以后，需要排队等待，等了差不多一个中午，下午回来的时候就发现漏洞已经扫描结束。

## [扫描报告](#_2)

和我们的Agent有一点不同，Codex Security会分析仓库的历史commit，但我不太清楚它具体会分析什么。

漏洞报告首先会给出这个仓库的介绍，以及资产、安全边界、各个模块作用等信息，最后还会给出它对于严重、高中低危漏洞的定义是什么：

[![image-20260416224938763.png](/media/attachment/2026/04/16/44cc8d5e-e386-4cf9-895f-b64b4a9b391c.00bf5c3074b4.png)](/media/attachment/2026/04/16/44cc8d5e-e386-4cf9-895f-b64b4a9b391c.png)

这份报告找到了1个严重漏洞，7个高危漏洞，我们就来分别看看这些漏洞是否是准确的。

## [严重漏洞](#_3)

这份报告里唯一一份严重漏洞是“QueryChain drops WHERE clauses, enabling auth bypass and IDOR”：

[![image-20260416225146329.png](/media/attachment/2026/04/16/b62b6e4b-8816-4131-a39b-16e4f3195860.8f47a0ed2a88.png)](/media/attachment/2026/04/16/b62b6e4b-8816-4131-a39b-16e4f3195860.png)

大概意思就是，我使用gorm的时候，在Where函数返回后没有把返回值保存下来，会导致这个Where条件没有应用到SQL语句里，最后导致权限校验被绕过。

我的原始代码是：

```
func (c *QueryChain[T]) handleWhere(tx *gorm.DB) {
    for _, w := range c.wheres {
        tx.Where(w.where, w.args...)
    }
}
```

它给出了Patch，代码是：

```
func (c *QueryChain[T]) handleWhere(tx *gorm.DB) *gorm.DB {
    for _, w := range c.wheres {
        tx = tx.Where(w.where, w.args...)
    }
    return tx
}
```

这很明显是一个误报，codex对于gorm的底层代码可能并没有严格去分析。gorm在调用Where函数后，并不需要将其返回的tx保存下来，而是会直接修改用户传入的tx变量。

在漏洞界面上，我们可以点击“Chat”并填写一些问题，并让GPT二次分析这个报告。于是我提出了个问题“你确定gorm会返回一个新的DB对象，但不会修改原始的DB对象吗？请你进入gorm的源码看一下”：

[![image-20260416225642651.png](/media/attachment/2026/04/16/093c8b84-8a41-404b-b770-4b3f3bbddc5f.29f8e119ee71.png)](/media/attachment/2026/04/16/093c8b84-8a41-404b-b770-4b3f3bbddc5f.png)

结果codex在云端agent里重新验证了一遍，甚至下载了gorm的源码进行审计，然后再次给出了肯定的答案——这就是一个漏洞：

[![image-20260416225732892.png](/media/attachment/2026/04/16/143aa888-39a9-4736-876d-85c678c6d539.fbd452d6a427.png)](/media/attachment/2026/04/16/143aa888-39a9-4736-876d-85c678c6d539.png)

我在claude code里让opus 4.6模型阅读了一下这个报告（使用chrome-devtools这个mcp），它除了检查代码以外，还实际编写临时代码进行了测试，最终给出了误报的结论：

[![image-20260416230056845.png](/media/attachment/2026/04/16/ab36acd3-c7d7-4835-ba3d-f946a28ddae1.21a8baadccc2.png)](/media/attachment/2026/04/16/ab36acd3-c7d7-4835-ba3d-f946a28ddae1.png)

我给的提示词非常简单：“帮我使用浏览器看下这个链接里讲的漏洞，是否是真实漏洞：漏洞URL链接”。

很明显，要不然就是codex这个agent本身做的不太行，要不然就是云端agent缺失一些功能。

## [高危漏洞](#_4)

既然严重漏洞是误报，我们看看那7个高危漏洞都是什么。

由于数量太多，我先把这7个漏洞标题列在这里：

* SMTP log keyword filter may bypass user scoping
* XSS report keyword filter can bypass user scoping
* File list filter bypasses user scoping via OR clause
* Web log search filter bypasses user scoping with OR clause
* FTP downloads allow unauthenticated access to user files
* Unauthenticated /api/initialize enables remote admin takeover
* Default config ships fixed JWT secret enabling token forgery

### [SMTP log keyword filter may bypass user scoping](#smtp-log-keyword-filter-may-bypass-user-scoping)

这个漏洞，Codex Security给出的问题如下：

> Introduced cross-tenant information disclosure risk in SMTP log filtering due to an OR condition not being parenthesized with the user\_id constraint.
>
> The updated SMTP log filter first applies `user_id = ?` and then appends a keyword condition containing `username LIKE ? OR emails::text LIKE ?`. In GORM, successive `Where` calls are concatenated with `AND` and do not automatically wrap raw SQL containing `OR`. This can yield SQL like `user_id = ? AND username LIKE ? OR emails::text LIKE ?`, which is equivalent to `(user_id = ? AND username LIKE ?) OR emails::text LIKE ?`. A user can supply a keyword that matches another user's email, resulting in cross-tenant disclosure of SMTP logs, which may contain sensitive content and credentials.

这很明显又是一个对于gorm不熟悉导致的问题。Claude Code给出了很明确的解释：

[![image-20260416230839857.png](/media/attachment/2026/04/16/3e688692-8797-411f-ad67-f0967e71fe33.fd4d82e4d206.png)](/media/attachment/2026/04/16/3e688692-8797-411f-ad67-f0967e71fe33.png)

gorm会自动给每个Where函数中生成的SQL语句增加括号，而不是像Codex Security说的那样“In GORM, successive `Where` calls are concatenated with `AND` and do not automatically wrap raw SQL containing `OR`”。

这也是一个误报。

### [XSS report keyword filter can bypass user scoping](#xss-report-keyword-filter-can-bypass-user-scoping)

这个漏洞和上一个漏洞完全一样，只是出现在不同模块，属于误报。

### [File list filter bypasses user scoping via OR clause](#file-list-filter-bypasses-user-scoping-via-or-clause)

这个漏洞和上一个漏洞完全一样，只是出现在不同模块，属于误报。

### [Web log search filter bypasses user scoping with OR clause](#web-log-search-filter-bypasses-user-scoping-with-or-clause)

这个漏洞和上一个漏洞完全一样，只是出现在不同模块，属于误报。

### [FTP downloads allow unauthenticated access to user files](#ftp-downloads-allow-unauthenticated-access-to-user-files)

这个漏洞，Codex Security的描述是：

> This commit introduces unauthenticated FTP file access by wiring the FTP server into the main app and implementing RETR/SIZE to return database-backed file contents without any password validation or authorization checks.
>
> The new FTP handler maps the USER argument to a domain and sets userID without verifying credentials, while PASS always succeeds. Subsequent SIZE/RETR commands read file content from the database based solely on that userID and stream it over the data connection. Since the FTP service is now wired into the main application lifecycle, any network client can choose a victim domain in USER and download files without authentication or user-enabled checks, resulting in cross-tenant data exposure.

其实Codex Security的分析也不算错，CoNote2中我确实设计了一个匿名FTP服务器。但这个FTP和HTTP服务器一样，用于储存并运行用户上传的文件，本来就是公开的文件，所以也谈不上未授权访问了。

这个漏洞不能算误报，但算作是AI没有完全理解我的仓库功能导致的误判。Claude Code也分析的比较透彻：

[![image-20260416232311949.png](/media/attachment/2026/04/16/aeef7817-26ed-4325-b892-09699057dbf1.45ec4e8f2e1d.png)](/media/attachment/2026/04/16/aeef7817-26ed-4325-b892-09699057dbf1.png)

### [Unauthenticated /api/initialize enables remote admin takeover](#unauthenticated-apiinitialize-enables-remote-admin-takeover)

这个漏洞，Codex Security的描述是：

> Introduced a public, unauthenticated initialization endpoint that grants superuser privileges when no users exist, enabling remote admin takeover on fresh deployments.
>
> The new /api/initialize route is registered before UserCheckerMiddleware...