---
title: New TorNet backdoor seen in widespread campaign
url: https://blog.talosintelligence.com/new-tornet-backdoor-campaign/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-29
fetch_date: 2025-10-06T20:11:09.830416
---

# New TorNet backdoor seen in widespread campaign

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# New TorNet backdoor seen in widespread campaign

By
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/)

Tuesday, January 28, 2025 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)
[Threats](https://blog.talosintelligence.com/category/threats/)

* Cisco Talos discovered an ongoing malicious campaign operated by a financially motivated threat actor since as early as July 2024 targeting users, predominantly in Poland and Germany, based on the phishing email language.
* The actor has delivered different payloads, including Agent Tesla, Snake Keylogger, and a new undocumented backdoor we are calling TorNet, dropped by PureCrypter malware.
* The actor is running a Windows scheduled task on victim machines—including on endpoints with a low battery—to achieve persistence.
* The actor also disconnects the victim machine from the network before dropping the payload and then connects it back to the network, allowing them to evade detection by cloud antimalware solutions.
* We also found that the actor connects the victim’s machine to the TOR network using the TorNet backdoor for stealthy command and control (C2) communications and detection evasion.

# The campaign

The intrusions start with a phishing email as the initial infection vector. The actor is impersonating financial institutions and manufacturing and logistics companies by sending fake money transfer confirmations and fake order receipts, respectively. The phishing emails are predominantly written in Polish and German, indicating actor’s intent to primarily target users in those countries. We also found some phishing email samples from the same campaign written in English. We assess with medium confidence that the actor is financially motivated, based on the phishing email themes and the filenames of the email attachments.

The phishing email has attachments with the file extension “.tgz”, indicating that the actor has used GZIP to compress the TAR archive of the malicious attachment file to disguise the actual malicious content of the attachment and evade email detections.

![](https://blog.talosintelligence.com/content/images/2025/01/data-src-image-03b2af04-6d02-4b57-bc7e-7f768ba132c1-1-1-1.png)

Sample phishing email in Polish.

![](https://blog.talosintelligence.com/content/images/2025/01/data-src-image-d66c1f12-a74c-4e85-b900-1d5e0df9056e-1-1.png)

Sample phishing email in German.

When a user opens the compressed email attachment and manually unzips it and runs a .NET loader executable, it eventually downloads encrypted PureCrypter malware from a compromised staging server. The Loader decrypts the PureCrypter malware and runs it in the system memory.

In a few intrusions in this campaign, we found that the PureCrypter malware drops and runs the TorNet backdoor. The TorNet backdoor establishes connection to the C2 server and also connects the victim machine to the TOR network. It has the capabilities to receive and run arbitrary .NET assemblies in the victim machine’s memory, downloaded from the C2 server, increasing the attack surface for further intrusions.

![](https://blog.talosintelligence.com/content/images/2025/01/data-src-image-f20f9234-69b0-4187-bd36-2a1b9efb1715.jpeg)

# .NET loader implants PureCrypter

Talos found that the compressed attachment files contain a large .NET executable file. The actor has instrumented the .NET executable to either download the next-stage malicious executables from a remote staging server or to reflectively load an embedded malicious binary.

Some of the loader samples we analyzed in this campaign download the AES-encrypted binary of the PureCrypter malware hosted on compromised websites in paths “/filescontentgalleries/pictorialcoversoffiles/” and “/post-postlogin/” using a hardcoded URL. The encrypted PureCrypter binaries were stored with the arbitrary filenames using different file extensions, including .pdf, .dat, .wav, .vdf, .mp3 and .mp4. The loader decrypts the PureCrypter binary and loads reflectively.

![](https://blog.talosintelligence.com/content/images/2025/01/data-src-image-5b739db9-cb3c-4c5b-9cc7-13f0c28d9cd6.png)

Snippet of the loader program that downloads the encrypted PureCrypter malware.

![](https://blog.talosintelligence.com/content/images/2025/01/data-src-image-e5f798e0-1d50-442f-adc0-d78da15b8f15-1.png)

Network traffic showing the encrypted PureCrypter malware downloaded from the hosting site.

In a few other loader samples, we found that the encrypted PureCrypter sample was embedded in the loader, which is decrypted using the AES algorithm and reflectively loaded into the victim machine’s memory.

![](https://blog.talosintelligence.com/content/images/2025/01/data-src-image-11928abf-74bb-4d76-9d76-15f0460f147d.png)

Snippet of the loader with embedded PureCrypter binary.

# PureCrypter drops the TorNet backdoor

The PureCrypter malware found in this intrusion is a Windows dynamic-link library obfuscated with Eziriz’s .NET Reactor obfuscator. It has resources of encrypted binaries of legitimate DLLs, including Protobuf-net and Microsoft task scheduler DLL along with the TorNet backdoor.

PureCrypter initially creates a mutex on the victim machine and executes the command to release the currently assigned DHCP IP address of the victim machine, establishes persistence, performs various anti-analysis and detections tasks, drops and runs the payload, and finally executes a command to renew the IP address of the victim machine.

```
Cmd /c ipconfig /release
Cmd /c ipconfig /renew
```

The threat actor is likely using this technique to evade detections from the cloud-based anti-malware programs by disconnecting the victim machine from the network and connects back to the network after dropping and running the backdoor.

The PureCrypter malware performs various a...