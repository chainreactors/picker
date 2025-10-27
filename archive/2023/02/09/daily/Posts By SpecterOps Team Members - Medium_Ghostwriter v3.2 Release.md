---
title: Ghostwriter v3.2 Release
url: https://posts.specterops.io/ghostwriter-v3-2-release-5acb517f154c?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2023-02-09
fetch_date: 2025-10-04T06:10:50.484091
---

# Ghostwriter v3.2 Release

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5acb517f154c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fghostwriter-v3-2-release-5acb517f154c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fghostwriter-v3-2-release-5acb517f154c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-5acb517f154c---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-5acb517f154c---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Ghostwriter v3.2 Release

[![Christopher Maddalena](https://miro.medium.com/v2/resize:fill:64:64/1*Qau5i8aEfpZkMb2PCBnyZw.jpeg)](https://cmaddy.medium.com/?source=post_page---byline--5acb517f154c---------------------------------------)

[Christopher Maddalena](https://cmaddy.medium.com/?source=post_page---byline--5acb517f154c---------------------------------------)

4 min read

·

Feb 8, 2023

--

Listen

Share

Press enter or click to view image in full size

![Ghostwriter v3.2, the tagging release]()

SpecterOps has released Ghostwriter v3.2 with some significant enhancements we think you’ll like. We overhauled how you interact with operation logs and added support for tagging clients, projects, reports, findings, evidence files, domains, servers, operation logs, and log entries.

## Tagging

Tags will help you organize and customize your projects. At the most basic level, a tag can help communicate something about the tagged object, like this project:

Press enter or click to view image in full size

![Tags Applied to a Project]()

Tags Applied to a Project

Ghostwriter’s tags work like tags in most modern web applications that you’re already familiar with. Tags are comma-separated and appear as grey badges in the interface. A comma designates the end of a tag, but you can get creative with other symbols. For example, these are all valid tags:

* att&ck:t1549
* language:en
* T1592.002
* objective-1

On the back end, Ghostwriter tracks which objects share a tag and which have similar tags. We plan to expand the tagging features to enable actions like filtering and sorting with tags. For now, tags act mostly as labels in the interface, but that doesn’t mean they are purely cosmetic.

Tags are accessible in your report templates, and you can use them to create more dynamic report content. Let’s take the above red team project as an example. If you were to look at the raw JSON report data, the `project` object has this `tags` key:

```
"tags": [
  "cvss:on",
  "language:en",
  "project"
]
```

We can use the *cvss:on* tag to check if we want to include a finding’s CVSS score alongside the severity rating. This change requires adding a simple *if/else* statement:

Press enter or click to view image in full size

![Jinja2 for Adding CVSS Based on the Project’s Tags]()

Jinja2 for Adding CVSS Based on the Project’s Tags

If the project’s tags include *cvss:on*, we will get output like this:

Press enter or click to view image in full size

![]()

The Results Displaying the CVSS

Taking this concept further, you can even create custom variables for your reports. With a little more work, we can use a tag like *entity-tested:internal network* to insert text into our report template. In this example, tags help us dynamically insert some text:

Press enter or click to view image in full size

![Jinja2 for Using Tags to Insert Content]()

Jinja2 for Using Tags to Insert Content

That Jinja2 expression checks the report’s tags for a tag that starts with *entity-tested:* and then strips that prefix from the tag to insert our custom variable. It does the same thing to dynamically update the document’s header based on a `status` tag. The output looks like this:

Press enter or click to view image in full size

![The Results Showing the Tags Inserted as Content]()

The Results Showing the Tags Inserted as Content

You can achieve similar results with *if/else* statements based on other values, like the project type or the presence of a certain finding type, but tags enable more flexibility. With some creativity, tags enable a wide range of report customization!

Tagging is also a helpful tool in the new activity logging interface.

## All New Operation Logs

We overhauled the logging page to make everything easier to use. When you visit the new page for the first time, you may notice the new *Show/Hide Columns* button. Previously, you had to choose which columns you wanted to view each time you visited the page. Your selections are now stored in your browser’s local storage so they are persistent between page refreshes and visits.

Press enter or click to view image in full size

![New Activity Logging Interface]()

New Activity Logging Interface

Another big change is the new editing window. It is now possible to edit fields all at once. All you need to do is double-click the table row you want to edit. Forms for new entries will be pre-filled with the current timestamp and your username so you can focus on filling in the important details.

Press enter or click to view image in full size

![New Log Event Modal]()

New Log Event Modal

As mentioned above, you can now tag logged events, and these tags can help you call out events with multi-colored tags. Ghostwriter will stylize tags that contain certain strings to help you easily identify key events in your logs. For example, a tag with `detect` will appear as a blue badge to help you identify events related to a detection or deconfliction event.

![Example Tags on a Log Event]()

Example Tags on a Log Event

There is more information on this feature in the Ghostwriter wiki:

[## Interacting with the Operation Log Table

### Using the live activity log

www.ghostwriter.wiki](https://www.ghostwriter.wiki/features/operation-logs/create-a-new-entry?source=post_page-----5acb517f154c---------------------------------------#applying-tags-to-log-entries)

## Wrap Up

This is the first big release of 2023 with more to come. As always, look here for more updates on Ghostwriter’s roadmap and future releases. For now, you can get the latest release on GitHub:

[## Release Ghostwriter v3.2.0 · GhostManager/Ghostwriter

### Summary This release includes significant enhancements, such as support for adding tags to most objects (e.g., log…

github.com](https://github.com/GhostManager/Ghostwriter/releases/latest?source=post_page-----5acb517f154c---------------------------------------)

[Red Team](https://medium.com/tag/red-team?source=post_page-----5acb517f154c---------------------------------------)

[Technology](https://medium.com/tag/technology?source=post_page-----5acb517f154c---------------------------------------)

[Cybersecurity](https...