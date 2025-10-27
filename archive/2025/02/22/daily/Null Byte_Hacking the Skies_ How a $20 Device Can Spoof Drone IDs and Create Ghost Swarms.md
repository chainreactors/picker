---
title: Hacking the Skies: How a $20 Device Can Spoof Drone IDs and Create Ghost Swarms
url: https://null-byte.wonderhowto.com/how-to/drone-spoofing/
source: Null Byte
date: 2025-02-22
fetch_date: 2025-10-06T21:55:29.452178
---

# Hacking the Skies: How a $20 Device Can Spoof Drone IDs and Create Ghost Swarms

![Header Banner](https://assets.content.technologyadvice.com/null_byte_3840x1800_e4f3abce80.webp)

[![Null Byte Logo](https://assets.content.technologyadvice.com/Logos_Null_Byte_white_b3593aed94.webp)](https://null-byte.wonderhowto.com/)

Null Byte

[WonderHowTo](https://www.wonderhowto.com/)  [Gadget Hacks](https://www.gadgethacks.com/)  [Next Reality](https://next.reality.news/)  [Null Byte](https://null-byte.wonderhowto.com/)

[![wonderhowto.mark.png](https://assets.content.technologyadvice.com/wonderhowto_mark_facd6be46b.webp)](https://null-byte.wonderhowto.com/)

[Cyber Weapons Lab](https://null-byte.wonderhowto.com/collection/cyber-weapons-lab/)  [Forum](https://null-byte.wonderhowto.com/forum)  [Metasploit Basics](https://null-byte.wonderhowto.com/how-to/metasploit-basics/)  [Facebook Hacks](https://null-byte.wonderhowto.com/how-to/facebook-hacks/)  [Password Cracking](https://null-byte.wonderhowto.com/how-to/password-cracking/)  [Top Wi-Fi Adapters](https://null-byte.wonderhowto.com/how-to/buy-best-wireless-network-adapter-for-wi-fi-hacking-2019-0178550/)  [Wi-Fi Hacking](https://null-byte.wonderhowto.com/how-to/wi-fi-hacking/)  [Linux Basics](https://null-byte.wonderhowto.com/how-to/linux-basics/)  [Mr. Robot Hacks](https://null-byte.wonderhowto.com/how-to/mr-robot-hacks/)  [Hack Like a Pro](https://null-byte.wonderhowto.com/how-to/hack-like-a-pro/)  [Forensics](https://null-byte.wonderhowto.com/how-to/forensics/)  [Recon](https://null-byte.wonderhowto.com/how-to/recon/)  [Social Engineering](https://null-byte.wonderhowto.com/how-to/social-engineering/)  [Networking Basics](https://null-byte.wonderhowto.com/how-to/networking-basics/)  [Antivirus Evasion](https://null-byte.wonderhowto.com/how-to/evading-av-software/)  [Spy Tactics](https://null-byte.wonderhowto.com/how-to/spy-tactics/)  [MitM](https://null-byte.wonderhowto.com/how-to/mitm/)  [Advice from a Hacker](https://null-byte.wonderhowto.com/how-to/advice-from-a-hacker/)

[YouTube](https://www.youtube.com/channel/UCgTNupxATBfWmfehv21ym-g/)  [X](https://x.com/NullByte)

Follow Us

Search

  Close Search

Search    Menu

[how to](https://null-byte.wonderhowto.com/how-to/)

# Hacking the Skies: How a $20 Device Can Spoof Drone IDs and Create Ghost Swarms

![](https://assets.content.technologyadvice.com/thumbnail_Logos_Null_Byte_color_light_8d3c214a02.webp)

By [Retia](https://creator.wonderhowto.com/retia/)

Feb 21, 2025, 05:00 PM

[Cyber Weapons Lab](https://null-byte.wonderhowto.com/collection/cyber-weapons-lab/)[Wireshark](https://null-byte.wonderhowto.com/collection/wireshark/)

![A DJI 2 mini quadcopter drone on a picnic table, equipped with D1 Mini microcontrollers powered by a LiPo battery pack.](https://assets.content.technologyadvice.com/drone_swarmer_51642d05ec.webp)

As drone technology continues to evolve, so do the systems designed to track and regulate them. One such system is Open Drone ID, an FAA-recognized remote identification protocol that allows drones to broadcast telemetry and identification data, similar to [ADS-B](https://null-byte.wonderhowto.com/how-to/track-ads-b-equipped-aircraft-your-smartphone-0179666/) for airplanes. While this was implemented for safety and accountability, serious security flaws leave it wide open to spoofing attacks that can flood drone tracking systems with fake UAVs.

Because [Open Drone ID](https://github.com/opendroneid) transmits unencrypted data over Bluetooth and, in some cases, Wi-Fi beacon frames, anyone with a basic ESP8266 microcontroller can intercept and spoof drone signals, generating phantom drone swarms that appear in real-time on tracking apps, law enforcement tools, and airspace monitoring systems. In tests, we were able to spawn up to 16 fake drones per module, each with its own GPS coordinates, altitude, speed, and operational status â all indistinguishable from legitimate UAVs.

This vulnerability presents serious risks to aviation safety, particularly in environments where manned and unmanned aircraft share airspace. Emergency responders, commercial drone operators, and even airports could face overloaded tracking systems, where separating real threats from spoofed drones becomes a logistical nightmare.

* **Don't Miss:** [**How to Track ADS-B Equipped Aircraft on Your Smartphone**](https://null-byte.wonderhowto.com/how-to/track-ads-b-equipped-aircraft-your-smartphone-0179666/)

In our controlled tests, where we monitored packets using [Wireshark](https://null-byte.wonderhowto.com/collection/wireshark/) and analyzed them with [opendroneid-wireshark-dissector](https://github.com/opendroneid/wireshark-dissector), fake drones displayed impossible telemetry â appearing at unrealistic altitudes, moving at excessive speeds, or showing up in physically impossible locations â offering one of the few clues to their fraudulent nature.

By adding a GPS module flashed with our [Drone Swarmer](https://github.com/ANG13T/drone-swarmer) code based on the [Remote ID Spoofer](https://github.com/jjshoots/RemoteIDSpoofer) repo on GitHub, attackers can ensure spoofed drone locations match real-world coordinates, making the swarm appear right where they want it. Without this modification, most spoofed drones default to locations in China, requiring manual GPS adjustments in the firmware. Once synchronized, these fake UAVs can appear to move alongside real drones, potentially masking unauthorized drone activity in sensitive areas.

While Open Drone ID was developed with good intentions, its reliance on unsecured broadcast signals makes it unreliable for security applications. While network-based Remote ID solutions may include authentication, the broadcast-based Open Drone ID protocol lacks encryption and verification mechanisms, making it vulnerable to spoofing. Without these protections, there's no built-in way to differentiate real drones from spoofed ones, leaving airspace monitoring systems susceptible to deception and overload attacks.

This flaw raises major concerns for aviation safety. Manned aircraft rely on ADS-B transponders, which broadcast telemetry data for tracking and deconfliction. Civil ADS-B is also unencrypted â and so is Open Drone ID â making them susceptible to similar spoofing concerns. Until stronger cryptographic security is implemented, drone detection tools and airspace monitoring systems will remain vulnerable to interference from low-cost spoofing devices.

## Products used in the Drone Swarmer

If you're interested in studying Open Drone ID vulnerabilities, here are the components used to create the spoofed drone swarm:

* [Five-pack D1 Mini (ESP8266) microcontroller](https://amzn.to/3WMZ6dz)
* [Solderable breakout board](https://amzn.to/3EoC9XO)
* [PCB mount terminals](https://amzn.to/3CDksmL)
* [LiPo battery charger board](https://amzn.to/4aI1ub0)
* [LiPo rechargeable battery](https://amzn.to/3En83E0)
* [Solderless breadboards](https://amzn.to/42Fr7aB)
* [NEO6M GPS flight controller module](https://amzn.to/3EkYO7r)
* [Jumper wires kit](https://amzn.to/3EGxTTI)
* [Different-sized zip ties](https://amzn.to/4baGmL6)

When you calculate the price to build one drone swarmer spoofing device, it's close to $20 on average. This assumes you already have a drone to attach it to. We used a [DJI Mini 2](https://amzn.to/3WIYEg8), which costs hundreds of dollars, but cheaper drones can also work.

* [DJI Mini 2 (ultralight, foldable drone quadcopter)](https://amzn.to/3WIYEg8%20)

## How to stay within legal limits

Before experimenting with Open Drone ID security, always check [Airspace Link](https://airspacelink.com/) or similar services to ensure your testing area is legal for drone flights. Never deploy drone spoofing in restricted airspace, airports, or populated areas. The purpose of this research is to highlight vulnerabilities â not to interfere with real drone and aircraft operations.

> **Don't Miss:** [**Create Your Own Ethical Hacking Kit with a Raspberry Pi 5**](https://null-byte.wonderhowto.com/...