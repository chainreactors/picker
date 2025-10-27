---
title: BloodHound Community Edition Custom Queries
url: https://blog.compass-security.com/2025/01/bloodhound-community-edition-custom-queries/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-29
fetch_date: 2025-10-06T20:10:56.814186
---

# BloodHound Community Edition Custom Queries

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [BloodHound Community Edition Custom Queries](https://blog.compass-security.com/2025/01/bloodhound-community-edition-custom-queries/ "BloodHound Community Edition Custom Queries")

[January 28, 2025](https://blog.compass-security.com/2025/01/bloodhound-community-edition-custom-queries/ "BloodHound Community Edition Custom Queries")
 /
[Emanuel Duss](https://blog.compass-security.com/author/eduss/ "Posts by Emanuel Duss")
 /
[1 Comment](https://blog.compass-security.com/2025/01/bloodhound-community-edition-custom-queries/#comments)

This blog post introduces our new custom queries for BloodHound Community Edition (CE) and explains how you can use them effectively to analyze your Active Directory infrastructure.

[![The 3d printed BloodHound logo on a notebook where the BloodHound UI is running in the background.](https://blog.compass-security.com/wp-content/uploads/2025/01/bloodhound_banner.jpg)](https://blog.compass-security.com/wp-content/uploads/2025/01/bloodhound_banner.jpg)
> *TL;DR*: Check out our new [BloodHound CE custom queries](https://github.com/compassSecurity/bloodhoundce-resources)!

## Active Directory and BloodHound

The majority of our customers run a Microsoft Active Directory infrastructure, either exclusively on-prem or increasingly in hybrid environments using Entra ID. BloodHound is one of our primary tools for identifying potential misconfigurations and attack paths in Active Directory. Therefore, we use BloodHound to analyze our customer’s infrastructure in nearly every internal penetration test we conduct.

In 2020, we published some custom queries[1](#8157f65e-cab6-48c5-9c7c-a11e15bfac82), to get even more out of the collected data with BloodHound. These are available on GitHub[2](#0a554723-20de-43ae-b2f6-7d56d0cf28e6).

In August 2023 [3](#1b4d1ec2-2adf-428d-9a90-e844ddb261d9), the BloodHound Community Edition (CE) was released. The queries from the “legacy” version of BloodHound are not compatible with the new CE version. To address this, we rewrote the queries to ensure compatibility with the CE edition and added many new queries to uncover even more attack paths. These queries can be found in our new BloodHound CE repository on GitHub[4](#c80c2de5-df4c-4328-9523-0bcf63a5f7b1):

[BloodHound CE Resources](https://github.com/CompassSecurity/bloodhoundce-resources)

## BloodHound CE Queries

The queries are available in a markdown file in the repository, allowing you to easily copy (1) them to your BloodHound CE instance. Sometimes, the queries also contain some additional information (2):

[![](https://blog.compass-security.com/wp-content/uploads/2025/01/image-6-1024x479.png)](https://blog.compass-security.com/wp-content/uploads/2025/01/image-6.png)

Example query you can copy (1) with some additional information (2).

BloodHound CE only supports importing queries through the BloodHound API. The Readme contains step-by-step instructions that guide you through the process of importing the queries, along with a script that simplifies the entire procedure using BloodHound Operator[5](#1d8a3266-1b53-45b8-a843-2b14376e8053).

Once the import is complete, you will see the queries in BloodHound (since ordering and categories are no longer supported, some ASCII formatting and a numbering scheme has been used instead):

[![](https://blog.compass-security.com/wp-content/uploads/2025/01/image-3.png)](https://blog.compass-security.com/wp-content/uploads/2025/01/image-3.png)

Our new BloodHound CE Custom Queries

There are queries regarding the domain, accounts, privileged accounts, computer accounts, Kerberos, owned objects, shortest paths, DACL abuse, GPOs and ADCS. I won’t go into detail about all these queries — you should try them out for yourself! BloodHound also provides you some example data[6](#fec95daa-c44f-4f3e-b5c2-126678555386).

## BloodHound Operator Queries

Since the new BloodHound no longer supports queries that update objects, we had to adopt a different approach. We decided to use BloodHound Operator to modify the objects. After importing the BloodHound Operator module and authenticating to the BloodHound API, the queries can be copied and pasted from the corresponding markdown file.

For example, if you want to set the groups “Server Operators”, “Account Operators” and “Print Operators” as high-value targets, you can use the first query:

[![](https://blog.compass-security.com/wp-content/uploads/2025/01/image-7-1024x321.png)](https://blog.compass-security.com/wp-content/uploads/2025/01/image-7.png)

Example query to update groups in BloodHound.

This will now mark these groups again as high-value, as it was in BloodHound legacy:

[![](https://blog.compass-security.com/wp-content/uploads/2025/01/image-4.png)](https://blog.compass-security.com/wp-content/uploads/2025/01/image-4.png)

The Account Operators group is again marked as high-value

There are several queries that set various accounts as high-value targets, add information about SMB signing, and remove inactive accounts. Be sure to check them out!

## BloodHound Legacy vs. BloodHound CE

The new BloodHound CE version is not yet perfect. Some useful features from the legacy version are missing, such as the back button, the ability to remember the “layout” display setting, custom query import via the UI, custom query ordering and categories, selection dialogues in queries, modifying queries, or UNION queries. However, these are minor issues, and either workarounds exist or some workflows may need to be adjusted.

Unfortunately, there is at least one more significant bug. The RDP/Admin/Code Execution edges are not always shown when configured via GPO[7](#ed06a5a3-119e-4403-a196-48c73565f91a). Since this information can be very crucial for penetration tests, it’s still necessary to use the legacy BloodHound version alongside the CE version until this is fixed.

Nonetheless, we really encourage using the new CE version! It includes many more edges and attack paths, such as all those related to AD Certificate Service abuse, applying GPOs, collecting additional AD properties, and, not to forget, all the attack paths concerning Azure/Entra ID (which we will cover in another blog post, stay tuned!).

For more information about BloodHound, its usage, possible attacks, and more, refer to the official documentation[8](#ae957881-9f43-47aa-94c5-fd866ef2657d).

So, have fun using our queries while exploring your next attack paths ;-)!

## Want to Learn Hands-On?

Gain experience and train your IT security skills in **realistic attack scenarios** with our Internal Network and System Security course in Zurich May 5th to 7th.

The course covers prevalent security issues, attacker tools, and methodologies, and introduces countermeasures for vulnerabilities commonly exploited. Seats are limited. Sign-up now.
<https://www.compass-security.com/en/trainings/internal-network-and-system-security/inss-zurich-may-2025>

## References

1. Make the most out of BloodHound: <https://blog.compass-security.com/2020/07/make-the-most-out-of-bloodhound/> [↩︎](#8157f65e-cab6-48c5-9c7c-a11e15bfac82-link)
2. GitHub, Compass Security, BloodHoundQueries: <https://github.com/CompassSecurity/BloodHoundQueries> [↩︎](#0a554723-20de-43ae-b2f6-7d56d0cf28e6-link)
3. BloodHound Community Edition: A New Era: <https://posts.specterops.io/bloodhound-community-edition-a-new-era-d64689806e90> [↩︎](#1b4d1ec2-2adf-428d-9a90-e844d...