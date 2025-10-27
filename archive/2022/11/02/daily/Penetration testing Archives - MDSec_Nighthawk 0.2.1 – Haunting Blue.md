---
title: Nighthawk 0.2.1 – Haunting Blue
url: https://www.mdsec.co.uk/2022/11/nighthawk-0-2-1-haunting-blue/
source: Penetration testing Archives - MDSec
date: 2022-11-02
fetch_date: 2025-10-03T21:35:23.078338
---

# Nighthawk 0.2.1 – Haunting Blue

* Our Services
* Knowledge Centre
* [About](https://www.mdsec.co.uk/about/)
* [Contact](https://www.mdsec.co.uk/contact/)

* Our Services
  + [Adversary Simulation](https://www.mdsec.co.uk/our-services/adversary-simulation/)
  + [Application Security](https://www.mdsec.co.uk/our-services/application-security/)
  + [Penetration Testing](https://www.mdsec.co.uk/our-services/penetration-testing/)
  + [Response](https://www.mdsec.co.uk/our-services/response/)
* Knowledge Centre
  + [Insights](https://www.mdsec.co.uk/knowledge-centre/insights/)
  + [Research](https://www.mdsec.co.uk/knowledge-centre/research/)
  + [Training](https://www.mdsec.co.uk/knowledge-centre/training/)
* [About](https://www.mdsec.co.uk/about/)
* [Contact](https://www.mdsec.co.uk/contact/)

* [![Adversary](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-adversary.svg)

  ## Adversary Simulation

  Our best in class red team can deliver a holistic cyber attack simulation to provide a true evaluation of your organisation’s cyber resilience.](https://www.mdsec.co.uk/our-services/adversary-simulation/)
* [![Application Security](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-application-security.svg)

  ## Application Security

  Leverage the team behind the industry-leading Web Application and Mobile Hacker’s Handbook series.](https://www.mdsec.co.uk/our-services/applicaton-security/)
* [![Penetration Testing](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-penetration-testing.svg)

  ## Penetration Testing

  MDSec’s penetration testing team is trusted by companies from the world’s leading technology firms to global financial institutions.](https://www.mdsec.co.uk/our-services/penetration-testing/)
* [![Response](https://www.mdsec.co.uk/wp-content/themes/mdsec/img/icons/icon-response.svg)

  ## Response

  Our certified team work with customers at all stages of the Incident Response lifecycle through our range of proactive and reactive services.](https://www.mdsec.co.uk/our-services/response/)

* [## Research

  MDSec’s dedicated research team periodically releases white papers, blog posts, and tooling.](https://www.mdsec.co.uk/knowledge-centre/research/)
* [## Training

  MDSec’s training courses are informed by our security consultancy and research functions, ensuring you benefit from the latest and most applicable trends in the field.](https://www.mdsec.co.uk/knowledge-centre/training/)
* [## Insights

  View insights from MDSec’s consultancy and research teams.](https://www.mdsec.co.uk/knowledge-centre/insights/)

ActiveBreach

# Nighthawk 0.2.1 – Haunting Blue

[Home](https://www.mdsec.co.uk/) >
[Knowledge Centre](https://www.mdsec.co.uk/knowledge-centre/) >
[Insights](https://www.mdsec.co.uk/knowledge-centre/insights) >
Nighthawk 0.2.1 – Haunting Blue

**November 1st 2022**

![](https://www.mdsec.co.uk/wp-content/uploads/2022/11/image-960x960.png)

This Halloween week brings our third and final Nighthawk release for the year and its packed with exciting new features, backed by MDSec’s world class research and development team. Indeed, there are so many new features that move the needle, this release could easily have been a major release. However, as it will be our last release in the current architecture (watch this space! :coolbemused:) we decided to issue it as a minor version. But let that take nothing away from the exciting new features it includes, many of which are first time to any public framework. Without further ado, let’s dive in to what’s new.

# Stego Stager

To date, Nighthawk has always been stageless; that is, the artifacts exported from the framework contained a full copy of the beacon. While we did introduce the concept of keying in 0.2, this release takes things one step further by offering a stager. The stager can be useful in a number of scenarios, and particularly when performing initial access or persistence as it allows the operator to send only a small portion of shellcode to the user without the risk of immediately exposing the full beacon.

0.2.1 provides a new payload generator within the UI, allowing the operator to export ~20kb of customisable shellcode that will retrieve an image over HTTP(S) and extract the Nighthawk stageless shellcode from it, then load it in process. Not only this, the stego stager also offers all the benefits of Nighthawk’s opsec, including the use of indirect syscalls, unhooking and other evasive features:

![](https://www.mdsec.co.uk/wp-content/uploads/2022/11/image-1-960x682.png)

For input, the payload generator will accept any shellcode and lossless image format, using steganography to hide the shellcode inside the modified image.

When combined with Nighthawk’s other payload generation features, such as keying, it allows the full execution chain to offer a high degree of protection for the beacon artifacts; a methodology for execution may look as follows:

![](https://www.mdsec.co.uk/wp-content/uploads/2022/11/image-2.png)

To illustrate the stager, the following video shows creation of 24kb of shellcode that performs a variety of OpSec magic, it then retrieves a PNG image via HTTP that Nighthawk has created and uses steganography to extract the shellcode and load it in process:

# Dark Load Library

In June 2021 we released a blog post on “[Bypassing Image Load Kernel Callbacks](https://www.mdsec.co.uk/2021/06/bypassing-image-load-kernel-callbacks/)” with a companion proof of concept tool called “[Dark Load Library](https://github.com/bats3c/DarkLoadLibrary)” from our colleague [@\_*batsec\_*](https://twitter.com/_batsec_). This research illustrated how manual mapping could be used to bypass telemetry associated with image load events. Conceptually, this technique is powerful as it can assist in avoiding signatures backed by these indicators which have plagued other frameworks as we illustrated in [other research](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/).

For example, to detect the use of mimikatz in an environment a threat hunter might simply hunt for all image load events that occurred within a short period of time and matched a signature of dlls loaded by the tool such as *vaultcli.dll*, *cryptdll.dll* and *samlib.dll*. See [this](https://docs.splunksecurityessentials.com/content-detail/detect_mimikatz_using_loaded_images/) example provided by Splunk for more practical detections. Other examples might include anomalous loading of the CLR and associated DLLs being used to hunt for .NET post exploitation activities.

Nighthawk 0.2.1 brings the integration of a fully weaponised implementation of Dark Loading, allowing all Nighthawk dependencies to be manually mapped in to memory of the host process. These DLLs can then held in an encrypted state at rest and removed from the PEB and other sources used by the loader such hashlinks. The Nighthawk dark loader is available not only for all Nighthawk threads, but also process wide if required. Consequently, this means Nighthawk is able to dark load all DLL dependencies used by post-exploitation tooling, including the *inproc-execute-assembly* CLR harness and the execute-exe PE harness. That is, running any .NET assembly or any PE binary in a unique thread inside the beaconing process will not trigger any image load events, nor will the DLL be immediately visible by tools that attempt to list the modules of a process.

Let’s take a look at this in action:

In this video, we see Nighthawk injected in to a remote process and then subsequently used to execute a .NET assembly in a thread of that process. While monitoring the process for image load events using procmon and Sysmon, we see no image load events (ID 7), we also see Nighthawk manually map the DLL dependencies to the process, monitoring this in Process Hacker we see they are linked in the PEB then subsequently unlinked where they are held in encrypted in virtual memory on sleep.

# Hidden Desktop

Sometimes during a red team engagement, t...