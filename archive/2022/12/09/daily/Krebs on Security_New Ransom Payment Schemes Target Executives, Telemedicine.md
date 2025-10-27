---
title: New Ransom Payment Schemes Target Executives, Telemedicine
url: https://krebsonsecurity.com/2022/12/new-ransom-payment-schemes-target-executives-telemedicine/
source: Krebs on Security
date: 2022-12-09
fetch_date: 2025-10-04T01:02:31.732120
---

# New Ransom Payment Schemes Target Executives, Telemedicine

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# New Ransom Payment Schemes Target Executives, Telemedicine

December 8, 2022

[7 Comments](https://krebsonsecurity.com/2022/12/new-ransom-payment-schemes-target-executives-telemedicine/#comments)

Ransomware groups are constantly devising new methods for infecting victims and convincing them to pay up, but a couple of strategies tested recently seem especially devious. The first centers on targeting healthcare organizations that offer consultations over the Internet and sending them booby-trapped medical records for the “patient.” The other involves carefully editing email inboxes of public company executives to make it appear that some were involved in insider trading.

![](https://krebsonsecurity.com/wp-content/uploads/2022/12/insidertrading.png)

**Alex Holden** is founder of [Hold Security](https://www.holdsecurity.com), a Milwaukee-based cybersecurity firm. Holden’s team gained visibility into discussions among members of two different ransom groups: **CLOP** (a.k.a. “**Cl0p**” a.k.a. “[TA505](https://malpedia.caad.fkie.fraunhofer.de/details/win.clop)“), and a newer ransom group known as **Venus**.

Last month, the **U.S. Department of Health and Human Services** (HHS) [warned](https://www.hhs.gov/sites/default/files/venus-ransomware-analyst-note.pdf) that Venus ransomware attacks were targeting a number of U.S. healthcare organizations. First spotted [in mid-August 2022](https://www.bleepingcomputer.com/news/security/venus-ransomware-targets-publicly-exposed-remote-desktop-services/), Venus is known for hacking into victims’ publicly-exposed Remote Desktop services to encrypt Windows devices.

Holden said the internal discussions among the Venus group members indicate this gang has no problem gaining access to victim organizations.

“The Venus group has problems getting paid,” Holden said. “They are targeting a lot of U.S. companies, but nobody wants to pay them.”

Which might explain why their latest scheme centers on trying to frame executives at public companies for insider trading charges. Venus indicated it recently had success with a method that involves carefully editing one or more email inbox files at a victim firm — to insert messages discussing plans to trade large volumes of the company’s stock based on non-public information.

“We imitate correspondence of the [CEO] with a certain insider who shares financial reports of his companies through which your victim allegedly trades in the stock market, which naturally is a criminal offense and — according to US federal laws [includes the possibility of up to] 20 years in prison,” one Venus member wrote to an underling.

“You need to create this file and inject into the machine(s) like this so that metadata would say that they were created on his computer,” they continued. “One of my clients did it, I don’t know how. In addition to pst, you need to decompose several files into different places, so that metadata says the files are native from a certain date and time rather than created yesterday on an unknown machine.”

Holden said it’s not easy to plant emails into an inbox, but it can be done with [Microsoft Outlook .pst files](https://support.microsoft.com/en-us/office/create-an-outlook-data-file-pst-to-save-your-information-17a13ca2-df52-48e8-b933-4c84c2aabe7c), which the attackers may also have access to if they’d already compromised a victim network.

“It’s not going to be forensically solid, but that’s not what they care about,” he said. “It still has the potential to be a huge scandal — at least for a while — when a victim is being threatened with the publication or release of these records.”

![](https://krebsonsecurity.com/wp-content/uploads/2022/12/venusransom.png)

The Venus ransom group’s extortion note. Image: Tripwire.com

Holden said the CLOP ransomware gang has a different problem of late: Not enough victims. The intercepted CLOP communication seen by KrebsOnSecurity shows the group bragged about twice having success infiltrating new victims in the healthcare industry by sending them infected files disguised as ultrasound images or other medical documents for a patient seeking a remote consultation.

The CLOP members said one tried-and-true method of infecting healthcare providers involved gathering healthcare insurance and payment data to use in submitting requests for a remote consultation on a patient who has cirrhosis of the liver.

“Basically, they’re counting on doctors or nurses reviewing the patient’s chart and scans just before the appointment,” Holden said. “They initially discussed going in with cardiovascular issues, but decided cirrhosis or fibrosis of the liver would be more likely to be diagnosable remotely from existing test results and scans.”

While CLOP as a money making collective is a fairly young organization, security experts say CLOP members hail from a group of Threat Actors (TA) known as “TA505,” which [MITRE’s ATT&CK database says](https://attack.mitre.org/groups/G0092/) is a financially motivated cybercrime group that has been active since at least 2014. “This group is known for frequently changing malware and driving global trends in criminal malware distribution,” MITRE assessed.

In April, 2021, KrebsOnSecurity detailed how CLOP helped pioneer another innovation aimed at pushing more victims into paying an extortion demand: [Emailing the ransomware victim’s customers and partners directly](https://krebsonsecurity.com/2021/04/ransom-gangs-emailing-victim-customers-for-leverage/) and warning that their data would be leaked to the dark web unless they can convince the victim firm to pay up.

Security firm **Tripwire** [points out](https://www.tripwire.com/state-of-security/healthcare-sector-warned-venus-ransomware-attacks) that the HHS advisory on Venus says multiple threat actor groups are likely distributing the Venus ransomware. Tripwire’s tips for all organizations on avoiding ransomware attacks include:

* Making secure offsite backups.
* Running up-to-date security solutions and ensuring that your computers are protected with the latest security patches against vulnerabilities.
* Using hard-to-crack unique passwords to protect sensitive data and accounts, as well as enabling multi-factor authentication.
* Encrypting sensitive data wherever possible.
* Continuously educating and informing staff about the risks and methods used by cybercriminals to launch attacks and steal data.

While the above tips are important and useful, one critical area of ransomware preparedness overlooked by too many organizations is the need to develop — and then periodically rehearse — a plan for how everyone in the organization should respond in the event of a ransomware or data ransom incident. Drilling this breach response plan is key because it helps expose weaknesses in those plans that could be exploited by the intruders.

As noted in last year’s story [Don’t Wanna Pay Ransom Gangs? Test Your Backups](https://krebsonsecurity.com/2021/07/dont-wanna-pay-ransom-gangs-test-your-backups/), experts say the biggest reason ransomware targets and/or their insurance providers still pay when they already have reliable backups of their systems and data is that nobody at the victim organization bothered to test in advance ...