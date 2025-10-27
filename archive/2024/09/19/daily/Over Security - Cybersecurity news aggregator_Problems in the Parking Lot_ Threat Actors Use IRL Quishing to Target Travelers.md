---
title: Problems in the Parking Lot: Threat Actors Use IRL Quishing to Target Travelers
url: https://www.netcraft.com/blog/irl-quishing-scams-target-travelers/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-19
fetch_date: 2025-10-06T18:27:48.052190
---

# Problems in the Parking Lot: Threat Actors Use IRL Quishing to Target Travelers

[**GUIDE:** The Total Economic Impactâ¢ of Netcraft Brand Protection | Download now â](../lp/forrester-tei-study)

[Pricing](../get-pricing)

[Contact Us](../contact)

[Report Fraud](https://report.netcraft.com/)

[Login](https://services.netcraft.com/)

Platform

Solutions

[Why Netcraft](../why-netcraft)

Resources

Company

[GET Demo](../book-a-demo)

[**GUIDE:** The Total Economic Impactâ¢ of Netcraft Brand Protection | Download now â](../lp/forrester-tei-study)

[**GUIDE:** The Total Economic Impactâ¢ of Netcraft Brand Protection | Download now â](../lp/forrester-tei-study)

[Pricing](../get-pricing)

[Contact Us](../contact)

[Report Fraud](https://report.netcraft.com/)

[Login](https://services.netcraft.com/)

Platform

Solutions

[Why Netcraft](../why-netcraft)

Resources

Company

[GET Demo](../book-a-demo)

[**GUIDE:** The Total Economic Impactâ¢ of Netcraft Brand Protection | Download now â](../lp/forrester-tei-study)

[## ALL POSTS](../resources/blog)

[## ALL POSTS](../resources/blog)

[## ALL POSTS](../resources/blog)

# Problems in the Parking Lot: Threat Actors Use IRL Quishing to Target Travelers

By

By

By

Sam Kitson

Sam Kitson

Sam Kitson

|

|

|

September 18, 2024

September 18, 2024

September 18, 2024

![](https://framerusercontent.com/images/jxxRGtMLzq6QxJ4GYRCCbx2QFQ.svg?width=27&height=28)

![](https://framerusercontent.com/images/qxE8AF5N0tvgi2NQPrJxo2Fjec8.svg?width=27&height=28)

![](https://framerusercontent.com/images/iPf6JKc4mxyBKQ0kzbQ3awaw.svg?width=27&height=28)

![Reddit logo](https://framerusercontent.com/images/SgQ1svDD2syGHlolx4eeBq0UPA.svg?width=28&height=29)

![](https://framerusercontent.com/images/u650vq1gBXhB8Cz6RG5UVcj3dQ.png?width=1424&height=718)

![](https://framerusercontent.com/images/u650vq1gBXhB8Cz6RG5UVcj3dQ.png?width=1424&height=718)

![](https://framerusercontent.com/images/u650vq1gBXhB8Cz6RG5UVcj3dQ.png?width=1424&height=718)

![](https://framerusercontent.com/images/u650vq1gBXhB8Cz6RG5UVcj3dQ.png?width=1424&height=718)

**This article explores Netcraftâs research into the recent surge in QR code parking scams in the UK. It also shows how parking payment provider PayByPhone is fighting back. Insights include:**

* At least two threat groups identified, one of which Netcraft can link to customs tax and postal scams carried out earlier this year.
* Up to 10,000 potential victims identified visiting this groupâs phishing websites between June 19 and August 23.
* At least 2,000 form submissions, indicating how much personal data has been extracted from victims, including payment information.
* Evidence suggesting the group is running activity across Europe, including France, Germany, Italy, and Switzerland.
* How PayByPhone is adapting its business model and working with leading brand protection and anti-phishing provider Netcraft to proactively tackle attacks and protect its customers.

## Introduction

Earlier this month, [RAC issued an alert](https://www.rac.co.uk/drive/news/motoring-news/be-qrareful-rac-warns-drivers-to-watch-out-for-parking-payment-scams/) for UK motorists to beware of threat actors utilizing Quick Response (QR) code stickers luring them to malicious websites. These sites are designed to exfiltrate personal data, including payment information, by impersonating known parking payment providers. Reports of similar scams across Europe and in Canada and the US have also been increasing and gaining public attention. In the US, the FBI has now issued alert number [I-011822-PSA](https://www.ic3.gov/Media/Y2022/PSA220118), *Cybercriminals Tampering with QR Codes to Steal Victim Funds*, to raise awareness. We can expect that these attacks will continue to be deployed on a global scale.

In the UK, phishing activity is peaking. On July 30, Southampton City Council posted on Facebook warning motorists of a wave of malicious QR codes appearing across the city center. Printed on adhesive stickers and affixed to parking meters, the QR codes directed users to phishing websites impersonating the parking payment app brand PayByPhone. Around the same time, several Netcraft staff shared stories of family members being duped by similar scams. In response, Netcraft deployed its research teams to analyze and understand the activity in depth.

![](https://framerusercontent.com/images/1JJD9oQXbllYrZgACJgpxQNrLM.png?width=338&height=512)

*Fig. 1. Southampton City Councilâs post on Facebook warning users to avoid scanning the QR codes and explaining the risk.*

Looking at British media reports, these parking QR code scams appeared to peak during the summer holiday period (June to September). Activity concentrated in and around coastal tourism locations such as Blackpool, Brighton, Portsmouth, Southampton, Conwy, and Aberdeen. There are now at least 30 parking apps in the UK, varying by locationâan abundance that benefits criminals. By targeting tourist destinations, threat actors can prey on tourists who need to download the parking payment apps and are searching for ways to do so.

Netcraft was able to identify two threat groups running such scams. This report focuses on an active group impersonating the PayByPhone brand. The other group has been identified using a phishing kit to simulate multiple brands, including RingGo.

## How do Parking QR Code Scams work?

Mobile payments are now standard in many public and private parking lots across the world. While transactions were once used to involve calling or texting a number, mobile apps have become more commonplace.

In the UK, the main providers include PayByPhone, RingGo, JustPark, ParkMobile, and MiPermit. Providers display user instructions in parking lots, typically on parking meters. These include a download link or QR code to access the payment app, as well as a unique location code to geolocate the user. This approach not only offers an opportunity for threat actors to target victims on-site, it may also enable them to further target victims with additional location-specific malicious messages.

### Step-by-step process

Based on the PayByPhone threat group which forms the basis of the research, the following step-by-step process being used to extract victim data was observed:

1. Threat actor acquires and deploys âboots on the groundâ resources to set up the attack.
2. Malicious QR codes are affixed to parking lot payment machines.
3. A victim visiting that parking lot scans the malicious QR code and is directed to a mobile phishing website mimicking a legitimate parking lot payment provider.
4. The phishing website prompts the victim to enter the following details in this order:
5. Their 6-digit parking lot location code.
6. Vehicle details, including license plate and vehicle type
7. Parking duration
8. Payment card details
9. The website then displays a fake âProcessingâ page, simulating a familiar user experience. In some cases, a 3D secure code will be prompted from the victimâs bank/card provider.
10. The victim is redirected to a âPayment accepted!â page.
11. The phishing website confirms the victimâs entered details.
12. The victim is directed to the official PayByPhone website.

![](https://framerusercontent.com/images/SfqyDwQwresB7crsqBcDYSJkVz4.png?width=347&height=751)![](https://framerusercontent.com/images/F3ie0lY8BQ0jr6RiaAVf3he30.png?width=347&height=751)![](https://framerusercontent.com/images/s5AfvSiRhM0yshfkZ9ES70H81U.png?width=347&height=751)![](https://framerusercontent.com/images/wYYp25QPrnRwtVUKnhcm18zsS2E.png?width=347&height=751)![](https://framerusercontent.com/images/mE9nGgkNHN9iC5i0bZPxJXVUbc.png?width=347&height=751)![](https://framerusercontent.com/images/mP7DjomuitMqrd1xaGEZRLZmvAk.png?width=347&height=751)

*Fig. 2. Screenshots showing the step-by-step process on one of the fake PayByPhone websites.*

Following payment, phishing kit groups send the victim to a failed payment page, prompting them to use an alternative payment card. This extends the volume of credentials a...