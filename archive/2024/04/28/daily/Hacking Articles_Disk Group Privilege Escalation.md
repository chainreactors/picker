---
title: Disk Group Privilege Escalation
url: https://www.hackingarticles.in/disk-group-privilege-escalation/
source: Hacking Articles
date: 2024-04-28
fetch_date: 2025-10-04T12:14:29.918223
---

# Disk Group Privilege Escalation

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
»* [Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/)
»* [Disk Group Privilege Escalation](https://www.hackingarticles.in/disk-group-privilege-escalation/)
»

[Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/)

# Disk Group Privilege Escalation

[April 27, 2024June 19, 2025](https://www.hackingarticles.in/disk-group-privilege-escalation/) by [Raj](https://www.hackingarticles.in/author/raj/)

**Disk Group Privilege Escalation** is a complex attack method that targets **vulnerabilities** or **misconfigurations** within the **disk group management system** of **Linux environments**. Specifically, attackers often focus on disk devices such as **/dev/sda**, which represents the **primary hard drive** in **Linux systems** and typically corresponds to the first **SCSI (Small Computer System Interface)** disk device. During **Disk Group Privilege Escalation** attacks, they exploit vulnerabilities or misconfigurations linked to **/dev/sda** and similar devices to gain **unauthorized access** to **sensitive data** or further exploit related weaknesses. Moreover, by **manipulating permissions** or exploiting **misconfigurations** concerning disk devices, attackers aim to **escalate their privileges** or access **critical system resources**.

### Table of Contents

* **Lab Setup**
* **Configuration**
* **Exploitation**
* **Conclusion**

### Lab Setup

In this article, we are going to exploit the disk group privilege escalation vulnerability on the ubuntu machine and obtain the root access. Following are the machines:

Target Machine: Ubuntu (192.168.1.6)

Attacker Machine: Kali Linux (192.168.1.7)

### Configuration

Let’s start by creating a new user **raj** in the ubuntu machine.

```
adduser raj
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSdjF8PbDnPdVp9Hu1AQCEDoiRsGsuLzrObADtJQ7B6XGTHHCTB5TwCSww0L9BcNsIDeHmOi1lIO2T6aSWvPSpIXwYunyl6XTZ9GfxO4LraAGNSxIPwXoID-h4iq9b5XAbj3r0i9AfV-PG-WHDDITdMZp_4Bn3ni98GORohd07PUcAcck-8sQwtwc5A8-P/s16000/1.png)

Add the newly created **raj** user to the **disk** group using the following command:

```
usermod -aG disk raj
groups raj
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEt8YlJWzHDTvE7fvjXah7gr-owXLvRDyYNs0sntbiTtZqyCT7qSlR-xa7uq8XlTclpHpJKDC6YPJrTOGc2OyorBroW895JWStzekIKoklav5mZr0f9PhYt0ZakdHRE_FOV-22rzQP0OYYFJHVJSDRuiERDV65rw0F_FeyXNDZ2dUKekoyuzESb5ee8NG5/s16000/2.png)

Install the **openssh-server** using the following command:

```
apt install openssh-server
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLi04ybytFK8_Ubd4vEPuEETO5OAywBmwo0l7LhOC0cuhsqd6h3ALGpR8qENb1XFvvs8_uR2sH0LnSX9NMHG1yjfvVCA2EgddYB7TMLYvEyKDoHmlJ-_mU0UzG0bwqYr8LrIr7wnPLbFLFqHYS9CXha7NCvh4Vsp_k1yfb4MWGCqG2Se-6fLMdqk1rZZVL/s16000/3.png)

Generate the **ssh** **private key** and **public key** for the root user using the following command:

```
ssh-keygen
mv id_rsa.pub authorized_keys
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgL_9JC0Msp65NRmoZRoUof_Jx9muUmWIS5J5TiZvcNuL2yTP8Cd7Wl1PfCuo836Di3HVOfvWfcAOODqpuyPdvR1MVzLsg6XnOQbGcgNOt_dWTkkB-u2O-rViQsdcX7KoDPHbmg58hjyT61lppXWuSqmPRqnF6rwvMhD5bUbm5u6MIHkVEfHQH08OWifELJ/s16000/4.png)

By default, inside the **sshd server system-wide configuration file** options for **PermitRootLogin** and **PubkeyAuthentication** is commented out.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFkUD7baVSxft-KztSTx5f9XUOfCq3kSainZ9lCbYCjZWBuoxMMFXLsX9ffObVAzPSofKIOEMEnVx8dwhGMgbTNP55gayAgliSb6TKzZlCsV9kEswoH_fmphVsu2hUNfJaWjaAUBFg8T1snyWgdYj2OvDwDwzfeIDbrcJzkMq7sTfyHutAi4IpFz7QBLa_/s16000/5.png)

Here, we need to perform two changes in the configuration file, the first one is changing the value of **PermitRootLogin** to **yes** and removing the comment (#) and second is removing the comment (#) on the **PubKeyAuthentication.**

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjt-kjt7kNhNvjou3OKcIjHUxWgJdOWfZgichZPSvEYFSnHv6JGBwUira86k-LeoANIO9yBWs80lTKK-RKA8WEO_RCkO1Bi0IRNmaAgBColKbsFSCDvR9J2jjnN29Md4kq_d8wfNY64daFq0xLTRGzmpQsNZvEEVgUhMdijbD_K1fVB1OwVc6uOrhXSVx90/s16000/6.png)

Now, after the configuration is complete restart the **ssh** service.

```
service ssh restart
service ssh status
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNwf7yrNGt1wr8ywipCs7Gelee2_wydjMnBvpzxUFuCygYgbKYGHrn7L4OCgl6y1pW7SVX9SgVaAvZsR8XYmLQmPqe8EEsqC2Z4zlqPy6GgkbRcFpng_QzJR7kUyYrslDOMPCbt5lLy3ou6zntInjQGLSC4m3e1F4JVX4557gKgc7v9_0Th-9LQOAEKK6d/s16000/7.png)

### Exploitation

Since the disk group misconfiguration vulnerability is a privilege escalation technique in linux, so we are taking an initial shell using the **ssh** service and as **raj** user to show the privilege escalation part using this vulnerability.

```
ssh raj@192.168.1.6
```

We can use the **id** command to verify the **groups** that **raj** user belongs to. It can be seen that **raj** is a member of **disk** group.

To check the **disk space summary** for each mounted file in **human-readable** format we will use the following command:

```
df -h
```

Here we are going to consider the partition where the **/** (root) directory is mounted i.e., **/dev/sda3**.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8eqLE_lXQwRZJcCGAWIrBMBH8h2P-_nSQEWqRhyUpSB62L-hQyS1v9UZ7aZCXjU4hMqLiL9KBH3g3dRvs8cgdjtphL9ZSvcg-njouuye45meJyvpPkfi073eVlPDpLFXV2KBzW05slvO49d7OGqO8A4Gk5jW2wNWN-I6zRn_RUty_06vMc8ugQYV7G8gX/s16000/8.png)

After selecting the partition, we can now examine and modify it using the **debugfs utility** in **Linux**. Additionally, this utility allows us to **create a directory** or **read the contents** of an existing directory.

After creating a test directory using **debugfs** utility, it shows that the filesystem has **read/only** permissions. So, we can try here reading the ssh **private key** of root user so that we can login later using ...