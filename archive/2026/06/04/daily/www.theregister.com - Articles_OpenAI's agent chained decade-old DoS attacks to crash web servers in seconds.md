---
title: OpenAI's agent chained decade-old DoS attacks to crash web servers in seconds
url: https://www.theregister.com/security/2026/06/04/openais-codex-chains-decade-old-dos-techniques-into-http/2-bomb/5251377
source: www.theregister.com - Articles
date: 2026-06-04
fetch_date: 2026-06-05T06:14:28.045217
---

# OpenAI's agent chained decade-old DoS attacks to crash web servers in seconds

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
  + [OSes](/oses)
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
  + [SC25](/special_features/2025_11_sycomp_supercomputing)
  + [Supercomputing Month](/special_features/2025_11_supercomputing_month)
  + [Computex 2026](/special_features/computex)
* Vendor Voice
  + [All Vendor Voice](https://vendorvoice.theregister.com/)
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

* [Computex 2026](/special_features/computex)
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

Security

# OpenAI's agent chained decade-old DoS attacks to crash web servers in seconds

Codex drops an HTTP/2 Bomb

Jessica Lyons
[Jessica
Lyons](https://www.theregister.com/author/jessica-lyons)

Published
thu 4 Jun 2026 // 20:08 UTC

The next threat your server faces may have been helped along by a bot. OpenAI's Codex agent helped uncover a remote denial-of-service (DoS) exploit that can be launched from a single machine to render vulnerable web servers inaccessible in seconds, according to Calif security researchers.

The attack works on default HTTP/2 configurations of major web servers including nginx, Apache HTTP Server, Microsoft IIS, Envoy, and Cloudflare Pingora. As of Thursday, Microsoft IIS and Cloudflare Pingora still don’t have a patch, according to the researchers, although Cloudflare disputes this finding.

“Cloudflare's existing architecture and DDoS mitigations automatically detect and protect against this attack, making customers resilient to this vulnerability,” a spokesperson told The Register. “No patch is needed.”

REG AD

REG AD

“We are aware and actively investigating appropriate mitigations to help keep customers protected," a Microsoft spokesperson told The Register.

Calif researcher Quang Luong discovered the exploit, named it HTTP/2 Bomb, and will present the full technical details of the attack at the [Real World AI Security](https://seclab.stanford.edu/RealWorldAIsec/) conference later this month. In the meantime, there are [proof-of-concept exploit scripts](https://github.com/califio/publications/tree/main/MADBugs/http2-bomb) on GitHub along with a warning from the AI red teaming security shop: “Please don't point these at infrastructure you don't own.”

In a Tuesday [blog](https://blog.calif.io/p/codex-discovered-a-hidden-http2-bomb), Luong says Codex chained two existing DoS attack techniques that have been known for more than a decade - HPACK compression bomb and Slowloris-style hold - and warns that upwards of [880,000 websites](https://www.shodan.io/search?query=ssl.alpn%3A%22h2%22+product%3Anginx%2CApache%2CIIS%2CEnvoy%2CPingora) supporting HTTP/2 and running one of the vulnerable web servers may be affected.

An HPACK bomb attack (also known as [CVE-2016-6581](https://nvd.nist.gov/vuln/detail/CVE-2016-6581)) exploits the HTTP/2 header compression algorithm (HPACK) by sending thousands of tiny messages to the server, forcing it to rapidly allocate memory and ultimately crash.

Then the [Slowloris DoS attack](https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris/) ([CVE-2016-8740](https://www.cve.org/CVERecord?id=CVE-2016-8740) and [CVE-2016-1546](https://www.cve.org/CVERecord?id=CVE-2016-1546)) overwhelms the server by opening legitimate connections and maintaining them as long as possible.

Combining the two exhausts the server’s memory and forces it offline.

“A home computer on a 100Mbps connection can render a vulnerable server inaccessible within seconds,” Luong wrote. “Against Apache httpd and Envoy, a single client can consume and hold 32GB of server memory in roughly 20 seconds.”

The Calif research team disclosed the issue to nginx in April, and the web server’s maintainers fixed it the next day in version 1.29.8, which [imports the max\_headers directive](https://github.com/nginx/nginx/commit/365694160a85229a7cb006738de9260d49ff5fa2) from freenginx.

REG AD

Apache issued a fix ([mod\_http2 v2.0.41](https://github.com/icing/mod_h2/releases)) the same day that Calif submitted its report, and assigned it CVE-2026-49975.

“The fix commits above are public and disclose the vectors directly; any capable AI model can turn those diffs into a working exploit, which is exactly how we found that Microsoft IIS, Envoy, and Pingora are also vulnerable,” the threat hunting team wrote, adding that all three have been notified.

In a Wednesday update, Calif pointed to Envoy [patches](https://github.com/envoyproxy/envoy/security/advisories/GHSA-22m2-hvr2-xqc8) “that appear to mitigate this attack,” and notes that its researchers are still validating the fix to ensure it works.

## MORE CONTEXT

* [### 'Please do not vibe f--- up this software': Broken backups spark AI coding row in rsync project](/ai-and-ml/2026/06/04/please-do-not-vibe-f-up-this-software-broken-backups-spark-ai-coding-row-in-rsync-project/5251189)
* [### AI agents show they can create exploits, not just find vulns](/ai-ml/2026/05/15/ai-agents-show-they-can-create-exploits-not-just-find-vulns/5241453)
* [### Agent harnesses, like OpenClaw, are changing how we build and run AI models](/ai-ml/2026/05/17/how-ai-agent-harnesses-like-openclaw-are-changing-llms-inference-and-cpus/5241530)
* [### Nobody needs Mythos or 0-days to build a chaos-causi...