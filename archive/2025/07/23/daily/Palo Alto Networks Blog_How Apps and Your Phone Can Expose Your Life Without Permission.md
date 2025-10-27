---
title: How Apps and Your Phone Can Expose Your Life Without Permission
url: https://www.paloaltonetworks.com/blog/2025/07/apps-and-your-phone-expose-your-life/
source: Palo Alto Networks Blog
date: 2025-07-23
fetch_date: 2025-10-06T23:55:27.588279
---

# How Apps and Your Phone Can Expose Your Life Without Permission

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [Interview](https://www.paloaltonetworks.com/blog/category/interview/)
* How Apps and Your Phone C...

# How Apps and Your Phone Can Expose Your Life Without Permission

Link copied

By [Dena De Angelo](/blog/author/ddeangelo/ "Posts by Dena De Angelo")

Jul 22, 2025

8 minutes

[Interview](/blog/category/interview/)

[Must-Read Articles](/blog/security-operations/category/must-read-articles/)

[Points of View](/blog/category/points-of-view/)

[Use-Cases](/blog/security-operations/category/use-cases/)

[exposure management](/blog/tag/exposure-management/)

[IoT devices](/blog/tag/iot-devices/)

Health and Human Services Secretary Robert F. Kennedy Jr. [recently announced](https://www.reuters.com/business/healthcare-pharmaceuticals/us-health-secretary-kennedy-says-hhs-launch-campaign-encourage-wearable-devices-2025-06-24/) that he wants “every American wearing a health monitoring device within four years.” His department plans to launch "one of the biggest campaigns in HHS history" to promote wearables as affordable alternatives to expensive medications. While the health benefits may seem appealing, this federal push toward ubiquitous biometric monitoring highlights a broader digital privacy crisis that cybersecurity practitioners witness daily – the systematic erosion of personal data protection across all connected devices and services.

Kennedy's wearables initiative represents just the latest example of how convenience-focused technology adoption often overlooks fundamental privacy implications. The real security challenge extends far beyond fitness trackers to encompass the entire ecosystem of apps, services and [IoT](/cyberpedia/what-is-iot-security) devices that modern consumers use without understanding the data exposure risks they create.

## **Your Phone Number Unlocks (Nearly) Everything**

Privacy expert [Arjun Bhatnagar](https://www.linkedin.com/in/arjunbhatnagar/), CEO of [Cloaked](https://www.cloaked.com/), discovered something alarming while building an AI system to analyze his personal health data. In a [recent interview on the Threat Vector podcast](https://thecyberwire.com/podcasts/threat-vector/70/notes) with host David Moulton, Bhatnagar demonstrated how a single, seemingly harmless data point can expose comprehensive personal profiles.

As Bhatnagar explains, "a single data point, for example, your phone number can leak everything about you. Your email address, your family members, your social security number, your credit card, your passwords can all be found from just one data point."

The problem stems from how companies treat data collection. Bhatnagar describes the issue: "We give the same information to the IRS that we give to Domino’s® pizza. That phone number, for example, can easily tie your entire digital life, your family's life, everyone you’re connected to with just one data point."

When companies suffer data breaches, the exposure often exceeds user expectations. Bhatnagar recounts discovering a parking app breach notification that revealed comprehensive personal information while emphasizing that passwords remained secure. The exposed data included names, addresses, license plate numbers, vehicle details, personal interests, birthdays and behavioral patterns — far more information than users expected when they simply wanted to pay for parking.

Curious to understand how data breaches, data brokers and general sharing may have exposed your personal information? Bhatnagar offers a safe and secure way to know your risk by calling 855-752-5625.

## **Permission Creep and Default Surveillance**

Most users approach app permissions backwards. They default to accepting everything and only restrict access when problems occur. Bhatnagar advocates a different strategy:

> Start with 'No.' Use the app and give selective permissions as you use it.

This approach reveals how many apps request far more access than their core functionality requires. Bhatnagar uses TikTok as an example. He shares that no matter how much TikTok asks for access to his contacts, he continues to say *no*.

When users do grant permissions, Bhatnagar recommends avoiding "allow all" options: "when you're using a permission, I recommend that you don't choose ‘allow all’, do allow ‘selective’ and pick and choose what you want to share with an app or a website you're using."

That being said, security practitioners should educate users:

* Review app permissions quarterly and revoking unnecessary access.
* Use device-level restrictions to prevent apps from accessing sensitive data.
* Create separate email addresses for different service categories.

## **Public Wi-Fi Creates Attack Opportunities**

Coffee shops and airports offer convenient internet access, but public Wi-Fi networks create significant security exposures. Bhatnagar explains the fundamental vulnerability: "When you are on any Wi-Fi network, whether it's going through a password or not, all of your internet's traffic is flowing over that router so an admin or other computers in the network can snoop and watch that traffic."

What’s more concerning is how attackers often create fake networks. As Bhatnagar warns, "people often will spoof Wi-Fi networks.... It might look like Google because you're on somebody else's router, but when you type in login information, it'll fail. And you've now given up your password, your email address, everything."

*Anyone* using public Wi-Fi should follow these essential safety protocols:

* Verify network names with venue staff before connecting.
* Avoid accessing sensitive accounts on public networks.
* Use cellular data for critical transactions when possible.

## **Social Media's Permanent Record Problem**

Everything users post online becomes permanent, searchable and potentially weaponized against them. Bhatnagar emphasizes this persistence:

> Everything that we're putting out there lives forever. And now when we put it out there, people are using it to train AI models and it's being aggregated.

Users often focus on privacy settings while overlooking how their data contributes to broader algorithmic systems. As Bhatnagar notes, "everybody wants you to share more. We want to be careful because we do not know how that information comes back to target, attack or be used to infer things about us."

Bhatnagar recommends conscious evaluation before posting: "At least being conscious before you're posting is a very big win... and knowing that this information will be used even with privacy settings in place – some way or another. So starting there and then actually not posting something if you realize it shouldn’t be out there."

## **The Retargeting Surveillance Economy**

Users frequently experience "creepy" advertising where products they viewed online appear in ads across different websites and apps. Bhatnagar explains how this tracking actually works: "You are being retargeted and tracked based on inputs that you provide. If you tap an ad or you tap a piece of content, they're tracking that. But, it could also be that you are in the vicinity of other people who did the same thing."

The tracking mechanisms extend beyond individual behavior to proximity-based profiling. Companies connect users through shared IP addresses, contact lists and location data. When users click promotional offers, they often provide information that becomes permanent tracking identifiers.

Bhatnagar warns against this practice: "Don't put your phone number or email on that free $10 promotion coupon. That's how they find you everywhere else. And they keep retargeting you because you gave them the one piece of data they need to find you anywhere."

He recommends "data poisoning" strategies to disrupt tracking:

* Use outdated addresses when signing up for promotional offers.
* Avoid clicking ads directly. Search for products independently instead.
* Use browsers ...