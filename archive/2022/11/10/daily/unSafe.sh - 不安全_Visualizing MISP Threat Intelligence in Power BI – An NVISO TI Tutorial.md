---
title: Visualizing MISP Threat Intelligence in Power BI – An NVISO TI Tutorial
url: https://buaq.net/go-134923.html
source: unSafe.sh - 不安全
date: 2022-11-10
fetch_date: 2025-10-03T22:12:52.457042
---

# Visualizing MISP Threat Intelligence in Power BI – An NVISO TI Tutorial

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/e19699210e8901a0b8c6976757fd1346.jpg)

Visualizing MISP Threat Intelligence in Power BI – An NVISO TI Tutorial

Problem StatementPicture this. You are standing up your shiny new MISP instance to start to
*2022-11-9 21:42:20
Author: [blog.nviso.eu(查看原文)](/jump-134923.htm)
阅读量:33
收藏*

---

## Problem Statement

Picture this. You are standing up your shiny new MISP instance to start to fulfill some of the primary intelligence requirements that you gathered via interviews with various stakeholders around the company. You get to some requirements that are looking for information to be captured in a visualization, preferably in an automated and constantly updating dashboard that the stakeholder can look into at their leisure.

Well MISP was not really made for that. There is the MISP-Dashboard repo but that is not quite what we need. Since we want to share the information and combine it with other data sources and make custom visualizations we need something more flexible and linked to other services and applications the organization uses. Also it looks as if other stakeholders would like to compare and contrast their datasets with that of the TI program. Then you think, it would be nice to be able to display all the work that we put into populating the MISP instance and show value over time. How the heck are we going to solve all of these problems with one solution which doesn’t cost a fortune???

Links to review:

CTIS-2022 Conference talk – MISP to PowerBI: <https://youtu.be/0i7_gn1DfJU>

## Proposed Solution

Enter this idea = “Making your data (and yourself/your team) look amazing with Power BI!”

In this blog we will explain how to use the functionality of Power BI to accomplish all of these requirements. Along the way you will probably come up with other ideas around data analytics that go beyond just the TI data in your MISP instance. Having all this data in a platform that allows you to slice and dice it without messing with the original source is truly game changing.

## What is MISP???

If you do not know what MISP is, I prepped this small section.

MISP is a Threat Intelligence Sharing Platform that is now community driven. You can read more about its history here: <https://www.misp-project.org/>

In a nutshell, MISP is a platform that allows you to capture, generate, and share threat intelligence in a structured way. It also helps control access to the data that the user and organization is supposed to be able to access. It uses MariaDB as its back-end database. MariaDB is a fork of MySQL. This makes it a prime candidate for using Power BI to analyze the data.

## What is Power BI???

Power BI is a set of products and services offered by Microsoft to enable users to centralize Business Intelligence (BI) data with all the tools to analyze and visualize it. Other applications and services that are similar to Power BI are Tableau, MicroStrategy, etc.

### Power BI Desktop

* Desktop application
* Complete data analysis solution
* Includes Power Query Editor (ETLs)
* Can upload data and reports to the Power BI service
* Can share reports and templates manually with other Power BI Desktop users
* Free (as in beer), runs on modern Windows systems

### Power BI Service

* Cloud solution
* Can link visuals in reports to dashboards (scheduled data syncs)
* Used for collaboration and sharing
* Limited data modelling capabilities
* Not Free (Pro license level included with Microsoft E5 license, per individual licenses available as well)

#### Links to Pricing

More information here: <https://docs.microsoft.com/en-gb/power-bi/fundamentals/power-bi-overview> and <https://powerbi.microsoft.com/en-au/pricing/>

## Making the MISP MariaDB accessible to Power BI Desktop

> MISP uses MariaDB which is a fork of MySQL. These terms are used interchangeably during this blog. You can use MariaDB or MySQL on the command line. I will use MySQL in this blog for conciseness.

### Adding a Power BI user to MariaDB

When creating your MISP instance, you create a root user for the MariaDB service. Log in with that user to create a new user that can read the MISP database.

```
mysql -u root -p
# List users
SELECT User, Host FROM mysql.user;
# Create new user
CREATE USER 'powerbi'@'%' IDENTIFIED BY '<insert_strong_password';
GRANT SELECT on *.* to 'powerbi'@'';
FLUSH PRIVILEGES;
# List users again to verify
SELECT User, Host FROM mysql.user;
# Close mysql terminal
exit
```

### Configuring MariaDB to Listen on External Interface

We need to make the database service accessible outside of the MISP instance. *By default it listens only on 127.0.0.1*

```
sudo netstat -tunlp
# You should see that mysqld is listening on 127.0.0.1:3306

# Running the command below is helpful if you do not know what locations are being read for configuration information by mysql
mysql --help | grep "Default options" -A 1

# Open the MariaDB config file below as it is the one that is being used by default in normal MISP installs.
sudo vim /etc/mysql/mariadb.conf.d/50-server.cnf

# I will not go into how to use vim as you can use the text editor of your choice. (There are strong feelings here....)
# Add the following lines in the [mysqld] section:

skip-networking=0
skip-bind-address

# Comment out the bind-address line with a #
#bind-address

# Should look like this when you are done: #bind-address            = 127.0.0.1
# Then save the file

# Restart the MariaDB service
sudo service mysql restart

# List all the listening services again to validate our changes.
sudo netstat -tunlp
# You should see the mysqld service now listening on 0.0.0.0:3306
```

### Optional: Setup Firewall Rules to Control Access (recommended)

To maintain security we can add host-based firewall rules to ensure only our selected IPs or network ranges are allowed to connect to this service. If you are in a local environment, behind a VPN, etc., then this step might not be necessary. Below is a quick command to enable UFW on Ubuntu and allow all the ports needed for MISP, MySQL, and for maintenance via SSH.

```
# Switch to root for simplicity
sudo su -

# Show current status
ufw status

# Set default rules
ufw default deny incoming
ufw default allow outgoing

# Add your trusted network range or specific IPs for the ports below. If there are additional services you need to allow connections to you can add them in the same manner. Example would be SNMP. Also if you are using an alternate port for SSH, make sure you update that below or you will be cut off from your server.
ufw allow from 10.0.0.0/8 to any port 22,80,443,3306 proto tcp

# Show new rules listed by number
ufw status numbered

# Start the firewall
ufw enable
```

> For more information on UFW, I suggest the Digital Ocean tutorials.
>
> You can find a good one here: <https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04>

### Testing Access from Remote System with MySQL Workbench

Having a tool to test and work with MySQL databases is crucial for testing in my opinion. I use the official “MySQL Workbench” that can be found at the link below:
<https://dev.mysql.com/downloads/workbench/>

You can follow the documentation here on how to use the tool and create a connection: <https://dev.mysql.com/doc/workbench/en/wb-mysql-connections-new.html>

> Newer versions of the Workbench try to enforce connections to databases over SSL/TLS for security reasons. By default, the database connection in use by MISP does not have encryption configured. It is also out of the scope of this article to set this up. To get around this, you can add useSSL=0 to th...