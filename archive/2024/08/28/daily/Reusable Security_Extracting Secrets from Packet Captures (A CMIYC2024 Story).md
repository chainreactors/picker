---
title: Extracting Secrets from Packet Captures (A CMIYC2024 Story)
url: https://reusablesec.blogspot.com/2024/08/extracting-secrets-from-packet-captures.html
source: Reusable Security
date: 2024-08-28
fetch_date: 2025-10-06T18:04:02.042322
---

# Extracting Secrets from Packet Captures (A CMIYC2024 Story)

[Skip to main content](#main)

### Search This Blog

# [Reusable Security](https://reusablesec.blogspot.com/)

Password Cracking, Crypto, and General Security Research

### Extracting Secrets from Packet Captures (A CMIYC2024 Story)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

By

[Matt Weir](https://draft.blogger.com/profile/16111343330590419341 "author profile")

-
[August 26, 2024](https://reusablesec.blogspot.com/2024/08/extracting-secrets-from-packet-captures.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheivB25FHTWpmSuqqKo2sOyr2m5HblpHxlqm7fvuALSWZAZ8b5oZYdvDtZB4HKTBSJXRTbsHCsdolug5P7PtbDf9SSj5FmwX0PUvc93jVPSEz5ZK6990qobcne9p-lyNrriyVDfTeYLhD6DVoFRKzNUH4MCKQDpp1pqykU6NoaK7czkEMLsIWjn4KB5N4/s16000/analyzing_packet_captures.webp "Midjourney really doesn't like drawing the back of computer monitors")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheivB25FHTWpmSuqqKo2sOyr2m5HblpHxlqm7fvuALSWZAZ8b5oZYdvDtZB4HKTBSJXRTbsHCsdolug5P7PtbDf9SSj5FmwX0PUvc93jVPSEz5ZK6990qobcne9p-lyNrriyVDfTeYLhD6DVoFRKzNUH4MCKQDpp1pqykU6NoaK7czkEMLsIWjn4KB5N4/s1456/analyzing_packet_captures.webp)

> ***"******Interest is the most important thing in life; happiness is temporary, but interest is continuous.****"*

> **- Georgia O'Keeffe**

# Introduction:

The focus of this blog entry will be on tools and scripts to analyze packet captures. This is the result of falling down a rabbit hole when writing the previous tutorial on the CMIYC 2024 WIFI cracking challenge: [[Link](https://reusablesec.blogspot.com/2024/08/cmiyc2024-wifi-cracking-challenge.html)]. In that writeup I realized I hadn't been keeping up on the state of automated tooling to help extract secrets and interesting data from packet captures. So I asked for tips and suggestions on what I could use. And you all responded! This is another reason why these blog posts are really beneficial to me. I learn so much writing them, so thank you!

As a disclaimer, while I will be using the CMIYC2024 dataset to explore using some of these tools, these tools are not really suited for password cracking competitions. For short competitions, you are better off performing manual analysis of the data. As a spoiler, none of the tools I looked at identified many of the CMIYC2024 secrets out of the box. I needed to look through the packet captures myself to figure out those clues. Instead as you read through this blog entry, I'd like you to consider analyzing real world data which can take up Gigabytes of disk space. That's where these tools can be helpful.

## Important Links, Tools, and References for this Post:

# * **Previous Blog Entry: CMIYC2024 WIFI Cracking Challenge** + Link: <https://reusablesec.blogspot.com/2024/08/cmiyc2024-wifi-cracking-challenge.html> + Reason: I'm not going to cover cracking WIFI passwords or decrypting encrypted traffic in Wireshark in this post since I already covered those topic in this previous entry. So consider that entry a prerequisite (or at least an earlier chapter) to this blog post. * PCredz + Code Link: <https://github.com/lgandx/PCredz> + Documentation LInk: <https://shellcode33.github.io/CredSLayer/index.html> + Reason: A popular tool to sniff network traffic and capture plaintext credentials as well as other interesting secrets such as credit card numbers * CredSLayer + LInk: <https://github.com/ShellCode33/CredSLayer> + Reason: An enhancement on PCredz with a focus on making it easier to add support for extracting secrets from new protocols. * DSniff + Link: <https://github.com/tecknicaltom/dsniff> + Reason: A very popular tool to sniff network traffic and extract plaintext credentials.

# Manual Analysis:

To start things off, I wanted to create a control set of myself manually analyzing a packet capture file. That way I knew what to expect when I start trying to process the same data with automated tools. For this blog post I'm going to use CMIYC2024 contest's packet capture challenge since it includes different types of secrets, and quite honestly this provides a good incentive to spend more time trying to solve the other CMIYC2024 challenges as well.

To reiterate from my previous post on how I manually analyzed the data, I opened up the packet capture in Wireshark, decrypted the WPA1 encrypted traffic, and then manually walked through the different TCP streams using the Wireshark filters.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvrssalLHGWG5oxFiy3RsrsfazatSyXDPJRYduMAlCOjgwUHAeGFj10di96eWX8JVc7VW9owdfL4cFJn7KDtDWMoAbd-RBe3xSPhdCyBWqEJKY3q9cRmUKGkxDerql1u_4WyTMGNF4S2xseCwOhogrBrivNPERpjAFDt2n0SqXpY7557Jmjy2xOANcaNA/s16000/wireshark_filter.png "It's nice sometimes to reuse the same screenshots")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvrssalLHGWG5oxFiy3RsrsfazatSyXDPJRYduMAlCOjgwUHAeGFj10di96eWX8JVc7VW9owdfL4cFJn7KDtDWMoAbd-RBe3xSPhdCyBWqEJKY3q9cRmUKGkxDerql1u_4WyTMGNF4S2xseCwOhogrBrivNPERpjAFDt2n0SqXpY7557Jmjy2xOANcaNA/s1357/wireshark_filter.png)

**Note:** There was UDP traffic as well, (which you can walk through in a similar fashion). Looking through the UDP traffic there wasn't anything that I saw that was interesting to this contest. It was mostly "plumbing" traffic like DHCP address leases. When doing this yourself though, make sure you don't forget to look at UDP traffic since there can often be some really interesting findings in it.

As far as content went, there were four main types of sessions that Korelogic included in the contest:

* **FTP Sessions (Covered in the previous blog post)**

+ **Interesting Secrets:**

- Username/password to log into the FTP server
- Each session downloaded a passwords file containing the same three passwords.

+ **Number of Sessions:**

- 10 FTP protocol (Packet capture missed one of the FTP protocol sessions)
- 11 FTP Data

* **HTTP Sessions (Covered in the previous blog post)**

+ **Interesting Secrets:**

- HTTP Basic Auth: Username/password
- Each session displayed a "password vault" which was just a plain HTML page containing the same four passwords

+ **Number of Sessions:**

- 4

* **Telnet**

+ **Interesting Secrets:**

- Username/password to log into the telnet server

+ **Number of Sessions:**

- 8

* **Email**

+ **Interesting Secrets:**

- This was a password reset e-mail for the **\*WORST\*** password reset service. So it included the original username/password combo and the new username/password combo as text inside the e-mail.

+ **Number of Sessions:**

- 7

I talked about most of these session types in the previous blog post, but I wanted to highlight the password reset e-mails that Korelogic created for this contest:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEga8uYZfmKrUPowj-_IY0lECAYnBkJ91hwi1gWDhHeAws2Zq7b94elbmrtrgvWy03WSTay58Gf6OITO6qbfSeg6cYi-Dr9XeQsnuZZc5Q9Lla5Diunqz1xHaon1xEzHHM40MevGGU9bR1VcxYOGC066-5YxbGU6I2eHgRezrdO0rbn2Qtp-Pc7NsQudkzA/s16000/email_pcap.png "Please don't implement a password reset service like this")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEga8uYZfmKrUPowj-_IY0lECAYnBkJ91hwi1gWDhHeAws2Zq7b94elbmrtrgvWy03WSTay58Gf6OITO6qbfSeg6cYi-Dr9XeQsnuZZc5Q9Lla5Diunqz1xHaon1xEzHHM40MevGGU9bR1VcxYOGC066-5YxbGU6I2eHgRezrdO0rbn2Qtp-Pc7NsQudkzA/s1259/email_pcap.png)

Getting a user's previous password as well as what the password reset service reset it to will probably be helpful for cracking other passwords during this competition! You may also notice that the new password matches the HTTP Basic Auth password highlighted in the previous blog post. So Korelogic is working to try and tell a consistent story here.

To actually save the data, I copy/pasted interesting fields from Wireshark into an Excel Workbook.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAUoyJhKI1xiE0Yz9d09qW5JlMmUzgzz9-j0Dw1F7hQpuTx6oJ9jC-XldnKQSroLAo3z2jTUEz5U60WWhLx7kdF-V2yr8y0nZhfFoIwThDyk-DEo6AywoXOUKj5Oewu5FwXDNrMofR6evDdz1IbOp0F8OPL_VQxrkCc2TuKMFVFyNWDZj00_sV3ilsi...