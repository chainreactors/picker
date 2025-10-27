---
title: Leaked Secrets and Unlimited Miles: Hacking the Largest Rewards Vendor
url: https://samcurry.net/points-com/
source: Over Security - Cybersecurity news aggregator
date: 2023-08-04
fetch_date: 2025-10-04T12:03:21.367052
---

# Leaked Secrets and Unlimited Miles: Hacking the Largest Rewards Vendor

[‹ Back](/)

* Introduction
* Collaborators
* High Level Overview
* Investigating Points.com
* How does it all work?
* Exploring the United Airlines Points Management Website
* (1) Improper Authorization on Points Recipient Endpoint Allows Attacker to Authenticate as Any User Using Only Surname and Rewards Number
* Escalating the issue to affect other rewards programs
* (2) Directory Traversal on Privileged API leads to Access of 22 Million Customer Order Records for Points.com Reward Programs
* Points.com Catches Us
* (3) Leaked Credentials for Virgin Rewards Program allows Attacker to Sign API Requests on Behalf of Virgin, Add/Remove Rewards Points, Access Customer Accounts
* (4) Authorization Bypass on "widgets.unitedmileageplus.com" allows Attacker to Authenticate as Any User via Last Name and Rewards Number, Potential Access to United MileagePlus Administration Panel
* Looking for something more critical…
* Switching Back to Hunting on the Points.com Global Administration Console
* (5) Full Access to Core Points.com Administration Console and Loyalty Admin Website via Weak Flask Session Secret
* Closing
* Disclosure Timeline
* Special thanks to...

[‹ Back](/)

# Leaked Secrets and Unlimited Miles: Hacking the Largest Airline and Hotel Rewards Platform

Thu Aug 03 2023

![Leaked Secrets and Unlimited Miles: Hacking the Largest Airline and Hotel Rewards Platform](/images/points-com/points-man.png)

## Introduction

Between March 2023 and May 2023, we identified multiple security vulnerabilities within points.com, the backend provider for a significant portion of airline and hotel rewards programs. These vulnerabilities would have enabled an attacker to access sensitive customer account information, including names, billing addresses, redacted credit card details, emails, phone numbers, and transaction records. Moreover, the attacker could exploit these vulnerabilities to perform actions such as transferring points from customer accounts and gaining unauthorized access to a global administrator website. This unauthorized access would grant the attacker full permissions to issue reward points, manage rewards programs, oversee customer accounts, and execute various administrative functions.

Upon reporting these vulnerabilities, the points.com team responded very quickly, acknowledging each report within an hour. They promptly took affected websites offline to conduct thorough investigations and subsequently patched all identified issues. All vulnerabilities reported in this blog post have since been remediated.

![](/_next/image?url=%2Fimages%2Fpoints-com%2Fnick.png&w=3840&q=75)

## Collaborators

* Ian Carroll (<https://twitter.com/iangcarroll>)
* Shubham Shah (<https://twitter.com/infosec_au>)
* Sam Curry (<https://twitter.com/samwcyo>)

## High Level Overview

The following is a high level overview of the reported vulnerabilities. For the technical write-ups, please scroll down to the "Investigating Points.com" section.

**Directory Traversal leads to Query Access to Points.com Customer Order Records (March 7, 2023)**

Our first report was an unauthenticated HTTP path traversal allowing access to an internal API which would've allowed an attacker to query entries from a set of 22 million order records. The data within the records included partial credit card numbers, home addresses, email addresses, phone numbers, reward points numbers, customer authorization tokens, and miscellaneous transaction details. This information could be queried through an API call that returned one-hundred results per HTTP request. By appending optional sorting parameters, an attacker could enumerate the data or query for specific information (e.g. searching a customer's name or email address).

**Ability to Transfer Rewards Points and Leak Customer Information using only Rewards Number and Surname (March 7, 2023)**

The second vulnerability we reported was an authorization bypass that would allow an attacker to transfer airline rewards points from other users by knowing only their surname and rewards points number (both of these fields were disclosed in our first vulnerability report) via an improperly configured API. An attacker could generate full account authorization tokens which would allow them to manage customer accounts, view order history, view billing information, view contact information, and transfer points from customers.

For both of the initial reports, the team responded in under 10 minutes and immediately took the websites offline. The issues were quickly fixed and the websites were back online shortly thereafter.

**Leaked Tenant Credentials for Virgin Rewards Program allows Attacker to Sign API Requests on Behalf of Virgin (Add/Remove Rewards Points, Access Customer Accounts, Modify Rewards Program Settings, etc.)**

On May 2nd, 2023, we discovered an endpoint on a points.com-hosted Virgin rewards website that leaked the "macID" and "macKey" used by Virgin to authenticate to the core points.com API on behalf of the airline. The credentials could be used to fully authenticate as the airline to the "lcp.points.com" API by signing HTTP requests using the disclosed secret, allowing an attacker to call any of the API calls intended for the airline like modifying customer accounts, adding/removing points, or modifying settings related to the Virgin rewards program.

The points.com team responded and fixed the issue within only an hour.

**New Method for Transferring Airline Miles and Accessing Customer Account and Order Information from United MileagePlus members (April 29th, 2023)**

On April 29th, 2023, we identified an additional fourth vulnerability affecting specifically United Airlines where an attacker could generate an authorization token for any user knowing only their rewards number and surname. Through this issue, an attacker could both transfer miles to themselves and authenticate as the member on multiple apps related to MileagePlus, potentially including the MileagePlus administrator panel. This issue disclosed the member's name, billing address, redacted credit card information, email, phone number, and past transactions on the account.

After reporting the issue, the team responded in under 10 minutes and immediately took the website offline. The issue was quickly fixed and the website was back online shortly thereafter.

**Full Access to Global Points.com Administration Console and Loyalty Wallet Administration Panel via Weak Flask Session Secret (May 2nd, 2023)**

On May 2nd, 2023, we identified that the Flask session secret for the points.com global administration website used to manage all airline tenant and customer accounts was the word "secret". After discovering this vulnerability, we were able to resign our session cookies with full super administrator permissions.

After resigning the cookie with roles that give full administrator permissions, we observed that we could access all core administration functionality on the website, including user lookup, manual bonuses, rewards points conversion modifications (e.g. setting the exchange rate between two programs where 1 point would give you 1 million points), and many more points.com administrative endpoints (e.g. managing promotions, branding, resetting loyalty program credentials, etc.). An attacker could abuse this access to revoke existing reward program credentials and temporarily take down airline rewards functionality.

For our last vulnerability report, the team responded within an hour (even though we'd reported it at 3:30 AM CST) by taking the website offline and changing the secret.

## Investigating Points.com

With the cost of air travel becoming so expensive recently, I've gotten more and more into the "credit card churning" community where you can try to gamify credit cards and purchases to save rewards points which can be converted into things like flights and hotels. From a hacker's perspective, it's super interesting seeing a system that stores a numeric value th...