---
title: Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters
url: https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html
source: The Hacker News
date: 2026-07-01
fetch_date: 2026-07-02T05:58:20.869293
---

# Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters

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

# [Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters](https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html)

**Swati Khandelwal**Jul 01, 2026Kubernetes / Server Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9emdIsaMBcMQoyS0ot-ckXq8LWhMk6P2zAm3WdCVFBhRMNUqN6E1vZqllIq6qYHBvGm8WhCGi8C3PLUNOecmNYU4LLoWH5zRBadBejDgpbC5DihDwqiYAMLpZNsQBk2MsiN89nt-honwtPiQzjg4fDUp5w2aiCXWZBKk94qHwfG4yEHak6zoZuNmXKgY/s1700-e365/argo-cd.jpg)

**Argo CD**, a widely used tool for deploying software to Kubernetes, has an unpatched flaw in its repo-server component that lets an unauthenticated attacker run code, provided they can reach the component's internal network port.

[Synacktiv](https://www.synacktiv.com/en/publications/caught-in-the-octopus-trap-unauthenticated-rce-in-argo-cd-with-codeql), which found the bug, says it can lead to a full cluster takeover. There is no fix and no CVE. The firm says it reported the flaw to Argo CD's maintainers in January 2025; roughly eighteen months later, it remains unpatched, so it published the details to warn users.

The bug sits in repo-server, the Argo CD component that reads Git repositories and builds Kubernetes manifests, the files that define what the cluster deploys.

Its internal gRPC service has no authentication; anyone who can reach it can send a crafted request to run a command. Synacktiv demonstrated the attack against Argo CD v2.13.3 and reports no patched release; it did not publish a full list of affected versions.

The technique abuses **kustomize**, a standard tool Argo CD runs to turn repository files into manifests. Kustomize has a --helm-command option that points to the helm binary it should call.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Synacktiv found that an unauthenticated request to the repo-server's GenerateManifest service can set that option to a script instead, pulled from an attacker-controlled Git repository. When kustomize runs, it executes the script rather than helm.

But "internal" does not mean isolated by default. Argo CD [ships Kubernetes network policies](https://github.com/argoproj/argo-cd/blob/e3bcc48bf2dc92c1f397dc28a333881106a8a653/manifests/base/repo-server/argocd-repo-server-network-policy.yaml) that wall the repo-server off from everything except its own components.

Synacktiv found the Helm chart, a common way to install Argo CD, [leaves those policies off by default](https://github.com/argoproj/argo-helm/blob/2685b861d2b2af4f5797522ec3cef8140c3d6049/charts/argo-cd/values.yaml#L112), with networkPolicy.create set to false. In that setup, an attacker who compromises a single pod in the cluster can reach the repo-server and trigger the bug.

Running code on the repo-server is not the end of it. Synacktiv used that access to read the cluster's Redis password from an environment variable, connect to Argo CD's Redis cache, and poison the stored deployment data. On the next automatic sync, Argo CD deployed an attacker-supplied workload.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbbVXb98P5LUTJ7dZ-shA5v5APRA5U2zXK-1s1e-BvYed1oUrDmp5nzawSY1ap8HONEcHec89DOY5FNNJK6fOkl_akpFxJHRBYlWFOd7Jxhmpv7cAmrlOUNB1e4vA2h8ofNk-d699EjJjktY3bNEzCiR0MaeFtxRSUCDFocRWCmIOe3-RV0Ps-5IpKoVo/s1700-e365/argo.jpg)

That step revives [CVE-2024-31989](https://cycode.com/blog/revealing-argo-cd-critical-vulnerability/), a 2024 flaw Cycode found where Argo CD's Redis had no password, letting any pod in the cluster poison the deployment cache. Argo CD fixed that by adding a Redis password, but the cache itself is still not signed, so stealing the password back reopens the same attack.

## What to do

There is no patched version, so the defense is network isolation. Turn on Kubernetes network policies so only Argo CD's own components can reach the repo-server and Redis ports. Argo CD provides the policy files; Helm users have to enable them because the chart leaves them off.

Check what is active with: *kubectl get networkpolicy -A.*A healthy install shows one network policy per component, including the repo-server and Redis. If those policies are missing, the repo-server and Redis ports are reachable from the rest of the cluster.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

Synacktiv built a tool, argo-cdown, that automates the full attack. It is holding the tool back for now to give defenders time to lock down their network policies, and says it will publish it on GitHub later so administrators can test their own deployments.

This is not Argo CD's first exposure of its own internals. In September 2025, it patched [CVE-2025-55190](https://github.com/argoproj/argo-cd/security/advisories/GHSA-786q-9hcg-v9ff), where an API token with only basic read access could pull back a project's Git repository credentials, a flaw that [The Hacker News flagged at the time](https://thehackernews.com/2025/09/weekly-recap-bootkit-malware-ai-powered.html#:~:text=ArgoCD%20Attack%20to%20Exfiltrate%20Git%20Credentials).

In May 2026, another bug, [CVE-2026-42880](https://github.com/argoproj/argo-cd/security/advisories/GHSA-3v3m-wc6v-x4x3), allowed read-only users to read plaintext Kubernetes secrets. The pattern is hard to miss: Argo CD concentrates cluster access and repository secrets, and its internal surfaces keep handing them out, to an unauthenticated request in one bug and a low-privilege token in the next.

Until a patch ships, treating the cluster network as hostile is the only real defense.

Found this article interesting? Follow us on [Google News](https://news.google.com/publ...