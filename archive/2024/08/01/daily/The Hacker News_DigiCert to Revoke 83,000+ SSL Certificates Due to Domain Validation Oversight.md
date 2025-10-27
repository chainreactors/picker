---
title: DigiCert to Revoke 83,000+ SSL Certificates Due to Domain Validation Oversight
url: https://thehackernews.com/2024/07/digicert-to-revoke-83000-ssl.html
source: The Hacker News
date: 2024-08-01
fetch_date: 2025-10-06T18:11:58.841474
---

# DigiCert to Revoke 83,000+ SSL Certificates Due to Domain Validation Oversight

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [DigiCert to Revoke 83,000+ SSL Certificates Due to Domain Validation Oversight](https://thehackernews.com/2024/07/digicert-to-revoke-83000-ssl.html)

**Jul 31, 2024**Ravie LakshmananWeb Security / Compliance

[![DigiCert](data:image/png;base64... "DigiCert")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFSKYvS6C2tA6QuQ2EgSv6V2lCs-WzvKUe-PATLOFI62WrmhWrW6RYoB_1nvrnRf8-P8hRQqOoJaWCL9i3OiZlqX7a9ewv7viU9etVVxmRQSByWpRYxw6xxVhXdIwwLW_HWJh0Z0j6Ilg7y5ywzKXrxvkTICzwMCUnpQH5J77LJFlg7ku01Omva-mInWHt/s790-rw-e365/ssl.png)

Certificate authority (CA) DigiCert has warned that it will be revoking a subset of SSL/TLS certificates within 24 hours due to an oversight with how it verified if a digital certificate is issued to the rightful owner of a domain.

The company said it will be taking the step of revoking certificates that do not have proper Domain Control Validation ([DCV](https://docs.digicert.com/en/certcentral/manage-certificates/dv-certificate-enrollment/domain-control-validation--dcv--methods.html)).

"Before issuing a certificate to a customer, DigiCert validates the customer's control or ownership over the domain name for which they are requesting a certificate using one of several methods approved by the CA/Browser Forum ([CABF](https://cabforum.org/working-groups/server/baseline-requirements/documents/))," it [said](https://www.digicert.com/support/certificate-revocation-incident).

One of the ways this is done hinges on the customer setting up a [DNS CNAME record](https://www.cloudflare.com/en-in/learning/dns/dns-records/dns-cname-record/) containing a random value provided to them by DigiCert, which then performs a DNS lookup for the domain in question to make sure that the random values are the same.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The random value, per DigiCert, is prefixed with an underscore character so as to prevent a possible collision with an actual subdomain that uses the same random value.

What the Utah-based company found was that it had failed to include the underscore prefix with the random value used in some CNAME-based validation cases.

The issue has its roots in a series of changes that were enacted starting in 2019 to revamp the underlying architecture, as part of which the code adding an underscore prefix was removed and subsequently "added to some paths in the updated system" but not to one path that neither added it automatically nor checked if the random value had a pre-appended underscore.

"The omission of an automatic underscore prefix was not caught during the cross-functional team reviews that occurred before deployment of the updated system," DigiCert said.

"While we had regression testing in place, those tests failed to alert us to the change in functionality because the regression tests were scoped to workflows and functionality instead of the content/structure of the random value."

"Unfortunately, no reviews were done to compare the legacy random value implementations with the random value implementations in the new system for every scenario. Had we conducted those evaluations, we would have learned earlier that the system was not automatically adding the underscore prefix to the random value where needed."

Subsequently, on June 11, 2024, DigiCert said it revamped the random value generation process and eliminated the manual addition of the underscore prefix within the confines of a user-experience enhancement project, but acknowledged it again failed to "compare this UX change against the underscore flow in the legacy system."

The company said it didn't discover the non-compliance issue until "several weeks ago" when an unnamed customer reached out regarding the random values used in validation, prompting a deeper review.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It also noted that the incident impacts approximately 0.4% of the applicable domain validations, which, according to an [update](https://bugzilla.mozilla.org/show_bug.cgi?id=1910322#c3) on the related Bugzilla report, affects 83,267 certificates and 6,807 customers.

Notified customers are recommended to replace their certificates as soon as possible by signing into their DigiCert accounts, generating a Certificate Signing Request (CSR), and reissuing them after passing DCV.

The development has prompted the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to publish an alert, [stating](https://www.cisa.gov/news-events/alerts/2024/07/30/digicert-certificate-revocations) that "revocation of these certificates may cause temporary disruptions to websites, services, and applications relying on these certificates for secure communication."

### Update

"DigiCert continues to actively engage with customers impacted by this incident and many of them have been able to replace their certificates," the company [said](https://status.digicert.com). "Some customers have applied for a delayed revocation due to exceptional circumstances and we are working with them on their individual situations. We are no longer accepting any applications for delayed revocation."

These include [customers operating critical infrastructure](https://status.digicert.com/incidents/3sccz3v31lc9), who it said, "are not in a position to have all their certificates reissued and deployed in time without critical service interruptions." It further noted that all impacted certificates, regardless of circumstances, will be revoked no later than August 3, 2024, 7:30 p.m. UTC.

### All Impacted Certificates Revoked

DigiCert on Sunday confirmed that "all identified TLS certificates impacted by the CNAME-based Domain Validation incident were revoked" as of August 3, 2024, 7:30 p.m. UTC.

### Vodafone, Bloomberg, ABB Most Affected

"As of August 6, 2024, 98.82% of unique leaf certificates affected by this incident that we observe in use on public-facing hosts have been revoked," attack surface management company Censys [said](https:/...