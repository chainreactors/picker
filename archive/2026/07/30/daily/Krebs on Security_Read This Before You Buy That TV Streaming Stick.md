---
title: Read This Before You Buy That TV Streaming Stick
url: https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/
source: Krebs on Security
date: 2026-07-30
fetch_date: 2026-07-31T05:31:41.825041
---

# Read This Before You Buy That TV Streaming Stick

Advertisement

[![](/b-flashpoint/1.png)](https://flashpoint.io/ignite/vulnerability-intelligence/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=brand-vuln&utm_content=vuln-a)

Advertisement

[![](/b-cape/2.jpg)](https://www.cape.co/?utm_source=Krebs&utm_medium=Banner&utm_campaign=Krebs_Display_Footer_Mobile)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Read This Before You Buy That TV Streaming Stick

July 30, 2026

[20 Comments](https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick/#comments)

Security experts have been sounding the alarm for years about the risks of using generic TV boxes that promise unlimited content streaming for a one-time fee, warning that they secretly rent the user’s Internet connection out to strangers. But a groundbreaking new analysis finds these devices also routinely spoof themselves as mobile phones clicking ads on AI-generated websites as part of a sprawling operation that seeks to defraud online merchants and advertising networks.

**Pedro Falé** is a threat researcher with the security firm **Bitsight**. Falé told KrebsOnSecurity he was able to peer inside a vast and complex ad fraud network by registering an expired domain name that was used to coordinate fake ad clicks across a particularly popular brand of these streaming devices known as **H96**.

![](https://krebsonsecurity.com/wp-content/uploads/2026/07/h96-amazon.png)

An H96 TV streaming device currently advertised for sale on Amazon.

Falé said the domain he scooped up was previously used for telemetry, periodically collecting full hardware information and the entire list of installed apps from tens of thousands of H96 streaming sticks plugged into television sets around the globe. But upon inspecting the traffic being funneled to the domain, he discovered nearly all of the TV boxes transmitting data claimed to be mobile phone models from a variety of manufacturers, including Samsung, Vivo, Huawei, and Xiaomi.

“We noticed something was wildly wrong,” Falé said. “Multiple devices reporting to this factory Android TV Box backdoor were ‘phones.'”

![](https://krebsonsecurity.com/wp-content/uploads/2026/07/h96-shipspreinfected.png)

Image: Bitsight.

The researcher found all of the devices reported having the same two apps installed, and that those apps were made by a company called **Zhejiang Fengwo IoT Technology Ltd**, an entity founded in 2019 in mainland China which operates an ad-publishing portfolio under the name **Fengwo Group**. Further investigation into the Fengwo Group revealed it has registered multiple patents that match the inner workings of these apps.

“Bitsight TRACE identified several Hong Kong, Singapore, and single person ‘legal’ shell identities used to collect the monetization and traced the operation back to a mainland China company known as Zhejiang Fengwo IoT Technology Co., Ltd, which operates under the Fengwo Group,” Falé [wrote](https://www.bitsight.com/blog/fuyao-enterprise-building-ad-fraud-empire-ai-and-kids-coding-blocks) in a report released today about their findings.

Falé said an analysis of the apps shows they help to coordinate an ad fraud network that uses these H96 devices as a captive traffic source to click on ads at AI-generated websites operated by the Fengwo Group.

Bitsight discovered the websites contain machine-generated news articles and graphics across a range of categories, including finance, health, education, gaming, music and food blogs. But they also found none of those sites displayed ads unless the device visiting the page matched the spoofed mobile profile of these H96 devices.

## AI DIGITAL HUMANS

The domain for the Fengwo Group — fwgcloud[.]com — claims the company is “redefining the boundaries of human-AI interaction,” and that it has created more than 120,000 “AI digital humans” available to rent for everything from emotional companionship to 24/7 customer service and creative design.

![](https://krebsonsecurity.com/wp-content/uploads/2026/07/fwgcloud-dot-com.png)

The homepage for fwgcloud dot com.

Falé said the Fengwo Group’s domain shared its SSL certificate data with other domains associated with the apps found on H96 devices, specifically the phone spoofing mechanism. He noted the domain also has an internal wiki platform that directly ties the Fengwo Group to a proprietary implementation of a Google-built visual programming language called **Blockly**, which was originally designed to help kids learn how to write software.

According to Bitsight, the Fengwo Group’s employees use Blockly to build the sham websites, allowing low-skilled operators to drag blocks of code together in their Blockly editor — without any need to understand what the underlying code blocks do or how they work.

![](https://krebsonsecurity.com/wp-content/uploads/2026/07/tryblockly.png)

The Blockly homepage.

“An operator can drag blocks together in their Blockly editor, to define each fraud routine, given a task type,” reads Bitsight’s report. “Once the routine is saved, it gets exported as JavaScript and uploaded to the S3 buckets. An operator doesn’t need as much understanding of the underlying technicalities, as it is all set in place for ease of use.”

Bitsight even found one of the Fengwo Group app developers mentioning exactly these advantages, noting the developer remarked that “only a small number of highly-skilled developers are needed to build the template execution-unit images,” and that “developers who create execution units from those templates have significantly lower technical requirements, greatly reducing the company’s operating costs.”

Falé said if a user’s H96 streaming stick is selected for a specific fraud task, it will be pushed the appropriate Blockly module according to the task desired, which can include silently launching a web browser, visiting websites, browsing pages, managing tabs, and clicking on ads.

To ensure the TV boxes masquerading as mobile phones can reliably click on ads displayed via the AI-generated websites, the Fengwo group “fuses three vision and reasoning systems into a single interface,” allowing the bots to correctly identify an ad on the webpage and navigate the site much like a human would, the Bitsight report observed.

![](https://krebsonsecurity.com/wp-content/uploads/2026/07/fengwogroupwebsites.png)

Examples of ad landing pages linked to the Fengwo Group. Image: Bitsight.

## TV ON? PROXY. TV OFF? AD FRAUD

Bitsight found the H96 devices were either relaying residential proxy traffic or participating in ad fraud, but never both at the same time. In fact, they concluded that when these TV boxes detect an HDMI signal from an attached television — indicating the user intends to stream video content — the box is usually functioning as a residential proxy. When the TV is off, it switches back to waiting for ad fraud jobs.

Falé said he believes the TV boxes are set up this way because its ad fraud activities are far more resource intensive and could interfere with the device’s stated purpose — streaming video content over the Internet.

Despite repeated [warnings from the FBI](https://www.fbi.gov/investigate/cyber/alerts/2025/home-internet-connected-devices-facilitate-criminal-activity) and security industry leaders about the security and privacy risks of using these streaming devices, major e-commerce providers like Amazon, Best Buy, Newegg and others continue to sell hundreds of different models and brands that bundle unofficial versions of Google’s Android operating system and are frequently marketed ([via online influencers](https://krebsonsecurity.com/2025/11/is-your-android-tv-streaming-box-part-of-a-botnet/...