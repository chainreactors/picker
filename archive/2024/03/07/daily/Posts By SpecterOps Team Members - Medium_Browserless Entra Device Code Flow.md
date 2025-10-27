---
title: Browserless Entra Device Code Flow
url: https://posts.specterops.io/browserless-entra-device-code-flow-0802f3bbb91a?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-03-07
fetch_date: 2025-10-06T17:11:27.694259
---

# Browserless Entra Device Code Flow

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0802f3bbb91a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fbrowserless-entra-device-code-flow-0802f3bbb91a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fbrowserless-entra-device-code-flow-0802f3bbb91a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-0802f3bbb91a---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-0802f3bbb91a---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Browserless Entra Device Code Flow

[![Andy Robbins](https://miro.medium.com/v2/resize:fill:64:64/2*G-LlqSNRGI8wIrjrYRzWdA.png)](https://medium.com/%40_wald0?source=post_page---byline--0802f3bbb91a---------------------------------------)

[Andy Robbins](https://medium.com/%40_wald0?source=post_page---byline--0802f3bbb91a---------------------------------------)

6 min read

·

Mar 6, 2024

--

Listen

Share

Press enter or click to view image in full size

![]()

Zugspitze, Bavaria, Germany. Photo by [Andrew Chiles](https://twitter.com/AndrewChiles)

Did you know that it is possible to perform every step in Entra’s OAuth 2.0 Device Code flow — including the user authentication steps — without a browser?

**Why that matters:**

* Automating authentication flows enables and accelerates comprehensive and ongoing offensive research
* Headless authentication frees red teamers and pentesters from requiring browser or cookie access
* Demonstrating and explaining the automated flow enables future research and tooling by other parties, including automation of other flows

**Yes, but:**

* These systems change. While this automation works today, slight changes in the future may require updates to the code in this blog post.
* This code does not support any sort of MFA challenge a user may be subjected to during authentication.

## Automating the Flow

Automating device code flow requires five requests:

**Request One: *POST* to** [***https://login.microsoftonline.com/common/oauth2/devicecode?api-version=1.0***](https://login.microsoftonline.com/common/oauth2/devicecode?api-version=1.0)

In this request, the application initiates the flow and receives a “user code” back from the devicecode API. This “user code” is what a human being would enter into the browser later:

```
# Device Code OAuth flow begins:
$body = @{
 "client_id" = "1b730954–1685–4b74–9bfd-dac224a7b894"
 "resource" = "https://graph.microsoft.com"
}
$UserAgent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"
$Headers=@{}
$Headers["User-Agent"] = $UserAgent
$authResponse = Invoke-RestMethod `
 -UseBasicParsing `
 -Method Post `
 -Uri "https://login.microsoftonline.com/common/oauth2/devicecode?api-version=1.0" `
 -Headers $Headers `
 -Body $body
$OTC = $authResponse.user_code
```

**Request Two: *GET* to** [***https://login.microsoftonline.com/common/oauth2/deviceauth***](https://login.microsoftonline.com/common/oauth2/deviceauth)

The next request is performed “as the user” and is a simple request to the initial deviceauth page:

```
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
$SecondRequest = $null
$SecondRequest = Invoke-WebRequest `
 -UseBasicParsing `
 -Uri "https://login.microsoftonline.com/common/oauth2/deviceauth" `
 -WebSession $session `
```

The response to this request includes our first collection of cookies and unique identifiers that we must keep track of during the flow:

**x-ms-request-id** — The value of this response header is required in later requests as the value for “hpgrequestid”

**fpc** — This cookie is required in later requests

**esctx** — This cookie is required in later requests

**hpgid** — A four-digit code that is required in later requests and must be parsed out of the response body HTML

**canary** — A token required in later requests, must be parsed from the response body HTML

We can assign all of these cookies, tokens, and other identifiers to their relevant variables with some basic parsing of the response headers and body in PowerShell:

```
$hpgrequestid = $SecondRequest.Headers.'x-ms-request-id'
$CookieFPC = (($SecondRequest.Headers.'Set-Cookie' | select -first 1) -Split '; ') -Split '=' | Select -First 2 | Select -Last 1
$CookieESCTX = (($SecondRequest.Headers.'Set-Cookie' | select -first 2 | Select -Last 1) -Split '; ') -Split '=' | Select -First 2 | Select -Last 1
$html = $SecondRequest.Content
$pattern = ',"hpgid":(.*?),"pgid"'
$match = $html | Select-String -Pattern $pattern
if ($match) {
 $HPGID = $match.Matches.Groups[1].Value
 Write-Output "HPGID: $HPGID"
} else {
 Write-Output "HPGID not found in the HTML."
}
$pattern = '","canary":"(.*?)","sCanaryTokenName"'
$match = $html | Select-String -Pattern $pattern
if ($match) {
 $desiredString = $match.Matches.Groups[1].Value
 $Canary = [System.Web.HttpUtility]::UrlEncode($desiredString)
 Write-Output "Canary: $Canary"
} else {
 Write-Output "Canary not found in the HTML."
}
```

This code block shows what each value looks like:

```
$hpgrequestid: e2a89eff-5dd0–4262-b27b-4ee2468a5900
$CookieFPC AuxOg1aj0H5EpEVcclZOs4Q
$CookieESCTX PAQABAAEAAAD - DLA3VO7QrddgJg7WevrzJCyhs37r8aEEog6PXOivCF953PRt68FvlHkjFnSplN2mNHQwqEBcTTmf5EPXTIRQCQXFrA27_cEk2l3YG0F1JreF8T9WwL5PJldV5XZjdy2RF-A-EtDsFx_MHGWSV-FSw1Prci4lcfiDl7vsxQMqXKGgaUSdNPbA9iJPFfIh8cgAA
$HPGID 1119
$Canary t%2frFkhW25KShBl3S2O7pyXaB6GA3P3orfpFUxom3RH4%3d7%3a1%3aCANARY%3acDaoWAl7lE%2f5UyKpxyvQpCptwytSp3fwGEJMnTyNAXQ%3d
```

**Request Three: *POST* to** [***https://login.microsoftonline.com/common/oauth2/deviceauth***](https://login.microsoftonline.com/common/oauth2/deviceauth)

In this request, we include the ESCTX cookie, One-Time Code (OTC), Canary, and hpgrequestid values when *POST*ing to the deviceauth endpoint:

```
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
$session.Cookies.Add((New-Object System.Net.Cookie("esctx", $CookieESCTX, "/", ".login.microsoftonline.com")))
$ThirdRequest = $null
$ThirdRequest = Invoke-WebRequest `
 -UseBasicParsing `
 -Uri "https://login.microsoftonline.com/common/oauth2/deviceauth" `
 -Method "POST" `
 -WebSession $session `
 -ContentType "application/x-www-form-urlencoded" `
 -Body "otc=$($OTC)&canary=$($Canary)&flowToken=&hpgrequestid=$($hpgrequestid)"
```

The response will include NEW values for hpgrequestid and ESCT...