---
title: Inspektor Gadget Security Audit
url: https://www.shielder.com/blog/2026/04/inspektor-gadget-security-audit/
source: Blog on Shielder
date: 2026-04-30
fetch_date: 2026-05-01T05:39:54.470562
---

# Inspektor Gadget Security Audit

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage")

* [Home](https://www.shielder.com/ "Home")
* [Company](https://www.shielder.com/company "Company")
* [Services](https://www.shielder.com/services "Services")
* [Advisories](https://www.shielder.com/advisories "Advisories")
* [Blog](https://www.shielder.com/blog "Blog")
* [Careers](https://www.shielder.com/careers "Careers")
* [Contacts](https://www.shielder.com/contacts "Contacts")
* ENG

  [ENG](https://www.shielder.com/blog/2026/04/inspektor-gadget-security-audit/ "ENG")
  [ITA](https://www.shielder.com/it/blog/2026/04/inspektor-gadget-security-audit/ "ITA")

# Inspektor Gadget Security Audit

## TL;DR

In early 2026, Shielder was hired by [OSTIF](https://ostif.org/) to perform a security audit of [Inspektor Gadget](https://github.com/inspektor-gadget/inspektor-gadget), an eBPF-based framework that provides powerful and flexible observability tools for Kubernetes and Linux hosts.

**Today, we are publishing the [full report](https://github.com/ShielderSec/public-reports/blob/main/2026/%5BOSTIF%5D%20Inspektor%20Gadget%20-%20Report%20v1.2.pdf) in our [dedicated repository](https://github.com/ShielderSec/public-reports/)**.

## Context

Inspektor Gadget is both a framework and a toolkit to enhance observability on a Linux machine/Kubernetes node, using the eBPF technology. Inspektor Gadget manages the packaging, deployment and execution of “gadgets”, which are essentially eBPF programs encapsulated in OCI images. Gadgets export events that are caught by the tool and that can be filtered, sorted, exported or enriched.

See it in action:

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` $ kubectl gadget run trace_open:latest --podname mypod K8S.NODE           K8S.NAMESPACE K8S.PODNAME   K8S.CONTAINEâ¦ COMM        PID     TID      FD FNAME                    MODE    ERROR minikube-docker    default       mypod         mypod         true     511559  511559       0 /etc/ld.so.cache         ------â¦ ENOEN minikube-docker    default       mypod         mypod         true     511559  511559       0 /lib/x86_64-linux-gnu/gâ¦ ------â¦ ENOEN minikube-docker    default       mypod         mypod         true     511559  511559       0 /lib/x86_64-linux-gnu/gâ¦ ------â¦ ENOEN minikube-docker    default       mypod         mypod         true     511559  511559       0 /lib/x86_64-linux-gnu/tâ¦ ------â¦ ENOEN minikube-docker    default       mypod         mypod         true     511559  511559       0 /lib/x86_64-linux-gnu/tâ¦ ------â¦ ENOEN minikube-docker    default       mypod         mypod         true     511559  511559       0 /lib/x86_64-linux-gnu/tâ¦ ------â¦ ENOEN minikube-docker    default       mypod         mypod         true     511559  511559       0 /lib/x86_64-linux-gnu/tâ¦ ------â¦ ENOEN minikube-docker    default       mypod         mypod         true     511559  511559       0 /lib/x86_64-linux-gnu/xâ¦ ------â¦ ENOEN minikube-docker    default       mypod         mypod         true     511559  511559       0 /lib/x86_64-linux-gnu/xâ¦ ------â¦ ENOEN minikube-docker    default       mypod         mypod         true     511559  511559       0 /lib/x86_64-linux-gnu/xâ¦ ------â¦ ENOEN minikube-docker    default       mypod         mypod         true     511559  511559       0 /lib/x86_64-linux-gnu/lâ¦ ------â¦ ENOEN ... minikube-docker    default       mypod         mypod         whoami   511560  511560       0 /lib/x86_64/libm.so.6    ------â¦ ENOEN minikube-docker    default       mypod         mypod         whoami   511560  511560       3 /lib/libm.so.6           ------â¦ minikube-docker    default       mypod         mypod         whoami   511560  511560       3 /lib/libresolv.so.2      ------â¦ minikube-docker    default       mypod         mypod         whoami   511560  511560       3 /lib/libc.so.6           ------â¦ minikube-docker    default       mypod         mypod         whoami   511560  511560       3 /etc/passwd              ------â¦ ^C ``` |

Before starting the audit, we sit with the maintainers for a collaborative threat modeling session. With open source projects, we have found this to be crucial: just looking at the code often does not yield the most interesting information, that is, **how end-users install, configure and use the project**.

As a result, two main points emerged:

1. In order to load eBPF code in the kernel, Inspektor Gadget needs a privileged account/role in the system (typically `root`, or at the very least, the all-powerful `CAP_SYS_ADMIN` capability). This makes it a clear target for privilege escalation scenarios, both on standalone Linux hosts and Kubernetes clusters.
2. Inspektor Gadget provides ready-to-use gadgets (such as the `trace_open` used in the example above). One of the main reasons operators might want observability in their cluster is to build security monitoring; but if the tracing can be bypassed, attackers could execute operations on the host without generating events/alerts.

With these attack scenarios in mind, we have performed the audit by combining manual and AI-assisted analysis, dynamic testing, and usage of SAST tooling such as `semgrep` and `gosec`.

## Findings

While auditing, we have discovered three vulnerabilities (two with Medium severity, one with Low) that we reported through the project [Github Security](https://github.com/inspektor-gadget/inspektor-gadget/security/advisories?state=published) portal:

**Command Injection in `ig build`**

Inspektor Gadget provides the tooling to build, push and pull custom gadgets ([https://inspektor-gadget.io/docs/latest/gadget-devel/)](https://inspektor-gadget.io/docs/latest/gadget-devel/%29). The building flow uses `Makefile` variable interpolation, which is prone to command injections, if an attacker controls some of the variables that are used to build new gadgets.
This could be leveraged by attackers, for instance, to gain code execution in CI/CD runners. The severity was set to Medium/Moderate, given the added complexity of controlling the build variables.

The maintainers fixed this in version `v0.51.1` by refactoring the building process to use Golang machinery rather than Makefiles.

**Denial of Service via Event Flooding**

Inspektor Gadget captures all the events coming from deployed gadgets in a single kernel ring-buffer, with a size that is hard-coded to 256KB. When the gadgets push more events than what the user-space collector can handle, this buffer can be filled completely, leading to new events being dropped. Inspektor Gadget silently ignored those dropped packets, which would allow an attacker to first produce many harmless events to flood the buffer, and then perform malicious operations that would not be caught by any gadget. The severity was set to Medium/Moderate, as this only affects the integrity of the observation pipeline.

The maintainers fixed this by implementing a map of dropped packets to detect when events are being lost, so that users can build alerts on top of this limitation.

**Unsanitized ANSI Escape Sequences in Columns Output Mode**

When displaying gadget events through a terminal using the default output formatter, there was no sanitization of control characters of ANSI escape sequences. Therefore, an attacker in a container could craft malicious events (for instance, by opening/creating files with controlled names) to inject these in the terminal. The impact depends on what terminal is used - at the very least, it could be used to inject new logs or delete existing ones. The severity was set to Low, as this already required a compromised pod in the cluster, and the exploitability highly varies on the terminal used.

The maintainers fixed this by sanitizing the text before sending it to the terminal.

**Hardenings**

During the audit, we gathered some recommendations for the project to improve its security posture:

...