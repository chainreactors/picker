---
title: Cloud Integration – How to setup a SFTP connection from CPI to portable Cloud Connector with openSSH Server on Windows
url: https://blogs.sap.com/2023/02/15/cloud-integration-how-to-setup-a-sftp-connection-from-cpi-to-portable-cloud-connector-with-openssh-server-on-windows/
source: SAP Blogs
date: 2023-02-16
fetch_date: 2025-10-04T06:45:43.955657
---

# Cloud Integration – How to setup a SFTP connection from CPI to portable Cloud Connector with openSSH Server on Windows

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Cloud Integration - How to setup a SFTP connection...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163333&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cloud Integration - How to setup a SFTP connection from CPI to portable Cloud Connector with openSSH Server on Windows](/t5/technology-blog-posts-by-members/cloud-integration-how-to-setup-a-sftp-connection-from-cpi-to-portable-cloud/ba-p/13568946)

![RobertQ](https://avatars.profile.sap.com/4/0/id403ff67f0c95beecefe426d1fc8bec2c2c8650a47f14267dfcef9a0340d2ffdb_small.jpeg "RobertQ")

[RobertQ](https://community.sap.com/t5/user/viewprofilepage/user-id/121246)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163333)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163333)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568946)

‎2023 Feb 15
10:54 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163333/tab/all-users "Click here to see who gave kudos to this post.")

10,660

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [Cloud Connector](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Connector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [Cloud Connector

  Additional Software Product](/t5/c-khhcw49343/Cloud%2BConnector/pd-p/0f95abc4-29f3-477d-874c-7c758b81f779)

View products (3)

# Requirement

Some time ago I had to build an Iflow to save E-Mails on an SFTP Server. In the development phase I had no access to a SFTP Server from the customer. I wanted to have a SFTP server for testing purpose on my work PC that I could reuse for several projects. I looked through the blogs section and found solution for a [Linux setup](https://blogs.sap.com/2021/04/21/configure-sftp-on-your-local-machine-and-connect-to-cpi/) or [Google Cloud Services](https://blogs.sap.com/2019/06/29/try-sftp-scenarios-in-cpi-with-your-own-sftp-server-using-google-cloud/), but nothing with my windows PC. So I decided to build one myself. I hope that you can reuse this solution if you need to test IFlows with a SFTP connection and do not have access to a dedicated SFTP server.

In this blog I will describe the setup of an openSSH server on a Windows 10 PC and the configuration of a portable cloud connector instance. Furthermore I will connnect a Subaccount to the SFTP server over the cloud connector and test the connectivity from a SAP Integration Suite instance.

# Setup openSSH server on local PC

To set up an SFTP server I followed the documentation on the microsoft help page to [Get started with OpenSSH for Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui).

### First I open a PowerShell as an administrator:

![](/legacyfs/online/storage/blog_attachments/2023/02/1_openPowerShell.png)

### Then I checked the prerequisites like described by microsoft:

```
winver.exe

$PSVersionTable.PSVersion

(New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
```

![](/legacyfs/online/storage/blog_attachments/2023/02/2_Check_Prereq.png)

### The next step is to check/ install the openSSH Server and configure a firewall rule to enable traffic on port 22:

```
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH.S*'

Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Start the sshd service

Start-Service sshd

# OPTIONAL but recommended:

Set-Service -Name sshd -StartupType 'Automatic'

# Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify

if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {

    Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."

    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22

} else {

    Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."

}
```

![](/legacyfs/online/storage/blog_attachments/2023/02/3_Install.png)

### Create a local user. You can use your own local user, but I prefere a specific user for my tests:

```
New-LocalUser -Name 'cpisftp' -Description "Cloud Integration SFTP user" -PasswordNeverExpires
```

![](/legacyfs/online/storage/blog_attachments/2023/02/4_user.png)

### Test the connection with the user localy:

![](/legacyfs/online/storage/blog_attachments/2023/02/5_logon.png)

With this, we have successfully installed and configured our local SFTP server.

# Setup a portable cloud connector instance

To setup the cloud connector instance I follow the descriptions from the [SAP documentation](https://help.sap.com/docs/CP_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/e6c7616abb5710148cfcf3e75d96d596.html?locale=en-US).

The Installation on Microsoft Windows OS describes the needed stepts.

### Download the portable variant as ZIP archive for Windows from the [SAP Development Tools for Eclipse](https://tools.hana.ondemand.com/#cloud) page:

If you want to use the SAP JVM istead of a Oracle JDK download it also from this page. I use an already installed Oracle JDK on my mashine. Extract the ZIP archive to a folder of your choise.

![](/legacyfs/online/storage/blog_attachments/2023/02/6_CC_Download.png)

### Start the Cloud Connector from a command line or PowerShell as administrator:

![](/legacyfs/online/storage/blog_attachments/2023/02/7_CC_start-1.png)

### Open a browser and navigate to the cloud connector instance:

The initial user credentials are Administrator/manage.

![](/legacyfs/online/storage/blog_attachments/2023/02/8_Browser.png)

After the first login you have to change the current password for the administartor account.

![](/legacyfs/online/storage/blog_attachments/2023/02/9_New-Password.png)

With this setup I created an initial cloud connector instance for my tests.

# Connect a SAP Integration Suite Subaccount to the local cloud connector instance

After the cloud connector setup and the password change the cloud connector needs to be connected to at least one subaccount as described in the [Initial Configuration](https://help.sap.com/docs/CP_CONNECTIVITY/cca91383641e40ffbe03bdc78f00f681/db9170a7d97610148537d5a84bf79ba2.html?locale=en-US). For this purpose I use a [Trial](https://cockpit.hanatrial.ondemand.com/trial/#/home/trial) account.

You can use any other subaccount for your purp...