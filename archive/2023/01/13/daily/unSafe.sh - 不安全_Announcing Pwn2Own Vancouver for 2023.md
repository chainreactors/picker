---
title: Announcing Pwn2Own Vancouver for 2023
url: https://buaq.net/go-145273.html
source: unSafe.sh - 不安全
date: 2023-01-13
fetch_date: 2025-10-04T03:43:15.518880
---

# Announcing Pwn2Own Vancouver for 2023

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

![]()

Announcing Pwn2Own Vancouver for 2023

Jump to the contest rulesLast year, we celebrated the
*2023-1-12 22:43:33
Author: [www.thezdi.com(查看原文)](/jump-145273.htm)
阅读量:27
收藏*

---

[*Jump to the contest rules*](https://www.zerodayinitiative.com/Pwn2OwnVancouver2023Rules.html)

Last year, we celebrated the 15th anniversary of Pwn2Own with a spectacular contest. We awarded more than $1,000,000 USD for the amazing research demonstrated. That makes us even more excited to return to Vancouver for the 2023 edition of Pwn2Own. Similar to last year, we’ll be holding a hybrid conference with most of us in person at the Sheraton Wall Center in Vancouver for the [CanSecWest](https://www.secwest.net/) conference on March 22-24, 2023. The other part of the hybrid event means that we also allow remote participation. If you have either travel restrictions or travel safety concerns, you can opt to compete remotely.

We’re also excited to have **Tesla** return as a partner. They always innovate, and we’ve updated our target list to keep up. We’ve added a [Steam VM Escape](https://arstechnica.com/gaming/2022/12/steam-powered-cars-tesla-adds-valves-game-platform-to-latest-models/#:~:text=The%20newest%20models%20of%20Tesla's,addition%2C%20part%20of%20Tesla's%202022.44.) category with multiple targets. It may a bit strange to be targeting a steam engine on an electric car, but here we are. We’ll have both a Tesla Model 3 *and* a Tesla Model S available as targets, with the top prize going for $600,000 (plus the car itself). Of course, virtualization exploits are always a contest highlight, and **VMware** returns as a sponsor with VMware Workstation and ESXi returning as targets.

We’ve added a couple of new targets in other existing categories as well. DNS is one of the core services of the internet, and cloud computing couldn’t work without it. That’s why we’ve added Microsoft DNS Server and ISC BIND into the Servers category. Apple systems are a common item found in work centers, so we’ve added macOS back into the Local Escalation of Privilege category with a focus on the M-series MacBook Pro.

In addition to the in-person attempts at the conference, we’ll be producing quick videos of the exploits, so if you can’t attend you can still get a feel for what it’s like in the room. All told, more than $1,000,000 USD in cash and prizes are available to contestants, including the Tesla vehicle, in the following categories:

Of course, no Pwn2Own competition would be complete without us crowning a Master of Pwn. Since the order of the contest is decided by a random draw, contestants with an unlucky draw could still demonstrate fantastic research but receive less money since subsequent rounds go down in value. However, the points awarded for each unique, successful entry do *not* go down. Someone could have a bad draw and still accumulate the most points. The person or team with the most points at the end of the contest will be crowned Master of Pwn, receive 65,000 ZDI reward points (instant [Platinum](https://www.zerodayinitiative.com/about/benefits/) status), a killer [trophy](https://static1.squarespace.com/static/5894c269e4fcb5e65a1ed623/t/5b8993b321c67c67b886f506/1535742910114/trophy.jpg), and a [pretty](https://pbs.twimg.com/media/C6Z5iQQXEAEPQ0Q.jpg) [snazzy](https://pbs.twimg.com/media/DNhpw_xUEAEkEwG.jpg) [jacket](https://pbs.twimg.com/media/Cu-6uFSWcAEefBS.jpg) to boot.

Let's look at the details of the rules for this year's contest.

We’re happy to have **VMware** returning as a Pwn2Own sponsor for 2023, and this year, again we’ll have VMware ESXi alongside VMware Workstation as a target with awards of $150,000 and $80,000 respectively. VMware has been a sponsor of Pwn2Own for multiple years, and we’ve seen some great research presented at the contest in years past. Microsoft also returns as a target and leads the virtualization category with a $250,000 award for a successful Hyper-V Client guest-to-host escalation. Oracle VirtualBox rounds out this category with a prize of $40,000. We’ve seen some amazing guest-to-host OS escalations demonstrated at previous Pwn2Own contests. Here’s hoping we see more this year.

There’s an add-on bonus in this category as well. If a contestant can escape the guest OS, then escalate privileges on the host OS through a Windows kernel vulnerability (excluding VMware ESXi), they can earn an additional $50,000 and 5 more Master of Pwn points. That could push the payout on a Hyper-V bug to $300,000. Here’s a detailed look at the targets and available payouts in the Virtualization category:

[*Back to categories*](#top)

***Web Browser Category***

While browsers are the “traditional” Pwn2Own target, we’re continuously tweaking the targets in this category to ensure they remain relevant. We re-introduced renderer-only exploits last year, and this year, their price increases to $60,000. However, if you have that Windows kernel privilege escalation or sandbox escape, that will earn you up to $100,000 or $150,000 respectively. If your exploit works on *both* Chrome and Edge, it will qualify for the “Double Tap” add-on of $25,000. The Windows-based targets will be running in a VMware Workstation virtual machine. Consequently, all browsers (except Safari) are eligible for a VMware escape add-on. If a contestant can compromise the browser in such a way that also executes code on the host operating system by escaping the VMware Workstation virtual machine, they will earn themselves an additional $80,000 and 8 more Master of Pwn points. Full exploits are still required for Apple Safari and Mozilla Firefox. Here’s a detailed look at the targets and available payouts:

[*Back to categories*](#top)

***Enterprise Applications Category***

Enterprise applications also return as targets with Adobe Reader and various Office components on the target list once again. This year, we’re also allowing these applications to be run on an M-series MacBook. Prizes in this category run from $50,000 for a Reader exploit with a sandbox escape or a Reader exploit with a kernel privilege escalation and $100,000 for an Office 365 application. Word, Excel, and PowerPoint are all valid targets. Microsoft Office-based targets will have Protected View enabled where applicable. Adobe Reader will have Protected Mode enabled where applicable. Here’s a detailed view of the targets and payouts in the Enterprise Application category:

[*Back to categories*](#top)

***Server Category***

As mentioned, we’re again expanding the Server category by adding ISC BIND and Microsoft DNS Server to the target list. A successful exploit on one of these will earn the contestants $200,000 or $150,000 respectively. We added Samba as a target last year but has no takers. We’ll see if any registers for it in 2023. This category is rounded out by Microsoft Windows RDP/RDS, which also has a payout of $200,000. Here’s a detailed look at the targets and payouts in the Server category:

[*Back to categories*](#top)

***Local Escalation of Privilege Category***

This category is a classic for Pwn2Own and focuses on attacks that originate from a standard user and result in executing code as a high-privileged user. A successful entry in this category must leverage a kernel vulnerability to escalate privileges. Ubuntu Desktop, Apple macOS, and Microsoft Windows 11 are the OSes available as targets in this category.

[*Back to categories*](#top)

***Enterprise Communications Category***

We introduced this category in 2021 to reflect the importance of these tools in our modern, remote workforce, and we were thrilled to see both targets compromised duri...