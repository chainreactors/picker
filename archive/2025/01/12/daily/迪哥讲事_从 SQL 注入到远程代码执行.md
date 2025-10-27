---
title: 从 SQL 注入到远程代码执行
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496813&idx=1&sn=eab6d19d242d637c1797d76ec3ae43fa&chksm=e8a5fe0edfd277188a3ce54336fe9ddf992716daadef1e899d9d6e4de34f5c25335a2222782c&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-01-12
fetch_date: 2025-10-06T20:09:32.267455
---

# 从 SQL 注入到远程代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6D2NqCIvYw2QC3wrERBnVAh4GKSeR8iaWUO3bbCmFwdbqkOpmiaxE4H5DGA1OhtRXfrnvibNJDVOqVA/0?wx_fmt=jpeg)

# 从 SQL 注入到远程代码执行

迪哥讲事

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

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmZHnoibapuiaRHDBMQ9iaRNRsZuEaE6VCgQuUOp58AGicCfEhUrFsANuhfYgIAJ31ZhUzKXp2PBHtmgw/640?wx_fmt=png&from=appmsg)**

背景介绍

#

还记得之前的那篇 [Hello Lucee! 让我们再次黑掉Apple～](http://mp.weixin.qq.com/s?__biz=MjM5Mzc4MzUzMQ==&mid=2650258000&idx=1&sn=59553b3a46882c411436d78be50bc02c&chksm=be92d1d489e558c218ff7da6655bd824f14e735bcf2323dfecaedcf5335c9631db0832326695&scene=21#wechat_redirect)吧？国外研究人员深入研究了 Lucee 的内部工作原理，并查看了 Masa/Mura CMS 的源代码，巨大的潜在攻击面让研究人员震惊，很明显，投入时间理解代码也收获了相应回报。

经过一周的探索，研究人员又发现了几个漏洞利用点，其中包括能够在 Apple Book Travel 门户中利用一个关键 SQL 注入漏洞，本文将为分享他们如何识别漏洞接收器并将其链接回源头，以及如何利用 SQL 注入来最终实现远程代码执行 (RCE)。让我们开始吧～

# 寻找漏洞点

通过使用 Masa/Mura CMS，研究人员了解了 Apple 环境中可访问的攻击面，他们的主要关注点是 JSON API，因为它公开了一些可在 Apple 环境中访问的方法。

研究人员发现找到的任何潜在的漏洞点都应该源自 JSON API，于是他们仔细考虑了优化方法，从而简化源代码审查流程。研究人员探讨了是否有静态分析器或 CFM 解析器能够在不考虑消毒器的情况下遍历代码。

例如，这是通过基于标签的 CFM 编写安全参数化 SQL 查询的方式：

```
<cfquery>
select * from table where column=<cfqueryparam cfsqltype="cf_sql_varchar" value="#arguments.user_input#">
</cfquery>
```

下面是不安全 SQL 查询的编写方式:

```
<cfquery>
select * from table where column=#arguments.user_input#
</cfquery>
```

如果能够解析和遍历代码，并且只打印具有未经处理的输入的 `cfquery` 标签，无论内部是否有 `cfqueryparam` 标签，那就太棒了。他们发现 https://github.com/foundeo/cfmlparser 可以轻松实现这一点。

以下是针对 SQL 注入接收器检测的方式：

* 解析每个 CFM/CFC 文件
* 浏览每个语句，如果它是标签且名称为 `cfquery` ，则选择该语句
* 删除 `cfquery` 代码块内的所有标签（如`cfqueryparam`），如果代码块中仍然有 `arguments` ，则输入不会参数化，并且查询容易受到 SQL 注入（假设没有其他验证）地方
* 打印此查询

```
<cfscript>
    targetDirectory = "../mura-cms/";
    files = DirectoryList(targetDirectory, true, "query");

    for (file in files) {
        if (FindNoCase(".cfc", file.name) or FindNoCase(".cfm", file.name)) {
            fname = file.directory & "/" & file.name;
            if (file.name != "dbUtility.cfc" && file.name != "configBean.cfc" && !FindNoCase("admin", file.directory) && !FindNoCase("dbUpdates", file.directory)) {
                filez = new cfmlparser.File(fname);
                statements = filez.getStatements();
                info = [];
                for (s in statements) {
                    if (s.isTag() && s.getName() == "cfquery" && FindNoCase("arguments", s.getStrippedInnerContent(true, true))) {
                        WriteOutput("Filename: <b>#fname#</b>");
                        WriteOutput("<br><br>" & s.getStrippedInnerContent(true, true));
                        WriteOutput("<br><br><br><br>");
                    }
                }
            }
        }
    }
</cfscript>
```

研究人员开始检查结果时考虑了一些事情，例如忽略像 `siteid` 这样的输入，因为 JSON API 会提前对其进行验证。

有两个其它输入的查询之一是这样的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmZHnoibapuiaRHDBMQ9iaRNRsBIN7qCfB6M96vrEd9obKicibMvuU8icUk3LfcyKia2f6NJA4ib572f8Af2Q/640?wx_fmt=png&from=appmsg)

