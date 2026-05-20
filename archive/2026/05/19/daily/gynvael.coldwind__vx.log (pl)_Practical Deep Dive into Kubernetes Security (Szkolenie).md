---
title: Practical Deep Dive into Kubernetes Security (Szkolenie)
url: https://gynvael.coldwind.pl/?id=808
source: gynvael.coldwind//vx.log (pl)
date: 2026-05-19
fetch_date: 2026-05-20T06:03:23.384548
---

# Practical Deep Dive into Kubernetes Security (Szkolenie)

# [![gynvael.coldwin//vx.log](/img/logo.gif)](/?blog=1)

![](/images/something_suspicious.png)

[Available for Consulting and Projects](https://hexarcana.ch/?utm=gyn-blog)
[hackArcana (edu+CTF)](https://hackarcana.com/?utm=gyn-blog-w)

![](/img/gynvael-close.jpg)

* [Return to dashboard ⇪](/)

### *Sections*

* **lang**: [![PL](/images/lang_pl.png)](?blog=1&lang=pl) | [![EN](/images/lang_en.png)](?blog=1&lang=en)
* **RSS**: [![RSS PL](/images/lang_pl.png)](/rss_pl.php) | [![RSS EN](/images/lang_en.png)](/rss_en.php)
* [About me](?id=50)
* [Tools](?id=182)
* [→ YT YouTube (EN)](https://youtube.com/c/GynvaelEN)
* [→ D Discord](/discord)* [→ M Mastodon](https://infosec.exchange/%40gynvael)* [→ T Twitter](https://twitter.com/gynvael)* [→ GH GitHub](https://github.com/gynvael)

        [![](/img/hA-logo.png)](https://hackarcana.com)

        [My edu+CTF site](https://hackarcana.com)

        [![](/img/hexarcana160_2.png)](https://hexarcana.ch)

        [My consulting company](https://hexarcana.ch)

        [![](/img/po_issue_5_rbanner.png)](https://pagedout.institute/)

        [Paged Out! zine](https://pagedout.institute/)

        [![](/img/ds_logo_160.jpg)](https://dragonsector.pl/)

        [Dragon Sector CTF Team](https://dragonsector.pl/)

### *Links / Blogs*

* **Security/Hacking:**
  + [j00ru's blog](https://j00ru.vexillium.org/)
  + [lcamtuf's thing](https://lcamtuf.substack.com/)
  + [pi3's blog](http://blog.pi3.com.pl/)
  + [tavis ormandy's site](https://lock.cmpxchg8b.com/)
  + [pawel golen's blog](http://wampir.mroczna-zaloga.org/)
  + [zaufana trzecia strona](http://zaufanatrzeciastrona.pl/)
  + [niebezpiecznik](https://niebezpiecznik.pl/)
  + [sekurak](https://sekurak.pl/)
* **Reverse Eng./Low-Level:**
  + [security news](https://www.secnews.pl/)
  + [rev3rsed](http://rev3rsed.blogspot.com/)
* **Programming/Code:**
  + [adam sawicki](http://asawicki.info/)

### *Posts*

* [Practical Deep Dive into Kubernetes Security (Workshop),](?id=807)
* [Paged Out! prints are here, and so is #7 CFP deadline,](?id=805)
* [CONFidence 2025 is next week,](?id=804)
* [No, CTRL+D in Linux terminal doesn't send EOF signal,](?id=801)
* [New edu platform and 'Sanitization and Validation and Escaping, Oh My!' article,](?id=800)
* [On hackers, hackers, and hilarious misunderstandings,](?id=799)
* [Paged Out! #5 is out,](?id=797)
* [CVEs of SSH talk this Thursday,](?id=796)
* [Debug Log: Internet doesn't work (it was the PSU),](?id=793)
* [FAQ: The tragedy of low-level exploitation,](?id=791)
* [→ see all posts on main page](/)

// copyright © Gynvael Coldwind
// design & art by Xa
// logo font (birdman regular) by utopiafonts / Dale Harris

/\* the author and owner of this blog hereby allows anyone to test the security of this blog (on HTTP level only, the server is not mine, so let's leave it alone ;>), and try to break in (including successful breaks) without any consequences of any kind (DoS attacks are an exception here) ... I'll add that I planted in some places funny photos of some kittens, there are 7 of them right now, so have fun looking for them ;> let me know if You find them all, I'll add some congratz message or sth ;> \*/

**Vulns found in blog:**
\* XSS *(pers, user-inter)* by ged\_
\* XSS *(non-pers)* by Anno & Tracerout
\* XSS *(pers)* by Anno & Tracerout
\* Blind SQLI by Sławomir Błażek
\* XSS *(pers) by* Sławomir Błażek

2026-05-19:

## [Practical Deep Dive into Kubernetes Security (Szkolenie)](?id=808)

workshop:hackarcana

[![](img/k8s.jpg)](https://hackarcana.com/practical-k8s-sec)

Kubernetes jest fundamentem nowoczesnej infrastruktury - i jednym z najbardziej atrakcyjnych celów dla atakujących. W związku z tym z wielką przyjemnością chciałbym dać znać, że na moim serwisie szkoleniowych hackArcana pojawiły się [praktyczne warsztaty poświęcone bezpieczeństwu Kubernetes](https://hackarcana.com/practical-k8s-sec). Oto garść informacji na ich temat:

* Szkolenie: **[Practical Deep Dive into Kubernetes Security](https://hackarcana.com/practical-k8s-sec)**
* Format: **Online, na żywo (z trenerami), szkolenie z ćwiczeniami**
* Trenerzy: **Jarosław Jedynak, Michał Leszczyński** (miałem okazję pracować / robić CTF z nimi, są solidni!)
* Czas trwania: **18 godzin rozbite na 6 tygodni (6 modułów)**
* Nagrania: **Wszystkie sesje będą nagrywane a nagrania będą dostępne minimum 3 miesiące**
* Harmonogram: **Wtorki, 19:00 CEST, 9.06, 16.06, 23.06, 30.06, 07.07, 14.07**
* Język: **Angielski**
* Poziom: **średnio zaawansowany** (tj. trzeba znać podstawy K8s)

Wszystkie informacje są na stronie szkolenia, ale wklejam tutaj również agendę (po angielsku, z uwagi na to, że szkolenie i tak jest w tym języku):

**Module 1 - Kubernetes Architecture**
Session: June 9th, Tuesday, 7 PM CEST

* Kubernetes components and how they interact
* Threat modeling the cluster: what attackers target and why
* Workshop environment walkthrough and lab access
* First hands-on exercises: exploring the cluster from an attacker's perspective

**Module 2 - Build Phase Security**
Session: June 16th, Tuesday, 7 PM CEST

* Container image pitfalls and common misconfigurations
* Source code and dependency scanning in CI/CD pipelines
* Supply chain risks: what happens before the image reaches the cluster
* Lab: identifying and fixing vulnerable image builds

**Module 3 - Deploy Phase Security**
Session: June 23rd, Tuesday, 7 PM CEST

* Image signing and verification
* Namespaces, pod security standards, and admission policies
* Secrets management: what goes wrong and how to fix it
* Lab: hardening deployment manifests and catching misconfigurations before they reach production

**Module 4 - Runtime Phase Security**
Session: June 30th, Tuesday, 7 PM CEST

* Service account tokens and their abuse
* Cloud environment pitfalls and metadata API attacks
* Privilege escalation and container breakout scenarios
* Lab: reproducing real runtime attack paths and applying mitigations

**Module 5 - Administration, Access Control, and Networking**
Session: July 7th, Tuesday, 7 PM CEST

* Authentication mechanisms and common weaknesses
* RBAC deep dive: misconfigurations, auditing, and least privilege
* Admission controllers and policy enforcement
* CNI configuration, network policies, firewalls, and network-level attacks
* Service meshes and their role in cluster security
* Lab: attacking and hardening cluster access and network segmentation

**Module 6 - Low-Level Container Security**
Session: July 14th, Tuesday, 7 PM CEST

* Linux namespaces, cgroups, and capabilities in depth
* Seccomp profiles: building and applying them
* Kernel exploits and container escape techniques
* Wrap-up, Q&A, and next steps in your Kubernetes security journey
* Lab: hands-on container isolation assessment and hardening

Szkolenie zaczyna się 9 czerwca, a zapisać można się tutaj: [Zarejestruj się!](https://hackarcana.com/practical-k8s-sec)

## Add a comment:

|  |  |
| --- | --- |
| Nick: |  |
| URL (optional): |  |
| Math captcha: 6 ∗ 3 ＋ 2 = |  |
|  | |