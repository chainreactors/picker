---
title: quark-engine v26.9.1
url: https://kitploit.com/en/posts/github-ev-flow-quark-engine-v2691
source: Kitploit
date: 2026-09-05
fetch_date: 2026-09-06T06:39:22.718516
---

# quark-engine v26.9.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/6741/896c831335911a2de27ffe4eaa7f501d0f1670432afde44c94df5f1a46b06bd1.png)

New releaseSep 5, 2026

# quark-engine v26.9.1

Rule-based Android malware scoring engine that analyzes APKs using static and dynamic analysis to detect vulnerabilities, identify malware families, and generate detailed threat reports.

Share

[![Black Hat Arsenal](https://img.shields.io/badge/Black%20Hat%20Arsenal-Asia%202024-blue)](https://www.blackhat.com/asia-24/arsenal/schedule/index.html#quark-script---dig-vulnerabilities-in-the-blackbox-37549)
[![Black Hat Arsenal](https://img.shields.io/badge/Black%20Hat%20Arsenal-Asia%202021-blue)](https://www.blackhat.com/asia-21/arsenal/schedule/index.html#quark-engine-storyteller-of-android-malware-22458)
[![HITB](https://img.shields.io/badge/HITB-Lockdown%20002-red)](https://conference.hitb.org/hitb-lockdown002/sessions/quark-engine-an-obfuscation-neglect-android-malware-scoring-system/)
[![defcon](https://img.shields.io/badge/DEFCON%2028-BTV-blue)](https://www.youtube.com/watch?v=XK-yqHPnsvc&ab_channel=DEFCONConference)
[![build status](https://github.com/quark-engine/quark-engine/actions/workflows/pytest.yml/badge.svg)](https://github.com/quark-engine/quark-engine/actions/workflows/pytest.yml)
[![codecov](https://codecov.io/gh/ev-flow/quark-engine/graph/badge.svg)](https://codecov.io/gh/quark-engine/quark-engine)
[![license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/18z/quark-rules/blob/master/LICENSE)
[![python version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-31015/)
[![PyPi Download](https://pepy.tech/badge/quark-engine)](https://pypi.org/project/quark-engine/)
[![Twitter](https://img.shields.io/twitter/follow/quarkengine?style=social)](https://twitter.com/quarkengine)
![](https://assets.kitploit.com/production/public/readmes/6741/03a197011a23cc6c340ef8243156a4a8da0cb226daf3ea012a0d007029c48fa9.png)

## Malware Family Analysis Report Showcase

|  |  |  |
| --- | --- | --- |
| ![](https://assets.kitploit.com/production/public/readmes/6741/e14e7970a278faef3a85a6ceee30dd7681c8d7be6f16bc8fad16ff3230600bc1.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/72948195e3960572f7c23ff84362625375890339c5f75d651fe42d02e9ed1e95.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/1705305abf7957429991bf0cf5ba0bc619edc460604806451ecd0ddc8c464a23.png) |
| ![](https://assets.kitploit.com/production/public/readmes/6741/d94cb3d285cfcc850934be26d17b38c226bc671cddb707ce6597e399f2dca1de.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/2423f24f7933d1923794763e041bdb9d99027688f5f3254e73f7b36e79e3c00a.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/0035c5f69112d8097ee4ece87a8b0f05f28bc2dec6a8f8cec645138c4d0b5080.png) |
| ![](https://assets.kitploit.com/production/public/readmes/6741/f73f15ad9490c35e70dbea6a90acbd69b480103f9fcdc87440868c3f745c1450.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/c0628a03cbd744f7cb5077d27e9cf3b31e4e6faa11a480c729e6f66f1c9f9391.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/ff076c7dc8c384297783518dcec6861ef3de193f292724589759ab38c6717032.png) |
| ![](https://assets.kitploit.com/production/public/readmes/6741/d8a967c14e5b508626a281d50f008ab3a6422008231e9e7b3b6b8bbc0822afe5.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/eea1fde985ce1cbc5097045e39ed59a92b3c1b9defa920084d64764bd582b8f6.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/4e1ef70891c707c427030190d413c66e65183608abfc96d550c203ae7b121ead.png) |
| ![](https://assets.kitploit.com/production/public/readmes/6741/64d7d5044f1b2e2219507f765302a95313f04c19e81a10f5b7c0dd04ceb13a12.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/5a4348c3ee554e08cf1509923c29152a337b9c1e7f674b5d0f187feb8884b7f0.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/cf2ac808de2437476ff2b20e8178cd906614fe5daea9c3d56c57683c45f73558.png) |
| ![](https://assets.kitploit.com/production/public/readmes/6741/00a382b46e7116952deba2411f72d1eb3addd9d94a0f43cc28419c6e7728c4c0.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/fb3f3c0f39b14940edfc6ba133a0670a333e509b19d1e4c5d259621d8875eefb.png) | ![](https://assets.kitploit.com/production/public/readmes/6741/6bc7b397dedd9d531ff7a4add4e97001ff5bfe6f78d0506de06b0f4352f65538.png) |
| ![](https://assets.kitploit.com/production/public/readmes/6741/946a13c57e64267f069f0bd0ca98dba98216d014092dc0f09c5eadb060854986.png) |

| Family | Summary | Signature Behaviors | Report |
| --- | --- | --- | --- |
| DroidKungFu | Privilege escalation with C2 control. | 1. Gain unlimited access to a device. 2. Install/Uninstall additional apps. 3. Forward confidential data. | [View](https://quark-engine.readthedocs.io/en/latest/malware_report.html#new-quark-rules-for-droidkungfu) |
| GoldDream | SMS/call log exfiltration with remote C2 commands. | 1. Monitor SMS messages and phone calls. 2. Upload SMS messages and phone calls to remote servers. | [View](https://quark-engine.readthedocs.io/en/latest/malware_report.html#new-quark-rules-for-golddream) |
| SpyNote | Credential theft and device surveillance via RAT. | 1. Take screenshots. 2. Simulate user gestures. 3. Log user input. 4. Communicate with C2 servers. | [View](https://quark-engine.readthedocs.io/en/latest/malware_report.html#new-quark-rules-for-spynote) |
| DawDropper | Dropper that installs banking trojans for financial theft. | 1. Download APKs from remote servers. 2. Install additional APKs. | [View](https://quark-engine.readthedocs.io/en/latest/malware_report.html#new-quark-rules-for-dawdropper) |
| SLocker | Android ransomware locking/encrypting devices. | 1. Lock the device with an overlay screen. | [View](https://quark-engine.readthedocs.io/en/latest/malware_report.html#new-quark-rules-for-slocker) |
| PhantomCard | NFC relay–based financial fraud. | 1. Communicate with C2 servers. 2. Read the payment data of NFC cards. 3. Captures PINs of NFC cards through deceptive screens. | [View](https://quark-engine.readthedocs.io/en/latest/malware_report.html#new-quark-rules-for-phantomcard) |
| ToxicPanda | Banking trojan enabling on-device fraud. | 1. Abuse Accessibility. 2. Remote device control. 3. Intercept OTP. | [View](https://quark-engine.readthedocs.io/en/latest/malware_report.html#new-quark-rules-for-toxicpanda) |
| Hydra | Banking trojan using overlay attacks. | 1. Overlay credential theft. 2. Accessibility abuse. 3. Steal OTP/cookies. | [View](https://quark-engine.readthedocs.io/en/latest/malware_report.html#new-quark-rules-for-hydra) |
| SharkBot | Banking trojan targeting financial credentials and transactions. | 1. Abuse Accessibility services. 2. Perform overlay attacks to steal credentials. 3. Intercept SMS messages (OTP). | [View](https://quark-engine.readthedocs.io/en/latest/malware_report.html#new-quark-rules-for-sharkbot) |
| Antidot | Banking trojan disguised as legitimate updates for financial data theft. | 1. Intercept SMS messages (OTP). 2. Log user input (keylogging). 3. Enable remote control via C2. | [View](https://quark-engine.readthedocs.io/en/latest/malware_report.html#new-quark-rules-for-antidot) |
| Arsink | Banking trojan focusing on credential and financial data exfiltration. | 1. Steal sensitive data from device. 2. Intercept SMS messages (OTP). | [View](https://quark-engine.readthedocs.io/en/latest/malware_report.html#new-quark-rules-for-arsink) |
| TrickMo | Banking trojan using over...