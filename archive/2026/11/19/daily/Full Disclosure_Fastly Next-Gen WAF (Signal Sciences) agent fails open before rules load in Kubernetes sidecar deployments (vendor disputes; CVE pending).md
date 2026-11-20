---
title: Fastly Next-Gen WAF (Signal Sciences) agent fails open before rules load in Kubernetes sidecar deployments (vendor disputes; CVE pending)
url: https://seclists.org/fulldisclosure/2026/Nov/40
source: Full Disclosure
date: 2026-11-19
fetch_date: 2026-11-20T09:23:10.907370
---

# Fastly Next-Gen WAF (Signal Sciences) agent fails open before rules load in Kubernetes sidecar deployments (vendor disputes; CVE pending)

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](39)
[By Date](date.html#40)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](39)
[By Thread](index.html#40)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Fastly Next-Gen WAF (Signal Sciences) agent fails open before rules load in Kubernetes sidecar deployments (vendor disputes; CVE pending)

---

*From*: Zac Lohrenz <zaclohrenz () gmail com>
*Date*: Tue, 17 Nov 2026 17:29:12 -0600

---

```
Fastly Next-Gen WAF (Signal Sciences) agent: fail-open before rules
load in Kubernetes sidecar deployments

Product:     Fastly Next-Gen WAF agent (sigsci-agent) with the NGINX
             module, Kubernetes sidecar deployment
Vendor:      Fastly, Inc.
Affected:    All agent versions in default configuration, through at
             least 4.83.2 (tested 2026-11-12). Before 4.52.0 no
             mitigation existed. 4.52.0 and later are affected unless
             the startup probe is configured.
Weakness:    CWE-636 Not Failing Securely ('Failing Open');
             CWE-1188 Initialization of a Resource with an Insecure
             Default; CWE-696 Incorrect Behavior Order
CVSS 4.0:    6.3 Medium
             CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:N/VI:L/VA:N/SC:N/SI:L/SA:N
CVE:         Requested from MITRE CNA-LR 2026-09-29; pending
Vendor
position:    Not a vulnerability; intended fail-open design. Will not
             change the default.
Mitigation:  Configure the agent startup probe (4.52.0+)
Researcher:  Zac Lohrenz
Writeup:     https://zaclohrenz.com/posts/cve/fastly-nextgen-waf/
Evidence:    https://github.com/zaclohrenz/fastly-ngwaf-poc

1. Summary
----------

In the Kubernetes sidecar deployment of Fastly's Next-Gen WAF (NGINX
ingress controller with the sigsci module, plus a sigsci-agent sidecar
sharing a Unix socket), the WAF passes traffic uninspected whenever
the agent has not loaded a ruleset, while the pod reports Ready.

  - Until the agent creates its RPC socket, the module cannot connect
    (errno=2), logs an error, and passes the request through.
  - The agent creates the socket when its first configuration
    download attempt ends, whether or not it succeeded. With no
    ruleset loaded, it answers every RPC.PreRequest with
    WAFResponse 200 and the header "X-SigSci-Agent: disabled", and
    keeps doing so until a later download succeeds.

Nothing in the default deployment ties pod readiness to rule load.
Every rollout, restart, eviction and scale-out creates a window, and
any startup failure to fetch configuration extends it for as long as
the failure lasts.

2. Lab testing
--------------

Tested 2026-11-12: sigsci-agent 4.83.2 (index digest
sha256:4aa2f5296b5f2eeb1a71e79643a93afb19ce85a635a21895ff35b2d0701578d2)
and sigsci-nginx-ingress-controller 1.15.1-fastly1.4.0 (index digest
sha256:a4c66bfe5c0b06c6507ce89881ba891711ab3009b2d5d934db192a91e0f452ba),
deployed with Fastly's published sigsci-values.yaml (commit 9794dfb) in
a local kind cluster. Generator at ~20 req/s including SQLi, XSS and
path traversal payloads; echo backend logging all request headers.
Black-box: logs, documented flags, the agent's documented RPC debug
dump, and HTTP headers. No Fastly credentials were available, so the
agent could never load a ruleset.

Phases observed:

  Phase                       Behavior                Default signal
  --------------------------  ----------------------  -----------------
  Socket not yet created      Module fails open       NGINX [error]
                                                      "cannot connect
                                                      uds socket" per
                                                      request
  Socket created, no ruleset  Agent answers           None in NGINX;
                              WAFResponse 200 +       agent logs only
                              X-SigSci-Agent:         "Config update
                              disabled                failed" ~every 30s

Config-download failure types tested, 3 runs each: connection drop,
HTTP 403 (rejected credentials), DNS NXDOMAIN, TCP reset. All four
produced the same state: 20,304 decoded agent responses, one distinct
value (allow, marked disabled). The state persisted with retries every
~30 s for as long as configuration could not be loaded.

With slow failures (dropped connections) the socket appeared after
~60 s and ~935 requests per run passed during the no-socket phase.
With fast failures it appeared within ~1.7 s. The 60 s figure is an
artifact of how egress was blocked, not a typical duration.

Mitigations tested:

  - Startup probe (SIGSCI_STARTUP_PROBE_LISTENER + startupProbe): pod
    held out of Service endpoints, zero requests to the upstream,
    3 of 3 runs.
  - Readiness probe initialDelaySeconds 10/30/60 (vendor-suggested
    alternative): traffic, including attack payloads, reached the
    upstream after each delay expired.
  - No documented module or agent option made either component fail
    closed. The experimental debug-standalone=4 removed the
    no-socket phase and the "disabled" marker but still allowed every
    request.

For contrast, freezing the agent after its socket existed (the
documented timeout path) made the module fail open after ~320 ms per
request, also with no log line at default level. The vendor documents
the timeout behavior; it documents nothing about an agent that answers
with no ruleset loaded.

Per-request evidence of the disabled state appears only with
non-default options, e.g. SIGSCI_STATSD_ADDRESS (counter
sigsci.agent.rpc.tx.dropped.engine_disabled) or
SIGSCI_DEBUG_LOG_UPLOADS (AgentEnabled:0).

Limits: without working credentials, a healthy start was not observed
(whether a valid agent ever opens its socket before its first ruleset
loads, the probe's 503 -> 200 transition, and how these requests appear
in the vendor console). The finding is about failure at startup: in
every failure tested, an agent that could not load its configuration
allowed everything until it could, and the default deployment gave
Kubernetes no readiness signal for it.

Full report, manifests, scripts and raw evidence with SHA-256
checksums: https://github.com/zaclohrenz/fastly-ngwaf-poc

3. Detection
------------

  - Agent container spec: look for SIGSCI_STARTUP_PROBE_LISTENER or
    SIGSCI_STARTUP_PROBE_FILEPATH AND a startupProbe on the agent
    container that checks it. If either is missing, the deployment is
    exposed. The env var alone does nothing.
  - Backend logs: search request headers for "X-SigSci-Agent:
    disabled". Requests that passed while the socket was missing carry
    no X-SigSci-* header and will not show up this way.
  - Agent logs: "Config update failed" near pod starts.
  - Ingress controller logs: "cannot connect uds socket" from the
    sigsci module.

4. Mitigation
-------------

On agent 4.52.0 or later, configure the startup probe:

  containers:
    - name: sigsci-agent
      ports:
        - name: "startup-port"
          containerPort: 2024
      env:
        - name: SIGSCI_STARTUP_PROBE_LISTENER
          value: "0.0.0.0:2024"
      startupProbe:
        httpGet:
          path: /startup
          port: startup-port
        failureThreshold: 90
        periodSeconds: 2

The endpoint returns 503 until rules are loaded. Size failureThreshold
x periodSeconds for the slowest realistic rule fetch; a pod that cannot
load rules within that time is restarted by the kubelet.

Fastly'...