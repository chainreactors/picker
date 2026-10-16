---
title: Drupal Patches Critical Field UI Flaw With Unauthenticated RCE Path via Contributed Modules
url: https://thehackernews.com/2026/10/drupal-patches-critical-core-rce-flaw.html
source: The Hacker News
date: 2026-10-15
fetch_date: 2026-10-16T06:37:55.266349
---

# Drupal Patches Critical Field UI Flaw With Unauthenticated RCE Path via Contributed Modules

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Drupal Patches Critical Field UI Flaw With Unauthenticated RCE Path via Contributed Modules](https://thehackernews.com/2026/10/drupal-patches-critical-core-rce-flaw.html)

**Swati Khandelwal**Oct 15, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWENfwA4xQHfwINduJpVTTiNeAmBkevujxbloFijpq7PQV8xOV-iApTx_f5g9ImW_oKJolO1RuhlNeDc2NwoWKOdPfjfdDzMhCuOsWtdyCZOOs2fTW4vmXYixSIdOCw2CwsvSgvEOPxqHUwSoRpxxoMRKKRqsqezOqVNpF5uQaU3cdI7z9L_Y_2WeTImA/s1700-nu-rw-lo-l85-e365/drupal.jpg)

Drupal core has a critical flaw in its Field UI module that could let an attacker run code on the site's server, and fixes were shipped on October 14 in Drupal 11.4.10, 11.3.19, and 10.6.19.

An attacker cannot reach the flaw through core alone, the Drupal Security Team said in [its advisory](https://www.drupal.org/sa-core-2026-014). Several exploit paths exist through contributed modules, and at least one known path needs no login.

Tracked as **CVE-2026-108097**, the flaw sits in Field UI, the core module behind the admin pages where site builders manage fields and how they display. Drupal rates it 19 out of 25 on its own risk scale, the level the project calls critical.

The advisory does not name the contributed modules that open a path to the flaw, and custom code may also expose it. Drew Webber of the Security Team and Octavio Galland are credited with reporting it.

### What to Do Now

The fixed release for each supported branch:

* Drupal 11.4.x: update to [11.4.10](https://www.drupal.org/project/drupal/releases/11.4.10)
* Drupal 11.3.x: update to [11.3.19](https://www.drupal.org/project/drupal/releases/11.3.19)
* Drupal 10.6.x: update to [10.6.19](https://www.drupal.org/project/drupal/releases/10.6.19)
* Drupal 12.0.0 beta: [12.0.0-beta2](https://www.drupal.org/project/drupal/releases/12.0.0-beta2), which is not for production use
* No fix: Drupal 11.2.x and below, 10.5.x and below, and Drupal 8 and 9, all of which are end-of-life

Both 11.3.x and 10.6.x lose security coverage in December 2026.

In the week starting October 4, 151,442 of the 531,499 sites that [reported their Drupal core version to drupal.org](https://new.drupal.org/project/usage/drupal) (28.5%) were on a branch that the advisory lists as affected and that received no fix.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

A site that cannot update yet can uninstall the Field UI module, field\_ui, which "will provide protection while sites are updated," the advisory says. The admin pages for managing fields and their display are unavailable while the module is uninstalled.

Field UI is installed by Drupal's Standard install profile, so a site built from that profile has the module unless someone removed it.

[Drupal Steward](https://new.drupal.org/steward), a web application firewall service with rules written by the Security Team, already blocks some known attack vectors for this flaw. Acquia, Pantheon, Ironstar, and Skpr run it for their customers. It does not cover every possible exploit, and those sites should still update, the advisory says.

The advisory rated the flaw as having no publicly available exploit code at the time of publication. As of October 15, none had surfaced, and neither the advisory nor public reports described attacks using it.

The Security Team had [pre-announced the release on October 12](https://www.drupal.org/psa-2026-10-12) and told sites to reserve time for it "because exploits might be developed within hours or days."

In May, Drupal [reported exploit attempts within two days](https://thehackernews.com/2026/05/drupal-core-sql-injection-bug-actively.html) of its advisory for a core SQL injection flaw that affected only sites on PostgreSQL, and CISA added that flaw to its catalog of exploited vulnerabilities.

### What the Fix Changed

Field UI builds its admin tables from render arrays, the PHP arrays Drupal turns into HTML. Before the fix, the table element's pre-render step ran whatever PHP callable each table row carried in its #region\_callback property, through call\_user\_func\_array, with no check on what that callable was.

Drupal's renderer has refused to run untrusted render callbacks [since version 8.8 in 2019](https://www.drupal.org/node/2966725), a restriction added after earlier advisories showed that the render system could too easily call arbitrary callbacks. The renderer trusts the table element's own methods, so it ran the pre-render step, and the check never reached the callable that step then executed.

[The 11.4.10 code](https://raw.githubusercontent.com/drupal/drupal/11.4.10/core/modules/field_ui/src/Element/FieldUiTable.php) no longer calls the callback. It reads each row's region from the row's own region value and uses the table's hidden region, or its first region, when that value is not a known region. The same call had been in the code since at least Drupal 8.9.0 in 2020.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

In core itself, the callback is set only by Field UI's own display forms. Custom code that set #region\_callback on a field\_ui\_table row will find it no longer runs after the update. [Pantheon tells sites](https://docs.pantheon.io/release-notes/2026/10/drupal-7-107-security-update) to check such code and to test the manage fields and manage display pages after updating.

Separately, the [Entity List module](https://www.drupal.org/sa-contrib-2026-218) received its own critical remote code execution advisory, CVE-2026-108099, with the same conditions, including a known path that needs no login. Its [3.0.10 release note](https://www.drupal.org/project/entity_list/releases/3.0.10) says the fix mirrors the Field UI change, and updating core does not update the module. In the week starting October 4, [90 sites reported using it](https://new.drupal.org/project/usage/entity_list).

The sam...