# 从源头追溯

查看具有此查询的函数可以得出结论，只有一个可利用的参数，即 `ContentHistID` ，参数 `columnid` 是数字，并且 `siteid` 默认情况下经过验证。

```
<cffunction name="getObjects" output="false">
    <cfargument name="columnID" required="yes" type="numeric" >
    <cfargument name="ContentHistID" required="yes" type="string" >
    <cfargument name="siteID" required="yes" type="string" >

    <cfset var rsObjects=""/>

    <cfquery attributeCollection="#variables.configBean.getReadOnlyQRYAttrs(name='rsObjects')#">
        select tcontentobjects.object,tcontentobjects.name,tcontentobjects.objectid, tcontentobjects.orderno, tcontentobjects.params, tplugindisplayobjects.configuratorInit from tcontentobjects
        inner join tcontent On(
        tcontentobjects.contenthistid=tcontent.contenthistid
        and tcontentobjects.siteid=tcontent.siteid)
        left join tplugindisplayobjects on (tcontentobjects.object='plugin'
                                            and tcontentobjects.objectID=tplugindisplayobjects.objectID)
        where tcontent.siteid='#arguments.siteid#'
        and tcontent.contenthistid ='#arguments.contentHistID#'
        and tcontentobjects.columnid=#arguments.columnID#
        order by tcontentobjects.orderno
    </cfquery>

    <cfreturn rsObjects>

</cffunction>
```

函数 `getObjects` 在 `core/mura/content/contentRendererUtility.cfc` 组件的 `dspObjects` 函数中调用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmZHnoibapuiaRHDBMQ9iaRNRsfC5ZgqYcwkeEedniaFX1iaUibrlKgavLLVSOiaUv2k9R7QNnb9jRrvhOWg/640?wx_fmt=png&from=appmsg)

堆栈调用过程:

JSON API -> processAsyncObject -> object case: displayregion -> dspobjects() -> getobjects().

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmZHnoibapuiaRHDBMQ9iaRNRsunJmP1icC9pFcNJb1d5tyYVth6N0icLd0kFsRxWObQUWYuTewlS3Twtg/640?wx_fmt=png&from=appmsg)

# 触发与利用SQL注入

默认情况下，Lucee 在作为输入传递时通过在单引号前添加反斜杠来转义单引号，这可以通过使用反斜杠转义单引号之一来管理，应该会触发SQL注入：

```
/_api/json/v1/default/?method=processAsyncObject&object=displayregion&contenthistid=x%5c'
```

然而，事实并非如此，重新访问源代码后，研究人员发现了 `dspObjects` 函数中的一个关键条件，在调用 `getObjects` 之前，必须满足 `if` 条件：必须在 Mura servlet 事件处理程序中将 `isOnDisplay` 属性设置为 true。

最初，研究人员假设事件处理程序上的任何属性都可以通过将属性名称及其值作为参数传递来简单地设置，这个假设是基于在代码库中的调试会话。尝试以这种方式设置 `isOnDisplay` 属性没有成功，看来在代码中的某个地方，该属性被覆盖了。

