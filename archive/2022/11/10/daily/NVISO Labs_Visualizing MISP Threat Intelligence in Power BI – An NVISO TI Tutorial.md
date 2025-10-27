---
title: Visualizing MISP Threat Intelligence in Power BI – An NVISO TI Tutorial
url: https://blog.nviso.eu/2022/11/09/visualizing-misp-threat-intelligence-in-power-bi-an-nviso-ti-tutorial/
source: NVISO Labs
date: 2022-11-10
fetch_date: 2025-10-03T22:13:41.133499
---

# Visualizing MISP Threat Intelligence in Power BI – An NVISO TI Tutorial

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Visualizing MISP Threat Intelligence in Power BI – An NVISO TI Tutorial

[NVISO Blog](https://blog.nviso.eu/author/nviso-blog/ "Posts by NVISO Blog")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [Tools](https://blog.nviso.eu/category/tools/), [Data Visualisation](https://blog.nviso.eu/category/data-visualisation/), [Threat data](https://blog.nviso.eu/category/threat-intelligence/threat-data/)

November 9, 2022March 12, 2024
24 Minutes

## Problem Statement

Picture this. You are standing up your shiny new MISP instance to start to fulfill some of the primary intelligence requirements that you gathered via interviews with various stakeholders around the company. You get to some requirements that are looking for information to be captured in a visualization, preferably in an automated and constantly updating dashboard that the stakeholder can look into at their leisure.

Well MISP was not really made for that. There is the MISP-Dashboard repo but that is not quite what we need. Since we want to share the information and combine it with other data sources and make custom visualizations we need something more flexible and linked to other services and applications the organization uses. Also it looks as if other stakeholders would like to compare and contrast their datasets with that of the TI program. Then you think, it would be nice to be able to display all the work that we put into populating the MISP instance and show value over time. How the heck are we going to solve all of these problems with one solution which doesn’t cost a fortune???

Links to review:

CTIS-2022 Conference talk – MISP to PowerBI: <https://youtu.be/0i7_gn1DfJU>
MISP-Dashboard powered by ZMQ: <https://github.com/MISP/misp-dashboard>

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
ufw default d...