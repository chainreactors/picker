---
title: Daily Krypt3ia Cyber Threat Intelligence Digest:
url: https://krypt3ia.wordpress.com/2025/01/16/daily-krypt3ia-cyber-threat-intelligence-daily-digest/
source: Krypt3ia
date: 2025-01-17
fetch_date: 2025-10-06T20:13:26.233793
---

# Daily Krypt3ia Cyber Threat Intelligence Digest:

# [Krypt3ia](https://krypt3ia.wordpress.com/)

(Greek: κρυπτεία / krupteía, from κρυπτός / kruptós, “hidden, secret things”)

## Daily Krypt3ia Cyber Threat Intelligence Digest:

[with one comment](https://krypt3ia.wordpress.com/2025/01/16/daily-krypt3ia-cyber-threat-intelligence-daily-digest/#comments)

**Date:** January 16, 2025
**Time:** 0800 ET

This report provides key insights into the most critical cybersecurity events and threats across the categories of **Malware**, **Advanced Persistent Threats (APTs)**, **Internet Crime**, **Ransomware**, **Phishing**, and **Hacking**. It highlights active risks, emerging tactics, and actionable intelligence to enhance your cybersecurity posture.

---

### **Malware**

#### **FBI Deletes PlugX Malware from Thousands of Computers Worldwide**

* **Source:** [IT PRO](https://www.itpro.com/security/cyber-crime/us-authorities-just-purged-malware-from-thousands-of-devices-across-the-world)
* **Details:**
  + A global FBI-led operation successfully removed the PlugX malware from thousands of infected systems.
  + **Background:** PlugX, a remote access Trojan (RAT), is commonly used by Chinese APT groups such as APT10. It allows attackers to execute commands, exfiltrate data, and maintain persistence on compromised systems.
  + **Significance:** This marks one of the largest coordinated malware removal efforts by U.S. law enforcement.
  + **Recommendations:**
    - Conduct a full system scan to identify residual PlugX artifacts.
    - Update and harden endpoint security solutions to detect future RAT infections.

#### **Hackers Hiding Malware in Images via Steganography**

* **Source:** [The Hacker News](https://thehackernews.com/2025/01/hackers-hide-malware-in-images-to.html)
* **Details:**
  + Attackers are embedding malware such as the VIP Keylogger and 0bj3ctivity Stealer within image files (.png, .jpg) using steganographic techniques.
  + **Impact:** This tactic evades traditional email and web filters, enabling silent delivery of payloads to victims’ devices.
  + **Recommendations:**
    - Use advanced threat detection tools capable of scanning image metadata and analyzing steganographic payloads.
    - Block suspicious image downloads from unknown or untrusted sources.

---

### **Advanced Persistent Threats (APTs)**

#### **North Korean Hackers Targeting Freelance Developers**

* **Source:** [SecurityWeek](https://www.securityweek.com/north-korean-hackers-targeting-freelance-software-developers/)
* **Details:**
  + North Korean APT groups are targeting freelance software developers through fake job offers. These campaigns implant malware disguised as legitimate development tools, compromising devices for data theft or cryptocurrency wallet breaches.
  + **Significance:** Highlights North Korea’s evolving tactics to fund state operations via cybercrime.
  + **Recommendations:**
    - Verify the legitimacy of job offers before engaging.
    - Use sandbox environments for testing new tools or software downloaded from untrusted sources.

#### **Russia Allegedly Spying on Kazakhstan Amid Renewed Tensions**

* **Source:** [The Times of Central Asia](https://timesca.com/cyber-deja-vu-is-russia-spying-on-kazakhstan-again/)
* **Details:**
  + Russian APT groups have reportedly resumed espionage campaigns targeting critical infrastructure and government networks in Kazakhstan.
  + **TTPs:** These groups are leveraging spear-phishing campaigns and exploiting unpatched vulnerabilities in legacy software.
  + **Global Implications:** Neighboring nations may also be targeted as part of Russia’s regional influence strategy.
  + **Recommendations:**
    - Prioritize patching vulnerabilities in government and industrial systems.
    - Implement email filtering solutions to detect and block spear-phishing attempts.

---

### **Internet Crime**

#### **Hackers Exploiting Google Ads to Serve Malicious Links**

* **Source:** [Cyber Security News](https://cybersecuritynews.com/hackers-exploiting-companies-google-ads-accounts/)
* **Details:**
  + Cybercriminals are compromising Google Ads accounts to distribute malicious links that redirect users to phishing websites or deliver malware payloads.
  + **Targets:** Businesses using Google Ads for their marketing campaigns.
  + **Recommendations:**
    - Regularly audit ad account activity for unauthorized changes.
    - Enable two-factor authentication (2FA) on all ad platform accounts.

#### **PowerSchool Data Breach Exposes Student and Teacher Records**

* **Source:** [JD Supra](https://www.jdsupra.com/legalnews/powerschool-data-breach-confirmed-6415852/)
* **Details:**
  + Hackers stole historical student and teacher data from PowerSchool’s database. The breach exposed sensitive personal information of thousands of individuals.
  + **Impact:** Victims face risks of identity theft and further exploitation.
  + **Recommendations:**
    - Notify affected individuals and offer identity monitoring services.
    - Enhance encryption and access controls on sensitive databases.

---

### **Ransomware**

#### **UK Considers Banning Ransomware Payments for Public Services**

* **Source:** [TechInformed](https://techinformed.com/uk-mulls-ransomware-payment-ban-for-public-services/)
* **Details:**
  + The UK government is debating a policy to prohibit public sector organizations and critical infrastructure companies from paying ransomware demands.
  + **Objective:** Remove financial incentives for ransomware groups.
  + **Challenges:** Without robust recovery capabilities, this policy may leave organizations vulnerable to prolonged disruptions.
  + **Recommendations:**
    - Invest in ransomware prevention strategies, including offline backups and incident response plans.
    - Enhance disaster recovery capabilities across public sector organizations.

#### **Ransomware Victims and Threat Groups Hit Record Highs in 2024**

* **Source:** [Business Wire](https://www.businesswire.com/news/home/20250116994599/en)
* **Details:**
  + Recent data shows ransomware attacks and victims reached an all-time high, with notable activity from groups such as LockBit and Black Basta.
  + **Trends:** Double-extortion tactics remain the primary strategy, where data is both encrypted and threatened with public exposure.
  + **Recommendations:**
    - Enforce endpoint monitoring to detect ransomware payloads early.
    - Deploy threat intelligence feeds to block indicators of compromise (IoCs) associated with major ransomware operators.

---

### **Phishing**

#### **AI-Generated Phishing Campaigns Bypass Email Filters**

* **Source:** [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/hackers-image-malware-genai-evade/)
* **Details:**
  + Threat actors are leveraging generative AI to craft highly convincing phishing emails. These emails evade traditional email security tools and target high-level executives with credential-stealing links.
  + **Impact:** Increases the likelihood of successful credential harvesting and unauthorized access to sensitive systems.
  + **Recommendations:**
    - Train employees to recognize AI-crafted phishing emails.
    - Use AI-powered email filtering tools capable of analyzing message intent.

#### **Microsoft Teams Abused to Deliver Black Basta Ransomware**

* **Source:** [Cyber Security News](https://cybersecuritynews.com/black-basta-abusing-teams-chat-for/)
* **Details:**
  + The Black Basta ransomware group is exploiting Microsoft Teams by using stolen credentials to send malicious links or payloads via chat.
  + **Recommendations:**
    - Implement MFA for Microsoft 365 accounts.
    - Monitor Teams usage logs for anomalous activity, such as messages from unauthorized devices or accounts.

---

### **Hacking**

#### **Hackers Abusing Image Metadata for VIP Keylogger and Steganographic Attacks**

* **Source:** [The Hacker News](https://thehackernews.com/2025/01/hackers-hide-malware-in-images-to.html)
* **Details:**
  + Attackers are hiding malicious scripts...