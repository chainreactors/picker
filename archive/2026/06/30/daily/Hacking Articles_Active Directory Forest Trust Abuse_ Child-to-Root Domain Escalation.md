---
title: Active Directory Forest Trust Abuse: Child-to-Root Domain Escalation
url: https://www.hackingarticles.in/active-directory-forest-trust-abuse-child-to-root-domain-escalation/
source: Hacking Articles
date: 2026-06-30
fetch_date: 2026-07-01T06:23:00.571373
---

# Active Directory Forest Trust Abuse: Child-to-Root Domain Escalation

[Skip to content](#content)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [Red Teaming](https://www.hackingarticles.in/category/red-teaming/)
»* [Active Directory Forest Trust Abuse: Child-to-Root Domain Escalation](https://www.hackingarticles.in/active-directory-forest-trust-abuse-child-to-root-domain-escalation/)
»

[Red Teaming](https://www.hackingarticles.in/category/red-teaming/)

# Active Directory Forest Trust Abuse: Child-to-Root Domain Escalation

[June 30, 2026June 30, 2026](https://www.hackingarticles.in/active-directory-forest-trust-abuse-child-to-root-domain-escalation/) by [raj](https://www.hackingarticles.in/author/admin/)

### **Overview**

This article walks through **a complete forest compromise of an Active Directory environment, escalating from a single child domain all the way to the forest root**. The engagement targets the ignite.local forest, which contains a dedicated child domain named pentest.ignite.local. Starting from a Domain Admin account in the child domain, the attacker confirms that this privilege does not directly reach the parent, enumerates the forest trust, extracts the child domain krbtgt hash, and forges a cross-domain Golden Ticket that injects the parent Enterprise Admins SID through SID History.

From there, the attacker weaponises the forged ticket: a pass-the-ticket attack unlocks the forest root domain controller, secrets are harvested from both Windows and Linux, the entire escalation is automated with a single NetExec module, and the forest finally falls through a full DCSync and an interactive SYSTEM shell. A second, independent path then reaches the same outcome by coercing the forest root into authenticating to an attacker-controlled child domain controller. Every action shown here was performed against an isolated, fully authorised laboratory built solely for security research and education.

### **Table of Contents:**

* **Introduction**
* **Lab Environment**
* **Phase 1: Building and Seizing the Child Domain**
* **Phase 2: Confirming the Access Boundary**
* **Phase 3: Enumerating the Forest Trust**
  + Trust discovery with NetExec
  + Trust details with PyWerView
  + Trust confirmation with Impacket and nltest
  + Trust confirmation with PowerShell
  + Trust confirmation with bloodyAD
* **Phase 4: Extracting the krbtgt Hash and Required SIDs**
  + Dumping the child krbtgt hash
  + Child domain SID
  + Parent Enterprise Admins SID
* **Phase 5: Forging the Cross-Domain Golden Ticket**
  + Staging Rubeus
  + Building the ticket
* **Phase 6: Passing the Ticket into the Forest Root**
* **Phase 7: Harvesting Forest Root Secrets from Linux**
* **Phase 8: Automating the Escalation with NetExec**
  + Forging the ticket with raisechild
  + Validating the forged ticket
* **Phase 9: Achieving Full Forest Compromise**
  + DCSync of the forest root
  + Interactive SYSTEM shell on the forest root
* **Phase 10: Alternative Path — Coercion-Based Compromise**
  + Confirming the coercion vector
  + Monitoring for the DC machine account ticket
  + Coercing the forest root with PetitPotam
  + Capturing the forest root ticket
  + Converting the captured ticket
  + DCSync with the captured machine account
* Mitigation Strategies
* Conclusion

### **Introduction**

Active Directory organises large environments into forests, and a forest can contain multiple domains arranged in a parent-child hierarchy. Administrators often assume that a child domain forms a strong security boundary. In reality, the security boundary in Active Directory is the forest, not the domain. Every domain in a forest is connected by an automatic, bidirectional, transitive trust, and SID filtering is intentionally relaxed for these intra-forest trusts so that universal groups and SID History flow freely between domains.

Attackers weaponise this design. A Golden Ticket is a Kerberos Ticket Granting Ticket forged with the krbtgt account hash of a domain; because it is signed with the very key the Key Distribution Center uses to validate tickets, the domain accepts it without question. Rubeus extends this primitive with the /sids parameter, which writes additional SIDs into the ExtraSids field of the ticket — the same field SID History uses. Placing the parent Enterprise Admins SID into that field turns a single child domain compromise into a complete forest takeover.

A forged ticket only becomes useful once it is presented to a service. Pass-the-ticket injects a Kerberos ticket directly into the current logon session, letting the attacker authenticate as the forged identity without ever knowing a password. The same outcome can also be reached without any krbtgt hash: domain controllers enable unconstrained delegation by default, so coercing the forest root into authenticating to an attacker-controlled child domain controller captures the parent machine account ticket, whose built-in replication rights are enough to dump the domain. This article demonstrates all of these techniques, in phases, against ignite.local.

### **Lab Environment**

The lab models a typical multi-domain forest. The forest root ignite.local hosts the Enterprise Admins group and runs on the domain controller DC, while a child domain pentest.ignite.local runs on a separate domain controller named CDC01. The attacker operates from Kali Linux and works toward, and then from, a Domain Admin account named raaz inside the child domain.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2LbZv7-GrTp8Otnbkeno2Q0ASBrE08z_nlHYnYMAPt-I3OooP3ZFywdL_A3t_Q3La27wPubn-yh4Fx541Rtbt0t1I2Ji-NSn6Dlsrbn684eSmuo3i996EEEldHLQRMi9umNbNoFlwtqZS-VFDbNWPgB61w1y4iLCW-H5SVNgEScJn03R2XsrhOiJdb8WZ/s1600/0.1.png)

## **Phase 1: Building and Seizing the Child Domain**

The engagement begins by standing up the child domain so the parent-child trust exists to attack, then planting a Domain Admin foothold inside it. Before promoting the new server, the network adapter must point at the forest DNS infrastructure, because Active Directory promotion relies entirely on DNS to locate the parent domain. The image below shows the IPv4 properties of the prospective child domain controller, resolving through the loopback address as its own future DNS service while delegating to the parent domain controller at **192.168.1.11** as the alternate server.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgeSuAkngodrk3_5XhKCYs4Gi7XqGtU3pZyv6EcTzpskGEdLnVPmwytFt9Hs2L_8cRv1oG0puLQOiJnI2it7QAO2mIfgg4r0HOkTTZhr6W-Vb_JOeRxG8_QM6AL10VH_WQrFFp-E1tHkpJGqlH2XoIc0BaY27Mx7_PHxwtYRachiR-ke8YqN6hAxvpMBpZN/s1600/0.png)

With DNS in place, the **Add Roles and Features Wizard launches from Server Manager on the host named CDC01**. The opening page restates the prerequisites — a strong administrator password, static networking, and current updates — before role selection begins.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnm5LVVv_ryIBQKAN46P2uxDDFydcClz1S61u_MNehVnGh48b7H8n_Kb2_psOQK31sWkUbpZmmbLx5CM299YHt8P_fZ0CsmVCjo_YPscdgGp7x1nrnKn0cvQZomMH171RNfmMChQbh_eCA2mzGUrRcC2-xrGDqMk9xx6dyVruciq2I5NhNBJ6aIr88yACJ/s1600/1.png)

On the role selection page, the attacker enables the **Active Directory Domain Services role**, which installs the **binaries** required to **promote the machine into a domain controller**, along with the supporting management tools.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYNcGJkcyZrlFNHwuAv_jMOSfSlpAk75YUj8jG1KH5shHi6f8gmd0RRcAme9b10zz9f3RxRxpJT4h19...