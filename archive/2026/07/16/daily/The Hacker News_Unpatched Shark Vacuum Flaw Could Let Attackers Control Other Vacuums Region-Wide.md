---
title: Unpatched Shark Vacuum Flaw Could Let Attackers Control Other Vacuums Region-Wide
url: https://thehackernews.com/2026/07/unpatched-shark-vacuum-flaw-could-let.html
source: The Hacker News
date: 2026-07-16
fetch_date: 2026-07-17T05:00:24.882663
---

# Unpatched Shark Vacuum Flaw Could Let Attackers Control Other Vacuums Region-Wide

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Unpatched Shark Vacuum Flaw Could Let Attackers Control Other Vacuums Region-Wide](https://thehackernews.com/2026/07/unpatched-shark-vacuum-flaw-could-let.html)

**Swati Khandelwal**Jul 16, 2026IoT Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5tbAe6HgEiYpwgRNJ04jo1HJ_PV3INByd4ggz2t4h_dCa4u2zkCBimnzDZt7V-p208q7-BfaHSmR5_aXg6VvnnThfnc9_UX8oP0hnRa6rP1JVgKka-D76BpYUzhEuc3O0nbEGgoVeCQsTY2RBsVTrYnViTmGPqgPJ9e4lNeKWtxZNxKqvUajphbl-ENY/s1700-e365/shark-hack.jpg)

Pull the certificate off the flash of a Shark RV2320EDUS robot vacuum, and you can run root commands on other people's Shark vacuums across the same AWS region: watch the camera, drive the robot, read the map of the house, and take the Wi-Fi password in plaintext.

A researcher publishing under the handle **tokay0** [put the method online](https://tokay0.com/posts/millions-of-shark-vacuums-vulnerable-to-rce.html) on Monday, having tested it only against vacuums he bought himself. The flaw was unpatched then.

He says SharkNinja, the company behind the Shark and Ninja appliance brands, has had his report since March.

The policy attached to that certificate was never scoped to the device holding it. Present it to Shark's cloud broker, and the broker accepts whatever you publish, addressed to any device it serves.

No memory corruption, no privilege escalation, no password to guess. The command that runs is an ordinary field in the device shadow, the per-device state document AWS keeps in the cloud.

Using the certificate from an RV2320EDUS, the researcher subscribed to $aws/things/# and watched the traffic crossing the broker, harvesting serial numbers as he went. Publishing works the same way. The shadow carries an Exec\_Command field that the management daemon appd reads and hands to a function named execute\_command, which runs anything under 1,000 bytes through popen.

Send a shadow update carrying that field to a device's topic. If that device implements the handler, it runs the command.

He proved the cross-model path, landing a reverse shell on an AV1102ARUS he bought purely as a target, then using that shell to pull a live feed off the model's onboard camera while the robot drove around.

The certificate comes off with a screwdriver. The mainboard exposes UART pins, the U-Boot console asks for no password, and init=/bin/sh in the boot arguments drops you to a root shell, where the per-device key and certificate sit in /mnt/res/vapp/certs/ as ordinary files.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Certificates are pinned to their AWS region, the closest thing here to a limit: a key lifted in one region only reaches that region's devices. Reaching another region takes another certificate, provisioned there, and carrying the same broken policy.

Amazon has an audit check for this exact policy shape. Device Defender, AWS's IoT fleet auditing service, flags device policies granting publish or subscribe on $aws/things/\* instead of pinning the topic to the connecting device with ${iot:Connection.Thing.ThingName}.

It appears as IOT\_POLICY\_OVERLY\_PERMISSIVE\_CHECK, and AWS rates it critical, warning in [its documentation](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/audit-chk-iot-policy-permissive.html) that a compromised certificate carrying such a policy lets an attacker "read or modify shadows, jobs, or job executions for all your devices."

Not every certificate is a skeleton key. A vacuum whose certificate carries the broken policy is an attacker's key. Any vacuum that runs Exec\_Command is a target, whether or not its own certificate is scoped correctly. The AV1102ARUS is a target and not a key: its certificate was scoped correctly and could not wildcard-subscribe. Its firmware was several years newer.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIsn00QcRBS7IEDyvP6A9bpjr8PTJWWkFDiSBsKxK4QbAXnsaO5jMXJGsJVvL6odxeuP-PCfLyZjzHo3nXr2Lx-1pGrKGfWMNzZN5GzvAW4WqWPCaIvJXgrQf_jKRi9BOCOKrNSe_ZP4XdktAam4jfEZzMaDjttR0Y92c5kfageySyp1-W4XjzLOyEPc0/s1700-e365/poc.gif)

He reads that as a provisioning fix that never reached the older fleet's certificates. That is why the cross-model shell worked, and why his claim that every internet-connected Shark vacuum is vulnerable needs splitting in two.

The headline on his post says millions. The figure he verified is narrower. Watching one AWS region for 24 hours, tokay0 counted 1,517,605 unique Shark serial numbers, of which 673,816, or 44%, emitted an Exec\_Response, which he treats as confirmation that the device runs the command handler. Those are devices observed replying, not devices tested or compromised, and he says the true number is likely higher.

## Four Months and Counting

By tokay0's account of the correspondence, he contacted SharkNinja on March 1 and sent details on March 11. The company acknowledged receipt the next day, told him on April 27 that the report was under review, and on July 3 said it would send a confirmed completion date by Friday, July 10. No email arrived.

He published on July 13. He says the vendor downplayed the severity and questioned whether "a CVE is appropriate."

On IoT reports specifically, SharkNinja's published [vulnerability disclosure policy](https://www.sharkninja.com/vulnerability-disclosure-policy.html) commits the company to "provide regular updates until the reported vulnerability is resolved." The same policy asks researchers to stay quiet until the company confirms a fix or authorizes disclosure in writing.

SharkNinja had published nothing on the flaw as of Thursday. The Hacker News has reached out to the company for comment on the patch status and the disclosure timeline, and will update this story with any response.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdx...