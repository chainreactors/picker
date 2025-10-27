---
title: How to Set Up Proxifier for Penetration Testing
url: https://redsiege.com/blog/2025/09/how-to-set-up-proxifier-for-penetration-testing/
source: Blog – Red Siege Information Security
date: 2025-09-09
fetch_date: 2025-10-02T19:50:34.110761
---

# How to Set Up Proxifier for Penetration Testing

Register Now For On-Demand Training!

[Learn More](https://training.redsiege.com)

[![](https://redsiege.com/wp-content/uploads/2022/01/redsiege-logo-300x73.png)](https://redsiege.com)

* [About us](https://redsiege.com/about-us/)
* [Blog](https://redsiege.com/red-siege-blog/)
* [Tools](https://redsiege.com/tools/)
* [Training](/training)
* [The Wednesday Offensive](https://redsiege.com/event/wednesdayoffensive/)
* [Contact](https://redsiege.com/contact/)

* [About us](https://redsiege.com/about-us/)
* [Blog](https://redsiege.com/red-siege-blog/)
* [Tools](https://redsiege.com/tools/)
* [Training](/training)
* [The Wednesday Offensive](https://redsiege.com/event/wednesdayoffensive/)
* [Contact](https://redsiege.com/contact/)

![](https://redsiege.com/wp-content/themes/red-siege-theme/img/icon-phone.svg) +1 234-249-1337

# How to Set Up Proxifier for Penetration Testing

By Red Siege | September 8, 2025

![](https://redsiege.com/wp-content/uploads/2025/08/SET-UP-PROXIFIER-1.jpg)

**by Justin Palk**

ProxyChains is a great tool for running Linux-based tools, such as those in Impacket, and everything built on top of them, but sometimes there’s a .NET tool you need to execute, that you can’t run in your beacon for some reason.

Enter Proxifier.

Proxifier is a Windows tool for proxying network traffic from the host it’s running on through a proxy and into another network. It’s got a free trial license, but you really ought to buy a copy if you’re using it regularly.

A quick primer on proxies:

Putting it simply, a proxy is an application that accepts network traffic and redirects it to another destination.The three most common types you’ll encounter are HTTP, SOCKS4 and SOCKS5.

* HTTP(S) proxies relay primarily web traffic between clients and servers.
* SOCKS4 proxies can relay TCP traffic, but not UDP, and have no authentication or encryption
* SOCKS5 proxies can relay TCP and UDP, and support authentication, but are not encrypted

Proxies have their own protocols, or, in the case of HTTP proxies, specific HTTP methods, that let them know where they are supposed to send traffic. Some tools are built to be proxy-aware, that is, they have functionality built-in that can speak the relevant proxy protocol and connect directly to a proxy specified by command-line options. Others aren’t proxy-aware, so something else needs to handle the proxy communications for them, which is where Proxifier comes in.

As opposed to ProxyChains, which runs on a per-application-execution basis, Proxifier runs continuously, watching for network connections being made by programs the user has selected, and routing them through the desired proxy. With its rule-based configuration, you can direct traffic into different proxies based on the executable name, or targeted host or network. The image below shows Proxifier’s main window.

![](https://redsiege.com/wp-content/uploads/2025/08/proxifier1-300x163.png)

Proxifier Main Window

The first thing to configure is DNS, which is accessible under the Profile->Name Resolution menu. As shown in the image below, you should configure Proxifier to resolve hostnames through the proxy, and to not proxy network requests destined for your own machine.

![](https://redsiege.com/wp-content/uploads/2025/08/proxifier2-300x229.png)

Configuring Proxifier Name Resolution

The next thing to configure is forwarding of services and processes belonging to other users. Windows executables sometimes work through other processes, such as `svchost.exe`, meaning we need to be sure those processes are proxied as well. This option can be accessed under Profile->Advanced->Services and Other Users.

![](https://redsiege.com/wp-content/uploads/2025/08/proxifier3-300x252.png)

Configuring Proxifier to Proxy Connections for Windows Services and Other Users

With this out of the way, it’s time to configure a proxy. Click the Proxy->Proxy Servers menu, and you’ll get a popup listing any currently configured proxies, and giving you the option to add, edit and delete proxies. Here, you can specify the proxy address, port, and type (Proxifier supports HTTP, SOCKSv4 and SOCKSv5 proxies). For purposes of this exercise, I just SSH’d to one of my lab’s Windows workstations with `-D 9000` to create a SOCKSv5 proxy on port `9000/tcp`. To access it via Proxifier, set the IP address, port and proxy type, as shown below.

![](https://redsiege.com/wp-content/uploads/2025/08/proxifier4-300x146.png)

Configuring a Proxy in Proxifier

In the Proxy Servers window, there is also the option to check a proxy, which Proxifier will do by attempting to connect to http://www.google.com:80 over the proxy. It’s up to you whether you want to do this, depending on how quiet you’re attempting to be, but it is a useful troubleshooting mechanism.

![](https://redsiege.com/wp-content/uploads/2025/08/proxifier5-300x238.png)

Testing a Proxy Connection

After configuring the proxy, it’s time to configure proxy rules. These rules allow you to control how traffic gets directed into which proxy (if any), based on a combination of the executable and the domain, port, and network or host the traffic is destined for. Below I’ve configured a rule that will direct any traffic being generated by `Rubeus.exe` and destined for either the `rslabs.lan` domain or `10.1.0.*` network, through the SOCKS proxy on `127.0.0.1:9000`. Note: If you’re trying to proxy PowerShell using Proxifier, be sure to make PowerShell.exe the application to proxy, not the script you’re trying to execute. Also, do not just proxy everything through Proxifier, as this will result in all of your Windows machine’s telemetry, updates, etc. getting sent through the target network, which is, to say the least, not stealthy.

![](https://redsiege.com/wp-content/uploads/2025/08/proxifier6-300x290.png)

Creating a Proxy Rule in Proxifier

If you’re planning on running a tool that can be executed unauthenticated, this is all you need. If, however, you’re going to be running a tool that needs authentication and doesn’t take a username and password on the command line, there’s a couple more steps. First, you need to need to create a shell that is associated with the domain user in domain you’re targeting. In this case, I’m going to target the obrienmuser in my test domain, `rslabs.lan`, as shown below.

![](https://redsiege.com/wp-content/uploads/2025/08/proxifier7-300x85.png)

Launching a Windows Shell as RSLABS\obrienm

Next, in that shell, I need to add a Kerberos ticket to the session. This can be a ticket requested using Rubeus, or Impacket’s `getTGT.py`. Below I show using Rubeus’s `asktgt` command with the `/ptt` flag to request a ticket and then import it into the current session.

![](https://redsiege.com/wp-content/uploads/2025/08/proxifier8-300x176.png)

Requesting a Kerberos Ticket and Importing it into the Current Session

Now, I can run SharpView using the Kerberos ticket in my session, but as shown below, I run into a different problem – the domain can’t be located.

![](https://redsiege.com/wp-content/uploads/2025/08/proxifier9-300x61.png)

SharpView Cannot Find Rslabs.lan Domain

The problem is that, although there’s a proxy in place and we’ve told the shell to act as a domain user, the local host isn’t domain joined, so if it tries to look up the `rslabs.lan` domain, it won’t find it. (Earlier, we configured Proxifier to resolve hostnames through the proxy, but it won’t resolve domains that way). So, I need to add the `-DomainController` flag, with the DC’s IP, so SharpView knows which server to connect to. I find I often need to do this when using .NET tools through a proxy, whereas running the tool in a beacon on a domain-joined host using something like BOF.NET or inline-executeassembly, I typically don’t. Re-running SharpView, this time specifying the DC’s IP address, I can now pull domain information from the `rslabs.lan` DC, as shown below.

![](https://redsiege.com/wp-content/uploads/2025/08/proxifier10-300x173.png)

Execut...