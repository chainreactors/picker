---
title: ClickFix moves into the browser: Cryptocurrency theft with Google-hosted C2
url: https://blog.talosintelligence.com/clickfix-moves-into-the-browser/
source: Over Security
date: 2026-09-08
fetch_date: 2026-09-09T06:56:41.115740
---

# ClickFix moves into the browser: Cryptocurrency theft with Google-hosted C2

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# ClickFix moves into the browser: Cryptocurrency theft with Google-hosted C2

By
[Sean Gallagher](https://blog.talosintelligence.com/author/sean-gallagher/)

Tuesday, September 8, 2026 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)

* Cisco Talos is tracking a cryptocurrency-stealing campaign that abuses the Google Visualization API for command and control (C2), retrieving obfuscated JavaScript from a publicly published Google Sheets document and injecting it into the victim's browser session.
* The actors use a variation on ClickFix social engineering. Instead of convincing targets to run commands against the operating system, they convince targets to paste JavaScript into the Chrome address bar or install it into the Tampermonkey browser extension, which also provides persistence.
* The lure poses as a leaked vulnerability report describing a nonexistent API flaw at cryptocurrency swap services, and is aimed at users willing to exploit it for financial gain. Talos observed lures distributed through Telegram, DarkForums, and paste sites.
* The injected script functions as a web skimmer. It hooks the browser's fetch API, replaces cryptocurrency deposit addresses in server responses and the user's clipboard, and displays counterfeit "bonus" interface elements.

---

Cisco Talos has recently observed a criminal campaign that leveraged an interesting twist on what we refer to as “legitimate service abuse.” In this monthslong campaign, the criminal actors used the Google Visualization API as part of a scheme to inject malicious JavaScript into two cryptocurrency trading websites.

This campaign uses a twist on the tactics associated with [“ClickFix” social engineering attacks](https://www.proofpoint.com/us/blog/threat-insight/clipboard-compromise-powershell-self-pwn), in which targets are manipulated into copying and pasting PowerShell or other commands and executing them to launch malware. Rather than targeting the victim device’s OS, the actors behind this campaign aim to convince the user to inject malicious code into their own browser session.

Early versions of this campaign began in [early October 2025](https://bolster.ai/blog/swapzone-profit-trick-web-inject-from-lure-to-live-dom-hijack). The social engineering lures used initially focused on getting targets to paste a code snippet directly into the Chrome web browser’s navigation bar; the latest version relies on a legitimate Chrome plugin, Tampermonkey, to inject a loader script pasted in by the user and provide persistence across sessions with the current targeted site.

In March 2026, the actors behind the campaign began using the Google Visualization API to deliver malicious scripts stored in a Google Sheets document. In July, after frequent disruption of their posts on shared text sites, the actors moved to hosting all the components of their campaign in Google Docs and Google Sheets.

So far, the actors behind the scheme have largely targeted individuals who frequent web discussion boards and forums focused on cryptocurrency trading, software development, basic cybersecurity, and hacking. The lure used in the campaign is designed to appeal mostly to would-be cybercriminals looking to make a quick profit off an “API vulnerability” that doesn’t exist to get bigger payouts on cryptocurrency trades.

While this campaign doesn’t pose a specific threat to most organizations, the approaches that the actors here are using do. These techniques and tools could be leveraged in other malware and web attacks with much wider impact, including supply-chain attacks on e-commerce sites and other customer-facing systems.

## Just Google it

Google application abuse for C2 is not new by any stretch of the imagination. There have been multiple cases of state-sponsored actors using Google Sheets APIs, Google Drive, and other Google cloud services to help control deployed malware, concealing communications within traffic to otherwise trusted network spaces.

Hunting for these threats usually requires examination of DNS traffic and the processes that are making the requests to reach these destinations — like a random executable making a DNS request for “docs.google[.]com”. But when the requests are made from within a browser session, that makes detection much more difficult.

The [Google Visualization API](https://developers.googleblog.com/introducing-the-google-visualization-api/) is a feature of Google Docs that is almost as old as the platform itself. Initially introduced in 2008, the API provides free, unauthenticated read-only access to the contents of any Google Sheets spreadsheet that has been publicly published to the web via queries embedded in a URI. These queries result in delivery of data from within the spreadsheet in JSON format or as an HTML table.

A Visualization API request URI looks like this:

```
https[:]//docs.google[.]com/spreadsheets/d/[document identifier] /gviz/tq?[query language input formatted for HTTP]
```

The API’s query language is very similar to Structured Query Language (SQL). For example, to get all of the content from a sheet’s column B returned as a JSON object, the query portion of the URI would be:

```
/gviz/tq?tqx=out:json&tq=SELECT%20B
```

API responses in JSON are returned in the format like the one below, ready to be parsed by the calling JavaScript application:

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/09/carbon.png)

This is a read-only API, so it can’t be used by an application to alter the data in the spreadsheet. However, an application could append to the data to a spreadsheet connected to a Google Forms page [by sending an HTML POST request](https://www.sophos.com/en-us/blog/phishing-and-malware-actors-abuse-google-forms-for-credentials-data-exfiltration). Pres...