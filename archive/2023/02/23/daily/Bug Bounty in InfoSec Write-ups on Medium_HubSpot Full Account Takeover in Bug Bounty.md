---
title: HubSpot Full Account Takeover in Bug Bounty
url: https://infosecwriteups.com/hubspot-full-account-takeover-in-bug-bounty-4e2047914ab5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-23
fetch_date: 2025-10-04T07:50:37.507951
---

# HubSpot Full Account Takeover in Bug Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4e2047914ab5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhubspot-full-account-takeover-in-bug-bounty-4e2047914ab5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhubspot-full-account-takeover-in-bug-bounty-4e2047914ab5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4e2047914ab5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4e2047914ab5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# HubSpot Full Account Takeover in Bug Bounty

[![Omar Hashem](https://miro.medium.com/v2/resize:fill:64:64/1*ayu-cF0Elq8Emv1cdCLf_A.jpeg)](https://omar0x01.medium.com/?source=post_page---byline--4e2047914ab5---------------------------------------)

[Omar Hashem](https://omar0x01.medium.com/?source=post_page---byline--4e2047914ab5---------------------------------------)

11 min read

·

Feb 11, 2023

--

40

Listen

Share

Hi everybody, our story today will be about how I was able to get a Full account takeover on HubSpot Public Bug Bounty Program at Bugcrowd platform

Press enter or click to view image in full size

![]()

### Let’s start our story

Our subdomain was [https://growanz.hubspot.com](https://growanz.hubspot.com/)

While I was testing authentication functions I came across Forgot registration number (Forgot Password)

Press enter or click to view image in full size

![]()

The function asks us to enter an email to send a magic link to log in without a registration number (password)

Press enter or click to view image in full size

![]()

## SQL Injection

As there is an email parameter absolutely there is some type of database in the backend to handle these emails which makes the email parameter the best place to test for SQLI

Press enter or click to view image in full size

![]()

After testing it found nothing but it was okay

## Host Header Poisoning:

It’s common for developers to use HOST HEADER Value in reset password URI

```
$ForgotPassURI = "https://{$_SERVER['HTTP_HOST']}/dream-auth/forgot?
registration=$token&email=$email";
```

So let’s try to change the host header to a domain under our control

Press enter or click to view image in full size

![]()

Did not work

### Load Balancer Host Header Override:

Okay sometimes there is a load balancer or a reverse proxy server between the users and the server so if developers used the HOST Header they will get the host of load balancer so the developer moves to use the X-Forwarded-Host header because the load balancer saves the original HOST header value in X-Forwarded-Host header

Anyway, this header should not be modified by the users but some weak load balancers or reverse proxies rewrite this header from user input which makes this header suitable for our test

Press enter or click to view image in full size

![]()

The email was sent successfully but after checking the mail I found that the forgot registration URI still contains growanz.hubspot.com

### Referer Header:

Some developers expect that to access the forgot password endpoint you need to come from the main subdomain which makes them use the referer header value in their reset password

```
$ForgotPassURI = "https://{$_SERVER['HTTP_REFERER']}/dream-auth-forgot?
registration=$token&email=$email";
```

Press enter or click to view image in full size

![]()

Did not work

### ORIGIN Header:

So I moved to the origin header

```
$ForgotPassURI = "https://{$_SERVER['HTTP_ORIGIN']}/dream-auth-forgot?
registration=$token&email=$email";
```

trying to add my burp collaborator domain

Press enter or click to view image in full size

![]()

Did not work too

## Bypass Regular Expression:

So maybe developers do some regex to validate the user input in the previous techniques, if the user input matches the regex they will send our domain, while if it does not match the regex they will send the default subdomain from their configuration file, So let’s try to bypass it

Bypass matching on host contain growanz.hubspot.com

> growanz.hubspot.com.mydomain.com

Weak regex by using dot on regex without bypassing it e.g ”^growanz.hubspot.com$|^example.virtual.host$”

> growanzXhubspot.com

Bypass matching on the end at growanz.hubspot.com

> mydomain.com/growanz.hubspot.com

Bypass white list validation

> mydomain.com%23@growanz.hubspot.com
>
> mydomain.com%25%32%33@growanz.hubspot.com

But the previous bypasses on the previous headers none of them worked

So let’s move to test the email parameter

## HTTP-Parameter-Pollution (HPP) :

Okay we have different types of applications architecture used in application development like Monolithic, EDA, SOA, or Microservices

So as Microservices became more trendy in development these days as it has a lot of advantages that did not exist in some old architectures like Monolithic, which will help to expand our surface of attacks so what if our target relies on microservices internally that using RestFull API to communicate with each other!

So let’s figure that out

Press enter or click to view image in full size

![]()

I made this graph as a simple example for our scenario

So maybe our reset password request passed to a microservice that relay on JSP that handles requests dealing with Database (e.g. reset password email) if it exists it responds to the business routing logic which will route the original request again to the PHP microservice that deals with the SMTP service to send the reset password mail

So if microservices are used in our target we need to test other attacks like HTTP Parameter Pollution

Press enter or click to view image in full size

![]()

According to that table if we entered two parameters into PHP it will use the second parameter while other technology like JSP will use the first parameter

```
// HTTP parameter pollution (HPP)
{"email":"victim@mail.com","email":"attacker@mail.com"}
```

So if our request is passed to JSP that deals with the database it will create the reset password URI to the first email but when the request is routed again to the PHP it will send the reset pass mail to the second email

Press enter or click to view image in full size

![]()

But after checking the email I found it did not work

## Attack chain (SMTP injection && HTTP Parameter Pollution)

> Note: I am using PHP as an example to illustrate. I don’t mean that these attacks are specific to PHP because these attacks are suitable for other technologies that rely on SMTP parsers and services.

Imagi...