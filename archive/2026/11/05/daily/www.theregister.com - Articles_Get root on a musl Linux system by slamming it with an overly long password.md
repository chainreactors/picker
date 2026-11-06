---
title: Get root on a musl Linux system by slamming it with an overly long password
url: https://www.theregister.com/security/2026/11/05/get-root-on-a-musl-linux-system-by-slamming-it-with-an-overly-long-password/5307910
source: www.theregister.com - Articles
date: 2026-11-05
fetch_date: 2026-11-06T08:41:43.830219
---

# Get root on a musl Linux system by slamming it with an overly long password

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
  + [Anthropic](/tag/anthropic)
  + [BOFH](/bofh)
  + [Legal](/legal)
  + [Site News](/site_news)
  + [About Us](https://www.theregister.com/about_us)

* Special Features
  + [All Special Features](/special_features)
  + [Supercomputing Month 2026](/special_features/supercomputing_month_2026)
  + [Nvidia GTC Berlin 2026](/special_features/nvidia_gtc_berlin_2026)
  + [Cybersecurity Month 2026](/special_features/cybersecurity_month_2026)
  + [VMware Explore 2026](/special_features/vmware_explore_2026)
  + [Cloud Infrastructure Month 2026](/special_features/cloud_infrastructure_month_2026)
  + [HPE: AI Explainers](/explainer/ai-explainer)
  + [Agentic AI](/special_features/agentic_ai)
  + [The Future of the Datacenter](/special_features/future_of_the_datacenter)
  + [AWS:Reinvent](/special_features/aws_reinvent)
  + [Nvidia GTC](/special_features/nvidia_gtc)
  + [Computex 2026](/special_features/computex)
  + [AI Infrastructure Month 2026](/special_features/ai_infrastructure_month_2026)
  + [The State of Storage 2026](/special_features/state_of_storage_2026)
  + [RSA Conference](/special_features/rsa)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
  + [Modernizing Financial Services with FIS and AWS](https://vendorvoice.theregister.com/aws_fis_capital_markets/)
  + [Barco](https://vendorvoice.theregister.com/barco/)
  + [Infinidat](https://vendorvoice.theregister.com/infinidat/)
  + [Everpure](https://vendorvoice.theregister.com/everpure/)
  + [Rubrik](https://vendorvoice.theregister.com/rubrik/)
  + [Make it real with Capgemini and AWS](https://vendorvoice.theregister.com/aws_capgemini/)
  + [Money Movement Hub](https://vendorvoice.theregister.com/aws_fis/)
  + [ZTE](https://vendorvoice.theregister.com/zte_news_and_stories/)
  + [Nutanix: Scale Kubernetes. Not Chaos.](https://vendorvoice.theregister.com/nutantix_cloud_native_apps/)
  + [AWS New Horizon](https://vendorvoice.theregister.com/aws_new_horizon/)
  + [Digicert](https://vendorvoice.theregister.com/digicert)
  + [Netscout](https://vendorvoice.theregister.com/netscout)
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
* [Software](/software)
* [Microsoft](/tag/microsoft)
* [Developer](/devops)
* [Open Source](/tag/open%20source)
* [BOFH](/tag/bofh)
* [Who, Me?](/tag/who%20me)
* [On Call](/tag/on%20call/)
* [Anthropic](/tag/anthropic)

REG AD

[security](/tag/security)

# Get root on a musl Linux system by slamming it with an overly long password

Decade-old vulnerability in OpenSSH is now fixed, so get a-patchin'

Brandon Vigliarolo
[Brandon
Vigliarolo](https://www.theregister.com/author/brandon-vigliarolo)
GOVERNMENT AND IT NEWS REPORTER

Published
thu 5 Nov 2026 // 18:29 UTC

[Make us preferred on Google](https://google.com/preferences/source?q=theregister.com)

### READ MORE

* [#### openSUSE Leap 16.1 gives Linux users the right to remain immutable

  14 hours ago](/os-platforms/2026/11/05/opensuse-leap-161-gives-linux-users-the-right-to-remain-immutable/5307874)
* [#### Fedora 45 is finally finished and fit

  1 day ago](/os-platforms/2026/11/04/fedora-45-is-finally-finished-and-fit/5307631)
* [#### Turn your home into a giant crane game with this open source robot

  1 day ago](/offbeat/2026/11/04/turn-your-home-into-a-giant-crane-game-with-this-open-source-robot/5307628)
* [#### Achieving nirvana: Enlightenment 0.28 hits the desktop

  1 day ago](/os-platforms/2026/11/04/achieving-nirvana-enlightenment-028-hits-the-desktop/5307329)
* [#### Nvidia is happy to take your money whether you're using open or closed models, says Jensen Huang

  2 days ago](/ai-and-ml/2026/11/03/nvidia-is-happy-to-take-your-money-whether-youre-using-open-or-closed-models-says-jensen-huang/5307368)

On certain Linux systems, an attacker could gain root access by entering a password longer than 256 bytes. The vulnerability, dubbed [\*sshole](https://sshhole.com/) by Wakefield researcher Özgün Kültekin, who discovered it, can only be exploited in very specific conditions.

The flaw affects certain Linux systems using musl libc instead of the traditional GNU C library, and even then only those running OpenSSH's secure shell daemon without Pluggable Authentication Modules (PAM) and with password authentication enabled.

If those conditions are met, and at least one other account has a valid password hash, accounts that shouldn't accept passwords, such as root, key-only deployment users, and LDAP users, may be accessed by supplying a password between 257 and 1,024 characters. The targeted accounts must have an asterisk (\*) in their password field, and direct root login remains subject to OpenSSH's configuration.

REG AD

That might seem niche, but sorry: It’s not.

REG AD

Musl libc is common in embedded Linux systems due to its low footprint. More critically than that, it's also the standard C library for Alpine Linux, which provides official cloud images for both AWS and Azure. Some Alpine systems running in those environments may therefore be vulnerable, depending on their configuration.

### Dawn of the \*sshole

The vulnerability in OpenSSH on musl-based Linux systems dates back to 2016, but Kültekin explains that its roots go back much further – to the BSD Unix era, actually.

In 1980, Sun Microsystems cofounder and BSD Unix heavyweight [Bill Joy](https://www.theregister.com/software/2003/09/09/bill-joy-leaves-sun/1442431) was involved in the development of BSD Unix, whose password file contained a single asterisk in the /etc/passwd entry for the daemon user. The asterisk wasn't a password hash and effectively disabled password authentication for that account.

Nowadays, password hashes typically live in /etc/shadow and contain hashed information that the system uses to verify a plaintext password entered by a user. Asterisks are still present for accounts that aren't supposed to accept password logins, but as Kültekin explains in his writeup, that isn't exactly a foolproof way to keep people out.

The crypt() function, which generates password hashes for comparison with stored values, can return NULL if it can't compute a hash. Applications that fail to check that result may crash. Musl libc's developers instead chose to return a single character for certain failures, and they picked the asterisk.

Musl also added SHA-512-based password hashing around the same time, which Kültekin notes gets slower the longer a password is, potentially leading to denia...