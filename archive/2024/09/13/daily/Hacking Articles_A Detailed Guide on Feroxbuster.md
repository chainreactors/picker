---
title: A Detailed Guide on Feroxbuster
url: https://www.hackingarticles.in/a-detailed-guide-on-feroxbuster/
source: Hacking Articles
date: 2024-09-13
fetch_date: 2025-10-06T18:20:01.558876
---

# A Detailed Guide on Feroxbuster

[Skip to content](#content)

Hacking Articles

## Recent Posts

* [AWS: IAM CreateLoginProfile Abuse](https://www.hackingarticles.in/aws-iam-createloginprofile-abuse/)
* [Privacy Protection: Encrypted DNS](https://www.hackingarticles.in/privacy-protection-encrypted-dns/)
* [Privacy Protection: Windows Privacy](https://www.hackingarticles.in/privacy-protection-windows-privacy/)
* [Privacy Protection: Browsers](https://www.hackingarticles.in/privacy-protection-browsers/)
* [Privacy Protection: Password Manager](https://www.hackingarticles.in/privacy-protection-password-manager/)

## Most Used Categories

* [CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/) (504)
  + [VulnHub](https://www.hackingarticles.in/category/ctf-challenges/vulnhub/) (311)
  + [HackTheBox](https://www.hackingarticles.in/category/ctf-challenges/hackthebox/) (164)
* [Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/) (408)
* [Red Teaming](https://www.hackingarticles.in/category/red-teaming/) (126)
* [Website Hacking](https://www.hackingarticles.in/category/website-hacking/) (64)
* [Cyber Forensics](https://www.hackingarticles.in/category/cyber-forensics-tricks/) (68)
* [Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/) (59)
* [Hacking Tools](https://www.hackingarticles.in/category/collection-of-hacking-tools/) (33)
* [Pentest Lab Setup](https://www.hackingarticles.in/category/pentest-lab-setup/) (29)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Search for:

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/)
»* [A Detailed Guide on Feroxbuster](https://www.hackingarticles.in/a-detailed-guide-on-feroxbuster/)
»

[Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/)

# A Detailed Guide on Feroxbuster

[September 12, 2024June 19, 2025](https://www.hackingarticles.in/a-detailed-guide-on-feroxbuster/) by [Raj](https://www.hackingarticles.in/author/raj/)

**This Feroxbuster guide** covers everything you need to know about using this powerful tool to identify directories and files on web servers through brute-force techniques. **Feroxbuster** is a robust tool designed to identify directories and files on web servers using **brute-force techniques**. It is frequently utilized in penetration testing and security evaluations to **detect concealed paths and resources**. Here we are going to discuss various tasks which we can perform using **Feroxbuster**.

### Table of contents

* **Lab setup**
* **Installation**
* **Default mode**
* **Redirects**
* **Extensions**
* **Result output**
* **User agent**
* **Filter status code**
* **Quiet mode**
* **Controlling threads**
* **Custom wordlist**
* **Disable recursion**
* **Limit recursion depth**
* **Force Recursion**
* **Filter by character size**
* **Filter by number of words**
* **Filter by number of lines**
* **Filter by status code using deny list**
* **Filter by status code using allow list**
* **Generating random User-Agent**
* **HTTP methods**
* **Custom headers**
* **Cookies**
* **Adding slash**
* **Capturing requests in Burp**
* **Read target from list**
* **Resume from last state**
* **Follow redirect**
* **Timeout**
* **Comparasion between Feroxbuster and other tools**
* **Conclusion**

### Lab setup

Target Machine: 192.168.1.4

Attacker Machine: 192.168.1.31 (Kali Linux)

After setting up a web server in the target machine, we can proceed with the enumeration in the kali linux after installing Feroxbuster.

### Installation

To install the Feroxbuster in kali linux, we can use the following command:

```
apt install feroxbuster
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqU9nvAjtNDaaX7aYFWfV8BMLsfrUkp_Mg5mdGi2KbXOhHOec1knKLkksJAEz7g3B8oMM98KQiMgDKeSrrwkuWjfV5KwDIcWsthtdsZ0MEidx_liIFhDKNBhD83rPAxxpgVttJbrxb2nghsvyHJkG3fBy2SKpTmMh1YZsxJ198Uvp9H3DEeUaW7K2SQdeG/s16000/1.png)

### Default mode

Once we are done with the installation, we can proceed with the enumeration part. To perform a default directory brute force, we can use the following the command:

```
feroxbuster -u http://192.168.1.4
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCdBWdpuQtFw1BJQfzo8b8Ibn7mBuJsdJFLAb0MgFTw6rNDGFZu1C7HN2C7MlOi7h-QUmCbb-b0pq_ueK9N7fUqs8O8eQveXMcPEtXauy3PavrSS4rZZU4b19p2eqizj9fBwe-TrHWpVO56-6t4OhW_j6lfw715jinab6nTNvHEw5BGRyPf9PnZlVCOJZr/s16000/2.png)

It can be seen from above that the wordlist used in default mode is the **raft-medium-directories.txt**.

To get a less verbose output, we can use the **–silent** flag to hide the non-essential data.

```
feroxbuster -u http://192.168.1.4 --silent
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDgVL6Q524kSZu9ZCEeLEFEpa4wHR-BsPIemI9gOIPRE9J1OjTjX8Y6jcH_Hq0MF6h-4U2TpaTUrUhHBd6jpBgUX_cBteC3Wcp7p2ZljmrRUOZJ_7lzN5_ZnsU8ocQIpchrEofOIeckrdKhDH8ioVEeuM3YdATRZPNfCWPvROpNhBRtWNPACiucEZC-00x/s16000/3.png)

### Redirects

In order to allow the Feroxbuster to continue the directory brute forcing on the redirected URL, we can use the **-r** or **–redirect** flag. For example if http://192.168.1.4 redirects to http://192.168.1.4/newpath, Feroxbuster will follow this redirection and continue to scan http://192.168.1.4/newpath for directories and files.

```
feroxbuster -u http://192.168.1.4 -r
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCuqYHm6dGRy7RqJA-n-PJdOKS_Jmdne_C_7IRGUQdFHdrWoYuGWayQZfo8RLBWAKlvZJoW_-mi5mHnLKNZJrMGDdUd4ZQcZfuw8nQgCOBmml2htGmC56GRqdmJNg7Su4pW7raljbPlj7_E9N6ytYE1d168LX21UBcxJvCV-9XBH7MDwjThRBmFglEU-5M/s16000/6.png)

### Extensions

To perform brute-force for a particular type of file extension, the **-x** or **–extensions** flag can be used.

```
feroxbuster -u http://192.168.1.4 -x php,txt --silent
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9CL4RJ3NU9slFoNyzOiaQy-I1Tvrj9AB1faXpyk39MXnSms_XTWKr6fptKpi56h3qj8FHFd9wfh0cRNjrtde46z2xjkK0zP9oCJlBhl55Ww9QBzqaDhy11sXuW2UrZWCPn6oM0C4sl1xjAm4lxx3Fb3wNZx4WixWEvvD9rubBEmeLesffl-kcgqMce9u8/s16000/7.png)

### Result output

If we want to log the output, we use the **–output** flag and then mentioning the file name.

```
feroxbuster -u http://192.168.1.4 --output results.txt
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSpooB2JCzeP25nunaVg-dKaJSe1iFogq8JnpyyWHzo1l0FNx7tuZZNswy0DnyC8e1kLpGDGZ2v4G3TcdoVae20bQHsiZgmL8G83mmXuj1finEut_Z3FHYdAwHfX0qSKJPmSUWgHIZNpCDSpshpyWdUWNmbMXVT1_rZOBlFqmZgq0LNOKtJPLYAgkHcutl/s16000/8.png)

### User agent

To set up a custom user agent to send request at the server, we can use the **-a** or **–user-agent** flag. By default, the user agent used by Feroxbuster is **feroxbuster/<version>**.

```
feroxbuster -u http://192.168.1.4 -a "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHCmkz7hAvR8G4gNwsBHhuKEe-qxxwbuSeHc-cxDcaORezWaq6bqAS1BCEzagzDmBLXghTVXYUzVeCAEaqbV43rkKIvnRC7CrUwNGJi4RF3a9xggmyxHRu8YTn3BNGCNdWBQy7Pp42MMCJGZ_3CRvGXmCUPj-B16ANFKdYinhY_Jm2nGZEafTufORqPnAk/s16000/9.png)

### Filter status code

There are times when we need to skip certain status codes responses, so we can use the **-C** or **–filter-status**, to skip the results of the mentioned codes. If we want to include a particular status code in output, we can use the **-s** or **–status-codes** flag.

```
feroxbuster -u http://192.168.1.4 -C 403,404
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/A...