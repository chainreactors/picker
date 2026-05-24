---
title: SSRF in APIs: How a Single URL Parameter Can Expose Internal Systems
url: https://infosecwriteups.com/ssrf-in-apis-how-a-single-url-parameter-can-expose-internal-systems-63128bff63a4?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-23
fetch_date: 2026-05-24T06:00:46.728383
---

# SSRF in APIs: How a Single URL Parameter Can Expose Internal Systems

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-in-apis-how-a-single-url-parameter-can-expose-internal-systems-63128bff63a4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-in-apis-how-a-single-url-parameter-can-expose-internal-systems-63128bff63a4&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-63128bff63a4---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-63128bff63a4---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# SSRF in APIs: How a Single URL Parameter Can Expose Internal Systems

[![Sana Jalil](https://miro.medium.com/v2/resize:fill:64:64/1*LqoTX3tRaXI9G2Nxx8G7oQ.jpeg)](https://medium.com/%40sanajalil9090?source=post_page---byline--63128bff63a4---------------------------------------)

[Sana Jalil](https://medium.com/%40sanajalil9090?source=post_page---byline--63128bff63a4---------------------------------------)

5 min read

·

1 day ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D63128bff63a4&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-in-apis-how-a-single-url-parameter-can-expose-internal-systems-63128bff63a4&source=---header_actions--63128bff63a4---------------------post_audio_button------------------)

Share

*A single misconfigured URL parameter can allow an attacker to abuse server-side requests and potentially access internal services, cloud metadata endpoints, or hidden resources that were never meant to be exposed.*

Press enter or click to view image in full size

![]()

### **What is SSRF? The Silent Attack Hiding in Plain Sight**

SSRF stands for **Server-Side Request Forgery**.

Imagine asking a waiter to bring food from the kitchen, but instead you trick the waiter into entering the manager’s office and retrieving confidential documents. The waiter is trusted, so security does not stop him. SSRF works in a similar way.

In web applications, servers frequently make requests on behalf of users, such as:

* Fetching URLs
* Generating previews
* Calling external APIs
* Retrieving remote resources

SSRF occurs when an attacker manipulates these requests and causes the server to communicate with destinations it was never intended to access.

Instead of fetching a harmless webpage, the server may begin interacting with:

* Internal services
* Cloud metadata endpoints
* Private APIs
* Administrative interfaces

The dangerous part is that the request originates from the server itself, which is generally considered a trusted source. Firewalls and network controls may treat this traffic as legitimate.

No credentials may be required. In some cases, all it takes is a URL parameter that lacks proper validation.

### What Does an SSRF Attack Actually Look Like?

To demonstrate this vulnerability, I used **crAPI**, a deliberately vulnerable API application designed for security practice. It provides a safe and legal environment for learning and testing web application security concepts.

I navigated to the **Contact Mechanic** section, submitted the form, and intercepted the request using **Burp Suite**.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

The application sends requests to an endpoint responsible for processing service reports. The key parameter here is **mechanic\_api**, which uses user-supplied input to make an outbound request on behalf of the user. Since this parameter controls the request destination, it becomes a potential SSRF injection point.

Press enter or click to view image in full size

![]()

### Step 1: Confirming the SSRF

To determine whether arbitrary URLs were accepted, I replaced the mechanic\_api value with an external URL.

The server returned a successful response containing external page content.

This confirms several important observations:

* The application performs outbound HTTP requests using user-controlled input
* URL validation or allowlisting is absent
* The server can access external destinations and potentially internal resources

This confirms SSRF behavior.

The server is processing user-controlled requests without proper validation, allowing attackers to abuse it to access unintended destinations.

Press enter or click to view image in full size

![]()

## Step 2: Accessing Internal Admin Functionality

Since requests originate from the server itself, internal resources that are inaccessible externally may sometimes become reachable through SSRF. I attempted to access internal administrative paths. The response returned: HTTP 404:Not Found This suggests the resource does not exist at that specific location. I then tested access to the application’s own endpoint through localhost.

Press enter or click to view image in full size

![]()

I then tested access to the application’s own endpoint through localhost.

This time the response returned:

**HTTP 405 :Method Not Allowed**

## Get Sana Jalil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

This is interesting because it suggests the endpoint exists and is reachable, but the request method used was incorrect.

This indicates that additional testing with different HTTP methods may reveal more functionality.

Press enter or click to view image in full size

![]()

## Potential Post-Exploitation Scenarios

Once SSRF is confirmed, attackers may attempt additional actions depending on the target environment:

* Internal service discovery through port scanning
* Accessing internal-only APIs
* Retrieving cloud metadata information
* Testing filter bypass techniques
* Identifying blind SSRF behavior using out-of-band interactions

The success of these activities depends heavily on application design and network architecture.

## Why APIs Frequently Become SSRF Targets

Modern APIs frequently process user-controlled URLs and remote resources.

Common examples include:

* Webhook functionality accepting external endpoints
* URL preview generation
* File import features
* Image retrieval functionality
* Microservice communication between internal services

Developers may unintentionally trust internal traffic, creating opportunities for SSRF abuse.

## Potential Impact of SSRF

Depending on the environment, SSRF can result in:

* Internal network mapping and service discovery
* Access to internal APIs that bypass external access restrictions
* Retrieval of cloud ...