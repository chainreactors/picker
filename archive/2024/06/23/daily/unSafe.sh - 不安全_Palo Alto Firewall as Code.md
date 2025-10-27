---
title: Palo Alto Firewall as Code
url: https://buaq.net/go-246718.html
source: unSafe.sh - 不安全
date: 2024-06-23
fetch_date: 2025-10-06T16:55:05.304413
---

# Palo Alto Firewall as Code

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/12235cf340c2af85407c0caeaf2e5ca3.jpg)

Palo Alto Firewall as Code

It has been about 6 years since the Automate IT² event organized by me and Gabriele Gerbino. During
*2024-6-22 21:16:35
Author: [www.adainese.it(查看原文)](/jump-246718.htm)
阅读量:23
收藏*

---

[![Post cover](https://www.adainese.it/blog/2024/06/22/palo-alto-firewall-as-code/cover.webp)](https://www.adainese.it/blog/2024/06/22/palo-alto-firewall-as-code/cover.webp)

It has been about 6 years since the [Automate IT²](https://automateit2.com/ "Automate IT²") event organized by me and [Gabriele Gerbino](https://www.linkedin.com/in/gabrielegerbino/ "Gabriele Gerbino"). During the event, [Xavier Homes](https://www.linkedin.com/in/xhoms/ "Xavier Homes") presented a case that fascinated me. Today we might call it: Firewall as Code.

My interest was not just in the elegance of the solution but also in the practical implications for operations and security.

For several years, I managed firewalls and now, as a consultant, I see many client implementations. All the installations I encounter have the same problems:

* Hundreds of rules;
* Each rule is built based on the perception of the operator who creates it;
* No clear understanding, except for a brief description, of the origin and evolution of the rule;
* Likely obsolete rules remain configured because no one can confirm if they are necessary or not;
* Rules refer to decommissioned or reused systems, thereby introducing undefined risks;
* Rules are grouped and simplified solely to make operations easier (without any security assessment);
* Constant requests to add new rules without fully understanding what an application should or should not do;
* Impossibility to review due to the reasons above and because the rules change continuously;
* Enormous operational time spent managing the firewalls;
* No one can say if the policies comply with any security directives the company should have.

While there is software intended to solve the above problems, these solutions are often:

* Another patch for poorly designed processes;
* Complicated to use;
* So expensive that they are not economically sustainable for most companies.

Let’s start from scratch by designing a process that addresses the problems described above, from which (and not the other way around) we derive a technology that allows us to manage our firewalls.

In the example shown, I used Palo Alto Networks firewalls. The reasons for this choice are:

* I am quite familiar with them;
* They have a configuration entirely exportable in text format (XML in particular);
* I can manipulate the configuration file and then apply it entirely at a later stage (commit).

The approach we will see should be applicable to all firewalls that meet these three properties.

## The Process

The process I want to design is very simple:

1. Application managers define the operating rules of their applications in terms of necessary traffic flows;
2. Security managers define high-level traffic policies between different security zones, based on a risk assessment;
3. Security architects design, implement, and oversee the firewall solutions;
4. Automation takes the requirements from (1), applies the constraints defined in (2), generates the rule base, and applies it to the firewalls. The operational activities of the security architects are limited to what is defined in (3).

Specifically, application managers must define network requirements through files and make them available along with the application’s code or documentation (Git would be a good tool, but not the only one). Daily or on request, the automation updates the policies.

## The Model

As always, the modeling phase takes the most time. In the example, I assumed that:

* The definition of services in terms of protocol/port/application is centralized and managed by the security architects. The reason is that choosing the application associated with a specific port requires specific knowledge of the firewall solution.
* The definition of security zones and their relationship with networks is centralized and managed by the security architects. The reason is that the concept of a security zone is linked to network design.
* Settings like logging and security profiles are managed by the security architects.
* Each application’s definition is done via two files: `networks.yml` and `rules.yml`. The maintenance of both files is the responsibility of the application manager.

Here’s an example:

```
# networks.yml
networks:
  WWW:
    - 10.20.1.7/32
  APP:
    - 10.20.2.15/32
  DB:
    - 10.20.2.23/32
```

The above file defines three objects: `WWW`, `APP`, `DB`.

```
rules:
  - destination-address: WWW
    service: HTTP
    description: |
      Allow HTTP external traffic to exposed web server.
  - destination-address: WWW
    service: HTTPS
    description: |
      Allow HTTPS external traffic to exposed web server.
  - source-address: WWW
    destination-address: APP
    service: HTTPS_8443
    description: |
      Allow traffic from exposed web server to application server.
  - source-address: APP
    destination-address: DB
    service: MYSQL
    description: |
      Allow traffic from application server to database server.
```

The above file defines the rules for a specific application. Services are defined in the centralized `services.yml` file:

```
services:
  HTTP:
    applications: web-browsing
  HTTPS:
    applications: ssl
  HTTPS_8443:
    protocol: tcp
    port: 8443
    applications: ssl
  MYSQL:
    applications: mysql
```

Security zones are mapped based on the rules defined in the `network-zone_mapping.yml` file:

```
zones:
  servers:
    type: internal
    networks:
      - 10.20.2.0/24
  dmz:
    type: internal
    networks:
      - 10.20.1.0/24
  # Internet (catch all)
  internet:
    type: external
    networks:
      - 0.0.0.0/0
```

## Implementation Approach

To summarize the key points of the approach:

* Security architects need to be able to configure the firewalls in detail, and it’s unthinkable to replicate an interface with all necessary settings;
* Application managers need to be able to abstractly define traffic rules.

The most practical approach is therefore:

1. Read the updated configuration from the firewall;
2. Delete all traffic rules and associated objects;
3. Regenerate rules and objects from the files described above and add them to the cleaned configuration;
4. Validate the configuration;
5. Apply the configuration.

The advantage of this approach is clear: I never have to worry about checking if an object exists, if it is correct, or if it is in the right position. This greatly simplifies the implementation.

There are, of course, disadvantages or constraints:

* Rules must be written so that order does not matter;
* All rules must be defined by the files described above.

Exceptions can obviously be made, but each special case will complicate the implementation.

Once the model is defined, a tool must be chosen to translate the model into an actual configuration. In my evaluation, I focused on:

* [Aerleon](https://github.com/aerleon/aerleon "Aerleon") (formerly [Google Carpica](https://github.com/google/capirca "Google Carpica"))
* [pan-os-python](https://github.com/PaloAltoNetworks/pan-os-python "pan-os-python"): official libraries developed by Palo Alto Networks
* [pan-python](https://github.com/kevinsteves/pan-python "pan-python"): privately developed libraries on which `pan-os-python` is based (interesting, isn’t it?)
* [PAN-OS XML API](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-panorama-api/get-started-with-the-pan...