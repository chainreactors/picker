---
title: SAP CPQ : How to Write Cleaner, Safer Code with SonarQube & Docker
url: https://blogs.sap.com/2023/04/08/sap-cpq-how-to-write-cleaner-safer-code-with-sonarqube-docker/
source: SAP Blogs
date: 2023-04-09
fetch_date: 2025-10-04T11:29:46.820468
---

# SAP CPQ : How to Write Cleaner, Safer Code with SonarQube & Docker

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)
* SAP CPQ : How to Write Cleaner, Safer Code with So...

Financial Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-sap/article-id/8123&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP CPQ : How to Write Cleaner, Safer Code with SonarQube & Docker](/t5/financial-management-blog-posts-by-sap/sap-cpq-how-to-write-cleaner-safer-code-with-sonarqube-amp-docker/ba-p/13571432)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-sap&message.id=8123)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-sap/article-id/8123)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571432)

‎2023 Apr 08
9:35 PM

[1
Kudo](/t5/kudos/messagepage/board-id/financial-management-blog-sap/message-id/8123/tab/all-users "Click here to see who gave kudos to this post.")

1,513

* SAP Managed Tags
* [SAP CPQ](https://community.sap.com/t5/c-khhcw49343/SAP%2520CPQ/pd-p/73555000100800001601)

* [SAP CPQ

  SAP Billing and Revenue Innovation Management](/t5/c-khhcw49343/SAP%2BCPQ/pd-p/73555000100800001601)

View products (1)

# Introduction

**SonarQube** is a tool that helps you catch bugs and vulnerabilities in your SAP CPQ application written on Ironpython scripting. Working together with **PY****Lint** and **Unit tests,** it provides a **great code quality scan**.

On this blog, I will show you how to set up SonarQube and run locally over a Ironpython scripts folder project. Then, we will improve SonarQube analysis by adding PYLint reports.

### Pre-requisite :

### <https://blogs.sap.com/2023/03/03/how-to-use-sap-cpq-script-plugin-step-by-step-instructions/>![](/legacyfs/online/storage/blog_attachments/2023/04/download-3.png)  What is SonarQube?

SonarQube is a popular continuous inspection tool for code quality and code security that aims to help development teams ship better software. It functions as an automatic code review tool with support for more than 30 programming languages.

SonarQube easily interfaces with CI pipelines and DevOps builds to make code inspection swift and efficient for engineers. It is also self-managed, satisfying the need for developers to ship quality and maintainable code at a fast pace.

## Installing SonarQube on Docker

Getting SonarQube on Docker simply involves grabbing the image from [Docker Hub](https://hub.docker.com/_/sonarqube). If you use a Linux machine, you’ll need to set the recommended base configurations using the commands provided by Docker under [“Docker Host Requirements”](https://hub.docker.com/_/sonarqube).![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-08_21-53-28.png)

Next, launch the Docker daemon in a separate terminal. On the terminal, run the below command to start a server:

```
docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest
```

You can access the SonarQube instance with the host IP address and the specified port (localhost:9000, in our example).  <http://localhost:9000/>![](/legacyfs/online/storage/blog_attachments/2023/04/0-8uQPpXvk__IB0CQI.png)

When the SonarQube portal homepage appears, go ahead and log in; use the default username and password (“admin”). Next, you’ll be asked to update your password:

Select the **"Manually"** option. (If you want setup SonarQube with GitHub or another platform then select that option)![](/legacyfs/online/storage/blog_attachments/2023/04/How-to-Setup-the-SonarQube-on-Local-Machine08.png)

Enter the **"display name"** and **"key"** and click **"Set Up"**.![](/legacyfs/online/storage/blog_attachments/2023/04/9-5.png)

Now select the **"Locally"** option. Because we are going to setup in our local machine.![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-08_22-03-44.png)

Enter the **token name** and click the **"Generate"** button. You will get the sonar token. ![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-08_22-04-51.png)

Save that token and Click **"Continue"** and **Choose your project language.**![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-08_22-05-31.png)

Download the **Scanner zip file** from the link and Extract it.

<https://docs.sonarqube.org/latest/analyzing-source-code/scanners/sonarscanner/>

Copy all folders and paste them somewhere and add the **"bin"** directory path under the **PATH environment variable**![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-08_21-47-06.png)

---

# Let's Run your code Analysis

Running a SonarQube analysis is now very simple. You just need to execute the following commands in **your project's root folder**. The command runs a sonar check for your **whole project**.

```
sonar-scanner.bat -D"sonar.projectKey=test-key" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.login=<sonar-token-here>"

// Here replace <sonar-token-here> above generated token
```

```
sonar-scanner.bat -D"sonar.projectKey=test-key" -D"sonar.sources=<file-or-folder-path-here>" -D"sonar.host.url=http://localhost:9000" -D"sonar.login=<sonar-token-here>"
```

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-08_22-12-20.png)

![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-08_22-13-52.png)

After the above command runs successfully, you can check the results on your SonarQube project page **<http://localhost:9000/>**

Sonar report will automatically infer the project name from your code. i.e., the final report will not have **test-key** as the project name but **your actual project name.**![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-08_22-22-54.png)

**Code Smell Issues**![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-08_22-23-25.png)

**SAP CPQ Script suggests from Code Smell to make some changes.**![](/legacyfs/online/storage/blog_attachments/2023/04/2023-04-08_22-20-25.png)

---

# Final Thoughts

SonarQube is a great tool for checking the quality of code and also supports more than 25 languages. I hope you have liked it and know about SonarQube and how to setup it in a local machine.

**Note**

*We can discuss about CI configuration on another time. The main goal here was to run and use SonarQube locally.*

Labels

* [Technology Updates](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap/label-name/technology%20updates)

* [analysis](/t5/tag/analysis/tg-p/board-id/financial-management-blog-sap)
* [clean scripts](/t5/tag/clean%20scripts/tg-p/board-id/financial-management-blog-sap)
* [codesmell](/t5/tag/codesmell/tg-p/board-id/financial-management-blog-sap)
* [sonarqube](/t5/tag/sonarqube/tg-p/board-id/financial-management-blog-sap)

You must be a re...