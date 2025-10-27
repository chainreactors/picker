---
title: Bypassing airport security via SQL injection
url: https://ian.sh/tsa
source: Over Security - Cybersecurity news aggregator
date: 2024-08-30
fetch_date: 2025-10-06T18:06:13.042045
---

# Bypassing airport security via SQL injection

[ian carroll](/)

![Bypassing airport security via SQL injection](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/727c7878-4188-46dd-a7ff-52f28720199b/lucia-serone--0DVsjv1AHc-unsplash/w=3840,quality=90,fit=scale-down)

# Bypassing airport security via SQL injection

08/29/2024

# Introduction

Like many, [Sam Curry](https://twitter.com/samwcyo) and I spend a lot of time waiting in airport security lines. If you do this enough, you might sometimes see a special lane at airport security called **Known Crewmember** (KCM). KCM is a TSA program that allows pilots and flight attendants to bypass security screening, even when flying on domestic personal trips.

The KCM process is fairly simple: the employee uses the dedicated lane and presents their KCM barcode or provides the TSA agent their employee number and airline. [Various forms of ID](https://www.apfa.org/wp-content/uploads/2019/10/KCM-Program-Changes_OCT19.pdf) need to be presented while the TSA agent’s laptop verifies the employment status with the airline. If successful, the employee can access the sterile area without any screening at all.

A similar system also exists for cockpit access, called the **Cockpit Access Security System** (CASS). Most aircraft have at least one jumpseat inside the cockpit sitting behind the flying pilots. When pilots need to commute or travel, it is not always possible for them to occupy a revenue seat, so a jumpseat can be used instead. CASS allows the gate agent of a flight to verify that the jumpseater is an authorized pilot. The gate agent can then inform the crew of the flight that the jumpseater was authenticated by CASS.

The employment status check is the most critical component of these processes. If the individual doesn’t currently work for an airline, they have not had a background check and should not be permitted to bypass security screening or access the cockpit. This process is also responsible for returning the photo of the crewmember to ensure the right person is being authorized for access. So how does this work, when every airline presumably uses a different system to store their employee information? That is what we were wondering, and where it gets interesting…

## ARINC

[ARINC](https://en.wikipedia.org/wiki/ARINC) (a subsidiary of Collins Aerospace) appears to be contracted by the TSA to operate the Known Crewmember system. ARINC operates a few central components, including an online website for pilots and flight attendants to check their KCM status, and an API to route authorization requests between different airlines. Each airline appears to operate their own authorization system to participate in KCM and CASS, and it interacts with the “hub” of ARINC.

The TSA and airlines can send requests such as `CockpitAccessRequest` and `CrewVerificationRequest` to ARINC, which then routes it to the appropriate airline’s system and receives the response. There are [77 airlines](https://www.knowncrewmember.org/airlines/) currently participating in KCM. While larger airlines have likely built their own system, how do smaller airlines respond to these requests to participate in KCM or CASS?

## FlyCASS.com

In our search for vendors that actually run the authorization systems, we found a site called [FlyCASS](https://www.flycass.com/) which pitches small airlines a web-based interface to CASS. Intrigued, we noticed every airline had its own login page, such as Air Transport International (8C) being available at `/ati`. With only a login page exposed, we thought we had hit a dead end.

Just to be sure though, we tried a single quote in the username as a SQL injection test, and immediately received a MySQL error:

![Uh oh.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7ed29a04-c03b-44f4-934d-107be6abbc1a/Untitled/w=3840,quality=90,fit=scale-down)

Uh oh.

This was a very bad sign, as it seemed the username was directly interpolated into the login SQL query. Sure enough, we had discovered SQL injection and were able to use sqlmap to confirm the issue. Using the username of `' or '1'='1` and password of `') OR MD5('1')=MD5('1`, we were able to login to FlyCASS as an administrator of Air Transport International!

## KCM and CASS Admin

It turns out that FlyCASS also operates both KCM and CASS for its participating airlines. Now that we are an administrator of Air Transport International, we are able to manage the list of pilots and flight attendants associated with them. Surprisingly, there is **no further check or authentication** to add a new employee to the airline. As the administrator of the airline, we were able to add anyone as an authorized user for KCM and CASS.

![image](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/c87f2023-3162-45ba-b76e-5c976807e690/Untitled/w=3840,quality=90,fit=scale-down)

To test that it was possible to add new employees, we created an employee named `Test TestOnly` with a test photo of our choice and authorized it for KCM and CASS access. We then used the Query features to check if our new employee was authorized. Unfortunately, **our test user was now approved to use both KCM and CASS**:

![image](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/c8f35f9c-f7f9-433d-8479-4c07b1668218/Untitled/w=3840,quality=90,fit=scale-down)

At this point, we realized we had discovered a very serious problem. Anyone with basic knowledge of SQL injection could login to this site and add anyone they wanted to KCM and CASS, allowing themselves to both skip security screening and then access the cockpits of commercial airliners.

We ended up finding several more serious issues but began the disclosure process immediately after finding the first issue.

## Disclosure

We had difficulty identifying the right disclosure contact for this issue. We did not want to contact FlyCASS first as it appeared to be operated only by one person and we did not want to alarm them. On April 23rd, we were able to disclose the issue to the Department of Homeland Security, who acknowledged the issue and confirmed that they “are taking this very seriously”. FlyCASS was subsequently disabled in KCM/CASS and later appears to have remediated the issues.

After the issue was fixed, we attempted to coordinate the safe disclosure of this issue. Unfortunately, instead of working with us, the Department of Homeland Security stopped responding to us, and the TSA press office issued dangerously incorrect statements about the vulnerability, denying what we had discovered.

The TSA press office said in a statement that this vulnerability could not be used to access a KCM checkpoint because the TSA initiates a vetting process before issuing a KCM barcode to a new member. However, a KCM barcode is not required to use KCM checkpoints, as the TSO can enter an airline employee ID manually. After we informed the TSA of this, [they deleted the section of their website that mentions manually entering an employee ID](https://web.archive.org/web/20221001213220/https%3A//mykcmsupport.com/faq/), and did not respond to our correction. We have confirmed that the interface used by TSOs still allows manual input of employee IDs.

Several other attacks were also likely possible. Since our vulnerability allowed us to edit an existing KCM member, we could have changed the photo and name of an existing enrolled user, which would likely bypass any vetting process that may exist for new members. If you are able to obtain an unenrolled KCM barcode, you can also enroll it to an employee ID yourself on the KCM website.

## Timeline

* 04/23/2024: Initial disclosure to ARINC and FAA
* 04/24/2024: Subsequent disclosure to DHS via CISA
* 04/25/2024: DHS CISO confirms they are working on a resolution
* 05/07/2024: DHS CISO confirms FlyCASS was disconnected from KCM/CASS
* 05/17/2024: Follow-up to DHS CISO about TSA statements (no reply)
* 06/04/2024: Follow-up to DHS CISO about TSA statements (no reply)

## Collaborators

* Ian...