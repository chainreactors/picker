---
title: OSINT : User Privacy in Linux
url: https://www.hackingarticles.in/osint-user-privacy-in-linux/
source: Hacking Articles
date: 2024-09-25
fetch_date: 2025-10-06T18:20:05.489905
---

# OSINT : User Privacy in Linux

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
»* [OSINT](https://www.hackingarticles.in/category/osint/)
»* [OSINT: User Privacy in Linux](https://www.hackingarticles.in/osint-user-privacy-in-linux/)
»

[OSINT](https://www.hackingarticles.in/category/osint/)

# OSINT: User Privacy in Linux

[September 24, 2024June 19, 2025](https://www.hackingarticles.in/osint-user-privacy-in-linux/) by [Raj](https://www.hackingarticles.in/author/raj/)

Linux telemetry, which involves gathering and sending data from a Linux-based system to an external server or service, raises concerns about **Linux telemetry and privacy**. The purpose of this process is often to monitor system performance, provide diagnostics, enable analytics, or improve system functionality. The collected data may encompass system performance indicators, usage patterns, hardware specifications, error logs, and other relevant information. In this article, we are going to discuss why telemetry can be seen as a potential threat to privacy, even when used for legitimate purposes. We will also explore methods to make the system more secure than before.

### Table of Contents

* **Secure OS Installation**
* **Removing the packages**
* **Settings in ubuntu**
* **Disable diagnostics reporting**
* **Disable lock screen notifications**
* **Disable tracking of recent files**
* **Turning off the problem reporting**
* **Turning off the screen blank**
* **Disable automatic screen locking**
* **Permanently delete option**
* **Show hidden files**
* **BleachBit**
* **KeePassXC**
* **Virus Scanner**
* **Metadata removal**
* **Firefox profilemaker**
* **Flatpak**
* **LibreWolf**
* **VeraCrypt**
* **Tor Browser**
* **Proton VPN**
* **NextDNS**
* **Conclusion**

### Secure OS Installation

Ideally we should consider the **POP!\_OS** by **System76** for installation, it is based on Ubuntu but redesigned for privacy and security. However, here we are considering the **Ubuntu 22.04.4** version. We are considering this version of Ubuntu because the versions which begin with an **odd number** or end with the **0.10** are **interim** releases with a short support cycle and we will be needing a version which has the Long Term Support (**LTS**). Hence only versions which begin with an **even number** and end with **0.04** should be considered. We will discuss the steps to make it secure from the installation itself.

#### Steps:

1: Download the ubuntu-22.04.4-desktop-amd64.iso image from the following URL: <https://old-releases.ubuntu.com/releases/22.04/>

![OSINT Linux Telemetry and Privacy](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikZAD0cEPhHCQrHrLgy47uK1P7B86oFbMmFajlKH0cORnxzhS_uLzdmP9wMVii6uX434ES-Ex9W0atiFhkXkPewGM3teTpSOcYJto1M6m7n2xNgZ8-LNPt9Mi9ElBUK2M0kcgUwypL7C7AVdbYX8UqBTAHAJCxQ0aKFWb3a-lFyARYsRUJM5NHsOHIR0F0/s16000/1.png)

2: Create a new virtual machine in VMware workstation PRO.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbz8zA6EqQlBCcMTz6McdKh1Be6t44lQxhekL-0EA5-2t-XF8JZfzb9A8g82CmPO1-xzmPcBWCRHK6iAT86YPdapu79ZIgEyAkxF6XbOYJkmPsrl_uNUIl_2r2qex4zI8apJsY27L4vSwOhJBPQvWA1_mVcHBsKd7O4JRm7RQ2d5IXoeuvWCX2AD7tXx0R/s16000/2.png)

3: Select the path of the installer disc.

![OSINT Linux Telemetry and Privacy](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzK4T2PvLS5JPgDrsZmzgugD3hJnr3yJckLXE0n9QW8u8zf0F10HXXFmL0t4ERpPNz4NOk4RJYsPBpYBu01ovRgOz2L2nEA4xshpD4TcTfYXS7v6pN_vB2haMgh_WhWP6OtSyig06aOJ2lf1nIWP8ybOvm816PFGnmg9off6S0tuZ-j4IpNTJMVQOotmul/s16000/3.png)

4: Enter the Full name, User name, Password and Confirm.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjP2ZlXU-WSGIWYGssEIMpWvuEoD9EsVvqpYykUC9KaTISTHvdOKgU_m40yei2AmxtCAiANRuj66KOMOuKCpO20ZQgGADpBiWK-53ssxfiEfGjHjZeSDPfUuoX4sk-bMadGLZKxxsH0me5zo_4BZZKRIvwuiJgWKKR9uW78ZmPufe41_DwlM3lYDlr5Mga-/s16000/4.png)

5: Select the Normal installation and select both options in the Other options.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYF3z19-pVU7ga62l2sds1sP-at7LZx8rUVDDXn20ANPqpmEou-3GK3g4YsVrgMBGUT7Oh9tG8EAXj9IstBHb_SepxaOFrNttoDrcsPlKhHlQXyiq-728qd7zGlfquEP-Vep9Gygm9w-Tm8ojZPLe0Bd8cRG9JyZhFQIya-Et3VSxJMPTljloGizcSFDea/s16000/5.png)

6: Select Erase disk and install Ubuntu, click on Advanced features.

![OSINT Linux Telemetry and Privacy](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfGDYOiAigqBfM6Bn6CUnC2ZHwhasawowwg7tD83xFF5jw-RKA63XtH-a_u5MmrME7mc0XNiS5a7jJ3yOQ3UbfTGgfmUrkj1faHAcBCKsZhnYGRWkJdHTd7MlWki-SYGXlujTww1mwG17PbP8FYmxJPPt1X1_GXg9F96DJ4GXlppnMEivDXz2qRp1rlpX_/s16000/6.png)

7: Inside Advanced features, use the following options: Use LVM with the new Ubuntu installation and Encrypt the new Ubuntu installation for Security.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFukhdivQjmlYIHv0oej80a4r_nzrHx_jo6DRhtu2-frmdW1xgQu7LneP0kpeCj-7exjYw3KhyNuK2ExGIb1rc_cwAd0vLGrV5XjbrGtDDcyQDGk66f2VNgLTloSBawPPxfGgQ5nNqZGjU6QQGnmfYFtxUSuMTVvPswQs17d6vx5k45WRl1kBN7Q1s1YsG/s16000/7.png)

