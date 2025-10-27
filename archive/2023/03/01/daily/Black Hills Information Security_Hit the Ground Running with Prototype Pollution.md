---
title: Hit the Ground Running with Prototype Pollution
url: https://www.blackhillsinfosec.com/hit-the-ground-running-with-prototype-pollution/
source: Black Hills Information Security
date: 2023-03-01
fetch_date: 2025-10-04T08:20:25.267548
---

# Hit the Ground Running with Prototype Pollution

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

28
Feb
2023

[Finding](https://www.blackhillsinfosec.com/category/finding/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Isaac Burton](https://www.blackhillsinfosec.com/category/author/isaac-burton/), [Web App](https://www.blackhillsinfosec.com/category/red-team/web-app/)
[Prototype Pollution](https://www.blackhillsinfosec.com/tag/prototype-pollution/), [Web API](https://www.blackhillsinfosec.com/tag/web-api/)

# [Hit the Ground Running with Prototype Pollution](https://www.blackhillsinfosec.com/hit-the-ground-running-with-prototype-pollution/)

[Isaac Burton](https://www.blackhillsinfosec.com/team/isaac-burton/) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/BLOG_chalkboard_00618-1024x576.png)

For as long as we have known about prototype pollution vulnerabilities, there has been confusion on what they are and how they can be exploited. We’re going to discuss some of the easiest ways to identify a prototype pollution vulnerability in the wild, which can lead to all kinds of exploitation!

Prototype pollution can exist server side or client side. Server-side prototype pollution can be used to modify application control flow, which can be fun and rewarding to exploit. When a prototype pollution vulnerability is present client-side, it can be leveraged to perform cross-site scripting (XSS). In both cases, exploiting prototype pollution is heavily dependent on context. Fortunately, identifying the vulnerability is often not so difficult.

We’re going to jump into a couple examples just to show how easy identifying this vulnerability can be. Then, we will dig into why these vulnerabilities occur and explore other methods of identification and exploitation.

## Finding Server-Side Prototype Pollution

One of the easiest ways to identify this vulnerability is to send an API method to Burp Suite’s Repeater and wrap a JSON formatted request body in a ‘\_\_proto\_\_’ object.

The example below shows a request that is valid for an imaginary pizza restaurant’s website. As an example, the user is supplying their favorite pizza type and phone number so that they can sign up for a rewards program.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture1-4-500x285.png)

On the backend, the API parses the request body and makes sure that all the required parameters are present. If we sent the request below, we would receive a 400 Bad Request response.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture2-4-500x265.png)

We can use this input validation to our advantage. We then wrap the valid request body in a ‘\_\_proto\_\_’ object as shown below, to which the application returns a 200 OK response.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture3-4-500x366.png)

It may seem strange that this works, but it’s our first indicator that there is a vulnerability here. At this point, there are two potential reasons that this request was accepted:

1. The API searches the request body for valid request keys.

2. An unsafe merge is being performed (more on this later.)

We can send the request below to rule out the first option. If the application is searching for valid keys, then we should be able to change the ‘\_\_proto\_\_’ object to anything else and the application will respond 200 OK. As an example, we will change ‘\_\_proto\_\_’ to `false\_positive`.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/02/Picture4-4-500x376.png)

Since the application rejected this request, we can assume that the ‘\_\_proto\_\_’ object has a special meaning in the application. Feel free to try variations such as ‘\_proto\_’ or ‘\_\_proto’, the responses should all return 400 Bad Request.

If you only receive 200 OK responses when the object’s name is ‘\_\_proto\_\_’, then congratulations, you just found a server-side prototype pollution vulnerability! Later, we will dive deeper into why this works and how this can be exploited.

## Testing for Client-Side Prototype Pollution

PortSwigger has added automated prototype pollution identification and exploitation into their browser tool, DOM Invader. The tool can identify sinks and gadgets, and even create a proof-of-concept exploit!

Sinks are places in the code where you can modify the prototype object, such as a URL parameter that is unsafely handled by the application. Gadgets are locations where polluted objects can be leveraged for exploitation. DOM Invader makes finding sinks and gadgets easy, just be sure that you have an updated version of Burp Suite and follow the steps below:

1. Open DOM Invader in Burp (Proxy > Intercept > Open Browse...