---
title: safeurl for Go
url: https://blog.doyensec.com//2022/12/13/safeurl.html
source: Over Security - Cybersecurity news aggregator
date: 2022-12-14
fetch_date: 2025-10-04T01:25:31.533557
---

# safeurl for Go

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

# safeurl for Go

13 Dec 2022 - Posted by Alessandro Cotto and Viktor Chuchurski

**Do you need a Go HTTP library to protect your applications from SSRF attacks?** If so, try [safeurl](https://github.com/doyensec/safeurl).
Itâs a one-line drop-in replacement for Goâs `net/http` client.

## No More SSRF in Go Web Apps

When building a web application, it is not uncommon to issue HTTP requests to internal microservices or even external third-party services. Whenever a URL is provided by the user, it is important to ensure that *Server-Side Request Forgery* (SSRF) vulnerabilities are properly mitigated. As eloquently described in PortSwiggerâs [Web Security Academy](https://portswigger.net/web-security/ssrf) pages, SSRF is a web security vulnerability that allows an attacker to induce the server-side application to make requests to an unintended location.

While libraries mitigating SSRF in numerous programming languages exist, Go didnât have an easy to use solution. Until now!

`safeurl for Go` is a library with built-in SSRF and DNS rebinding protection that can easily replace Goâs default `net/http` client. All the heavy work of parsing, validating and issuing requests is done by the library. The library works out-of-the-box with minimal configuration, while providing developers the customizations and filtering options they might need. Instead of fighting to solve application security problems, developers should be free to focus on delivering quality features to their customers.

This library was inspired by SafeCURL and SafeURL, respectively by [Jack Whitton](https://twitter.com/fin1te) and [Include Security](https://blog.includesecurity.com/2016/08/introducing-safeurl-a-set-of-ssrf-protection-libraries/). Since no SafeURL for Go existed, Doyensec made it available for the community.

## What Does `safeurl` Offer?

With [minimal configuration](#configuration), the library prevents unauthorized requests to internal, private or reserved IP addresses. All HTTP connections are validated against an allowlist and a blocklist. By default, the library blocks all traffic to private or reserved IP addresses, as defined by [RFC1918](https://datatracker.ietf.org/doc/html/rfc1918). This behavior can be updated via the `safeurl`âs client configuration. The library will give precedence to allowed items, be it a hostname, an IP address or a port. In general, allowlisting is the recommended way of building secure systems. In fact, itâs easier (and safer) to explicitly set allowed destinations, as opposed to having to deal with updating a blocklist in todayâs ever-expanding threat landscape.

## Installation

Include the `safeurl` module in your Go program by simply adding `github.com/doyensec/safeurl` to your projectâs `go.mod` file.

```
go get -u github.com/doyensec/safeurl
```

## Usage

The `safeurl.Client`, provided by the library, can be used as a drop-in replacement of Goâs native `net/http.Client`.

The following code snippet shows a simple Go program that uses the `safeurl` library:

```
import (
    "fmt"
    "github.com/doyensec/safeurl"
)

func main() {
    config := safeurl.GetConfigBuilder().
        Build()

    client := safeurl.Client(config)

    resp, err := client.Get("https://example.com")
    if err != nil {
        fmt.Errorf("request return error: %v", err)
    }

    // read response body
}
```

The minimal library configuration looks something like:

```
config := GetConfigBuilder().Build()
```

Using this configuration you get:

* allowed traffic only for ports 80 and 443
* allowed traffic which uses HTTP or HTTPS protocols
* blocked traffic to private IP addresses
* blocked IPv6 traffic to any address
* mitigation for DNS rebinding attacks

## Configuration

The `safeurl.Config` is used to customize the `safeurl.Client`. The configuration can be used to set the following:

```
AllowedPorts            - list of ports the application can connect to
AllowedSchemes          - list of schemas the application can use
AllowedHosts            - list of hosts the application is allowed to communicate with
BlockedIPs              - list of IP addresses the application is not allowed to connect to
AllowedIPs              - list of IP addresses the application is allowed to connect to
AllowedCIDR             - list of CIDR range the application is allowed to connect to
BlockedCIDR             - list of CIDR range the application is not allowed to connect to
IsIPv6Enabled           - specifies whether communication through IPv6 is enabled
AllowSendingCredentials - specifies whether HTTP credentials should be sent
IsDebugLoggingEnabled   - enables debug logs
```

Being a wrapper around Goâs native `net/http.Client`, the library allows you to configure others standard settings as well, such as HTTP redirects, cookie jar settings and request timeouts. Please refer to the [official docs](https://pkg.go.dev/net/http#Client) for more information on the suggested configuration for production environments.

## Configuration examples

To showcase how versatile `safeurl.Client` is, let us show you a few configuration examples.

It is possible to allow only a single **schema**:

```
GetConfigBuilder().
    SetAllowedSchemes("http").
    Build()
```

Or configure one or more allowed **ports**:

```
// This enables only port 8080. All others are blocked (80, 443 are blocked too)
GetConfigBuilder().
    SetAllowedPorts(8080).
    Build()

// This enables only port 8080, 443, 80
GetConfigBuilder().
    SetAllowedPorts(8080, 80, 443).
    Build()

// **Incorrect.** This configuration will allow traffic to the last allowed port (443), and overwrite any that was set before
GetConfigBuilder().
    SetAllowedPorts(8080).
    SetAllowedPorts(80).
    SetAllowedPorts(443).
    Build()
```

This configuration allows traffic to only one host, `example.com` in this case:

```
GetConfigBuilder().
    SetAllowedHosts("example.com").
    Build()
```

Additionally, you can block specific IPs (IPv4 or IPv6):

```
GetConfigBuilder().
    SetBlockedIPs("1.2.3.4").
    Build()
```

Note that with the previous configuration, the `safeurl.Client` will block the IP 1.2.3.4 in addition to all IPs belonging to internal, private or reserved networks.

If you wish to allow traffic to an IP address, which the client blocks by default, you can use the following configuration:

```
GetConfigBuilder().
    SetAllowedIPs("10.10.100.101").
    Build()
```

Itâs also possible to allow or block full CIDR ranges instead of single IPs:

```
GetConfigBuilder().
    EnableIPv6(true).
    SetBlockedIPsCIDR("34.210.62.0/25", "216.239.34.0/25", "2001:4860:4860::8888/32").
    Build()
```

## DNS Rebinding mitigation

DNS rebinding attacks are possible due to a mismatch in the DNS responses between two (or more) consecutive HTTP requests. This vulnerability is a typical TOCTOU problem. At the time-of-check (TOC), the IP points to an allowed destination. However, at the time-of-use (TOU), it will point to a completely different IP address.

DNS rebinding protection in `safeurl` is accomplished by performing the allow/block list validations on the actual IP address which will be used to make the HTTP request. This is achieved by utilizing Goâs `net/dialer` package and the provided `Control` hook. As stated in the official documentation:

```
// If Control is not nil, it is called after creating the network
// connection but before actuall...