8: Enter the Security key and click on Install now.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNkKgiOWaWgv1T0P43XWZ_hmi9KDb4aTq18OkEVOa-Z8_qmW7PPTrZcnLS9QbEn1ZKeebW2qvmnblW_8w51QuqYMij1fewKOIp2UrTGoDNqA68B8C_a38CoCNOI64f0jPqUbkKPWreYpVepm-OegefsGBN3sVJW9Xud9FhfFK_3jvXQMemZKVrN1L-bkEu/s16000/8.png)

9: Select Continue for the Write the changes to disks? Option.

![OSINT Linux Telemetry and Privacy](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_VPwNvaaRhmd9Pw9UHN7wdUocOTUtUQ0TGYY-Rb96g3P_nLu73Fo_6GeDMOpYFY-ed1cJRs_aMsz7T0bnLHCaxgrWXi8tFZN7o061ILji_zVr9UvUI2lf7oi2gOuWUb-9KHgyFn1ZCPeArH6_LjX9ynIu801XKiKjhKBOTZfqmjes3o18pnyZ6CU32y_8/s16000/9.png)

10: Enter the details in the Who are you? Installation option.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiK5zRXa_2vv7SUz9jWc8rrs1ELAGAv5rc-N-odB1y38AS7gTPZdf49RjFEVjzmfPXTF4ma1xxD8lcr337JDp7C_G81Nga8felVRiWa2q93cs12Lm4oymInY7CtBhYKSyWRMAXiMUCcz-5NogFmyr0_HuqA17XTVdV93gdk5CwwwJkgzO5moGuTZ-VS18-C/s16000/10.png)

O...