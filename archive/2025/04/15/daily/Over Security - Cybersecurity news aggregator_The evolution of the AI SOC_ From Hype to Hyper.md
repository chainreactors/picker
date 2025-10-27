---
title: The evolution of the AI SOC: From Hype to Hyper
url: https://blog.sekoia.io/agentic-ai-in-soc-operations/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-15
fetch_date: 2025-10-06T22:08:38.287690
---

# The evolution of the AI SOC: From Hype to Hyper

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

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

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

[SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/ "SOC Insights & Other News")

# The evolution of the AI SOC: From Hype to Hyper

[![](data:image/svg+xml...)![](https://secure.gravatar.com/avatar/28c7f8195a566b04453ac6788eb103d6eb119e36e8d17886f6057379433ab6b0?s=52&d=mm&r=g)](#molongui-disabled-link)

[David Greenwood](#molongui-disabled-link)
April 14 2025

0

7 minutes reading

## Table of contents

* [Perception AI](#h-perception-ai)
* [Security Co-pilots](#h-security-co-pilots)
* [Agentic AI](#h-agentic-ai)
  + [Alert Triage Agent](#h-alert-triage-agent)
  + [Response Agent](#h-response-agent)
* [Physical AI](#h-physical-ai)

At CES in January 2025, Nvidia CEO Jenson Huang stood before the audience and described the direction of travel in Artificial Intelligence;

![Graph showing the evolution of AI in SOCs from Perception to Generative, Agentic, and Physical AI, highlighting anomaly detection, co-pilots, and augmented SOCs](data:image/svg+xml...)![Graph showing the evolution of AI in SOCs from Perception to Generative, Agentic, and Physical AI, highlighting anomaly detection, co-pilots, and augmented SOCs](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/04/PXL_20250408_105525555-1024x771.jpg)

* **Perception AI** helps us to understand text, speech, and images
* **Generative AI** helps us to generate text, speech, pictures, and videos
* **Agentic AI** can perceive, reason, plan, and act
* **Physical AI** can interact with the physical world

The Sekoia platform has always been at the bleeding edge of each AI wave, empowering SOC teams to be more efficient.

Often, as time passes, we forget just how quickly technology changes both our daily and working lives. As we enter the Agentic AI era, I wanted to take a reflective look at how the various waves of AI have changed how SOC teams work.

## Perception AI

By extracting meaning from raw data, Perception AI allows computers to interpret and label the world around us.

It’s very likely you use perception AI in your personal life everyday, from speech recognition assistants like Apple’s Siri or Amazon Alexa, or image recognition such as in Apple Photos or Google images.

Inside the AI SOC, Perception AI plays a significant role by enhancing the detection, analysis, and response to security threats.

### Anomaly Detection

In the fledgling days of SIEM, detection rules were very simple. For example, looking for error codes or warning messages.

Time-to-detection was, and still remains one of the key metrics a lot of SOC teams measure. Anomaly detection was introduced in the first generation of AI SOCs, and delivered the first significant leap in enhancing the ability to surface security incidents in data lakes.

Using machine learning models, a baseline for normal network activity can be established. Perception AI can then identify deviations from this baseline, flagging potential security threats or unusual activities for further investigation.

To illustrate a real example, the following graph taken from the Sekoia platform shows the output of an anomaly detection rule that monitors the volume of services installed a systems, indicative of potential malicious activity, perhaps malware or the installation of benign tools to help exfiltrate data.

![Visualization graph from Sekoia.io detecting abnormal volume of 4697 Windows events with high anomaly scores across multiple time intervals](data:image/svg+xml...)![Visualization graph from Sekoia.io detecting abnormal volume of 4697 Windows events with high anomaly scores across multiple time intervals](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/04/172631385-a6054d11-3b42-45ff-b4ca-7f98b3a1ec9e-1024x356.png)

[You can read more about Anomaly Detection rule in the Sekoia platform here.](https://docs.sekoia.io/xdr/features/detect/anomaly/)

### Event Correlation

Detecting anomalous activity is useful. Understanding what happened in relation to the anomalous activity makes triaging much more effective.

To develop the previous example further, this could include considering other events related to an installation of services, for example, escalating a user’s privileges.

Event correlation allows SOC teams to observe the context of an event, or put another way, the big picture of an incident. This alone has made significant strides in reducing the volume of benign alerts that once overwhelmed SOC teams.

Perception AI has proved a game changer to the SOC in this regard because of the scale at which it can operate. It can link seemingly disparate events across vast and complex IT environments, where terabytes of generated data is now the norm.

One really cool example I’ve seen employed here is using Perception AI to track an actor inside a network and respond accordingly.

![SOC dashboard showing a potential MuddyWater cyber intrusion detected by Sekoia.io platform with alerts, attack storyline, and incident context](data:image/svg+xml...)![SOC dashboard showing a potential MuddyWater cyber intrusion detected by Sekoia.io platform with alerts, attack storyline, and incident context](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/04/Potential-MuddyWater-Intrusion-via-Microsoft-Office-Product-DNS-Tunnel-Technique-Cases-Sekoia-io-04-08-2025_12_01_PM-1024x610.png)

[You can read more about the Cases in the Sekoia platform here.](https://docs.sekoia.io/xdr/features/investigate/ai_cases/)

Ultimately being able to understand what has been done, what is currently underway, and therefore what might happen next at massive scale, has addressed another key SOC metric, time to resolution.

## Generative AI

Generative AI, hallmarked by the arrival of ChatGPT in November 2022, followed by a host of other AI tools across image, voice and video.

When people talk about AI today, it is likely they are referring to Generative AI. Generative AI refers to systems that create new conte...