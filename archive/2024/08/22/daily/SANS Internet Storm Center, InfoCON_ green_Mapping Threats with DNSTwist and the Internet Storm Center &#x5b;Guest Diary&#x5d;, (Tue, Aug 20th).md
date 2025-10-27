---
title: Mapping Threats with DNSTwist and the Internet Storm Center &#x5b;Guest Diary&#x5d;, (Tue, Aug 20th)
url: https://isc.sans.edu/diary/rss/31188
source: SANS Internet Storm Center, InfoCON: green
date: 2024-08-22
fetch_date: 2025-10-06T18:05:51.330270
---

# Mapping Threats with DNSTwist and the Internet Storm Center &#x5b;Guest Diary&#x5d;, (Tue, Aug 20th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31186)
* [next](/diary/31194)

# [Mapping Threats with DNSTwist and the Internet Storm Center [Guest Diary]](/forums/diary/Mapping%2BThreats%2Bwith%2BDNSTwist%2Band%2Bthe%2BInternet%2BStorm%2BCenter%2BGuest%2BDiary/31188/)

**Published**: 2024-08-20. **Last Updated**: 2024-08-21 00:17:41 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Mapping%2BThreats%2Bwith%2BDNSTwist%2Band%2Bthe%2BInternet%2BStorm%2BCenter%2BGuest%2BDiary/31188/#comments)

[This is a Guest Diary by Michael Tigges, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

On July 16, 2024, I received notification of a suspicious tunnel being opened via SSH in relation to the medical image viewing software "MicroDICOM". MicroDICOM is a medical imagery software and processing engine commonly used to examine x-ray’s, MRIs, and ultrasounds. This was atypical for this application-- while it contained the capabilities to perform network sharing, this application reused private keys and generally engaged in unsafe practices for a method that might connect to an organizational resource. Furthermore, all files were connecting back to the same IP address, 209.127.37.48. Upon investigation, we were able to determine that this application was not, in fact, the application it purported to be, but instead part of large phishing campaign that appeared to prey on a recent Common Vulnerability & Exploit (CVE) notification from the Cybersecurity & Infrastructure Security Agency (CISA).

On July 11, 2024, CISA released ICS Medical Advisory 'ICSMA-24-163-01'. This advisory raised two CVEs to public attention:

* CVE-2024-33606 (CVSS 8.8) for the improper authorization for custom URL scheme.
* CVE-2024-28877 (CVSS 8.8) for a stack buffer overflow.

The combination of these CVE's necessitates an immediate update to this application, and in fact, proper security due diligence would be to mitigate this as soon as possible with updating/patching. As such, a large portion of the MicroDICOM users were likely looking to update their software.

**Behavioral Analysis**

Armed with this context, we can focus on our binary analysis. I retrieved the payload from the host system that fired the alert. Our application, `MicroDicom-2024.2+2.exe` was much larger than the original application at 179 MB, versus the typical 10MB to 12.5MB that the original application is. Our first hint aside from the obvious non-matching file hash and size that we may be dealing with adversarial behavior came through the certificate utilized by this application, "Helping businesses Limited". (**Bonus**: *This is a commonly abused signature! More on that at the end.*)

Further examination of the application in a sandbox revealed the presence of several artifacts of interest inconsistent with the general behavior of this service. The first, `UpdaterSvc.exe` is a service registered on the target system upon installation of the suspicious MicroDICOM application. This service is quite simple, and process hierarchy reveals that this is responsible for the invocation of our second artifact of interest, 7655.bat. This, in turn, is responsible for the construction and execution of our SSH tunnel. Armed with this knowledge, we can begin enumeration in earnest to find some more information regarding potential attack vectors for our MicroDICOM application.

**Is this a campaign?**

My first stop in determining the acquisition of this malicious application was to consult business IT administrators to inquire about the acquisition source. System owners were able to reliably point directly back to the legitimate MicroDICOM website, https://microdicom.com. I'm going to abbreviate the steps I took to conclusively rule out the source of this website as the host for our malicious payload. My initial assumption was that this website was compromised, and so I used several geofencing bypass techniques including residential proxies, SOCKS5 proxies, Digital Ocean and AWS infrastructure, and a hand-rolled User Agent and Referrer engine. None of these efforts resulted in the successful retrieval of the malicious payload.

However, upon closer examination of the systems involved, I had missed a key artifact. When accessing these hosts via remote desktop software, the administrator downloaded the MicroDICOM application via a standard browser. And thus, armed with the user's browser history, we at last can recover the (first) of our malicious domains, "mLcrodicom[.]info". Upon visiting this website, we're greeted with a cloned version of the original site.

![](https://isc.sans.edu/diaryimages/images/Michael_Tigges_Picture1.png)Figure 1. Malicious MicroDICOM website clone using a homoglyph attack.

**Author’s Note**: This site now serves a phishing warning via CloudFlare interstitial. This was not in place during the initial examination.

Downloading the MicroDICOM application from this website does, in fact, contain the 179 MB executable that we were looking for, and generates a matching SHA2-256 hash with our suspicious MicroDICOM application.

However, the organizations targeted via this suspected spear-phishing campaign were not within the same organization, indicative of a wider attack. We can hypothesize that there may be additional malicious domains, and we have two ways to analyze this hypothesis.

Our first is a web application called DNSTwist [[1](https://dnstwist.it/)]. DNSTwist uses several permutation generation techniques and queries DNS records for common attacks such as homoglyph attacks, or exchanging letters for those that look structurally similar. (E.g., Lower case L, and I’s, etc.) Further, it generates omissions and subdomains that may exist that are structurally similar to the site. Using this tool, our first stop might be to check “microdicom.com” and look for permutations of this site. DNSTwist also enumerates top level domain swaps such as “.info” to look for similar sites present at that location as well.

At the time of this writeup, several of these sites are not being indexed by DNSTwist, but this site itself revealed the presence of “microdLcom[.]info” as a domain we may wish to examine as well. And local examination of this site also yields our malicious backdoored payload.

 DNSTwist can be a bit hit-and-miss on the results it retrieves, as it is generating permutations algorithmically. However, recall back to our hypothesis: We believe that these individuals are exploiting the recent CISA ICSMA notification. This means that we can enumerate newly registered domains (NRD) to obtain this information.

There are many NRD API’s present on the internet, but few are free. However, the SANS Internet Storm Center maintains a list of newly registered domains which is historically indexable for thirty days in the ISC/DShield API [2]. We can generate a Python script to perform enumeration of newly registered domains that might match our target domain.
**Author’s Note**: *This is an excerpt of a larger Python application I have generated to perform this scanning for threat hunting. There will be some anomalies that, while peculiar, lend themselves more to user extension and have thus been included for end-user modification.*

import requests
import datetime
import time

def destructure\_response(response: list[dict[str,str]]):
    results = ""
    for entries in response:
        domain\_name, tld = entries['domainname'].split('.')[0], entries['domainname'].split('.')[1]
        results += (f"{domain\_name}.{tld},{entries['ip']},{entries['firstseen']}\n")
    return results

def query\_domain(domain: str):
    headers = {'User-Agent': 'Python Requests, GrepDomain 0.1, Contact: <your-email>'}
    results = "domai...