---
title: Custom and variant licenses: What’s in the fine print?
url: https://buaq.net/go-137214.html
source: unSafe.sh - 不安全
date: 2022-11-26
fetch_date: 2025-10-03T23:47:21.788437
---

# Custom and variant licenses: What’s in the fine print?

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Custom and variant licenses: What’s in the fine print?

See examples of custom and variant licenses and how Black Duck Audits flag these licenses to help
*2022-11-25 21:45:18
Author: [www.synopsys.com(查看原文)](/jump-137214.htm)
阅读量:16
收藏*

---

*See examples of custom and variant licenses and how Black Duck Audits flag these licenses to help legal teams evaluate software risk.*

An open source audit reveals much about modern software. A thorough one will draw attention to license issues that go beyond typical open source license conflicts.

The baseline finding of an audit is a complete, accurate [software Bill of Materials](https://www.synopsys.com/blogs/software-security/software-bill-of-materials-bom/) (SBOM) of open source and third-party software in the code. That’s table stakes to providing analysis about licenses, vulnerabilities, and the vitality of the various components. With open source and third-party code making up an average of 78% of a typical codebase, that’s valuable information.

At some level, it’s straightforward to map to licenses once the heavy lifting of properly creating the SBOM is complete. For the majority of open source components, a human familiar with open source could manually search around and find the licenses, but some require extensive research. Further, with an average of more than 500 components per codebase and more than 1,700 components in a given M&A transaction, this adds up to a ton of work.

In addition to establishing a complete and accurate SBOM, Black Duck® Audits take care identifying licenses and also prioritizing components for legal review. Common standard [permissive licenses](https://www.synopsys.com/blogs/software-security/5-types-of-software-licenses-you-need-to-understand/) don’t require a lot of legal attention, so it is license conflicts that are highlighted for priority review. However, these conflicts are not the only situations that call for legal review. Black Duck Audit reports highlight a few different situations that fall under the heading “Research Needed.”

## Custom and variant licenses

In about 30% of codebases we audit (and 70% of M&A transactions), we find code that has a one-off license, a custom variant on a standard license, or no license at all. When we can identify where a component came from—a repository or a website—but find no indication of a license or terms of use in that location or in the code, we designate those components as “Not Licensed.”

Variants of standard licenses can be tricky because a cursory glance might suggest MIT or BSD licenses, for example. But closer inspection often reveals that a developer got “clever” and put their own spin on the standard.

###### JSON licenses

The most common variant is the JSON license, which is the MIT license plus eight consequential words: Software shall be used for Good, not Evil. The ambiguity this introduces was enough for the Apache Foundation to put a moratorium on JSON-licensed code.

We’ve also found a variant on the variant, intended to provide a solution, although it’s unlikely to make the risk more palatable. In this variant, text is added to the license that reads, “If anyone notifies you in writing that you have not complied with ethics, you can keep your license by taking all practical steps to comply within 30 days after the notice. If you do not do so, your license ends immediately.”

###### Beerware licenses

The famous Beerware license similarly is a variant on the MIT license, with language suggesting that users should buy a beer for the copyright holder if they run into them in a bar. This is an unlikely occurrence, but many organizations are wary of such vague obligations.

Some variants seem frivolous, like the license for the AMD64 patch by Mikhail Teterin. Its language includes “This is free software; you can redistribute it and/or modify it under the terms of the BSD License. Use by owners of Che Guevarra paraphernalia is prohibited, where possible, and highly discouraged elsewhere.”

A less ambiguous and less frivolous example of variant license is Facebook’s 2017 spin on the BSD license. It reads like the BSD but includes a provision requiring the assignment of certain patent rights.

###### Commons Clause variant licenses

The Commons Clause is a variant designed to modify a standard [open source license](https://www.synopsys.com/blogs/software-security/open-source-licenses/) to restrict the software from commercial use. An extract reads, “…the License does not grant to you, the right to Sell the Software.” Software that appears, at first glance, to be permissively licensed under, for example, the Apache license may be rendered completely unusable by this clause.

## How Black Duck Audits report on custom and variant licenses

Black Duck Audit reports also call out for [legal review](https://www.synopsys.com/software-integrity/solutions/legal-teams.html) any language a creative developer put in code comments that seems to carry obligations or restrictions. This doesn’t include language that is clearly permissive, such as “You can do anything with this software that you want, no problem,” for example.

The Code Project License is an example of a custom license that has a confusing grant of rights and requires one to notify the copyright holder before redistributing. In the code comments, the author of Quirksmode says they don’t believe in copyrights but goes on to describe a bunch of obligations and restrictions that come with the code.

Another example of creative license language is the imgui\_lua\_bindings project, which includes the following text in its license:

“I don’t feel like writing a license so here’s it in laymans terms…

## Proprietary and commercial licenses

It’s not unusual for a codebase to contain content from third-party commercial software companies. Audits frequently find copyrights from Adobe, Microsoft, Oracle, and others. As part of [software due diligence](https://www.synopsys.com/blogs/software-security/four-aspects-software-due-diligence-audits/), it’s well worth an acquirer’s time to check whether proper licenses are in place and have been disclosed. Assuming licensing is proper, lawyers will still want to ensure that a change of control won’t introduce any issues going forward.

## Dual licenses

Increasingly, companies are using a clever business model implemented through dual licensing. The idea is to make software available to developers under an open source license that contains obligations that make it difficult to utilize for commercial purposes.

The AGPL license often turns up in this context; most companies can’t use AGPL-licensed code in their products. (There are also other licenses that more explicitly exclude commercial use without a commercial license.) If developers use code licensed under AGPL, their companies need to enter into a commercial license with the vendor for the same code.

When an audit uncovers dual-licensed software, we highlight it as such so the acquirer can ensure the target is properly licensed. Part of the business model of companies using a dual-license scheme is to go after users of the open source version—sometimes in court, as with the Artifex Hancom case, so these situations are well worth some diligence.

## Know what’s in your code

Getting a complete picture of whether code is properly licensed requires an accurate and complete Bill of Materials, as well as analysis of possible conflicts between the intended use and open source licenses included. And there are other license issues that go beyond standard open source, which require a deeper dive and more legal scrutiny. It’s...