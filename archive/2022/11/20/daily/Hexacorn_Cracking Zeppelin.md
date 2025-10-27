---
title: Cracking Zeppelin
url: https://www.hexacorn.com/blog/2022/11/19/cracking-zeppelin/
source: Hexacorn
date: 2022-11-20
fetch_date: 2025-10-03T23:17:08.595007
---

# Cracking Zeppelin

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2022/11/19/beyond-good-ol-run-key-part-139/)
[Next →](https://www.hexacorn.com/blog/2022/12/02/environment-is-variable/)

# Cracking Zeppelin

Posted on [2022-11-19](https://www.hexacorn.com/blog/2022/11/19/cracking-zeppelin/ "11:29 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

A few days ago Brian Krebs published a [piece](https://krebsonsecurity.com/2022/11/researchers-quietly-cracked-zeppelin-ransomware-keys/) about Zeppelin key cracking, so … since I was also involved in recovering files for some of the ransomware gang victims I thought I will add a few cents…

Back in 2020, I was approached by one of my clients to have a quick look at this particular piece of Zeppelin ransomware sample; and as you can imagine, I was immediately skeptical — it’s really unlikely to crack crypto of modern ransomware so I pretty much threw a towel, immediately, kinda by default.

BUT…

I was also aware of work of Lance Jones, and his UNIT221B on this particular malware strain and… that offered some hope…

I decided to try to factor these keys myself and what followed was a VERY intense week where I had to very quickly learn how to use and pay for AWS, how to allocate its resources, how to fix lots of other peoples’ bugs in a software that was — by that time — full of legacy assumptions, and – for the lack of a better word — in a need of a lot of troubleshooting and ‘code massaging’.

But the rewards were there, waiting…

The morning I saw the first cracked key I became ecstatic. I didn’t care about money this was earning me, I didn’t care what a bill I had to pay to AWS, here I was, breaking the damn ransomware! We were able to recover files for the client. Just like that!

Working in a cybersecurity space can be quite daunting, we often see ‘bad’ things, we live ‘failure’ every day. Yet, that moment I managed to crack the first key was a moment of triumph. Not all is lost. We are actually helping. We matter. it’s cheesy as hell, but there is no better satisfaction than disrupting the bad, for good.

And … it did happen again, I’ve spent a lot of time cracking other keys, but we did beat them. For a cost of a few hundred dollars on AWS, each time, we did beat them, every single time.

This entry was posted in [Factorization](https://www.hexacorn.com/blog/category/factorization/), [ransomware](https://www.hexacorn.com/blog/category/ransomware/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2022/11/19/cracking-zeppelin/ "Permalink to Cracking Zeppelin").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")