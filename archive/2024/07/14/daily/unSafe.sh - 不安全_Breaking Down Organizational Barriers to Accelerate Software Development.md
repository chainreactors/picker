---
title: Breaking Down Organizational Barriers to Accelerate Software Development
url: https://buaq.net/go-250435.html
source: unSafe.sh - 不安全
date: 2024-07-14
fetch_date: 2025-10-06T17:40:58.700984
---

# Breaking Down Organizational Barriers to Accelerate Software Development

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

![](https://8aqnet.cdn.bcebos.com/92292cb3d2308805361c2ce9406ef450.jpg)

Breaking Down Organizational Barriers to Accelerate Software Development

Understanding why certain features are not delivered can often be challenging. Management might blam
*2024-7-13 21:0:13
Author: [hackernoon.com(查看原文)](/jump-250435.htm)
阅读量:6
收藏*

---

Understanding why certain features are not delivered can often be challenging. Management might blame the technical teams, while the technical teams point fingers back at management. Meanwhile, the business side is caught in the middle, trying to identify the root cause while pushing for results regardless of the circumstances. This scenario typically arises after significant company growth or when earlier issues, previously easy to fix, have been neglected over time. It’s a common misconception that all problems in a tech company are purely technical; this is far from the truth.

In this article, I will outline areas within a company’s organization that can significantly hinder feature delivery. I will also suggest directions to investigate to identify root causes, which can then be escalated or resolved within your level of authority.

It’s crucial to understand our working environment before implementing any changes or improvements. Although many insightful books have been written on this topic, not all approaches will fit every company. This is not a reflection of doing something wrong, but rather an acknowledgment of the unique nature of each company.

An important note is the insights shared here are primarily related to software development and are most applicable to companies or departments with 50 or more employees.

## Organizational structure

First and foremost, understand the size and structure of your company. Identify the various departments and clarify your expectations from each. Assess whether all these departments are necessary. Create a diagram of the organizational structure, detailing each department and its roles, ensuring you understand what they do and why they exist. Often, each department consists of several teams — include these in your diagram as well but don’t describe them for now just keep team names.

As companies grow, organizational structures can become complex, making it difficult to track progress. In this complexity, you might lose sight of the original rationale behind the creation of certain departments or teams. Some teams might have been established to address problems that are no longer relevant. Here, is how it may look at a high level:

![Sample organizational structure](https://hackernoon.imgix.net/images/Y56tfSgkuIgpbx3m4OA15Phv3S93-wf83ilk.jpeg?auto=format&fit=max&w=3840)

**Once you have a clear diagram of your organizational structure, what comes next?**

## Employee hierarchy

Next, it’s essential to map out the hierarchy of your employees. Understanding who reports to whom, and why, is crucial. Line managers need to effectively communicate with their subordinates, whether they manage a large business unit or a small team. Communication should be clear, either in technical or business language, as handling both can be challenging. In larger companies, there may be direct and functional managers with distinct areas of responsibility, which should be clearly represented in your hierarchy diagram.

An employee hierarchy not only clarifies reporting lines but also helps identify verticals within the organization. Verticals are hierarchical structures that serve as shared resources across multiple departments, such as designers, HR, DevOps, and even developers. While verticals can be very beneficial, they can sometimes become bottlenecks, particularly when developers work on different projects and report to managers who are not familiar with the business goals or technical challenges. As a result, developers don’t get a proper feedbacks, managers don’t have a proper context. Therefore, understanding the hierarchy is vital for identifying and analyzing potential issues or prioritizations of the tasks. At the end, you will have something like this.

![Sample employee hierarchy ](https://hackernoon.imgix.net/images/Y56tfSgkuIgpbx3m4OA15Phv3S93-s5e3ii1.jpeg?auto=format&fit=max&w=3840)

**Annotation**

*CEO — Chief Executive Officer*

*CPO — Chief Product Officer*

*CTO — Chief Technical Officer*

*COO — Chief Operational Officer*

*HD — Head of Design*

*PO — Product Owner*

*HE — Head of Engineering*

*HS — Head of Sales*

*HM — Head of Marketing*

*D — Developer*

*PM — Product Manager*

*TL — Tech Lead*

*EM — Engineering Manager*

*S — Sales Manager*

*M — Marketer*

Compare your organizational structure with your reporting lines to gain insights into the involvement of each employee in various activities. Moreover, aligning your organizational structure with the employee hierarchy can help determine whether individuals are working within the same departments and teams and towards a common goal. The template of mapping is totally up to you but it could be like this:

![Mapping your employee hierarchy on one department](https://hackernoon.imgix.net/images/Y56tfSgkuIgpbx3m4OA15Phv3S93-oub3ivq.png?auto=format&fit=max&w=3840)

## Team’s responsibilities

It is important to clearly define the area in which each team operates. If a team works with code, specify the services they use and those they own. Surprisingly, these can often be different. Determine if the team operates solely within one department or if it is a platform team working on core features utilized by other teams without directly altering them.

Creating a table can be very helpful, with the following columns: team name, department, list of owned services, list of general services the team can modify but does not own (ideally, there should not be such services), and a brief description. This table will help you examine if multiple teams are working on the same codebase, leading to conflicts, or if there is a lack of clarity regarding their areas of responsibility. It can also reveal if a team is primarily fixing bugs or dabbling in various tasks without a clear focus.

This level of detail is crucial for identifying overlaps, conflicts, and gaps in team responsibilities, ensuring smoother collaboration and more efficient project execution.

## Employee’s responsibilities

In addition to describing teams, it is crucial to understand general employee’s positions and prepare a detailed description of their responsibilities. Often, what management envisions may differ significantly from what employees are actually doing. The software development industry has a variety of positions, and expectations can vary greatly from company to company. For instance, the role of an Engineering Manager can differ widely, not to mention roles like Delivery Managers, Data Scientists, Architects, Technical Leads, and so on. In some companies, a single person might be expected to fulfil multiple roles.

Setting clear expectations for each position is essential. This clarity not only helps track activities properly but also ensures that employees understand what is expected of them and what falls outside their scope. This applies to all positions within the organization. Clear role definitions help prevent overlap, reduce confusion, and ensure that everyone is working towards common goals in an efficient and organized manner.

## Feature delivery process

By now, you should have a clear understanding of your company structure, employee hierarchy, and responsibilities. Although things might seem confusing, the goal is to first understand the current state before making any changes. Now, it’s tim...