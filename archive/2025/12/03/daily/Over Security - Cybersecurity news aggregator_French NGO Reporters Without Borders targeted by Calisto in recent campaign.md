---
title: French NGO Reporters Without Borders targeted by Calisto in recent campaign
url: https://blog.sekoia.io/ngo-reporters-without-borders-targeted-by-calisto-in-recent-campaign/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-03
fetch_date: 2025-12-04T03:19:11.725733
---

# French NGO Reporters Without Borders targeted by Calisto in recent campaign

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# French NGO Reporters Without Borders targeted by Calisto in recent campaign

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR](#molongui-disabled-link)
December 3 2025

0

9 minutes reading

*Some portions of this article were first distributed as a private report to our customers in June 2025.*

In May and June 2025, TDR team analysts were contacted by two organisations — including the French NGO **Reporters Without Borders (RSF)** — over suspicions of a new spear phishing attempts by the intrusion set **Calisto** (also known as **ColdRiver** or **Star Blizzard**).

Calistois a Russia-nexus intrusion set active since at least April 2017, attributed by the USA, the UK, New Zealand and Australia to the Russian intelligence service **FSB**, more specifically to the **Center 18 for Information Security** (TsIB), [military unit 64829](https://www.gov.uk/government/publications/russias-fsb-malign-cyber-activity-factsheet/russias-fsb-malign-activity-factsheet), also known to operate the intrusion set Gamaredon. Sekoia.io concurs with such attribution as past Calisto operations investigated by TDR analyst [showed](https://blog.sekoia.io/calisto-show-interests-into-entities-involved-in-ukraine-war-support/) objectives and victimology that align closely with Russian strategic interests.

Calisto mainly conducts **cyber espionage operations**, targeting Western countries, especially Eastern European countries and any countries supporting Ukraine. The group was observed carrying out phishing campaigns aiming at credential theft and code execution using recently the [ClickFix technique](https://attack.mitre.org/techniques/T1204/004/), targeting **military and strategic research** sectors such as NATO entities and a Ukraine-based defense contractor, as well as **NGOs and think tanks**. Additional victimology includes former intelligence officials, experts in Russian matters, and Russian citizens abroad.

Calisto spear-phishing campaigns often involve the **impersonation of trusted contacts**, sending email either **forgetting the attachment**, or sending a dysfunctional yet benign PDF file, in order to trigger a response for the victim asking for a resend. We assess this technique is likely to increase the credibility of the exchange.

TDR analysts have been following Calisto TTPs and their C2 infrastructure tactics since 2022. We have published in 2022 an [investigation](https://blog.sekoia.io/calisto-show-interests-into-entities-involved-in-ukraine-war-support/) showing that this group conducts intelligence collection activities targeting parties involved in Ukraine support, especially those in the tactical equipment logistics, probably to contribute to Russian efforts to disrupt Kiev supply-chain for military reinforcements.

Later, in 2023, we [published](https://blog.sekoia.io/calisto-doxxing-sekoia-io-findings-concurs-to-reuters-investigation-on-fsb-related-andrey-korinets/) a follow-up investigation focusing on Andrei Korinets, a Russian individual whose name was [disclosed](https://www.reuters.com/world/europe/russian-hackers-targeted-us-nuclear-scientists-2023-01-06/) by Reuters, who was likely registering phishing domains used previously by Calisto to conduct at least a phishing campaign targeting UK entities, including the British Parliament.

## **Reporters Without Borders targeting**

On march 2025, TDR was contacted by the NGO **Reporters Without Borders** regarding a strange phishing email receveid by one of its core member. Reporters Without Borders is an international non-profit organisation that defends press freedom worldwide. It monitors violations against journalists, provides support to reporters under threat, and advocates for free, independent, and pluralistic media. The organisation, which has assisted Russian journalists in fleeing the country, has been [designated an “undesirable organisation” in Russia in august 2025](https://rsf.org/fr/rsf-class%C3%A9e-organisation-ind%C3%A9sirable-en-russie-ou-le-droit-%C3%A0-l-information-consid%C3%A9r%C3%A9-comme-une).

As usual for Calisto, **the phishing email came from a ProtonMail address made to look like a trusted contact**. It asked the recipient to review a document, but no document was attached. This tactic, seen before in the Calisto credential-harvesting campaign, is meant to make the recipient ask for the missing file. The attacker can then send a “follow-up” document that contains the malicious payload.

Here is the email sent by the Calisto operator. As shown in the screenshot, the message is written in French and includes the proper signature of the trusted contact, but **the link to the PDF at the end of the document is not active**.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/11/phishing1-scaled.png)

After the victim requested the document, the Calisto operator responded with another email — this time in English — containing **a link to a previously compromised website**, as shown below. The site acted as a **redirector** to a ProtonDrive URL that likely presented a malicious PDF to the user. However, the file itself could not be retrieved because ProtonMail had blocked the operator’s account. It is worth mentioning that Proton Security is very cooperative regarding this kind of spear phishing operations that impersonate real persons belonging to NGOs.

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/11/phishing2-scaled.png)

## Other targeting

We came aware of a second case against a second victim. This time, **the attacker did attach a file labeled as a PDF**. However, it was in fact a ZIP archive with a .pdf extension. Although not malicious, the file could not be opened as a PDF, furthering the deception of the victim.

Our contact was...