---
title: BloodHound Operator — Dog Whispering Reloaded
url: https://posts.specterops.io/bloodhound-operator-dog-whispering-reloaded-156020b7c5e9?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-08-07
fetch_date: 2025-10-06T18:05:56.976342
---

# BloodHound Operator — Dog Whispering Reloaded

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F156020b7c5e9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fbloodhound-operator-dog-whispering-reloaded-156020b7c5e9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fbloodhound-operator-dog-whispering-reloaded-156020b7c5e9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-156020b7c5e9---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-156020b7c5e9---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# BloodHound Operator — Dog Whispering Reloaded

[![SadProcessor](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*3O5XzqqVZaOXYKxt)](https://medium.com/%40walter.legowski?source=post_page---byline--156020b7c5e9---------------------------------------)

[SadProcessor](https://medium.com/%40walter.legowski?source=post_page---byline--156020b7c5e9---------------------------------------)

14 min read

·

Aug 6, 2024

--

Listen

Share

It’s summer 2024 and we are back! Actually, we are SO back, so I decided that this required a little blog post.

If you like **BloodHound & PowerShell**, and if you want to automate all the BloodHound things, this post is written for you. In the last part, I’ll be sharing a new tool for all your Dog Whispering needs; but before that, a little intro…

> ***TL;DR:*** *Code is* [*here*](https://github.com/SadProcessor/BloodHoundOperator)*.*

Back in the BloodHound “Legacy” days, I wrote some PowerShell tooling to make my life easy and automate various tasks around BloodHound. When the [new BloodHound came out](/your-new-best-friend-introducing-bloodhound-community-edition-cb908446e270), most of these tools were made obsolete.
At first, I thought about going into a deep depression, but then I realized it would be a great opportunity to write a better tool, and so I did (and joined the SpecterOps crew while I was at it!).

This post introduces this new PowerShell module and contains instructions on how to get started.

**In this post**:

* Differences between the old and new BloodHound
* Intro to the new BloodHound REST API
* How to authenticate to the BloodHound API (with PowerShell)
* Getting started with the BloodHound Operator module

## Old BloodHound vs New BloodHound

In the old BloodHound (a.k.a. Legacy), the application was a single page electron app build on top of a neo4j graph database.

Press enter or click to view image in full size

![]()

Old BloodHound / CypherDog

Interacting with Legacy BloodHound via the command-line was done by sending cypher queries directly to the neo4j database (and this is what the old CypherDog tool was doing).

Although this neo4j cypher query endpoint covered a lot of possible use cases for automation, we were kind of limited to just that. No other BloodHound application features were accessible.

For example, you had to be there to drag the the zip in the UI in order to import data, which has been the main show stopper for my dreams of fully automated BloodHound Collect-Ingest-Query-Analyze cycles when working with legacy.

**But that was before…**

The [new BloodHound](https://github.com/SpecterOps/BloodHound) is a full Golang rewrite of the application and is built quite differently. The application is now containerized and composed of three images: BloodHound, neo4j and PostgreSQL.

Press enter or click to view image in full size

![]()

New BloodHound / BloodHound Operator

Not only does this allow for much easier install and updates (raise your hand if you remember the pain of finding the proper jdk…), but the addition of the new database allows for some solid application features; turning the dog into a beast:

* Multi-user access
* Granular user roles & permissions
* SAML SSO / MFA
* Secure API auth
* and more…

Last but not least, the new BloodHound is build around it’s own REST API: exactly what we need for automation. In the next part of this post, we’ll have a quick look at how it works.

> ***Note****: Accessing neo4j directly is still possible in BHCE, but it is no longer the recommended method as neo4j will be deprecated in a near future. Tooling built to interact with BHCE via neo4j will become obsolete.*

Press enter or click to view image in full size

![]()

## BloodHound REST API

## API Specs

The new BloodHound is build around it’s REST API. Request made via the UI are translated into REST API calls to query the databases. A list of available API endpoints can be found in the BloodHound UI under `Setting Icon`/`API Explorer`.

Press enter or click to view image in full size

![]()

Below a full list of endpoint & methods available at the time of writing this post:

```
Method Route                                                                     Summary
------ -----                                                                     -------
get    /api/v2/accept-eula                                                       Accept EULA
get    /api/v2/ad-domains/{domain_id}/data-quality-stats                         Time series list of data qu…
get    /api/v2/aiacas/{object_id}                                                Get aiaca entity info
get    /api/v2/aiacas/{object_id}/controllers                                    List aiaca controllers
get    /api/v2/asset-groups                                                      List all asset isolation gr…
post   /api/v2/asset-groups                                                      Create an asset group
delete /api/v2/asset-groups/{asset_group_id}                                     Delete an asset group
get    /api/v2/asset-groups/{asset_group_id}                                     Retrieve asset group by ID
put    /api/v2/asset-groups/{asset_group_id}                                     Update an asset group
get    /api/v2/asset-groups/{asset_group_id}/collections                         Returns asset group collect…
get    /api/v2/asset-groups/{asset_group_id}/combo-node                          Get the combo tree for an a…
get    /api/v2/asset-groups/{asset_group_id}/custom-selectors                    Get asset group custom memb…
get    /api/v2/asset-groups/{asset_group_id}/members                             List all asset isolation gr…
get    /api/v2/asset-groups/{asset_group_id}/members/counts                      List counts of members of a…
post   /api/v2/asset-groups/{asset_group_id}/selectors                           Update asset group selectors
put    /api/v2/asset-groups/{asset_group_id}/selectors                           Update asset group selectors
delete /api/v2/asset-groups/{asset_group_id}/selectors/{asset_group_selector_id} Delete an asset group selec…
get    /...