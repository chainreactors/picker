---
title: Re: SEC Consult SA-20260427-0 :: Missing TLS Certificate Validation leading to RCE in DeskTime Time Tracking App
url: https://seclists.org/fulldisclosure/2026/Apr/21
source: Full Disclosure
date: 2026-04-29
fetch_date: 2026-04-30T05:30:37.121545
---

# Re: SEC Consult SA-20260427-0 :: Missing TLS Certificate Validation leading to RCE in DeskTime Time Tracking App

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

[![Previous](/images/left-icon-16x16.png)](20)
[By Date](date.html#21)
[![Next](/images/right-icon-16x16.png)](18)

[![Previous](/images/left-icon-16x16.png)](20)
[By Thread](index.html#21)
[![Next](/images/right-icon-16x16.png)](18)

![](/shared/images/nst-icons.svg#search)

# Re: SEC Consult SA-20260427-0 :: Missing TLS Certificate Validation leading to RCE in DeskTime Time Tracking App

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 28 Apr 2026 06:55:00 +0000

---

```
*Update 2026-04-28:* The vendor contacted us and now provides a patched version v1.3.674 which can be obtained at the
following URL:

https://desktime.com/download

On 4/27/26 12:53, SEC Consult Vulnerability Lab wrote:
```

> ```
> SEC Consult Vulnerability Lab Security Advisory < 20260427-0 >
> =======================================================================
>                title: Missing TLS Certificate Validation leading to RCE
>              product: DeskTime Time Tracking App
>   vulnerable version: 1.3.671
>        fixed version: -
>           CVE number: CVE-2025-10539
>               impact: medium
>             homepage:https://desktime.com
>                found: 2025-05-23
>                   by: Daniel Hirschberger
>                       Thorger Jansen (Office Bochum)
>                       Tobias Niemann (Office Bochum)
>                       Marius Renner (Office Bochum)
>                       SEC Consult Vulnerability Lab
>
>                       An integrated part of SEC Consult, an Atos business
>                       Europe | Asia
>
>                       https://www.sec-consult.com
>
> =======================================================================
>
> Vendor description:
> -------------------
> "A time tracker that won't interrupt your team's workflow. Ever.
> DeskTime is an automatic time tracking tool that will help you increase
> transparency in your team, enable easy hybrid work, and optimize work hours."
>
> Source:https://desktime.com/
>
>
> Business recommendation:
> ------------------------
> The vendor did not provide a patch nor a timeline when a fix will be available.
> In case you are using this product, please approach the vendor and demand a fix.
>
> SEC Consult highly recommends performing a thorough security review of the
> product conducted by security professionals to identify and resolve potential
> further security issues.
>
>
> Vulnerability overview/description:
> -----------------------------------
> 1) Missing TLS Certificate Validation leading to RCE (CVE-2025-10539)
> Due to missing TLS Certificate Validation, attackers, who can inject themselves
> into the network path between the client and the DeskTime update servers, can
> return a malicious executable in response to an update request and achieve
> user-level code execution on the client.
>
>
> Proof of concept:
> -----------------
> 1) Missing TLS Certificate Validation leading to RCE (CVE-2025-10539)
> The DeskTime application periodically checks if there is an update for itself.
> This is done via an HTTPS URL, but the server certificate is not checked
> correctly.
>
> The certificate validation is implemented as follows:
>
> <cert_validation.png>
>
> There are two possibilities to pass the certificate checks:
> 1. There are no errors during the certificate validation
> 2. The request was made by the class `HttpWebRequest` and
>     the used certificate is object of the class `X509Certificate2` and
>     the SSLPolicyError has the value `RemoteCertificateChainErrors`.
> ```
>
> Since 1) is just the regular and correct way to check the server certificate,
>
> ```
> 2) should be further scrutinized.
>
> The .NET documentation for SSLPolicyErrors shows that this enum has the
> following values and meanings:
> https://learn.microsoft.com/en-us/dotnet/api/system.net.security.sslpolicyerrors
>
> None = No SSL policy errors.
> RemoteCertificateNotAvailable = Certificate not available.
> RemoteCertificateNameMismatch = Certificate name mismatch.
> RemoteCertificateChainErrors = ChainStatus has returned a non empty array.
>
> This means that as long as any certificate is provided by the server and that it
> is issued for the expected hostname, it does not matter if there are any errors
> in the validation of the certificate chain.
> This effectively allows man-in-the-middle attacks by using self-signed
> certificates.
>
> To validate this finding on the machine where DeskTime is installed, the
> following steps have to be performed.
>
> Add an entry for `desktime.com` to `C:\Windows\System32\drivers\etc\hosts` and
> point it to localhost:
>
> --------------------------------------------------------------------------------
> 127.0.0.1 desktime.com
> --------------------------------------------------------------------------------
>
> Create a listener in Burp Proxy on port `443`, enable `Force use of TLS` and
> `Invisible Proxy support`.
>
> <burp_request_handling.png>
>
> Since desktime.com now points to 127.0.0.1 because of the modification of the
> hosts file, we have to create a static DNS override in Burp to let the hostname
> `desktime.com` resolve to the real upstream IP.
>
> <burp_dns_override.png>
>
> When DeskTime is started now, the Burp HTTP history shows all client requests.
>
> <burp_requests.png>
>
> If the update function is triggered, a request containing the currently
> installed version, the userID and some other parameters, is sent to the server.
>
> <update_request.png>
>
> The server responds with the version of the installer that it currently hosts,
> as well as a link to that version.
>
> <update_response.png>
>
> If the returned version is greater than the one installed on the client machine,
> it is automatically downloaded and installed in the current user context.
>
> By performing the mentioned man-in-the-middle attack, it is therefore possible
> to achieve Remote Code Execution.
>
> For example, the following Burp Response Rewrite Rule can be used to
> automatically refer the client to another update.
>
> <replace_rule.png>
>
> In this case, the client is redirected to a locally hosted copy of the Windows
> calculator `calc.exe`.
>
> <malicious_update.webm>
>
> Since the updater triggers automatically every hour, no user interaction is
> necessary to exploit this vulnerability.
>
>
> Vulnerable / tested versions:
> -----------------------------
> The following version has been tested which was the latest version available
> at the time of the test:
> * 1.3.671
>
>
> Vendor contact timeline:
> ------------------------
> 2025-06-26: Contacting vendor throughsupport () desktime com;
>              Vendor asks to send advisory information unencrypted;
>              We send the advisory.
> 2025-07-02: Vendor states that this is a duplicate and they are already
>              aware.
> 2025-07-03: We ask for a timeline for the remediation and about
>              assigning a CVE number.
> 2025-07-17: Vendor responds that it will take some time to patch this
>              issue.
>              We respond that we can create a CVE number and ask them
>              to notify us once the patch is released.
> 2025-07-18: Vendor informs us that the next public version will include
>              the fix, but no timeline was provided
> 2025-09-16: Reserved CVE-2025-10539, asking for a status update;
>              Vendor responds that this security issue "can't be used under
>              standard circumst...