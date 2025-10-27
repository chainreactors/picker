---
title: 3 ways to get Remote Code Execution in Kafka UI
url: https://artsploit.blogspot.com/2024/10/3-ways-to-get-remote-code-execution-in.html
source: Artsploit
date: 2024-10-04
fetch_date: 2025-10-06T18:50:21.727425
---

# 3 ways to get Remote Code Execution in Kafka UI

# [Artsploit](https://artsploit.blogspot.com/)

get shell or die trying

## Thursday, October 3, 2024

### 3 ways to get Remote Code Execution in Kafka UI

When I first encountered Kafka UI, I was thrilled that such a dangerous functionality is exposed without authentication. After some time I discovered different ways to turn it to Remote Code Execution.

Here is the technical analysis of these vulnerabilities in my GitHub blog: <https://github.blog/security/vulnerability-research/3-ways-to-get-remote-code-execution-in-kafka-ui/>

Posted by

[Michael Stepankin](https://www.blogger.com/profile/04043980848316413763 "author profile")

at
[3:48:00 AM](https://artsploit.blogspot.com/2024/10/3-ways-to-get-remote-code-execution-in.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=3888415135359405925&postID=2171863239734346833&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=3888415135359405925&postID=2171863239734346833&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=3888415135359405925&postID=2171863239734346833&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=3888415135359405925&postID=2171863239734346833&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=3888415135359405925&postID=2171863239734346833&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=3888415135359405925&postID=2171863239734346833&target=pinterest "Share to Pinterest")

[Older Post](https://artsploit.blogspot.com/2023/08/mtls-when-certificate-authentication-is.html "Older Post")
[Home](https://artsploit.blogspot.com/)

## Whoami

[Michael Stepankin](https://www.linkedin.com/in/michael-stepankin-4a4050110)
[@artsploit](https://twitter.com/artsploit)
artsploit [at] gmail.com
<https://github.com/artsploit/>
<https://portswigger.net/research/michael-stepankin>

## Popular Posts

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgz99dbfnGG4bdh7NBBcpTh2nH1S5_Ty0ps1RAWfkzHpD2G9JNBMgaKpSacOZfO2QJB918MW53dNjrJCkoEaYEw8CBWrBrenYMBsSE2uIJ2WvESlc3NUhG25GFMvjK59h3PMS-0WFcPHntW/w72-h72-p-k-no-nu/rce2_img2my.png)](https://artsploit.blogspot.com/2016/08/pprce2.html)

  [[demo.paypal.com] Node.js code injection (RCE)](https://artsploit.blogspot.com/2016/08/pprce2.html)

  When I am trying to find vulnerabilities in web applications, I always perform fuzzing of all http parameters, and sometimes it gives me som...
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-RC6gVnWqv_TVl5rC8Jufrf2KIgt2AGlzHpwzmb4Paxm87f_wy0P2CF9iTqGahXqENZRzlsDGmDdKzOsV7xZFrUyiJHZKm6byTYMHLMXj-aVU2ExTdbEfiS7cfLp13Z4seVUM3insKwPc/w72-h72-p-k-no-nu/img1my.png)](https://artsploit.blogspot.com/2016/01/paypal-rce.html)

  [[manager.paypal.com] Remote Code Execution Vulnerability](https://artsploit.blogspot.com/2016/01/paypal-rce.html)

  In December 2015, I found a critical vulnerability in one of PayPal business websites ( manager.paypal.com ). It allowed me to exe...
* [3 ways to get Remote Code Execution in Kafka UI](https://artsploit.blogspot.com/2024/10/3-ways-to-get-remote-code-execution-in.html)

  When I first encountered Kafka UI, I was thrilled that such a dangerous functionality is exposed without authentication. After some time I d...
* [mTLS: When certificate authentication is done wrong](https://artsploit.blogspot.com/2023/08/mtls-when-certificate-authentication-is.html)

  https://github.blog/2023-08-17-mtls-when-certificate-authentication-is-done-wrong/ In 2023 I spent some time researching x509 certificate au...
* [Hidden OAuth attack vectors](https://artsploit.blogspot.com/2021/03/hidden-oauth-attack-vectors.html)

  https://portswigger.net/research/hidden-oauth-attack-vectors I wrote this article while working at the PortSwigger Research team.
* [Pre-auth RCE in ForgeRock OpenAM (CVE-2021-35464)](https://artsploit.blogspot.com/2021/06/pre-auth-rce-in-forgerock-openam-cve.html)

  https://portswigger.net/research/pre-auth-rce-in-forgerock-openam-cve-2021-35464 I wrote this article while working at the PortSwigger Rese...
* [Exploiting JNDI Injections in Java](https://artsploit.blogspot.com/2019/01/exploiting-jndi-injections-in-java.html)

  https://www.veracode.com/blog/research/exploiting-jndi-injections-java I wrote this article while working at the Veracode Research team.
* [Exploiting Spring Boot Actuators](https://artsploit.blogspot.com/2019/02/exploiting-spring-boot-actuators.html)

  https://www.veracode.com/blog/research/exploiting-spring-boot-actuators I wrote this article while working at the Veracode Research team.
* [Spring View Manipulation Vulnerability](https://artsploit.blogspot.com/2020/09/spring-view-manipulation-vulnerability.html)

  https://www.veracode.com/blog/secure-development/spring-view-manipulation-vulnerability I wrote this article while working at the Veracode ...
* [Apache Solr Injection @ DEFCON 27](https://artsploit.blogspot.com/2019/08/apache-solr-injection-defcon-27.html)

  https://github.com/veracode-research/solr-injection A brand new vulnerability -  Apache Solr Injection , as well as new ways to RCE in this ...

## Blog Archive

* ▼
  [2024](https://artsploit.blogspot.com/2024/)
  (1)
  + ▼
    [October](https://artsploit.blogspot.com/2024/10/)
    (1)
    - [3 ways to get Remote Code Execution in Kafka UI](https://artsploit.blogspot.com/2024/10/3-ways-to-get-remote-code-execution-in.html)

* ►
  [2023](https://artsploit.blogspot.com/2023/)
  (1)
  + ►
    [August](https://artsploit.blogspot.com/2023/08/)
    (1)

* ►
  [2021](https://artsploit.blogspot.com/2021/)
  (2)
  + ►
    [June](https://artsploit.blogspot.com/2021/06/)
    (1)
  + ►
    [March](https://artsploit.blogspot.com/2021/03/)
    (1)

* ►
  [2020](https://artsploit.blogspot.com/2020/)
  (1)
  + ►
    [September](https://artsploit.blogspot.com/2020/09/)
    (1)

* ►
  [2019](https://artsploit.blogspot.com/2019/)
  (3)
  + ►
    [August](https://artsploit.blogspot.com/2019/08/)
    (1)
  + ►
    [February](https://artsploit.blogspot.com/2019/02/)
    (1)
  + ►
    [January](https://artsploit.blogspot.com/2019/01/)
    (1)

* ►
  [2016](https://artsploit.blogspot.com/2016/)
  (2)
  + ►
    [August](https://artsploit.blogspot.com/2016/08/)
    (1)
  + ►
    [January](https://artsploit.blogspot.com/2016/01/)
    (1)

## Labels

* [#bugbounty](https://artsploit.blogspot.com/search/label/%23bugbounty)
* [#paypal](https://artsploit.blogspot.com/search/label/%23paypal)
* [#RCE](https://artsploit.blogspot.com/search/label/%23RCE)

|  |  |
| --- | --- |
|  |  |

Powered by [Blogger](https://www.blogger.com).