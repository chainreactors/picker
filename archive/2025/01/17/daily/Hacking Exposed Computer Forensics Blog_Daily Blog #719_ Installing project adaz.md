---
title: Daily Blog #719: Installing project adaz
url: https://www.hecfblog.com/2025/01/daily-blog-719-installing-project-adaz.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-01-17
fetch_date: 2025-10-06T20:24:13.109560
---

# Daily Blog #719: Installing project adaz

[![Hacking Exposed Computer Forensics Blog](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)](https://www.hecfblog.com/)

* [Extended Mapi](https://www.hecfblog.com/search/label/extended%20mapi)
* [ObjectID](https://www.hecfblog.com/search/label/objectid)
* [Amcache](https://www.hecfblog.com/search/label/amcache)
* [CTF](https://www.hecfblog.com/search/label/ctf)
* [Python](https://www.hecfblog.com/search/label/python)
* [Syscache](https://www.hecfblog.com/search/label/syscache)
* [Daily Blogs](https://www.hecfblog.com/search/label/Daily%20Blog?max-results=6)
  + [Saturday Reading](https://www.hecfblog.com/search/label/Saturday%20reading)
  + [Solution Saturday](https://www.hecfblog.com/search/label/solution%20saturday)
  + [Forensic Lunch](https://www.hecfblog.com/search/label/forensic%20lunch?&max-results=8)
  + [Sunday Funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)

[Home](https://www.hecfblog.com/)

[project adaz](https://www.hecfblog.com/search/label/project%20adaz)

Daily Blog #719: Installing project adaz

# Daily Blog #719: Installing project adaz

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
January 15, 2025
•

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[project adaz](https://www.hecfblog.com/search/label/project%20adaz?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqSly9cb1HYqzY_k_78Z_NpchuuWr3JY45ITM1f6RBuSVqDwnNMUCLQtfIX9kk6Ymbnbf8LsGtwHe4diXmU_MJyL6_A14ROeA_DCJlIT_-YS2sEiLub6uOrqYs9v42FnizuoHJ86NZ57HPicZF9tTEJ9YevCOALreJw8gGRA_1Wt6h9CjMR3k5tRnLN-g/w640-h640/adaz.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqSly9cb1HYqzY_k_78Z_NpchuuWr3JY45ITM1f6RBuSVqDwnNMUCLQtfIX9kk6Ymbnbf8LsGtwHe4diXmU_MJyL6_A14ROeA_DCJlIT_-YS2sEiLub6uOrqYs9v42FnizuoHJ86NZ57HPicZF9tTEJ9YevCOALreJw8gGRA_1Wt6h9CjMR3k5tRnLN-g/s1024/adaz.webp)

**Hello Reader,**

Following up on our last post, I’m now testing the installation process for **Project Adaz** to see if it’s still functional. While the project is marked as "maintained," confirming it’s installable on a Windows 11 system is a different matter entirely.

Below are my updated installation instructions to ensure a smoother setup:

---

### **Updated Installation Instructions for Project Adaz**

1. **Clone the Repository**
   Assuming you already have Git installed, create a directory for the project, then run the following command:

   ```
   git clone https://github.com/christophetd/Adaz.git
   ```
2. **Set Up the Python Environment**
   Navigate to the newly created `adaz` directory and execute the following commands:

   ```
   python3 -m venv ansible/venv
   ./ansible/venv/bin/activate
   pip install -r ./ansible/requirements.txt
   deactivate
   ```
3. **Prepare Terraform**
   Download Terraform and extract it to the `terraform` directory within the `adaz` project folder.
4. **Initialize Terraform**
   Run the following commands:

   ```
   cd terraform
   terraform init
   ```
5. **Set Up Azure CLI**
   Ensure the Azure CLI is installed and log in to your desired Azure account using:

   ```
   az login
   ```
6. **Generate an SSH Key (if needed)**
   If you don’t already have an SSH key, generate one and store it in the `.ssh` directory. On Windows 11, run the following command in the terminal:

   ```
   ssh-keygen
   ```

   Make sure to name the key **id\_rsa** and avoid accepting the default name.
7. **Apply Terraform Configuration**
   Navigate to the `terraform` directory and execute:

   ```
   terraform apply
   ```

---

Once these steps are complete, Terraform will build an **Active Directory-enabled network** with an **ELK log forwarder** to support your project needs.

Tomorrow we can see if it was succesful.

Also Read:

[Project Adaz testing part 2](https://www.hecfblog.com/2025/01/daily-blog-724-project-adaz-testing.html)

[Project adaz testing part 3](https://www.hecfblog.com/2025/01/daily-blog-725-project-adaz-testing.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/01/daily-blog-720-spotlight-on-zeltser.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/01/daily-blog-718-building-test.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/6395700796230449786/comments/default)

## Top Posts/Right Now

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4Zw9KQkjNkc2JCwa0rDb1zPUCypCWZgocTE2voitZGOwzeZ2L_4D63LJ0j9JPosWO-nLahPLJYL-tsQMEgmfVhxmjpJ6Smn6FKVk2_JhClTq_WWhvcE13R76fsdeVWnJb-lPNFnJnif0HpOq-5yuADLWqHUQjQG4zpbLb46P0PM-dvHaM9rsb-D39qs/s72-c/sundayfunday.png)](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)

  [Daily Blog #814: Sunday Funday 4/20/25](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5GWh0tXGteqxfrTQFDzW2kMooGHcwNkA6h9f_bfBDpsRMJtvg0UR1SHfIqx4UYxViUSiLEJFeWq9SryUdFz5gwlrOlXEFCZDoNnqRlbU3pn_lGfYxr60W3HgTAXc7b3IqLHYN3F0kW72JbkCoEID0IEVH-rls7Q1LRd_0awNugK97uT7EDxugHyuXvFM/s72-c/forgive.png)](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)

  [Daily Blog #815: I missed a day](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi60iLy5WiSNWWSyeIoM9JsOK9Xwv5L7GT5g4NxBmdQwyQNbbHzgWoiG4FbwefVVrqg1yDaz0ripRAlyXSWNX4xJ3tACOcH7a0_YyoPVT2XMPnI2-0aE3gKc9hJWhMWYqDWlTUDM2XM3DEHiJB5Z1iSrtjQeP0qG5xKxmt4RewUfbqA0FR7cw1DXPwxYNM/s72-c/solutionsaturday.png)](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)

  [Daily Blog #813: Solution Saturday 4/19/25](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhK3OAgdGTujkTy5X-nM4364yuWc8TJa-ct4GGE-Phw3vdXX9DApDT_kRhIvjELWVYLvnTPIrJTGFuz2hhkhVoklmY6bixe4fypY1X1A8RuJgAoPUUK597HYTBKVrOgLMn11x2g6b0azfhNnVv7CE6p-ZZRcfmAnaIIB-RNEBL_rIakVyr80MUyDhMQGgI/s72-c/removefromgroup.png)](https://www.hecfblog.com/2025/04/daily-blog-812-testing-aws-log-latency.html)

  [Daily Blog #812: Testing AWS Log latency - Removing Users from Groups](https://www.hecfblog.com/2025/04/daily-blog-812-testing-aws-log-latency.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitgwVMjukTzCuo_bdlGs6epwr95Xl8x8_1MJt_djP4ZVpHlyf15v6pNOYVIhyphenhyphenEO0Tplcb2BMczNRo7gwcMaWeS0T64eGqUHQuini6o_dnTYA9dLg8oWfo4tJQD8i2ba_PZh3jQG6k_fgY_n86V6LkpQq2FQx4RO44Mvptg6TjE3V7-fs21BSiYgNXb2xk/s72-c/addusertogrou%5Bp.png)](https://www.hecfblog.com/2025/04/daily-blog-811-testing-aws-log-latency.html)

  [Daily Blog #811: Testing AWS Log latency - Modifying User Permissions](https://www.hecfblog.com/2025/04/daily-blog-811-testing-aws-log-latency.html)

Powered by [Blogger](https://www.blogger.com).

## About

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)

A Blog on computer and digital forensic research, DFIR programming, the forensic lunch and more wirrten by Hacking Exposed Computer Forensic author David Cowen

## Follow us

## Popular Posts

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4Zw9KQkjNkc2JCwa0rDb1zPUCypCWZgocTE2voitZGOwzeZ2L_4D63LJ0j9JPosWO-nLahPLJYL-tsQMEgmfVhxmjpJ6Smn6FKVk2_JhClTq_WWhvcE13R76fsdeVWnJb-lPNFnJnif0HpOq-5yuADLWqHUQjQG4zpbLb46P0PM-dvHaM9rsb-D39qs/s72-c/sundayfunday.png)](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)

  [Daily Blog #814: Sunday Funday 4/20/25](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)
* [...