---
title: Sandfly 2.6.0 – Elasticsearch Replication, Linux Docker Container Security Scanning, Hidden Process De-Cloaking and More
url: https://sandflysecurity.com/blog/sandfly-2-6-0-elasticsearch-replication-linux-container-security-scanning-hidden-process-de-cloaking-and-more
source: Sandfly Security Blog RSS Feed
date: 2025-05-27
fetch_date: 2025-10-06T22:28:29.766490
---

# Sandfly 2.6.0 – Elasticsearch Replication, Linux Docker Container Security Scanning, Hidden Process De-Cloaking and More

[Sandfly 5.5.4 - Chinese/Korean Rootkit Decloaking. Learn more](/blog/sandfly-5-5-4-north-korean-rootkit-decloaking)

[Partners](/about-us/partner)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Sandfly 2.6.0 – Elasticsearch Replication, Linux Docker Container Security Scanning, Hidden Process De-Cloaking and More

13 April 2020

Product Update

Sandfly 2.6.0 has been released and now has the ability to use external Elasticsearch databases. This new feature allows you to use Elasticsearch’s Kibana and other tools to analyze and display Sandfly data.

We also added Docker container scanning for file and directory Linux attacks. This is on top of our process level Docker container attacks we already searched for in prior versions.

Further, we added in new forensic engines to detect and de-cloak processes being actively hidden by Linux Loadable Kernel Module (LKM) stealth rootkits. Plus, new modules to hunt for other signs of compromise and intrusion such as incorrect permissions on critical files and strace artifacts.

Finally, we’ve improved internal caching so security sweeps are faster yet again, taking just seconds each time we investigate a host.

## External Elasticsearch Database

We now give users the ability to deploy Sandfly using an external Elasticsearch database. This means customers can now use their own Elasticsearch cluster they may already have, or use a [cloud-based Elasticsearch](https://cloud.elastic.co/) hosting service to hold Sandfly data.

Sandfly still uses an internal Elasticsearch database for customers with smaller deployments that do not want the trouble of maintaining their own cluster. This works well, but it means that customers wishing to use tools such as Kibana to view and search the data were not able to easily do so. Now, customers can host their own Elasticsearch database and use tools like Kibana as they see fit.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![External elasticsearch database](https://www.datocms-assets.com/56687/1635216293-sandfly-external-elasticsearch-database.png?auto=format&dpr=2&q=60&w=920 "External elasticsearch database")

During install, customers will have the chance to enter in the URL for the remote Elasticsearch database they wish to use. After that, all results will be available using standard Elasticsearch features including Kibana, machine learning modules, redundancy and so on.

## Elasticsearch Results Replication

We also added in a new feature where results from Sandfly can be replicated to a secondary Elasticsearch database. Customers can deploy Sandfly servers inside different network segments but have all results go to a central location for consolidated viewing and analysis.

Sandfly will only send results data to the replication database. Encrypted credentials, host, scheduling and related data are not sent to this database. This feature allows customers to have SOC personnel view results but they will have no ability to change system operations. Customers can however leverage Sandfly’s [REST API](https://docs.sandflysecurity.com/reference) to control scanning with security orchestration tools or custom scripts. Or, they can use the built-in user interface as normal.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Results elasticsearch database](https://www.datocms-assets.com/56687/1635216304-sandfly-results-elasticsearch-database.png?auto=format&dpr=2&q=60&w=920 "Results elasticsearch database")

During install you can setup an optional URL for results replication. Existing installations can simply add the replication database URL into their setup files and it will work immediately. Customers that wish to use this feature can contact us for details on how to set this up quickly.

## Elasticsearch Kibana Dashboards

With either external database option above, you can use Kibana to create dashboards and search the [extensive Linux system and forensic data](https://docs.sandflysecurity.com/docs/sandfly-forensic-keyword-list) Sandfly delivers to you agentlessly. Not only can you quickly find security events, but you can also generate tables around operating system versions, hardware, users, and anything else you can probably think about running on your Linux hosts.

We have sample Kibana dashboards available to customers. Here we’re using Sandfly to monitor Linux hosts locally, at Amazon AWS and Digital Ocean at the same time. We’re doing this on Linux kernels back to 2.x all the way to modern versions. Plus, we’re watching AMD and Arm based processors because Sandfly works across Intel, AMD, Arm and MIPS CPUs. Sandfly allows you to monitor all your Linux hosts with one platform and without needing to load agents everywhere.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly pulls over Linux operating system data easily.](https://www.datocms-assets.com/56687/1635216311-operating-system-1.png?auto=format&dpr=2&q=60&w=920 "Sandfly pulls over Linux operating system data easily.")

Here is another example where Sandfly gives you visibility to spot processes running with network connections on your hosts. Hot spots show the most common process and ports, while lighter colors show less used processes with open ports.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly’s Linux process graphs in Kibana quickly show you what is running.](https://www.datocms-assets.com/56687/1635216319-process-heat-maps-2.png?auto=format&dpr=2&q=60&w=920 "Sandfly’s Linux process graphs in Kibana quickly show you what is running.")

You can also obtain user login data without persistent agents on your hosts. Sandfly can easily pull over user login data and save it over time to tell you who is and is not logging into your systems. You can easily report failed logins across all your Linux hosts regardless of version, kernel patches, distribution, or even CPU type. You can also search across hosts for any usernames that did login and at what times. We pull user login data from all of your Linux systems agentlessly.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![User failed login reporting across Linux with Sandfly.](https://www.datocms-assets.com/56687/1635216328-user-failed-logins.png?auto=format&dpr=2&q=60&w=920 "User failed login reporting across Linux with Sandfly.")

Sandfly with Kibana’s tag cloud can quickly and easily show you suspicious processes. Below we’ve flagged processes running from /tmp or /dev/shm directories and also a couple processes running with suspicious extensions. You can customize your threat hunting and query [against hundreds of system and forensic artifact keywords](https://docs.sandflysecurity.com/docs/sandfly-forensic-keyword-list) we retrieve from your Linux hosts.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly spots suspicious processes on Linux with Kibana.](https://www.datocms-assets.com/56687/1635216335-sandfly-kibana-suspcious-processes-1.png?auto=format&dpr=2&q=60&w=920 "Sandfly spots suspicious processes on Linux with Kibana.")

There is so much more to show about how to leverage Sandfly’s agentless visibility into Linux with Kibana and other tools like Splunk. Stay tuned for more updates.

## Docker Container Scanning

Sandfly has been able to detect Linux process attacks inside Docker containers since version 1.x of the product. Today we are introducing container aware scanning for our extensive list of file and directory attack signatures as well.

Customers running Docker containers do not need to do anything to enable this feature. Sandfly is container aware and will see if containers are running on a host and automatically check them with our suite of signatures, completely agentlessly of course. This process is fast and has no risks to the running containers as we never write anything to the images or attach to the instances with invasive kernel ...