---
title: Interview #10 diencracked (BreachForums owner)
url: https://deepdarkcti.com/interview-10-diencracked-breachforums-owner/
source: Over Security
date: 2026-05-16
fetch_date: 2026-05-17T05:48:11.654411
---

# Interview #10 diencracked (BreachForums owner)

[![deepdarkCTI](https://deepdarkcti.com/wp-content/uploads/2025/02/deepdarkCTI_150_150.png)](https://deepdarkcti.com/)

# [deepdarkCTI](https://deepdarkcti.com)

* [Who Am I](https://deepdarkcti.com/who-am-i/)
* [Blog](https://deepdarkcti.com/blog/)

* [Twitter](https://x.com/fastfire)
* [Telegram](https://t.me/fastfire83)
* [Bluesky](https://bsky.app/profile/fastfire.bsky.social)
* [LinkedIn](https://www.linkedin.com/in/massimo-giaimo-b78ba0a/)

# [Interview #10 diencracked (BreachForums owner)](https://deepdarkcti.com/interview-10-diencracked-breachforums-owner/)

May 15, 2026

[![Interview #10 diencracked (BreachForums owner)](https://deepdarkcti.com/wp-content/uploads/2026/05/image-1.png)](https://deepdarkcti.com/interview-10-diencracked-breachforums-owner/)

The following interview, which we publish in full, was conducted in May 2026 by me, fastfire.

“BreachForums” (often referred to as “Breached”) is an English-language cybercriminal forum. It functioned as a clear-net marketplace and platform for threat actors to trade stolen databases, tools, access credentials, and other illicit services.

![](https://deepdarkcti.com/wp-content/uploads/2026/05/image-1-1024x430.png)

A few days ago, the forum owner, *diencracked*, published a post announcing a supply chain competition, in which the goal is to use the *Shai Hulud* malware to compromise organizations. In the post, diencracked promises a $1,000 prize to the person who conducts the largest attack.

![](https://deepdarkcti.com/wp-content/uploads/2026/05/image-2-1024x639.png)

## What if Shai Hulud malware?

The Shai Hulud malware is a sophisticated, self-propagating JavaScript-based worm that targets the npm (Node Package Manager) ecosystem. Named after the iconic sandworms from Dune, it specializes in supply chain attacks by automating the compromise of developer environments and repositories.

**Core Functionality and Attack Chain**

The malware typically spreads by injecting malicious code into the *postinstall* or *preinstall* scripts of legitimate npm packages.

**Credential Harvesting:** Once a developer installs a compromised package, the malware scans the local environment for sensitive secrets, including GitHub Personal Access Tokens (PATs), npm tokens, SSH keys, and cloud provider keys (AWS, GCP, Azure).
**Data Exfiltration:** Stolen data is often encoded and uploaded to newly created public GitHub repositories, frequently using descriptions like “Sha1-Hulud: The Second Coming” to organize the stolen credentials.
**Worm Propagation:** If the malware discovers valid npm publishing tokens, it automatically infects and republishes other packages managed by the compromised developer, creating an exponential cycle of infection across the ecosystem.
**Persistence:** It may establish persistence by pushing malicious GitHub Actions workflows (e.g., shai-hulud-workflow.yml) to accessible repositories.

**Evolution and Recent Variants**

Since its first appearance in late 2025, the malware has evolved through several iterations:

*Shai-Hulud 1.0 (Sept 2025):* Initial wave affecting approximately 180 packages, including libraries like @ctrl/tinycolor.
*Shai-Hulud 2.0 (Nov/Dec 2025):* A significantly more automated version that compromised over 30,000 GitHub repositories and hundreds of packages, including those from Zapier, ENS Domains, and Postman.
*Shai-Hulud 3.0 (Early 2026):* Introduced technical improvements for resilience and evasion, such as enhanced obfuscation and broader compatibility across different JavaScript runtimes.
*“The Golden Path” Variant:* A more recent variant seen testing cross-platform publishing features and updated file nomenclature to improve its “smash-and-grab” efficiency.

## Origin & Identity of diencracked

![](https://deepdarkcti.com/wp-content/uploads/2026/05/image-5-1024x606.png)

**Q (fastfire):** When did you first become active in the cybercrime community, and what led you to establish breached.st as the platform it is today? How do you position yourself relative to the other competing BreachForums iterations – the original (run by Indra and N/A) and HasanBroker’s “NotBreachForums”?

**A (diencracked):** I have been active in the community for a while now, and I found BreachForums at a starting phase where HasanBroker, the leader, was looking for a trusted partner to work with. We became partners and are now good friends. I created the site alongside him and manage everything development related. In the past, we breached Indra’s and N/A’s fake BreachForums, and we are running a bettered version of the site, that does not have the same issues that the myBB version does. We see ourselves and the forum as valuable and irreplacable parts of the community, and we will continue bettering the forum and making alliances with other groups.

**Q (fastfire):** Your forum handle “diencracked” – does it have a specific meaning or origin story? Were you active under a different alias before establishing this identity on breached.st?

**A (diencracked):** My handle “diencracked” is more of a random alias I chose. Originally, it was meant to be “die (a)n(d) cracked” but it’s been commonly shortened as “dien” too. I was active on different aliases in the past, but for operational security reasons I cannot share them here.

## Relationship with TeamPCP

**Q (fastfire):** Your post explicitly brands the competition as “BreachForums + TeamPCP.” What is the nature of your relationship with TeamPCP? Are you a member of TeamPCP, or is this a business partnership between two separate entities?

**A (diencracked):** Yes, I am currently working alongside TeamPCP, and BreachForums and TeamPCP are partners.

**Q (fastfire):** TeamPCP has also announced a formal partnership with the Vect ransomware group *(reference note: during the interview, Dien Cracked stated that he directly manages Vect’s infrastructure)*, offering BreachForums members affiliate access with 80-88% profit shares. Were you involved in brokering this tripartite alliance (breached.st + TeamPCP + Vect), and do you or your forum receive a cut from Vect’s ransomware operations?

**A (diencracked):** As BreachForums, yes, we were involved in the alliance and we received cuts from the operations. However, as stated before, TeamPCP has never used Vect encryption tools and we own CipherForce, our own private locker, which dozens of victims have recovered files using, our partnership with them has been for the negotiation/pentest team only. If you are encrypted by TeamPCP, any issues with Vect will not affect the situation.

## Relationship with LAPSUS$ group

![](https://deepdarkcti.com/wp-content/uploads/2026/05/image-4-1024x819.png)

**Q (fastfire):** In the post https[:]//breached[.]st/threads/lapsus-x-hasanbroker.1175/, user *LAPSUS$*, presumably a member of the group of the same name, stated their shared goal of deleting user Indra and his forum. What is the current status of this operation?

**A (diencracked):** Lapsus$ is a trusted partner of Breachforums and TeamPCP, and the current status of the operation is that it was a success. We destroyed breachforums.as, but for now, we are going into the defensive and are focused on improving and growing our own community.

## Origin & Development of Shai Hulud

**Q (fastfire):** Who originally developed Shai Hulud? Was it built by TeamPCP from scratch, or was it derived from existing tooling – for example, from the actor known as “s1ngularity” who has been linked to the initial September 2025 supply chain wave?

**A (diencracked):** The current Shai Hulud used in our latest attacks was developed by TeamPCP from scratch, I don’t have anything to say regarding the history of it.

**Q (fastfire):** The worm uses an elaborate Dune-themed naming convention for dead-drop commit branches – atreides, fedaykin, fremen, harkonnen, melange, sardaukar, and many more. Who designed this taxonomy, and is there an operational logic behind the branch names (e.g., do they map to specific camp...