---
title: Tomcat Penetration Testing
url: https://www.hackingarticles.in/tomcat-penetration-testing/
source: Hacking Articles
date: 2024-04-24
fetch_date: 2025-10-04T12:14:29.788283
---

# Tomcat Penetration Testing

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
»* [Tomcat Penetration Testing](https://www.hackingarticles.in/tomcat-penetration-testing/)
»

[Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/)

# Tomcat Penetration Testing

[April 23, 2024June 19, 2025](https://www.hackingarticles.in/tomcat-penetration-testing/) by [Raj](https://www.hackingarticles.in/author/raj/)

**Tomcat Penetration Testing** is essential for identifying vulnerabilities in **Apache Tomcat**, a widely used web server and servlet container. Originally, the **Apache Software Foundation** developed **Tomcat** to serve as a demonstration platform for **Java Servlet** and **JavaServer Pages (JSP)** technologies, which power **Java web applications**. Over time, **Tomcat** expanded its capabilities to support additional **Java web technologies**.

Moreover, a notable feature of **Tomcat** is its support for deploying web applications using **WAR (Web Application Archive) files**. These files bundle together all the components of a web application, including code, pages, and files, making deployment simpler. As a result, **Tomcat** allows users to upload and run these **WAR files**, enabling them to host their applications on the internet.

In addition to **WAR files**, **Tomcat** also supports the deployment of **JSP pages**. **JSP** is a technology that enables developers to create dynamic web pages using **Java**. Therefore, **Tomcat** can execute these **JSP pages**, making it a versatile platform for hosting a wide range of **web applications**.

By default, **Tomcat** supports the use of **WAR files** and **JSP pages**. However, administrators can configure settings to ensure **security** and control over file uploads, thereby enhancing the overall safety of the server.

### **Table of Contents**

* **Lab Setup**
* **Installation**
* **Configuration**
* **Enumeration**
* **Exploitation using Metasploit Framework**
* **Exploiting Manually (Reverse shell)**
* **Exploiting Manually (Web shell)**
* **Conclusion**

### Lab Setup

In this article, we are going to setup the Tomcat server on the ubuntu machine and exploit the file upload vulnerability. Following are the machines:

**Target Machine:** Ubuntu (192.168.1.5)

**Attacker Machine:** Kali Linux (192.168.1.7)

### Installation

Apache Tomcat relies on Java, meaning you’ll need to have the Java JDK installed on your server. You can install it by running the command below:

```
apt install openjdk-11-jdk
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjzLh7iXIcn8F3tNFjRPeSxFUrSXbJ5irE9eEKLb7lN-CUHbCU9GBtPVrYA6SgUB6iXOkIdxUVnhr0wppmma7Yj_W-B52K2pJGoL89kV8qlddD4Q3MtT8O4_ZM81QolzBrZGEFCQyEaU00IsR3qanonwb2HnByFAm2A2Pfc0a07i16CykH-DbwEpr6T4uf/s16000/1.png)

Add a new user by the name **tomcat** using the following command:

```
useradd -m -U -d /opt/tomcat -s /bin/false tomcat
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiyzxF2UvCrydGpgVJiYqkG9oWOG1YhuButOcVzl1rXWZJYm4TN8aGRFcExcuTooZNXSrFBAFpN5Q6aj4YbRGcYEBTetZ5b6RimKST3i03IfWnk4LE7UwyPgJlrEn2tfOmLJG8k-eE-40X5e9HC79HKJnDY-0C1Iksl4OudidqGNite5JJbpLYxLynJL-1/s16000/2.png)

Next, download the Tomcat **tar.gz** file from the official website.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1cvbdzS-G35VYBCNKhyphenhyphenjy2c2SD5SXE5HF66ytkPuMG3wWt8mKLwFRDeR62K6dMJLuSiqicIB_KWASEk_tGgeM9pQ2uJjDB6IuXiURUXD8Tf99YcGlhoPJtjMO68mW1jGnOn93oR2E1H8oIL1vO8bsjr7O__GAZFqSOPzeGJ6yBOIZp2poV8eUM_afV4Bp/s16000/3.png)

Then, download the latest version from the website into the ubuntu machine and extract the downloaded files.

```
wget https://archive.apache.org/dist/tomcat/tomcat-10/v10.0.20/bin/apache-tomcat-10.0.20.tar.gz
tar -xvf apache-tomcat-10.1.20.tar.gz
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguQzXfqFp642sufplZqEMMM8TJfEV6i5q3F1fTLDUIzha_s_wZjhaAtgfs2ZzBQVonmkj50KHbf7Qhu6fUkTFtXgj2HUZ8x3J9mDAQ1TfrXafa-BVMOsBP6p0ie2108gW4P7n15wfVtx2xorglr1ck0c4w2g7l2gpEa-8gwsAPzlAIyPe0CVCYUdhtcoCV/s16000/4.png)

Move the extracted folder in the **/opt/tomcat** directory, give the ownership permissions to tomcat user and set the execution permission on binary files.

```
mv apache-tomcat-10.1.20/* /opt/tomcat
chown -R tomcat: /opt/tomcat
sh -c 'chmod +x /opt/tomcat/bin/*.sh '
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWFPQ6D1-1jIOrdeuQ0mIfJkdG_fv1OViFSeuCLxtDZTmQvnRKvmWUsMPpgLoptrG4PT4s5_SncYLemzNLSzYSgLh4OwIjGw9DC6p476ULN9sIH701L2IqxOIk__vSQLXIeyjCYSos2ykJvBBTEyuC3SPKx6B22BMffwgAfbo3k-W_7vVpGIvdwor8QDTI/s16000/5.png)

Create a **tomcat.service** file in the **/etc/systemd/system/** directory and add the following content in the file:

```
[Unit]
Description=Apache Tomcat
After=network.target

[Service]
Type=forking

User=tomcat
Group=tomcat

Environment=JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
Environment=CATALINA_PID=/opt/tomcat/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat
Environment="CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC"

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

ExecReload=/bin/kill $MAINPID
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAfrxQXq4R-KeIK02EWM-H67QQVjhwFwdlps34Hgv91E0gDF9he6Ba41clONUyJnA7XGlR21DGN60EMTPRhuOoOxJMMUIdir3vcOXL6PWLlW_GiRzsUj6tD4Jl-3jd7ceJTbyinLNrXG1HCgTGLMm4zsLCNSVxAttRy92RdzGM8Vlr03hfFIX_UvL16gwW/s16000/6.png)

Reload the systemd daemon to apply the changes using the following command:

```
systemctl daemon-reload
```

 Also, enable the tomcat service to start at system reboot.

```
systemctl enable --now tomcat
```

Checking the status of the tomcat server:

```
systemctl status tomcat
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2qOIUQpwzmpb2CsYbgC7QU3Qtavpo5UnB-I4tnhxdOIYnBRcoUspyzlST1...