---
title: Easy Peasy TryHackMe Writeup | By Xploit Ayush
url: https://infosecwriteups.com/easy-peasy-on-tryhackme-1d9c0f84983b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-07
fetch_date: 2025-10-04T05:50:59.554265
---

# Easy Peasy TryHackMe Writeup | By Xploit Ayush

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1d9c0f84983b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Feasy-peasy-on-tryhackme-1d9c0f84983b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Feasy-peasy-on-tryhackme-1d9c0f84983b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1d9c0f84983b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1d9c0f84983b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Easy Peasy TryHackMe Writeup | By Xploit Ayush

[![Xploit Ayush ☠️](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*LyzepZKQhN6zlHk90QEb7g.gif)](https://xploitayush.medium.com/?source=post_page---byline--1d9c0f84983b---------------------------------------)

[Xploit Ayush ☠️](https://xploitayush.medium.com/?source=post_page---byline--1d9c0f84983b---------------------------------------)

6 min read

·

Jan 20, 2023

--

Listen

Share

Practice using tools such as Nmap and GoBuster to locate a hidden directory to get initial access to a vulnerable machine.

![]()

> Practice using tools such as Nmap and GoBuster to locate a hidden directory to get initial access to a vulnerable machine. Then escalate your privileges through a vulnerable cronjob.

This writeup contains all the steps necessary to root the easy box: [Easy Peasy](https://tryhackme.com/room/easypeasyctf) on [TryHackMe](https://tryhackme.com/).

First, Like always, we start by scanning the **ports** Along with services and their version on the machine by using **Nmap**, By using the following command.

```
nmap -sV -sC -A -T4 10.10.97.146
```

Press enter or click to view image in full size

![]()

But we found only 1 port is Open! What?

> Hint says there is 3 ports, there must be a higher ports available

So we'll try to scan all ports and their service version using this command:

```
Nmap -A 10.10.97.146 -Pn -T4 -p-
```

Nmap again to scan all ports on the machine, It takes time.

![]()

#1 How many ports are open?

> Answer: 3

**#2** What is the version of nginx?

> Answer: 1.16.1

**#3** What is running on the *highest port*?

> Answer: **Notice we have 3 ports open**:
>
> · 80: nginx 1.16.1
>
> · 6498: OpenSSH 7.6p1
>
> · 65524: Apache httpd 2.4.43

Press enter or click to view image in full size

![]()

The result shows us **3 open ports**. There are **2 web services running**. The web service on port **80** runs on a **Nginx web server** and the web service on **port 65524** runs on an **Apache web server**. Additionally, there is **1 SSH server running on port 6498.** Let’s start by checking the web server on port 80.

```
http://10.10.97.146/
```

Press enter or click to view image in full size

![]()

There is no information hidden in the source code as well. Let’s try `gobuster` to find hidden files and directories.

Use command :

```
gobuster dir -u http://10.10.97.146 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

Press enter or click to view image in full size

![]()

The outcome is shown below:

```
/hidden (Status: 301)
/index.html (Status: 200)
/robots.txt (Status: 200)
```

If **/hidden** we access the directory, you should get the following website

Press enter or click to view image in full size

![]()

There is nothing interesting, We can use `gobuster` again in order to find even more hidden directories or files within the `hidden` directory.

```
gobuster dir -u http://10.10.97.146/hidden -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

After the scan finishes ( you can run it for 15 mins, it’s more than enough too for this machine) you can see the following directories being discovered

**Hidden/whatever/**

Press enter or click to view image in full size

![]()

**Let us check what’s inside its source code, shall we?**

Press enter or click to view image in full size

![]()

**Nice! Our first flag with base64 encode. Let’s decode it with:**

![]()

You can try to enumerate anything inside /whatever , but nothing will show up, so **let’s go to the other service running on port 65524**

```
http://10.10.97.146:65524
```

Apache web server. The content of the page is:

Press enter or click to view image in full size

![]()

inspecting the source code we find the, we got our 1st flag!

Try to look Deeper for juicy information in **/robots.txt**

![]()

> Here we get a hash(which seems to me like a md5 hash), our first step will be to crack it, for this we are gonna use a website [MD5Hashing](https://md5hashing.net/), which yields us another flag.

![]()

we got our 2nd flag!

Try to investigate futher, look into source code did you find anything?

YES!

Press enter or click to view image in full size

![]()

The encoding turns out to be `base62` which gives, directory path..

Press enter or click to view image in full size

![]()

Using the file found in the hidden directory, find and *crack a password* hidden in the file:

Press enter or click to view image in full size

![]()

We notice there is a hash and a picture waiting for us to investigate

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

```
john --wordlists=easypeasy.txt hash.txt
```

Press enter or click to view image in full size

![]()

And we have successfully Cracked the password!

![]()

**Remember the image on the hidden directory? Let’s download it on our desktop to reveal what’s inside?**

Press enter or click to view image in full size

![]()

Use **steghide** to extract secrets out of this image and enter the password we just cracked.

```
steghide extract -sf binarycodepixabay.jpg
```

![]()

Used that password to extract the `secrettext.txt`. And in that we get another set of credentails. **And password seems to be encrypted!**

Press enter or click to view image in full size

![]()

> This seems like the credentials for the SSH server. We already got a username. The password seems to be binary encoded. You can decode it using [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space')). Now log into the server using the following command:

Press enter or click to view image in full size

![]()

```
ssh -p 6498 boring@10.10.97.146
```

Try to login using SSH credentials

> Don’t forget the flag -p 6498 because this machine’s ssh port is not 22, but 6498!

Press enter or click to view image in full size

![]()

BOOM!!! we CRACKED!!!

![]()

ls -la to see the user.txt w...