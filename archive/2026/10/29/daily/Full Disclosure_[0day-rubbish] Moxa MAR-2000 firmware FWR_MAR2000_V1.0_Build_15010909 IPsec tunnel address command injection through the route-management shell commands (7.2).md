---
title: [0day-rubbish] Moxa MAR-2000 firmware FWR_MAR2000_V1.0_Build_15010909 IPsec tunnel address command injection through the route-management shell commands (7.2)
url: https://seclists.org/fulldisclosure/2026/Oct/53
source: Full Disclosure
date: 2026-10-29
fetch_date: 2026-10-30T07:56:40.377246
---

# [0day-rubbish] Moxa MAR-2000 firmware FWR_MAR2000_V1.0_Build_15010909 IPsec tunnel address command injection through the route-management shell commands (7.2)

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

[![Previous](/images/left-icon-16x16.png)](52)
[By Date](date.html#53)
[![Next](/images/right-icon-16x16.png)](55)

[![Previous](/images/left-icon-16x16.png)](52)
[By Thread](index.html#53)
[![Next](/images/right-icon-16x16.png)](55)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Moxa MAR-2000 firmware FWR\_MAR2000\_V1.0\_Build\_15010909 IPsec tunnel address command injection through the route-management shell commands (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 27 Oct 2026 16:39:01 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in the Moxa
MAR-2000 series industrial 4G/LTE cellular router, firmware image
FWR_MAR2000_V1.0_Build_15010909, from Moxa Inc. (Taiwan). An authenticated
administrator converts one stored VPN address field into arbitrary command
execution as the identity of the product's model process, because the IPsec
model manages the tunnel's addresses and routes by interpolating stored,
never-validated configuration values into shell command lines. The payload
is committed by one request and executes at a lifecycle moment the product
performs on its own. This is one of three independent command injection
findings documented for this product and released together as a set.

Type and root cause. CWE-78, OS command injection, with CWE-20 co-equal, in
the IPsec model at /home/model/network/ipsec/ipsec.py inside the ARM
Debian 6.0.8 root filesystem of the firmware, which runs the vendor's MIRF
(Mobile Intelligent Routing Framework) stack: a Node.js Express 4.0
management application on port 80 bound to all interfaces, the express-sanji
middleware bridging REST resources onto a local MQTT broker, and Python 2.6
model scripts that persist configuration and act on it. The model stores
tunnelModeTable - whose keys include localVpnIp, tunnelRemoteVpnIp and
tunnelRemoteVpnInterface - together with transModeTable, as JSON
configuration written through the authenticated PUT /api/v1/network/ipsec
resource. When the IPsec service applies the tunnel, the model calls its
lifecycle functions, and every one of the four interpolates the stored
fields into an ip command line and hands it to
subprocess.call(cmd, shell=True):

```
add_ip:    cmd = 'ip addr add %s dev eth%s' % (localVpnIp + '/'
                + <computed subnet part>, tunnelRemoteVpnInterface)
del_ip:    'ip addr del %s dev eth%s' with the same stored fields
add_route: cmd = 'ip route add to %s via %s src %s' % (ipRange,
                localVpnIp, localVpnIp)
del_route: cmd = 'ip route del %s' % ipRange
```

The stored value sits at the front of the command line, ahead of every
literal token the product contributes, so a semicolon inside the value ends
the ip operation before any product token can interfere with the injected
statement. One stored localVpnIp arms several commands at once: it is the
operand of add_ip and del_ip and both the via and src operands of
add_route, so whichever lifecycle function a tunnel apply reaches first
carries the payload. The write side applies exactly one filter,
clean_data(), whose entire behaviour is to delete dictionary keys the model
does not recognise: no value is inspected, an address format is never
checked, and the payload rides a key the whitelist expects, so the filter
is not even encountered as an obstacle. An administrator who stores
"10.10.10.1; <command>; #" in that field has authored

```
ip addr add 10.10.10.1; <command>; #/24 dev eth0
```

- the ip segment fails harmlessly as an address operation, the injected
statement executes under the shell, and the hash sign comments away the
template tail. A fifth related construction sits in the same model:
update_config_file() assembles IPsec configuration lines interpolating
transModeTable's transServerIp and transClientIp into the stored
configuration file - the same unvalidated-field pattern, not exercised in
this research record, reported as structure rather than as a detonated
sink.

Authentication and reach. The validateUser middleware is the only
authentication check on the REST surface: it requires a server-side session
for every non-GET method, and login is POST /api/login compared against
bcrypt-hashed entries in the SQLite user table. The PUT that plants the
payload requires the session; past that check there is no second
authorisation layer, the broker leg carries no identity, and the model
implements no permission judgement, so the product's single documented
role, the device administrator, is the whole security boundary. The
listener binds all interfaces on port 80 in the shipped firmware; no WAN
exposure is assumed anywhere in the published rating.

Severity. The published score is 7.2 High,
CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H, from ISS = 0.914816, impact
5.873119, exploitability 1.234708 and base 7.107826 rounded up to 7.2,
Privileges Required High being the product's single administrator role. A
labelled conditional and never the headline: where a deployment still runs
the factory default administrator pair carried by the shipped firmware's
SQLite user table, the prerequisite collapses and the chain reads 9.8
Critical on the PR:N vector (exploitability 3.887043, base 9.760161); a
changed credential removes it, and the default pair is disclosed as a
separate weakness, never folded into the published vector. A PR:L reading
of 8.8 High is published only as the arithmetic of the rejected variant.
The score provenance is disclosed in public: the research record behind
this advisory carried 8.8 for all three same-product findings, that figure
is the arithmetic of a PR:L vector, no artefact shows a lower-privileged
product role, and every published number was recomputed from its own
vector - which lowered the researchers' own figure by 1.6 points. A
Scope-Changed reading computes to 9.1 and is deliberately not published,
because the model process belongs to the same single-purpose appliance
authority, and managing the appliance's interfaces and routes through its
management plane is the product's design rather than an escape.

Verification method, and its boundary. Two evidence classes carry the
finding, kept separate in the published advisory. The firmware's own
application sources establish the configuration write, the key-only
validation, and the four command constructions, read from the shipped
files. The dynamic layer is a sink-level replication on an isolated cloud
Linux sandbox: each of the four constructions, with the same template, the
same field position and the same shell=True hand-off, was executed with an
injected address value and separately with a benign control. All four
produced a marker file containing uid=0(root) under the payload; the
control produced no marker and no side effect of any kind. The boundary is
stated plainly: end-to-end detonation against powered-on hardware,
including the exact tunnel-apply moment at which the stored value is
consumed, is outside this research record, and the on-device model process
identity was neither measured nor claimed - uid=0(root) is the replication
sandbox's identity and nothing broader rests on it.

Impact. Arbitrary command execution as the identity of the Python model
process, begun by one authenticated configuration write and delivered by a
lifecycle step the product performs on its own, with no race and no
protocol manipulation anywhere in the chain. The payload is stored
configuration: it persists across reboots, is read fresh at each tu...