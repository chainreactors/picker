---
title: Enforcement vs. Enrollment-based Security: How to Balance Security and Employee Trust
url: https://thehackernews.com/2023/01/enforcement-vs-enrollment-based.html
source: The Hacker News
date: 2023-01-04
fetch_date: 2025-10-04T03:01:43.636438
---

# Enforcement vs. Enrollment-based Security: How to Balance Security and Employee Trust

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

# [Enforcement vs. Enrollment-based Security: How to Balance Security and Employee Trust](https://thehackernews.com/2023/01/enforcement-vs-enrollment-based.html)

**Jan 03, 2023**The Hacker NewsSecurity Automation / Cybersecurity

[![Enforcement vs. Enrollment-based Security](data:image/png;base64... "Enforcement vs. Enrollment-based Security")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSuvC4GDudryCFX42mhszySAumjeB9wax-DKuiRolIqwFCmV-XiNKgnFZCwR6JFWLlgFdqNnFpZ-fR61g7HdMMJI10m9_AHTEqfPPq0cLMPuOrYzwSSfQVmsg2CktMCBjmCMDsK4_UnuI-ZKtsMBJnoJBc-DbwQWahFBDAts3Eml8MZCh38V05PltyJg/s790-rw-e365/cerby.png)

#### Challenges with an enforcement-based approach

An enforcement-based approach to security begins with a security policy backed by security controls, often heavy-handed and designed to prevent employees from engaging in risky behavior or inadvertently expanding the potential attack surface of an organization.

Most organizations exclusively use enforcement-based security controls, usually carried out at the network level with a Cloud Access Security Broker (CASB) or a Security Services Edge (SSE). CASBs secure data between on-premises and cloud architectures, validate authorization rules, and access controls against the company's security policy. Some organizations also use CASBs to block SaaS applications, but like SSEs, CASBs only support *some* applications.

The applications these tools *don't* support are often the riskiest because they don't meet common industry and security standards, including SAML for authentication and SCIM for user management. At Cerby, these are called "unmanageable applications," and according to their research, **61% of SaaS applications are unmanageable**. Unmanageable applications are popular, and in a post-COVID world, the rate at which employees buy and deploy them has reached a new height.

Pre-COVID, IT departments were primarily responsible for purchasing and deploying organization-wide applications. The shift to remote work empowered employees across organizations to select their own tools. At the same time, rapid digitization gave them an ever widening selection of tools to choose from, causing a surge in unmanageable applications.

The average user doesn't typically think about security first. Most people tend to assume applications are secure, and some might not care about security at all. Most users care about user-friendly features, design aesthetics, and convenience. To meet these changing requirements, application vendors altered their product roadmaps; for many of them, security was no longer a top priority.

Whether employees know it or not, unmanageable applications can negatively affect an organization's security and often create more work for technology teams. *Someone* has to monitor for unmanageable applications, manually enable features like two-factor authentication (2FA), and enforce strong passwords.

To remove the burden, many organizations block or ban unmanageable applications.

It's entirely understandable why organizations take this approach – it's a quick and consistent way to address an immediate and concerning problem. However, as a long-term, comprehensive solution, a purely enforcement-based system isn't sustainable or realistic in practice.

[![Enforcement and Enrollment](data:image/png;base64... "Enforcement and Enrollment")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfmP_x9xaWYtE9l35L7I37Juk7UPI0IKVo0Q_do0MsnIZjFm6hRciCKyXhYv-KsgetXpExBRgl2cn4BUAF0zBa06MwI3XQI4t3Jegx1ErKnjd3JsrFyN_O4Hi339xnu2V-cra1R3iIfcwZsjb9hlZs5uqKR_5t6tgfWTXPufL9J-r9RE_hVvsfHkJo/s790-rw-e365/cerby.png)

Employees like choosing their work applications, and [**92% of employees and managers want complete control over application choice**](https://www.cerby.com/covid-survey-2022?utm_source=thn&utm_medium=contributed&utm_campaign=security-trust&utm_id=thn-article). This behavioral change creates some unexpected challenges for organizations with an enforcement-based approach.

For instance, many employees using banned or blocked applications also attempt to manage access manually, even when they're ill-equipped. [According to our research,](https://www.cerby.com/covid-survey-2022?utm_source=thn&utm_medium=contributed&utm_campaign=security-trust&utm_id=thn-article) employees and managers are making access management up as they go, creating risk and exposure for organizations at every point of interaction.

So, what's the solution? A more practical and forward-facing posture that balances employee application choice and employer priorities such as security and compliance.

## Benefits of enrollment-based approach

An enrollment-based cybersecurity approach empowers employees to have more freedom and individual autonomy and choice, and thereby engages them to participate in enterprise-wide security and compliance efforts actively. Unlike enforcement-based systems, an enrollment-based approach enables employees to choose the applications they want to use for work.

Cerby came into existence due to the previously unmet need for a solution that balances enforcement and enrollment and enables security and autonomy to live in peaceful coexistence. Creating this balance is the best answer for both organizations and employees. Employees should be able to **choose** their applications, and employers shouldn't worry about security.

When employees understand that application choice comes with responsibility, and the right tools are readily available to make this happen, security becomes everyone's concern. When self-enrolling and registering applications are accessible, the same employees who resent policies on application choice will willingly get on board with easier and strengthened security with the benefit ofcompliance as well.

[Check out this report](https://www.cerby.com/covid-survey-2022?utm_source=thn&utm_medium=contributed&utm_campaign=security-trust&utm_id=thn-article) to take a deeper dive into how you can empower your employees with the freedom to use their favor...