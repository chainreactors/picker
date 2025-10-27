---
title: Intercepting Traffic for Mobile Applications that Bypass the System Proxy
url: https://www.blackhillsinfosec.com/intercepting-traffic-for-mobile-applications/
source: Black Hills Information Security, Inc.
date: 2025-05-01
fetch_date: 2025-10-06T22:27:44.764777
---

# Intercepting Traffic for Mobile Applications that Bypass the System Proxy

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

30
Apr
2025

[Cameron Cartier](https://www.blackhillsinfosec.com/category/author/cameron-cartier/), [Dave Blandford](https://www.blackhillsinfosec.com/category/author/dave-blandford/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Mobile](https://www.blackhillsinfosec.com/category/red-team/mobile/)
[Flutter](https://www.blackhillsinfosec.com/tag/flutter/), [proxy](https://www.blackhillsinfosec.com/tag/proxy/), [traffic interception](https://www.blackhillsinfosec.com/tag/traffic-interception/)

# [Intercepting Traffic for Mobile Applications that Bypass the System Proxy](https://www.blackhillsinfosec.com/intercepting-traffic-for-mobile-applications/)

by [Cameron Cartier](https://www.blackhillsinfosec.com/team/cameron-cartier/) and [Dave Blandford](https://www.blackhillsinfosec.com/team/david-blandford/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/trafficproxy_header-1.png)

This is a foolproof guide to intercepting traffic from mobile applications built on Flutter, which historically have been especially challenging to intercept. The methods presented should work for other types of applications as well. In the first half of this blog, we will discuss a method of intercepting iOS traffic via internet sharing on Mac. In the second half, we will show you how to intercept traffic from a rooted Android virtual device (AVD) using HTTP Toolkit.

*Need help with the rooting process? You can check out Dave’s blog on ‘How to Root Android Phones’ here: <https://www.blackhillsinfosec.com/how-to-root-android-phones/>*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture1-2.jpg)

**Ben Taking a Break from a Flutter Mobile App Test**

### **Internet Sharing for iOS**

**Warning:** If you don’t follow every step exactly as specified, you will spend hours banging your head against a wall thinking you’ve gone crazy because it worked yesterday, and now everything looks broken because you forgot a single step. Ask me how I know.

Requirements:

* A Jailbroken iOS Device (tested on iPhoneX running iOS 16.5.1)
* MacBook Pro
* Some combination of adapters to connect the two

From the computer, go to Settings -> Sharing -> Internet Sharing. Before toggling this on, click the info icon on the right-hand side.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture2-1.png)

**Mac Settings**

This will bring you to the menu shown below.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture3-3.png)

**Internet Sharing Options**

Next, connect your iOS device via USB. This should still work if you’re using a program like USBFlux. Once you do this, you should see the “iPhone USB” option shown above. Change the settings to share from Wi-Fi to the iPhone. This should match the screenshot above. In addition, make sure that Wi-Fi and any other network interfaces are turned off on the phone.

This will create a new network interface on the Mac, which will show up if you run ifconfig. In my case, the new interface was bridge103.

To verify that the traffic you are interested in is now visible from the Macbook, you can run:

```
 tcpdump -i <bridge interface for the phone>
```

You should see traffic when using the iOS device. This indicates you are successfully sharing internet with the device over the bridge interface.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture4-3.png)

**Traffic Shown in TCPDump Interface**

Next, open the pf.conf file in your favorite text editor:

```
sudo vim /etc/pf.conf
```

Add the following line:

```
rdr on bridge103 inet proto tcp from any to any -> 127.0.0.1 port 8889
```

This must be added in the exact position shown below (after the rdr anchor and before the dummynet-anchor line), otherwise you will get an error when you run the next command.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture5-2.png)

**Properly Edited pf.conf File**

Now, flush the rules with the following command.

```
sudo pfctl -f /etc/pf.conf
```

Then we enable IP forwarding:

```
sudo sysctl -w net.inet.ip.forwarding=1
```

This should forward all traffic coming into the bridge103 interface over to localhost:8889. Now we will start a Burp Suite listener on that port.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture6-3.png)

**Burp Suite Proxy Binding Configuration**

In addition to changing the host and port shown above, we need to enable support for invisible proxying. Invisible proxying is a method for non-proxy-aware clients or applications to connect directly to a Burp Proxy listener. This is useful at times when the requests are not formatted in a way the proxy is expecting. More inform...