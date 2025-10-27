---
title: Introducing Proxy Enriched Sequence Diagrams (PESD)
url: https://blog.doyensec.com//2023/02/14/pesd-extension-public-release.html
source: Over Security - Cybersecurity news aggregator
date: 2023-02-18
fetch_date: 2025-10-04T07:25:08.088896
---

# Introducing Proxy Enriched Sequence Diagrams (PESD)

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# Introducing Proxy Enriched Sequence Diagrams (PESD)

14 Feb 2023 - Posted by Francesco Lacerenza

### PESD Exporter is now public!

We are releasing an internal tool to speed-up testing and reporting efforts in complex functional flows. Weâre excited to announce that PESD Exporter is nowÂ [available on Github](https://github.com/doyensec/PESD-Exporter-Extension).

![pesdExporter](../../../public/images/pesd.png)

Modern web platforms design involves integrations with other applications and cloud services to add functionalities, share data and enrich the user experience. The resulting functional flows are characterized by multiple state-changing steps with complex trust boundaries and responsibility separation among the involved actors.

In such situations, web security specialists have to manually model sequence diagrams if they want to support their analysis with visualizations of the whole functionality logic.

We all know that constructing sequence diagrams by hand is *tedious*, *error-prone*, *time-consuming* and sometimes even *impractical* (dealing with more than ten messages in a single flow).

**Proxy Enriched Sequence Diagrams** (**PESD**) is our internal Burp Suite extension to visualize web traffic in a way that facilitates the analysis and reporting in scenarios with complex functional flows.

## Meet The Format

A *Proxy Enriched Sequence Diagram* (*PESD*) is a specific message syntax for sequence diagram models adapted to bring enriched information about the represented HTTP traffic. The [MermaidJS](https://github.com/mermaid-js/mermaid) sequence diagram syntax is used to render the final diagram.

While classic sequence diagrams for software engineering are meant for an abstract visualization and all the information is carried by the diagram itself. PESD is designed to include granular information related to the underlying HTTP traffic being represented in the form of metadata.

The `Enriched` part in the format name originates from the `diagram-metadata linkability`. In fact, the HTTP events in the diagram are marked with flags that can be used to access the specific information from the metadata.

As an example, URL query parameters will be found in the arrow events as `UrlParams` expandable with a click.

![pesdExporter](../../../public/images/welcometopesd.png)

Some key characteristics of the format :

* *visual-analysis*, especially useful for complex application flows in multi-actor scenarios where the listed proxy-view is not suited to visualize the abstract logic
* *tester-specific syntax* to facilitate the analysis and overall readability
* *parsed metadata* from the web traffic to enable further automation of the analysis
* *usable for reporting* purposes like documentation of current implementations or Proof Of Concept diagrams

## PESD Exporter - Burp Suite Extension

The extension handles Burp Suite traffic conversion to the PESD format and offers the possibility of executing templates that will enrich the resulting exports.

![pesdExporter](../../../public/images/pesdextensionui.png)

Once loaded, sending items to the extension will directly result in a export with all the active settings.

Currently, two modes of operation are supported:

* **Domains as Actors** - Each domain involved in the traffic is represented as an actor in the diagram. Suitable for `multi-domain` flows analysis

![pesdExporter](../../../public/images/domainsasactors.png)

* **Endpoints as Actors** - Each endpoint (path) involved in the traffic is represented as an actor in the diagram. Suitable for `single-domain` flows analysis

![pesdExporter](../../../public/images/endpointsasactors.png)

### Export Capabilities

* **Expandable Metadata**. Underlined flags can be clicked to show the underlying metadata from the traffic in a scrollable popover
* **Masked Randoms in URL Paths**. UUIDs and pseudorandom strings recognized inside path segments are mapped to variable namesÂ `<UUID_N>`Â /Â `<VAR_N>`. The re-renderization will reshape the diagram to improve flow readability. Every occurrence with the same value maintains the same name
* **Notes**. Comments from Burp Suite are converted to notes in the resulting diagram. Use `<br>` in Burp Suite comments to obtain multi-line notes in PESD exports
* **Save as** :

  + Sequence Diagram in `SVG` format
  + `Markdown` file (MermaidJS syntax),
  + Traffic `metadata` in `JSON` format. Read about the metadata structure in the format definition page,Â [âexports sectionâ](https://github.com/doyensec/PESD-Exporter-Extension/blob/main/mds/Format.md#exports)

[![

Your browser does not support the video tag.
](../../../public/images/pesdexport.png)](../../../public/images/pesdexport.mp4)

### Extending the diagram, syntax and metadata with Templates

PESD Exporter supports syntax and metadata extension via templates execution.
Currently supported templates are:

* **OAuth2 / OpenID Connect**Â The template matches standard OAuth2/OpenID Connect flows and adds related flags + flow frame
* **SAML SSO** The template matches Single-Sign-On flows with SAML V2.0 and adds related flags + flow frame

Template matching example for *SAML SP-initiated SSO with redirect POST*:

![pesdExporter](../../../public/images/pesdsamlex.png)

The template engine is also ensuring consistency in the case of crossing flows and bad implementations. The current check prevents nested flow-frames since they cannot be found in real-case scenarios. Nested or unclosed frames inside the resulting markdown are deleted and merged to allow MermaidJS renderization.

**Note:** Whenever the flow-frame is not displayed during an export involving the supported frameworks, a manual review is highly recommended. This behavior should be considered as a warning that the application is using a non-standard implementation.

Do you want to contribute by writing you own templates? Follow the [template implementation guide](https://github.com/doyensec/PESD-Exporter-Extension/blob/main/mds/WritingTemplates.md).

## Why PESD?

### During Test Planning and Auditing

PESD exports allow visualizing the entirety of complex functionalities while still being able to access the core parts of its underlying logic. The role of each actor can be easily derived and used to build a test plan before diving in Burp Suite.

It can also be used to spot the differences with standard frameworks thanks to the HTTP messages syntax along with OAuth2/OpenID and SAML SSO templates.

In particular, templates enable the tester to identify uncommon implementations by matching standard flows in the resulting diagram. By doing so, custom variations can be spotted with a glance.

The following detailed examples are extracted from our testing activities:

* **SAML Response Double Spending**. The SAML Response was sent two times and one of the submissions happened out of the flow frame

![pesdExporter](../../../public/images/doublespendingSAML.png)

* **OIDC with subsequent OAuth2**. In this case, CLIENT.com was the SP in the first flow with Microsoft (OIDC), then it was the IdP in the second flow (OAuth2) with the tenant subdomain.

![pesdExporter](../../../public/images/pesdoidcexample.png)

### During Reporting

The major benefit from the research output was the conjunction of the diagrams generated with PESD with the analysis of the vulnerability. The inclusion of PoC-specific exports in reports allows to describe the issue in a straightforw...