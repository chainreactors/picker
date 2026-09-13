---
title: infected-drones
url: https://kitploit.com/en/tools/github/nicholasaleks/infected-drones
source: Kitploit
date: 2026-09-12
fetch_date: 2026-09-13T07:01:27.950177
---

# infected-drones

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/nicholasaleks/infected-drones

![](https://assets.kitploit.com/production/public/tools/54834/c2b7475bb8cd99660208fc1f381d030b0f67fd87b172025605250f2c08f80553-display-v1.webp)

[Embedded Systems Security](/en/categories/embedded-systems-security)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Exploitation](/en/categories/exploitation)[Reverse Engineering](/en/categories/reverse-engineering)[Penetration Testing](/en/categories/penetration-testing)[Hardware & IoT Security](/en/categories/hardware-iot-security)[Papers & Research](/en/categories/papers-research)[Learning & Education](/en/categories/education)

![GitHub](/providers/github.png)nicholasaleks/infected-drones

# infected-drones

A collection of vulnerabilities & exploits against modern GCS

[View Repository](https://github.com/nicholasaleks/infected-drones)

1321 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Infected Drones

**Drone-to-Ground Control Station attack vectors, vulnerabilities & exploits**

Drone fleets today are one operator flying dozens or hundreds of drones from a
single ground station. This makes the ground control station a valuable target for adversaries.
It is where the pilot is usually located, it often stores mission data, and it is a prime vector
for lateral movement across UxS networks and other drones in a fleet.

![Infected Drone](https://assets.kitploit.com/production/public/readmes/54834/c2b7475bb8cd99660208fc1f381d030b0f67fd87b172025605250f2c08f80553/d62de07797764f23c5862c4e3d110aad71e91689a06d3414c21e81f554c8b184-display-v1.webp)

Most drone security research has focused on targeting the drone. The [Infected Drone](https://github.com/nicholasaleks/infected-drones) research takes an
alternative approach and highlights how a single compromised drone can attack ground stations that connect to it.
Because most ground control software trusts whatever the drone sends it, there is a lack of
authentication, validation, and sanitization, allowing data from a compromised
drone to lead to file CRUD, code execution, or a crash on the operator's machine.

---

## Responsible use

This repository documents vulnerabilities in ground control station software and ships working
proof-of-concept code for them. It is published for educational purposes only and for operators
to understand their exposure and so maintainers can reproduce and fix these issues.

Run the PoCs only against systems you own or have written permission to test. Every one of them is
written for a bench: the payloads are benign markers, and nothing here is packaged for use against
someone else's aircraft or ground station. Using this material against systems you do not control is
likely illegal wherever you are.

Each finding's Reproduction section states what it needs and what it does. Read it before running
anything.

---

## Findings

Legend:

* ✅ reliable with that vector
* ⚠️ possible, but conditional, racy, or needs extra steps
* ❌ not applicable for this finding via that vector

**Delivery class** is what the attacker has to do on the link, and it decides which vectors work.
*Push* findings need only a frame arriving at the GCS, so any injection-capable vector is enough.
*Handshake* and *request/response* findings need the attacker to be, or fully control, the
conversational peer, which favours an on-bus peripheral, a compromised companion, the supply
chain, or a full MITM.

The **Fix** column links the upstream pull request where one has been submitted. Ten of the fifteen
findings ship with a patch filed against the vendor's own repository.

---

## Delivery vectors

The matrix scores seven columns per finding: the five vectors below, plus the two SiK radio
(RF telemetry) modes, which get their own callout below given the injection-vs-MITM nuance.

1. **Infected flight controller, serial connection, or supply chain.** A local attacker or a malicious
   flight controller gets physically connected to the GCS host or the radio. The vehicle or firmware is
   something the operator did **not** build: a demo unit, rental, seized airframe, or second-hand craft,
   whose firmware is implanted to emit hostile MAVLink the moment a GCS connects.
   The operator's *own* GCS is the victim; the "vehicle" was hostile before it was
   ever powered on. Applies to every finding, and is the cleanest way to deliver
   *connect-time* handshake exploits. This extends to forensic analysts who may connect directly to
   or extract data from an infected vehicle. Those artifacts, if not properly handled,
   could infect or spread to the analyst's computer and network.
2. **Malicious / counterfeit MAVLink peripheral on the vehicle's own bus.** A
   third-party camera, gimbal, ADSB-in, rangefinder, or any device that *speaks
   MAVLink and is itself the attacker.* It is a *legitimate participant* on the
   link emitting hostile frames. A counterfeit "smart camera" advertising
   poisoned messages is doing exactly what a real one does, just with
   hostile values.
3. **Compromised companion computer onboard** (Raspberry Pi / Jetson running
   mavlink-router / MAVProxy). Once compromised it *becomes* the vehicle endpoint,
   with full bidirectional access to the link and visibility of its live state. It can
   answer any handshake and emit any push frame, which makes it viable for every
   finding in this set.
4. **WiFi / UDP telemetry bridge** (ESP8266 / ESP32 "wifi telemetry"). Anyone on the
   access point or LAN can inject MAVLink data. This collapses the cost of the injection vectors to
   near zero and, for an attacker who can also intercept (ARP/AP MITM), enables
   full handshake control too.
5. **TCP / cloud relay** (SITL, mavlink-router TCP, mavp2p, 4G/LTE cloud GCS such
   as commercial UAV-cloud services). MITM at the relay, or anyone who can reach
   the exposed TCP port, can rewrite the stream. Cloud/4G links widen the
   geographic blast radius enormously and frequently lack mutual auth.

### SiK radio (RF telemetry link)

The dominant real-RF telemetry path for ArduPilot/PX4 hobby and prosumer craft is
a [SiK radio pair](https://ardupilot.org/copter/docs/common-sik-telemetry-radio.html), a transparent serial bridge that does not parse or
validate MAVLink, so it offers the GCS zero protection against hostile content.
A rogue SiK module joins or bridges an existing link using
[sikw00f](https://github.com/nicholasaleks/sikw00f). Two attack modes, with very
different reliability:

* **Injection (one rogue radio).** [sikw00f](https://github.com/nicholasaleks/sikw00f)
  can transmit hostile frames onto the shared channel once synced to the link.
  Reliable for one-shot push/stream messages (`STATUSTEXT`, `PARAM_VALUE`,
  `CAMERA_INFORMATION`, etc.), no reply needed. Unreliable for handshake
  protocols (MAVFTP, param/log download) since the injector must win an airtime
  race and match a session/sequence it doesn't control.
* **Full-MITM (rogue pair).** Two [sikw00f](https://github.com/nichola...