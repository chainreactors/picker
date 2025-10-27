---
title: Discovering Your Baud
url: https://trustedsec.com/blog/discovering-your-baud
source: TrustedSec
date: 2025-04-18
fetch_date: 2025-10-06T22:06:01.024161
---

# Discovering Your Baud

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Discovering Your Baud](https://trustedsec.com/blog/discovering-your-baud)

April 17, 2025

# Discovering Your Baud

Written by
Brian Berg

Hardware Security Assessment
IoT Security Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/DiscoveringYourBaud_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1744662266&s=09021ab524fad2541f8b5399fa308fa2)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#d0efa3a5b2bab5b3a4ed93b8b5b3bbf5e2e0bfa5a4f5e2e0a4b8b9a3f5e2e0b1a2a4b9b3bcb5f5e2e0b6a2bfbdf5e2e084a2a5a3a4b5b483b5b3f5e2e1f6b1bda0ebb2bfb4a9ed94b9a3b3bfa6b5a2b9beb7f5e2e089bfa5a2f5e2e092b1a5b4f5e391f5e2e0b8a4a4a0a3f5e391f5e296f5e296a4a2a5a3a4b5b4a3b5b3feb3bfbdf5e296b2bcbfb7f5e296b4b9a3b3bfa6b5a2b9beb7fda9bfa5a2fdb2b1a5b4 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdiscovering-your-baud "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Discovering%20Your%20Baud%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdiscovering-your-baud "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdiscovering-your-baud&mini=true "Share on LinkedIn")

I'm still pretty new to hardware hacking and find myself going through a lot of media (both text and moving pictures) about various techniques to interact with IoT devices and hardware in general. One of the tasks for a hardware assessment is attempting to get access to the device's firmware either through a debug interface, such as UART, or possibly removing the flash chip and extracting the firmware with additional hardware. Since leaving the flash chip on the device is a little less risky than blasting a PCB with hot air, finding a debug interface that offers an interactive terminal is a good place to start.

Once a [UART](https://trustedsec.com/blog/hardware-hacking-plunder-with-a-bus-pirate) interface is found, you will have to connect a device to interact with it, but you need to know the baud rate in order for the information to display properly.  If you were unaware, baud rate is basically another way of saying "bits per second." At this point, most blog posts or videos suggest using 115200, as this is the most common data rate based on their experience, but if that doesn’t work, try all of the other common baud rates (4800, 9600, 19200, 38400, 57600, 230400, 460800, 921600). "Just try everything" never really sat well with me, so I decided to do a little poking around the information superhighway to try and find some better resources.

The easiest way to measure the baud rate is with a logic analyzer or oscilloscope. Since a logic analyzer has more utility for my purposes, I picked up a relatively affordable device off Amazon—the DSLogic Plus. If you just intend to dip your toes in the water of hardware assessment and want to follow along with this post, you can get a cheaper logic analyzer for under $20. Even these devices have a high enough sample rate to get a good idea of what the baud rate should be.

Before I get too far ahead of myself, I should mention that the sample rate should be at least double the frequency of the target baud rate—in practice, four (4) times the target rate is recommended. The highest common baud rate is 921600, and doubling that brings the sample rate just shy of 2 MHz. Again, this is something that even a cheap logic analyzer should be able to handle. Try not to go too crazy on the sample rate if the captures are being stored to disk since they can chew through disk space fairly quickly if data is being captured for a long period of time.

Now we can attach logic analyzer probes to the target device's TX pin, set our sample rate to 2 MHz or higher, begin a capture, and power on the device.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/Baud_Berg/Fig1_Berg_Baud.png?w=320&q=90&auto=format&fit=max&dm=1744743360&s=a3c696ecf04cc231655599360259df9c)

Partial Output of Capture

After zooming in on one of the chunks of data, look for the shortest transition period, which we are assuming to be 1 bit. Using DSLogic's DSView, we're able to see the width of each bit. To turn this into a baud rate, divide 1 by the width. This results in a baud rate that's just a few bits off one of the common rate of 115200.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/Baud_Berg/Fig2_Berg_Baud.png?w=320&q=90&auto=format&fit=max&dm=1744743361&s=5e15fb7b6b00f3a001a72b4906f77c53)

Bit Measurement

![](https://trusted-sec.transforms.svdcdn.com/produ...