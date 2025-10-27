---
title: Intro to Debugging Java Web Servers Without Source Code For Security Researchers
url: https://infosecwriteups.com/intro-to-debugging-java-web-servers-without-source-code-for-security-researchers-80ff00de4753?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-31
fetch_date: 2025-10-06T17:42:08.263508
---

# Intro to Debugging Java Web Servers Without Source Code For Security Researchers

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F80ff00de4753&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fintro-to-debugging-java-web-servers-without-source-code-for-security-researchers-80ff00de4753&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fintro-to-debugging-java-web-servers-without-source-code-for-security-researchers-80ff00de4753&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-80ff00de4753---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-80ff00de4753---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Intro to Debugging Java Web Servers Without Source Code For Security Researchers

[![Jayateertha Guruprasad](https://miro.medium.com/v2/resize:fill:64:64/1*bmKMCGbQfIUNeymH5M7Pow.jpeg)](https://jayateerthag.medium.com/?source=post_page---byline--80ff00de4753---------------------------------------)

[Jayateertha Guruprasad](https://jayateerthag.medium.com/?source=post_page---byline--80ff00de4753---------------------------------------)

4 min read

·

Jul 16, 2024

--

Listen

Share

Debugging Java web servers in an on-premise environment is crucial for pentesting and source code reviews. It’s possible to easily decompile java based apps using tools like JD-GUI.

Often during dynamic analysis, we feel that, there’s a need to debug the application at runtime as if we had the source code, by placing breakpoints.
***Assuming that we do not have the source code, How do we debug Java based On-Premise Webservers ?***

> “🚀 JD-Eclipse to the Rescue! 🛠️”

## **Steps to Debug On-Premise Java Web Servers Without Source Code —**

First ,Download and Install “**Eclipse IDE for Enterprise Java and Web Developers**”.

Then, Download and Install **JD-Eclipse** Plugin from [here](https://github.com/java-decompiler/jd-eclipse) into your Eclipse IDE.

**Configure Eclipse IDE to associate \*.class files without source code to JD Class File Viewer** as follows. This can be done from “**Window > Preferences > General > Editors > File Associations**”.

Press enter or click to view image in full size

![]()

Associate \*.class files to use JD Class File Viewer

**Restart the Eclipse IDE** to finish the JD-Eclipse installation setup successfully.

**Install any Java-based web server for pentesting. In this example, we’ll use** [***ManageEngine Endpoint Central***](https://www.manageengine.com/products/desktop-central/)**.**

**Create any Java Project** in Eclipse IDE, For example, in our case I created a Java project with name EC.

Now open the created java project in Eclipse IDE, **create any valid java file inside project source**. It doesn’t matter what the code does.

Press enter or click to view image in full size

![]()

Creating valid java file in project src

Right click on your project folder in Eclipse IDE, Go to “**Properties” -> “Java Build Path” -> “Libraries” -> “Classpath” -> “Add External JARs**” to **Add jar files/libraries associated with the On-Premise software**.

Press enter or click to view image in full size

![]()

Adding Libraries & JARs to debug into the Project Build Path

Press enter or click to view image in full size

![]()

Example of Endpoint Central Libraries & JARs

### **Enabling remote debugging on java web server —**

This step is dependent on the installed Web server & might require some research & changes depending on your web server,

**You need to configure remote debugging in the webserver by enabling JPDA (Java Platform Debugger Architecture).**

For this, you need to find how the server is started & configure [JPDA](https://stackoverflow.com/a/36420167) before starting the server.

For, **Endpoint Central Server,** By viewing the service properties of “**ManageEngine UEMS — Server**”, We find that, The service is started using command “**D:\BB\Zoho\UEMS\_CentralServer\bin\wrapper.exe -s D:\BB\Zoho\UEMS\_CentralServer\conf\wrapper.conf**”.

Press enter or click to view image in full size

![]()

Searching for “**JPDA**” word in **wrapper.conf**, shows we need to uncomment few lines to enable JPDA.

Press enter or click to view image in full size

![]()

Enable JPDA in Web Server

**After configuring the server for JPDA, make sure all changes are saved & restart the server.**

### **Configure Eclipse IDE for Remote Debugging —**

Go to “**Run**” -> “**Debug Configurations**” -> “**Remote Java Application**” -> Right Click & select “**New Configuration**” & **Configure connection properties like Name, JPDA Host & Port** to use for debugging.

From **wrapper.conf** we find that \*:8787 is used for debugging, Hence we can configure Host as localhost, Port as 8787 in Eclipse as follows.

Press enter or click to view image in full size

![]()

Enabling Remote Debugging in Eclipse IDE

Name can be configured any, for ex: **EC Debug**.

**Apply and Close the Debug Configurations window** for now after configuring the above parameters.

### **Setting Breakpoint for Debugging —**

Now, as we have configured everything, we should be able to debug. But we need to set a initial breakpoint first to track code flow.

As this is Java based server, It should most probably have web.xml file where servlet & filters are configured. This can give a idea of where we can set initial breakpoint.

Searching for web.xml files in Web server directory, We find that web.xml file exists at “**D:\BB\Zoho\UEMS\_CentralServer\webapps\DesktopCentral\WEB-INF\web.xml**”

Searching for “**/\***” pattern in web.xml file, We find that all urls pass through **SecurityFilter** as follows**.**

Press enter or click to view image in full size

![]()

**SecurityFilter** class path is com.adventnet.iam.security.SecurityFilter.

Thus, Search for **com.adventnet.iam.security.SecurityFilter** class in Eclipse IDE & add a breakpoint inside **doFilter()** method.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

### Debugging the Java Server —

Go to “**Debug Configurations**” -> Select your previously saved configuration under “**Remote Java Application**”, Click on “**Debug**”.

Press enter or click to view image in full size

![]()

**Open any url associated with Endpoint Central server in a browser, say “**[**http://localhost:8020/client#/login**](http://localhost:8020/client#/login)**”.**

**Now we can debug the Java Web Server successfully in runtime, giving us the overview of variable values & expressions useful for dynamic analysis purpose.**

Press en...