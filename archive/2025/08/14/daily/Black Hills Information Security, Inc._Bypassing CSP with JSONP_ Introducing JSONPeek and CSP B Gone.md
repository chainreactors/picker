---
title: Bypassing CSP with JSONP: Introducing JSONPeek and CSP B Gone
url: https://www.blackhillsinfosec.com/jsonpeek-and-csp-b-gone/
source: Black Hills Information Security, Inc.
date: 2025-08-14
fetch_date: 2025-10-07T00:48:26.629789
---

# Bypassing CSP with JSONP: Introducing JSONPeek and CSP B Gone

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

13
Aug
2025

[Informational](https://www.blackhillsinfosec.com/category/informational/), [Jack Hyland](https://www.blackhillsinfosec.com/category/author/jack-hyland/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Web App](https://www.blackhillsinfosec.com/category/red-team/web-app/)
[CSP](https://www.blackhillsinfosec.com/tag/csp/), [CSP B Gone](https://www.blackhillsinfosec.com/tag/csp-b-gone/), [JSONPeek](https://www.blackhillsinfosec.com/tag/jsonpeek/)

# [Bypassing CSP with JSONP: Introducing JSONPeek and CSP B Gone](https://www.blackhillsinfosec.com/jsonpeek-and-csp-b-gone/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/JHyland-1-150x150.png)

| [Jack Hyland](https://www.blackhillsinfosec.com/team/jack-hyland/)

*Jack Hyland has worked in information security ever since graduating college and has dedicated his free time to deeply learning new techniques and technologies. He now spends his time creating and contributing to open-source projects along with performing security assessments of corporations networks and infrastructure.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/csp_header.png)

A Content Security Policy (CSP) is a security mechanism implemented by web servers and enforced by browsers to prevent various types of attacks, primarily cross-site scripting (XSS). CSP works by restricting resources (scripts, stylesheets, images, etc.) on a webpage to only execute if they come from approved sources. However, like most things in security, CSP isn’t bulletproof. We’ll explore one of the most common CSP weaknesses, JSONP endpoints, and introduce two new tools for security researchers to identify and exploit CSP weaknesses.

### **Content Security Policy Basics**

A content security policy can be applied in two ways:

* HTTP header
  + Content-Security-Policy: script-src \*.example.com
* Meta tag returned in the HTML document
  + **<meta http-equiv=”Content-Security-Policy” content=”script-src \*.example.com”>**

Content security policies have multiple directives that allow fine-tuned control of various internet resources. In this blog, we will mainly focus on the two directives listed below as they are relevant to JSONP.

* default-src: Sets a fallback for other directives
* script-src: Controls JavaScript sources

### **The JSONP Trick**

JSONP stands for “JSON with Padding.” The name doesn’t make much sense, but it’s a trick used by developers to load resources with arbitrary JavaScript from different origins. This trick takes advantage of the fact that a script tag’s source attribute can point to and use cross-domain resources without getting blocked by the same-origin policy.

To prove this to you, the simple HTML file below attempts to fetch **google.com** but is blocked by the browser. The developer console confirms the request was blocked since Google didn’t return a cross-origin resource sharing (CORS) header to relax the same origin policy (SOP).

```
<html>
    <script>
    	    fetch("https://google.com/ ");
    </script>
</html>
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture1.jpg)

**Cross Origin Resource Sharing Error**

If we modify the HTML page to request **google.com** using the **src** attribute of a **<script>** tag, we no longer see the CORS error and the request is successful, indicated by the 200 OK HTTP response code. This is intended functionality of browsers as its common in web development to include static JavaScript files from other domains.

```
<html>
    <script src="https://google.com/"></script>
</html>
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture2.png)

**Cross Origin Request Successful**

Now what if we configured a web server to accept a GET parameter that dynamically changes the JavaScript returned? This is how JSONP endpoints work. As shown below, **google.com** has a JSONP endpoint at **/complete/search** where we can modify the **jsonp** GET parameter to include arbitrary JavaScript. The returned content type is **text/javascript** which will be executed if referenced by a script tag.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Picture3-1.png)

**HTTP Request and Response of Google JSONP Endpoint**

### **How Does JSONP Bypass CSP?**

A website with a strict CSP configured to only allow scripts loaded from **google.com** appears quite secure at first glance.

```
"script-src https://google.com/;"
```

This policy prevents inline script tags from executing and doesn’t even allow JavaScript files from the same origin! However, if **google.com** hosts any JSONP endpoints, the CSP provides no protection against XSS. The simple HTML file below uses the CSP abov...