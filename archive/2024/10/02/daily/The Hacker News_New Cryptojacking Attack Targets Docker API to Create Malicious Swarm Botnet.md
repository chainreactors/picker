---
title: New Cryptojacking Attack Targets Docker API to Create Malicious Swarm Botnet
url: https://thehackernews.com/2024/10/new-cryptojacking-attack-targets-docker.html
source: The Hacker News
date: 2024-10-02
fetch_date: 2025-10-06T19:02:14.472849
---

# New Cryptojacking Attack Targets Docker API to Create Malicious Swarm Botnet

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [New Cryptojacking Attack Targets Docker API to Create Malicious Swarm Botnet](https://thehackernews.com/2024/10/new-cryptojacking-attack-targets-docker.html)

**Oct 01, 2024**Ravie LakshmananCryptojacking / Docker Security

[![Docker Swarm Botnet](data:image/png;base64... "Docker Swarm Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdsRPnFD736G2dKa6_CD-PeeGkbEjPRceULyY9rdE1Fi50fx_z5FMNRNvwQ60oiR7A9ZoZS0KCpxascMk5Gmy6qhHwX4kEbC-zY2qzyeNoz59tTJr8WZqFD8UKVAaqzbfx-nway84pQ1BhKhtMhGVQM3h3bEq1w65sO_bzMGOC8TjT-JeS3Uurl51j234W/s790-rw-e365/docker.png)

Cybersecurity researchers have uncovered a new cryptojacking campaign targeting the Docker Engine API with the goal of co-opting the instances to join a malicious Docker Swarm controlled by the threat actor.

This enabled the attackers to "use Docker Swarm's orchestration features for command-and-control (C2) purposes," Datadog researchers Matt Muir and Andy Giron [said](https://securitylabs.datadoghq.com/articles/threat-actors-leveraging-docker-swarm-kubernetes-mine-cryptocurrency/) in an analysis.

The attacks leverage [Docker for initial access](https://thehackernews.com/2024/04/millions-of-malicious-imageless.html) to deploy a cryptocurrency miner on compromised containers, while also fetching and executing additional payloads that are responsible for conducting lateral movement to related hosts running Docker, Kubernetes, or SSH.

Specifically, this involves identifying unauthenticated and exposed Docker API endpoints using Internet scanning tools, such as masscan and [ZGrab](https://thehackernews.com/2023/07/silentbob-campaign-cloud-native.html).

On vulnerable endpoints, the Docker API is used to spawn an Alpine container and then retrieve an initialization shell script (init.sh) from a remote server ("solscan[.]live") that, in turn, checks if it's running as the root user and tools like curl and wget are installed before downloading the XMRig miner.

Like other cryptojacking campaigns, it makes use of the [libprocesshider rootkit](https://thehackernews.com/2022/10/new-cryptojacking-campaign-targeting.html) to hide the malicious miner process from the user when running process enumerating tools like top and ps.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The shell script is also designed to fetch three other shell scripts – kube.lateral.sh, spread\_docker\_local.sh, and spread\_ssh.sh – from the same server for lateral movement to Docker, Kubernetes, and SSH endpoints on the network.

Spread\_docker\_local.sh "uses masscan and zgrab to scan the same LAN ranges [...] for nodes with ports 2375, 2376, 2377, 4244, and 4243 open," the researchers said. "These ports are associated with either Docker Engine or Docker Swarm."

"For any IPs discovered with the target ports open, the malware attempts to spawn a new container with the name alpine. This container is based on an image named upspin, hosted on Docker Hub by the user nmlmweb3."

The upspin image is designed to execute the aforementioned init.sh script, thus allowing the group's malware to propagate in a worm-like fashion to other Docker hosts.

What's more, the Docker image tag that's used to retrieve the image from Docker Hub is specified in a text file hosted on the C2 server, thereby allowing the threat actors to easily recover from potential takedowns by simply changing the file contents to point to a different container image.

The third shell script, spread\_ssh.sh, is capable of compromising SSH servers, as well as adding an SSH key and a new user named ftp that enables the threat actors to remotely connect to the hosts and maintain persistent access.

[![Cryptojacking Attack](data:image/png;base64... "Cryptojacking Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj926jleVncuaMxnDqR73zVOp0cGF5tbQMWHYQ49OcxCy-4glv-AvsRqBo3NtrNEZFmp5rZd5bbwdKC4vH7Vcu6pdbjQJPMR4T3CZxB-8zeK_WyDwbIGKd-anNhxcWtW4jnampy5KbJqKz5fWYBe1qPGczQb-SEBisyEggcEs92NLI52kxuR3KbxPpMaOBD/s790-rw-e365/cryptojacking.png)

It also searches for various credential files related to SSH, Amazon Web Services (AWS), Google Cloud, and Samba in hard-coded file paths within the GitHub Codespaces environment (i.e., the "/home/codespace/" directory), and if found, uploads them to the C2 server.

In the final stage, both the Kubernetes and SSH lateral movement payloads execute another shell script called setup\_mr.sh that retrieves and launches the cryptocurrency miner.

Datadog said it also discovered three other scripts hosted on the C2 server -

* ar.sh, a variant of init.sh that modifies iptables rules and clears logs and cron jobs to evade detection
* TDGINIT.sh, which downloads scanning tools and drops a malicious container on each identified Docker host
* pdflushs.sh, which installs a persistent backdoor by appending a threat-actor-controlled SSH key to the /root/.ssh/authorized\_keys file

TDGINIT.sh is also notable for its manipulation of Docker Swarm by forcing the host to leave any existing Swarm it may be part of and add it to a new Swarm under the attacker's control.

"This allows the threat actor to expand their control over multiple Docker instances in a coordinated fashion, effectively turning compromised systems into a botnet for further exploitation," the researchers said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's currently not clear who is behind the attack campaign, although the tactics, techniques, and procedures exhibited overlap with those of a known threat group known as [TeamTNT](https://thehackernews.com/2024/09/new-teamtnt-cryptojacking-campaign.html).

"This campaign demonstrates that services such as Docker and Kubernetes remain fruitful for threat actors conducting cryptojacking at scale," Datadog said.

"The campaign relies on Docker API endpoints being exposed to the Internet without authentication. The malware's ability to propagate rapidly means that even if the chances of initial access ...