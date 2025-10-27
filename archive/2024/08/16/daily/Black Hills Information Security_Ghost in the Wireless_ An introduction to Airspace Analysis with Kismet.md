---
title: Ghost in the Wireless: An introduction to Airspace Analysis with Kismet
url: https://www.blackhillsinfosec.com/an-introduction-to-airspace-analysis-with-kismet/
source: Black Hills Information Security
date: 2024-08-16
fetch_date: 2025-10-06T18:03:55.549099
---

# Ghost in the Wireless: An introduction to Airspace Analysis with Kismet

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

15
Aug
2024

[Cameron Cartier](https://www.blackhillsinfosec.com/category/author/cameron-cartier/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Recon](https://www.blackhillsinfosec.com/category/red-team/recon/), [Wireless](https://www.blackhillsinfosec.com/category/red-team/wireless/)
[Kismet](https://www.blackhillsinfosec.com/tag/kismet/), [wifi](https://www.blackhillsinfosec.com/tag/wifi/)

# [Ghost in the Wireless: An introduction to Airspace Analysis with Kismet](https://www.blackhillsinfosec.com/an-introduction-to-airspace-analysis-with-kismet/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/08/CCartier-150x150.png)

| [Cameron Cartier](https://www.blackhillsinfosec.com/team/cameron-cartier/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/08/BLOG_chalkboard_00683.png)

This is the first installment in a series of blogs relating to practical analysis of wireless communications: what they are, how they work, and how they can be attacked. In this post, we are going to walk through setting up the [Kismet](https://www.kismetwireless.net/) tool and performing basic analysis of 802.11x traffic.

### **Background**

*This section provides background on wireless communications and the electromagnetic spectrum. If you simply want instructions on setting up Kismet, skip to the “Setup” section.*

Rather than sending messages via electrical signal going over wires, WIFI, Bluetooth, and other recent technologies utilize waves of various frequencies to transmit information. This transmission relies on digital data being converted into an analogue waveform which will be projected onto the carrier wave using some modulation technique (i.e., Amplitude modulation or Frequency Modulation). The antenna then takes this modulated signal and transmits it out through the airspace.

The WIFI signals we’re talking about today transmit waves in the 2.4GHz and 5.8GHz ranges (“5G” operates at a frequency of 5.8GHz). The image below shows approximately where 2.4 GHz WIFI falls on EMF spectrum.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/08/Kismet_01.png)

[**A Diagram Showing the Electromagnetic Spectrum**](https://commons.m.wikimedia.org/wiki/File%3AElectromagnetic_spectrum_by_NIEHS.jpg)

The above may be a bit misleading as cellphones and 2.4G wireless, as well as microwave ovens, have some overlap; however, it gets the general idea across. 5G wireless would fall just on the right of microwaves and before infrared remote controls.

The next section provides a detailed walkthrough on setting up an adapter and software to view these signals. Then we will move on to interpreting and analyzing the data.

### **Equipment Setup**

We can see many interesting things while monitoring our surrounding airspace including nearby devices, our neighbors SSIDs, and if we’re lucky, maybe even capturing some [4-way handshakes](https://networklessons.com/cisco/ccnp-encor-350-401/wpa-and-wpa2-4-way-handshake). You can follow along from the comfort of your own home, or wherever you’d like, provided you are able to acquire the following items.

You will need:

* 1 Machine running Kali Linux (virtual machine is fine)

* 1 USB WIFI adapter capable of running in monitor mode

* 1 nerdy friend with a sense of adventure (optional)

Our setup consists of an ARM-64 Kali instance running in VMWare and a USB-C connected [ALFA AWUS036ACH](https://www.amazon.com/ALFA-AWUS036ACH-%E3%80%90Type-C%E3%80%91-Long-Range-Dual-Band/dp/B08SJC78FH) WIFI adapter.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/08/Kismet_02-345x500.png)

ALFA AWUS036ACH

Once you have your Kali machine up and running, you will need to install drivers for the wireless adapter. If you are using the same wireless adapter mentioned above, the following commands should be sufficient.

```
sudo apt install dkms

git clone https://github.com/aircrack-ng/rtl8812au

cd rtl8812au

sudo make dkms_install

# if you get an error about missing kernel headers, install them

sudo apt install linux-headers-6.6.9-arm64  # your version may differ. The error should tell you which version is requested.

make dkms_install  # again, after headers are installed

make clean  # run if the previous command fails

make

make install
```

Once you have your Kali machine up and running, you will need to install drivers for the wireless adapter. If you are using the same wireless adapter mentioned above, the following commands should be sufficient.

Your machine should now be abl...