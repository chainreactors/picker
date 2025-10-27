---
title: pWnOS 2 (SQL Injection)
url: https://blog.g0tmi1k.com/2012/09/pwnos-2-sql-injection/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:49.808215
---

# pWnOS 2 (SQL Injection)

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# pWnOS 2 (SQL Injection)

This is the second release in the "[pWnOS](https://blog.g0tmi1k.com/categories/pwnos/)" [vulnerable machine](https://blog.g0tmi1k.com/2011/03/vulnerable-by-design/) collection, however, it has a different creator from the previous one (which explains why it has a different "feel" to it). As before, it has purposely built in "issues" allowing the machine to become compromised. This method uses a SQL injection flaw (see [here](https://blog.g0tmi1k.com/2012/09/pwnos-2-php-web-application/) for exploiting the PHP web application). As always with "[boot2root](https://blog.g0tmi1k.com/categories/boot2root/)" machines, the end goal is to become the super user, "root".

![pwnOS Logo](/images/pwnos2.png "pwnOS2")

Table of Contents

* + [Links](#Links)
  + [Method](#Method)
  + [Tools](#Tools)
  + [Walkthrough](#Walkthrough)
  + [Commands](#Commands)
  + [Notes](#Notes)

## Links

Watch video on-line: [](http://download.g0tmi1k.com/videos_archive/pWnOS_2_%28SQL%29.mp4)

Download video: [http://download.g0tmi1k.com/videos\_archive/pWnOS\_2\_(SQL).mp4](http://download.g0tmi1k.com/videos_archive/pWnOS_2_%28SQL%29.mp4)

## Method

* Scanned the network to discover the target [Net Discover]
* Port scanned the target to determine the running services on the target [Unicorn Scan]
* Emulated the services by grabbing the banner/header of the running service(s) [NMap]
* Interacted with the web server, found a login form and entered a "default" injection statement(s), to identify a vulnerability [Firefox]
* Emulated the database which exposed information regarding the database itself, as well as the operating system [Burp proxy]
* Uploaded a PHP shell onto the target to gain remote command access into the system [Pentest Monkey PHP Shell & Burp proxy]
* Automated the same attack [SQLMap]
* Located hard coded plain text credentials, which had been re-used, allowing for complete system access

## Tools

* [pWnOS\_v2.0.7z](http://pwnos.com/) *(md5: 1eb0960c0ba29335230ada1df80cd22c)*
* A virtual machine *(Example: [VMware Player](http://www.filehippo.com/download_vmware_player/) or [Virtual Box](http://www.filehippo.com/download_virtualbox/))*
* [Net Discover](http://nixgeneration.com/~jaime/netdiscover/) - *(Can be found in [BackTrack 5](http://www.backtrack-linux.org/downloads/))*
* [Unicorn Scan](http://www.unicornscan.org/) - *(Can be found in BackTrack 5)*
* [NMap](http://nmap.org/) - *(Can be found in BackTrack 5)*
* [Firefox](http://www.mozilla.org/firefox/new/) - *(Can be found in BackTrack 5)*
* [Burp Proxy](http://www.portswigger.net/burp/proxy.html) - *(Can be found in BackTrack 5)*
* [cURL](http://curl.haxx.se/) - *(Can be found in BackTrack 5)*
* [php-reverse-shell](http://pentestmonkey.net/tools/web-shells/php-reverse-shell) - *(Can be found in BackTrack 5).*
* [Netcat](http://netcat.sourceforge.net/) - *(Can be found in BackTrack 5)*
* [Tamper Data](https://addons.mozilla.org/firefox/addon/tamper-data/) - *(Can be found in BackTrack 5)*
* [SQLMap](http://sqlmap.org/) - *(Can be found in BackTrack 5)*

## Walkthrough

By reading "pWnOS\_INFO-2\_0.txt" *(aka the readme file)*, the attacker discovers the IP range which the target is using, as well as the network configuration of the target *(it's using a static IP address of 10.10.10.100/24)*. The attacker confirms the given information, by sweeping the network range and detecting a single node on the specified IP address, by using "net discover".

After the attacker has changed their IP address to match the target's subnet, they then set out to discover what services the target has publicly exposed. "Unicorn Scan" quickly scans every TCP and UDP port belonging to the target, to reveal TCP 22 *(SSH)* & TCP 80 *(HTTP)* open. The attacker chooses to verify unicorn scan findings by repeating to scan every TCP port using "nmap". At the same time as scanning, they opt to use nmap's scripting engine to start emulating the services. This allows for the attacker to gather more information relating to the target. Nmap also confirms the same ports are open, plus the default ports are used for the default services *(for example SSH access on port 22 and a web server running on TCP 80)*. The SSH service is normally used to remotely execute commands, and, due to its nature, normally requires a form of authentication before the user can access the service, so the attacker focuses on the web server... for now!

The attacker interacts with the web server, by using "Firefox" to graphically render the web application on the target. Upon viewing the page, the attacker is presented with a form to fill in, to gain access to use the web application. On the right hand side, is a very small navigation menu to "home" *(which asks the attacker to login)*, "register" *(allowing them to gain access)* and to "login" *(same as "home" link)*. In the login prompt, the attacker fills in the first field *(the email address)*, with a single quote "'" and the password as "123". The justification for this is when web applications normally interact with backend databases; the command used to query the database consists of single quotes, around the variable(s). By adding an additional single quote, the attacker is able to see if the input fields have been sanitized *(escaping and filtering values)*, which would protect the query command from being altered. The result of adding an extra single quote has led to the query command being left "open" as it hasn't got a closing/matching quote, that means the database can't be queried which causes an error. Because of the way the web application has been created and the web server is configured, the end user is displayed as an error message *(and by the looks of it a very detailed 'debug' message which is used for developing applications)*. Inside the error message, it displays the failed query command which was sent to the database, this makes crafting an input value, to manipulate the database how the attacker chooses, very easy.

As the attacker is going to be sending multiple requests to the target, in order to emulate the database, they use "burp proxy" to help construct the attack. The attacker starts burp to behave as a proxy, capturing all the data which will be sent through it, without modifying any requests. Afterwards the attacker then changes firefox's network settings to use burp as the proxy, meaning all the traffic, sent and received, in firefox will be monitored by burp.

In order to perform an error based SQL injection attack, due to the hardcoded commands before the injection point, the attacker needs to emulate the table structure to use "[union](http://www.w3schools.com/sql/sql_union.asp)" to 'select'/view values to alter the perform query. The first thing the attacker needs to know is the amount of columns used in the table into which they are injecting.

The attacker goes back to the input form and enters in the email field an SQL command which is used to specify a column in the database, "[ORDERY BY](http://www.w3schools.com/php/php_mysql_order_by.asp)". Inside burp, the attacker sends the requested value to burp's "intruder" feature. The attacker selects the area in the requested field, which each time will be modified. By using the "number" payload, each request will have a different numeric value. The attacker chooses to start at 1, ending at 10 and increasing in value by 1 with each request. If the returned result isn't what the attacker was expecting, they can increase the range and repeat the request. The attacker looks at the data which was produced due to each request. They look to see which column was first requested that caused an SQL error due to a column not existing. For this web application, the value was "9", therefore there are "8" columns in the database.

The attacker tries to see if they are able to view the output value of their injected command. They now test ...