---
title: A practical Technical Security playbook oriented toward lawful, peaceful protest in the United States.
url: https://krypt3ia.wordpress.com/2026/01/09/a-practical-technical-security-playbook-oriented-toward-lawful-peaceful-protest-in-the-united-states/
source: Krypt3ia
date: 2026-01-09
fetch_date: 2026-01-10T03:33:22.976002
---

# A practical Technical Security playbook oriented toward lawful, peaceful protest in the United States.

# [Krypt3ia](https://krypt3ia.wordpress.com/)

(Greek: κρυπτεία / krupteía, from κρυπτός / kruptós, “hidden, secret things”)

## A practical Technical Security playbook oriented toward lawful, peaceful protest in the United States.

[with one comment](https://krypt3ia.wordpress.com/2026/01/09/a-practical-technical-security-playbook-oriented-toward-lawful-peaceful-protest-in-the-united-states/#comments)

Designed to reduce avoidable risk from surveillance, device seizure, data exposure, doxxing, and opportunistic violence, without advising wrongdoing or evasion of lawful processes.

This is not legal advice.

# **Introduction**

Public protest has always carried risk. What has changed in recent years is the density and permanence of that risk. Surveillance is no longer exceptional or episodic; it is ambient. Data collection is not limited to state actors; it is embedded in consumer devices, platforms, cameras, and data markets that operate continuously before, during, and long after a protest ends. At the same time, enforcement environments have become less predictable, accountability less certain, and post-event retaliation, through doxxing, employment pressure, or targeted harassment are more common. For many participants, the most serious consequences now occur after they have gone home.

This document is written for that reality.

It does not assume criminal intent, nor does it advocate evasion of lawful authority. It assumes lawful, peaceful protest conducted in an environment where risk is unevenly distributed, rules may be applied selectively, and mistakes compound quickly across technical, physical, and personal domains. In such conditions, safety is not achieved through any single tactic or tool. It is achieved through discipline, preparation, and an understanding that phones, bodies, identities, and communities are all part of the same security system.

The playbook that follows treats technical security, physical safety, operational behavior, and personal exposure as inseparable. A compromised phone can lead to compromised relationships. A moment of physical isolation can create lasting digital consequences. An impulsive post can undo hours of careful on-the-ground decision-making. Conversely, small, well-chosen precautions, clear threat modeling, device hardening, role clarity, exit planning, can dramatically reduce harm without diminishing the expressive or democratic purpose of protest.

This document is intentionally conservative. It favors risk reduction over bravado, exit options over endurance, and community protection over individual visibility. It is designed to be useful to first-time protesters and experienced organizers alike, adaptable across roles, and readable without technical specialization. Where possible, it consolidates guidance from established civil-liberties, digital-rights, and safety organizations into a single, coherent framework.

Above all, this playbook starts from a simple premise: the goal of protest is not merely to show up, but to return safely, with your autonomy, relationships, and future intact. Everything that follows is in service of that outcome.

## **Start with a threat model (10 minutes that changes everything)**

Before you optimize tactics, define what you are protecting and from whom.

**Assets at risk:**Your identity, your contacts, your location history, message content and metadata, photos and video (yours and others’), and your online accounts.

**Likely threats at protests:**Device loss or theft, device confiscation, account compromise, location tracking via routine phone telemetry, large-scale video capture, social media OSINT, and post-event doxxing campaigns. These threat categories; loss, confiscation, disruption, and targeted surveillance, are explicitly identified by Amnesty International.

**Constraints:**Local laws and policies (mask restrictions, curfews, dispersal orders), your role (organizer, medic, marshal, journalist, attendee), and your risk tolerance.

This threat model determines whether you should bring a smartphone at all. Multiple civil-liberties organizations recommend considering leaving it at home if feasible.

## **TECHSEC: Hardening your phone so seizure or loss is less catastrophic**

### **CAVEAT: BURN PHONES**

Much has been said about obtaining a “Burn Phone” if you plan on protesting. While this might be a prudent measure, there are a few things you must do in order to insure the security you are attempting to create by getting one.

* First, pay with cash, do not have a paper trail from purchase
* Disguise yourself as much as possible when purchasing, avoid cameras, phones can be tracked all the way back to purchase
* Understand that this device is a throwaway, no personal data should reside on it.
* Do not load your apps you use every day
* Keep the contacts empty and always erase call logs if possible
* Do not assume that buying a new SIM card means your phone isn’t trackable. Each use should be its only use.
* Follow all of the rules below for the burn phone just as you would for your personal to minimize risk.

### **Device encryption and lock discipline (highest ROI)**

* Ensure **full-device encryption** is enabled. Modern iOS and many Android devices encrypt by default when a passcode is set.
* Use a **strong passcode** (long PIN or alphanumeric) and set **auto-lock** to a short interval.
* **Disable biometric unlock** (Face ID, fingerprint) before arrival. Biometrics can be physically compelled in ways a passcode typically cannot.

*(Encryption, passcodes, biometrics guidance: ACLU of DC)*

### **Minimize exposed data on the lock screen**

* Disable lock-screen message previews.
* Remove sensitive widgets (calendar, email snippets, smart-home controls).

### **Reduce radios and location leakage when not actively needed**

* Use **airplane mode** when not communicating to reduce emitted signals and routine location updates.
* Turn off **Bluetooth and Wi-Fi** unless actively required.
* *Use a reliable Faraday bag after putting the phone in airplane mode and turning off Bluetooth and Wi-Fi. Keep the device in the Faraday bag until far enough away from the event before taking it out and turning it back on.*

*(Radio and signal-reduction guidance consolidated from ACLU of DC and World Justice Project toolkits)*

### **Pre-protest data minimization**

* **Back up your phone** beforehand so it can be wiped and restored if needed.
* Remove or sign out of high-risk apps (primary email, banking, password managers) if not required onsite.
* Update the operating system and critical apps before you go.

*(Backup and update guidance consolidated from protest safety toolkits)*

## **COMMS OPSEC: Make coordination resilient and reduce collateral exposure**

**Prefer end-to-end encrypted messaging for coordination.**Signal is widely recommended in protest safety guides as an additional layer of protection.

**Group hygiene to prevent cascade compromise**

* Keep logistics in **small, role-based groups** (marshals, medics, legal observers), not mass chats.
* Use disappearing messages for operational chatter when appropriate, balancing legal and accountability needs.
* Treat anything sent digitally as potentially shareable later.

**Non-digital fallback**

* Agree on a rally point, an exit route, and a check-in time in case of network disruption.

*(Encrypted comms and fallback planning consolidated from Amnesty and allied civil-liberties guidance)*

## **PERSEC: Protect identity, relationships, and your wider community**

Many harms occur ***after*** protests through doxxing, employer pressure, stalking, and targeted harassment.

### **Identity compartmentation**

* Keep protest planning separate from personal accounts and personal devices when feasible.
* Avoid using primary social accounts for logistics; reserve them for public advocacy only.

### **Photography and community privacy**

* Do not publish images that identify other attendees without consent (faces, tat...