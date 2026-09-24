---
title: A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You
url: https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html
source: The Hacker News
date: 2026-09-23
fetch_date: 2026-09-24T07:08:23.743726
---

# A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [A Leaked GitLab Issue Email Address Lets Anyone Push Code and Run CI Jobs as You](https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html)

**Swati Khandelwal**Sep 23, 2026DevOps Security / Supply Chain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjaHKzSxkk0R4wjlziQHsR5vS1s1mTJovZkES9XL9nn5VLYiM55XuJoiGP9cugwNUOBMEMG3NrW3iBL9cVOqfp0F-9roYS7K7R5w8t3_NJr61_2_XgRNltvjXBFoGLfQPQFhUk0ju_mMCRCqJHjr76BrbngafAtElKkD-LZWZ7uUcY82i8PAMKh0ljHJQI/s1700-nu-rw-lo-l85-e365/gitlab-email.jpg)

The private email address GitLab gives you for filing issues by email is a credential. Anyone who gets it can email a patch that GitLab commits in your name, to any branch you can push to, including main, and can start CI/CD jobs that run as you.

GitLab shows each user this address behind a button labeled "Email work item to this project." Mail sent to it opens an issue in that project, authored by you.

The string in the middle of the address is a token tied to your account, and GitLab's documentation says it does not expire.

The address looks like it belongs to one project. It does not. [Aikido Security](https://www.aikido.dev/blog/gitlab-email-push-to-main), which reported the behavior, found that the addresses GitLab creates for a user's different projects all share the same token, and that the token applies to every project the account can open, public or private.

GitLab does not check who sent the email. Any mailbox can write to the address, and GitLab acts on the message as if it came from you. Whoever holds the address can both sign in as you and act with your permissions, without ever touching your mailbox.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The address does more than file bugs. Aikido showed how a holder turns it into a way to commit code, using GitLab's own [merge request by email](https://docs.gitlab.com/user/project/merge_requests/creating_merge_requests/#by-sending-an-email) feature:

1. Change the address suffix from -issue to -merge-request. GitLab then opens a merge request instead of an issue.
2. Write a patch, and put the name of a target branch in the email subject line.
3. Attach the patch and send it. GitLab applies the patch to that branch, and creates the branch if it does not already exist.
4. The change lands as a commit on that branch, authored by you. If it is a branch you can push to, that includes main.
5. If the patch edits the project's .gitlab-ci.yml file and your role allows it, GitLab runs the attacker's job as you.

The merge request itself cannot be directed at a copy of the project the attacker controls, which is why the attached patch, not the merge request, carries the code.

Two things keep this from being worse. The token carries only your own permissions, so how far an attacker gets depends on your role. A leaked address for a Guest account is nearly useless, whereas one for a Maintainer can access protected branches and CI/CD secrets.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigdfoyYdWTEbsz954IcXpc1Na1WOd1I_BkO5P5LUDUkO2rIOKbc9V263qOcds8Du2rYgUy7d5CFJtJOxRtFTN6hqXi3mUzAPEsXPAxS4bjW-KETWR9oFZvJA9Jc9mNRodBDsw3Ggxz0Sd1pE2s_F8ZkO1VPLbvR7S6CsrAZYjfXHShTQD_axoybIojNlI/s1700-nu-rw-lo-l85-e365/email-2.png)

Reaching a project also takes more than the address. GitLab works out the target from the project's path and its numeric ID, so an attacker who wants a particular project needs that project's path and ID as well as the token. Public projects publish both. A private project takes a separate leak that names it, though GitLab's project IDs are easy to guess.

Because incoming email is exempt from IP restrictions, the attack can originate from outside an IP allowlist. GitLab's documentation states that incoming email is [not subject to IP restrictions](https://docs.gitlab.com/user/group/access_and_permissions/).

Aikido locked a private project to a single IP address that was not its own. GitLab blocked its browser and refused a git clone, but it accepted the merge request email, and the commit landed on main.

The same path skips two-factor authentication. GitLab's documentation notes that incoming email features work [without 2FA](https://docs.gitlab.com/administration/incoming_email/), even on instances that require it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLBqbDyqv6FtseJxPu6TOvCbKyvraj6sXEEmyxQdoegUdpR1I0AshCdXRiedWuMWfCbNI5xJqpj1PA_wLogFqv4ZxLXeYyU9yFLzDTJnMdSSxWIdYeMV2p4Ght3f_MxA4tx41UVzFEenLF9w1ypuiWcYyKAXNoyaaIaMfXLr28_en3xkwNG5p7hWOAK0E/s1700-nu-rw-lo-l85-e365/email-1.png)

Every GitLab.com account has one of these tokens, and so does every self-managed GitLab instance with incoming email turned on, which is the default on GitLab.com.

GitLab Dedicated does not appear to be affected, because GitLab limits the feature to self-managed and GitLab.com, but Aikido said it could not test Dedicated directly.

### What to do

You cannot stop other people from having the feature, but you can cut off a leaked address.

* Reset your incoming email token from the [personal access tokens page](https://docs.gitlab.com/security/tokens/#incoming-email-token) in your profile. The reset replaces every project address at once, so an address you are actively using will stop working until you hand out the new one.
* Look through your own READMEs, contributing guides, and support pages for a posted address. Aikido said it found about a dozen live addresses this way, most of them published on purpose as places to send bug reports, and a few in widely used open-source projects.
* On a self-managed instance, an administrator can turn incoming email off for the whole instance. There is no setting that lets an individual user turn off email-based issue or merge request creation.

GitLab changed the text around the token after Aikido's report. The description now ...