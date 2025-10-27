---
title: SSH key injection in Google Cloud Compute Engine [Google VRP]
url: https://buaq.net/go-170230.html
source: unSafe.sh - 不安全
date: 2023-06-26
fetch_date: 2025-10-04T11:44:58.841114
---

# SSH key injection in Google Cloud Compute Engine [Google VRP]

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

![](https://8aqnet.cdn.bcebos.com/c1f0622e7cc149ce275c77da7d52fc6f.jpg)

SSH key injection in Google Cloud Compute Engine [Google VRP]

This write-up is the first in a series of write-ups about bugs that I, and Sreeram, found in Go
*2023-6-25 19:8:20
Author: [govuln.com(查看原文)](/jump-170230.htm)
阅读量:31
收藏*

---

This write-up is the first in a series of write-ups about bugs that I, and [Sreeram](https://twitter.com/kl_sree), found in Google Cloud during 2022.

After hunting for bugs continuously in common Google apps such as Drive, we wanted to venture into Google Cloud. This was the first bug we discovered in the platform, which had the impact of a single-click RCE in a victim user's Compute Engine instance.

Since this was our first step into Google Cloud, we naturally stumbled upon one of the most popular products, Compute Engine. While exploring its features and how it works, I noticed *"SSH-in-browser."* It is a feature in GCP that lets users access their compute instances, through SSH, via the browser. Visually, this interface looks very similar to Cloud Shell.

![](https://blog.stazot.com/content/images/2023/01/image.png)

I was looking at the different features and options of SSH-in-browser. One feature that caught my eye was *"*Change Linux Username.*"*

![](https://blog.stazot.com/content/images/2023/01/image-1.png)

Getting username input from the user

This dialog takes an input username from the user, which is then passed to the server via a GET parameter `newLinuxUsername`. Even if the given username doesn’t exist, it’ll create a new user with the provided username and log you in as that user.

`https://ssh.cloud.google.com/v2/ssh/projects/{PROJECT-NAME}/zones/{INSTANCE-ZONE}/instances/{INSTANCE-NAME}?newLinuxUsername={USERNAME}`

Since there was *no random token or CSRF protection*, anyone could craft a link and send it to a Compute Engine user to create a new user in their instance. Not that impactful, but something to note. But the interesting part was that, at least on a surface level, it looked like it was just taking user input and passing it to `useradd` or `adduser` commands. So, command injection?

I tried to add payloads such as `` `whoami` ``, `$(whoami)`, to see if it gets executed. However, nothing happened. To check for second-order command execution, I tried `` `curl https://stazot.com` `` as the payload. Again, nothing happened. I returned to the Compute Engine instance page and started looking for other things.

I noticed that under the "SSH Keys" section, the usernames that I tried as payload were listed. This section contains the list of all users of the instance and their respective added/generated SSH keys. While payloads such as `` `whoami` `` were displayed as is, the `curl` payload was listed in a weird way.

![](https://blog.stazot.com/content/images/2023/01/image-5.png)

SSH keys of the instance

The username field contained `` `curl http ``, and the SSH key field contained `` stazot.com`:ssh-key-value ``. Instantly, bells started ringing in my head.

The server was using the colon symbol `:` as a delimiter. Anything before `:` was considered the username, and everything after `:` was considered the SSH key for that user. Theoretically, this should allow an attacker to inject a username and their public SSH key. This is possible because, as noted earlier, the server took this input in a GET request and had no CSRF protection.

So, making a victim open a malicious link would add the attacker's username and SSH key into their compute instance. To confirm the bug, I constructed the following URL with `attacker:{URL-ENCODED-SSH-PUBLIC-KEY}` as the payload:

`https://ssh.cloud.google.com/v2/ssh/projects/{PROJECT-NAME}/zones/{INSTANCE-ZONE}/instances/{INSTANCE-NAME}?newLinuxUsername=attacker:{URL-ENCODED-SSH-PUBLIC-KEY}`

Opened the link as the victim - and I tried to log into the compute instance as the attacker. However, it did not work. The reason was that the SSH key I added was then appended with the SSH key that Google generated in the backend. To fix this, I appended newline return characters to the payload:

`https://ssh.cloud.google.com/v2/ssh/projects/{PROJECT-NAME}/zones/{INSTANCE-ZONE}/instances/{INSTANCE-NAME}?newLinuxUsername=attacker:{URL-ENCODED-SSH-PUBLIC-KEY}%0d%0a`

Once this victim opened this link, I tried to log into that instance as the attacker - and *it worked!* I was logged into the target machine with *sudo* privileges.

🎉

Here is the video demonstrating the attack:

### Why did this bug exist?

This behavior existed to facilitate authorization via the SSH-in-browser feature. Since the browser acts like an SSH client, it needs an authorized SSH key to log into the instance.

Compute Engine handles this by creating an SSH key for each user in the instance (that uses SSH-in-browser) and storing it in the instance metadata. When the user logs in using SSH-in-browser, the instance fetches all the authorized SSH keys from the metadata server and logs in the user.

This is a very elaborate process, which is explained [here](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-public/red-team-tech-notes/-/tree/master/oslogin-privesc-june-2020#how-os-login-works) in detail.

### Disclosure

We received a $5000 bounty and a $1000 bonus for reporting this bug to Google VRP.

> *Rationale for this decision:*

### Timeline

`Jul 14, 2022 - Reported
Jul 15, 2022 - Closed as Intended Behavior
Jul 15, 2022 - Further explanation was sent
Jul 16, 2022 - Unable to reproduce
Jul 16, 2022 - PoC video was sent
Jul 23, 2022 - 🎉 Nice catch!
Jul 26, 2022 - Rewarded a $6000 bounty`

文章来源: https://govuln.com/news/url/k42a
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)