---
title: Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection
url: https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html
source: The Hacker News
date: 2026-08-17
fetch_date: 2026-08-18T02:54:01.742244
---

# Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Snowflake GitHub Actions Flaw Lets Crafted Issues Trigger Command Injection](https://thehackernews.com/2026/08/snowflake-github-actions-flaw-lets_0330881554.html)

**Swati Khandelwal**Aug 17, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJW5BJKjwNfnH2t8RrvgW0wUO3_ZJWnw30aS6GlU9qoaOWMQcyoZ9ZOZmTgLo7hWAqHlKDK2b4MrtF23Jv_1-1Ffd6bo6VlR8exLvIISBANwjHnW3dv7wLgCtyCIDlndpJ67TajeEpN-Ww9eVVutmS4fTpcDPJtlAk_ZU0GLtnkDvYLlqWPv75uMH7ob__/s1700-e365/snowflake.jpg)

Cybersecurity researchers at Wiz have disclosed a new GitHub Actions workflow injection vulnerability in Snowflake's public [snowflakedb/snowflake-connector-net](https://github.com/snowflakedb/snowflake-connector-net) repository that it said could be exploited through a crafted GitHub issue to execute commands in a workflow containing internal Jira credentials.

The issue was present in [.github/workflows/jira\_issue.yml](https://github.com/snowflakedb/snowflake-connector-net/blob/4a1b8cecd65b899540e4324715557d6b080ddeb5/.github/workflows/jira_issue.yml), which ran when a public issue was opened and exposed JIRA\_BASE\_URL, JIRA\_USER\_EMAIL, and JIRA\_API\_TOKEN to the same workflow step. The weakness was confined to the repository's CI/CD automation, with no affected Snowflake Connector for .NET release identified.

The workflow inserted attacker-controlled issue title and body values directly into a shell run: block. It also checked github.event.pull\_request.user.login even though the event was an issue, meaning the referenced pull request property did not exist.

[GitHub says](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts), "If you attempt to dereference a nonexistent property, it will evaluate to an empty string." In this case, the comparison against whitesource-for-github-com[bot] did not stop an ordinary issue from reaching the job.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Wiz [said](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) its Red Agent system exploited the injection during authorized security testing after the first payload resulted in a shell syntax error and the system changed its approach. The researchers said they subsequently received an out-of-band callback from the GitHub Actions runner and obtained the Jira API token used by the workflow.

The token, according to Wiz, belonged to qa@snowflake.net and allowed read access to Jira projects covering engineering, security compliance, and bug bounty tracking on snowflakecomputing.atlassian.net. The underlying Jira permissions, workflow run, and audit records are not public.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1e6rDEmjXWfr6jjXEHc8iH-LGkFKO36VVym4Dcjs9I9HWWmcEc4msFS6quNV93gzqLXfeMbsJtgZRMRAY7qOxT698AJxX9kclzAMRNw8tIjdqRIZ6Yf_JwL4Jh8sfGYzLdQW-VyObHOdtXSP2as1oQVoUs67h1h99BGDdrjCuMjGyUvXx3Ts5Lxf3gyxA/s1700-e365/comment.jpg)

Wiz said it reported the issue to Snowflake through HackerOne on June 23, 2026, under report #3819931. Snowflake merged a fix that day in [pull request #1402](https://github.com/snowflakedb/snowflake-connector-net/pull/1402), replacing the direct GitHub expression expansion with environment variables that are passed to jq as arguments.

The vulnerable workflow had reached the default branch five days earlier, on June 18, when [pull request #1218](https://github.com/snowflakedb/snowflake-connector-net/pull/1218) was merged. The corrected handling remains in the repository's [master branch](https://github.com/snowflakedb/snowflake-connector-net/blob/master/.github/workflows/jira_issue.yml).

Snowflake said in a statement reproduced by Wiz that "our investigation found no evidence of unauthorized access." Wiz said the Jira token was rotated on June 24 and that Snowflake's review found no unrelated external use of it during the five-day exposure window. Snowflake's underlying audit logs have not been made public.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYuPX6yhUhVIH8mkaqGF-kxLLo2HJqOuYTQeLDYTCu8hzVVaNxfSjMcg_VLaT5woKdPnGadBRanIQJD9HZkrxNV6rXpTNxIc-XWf0u6yri82ocCjDEVg14HFDG8hvMxJZa8vvBgglgOKKiKwi307c2NJyo90WmCoHis3WrFepopBOVkI-qISbJoxX-4bO-/s1700-e365/jira.jpg)

Wiz described the flaw as resulting from a GitHub Copilot Autofix change, although the underlying GitHub history does not establish Copilot as the author of the vulnerable jira\_issue.yml code. The explicit Copilot co-authored commit, [6d0e2fa](https://github.com/snowflakedb/snowflake-connector-net/pull/1218/commits/6d0e2fa1d644d04e036b9afa69513aa0c0c83132), changed jira\_close.yml, while the unsafe jira\_issue.yml refactor appears in a separate August 25, 2025, commit, [094038e](https://github.com/snowflakedb/snowflake-connector-net/pull/1218/commits/094038e59d112906f1790acf39999045fc0df243), attributed by GitHub to sfc-gh-hpathak.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Both changes were later folded into the June 18 squash merge commit [4a1b8ce](https://github.com/snowflakedb/snowflake-connector-net/commit/4a1b8cecd65b899540e4324715557d6b080ddeb5), which lists Copilot Autofix among its co-authors. The commit history therefore confirms Copilot participation in pull request #1218, but not authorship of the vulnerable lines.

[GitHub had documented this class of workflow injection in July 2025](https://github.blog/security/vulnerability-research/how-to-catch-github-actions-workflow-injections-before-attackers-do/), warning against expanding untrusted issue data directly inside run: blocks and recommending the use of intermediate environment variables.

As of August 17, 2026, no CVE, CVSS score, or CISA Known Exploited Vulnerabilities (KEV) catalog entry had been located for the issue, and no connector release update tied to it had been identified. The vulnerable interpolation is ...