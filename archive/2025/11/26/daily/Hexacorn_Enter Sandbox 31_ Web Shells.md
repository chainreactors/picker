---
title: Enter Sandbox 31: Web Shells
url: https://www.hexacorn.com/blog/2025/11/26/enter-sandbox-31-web-shells/
source: Hexacorn
date: 2025-11-26
fetch_date: 2025-11-27T03:11:13.427734
---

# Enter Sandbox 31: Web Shells

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2025/11/16/some-unusual-run-time-rundll32-exe-artifacts/)

# Enter Sandbox 31: Web Shells

Posted on [2025-11-26](https://www.hexacorn.com/blog/2025/11/26/enter-sandbox-31-web-shells/ "12:46 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Webshells are malicious scripts/programs that are uploaded to compromised web servers. Most webshells are written in JSP, ASP, PHP and they are interpreted by a dedicated script processor/interpreter executed by the web server (f.ex. Apache, IIS, Tomcat). The results of that processing are rendered into a content that is sent back to the client – typically a web browser, but more advanced offensive tools may choose a different communication protocol.

Once a webshell is installed, it allows the attacker to use the compromised web server for various purposes. The attacker can use it to steal web server data and code, attack other systems, act as a proxy, host phishing content/landing zones, give hacktivists an ability to deface a web site, impersonate web server owner, and do many other things…

The reason I talk about them in this series is because sandboxes don’t handle webshells well. And yes, analysing webshells is actually not an easy task, in general…

First the good news. There are still many cases today where very well-known webshells are being used by attackers, attackers who are not making any effort to change the code of these classic web shells.

Then the worse news: it is becoming more and more common nowadays that many of the web shells are obfuscated, code-protected (various wrappers and extensions), password-protected, many rely on POST instead of GET requests (which means that the parameters included in POST requests are usually not logged by the web server), and some more advanced webshell payloads can be very well hidden inside the legitimate server-side code (making them harder to spot). As you can imagine, manual webshell analysis of these more complicated cases is very time-consuming and non-trivial. This is because in most these cases there it now the authentication bit that we need to take care of… In other words, when you access a more modern webshell today, you often need to provide a password, token, secret to access that particular webshell’s GUI. So, if it is not included in an outer code layer of a webshell, we need to either find it via opportunistic hash cracking, leak, or, if lucky, borrow it from other researchers who were luckier and somehow got a hold of it… Anyone having an experience manually analysing webshells like this knows that it is a very time consuming game, and one that doesn’t necessary guarantee the positive outcome…

Luckily, not all cases are like this.

Many of the old-school webshells will still load and execute their code with no problem, they don’t include any guardrails, and are often instantly rendering a user-friendly interface, presenting its features to a curious analyst in their full glory.

Additionally, a lot of webshell functionality existing today is often… accidental. Many web developers don’t have any cybersecurity experience, they don’t validate the input, they don’t sanitize the output and happily include code in their creations that takes whatever the input user-controlled parameters provide, and push it directly to some very dangerous shell functions that can be easily fooled into running some unexpected code…

And this is why sandboxes should be used to analyse web-server code; same as they analyze traditional executables.

We can argue that at the very basic level, sandbox webshell (or, more precisely: web server code) analysis should:

* provide at least a screenshot of how the suspicious script is being rendered by a browser,
* allow the analyst to inspect the code, ideally, [unwrapped](https://www.hexacorn.com/blog/2023/06/03/analyzing-nested-obfuscated-php-files/),
* highlight references to GET and POST variables, and
* perhaps support interactive analysis by letting the analyst play around with the sample during the session, and allow them to send hand-crafted GET or POST requests (if lucky, manual code analysis can help to discover required credentials that will grant access to the web shell’s GUI).

So, with that… let’s look at some very practical aspects of web server code analysis from a sandbox designer’s perspective. Depending on the file type, we need to create an environment within the test system that is able to execute/interpret scripts on a server-side (web server running locally), and then present the results of script execution on a client side (browser), and then combine them to present the final results to the sandbox user.

**Analysis of JSP scripts**

* Download and install the latest [Java Development Kit](https://www.oracle.com/java/technologies/downloads/).
* Download and install the latest [Apache Tomcat installer](https://tomcat.apache.org/).
* Now you can access Tomcat Web Server on http://localhost:8080/.
* You can drop a JSP sample in c:\Program Files\Apache Software Foundation\Tomcat <version>\webapps\test\<file>.jsp, and access it via http://localhost:8080/test/<file>.jsp.

**Analysis of JSP and PHP scripts**

* Download and install the latest [Java Development Kit](https://www.oracle.com/java/technologies/downloads/).
* Download and install the latest [XAMPP](https://www.apachefriends.org/).
* Now you can access Apache Server on http://localhost/ and https://localhost/, and then Tomcat Web Server on http://localhost:8080/.

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/sandbox_xampp.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/sandbox_xampp.png)

* You can drop PHP sample into *c:\xampp\htdocs\test\<file>.php* and access it via *http://localhost/test/<file>.php* and *https://localhost/test/<file>.php*.

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/php.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/php.png)

* You can drop JSP sample into *c:\xampp\tomcat\webapps\test\<file>.jsp* and access it via *http://localhost:8080/test/<file>.jsp*.

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/jsp.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/jsp.png)

**Analysis of ASP scripts**

* Install Windows Server of your choice, f.ex. Windows Server 2025.
* Install IIS and ASP support following [this guide](https://techcommunity.microsoft.com/blog/iis-support-blog/how-to-enable-iis-and-key-features-on-windows-server-a-step-by-step-guide/4229883) or others.
* Now you can access IIS Web Server on http://localhost/.
* You can drop ASP sample into *c:\inetpub\wwwroot\test\<file>.asp* and access it via *http://localhost/test/<file>.asp*.

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/asp.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/asp.png)

Running possible web server scripts under Apache, Tomcat, IIS servers in an automatic fashion is cool, but we know it is just the first piece of puzzle.

If we are lucky, and the web server script code is not obfuscated, we can make an attempt to analyze its code, even if in a rudimentary way. The goal is to discover the following:

* is the code recognized by any yara rule?
* does the script expect GET, POST, or both requests ?
* how are these retrieved? (there are multiple ways to do it f.ex. $\_GET, $\_SERVER[‘QUERY\_STRING’] in PHP)
* what are the names of parameters passed to the script ?
* is the code obfuscated/wrapped/hidden/protected?
* can we analyze the script ...