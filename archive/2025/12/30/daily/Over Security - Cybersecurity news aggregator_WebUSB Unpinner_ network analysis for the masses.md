---
title: WebUSB Unpinner: network analysis for the masses
url: https://reversing.works/posts/2025/12/webusb-unpinner-network-analysis-for-the-masses/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-30
fetch_date: 2025-12-31T03:25:26.848225
---

# WebUSB Unpinner: network analysis for the masses

[>

$ cd /evidence/](/)

* [About](/about/)
* [Connect with us](https://fossil-milk-962.notion.site/13c5e1c20ecd80c59b7cc8ad3405ff75)
* [Posts](/posts/)

5 minutes

# [WebUSB Unpinner: network analysis for the masses](https://reversing.works/posts/2025/12/webusb-unpinner-network-analysis-for-the-masses/)

In this blog post we will introduce **WebUSB Unpinner,** an open-source Web application that makes Android network analysis more accessible by leveraging WebUSB.

We will explain how to bootstrap the application, which kind of security measures it can bypass and how to better understand its components to benefit as much as possible from this tool.

One of the key aspects of WebUSB Unpinner is that it does not require to install any additional tool on the user premises, or to compromise the security of the user device, and it does not require any previous knowledge of Android reverse engineering techniques to be used at its best.

Have you ever wondered what does pesky apps are actually doing on you phone? Read along, we will help you along the journey!

## Rationale

At [reversing.works](http://reversing.works) we are committed to create a legal and technical framework that can empower labour unions and workers councils to effectively counter digital surveillance in the workplace.

In our most successful case, we showed how Glovo used its courier delivery application to monitor workers outside of working hours, and how this data was shared with third party trackers.
According to the Italian Data Protection Authority, this represented a serious violation of both the General Data Protection Regulation (GDPR) and of the Italian labour law, and resulted in a [5 milion euro fine to the company.](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10074840)

In collaboration with the European Trade Union Institute (ETUI), we published a [research paper](https://www.etui.org/publications/exercising-workers-rights-algorithmic-management-systems) that explains the methodology that sustains our analysis, with an emphasis on the technical tools and the reversing techniques required to replicate a similar case.

We are currently working with several partners all across Europe, and we also have received a generous grant from the [European AI & Society Fund](https://europeanaifund.org/newspublications/15-new-grantees-to-hold-governments-employers-and-tech-companies-accountable-for-ai-harms-in-europe/) to continue our work, but we realized that still our resources are limited, and that the time to organize a workshop can become a cumbersome constraint. On the other hand, other organizations could be interested to conduct the same analysis on their own.

Hoping to make this subject more accessible, we decided to build a standalone tool that can replicate the same reverse engineering workflow as detailed in the Annexes section of the ETUI paper, with an emphasis on network analysis.

## WebUSB Unpinner

We are pleased to announce [WebUSB Unpinner](https://github.com/fisiognomico/webusb-unpinner), a web application that relies on WebUSB to instrument an app installed on an Android device.
The requirements to use this application are the following:

* A Chromium-based browser (e.g. Chrome 88+).
* An Android device with [ADB enabled](https://developer.android.com/tools/adb#Enabling).
* A running instance of an HTTPS proxy ([mitmproxy](https://www.mitmproxy.org/), [HTTPToolkit](https://httptoolkit.com/), Burp Suite etc.).

We do not assume that any tool is installed on the user device besides those listed above.
If you would like to run your own local instance of WebUSB Unpinner you can simply:

* Clone the repository `git clone [https://github.com/fisiognomico/webusb-unpinner](https://github.com/fisiognomico/webusb-unpinner)`.
* Install the dependencies `npm install`.
* Serve the application with webpack `npx webpack serve`.

And thatâs it! All the code runs locally on the userâs browser, so no external tool needs to be configured.

Then in order to launch and instrument a target application, you need to:

* Launch the HTTPS proxy, ensure that it can be reached by your Android phone.
* In the top panel click `Connect Device`, give authorization to your browser and select the connected device.
* Configure the IP, Port and SSL certificate of the Proxy (with mitmproxy configured you can visit [mitm.it](http://mitm.it) to download the certificate) in `Proxy Configuration`.
* When the device is ready, you can either drop an APK (or all of them in case of split APKs) or instrument an already installed app, as shown in the list.
* Enjoy traffic interception!

The five steps above are detailed in the video below, in which we use the application [Android SSL Pinning Demo](https://github.com/httptoolkit/android-ssl-pinning-demo/), developed by the HTTPToolkit team, to show how it works.

[

Your browser does not support the video tag.
](/video/demo.mp4)

## What we are looking for

WebUSB unpinner is in beta release, and we are interested to hear stories from people using it! We are interested in particular to receive feedback on its stability and usability from a broad audience, as it might still lack the real world tests done by a wider user pool.
In general every Android application implements its security mechanisms, and most of them are already packaged in third party libraries. This tool is already able to bypass some of them, but not all.

In case you encounter issues with an app, or would like to have some help from us, donât hesitate to let us know! [You can reach out via our submission form](https://www.notion.so/13c5e1c20ecd80c59b7cc8ad3405ff75?pvs=21).

## Conclusion

Mobile app reversing can be a tedious subject, and due to the technical expertise required to enter the field many civil society actors have forgone it for a long time.

At [reversing.works](http://reversing.works/about) we think that itâs a crucial topic in the fight against digital surveillance, and with the proliferation of mobile applications that mediate work relations, the capability to inspect them must be accessible to a non-expert audience.

This tool lowers the entrance barrier and is another step forward in the democratization of this topic, we hope that you will make great use of it!

---

[reversing.works](https://reversing.works/tags/reversing.works/)
[technical update](https://reversing.works/tags/technical-update/)

855 Words

2025-12-22 00:00

---

[Warsaw Workshop: Investigating Work Platforms with Food Delivery Workers
â](https://reversing.works/posts/2025/09/warsaw-workshop-investigating-work-platforms-with-food-delivery-workers/)