在进行一些 grep 搜索后，研究人员发现了 JSON API 的 `processAsyncObjects` 中的 `standardSetIsOnDisplayHandler` 函数调用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmZHnoibapuiaRHDBMQ9iaRNRsTicZR2gD5Prs8Qt97icWR4Kqvic1kdic1kWfo8aRKnpBVSDvKQn4ygMD4Q/640?wx_fmt=png&from=appmsg)

通过简单地向 `previewID` 参数传递任何值，就可以设置 `previewID` 属性，反过来又会将 `isOnDisplay` 属性设置为 true。

```
/_api/json/v1/default/?method=processAsyncObject&object=displayregion&contenthistid=x%5c'&previewID=x
```

成功！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmZHnoibapuiaRHDBMQ9iaRNRstRBkPJ3CdAucwAXfOer3AI3t4WhecRvVgHqzznn78siaY1b3K8FJySQ/640?wx_fmt=png&from=appmsg)

由于这是一个基于错误的 SQL 注入，因此可以利用它来实现远程代码执行 (RCE)，在本地环境中通过以下步骤成功执行了 RCE：

1. 重置管理员用户的密码
2. 通过SQL注入获取重置令牌和用户ID
3. 使用带有泄露信息的密码重置端点
4. 利用插件安装上传 CFM 文件

然而在Apple的环境中，只遇到了一个Unhandled Exception错误，没有任何查询相关的信息，从而将其变成了SQL盲注，幸运的是，token和用户 ID 是 UUID，因此泄露它们相对简单。

利用一些脚本编写，完成任务：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmZHnoibapuiaRHDBMQ9iaRNRsdwG0m18VZ89AeTTC3nicXCVdvH6qvFVIBZZXFWHtVIaWDDU0opiaNQ5g/640?wx_fmt=png&from=appmsg)

研究人员立即向苹果提交了漏洞报告，包括演示登录帐户的PoC（概念验证），同时理论上向他们提供了 RCE 详细信息。

# 通过Nuclei检测

可以利用以下 Nuclei 模板来识别 SQL 注入漏洞：

```
id: CVE-2024-32640
info:  name: Mura/Masa CMS - SQL Injection  author: iamnoooob,rootxharsh,pdresearch  severity: critical  description: |    The Mura/Masa CMS is vulnerable to SQL Injection.  reference:    - https://blog.projectdiscovery.io/mura-masa-cms-pre-auth-sql-injection/    - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-32640  impact: |    Successful exploitation could lead to unauthorized access to sensitive data.  remediation: |    Apply the vendor-supplied patch or update to a secure version.  metadata:    verified: true    max-request: 3    vendor: masacms    product: masacms    shodan-query: 'Generator: Masa CMS'  tags: cve,cve2022,sqli,cms,masa,masacms
http:  - raw:      - |        POST /index.cfm/_api/json/v1/default/?method=processAsyncObject HTTP/1.1        Host: {{Hostname}}        Content-Type: application/x-www-form-urlencoded
        object=displayregion&contenthistid=x\'&previewid=1
    matchers:      - type: dsl        dsl:          - 'status_code == 500'          - 'contains(header, "application/json")'          - 'contains_all(body, "Unhandled Exception")'          - 'contains_all(header,"cfid","cftoken")'        condition: and
```

# 结论

对 Masa/Mura CMS 的探索是一次相当有意义的旅程，代码审查过程首先关注易受攻击的 SQL 注入代码模式，然后利用 CFM/CFC 解析器在代码库中搜索特定模式，这与 `Semgrep` 的方法类似。一旦识别出潜在的接收器，将追溯源头，在本例中为 Mura/Masa CMS 的 JSON API。

苹果公司在收到初步报告后 2 小时内做出了回应并实施了修复，迅速解决了所报告的问题。

Masa 是 Mura CMS 的开源分支，它们非常透明，并发布了带有修复程序的新版本 Masa CMS。7.4.6、7...