---
title: How to bring data from local “node_exporter” to Prometheus, and then to the Grafana Cloud
url: https://blogs.sap.com/2023/04/16/how-to-bring-data-from-local-node_exporter-to-prometheus-and-then-to-the-grafana-cloud/
source: SAP Blogs
date: 2023-04-17
fetch_date: 2025-10-04T11:31:58.362948
---

# How to bring data from local “node_exporter” to Prometheus, and then to the Grafana Cloud

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [DevOps and System Administration](/t5/devops-and-system-administration/gh-p/devops-sysadmin)
* [Blog Posts](/t5/devops-and-system-administration-blog-posts/bg-p/devops-sysadminblog-board)
* How to bring data from local "node\_exporter" to Pr...

DevOps and System Administration Blog Posts

Explore DevOps and system administration blog posts. Stay current with best practices, tools, and insights into efficient IT management strategies.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/devops-sysadminblog-board/article-id/216&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to bring data from local "node\_exporter" to Prometheus, and then to the Grafana Cloud](/t5/devops-and-system-administration-blog-posts/how-to-bring-data-from-local-quot-node-exporter-quot-to-prometheus-and-then/ba-p/13548471)

![ChrisBaumann](https://avatars.profile.sap.com/9/4/id94b84703bbd112c5e2620dc4bf7821439af1d36a0004c5839dc44d73639db984_small.jpeg "ChrisBaumann")

[ChrisBaumann](https://community.sap.com/t5/user/viewprofilepage/user-id/8930)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=devops-sysadminblog-board&message.id=216)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/devops-sysadminblog-board/article-id/216)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548471)

‎2023 Apr 16
4:03 PM

0
Kudos

3,427

* SAP Managed Tags
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

View products (1)

## Introduction

In today’s data-driven world, collecting and analyzing data has become crucial for businesses to make informed decisions. Prometheus is a popular open-source monitoring and alerting toolkit that is widely used to monitor infrastructure and applications. It provides a powerful query language and visualization tools that enable users to collect, store, and analyze metrics.

One of the primary ways to collect metrics in Prometheus is through exporters. Exporters are small programs that run on the systems being monitored and collect metrics from the various services running on those systems. A commonly used exporters is “node\_exporter”.

However, collecting data is only half the battle. The data also needs to be stored and visualized in an accessible and easy-to-understand way. This is where Grafana comes in. Grafana Cloud is a cloud-based platform that provides a powerful and user-friendly interface for visualizing and analyzing data.

In this article, I will explore how to bring data from local installed “node\_exporter” to Prometheus Server, and visualise it on the Grafana Cloud. I will walk through the necessary steps to configure and set up Prometheus exporters, create a Prometheus data source in Grafana Cloud, and visualize the collected metrics using Grafana Cloud’s powerful dashboarding features. All this in a easy way with preconfigured Elements - so quite no work ...

## The Result

![](/legacyfs/online/storage/blog_attachments/2023/04/SIT.png)

## But first the "OnPrem" Work

### A - Download and Install "Note exporter" on the remote Host

1. Go to the Node Exporter GitHub page: <https://github.com/prometheus/node_exporter>

2. Navigate to the "Releases" tab.

3. Find the latest release and download the appropriate binary file for your operating system/architecture. For example, for Linux 64-bit, download "node\_exporter-<version>.linux-amd64.tar.gz".

4. Extract the downloaded archive file to a directory of your choice. This will create a directory named "node\_exporter-<version>.linux-amd64" (assuming you downloaded the Linux 64-bit version).

5. Open a terminal or command prompt and navigate to the directory where you extracted Node Exporter.

6. Start Node Exporter by running the following command: ./node\_exporter

![](/legacyfs/online/storage/blog_attachments/2023/04/node_exporter-1.png)

7. By default, Node Exporter will listen on port 9100. To verify that Node Exporter is running and accessible, navigate to <http://<node_exporter_IP_address>:9100/metrics> in your web browser. If you see a page containing metrics data, then Node Exporter is working correctly.

8. Create a Start/Stop Script - Start it

![](/legacyfs/online/storage/blog_attachments/2023/04/start_node_exporter.png)

## B - Download and Install local Prometheus Server

1. Go to the Prometheus website (<https://prometheus.io/>) and navigate to the "Downloads" section.

2. Download the latest version of Prometheus for your operating system.

3. Extract the downloaded archive file to a directory of your choice.

4. Open the "prometheus.yml" file located in the extracted directory. This file is used to configure Prometheus to scrape metrics from various targets.

5. Add target configurations to the "prometheus.yml" file. For example, to scrape metrics from the local node\_exporter, add the following target configuration:

![](/legacyfs/online/storage/blog_attachments/2023/04/job_name-2.png)

6. Save the "prometheus.yml" file.

7. Open a terminal or command prompt and navigate to the directory where you extracted Prometheus.

8. Start Prometheus by running the following command: ./prometheus

9. Prometheus should now be running and scraping metrics from the specified targets. You can view the collected metrics by navigating to <http://localhost:9090> in your web browser.

10. Create a Start/Stop Script - Start it

## And second the "Cloud" Work

### C - Sign up for a free Grafana Cloud Account

1. Go to the Grafana Cloud website: <https://grafana.com/products/cloud/>

2. Click on the "Get started for free" button.

3. Fill out the sign-up form with your information, including your name, email address, and a password. You can also sign up using your Google or GitHub account if you prefer.

4. Choose the plan that best suits your needs. Grafana Cloud offers a free plan that includes up to 10,000 series and 50 GB of logs per month, as well as paid plans with additional features and higher usage limits.

5. Enter your payment information if you choose a paid plan. You will not be charged for the free plan.

6. Review and agree to the terms of service and privacy policy.

7. Click on the "Create account" button.

8. Check your email for a verification message from Grafana Cloud. Click on the verification link in the email to activate your account.

### D - Download preconfigured Dashboard

![](/legacyfs/online/storage/blog_attachments/2023/04/Download_JSON.png)

1. Go to the Node Exporter dashboard page on Grafana's website: <https://grafana.com/grafana/dashboards/1860>

2. Click on the "Download JSON" button. (also possible direct import over "Copy ID")

3. Once the download is complete, open your Grafana instance in your web browser.

4. Click on the "Create" button in the left sidebar, then select "Dashboard".

5. Click on the "Import" button in the top toolbar.

6. Drag and drop the downloaded JSON file into the "Import via panel JSON" box, or click on "Upload .json file" and select the downloaded file.

7. Choose the data source you want to use for the dashboard (e.g., Prometheus), then click on "Import".

![](/legacyfs/online/storage/...