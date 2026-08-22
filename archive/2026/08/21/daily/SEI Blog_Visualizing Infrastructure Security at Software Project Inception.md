---
title: Visualizing Infrastructure Security at Software Project Inception
url: https://www.sei.cmu.edu/blog/visualizing-infrastructure-security-at-software-project-inception/?utm_source=blog&utm_medium=rss&utm_campaign=my_site_updates
source: SEI Blog
date: 2026-08-21
fetch_date: 2026-08-22T02:52:33.569871
---

# Visualizing Infrastructure Security at Software Project Inception

icon-carat-right

menu

search

cmu-wordmark

[Carnegie Mellon University

cmu-wordmark](https://www.cmu.edu)

About

Research and Development

Publications and Media

Education

Careers

Search

Mobile Menu

[# SEI Blog](/blog/)

1. [Home](/)
2. [Publications and Media](/publications-media/)
3. [Blog](/blog/)
4. Visualizing Infrastructure Security at Software Project Inception

[ ]

### Cite This Post

×

* [AMS](#amsTab)
* [APA](#apaTab)
* [Chicago](#chicagoTab)
* [IEEE](#ieeeTab)
* [BibTeX](#bibTextTab)

AMS Citation

Antunes, L., 2026: Visualizing Infrastructure Security at Software Project Inception. Software Engineering Institute blog, Accessed August 22, 2026, https://doi.org/10.58012/ssfc-qj88.

Copy

APA Citation

Antunes, L. (2026, August 21). Visualizing Infrastructure Security at Software Project Inception. Retrieved August 22, 2026, from https://doi.org/10.58012/ssfc-qj88.

Copy

Chicago Citation

Antunes, Luiz. "Visualizing Infrastructure Security at Software Project Inception." *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, August 21, 2026. https://doi.org/10.58012/ssfc-qj88.

Copy

IEEE Citation

L. Antunes, "Visualizing Infrastructure Security at Software Project Inception," *Software Engineering Institute blog*. Carnegie Mellon's Software Engineering Institute, 21-Aug-2026 [Online]. Available: https://doi.org/10.58012/ssfc-qj88. [Accessed: 22-Aug-2026].

Copy

BibTeX Code

```
@misc{antunes_2026,
author={Antunes, Luiz},
title={Visualizing Infrastructure Security at Software Project Inception},
month={Aug},
year={2026},
institution={Software Engineering Institute blog},
doi={10.58012/ssfc-qj88},
url={https://doi.org/10.58012/ssfc-qj88},
note={Accessed: 2026-Aug-22}
}
```

Copy

# Visualizing Infrastructure Security at Software Project Inception

![Headshot of Luiz Antunes.](/media/images/Antunes_Luiz_018_250417.max-180x180.format-webp.webp)

###### [Luiz Antunes](/authors/luiz-antunes)

###### August 21, 2026

##### PUBLISHED IN

[Continuous Deployment of Capability](/blog/topics/continuous-deployment-capability/)

##### CITE

<https://doi.org/10.58012/ssfc-qj88>

Get Citation

##### SHARE

The earliest stage of a software project carries engineering risks that are easy to overlook. The software does not yet exist, and the team is busy standing up infrastructure: provisioning servers, writing automation scripts, configuring access controls, and establishing the scaffolding that everything else will run on. The code that does this work—Terraform templates, Ansible playbooks, shell scripts, Dockerfiles—is software too, and it has vulnerabilities.

The potential issue at this stage is specific: *Scripts that create infrastructure can be exploited to open back doors*. A misconfigured Identity and Access Management (IAM) role, an exposed port left open in a provisioning script, or an unpatched base image can quietly become an entry point that persists through every phase of the lifecycle that follows. Because these issues are introduced before development begins in earnest, they tend not to appear in the usual development metrics—no sprint tickets, no code review comments. They can sit undetected for a long time.

The good news is that project inception is one of the most instrumentation-friendly stages in the entire lifecycle. As this post illustrates, vulnerability scanning is a well-understood problem with mature tooling, and the output of that tooling is exactly the kind of structured, time-series data that lends itself to effective visualization.

## What to Measure

The useful metric at the inception and project configuration stage is the *infrastructure vulnerability report*: This is a record of which known vulnerabilities ([CVEs](https://www.cve.org/)) are present in your infrastructure, at what levels of severity, and how that picture is changing over time.

A single vulnerability report is a snapshot. What we really want is a series of snapshots—one per scan—so we can answer questions like the following:

* Are new vulnerabilities appearing faster than we are resolving them?
* Is a particular CVE recurring after we thought it was patched?
* Are certain components consistently responsible for the bulk of our exposure?

The time dimension is what turns a security report into a monitoring tool.

## The Visualization: A CVE Presence Heat Map

One of the most effective ways to display this information is through a **heat map** with CVEs on one axis and scan dates on the other. In this visualization, each cell represents whether a given vulnerability was detected on a given date, and the cell's color encodes its severity. The result resembles something like the heat map in Figure 1.

[![figure1_08202026](/media/images/figure1_08202026.max-1280x720.format-webp.webp)](/media/images/figure1_08202026.original.png)

H = High severity (red), M = Medium (orange), L = Low (yellow), [ ] = not detected

What makes this format powerful is that it exposes patterns that a static snapshot cannot. A row where the same CVE lights up on alternating dates suggests a remediation that is not sticking—the vulnerability is being patched and reintroduced. A column that goes suddenly dense with high-severity findings suggests that a base image update introduced a batch of new issues. A CVE that appears once and never again is almost certainly resolved; one that keeps appearing is a candidate for escalation.

The human visual system is exceptionally good at detecting these kinds of patterns in a grid. Presented as a sorted table of CVE IDs and severity scores, the same data would require careful reading. Presented as a heat map, the patterns are immediately visible.

Please note that in the illustration above the CVE change rate is artificially shown as occurring daily to show how the visualization should work. In reality, changes are more subtle and spaced in time. The actual rate increases based on the number of dependencies within a project. Any changes to the number of dependencies within a project may result in increased vulnerabilities.

## Getting the Data

If you want to play with this visualization, you will need two things: a vulnerability scanner and a way to store its output over time.

### Scanning your infrastructure with Trivy

[Trivy](https://github.com/aquasecurity/trivy) is a free, open-source vulnerability scanner that works against container images, filesystems, Git repositories, and infrastructure as code (IaC) files (e.g., Terraform, Dockerfile, Helm charts). It produces structured JSON output that maps directly to what we need.

To scan a container image, type the command

```
trivy image --format json --output results.json your-base-image:latest
```

Similarly, to scan an IaC directory, you can type

```
trivy config --format json --output results.json ./infrastructure/
```

The JSON output includes CVE IDs, severity ratings, affected packages, and fix availability. A lightweight Python script can parse this output and append a dated record to a running log—one row per CVE per scan date.

### Building the Time-series Log

The goal of the following code sample is to demonstrate one path to accomplishing an action. To incorporate it into production and capture any additional conditions, it would most likely have to be developed further.

```
import json
import csv
from datetime import date

def append_scan_results(results_file, log_file):
    scan_date = date.today().isoformat()

    with open(results_file) as f:
        results = json.load(f)

    rows = []
    for result in results.get("Results", []):
        for vuln in result.get("Vulnerabilities", []):
            rows.append({
                "date": scan_date,
                "cve_id": vuln.get("VulnerabilityID"),
                "severity": vuln.get("Severity"),
                "package": vuln.get("PkgName"),
                "fixed_version": vuln.get("FixedVersion", "none")
            })

    if not rows:
        print("No vulnerabilit...