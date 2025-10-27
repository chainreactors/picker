---
title: A Network Nerd's Take on Emergency Preparedness, (Tue, Oct 15th)
url: https://isc.sans.edu/diary/rss/31356
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-22
fetch_date: 2025-10-06T18:55:35.460414
---

# A Network Nerd's Take on Emergency Preparedness, (Tue, Oct 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31354)
* [next](/diary/31360)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [A Network Nerd's Take on Emergency Preparedness](/forums/diary/A%2BNetwork%2BNerds%2BTake%2Bon%2BEmergency%2BPreparedness/31356/)

**Published**: 2024-10-15. **Last Updated**: 2024-10-21 15:10:48 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/A%2BNetwork%2BNerds%2BTake%2Bon%2BEmergency%2BPreparedness/31356/#comments)

Over the last month, two hurricanes barely missed me. Luckily, neither caused me any significant inconvenience. Sadly, others were not as lucky, and I think this is a good time to do a little "Lessons Learned" exercise. It made me reconsider some of my emergency preparations. I will take a "geek spin" on emergency preparedness in this post. There are better sources to talk about what food to store and how to fill your tub with sufficient water. I will focus more on power and data connectivity. At least once, someone complained that the "Internet Storm Center" does not talk about the weather. This post should keep them happy :).![for illustration, picture of heavy rain and storm](https://isc.sans.edu/diaryimages/images/Screenshot%202024-10-21%20at%2011_09_09%E2%80%AFAM.png)

One advantage of hurricanes, compared to other disasters like earthquakes, is that they are usually announced several days ahead. One very viable option is to "get out". If you plan to get out, make a hotel reservation in a safe spot early. Maybe make a hotel reservation that can be canceled on short notice if you do not need it. Or call some friends/family. Leave before mandatory evacuations are announced. Roads are usually packed 24-48 hours before the storm's landfall.

Unplug as many devices as possible before the storm hits (or before you leave), or disconnect circuit breakers. It may be worthwhile to disconnect cable modems and other devices. During a storm, power will often be unstable, and I have seen power lines fall on cable TV and phone lines. This should not cause harm, but it is best to be safe. At the same time, make sure any rechargeable devices and battery packs are fully charged, and turn them off.

If you own a portable backup battery, ensure they are fully turned off while not in use. These batteries' inverters can use significant power even without any devices plugged in [1].

I am not an electrician, so I refer to others for generator safety issues. Generators connected to natural gas may provide longer-term power backup as long as the natural gas supply is not disrupted. For other fuels, it depends on how much you can store locally.

If you use mobile solar cells: Bring them inside during the storm. Same for any antennas that can be detached, like satellite or cell phone external antennas.

Backup batteries will provide you power for a limited time. Most UPS systems will last 15-60 minutes. Some larger battery packs can last a day (e.g. Tesla Powerwall). Most will not last much longer, but you can extend the lifetime by reducing power consumption, particularly for heavy uses like air conditioners. People outside Florida may not realize it, but after the hurricane passes, you often end up with sunny and hot weather. It may not be easy to live without air conditioning.

Most solar systems will not provide backup power without a battery backup. Only some relatively new inverters can run without grid power or supporting a regular generator. The solar system should be off if the generator is running unless the solar system was specifically designed to support the generator. Do not overestimate the capacity of your backup power solution. You often have surges as devices are turned on (for example, refrigerators). My non-electrician rule of thumb is that you need about three times the capacity of your steady-state usage. [2]

And of course, electricity and water do not work well with each other. If water intrudes into your house, you may still want to turn the devices off.

One issue that kept coming up during the recent storms was the reliability of cellular services. In particular, in more rural areas, which often do not have great cellular coverage in the first place, cellular networks were often not usable. Cellular towers still require uplinks and are sometimes destroyed by high winds or water. Power backup is often limited. Mobile operators will sometimes deploy temporary emergency backup towers. However, these towers may only offer a limited range and capacity. Most phones will allow roaming by default, and mobile operators will allow each other's customers to use their network during disasters. But double-check that your phone has roaming enabled.

Luckily, more affordable satellite options have become available and play a larger role in disaster recovery. There are three main options:

Starlink Internet Access: Starlink offers a relatively affordable high-speed solution for internet access. Like all satellite solutions, it requires a clear sky view. But this is probably your best solution if you live in a location allowing Starlink internet access. The connection quality is usually similar to a good 4G/5G cellular connection. Costs vary and are usually more expensive than a cellular backup connection. But Starlink has a small terrestrial footprint and tends to work even after widespread power outages.

Direct to Phone Satellite Access: The SpaceX Starlink satellite constellation has recently added the ability to use a T-Mobile cellular frequency. Select satellites are equipped with this capability. The satellite will appear as a "cell tower in the sky" if enabled. The advantage of this service is that the user does not have to configure it. Any phone able to communicate on the respective frequency will be able to use the service. Some limited data services and messaging services should be available. [3]

Emergency Satellite Messaging: Apple devices and some Android devices can communicate directly with satellites for limited messaging services. Originally, this service was limited to contacting emergency services. However, recently (for Apple as of iOS 18), this service has been able to send limited text messages. This service is only available if no cellular service or WiFi is available. This service uses satellite operators contracted by the respective phone manufacturer (e.g. Apple uses the Globalstar network). Phones supporting this type of messaging usually offer a test feature to allow you to practice using the service. You usually have to point the phone towards the satellite. Sending a message may take a couple of tries. Consider it a service of "last resort", but it will be helpful to send brief messages to friends and family to tell them you are ok or need help. [4] [5]

As with any disaster recovery or backup plan, It does not work unless you test it. For backup network connectivity, it is usually best to always have it "online" and use it for some limited traffic. It can't hurt to have a simple spare router and other network equipment that you keep powered down and disconnected from any networks and power lines. Maybe do not throw out an older router that still works, but keep it around for emergencies (store it with the big bin of old power adapters and other misc cables that you likely keep somewhere).

[1] <https://www.donrowe.com/power-inverter-faq-a/258.htm>
[2] <https://www.greenlancer.com/post/solar-battery-backup-vs-generator>
[3] <https://api.starlink.com/public-files/DIRECT_TO_CELL_FIRST_TEXT_UPDATE.pdf>
[4] <https://support.apple.c...