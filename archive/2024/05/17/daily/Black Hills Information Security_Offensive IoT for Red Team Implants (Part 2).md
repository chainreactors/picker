---
title: Offensive IoT for Red Team Implants (Part 2)
url: https://www.blackhillsinfosec.com/offensive-iot-for-red-team-implants-part-2/
source: Black Hills Information Security
date: 2024-05-17
fetch_date: 2025-10-06T17:16:07.173093
---

# Offensive IoT for Red Team Implants (Part 2)

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

16
May
2024

[Hardware Hacking](https://www.blackhillsinfosec.com/category/how-to/hardware-hacking/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Physical](https://www.blackhillsinfosec.com/category/red-team/physical/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/), [Tim Fowler](https://www.blackhillsinfosec.com/category/author/tim-fowler/)

# [Offensive IoT for Red Team Implants (Part 2)](https://www.blackhillsinfosec.com/offensive-iot-for-red-team-implants-part-2/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/TFowler-150x150.jpg)

| [Tim Fowler](https://www.blackhillsinfosec.com/team/tim-fowler/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Offensive-IoT-Part-2-1024x576.png)

This is Part Two of the blog series, *Offensive IoT for Red Team Implants*, so if you have not read [PART ONE](https://www.blackhillsinfosec.com/?p=28558), I would encourage you do to so first and then come back here.

In this blog, we are going take a “from the ground up” approach to getting a Raspberry Pi Pico (Pico W) set up and running as a physical implant device for attacks such as USB Rubbery Ducky. Then, we will pivot slightly and extend the capability for the implant device by enabling and using a bolted-on LoRa module to take the entire attack process to level 11. Let’s dive in.

You are going to need to have some basic hardware accessible to you, mainly: a Raspberry Pi Pico or Pico W (which I will just reference as a Pico from here on out) and a micro USB cable. (You also need a computer, but I am assuming that was a given.)

### **Getting Started**

To get started, you will need to set up the environment for the configuring and programming of your Pico. For this blog series, we are going to be using CircuitPython[1](#1cb06f26-6788-465f-910c-1d3208588c2c) as our language of choice. There are many options available for the Pico platform, including C/C++ and Arduino, but, for this use case, Circuit Python is a pretty solid choice, with its ease of use and preexisting libraries.

You are also going to need some sort of IDE to develop your code in. For this blog, we are going to use Thonny IDE, which touts itself as a Python IDE for beginners.[2](#724d5d70-4e24-4640-9c4d-968afcda0708) You don’t have to use Thonny; there are many IDEs out there to choose from, but for the purpose of keeping it simple, that is what we will use.

#### Thonny IDE

First, you need to download Thonny from the website: <https://thonny.org/>

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/OffensiveIoTpt2_01.png)

Thonny is cross-platform compatible, so whether you are running on Windows, a Mac, or Linux, you should not have any issues.

After you have downloaded the installer for your OS of choice, you then need to install Thonny by executing the installer. I happened to be on a Windows system while authoring this blog, so below is a screenshot of what the install looks like on Windows.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/OffensiveIoTpt2_02.png)

Once you have Thonny installed, you are ready for the next steps — installing Circuit Python on your Pico.

#### Circuit Python

To get your Pico running with CircuitPython, you need to first download the version of CircuitPython that corresponds to the Pico you have. In my case, I am using a Pico W, but you could also be using just a Pico, or, possibly, one of the 495 boards CircuitPython supports. While this blog is based on the Pico and Pico W, it’s important to note that this process should work with any RP2040-based board (but your milage may vary).

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/OffensiveIoTpt2_03.png)

After selecting your board on the CircuitPython Download page, you will be taken to a page where you can download the CircuitPython firmware file, a *.UF2* file, for your chosen board.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/OffensiveIoTpt2_04.png)

Download the latest stable release firmware file to your computer; at the time of this writing, it was 9.0.4.

Once you have downloaded the .UF2 file, you can then connect your Pico to your computer using a micro USB cable. I would suggest you first plug the micro USB end of the cable into the Pico, WITHOUT the other end of the USB cable being plugged into your computer. The reason for this is that you will need to hold down the BOOTSEL button on the Pico when powering up to install CircuitPython, and that is a lot easier to do if you use one hand to hold ...