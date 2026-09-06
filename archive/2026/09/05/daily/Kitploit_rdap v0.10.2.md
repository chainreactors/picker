---
title: rdap v0.10.2
url: https://kitploit.com/en/posts/github-openrdap-rdap-v0102
source: Kitploit
date: 2026-09-05
fetch_date: 2026-09-06T06:39:29.126040
---

# rdap v0.10.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/41644/e84a5895278d6c54bc0bda92a87d71464ce4a5d80c204361a8e66874f51f3fe0.png)

New releaseSep 5, 2026

# rdap v0.10.2

Go-based RDAP command-line client for querying domain, IP, ASN, and entity registration data with automatic server detection and multiple output formats.

Share

![](https://assets.kitploit.com/production/public/readmes/41644/e8b627eca2fd3a2efa38e27f362b884336152683654a325c9e18fbf27092a599.png)

OpenRDAP is a command line [RDAP](https://datatracker.ietf.org/wg/weirds/documents/) client implementation in Go.
[![Build Status](https://travis-ci.org/openrdap/rdap.svg?branch=master)](https://travis-ci.org/openrdap/rdap)

<https://www.openrdap.org> - homepage

<https://www.openrdap.org/demo> - live demo

## Features

* Command line RDAP client
* Output formats: text, JSON, WHOIS style
* Query types supported:
  + ip
  + domain
  + autnum
  + nameserver
  + entity
  + help
  + url
  + domain-search
  + domain-search-by-nameserver
  + domain-search-by-nameserver-ip
  + nameserver-search
  + nameserver-search-by-ip
  + entity-search
  + entity-search-by-handle
* Automatic server detection for ip/domain/autnum/entities
* Object tags support
* Bootstrap cache (optional, uses $XDG\_CACHE\_HOME/openrdap by default, falling back to ~/.cache/openrdap)
* X.509 client authentication

## Installation

This program uses Go. The Go compiler is available from <https://golang.org/>.

To install:

root@kitploit:~

```
go install github.com/openrdap/rdap/cmd/rdap@master
```

This will install the "rdap" binary in your $GOPATH/go/bin directory. Try running:

root@kitploit:~

```
~/go/bin/rdap google.com
```

## Usage

| Query type | Usage |
| --- | --- |
| Domain (.com) | rdap -v example.com |
| IPv4 Address | rdap -v 192.0.2.0 |
| IPv6 Address | rdap -v 2001:db8:: |
| Autonomous System (ASN) | rdap -v AS15169 |
| Entity (with object tag) | rdap -v OPS4-RIPE |

## Advanced usage (server must be specified using -s; not all servers support all query types)

| Query type | Usage |
| --- | --- |
| Nameserver | rdap -v -t nameserver -s <https://rdap.verisign.com/com/v1> ns1.google.com |
| Help | rdap -v -t help -s <https://rdap.verisign.com/com/v1> |
| Domain Search | rdap -v -t domain-search -s $SERVER\_URL example\*.gtld |
| Domain Search (by NS) | rdap -v -t domain-search-by-nameserver -s $SERVER\_URL ns1.example.gtld |
| Domain Search (by NS IP) | rdap -v -t domain-search-by-nameserver-ip -s $SERVER\_URL 192.0.2.0 |
| Nameserver Search | rdap -v -t nameserver-search -s $SERVER\_URL ns1.example.gtld |
| Nameserver Search (by IP) | rdap -v -t nameserver-search-by-ip -s $SERVER\_URL 192.0.2.0 |
| Entity Search | rdap -v -t entity-search -s $SERVER\_URL ENTITY-TAG |
| Entity Search (by handle) | rdap -v -t entity-search-by-handle -s $SERVER\_URL ENTITY-TAG |

See <https://www.openrdap.org/docs>.

## Example output

Click the examples to see the output:

rdap example.com

root@kitploit:~

```
  Domain Name: EXAMPLE.COM
  Handle: 2336799_DOMAIN_COM-VRSN
  Status: client delete prohibited
  Status: client transfer prohibited
  Status: client update prohibited
  Conformance: rdap_level_0
  Conformance: icann_rdap_technical_implementation_guide_0
  Conformance: icann_rdap_response_profile_0
  Notice:
    Title: Terms of Use
    Description: Service subject to Terms of Use.
    Link: https://www.verisign.com/domain-names/registration-data-access-protocol/terms-service/index.xhtml
  Notice:
    Title: Status Codes
    Description: For more information on domain status codes, please visit https://icann.org/epp
    Link: https://icann.org/epp
  Notice:
    Title: RDDS Inaccuracy Complaint Form
    Description: URL of the ICANN RDDS Inaccuracy Complaint Form: https://icann.org/wicf
    Link: https://icann.org/wicf
  Link: https://rdap.verisign.com/com/v1/domain/EXAMPLE.COM
  Event:
    Action: registration
    Date: 1995-08-14T04:00:00Z
  Event:
    Action: expiration
    Date: 2023-08-13T04:00:00Z
  Event:
    Action: last changed
    Date: 2023-05-12T15:13:35Z
  Event:
    Action: last update of RDAP database
    Date: 2023-05-16T20:36:06Z
  Secure DNS:
    Delegation Signed: true
    DSData:
      Key Tag: 370
      Algorithm: 13
      Digest: BE74359954660069D5C63D200C39F5603827D7DD02B56F120EE9F3A86764247C
      DigestType: 2
  Entity:
    Handle: 376
    Public ID:
      Type: IANA Registrar ID
      Identifier: 376
    Role: registrar
    vCard version: 4.0
    vCard fn: RESERVED-Internet Assigned Numbers Authority
    Entity:
      Role: abuse
      vCard version: 4.0
  Nameserver:
    Nameserver: A.IANA-SERVERS.NET
  Nameserver:
    Nameserver: B.IANA-SERVERS.NET
```

rdap 8.8.8.8

root@kitploit:~

```
  Handle: NET-8-8-8-0-1
  Start Address: 8.8.8.0
  End Address: 8.8.8.255
  IP Version: v4
  Name: LVLT-GOGL-8-8-8
  Type: ALLOCATION
  ParentHandle: NET-8-0-0-0-1
  Status: active
  Port43: whois.arin.net
  Notice:
    Title: Terms of Service
    Description: By using the ARIN RDAP/Whois service, you are agreeing to the RDAP/Whois Terms of Use
    Link: https://www.arin.net/resources/registry/whois/tou/
  Notice:
    Title: Whois Inaccuracy Reporting
    Description: If you see inaccuracies in the results, please visit:
    Link: https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
  Notice:
    Title: Copyright Notice
    Description: Copyright 1997-2023, American Registry for Internet Numbers, Ltd.
  Entity:
    Handle: GOGL
    Port43: whois.arin.net
    Remark:
      Title: Registration Comments
      Description: Please note that the recommended way to file abuse complaints are located in the following links.
      Description: To report abuse and illegal activity: https://www.google.com/contact/
      Description: For legal requests: http://support.google.com/legal
      Description: Regards,
      Description: The Google Team
    Link: https://rdap.arin.net/registry/entity/GOGL
    Link: https://whois.arin.net/rest/org/GOGL
    Event:
      Action: last changed
      Date: 2019-10-31T15:45:45-04:00
    Event:
      Action: registration
      Date: 2000-03-30T00:00:00-05:00
    Role: registrant
    vCard version: 4.0
    vCard fn: Google LLC
    vCard kind: org
    Entity:
      Handle: ABUSE5250-ARIN
      Status: validated
      Port43: whois.arin.net
      Remark:
        Title: Registration Comments
        Description: Please note that the recommended way to file abuse complaints are located in the following links.
        Description: To report abuse and illegal activity: https://www.google.com/contact/
        Description: For legal requests: http://support.google.com/legal
        Description: Regards,
        Description: The Google Team
      Link: https://rdap.arin.net/registry/entity/ABUSE5250-ARIN
      Link: https://whois.arin.net/rest/poc/ABUSE5250-ARIN
      Event:
        Action: last changed
        Date: 2022-10-24T08:43:11-04:00
      Event:
        Action: registration
        Date: 2015-11-06T15:36:35-05:00
      Role: abuse
      vCard version: 4.0
      vCard fn: Abuse
      vCard org: Abuse
      vCard kind: group
      vCard email: [email protected]
      vCard tel: +1-650-253-0000
    Entity:
      Handle: ZG39-ARIN
      Status: validated
      Port43: whois.arin.net
      Link: https://rdap.arin.net/registry/entity/ZG39-ARIN
      Link: https://whois.arin.net/rest/poc/ZG39-ARIN
      Event:
        Action: last changed
        Date: 2022-11-10T07:12:44-05:00
      Event:
        Action: registration
        Date: 2000-11-30T13:54:08-05:00
      Role: technical
      Role: administrative
      vCard version: 4.0
      vCard...