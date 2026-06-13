---
title: Microsoft has mostly repaired flaw in Surface hardware that allowed unprotected devices to be bricked by a single packet
url: https://www.theregister.com/security/2026/06/12/microsoft-has-mostly-repaired-flaw-in-surface-hardware-that-allowed-unprotected-devices-to-be-bricked-by-a-single-packet/5253895
source: www.theregister.com - Articles
date: 2026-06-12
fetch_date: 2026-06-13T06:12:15.692996
---

# Microsoft has mostly repaired flaw in Surface hardware that allowed unprotected devices to be bricked by a single packet

[Jump to main content](#main)

Search

TOPICS

* Security
  + [All Security](/security)
  + [Cyber-crime](/cyber_crime)
  + [Patches](/patches)
  + [Research](/research)
  + [CSO](/cso)
* Off-Prem
  + [All Off-Prem](/off_prem)
  + [Edge and IoT](/edge_iot)
  + [Channel](/channel)
  + [PaaS and IaaS](/tag/paas-iaas)
  + [SaaS](/saas)
* On-Prem
  + [All On-Prem](/on_prem)
  + [Systems](/systems)
  + [Storage](/storage)
  + [Networks](/networks)
  + [HPC](/hpc)
  + [Personal Tech](/personal_tech)
  + [Cx0](/cxo)
  + [Public Sector](/public-sector)
* Software
  + [All Software](/software)
  + [AI and ML](/tag/ai%20and%20ml)
  + [Applications](/applications)
  + [Databases](/databases)
  + [DevOps](/devops)
  + [OS Platforms](/tag/os%20platforms)
  + [Virtualization](/virtualization)
* Offbeat
  + [All Offbeat](/offbeat)
  + [Columnists](/columnists)
  + [Science](/science)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Bootnotes](/bootnotes)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [RSA Conference](/special_features/rsa)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
* Resources
  + [Intelligence](https://intelligence.theregister.com)
  + [Webinars & Events](https://intelligence.theregister.com/events/list/)
  + [Newsletters](https://account.theregister.com/login?r=https%3A%2F%2Faccount.theregister.com%2Fedit%2Fnewsletter%2F)

Search

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

[![Go to frontpage. Logo, The Register](/view-resources/dachser2/public/theregister/logo.svg)](https://www.theregister.com)

* [Sign in](https://account.theregister.com/login)

* [AI](/tag/ai%20and%20ml)
* [Security](/security)
* [Microsoft](/tag/microsoft)
* [AWS](/tag/aws)
* [Developer](/tag/developer)
* [Open Source](/tag/open%20source)
* [Columnists](/tag/columnists)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)

REG AD

SECURITY

Surface studio laptop gif

# Microsoft has mostly repaired flaw in Surface hardware that allowed unprotected devices to be bricked by a single packet

And it was Microsoft Copilot that unwittingly revealed the longstanding vulnerability

Thomas Claburn
[Thomas
Claburn](https://www.theregister.com/author/thomas-claburn)
Senior reporter

Published
fri 12 Jun 2026 // 14:05 UTC

EXCLUSIVE For the past 90 days, Microsoft has been quietly patching a firmware flaw in Surface devices that allowed the hardware to be bricked with a single packet, though only for those who have disabled Secure Core and Secure Boot.

And the company's Copilot AI software inadvertently helped identify the faulty firmware.

According to Jack Darcy, a security researcher based in Australia, his instance of Microsoft Copilot stumbled across the bug after being asked to adjust the screen backlighting on a Surface device. The Copilot-conjured Python script ended up rendering the researcher's laptop inoperable by overwriting the embedded controller firmware.

REG AD

"Copilot autonomously created and executed four progressively aggressive Python scripts during a probe for backlight control values that sent raw SSAM ioctl commands (SSAM\_CDEV\_REQUEST = 0xC028A501) directly to the SAM microcontroller through the SAM software path," Darcy explained to The Register.

REG AD

The [SAM or SSAM](https://docs.kernel.org/driver-api/surface_aggregator/overview.html) is the embedded controller used in Surface devices. And as our source explained, Microsoft’s implementation of the controller in Surface devices did not include any defense against arbitrary write values.

## MORE CONTEXT

* [### It blocked us at 'hello!' Anthropic Fable 5 refusing innocuous prompts](/ai-and-ml/2026/06/10/anthropic-claude-fable-5-refuses-innocuous-prompts/5253754)
* [### Angry bug hunter with Microsoft beef drops new Windows 0-day](/security/2026/06/10/nightmare-eclipse-publishes-new-windows-defender-zero-day/5253725)
* [### Vercel escapes contempt rap after admitting it botched FBI warrant response](/legal/2026/06/10/vercel-escapes-contempt-rap-after-admitting-it-botched-fbi-warrant-response/5253563)
* [### GitHub pulls pin on npm's auto-run scripts](/devops/2026/06/10/github-pulls-pin-on-npms-auto-run-scripts/5253453)

Microsoft does not consider the bug to be a practical threat. "There is no realistic attack scenario with this issue," a spokesperson told The Register. "In order to successfully exploit it, an attacker would need to interact with specific drivers and send commands to a hardware interface. This would require administrator privileges on the machine, as well as disabling the Secure Boot feature. With this access, they could perform any number of actions."

Commonly, Darcy said, digital devices require holding a button down or connecting a jumper cable to enable arbitrary write access. But that security check is absent in Surface devices, we're told, enabling Copilot to vandalize the firmware in the absence of Secure Core and Secure Boot. Essentially, the probing triggered an update command from the SAM that overwrote the UEFI and Secure Boot firmware.

Surface devices treated to this sort of probing should continue to operate because the SAM was already initialized and is running in RAM. But upon reboot, when the SAM tries to reload using corrupted data in its non-volatile storage, it will fail to initialize, and the system will be unable to Power-On Self-Test (POST).

The Python script crafted by Copilot on the security researcher's Surface device iterated blindly over a particular Target Category and the set of Command ID (CID) pairs, sending empty/null payloads to WRITE commands.

The result, Darcy explained, is that the SET Feature Report was called with null payload, the Output Report was called with null payload, and other CIDs were hit by SET commands that wrote garbage data.

As a result, the device became inoperable. We're told this has been a [common](https://www.reddit.com/r/Surface/comments/h0fvl7/reboot_loop_help/) [complaint](https://www.ifixit.com/Answers/View/892575/Stuck%2Bon%2Bblack%2Bscreen%2Bwith%2Bsurface%2Blogo.) about Surface devices online support forums over the years, though we have no way to determine whether boot failures reported for other Surface devices can be attributed to this specific problem.

Many Surface hardware issues reported publicly appear to be fixable through various troubleshooting techniques. But devices made inoperable by SAM access, our source insists, are permanently bricked – a situation that can entail hundreds of dollars in repairs for a new motherboard. No USB, no factory reset, no access to the BIOS/UEFI, we're told.

REG AD

Darcy said that the ...