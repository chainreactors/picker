---
title: Security Considerations on Istio’s CRDs with Namespace-based Multi-Tenancy
url: https://insinuator.net/2026/03/security-considerations-on-istios-crds-with-namespace-based-multi-tenancy/
source: Insinuator.net
date: 2026-03-25
fetch_date: 2026-03-26T04:30:15.964660
---

# Security Considerations on Istio’s CRDs with Namespace-based Multi-Tenancy

[Insinuator.net](https://insinuator.net/)

Bold Statements

Primary Menu

* [About](https://insinuator.net/about/)

* [RSS Feed](https://insinuator.net/?feed=rss)
* [Follow us](http://infosec.exchange/%40insinuator)

## Categories

* [Breaking](https://insinuator.net/category/breaking/)
* [Building](https://insinuator.net/category/building/)
* [Events](https://insinuator.net/category/events/)
* [Misc](https://insinuator.net/category/misc/)

## Tags

[4G](https://insinuator.net/tag/4g/)
[Active Directory](https://insinuator.net/tag/active-directory/)
[advisory](https://insinuator.net/tag/advisory/)
[Android](https://insinuator.net/tag/android/)
[Black Hat](https://insinuator.net/tag/black-hat/)
[Bluetooth](https://insinuator.net/tag/bluetooth/)
[C3](https://insinuator.net/tag/c3/)
[Cisco](https://insinuator.net/tag/cisco/)
[cloud](https://insinuator.net/tag/cloud/)
[Day-Con](https://insinuator.net/tag/day-con/)
[disclosure](https://insinuator.net/tag/disclosure/)
[Docker](https://insinuator.net/tag/docker/)
[ERNW white paper](https://insinuator.net/tag/ernw-white-paper/)
[exploit](https://insinuator.net/tag/exploit/)
[extension headers](https://insinuator.net/tag/extension-headers/)
[forensics](https://insinuator.net/tag/forensics/)
[fuzzing](https://insinuator.net/tag/fuzzing/)
[GSM](https://insinuator.net/tag/gsm/)
[hardening](https://insinuator.net/tag/hardening/)
[hardware](https://insinuator.net/tag/hardware/)
[HITB](https://insinuator.net/tag/hitb/)
[incident analysis](https://insinuator.net/tag/incident-analysis/)
[iOS](https://insinuator.net/tag/ios/)
[IoT](https://insinuator.net/tag/iot/)
[IPv6](https://insinuator.net/tag/ipv6/)
[Linux](https://insinuator.net/tag/linux/)
[malware](https://insinuator.net/tag/malware/)
[medical](https://insinuator.net/tag/medical/)
[network](https://insinuator.net/tag/network/)
[pentest](https://insinuator.net/tag/pentest/)
[reversing](https://insinuator.net/tag/reversing/)
[RIPE](https://insinuator.net/tag/ripe/)
[risk](https://insinuator.net/tag/risk/)
[SAP](https://insinuator.net/tag/sap/)
[SDR](https://insinuator.net/tag/sdr/)
[Telco](https://insinuator.net/tag/telco/)
[TelcoSecDay](https://insinuator.net/tag/telcosecday/)
[tool](https://insinuator.net/tag/tool/)
[TROOPERS](https://insinuator.net/tag/troopers/)
[virtualization](https://insinuator.net/tag/virtualization/)
[VMware](https://insinuator.net/tag/vmware/)
[VoIP](https://insinuator.net/tag/voip/)
[vulnerability](https://insinuator.net/tag/vulnerability/)
[web application](https://insinuator.net/tag/web-application/)
[Windows](https://insinuator.net/tag/windows/)

## Archives

Archives

Select Month
 March 2026  (5)
 February 2026  (3)
 January 2026  (1)
 December 2025  (1)
 October 2025  (2)
 September 2025  (2)
 August 2025  (2)
 July 2025  (3)
 June 2025  (4)
 May 2025  (2)
 April 2025  (2)
 March 2025  (2)
 February 2025  (1)
 January 2025  (2)
 November 2024  (2)
 September 2024  (2)
 August 2024  (2)
 June 2024  (2)
 May 2024  (4)
 April 2024  (4)
 February 2024  (1)
 October 2023  (3)
 September 2023  (2)
 August 2023  (1)
 July 2023  (1)
 June 2023  (2)
 May 2023  (3)
 December 2022  (1)
 September 2022  (2)
 August 2022  (1)
 June 2022  (1)
 April 2022  (1)
 March 2022  (1)
 December 2021  (1)
 October 2021  (1)
 July 2021  (1)
 May 2021  (4)
 April 2021  (2)
 March 2021  (1)
 February 2021  (3)
 January 2021  (5)
 December 2020  (4)
 November 2020  (6)
 October 2020  (2)
 September 2020  (5)
 July 2020  (3)
 June 2020  (1)
 May 2020  (1)
 April 2020  (2)
 March 2020  (3)
 February 2020  (3)
 January 2020  (2)
 December 2019  (2)
 November 2019  (6)
 October 2019  (4)
 September 2019  (3)
 August 2019  (3)
 July 2019  (6)
 June 2019  (6)
 May 2019  (7)
 April 2019  (7)
 March 2019  (2)
 February 2019  (4)
 January 2019  (14)
 December 2018  (4)
 November 2018  (11)
 October 2018  (6)
 September 2018  (1)
 August 2018  (4)
 July 2018  (3)
 June 2018  (3)
 May 2018  (3)
 April 2018  (5)
 March 2018  (8)
 February 2018  (12)
 January 2018  (2)
 December 2017  (2)
 November 2017  (3)
 October 2017  (7)
 September 2017  (5)
 August 2017  (3)
 July 2017  (3)
 June 2017  (6)
 May 2017  (5)
 April 2017  (3)
 March 2017  (8)
 February 2017  (6)
 January 2017  (8)
 December 2016  (12)
 November 2016  (14)
 October 2016  (12)
 September 2016  (12)
 August 2016  (9)
 July 2016  (9)
 June 2016  (7)
 May 2016  (10)
 April 2016  (23)
 March 2016  (29)
 February 2016  (14)
 January 2016  (12)
 December 2015  (15)
 November 2015  (6)
 October 2015  (9)
 September 2015  (7)
 August 2015  (5)
 July 2015  (6)
 June 2015  (14)
 May 2015  (9)
 April 2015  (9)
 March 2015  (13)
 February 2015  (10)
 January 2015  (18)
 December 2014  (10)
 November 2014  (10)
 October 2014  (7)
 September 2014  (3)
 August 2014  (9)
 July 2014  (5)
 June 2014  (1)
 May 2014  (9)
 April 2014  (1)
 March 2014  (3)
 February 2014  (5)
 January 2014  (13)
 December 2013  (5)
 November 2013  (5)
 October 2013  (4)
 September 2013  (1)
 August 2013  (10)
 July 2013  (10)
 June 2013  (5)
 May 2013  (4)
 April 2013  (10)
 March 2013  (4)
 February 2013  (12)
 January 2013  (6)
 December 2012  (2)
 November 2012  (4)
 October 2012  (1)
 September 2012  (3)
 July 2012  (3)
 June 2012  (3)
 May 2012  (8)
 April 2012  (2)
 March 2012  (5)
 February 2012  (6)
 January 2012  (4)
 December 2011  (7)
 November 2011  (7)
 October 2011  (6)
 September 2011  (3)
 August 2011  (3)
 July 2011  (6)
 June 2011  (4)
 May 2011  (4)
 April 2011  (5)
 March 2011  (5)
 January 2011  (2)
 December 2010  (6)
 November 2010  (5)
 October 2010  (3)
 September 2010  (4)
 August 2010  (5)
 July 2010  (6)
 June 2010  (2)
 December 2009  (1)
 November 2009  (1)
 October 2009  (3)
 0  (1)

Search for:

Search

* [ERNW](https://www.ernw.de)
* [ERNW Research](https://www.ernw-research.de)

[Back](https://insinuator.net/#post-15892)

[Misc](https://insinuator.net/category/misc/)

[March 25, 2026](https://insinuator.net/2026/03/security-considerations-on-istios-crds-with-namespace-based-multi-tenancy/) by [Lorin Lehawany](https://insinuator.net/author/llehawany/)

# Security Considerations on Istio’s CRDs with Namespace-based Multi-Tenancy

We reported a possible Man-in-the-Middle (MitM) attack scenario in which a `VirtualService` can redirect or intercept traffic within the service mesh. This affects Namespace-based Multi-Tenancy clusters where tenants have the permissions to deploy Istio resources (`networking.istio.io/v1`).

In collaboration with Istio, we published [a guest submission in Istio’s blog](https://istio.io/latest/blog/2026/security-considerations-on-namespace-based-multi-tenancy/) (as well as below), a [Security Bulletin](https://istio.io/latest/news/security/istio-security-2026-002/), and an update to their [Security Model](https://istio.io/latest/docs/ops/deployment/security-model/#k8s-account-compromise) to address this issue.

This blog post highlights the risks of using Istio in multi-tenant clusters and explains how users can mitigate these risks and safely operate Istio in their deployments.

Please note that the issues even extend beyond the cluster scope in a [*“single mesh with multiple clusters”* deployment](https://istio.io/latest/docs/ops/deployment/deployment-models/#multiple-clusters).

The behavior described in this post applies to Istio version 1.29.0 and to all versions since the introduction of the mesh gateway option in the `VirtualService` resource.

## Background

### Namespace-based Multi-Tenancy

Namespaces in Kubernetes provide a mechanism for organizing groups of resources within a cluster. Namespaces provide a logical abstraction that allows teams, applications, or environments to share a single cluster while isolating their resources via controls such as Network Policies, RBAC, and so on.

In this blog post, we focus on running Istio in clusters where multiple tenants share the same cluster and service mesh, and can deploy Istio resources (`networking.istio.io/v1`) in their ...