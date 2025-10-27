---
title: Manual LDAP Querying: Part 2
url: https://posts.specterops.io/manual-ldap-querying-part-2-8a65099e12e3?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-05-03
fetch_date: 2025-10-06T17:17:42.220612
---

# Manual LDAP Querying: Part 2

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8a65099e12e3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fmanual-ldap-querying-part-2-8a65099e12e3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fmanual-ldap-querying-part-2-8a65099e12e3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-8a65099e12e3---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-8a65099e12e3---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Manual LDAP Querying: Part 2

[![Hope Walker](https://miro.medium.com/v2/resize:fill:64:64/0*1dLPs8bH356Tkfng.jpg)](https://medium.com/%40Ice_Moon?source=post_page---byline--8a65099e12e3---------------------------------------)

[Hope Walker](https://medium.com/%40Ice_Moon?source=post_page---byline--8a65099e12e3---------------------------------------)

17 min read

·

May 2, 2024

--

1

Listen

Share

This post is a follow-up to [my previous post](/an-introduction-to-manual-active-directory-querying-with-dsquery-and-ldapsearch-84943c13d7eb) on manual LDAP querying. I would highly recommend reading that post prior to reading this one if you are interested in some of the basics of searching LDAP.

A few people asked why I chose dsquery and ldapsearch for the last blog. There are several options for querying LDAP, but dsquery and ldapsearch were the tools I was most comfortable with. Additionally, dsquery being signed binary, it is easy to get on target without being flagged. Similarly, with ldapsearch, it is easily installed and is sometimes already present on hosts and it can be run through SOCKS proxies. For this blog, I will show less examples for conciseness, but remember the focus is how to query with LDAP filters. The important item to focus on is the LDAP filters themselves.

Many tools that query LDAP have a way for you to create custom filters baked in. Therefore, if you understand how to create LDAP filters, you can use any tool that allows you to create your own custom LDAP filter. While this blog focuses on querying in a Windows Active Directory (AD) environment, LDAP queries can work in other forms of directory services.

For this blog, I will focus on items not covered in the previous blog as well as discuss some of the complexities of manually querying. The goal is to try to get a more accurate understanding of an AD environment and recognize some of the common issues that can arise from querying manually.

## Combination Filters

One important item not included in the first blog was how to create compound filters with an OR operator. A compound filter with an OR operator will look like this:
`"(|(attribute1=value1)(attribute1=value2))"`

In this filter, the “`|`” indicates that it is a combination filter, and any results should have “value1” or “value2” for attribute1. As with other filters, these operators can be combined with others to create more complex queries.

Press enter or click to view image in full size

![]()

`dsquery * -filter "(&(objectClass=computer)(|(name=*WIN-10*)(name=*WIN-11))(!(description=*HIPAA*)))"`

The image and query listed show how these different operators can be used in a combination filter. Here, we are using the AND (`&`), OR (`|`), NOT (`!`), and wildcard (`*`) operators to create the query. The plain language explanation for this filter would read, “I want all of the computer objects that have WIN-10 or WIN-11 in the name but do not have HIPAA in the description.” When you are creating these queries, keep in mind that the parentheses do matter and if you do not close them correctly, your query may fail or give you inaccurate results.

Press enter or click to view image in full size

![]()

`dsquery * -filter "(&(objectClass=computer)(|(name=*WIN-10*)(name=*WIN-11)(!(description=*HIPAA*))))"`

This is one example of how the parentheses can affect your results. In this example, the parentheses around the OR statement were moved to include our not parameter. In plain language, the way this is interpreted is, “I want all of the computer objects that have WIN-10, WIN-11, or does not have HIPAA in the description.” The JZOID-WIN-10, which should have been excluded because it contains HIPAA in the description, was included in the results because it met the WIN-10 parameter in the OR statement while others which do not have WIN-10 or WIN-11 were included because they do not have HIPAA in the description.

## Nested Groups

Nested groups occur when one group is added as a member of another group. This is a common practice but can create additional complexities and unforeseen results. It can also make it harder to find what you are looking for when you are trying to understand permissions in an environment because permissions inherit down to nested members of a group. Here I will show why it is important to check for nested groups. In this first screenshot, the query is looking for any users who are members of the Domain Admins group.

Press enter or click to view image in full size

![]()

`dsquery * -filter "(&(objectClass=user)(memberOf=CN=Domain Admins,CN=Users,DC=PLANETEXPRESS,DC=LOCAL))"`

However, when we look at the same group through the administrator view, we see there is a group nested within the Domain Admins groups.

Press enter or click to view image in full size

![]()

This group did not show up because our query is looking for users who are members of the Domain Admins group, not groups who are members of the Domain Admins group.

This next block is a query which filters on the memberOf attribute of the Domain Admins group. This returns the Security group, but does not show who the members are who may also be part of the Domain Admins group.

Press enter or click to view image in full size

![]()

`dsquery * -filter "(&(objectClass=group)(name=Domain Admins))" -attr member`

From this information, you could further expand and query who the members of the Security group are, as shown below.

Press enter or click to view image in full size

![]()

`dsquery * -filter "(&(objectClass=group)(name=Security))" -attr member`

One option for getting a more precise list of group membership would be to ensure that your filter is not being too restrictive. While usually we want to be as specific as possible to reduce the number of results that must be evaluated, this query is an example of how making a query too specific of a filter can give inaccurate results.

Press enter or click to view image in full size

![]()

`dsquery * -filter "(memberOf=CN=Domain Admins,CN=Users,DC=PLANETEXPRESS,DC=LOCAL)"`

By not specifying an object class in the query, we will get a list of both the users and groups that are members ...