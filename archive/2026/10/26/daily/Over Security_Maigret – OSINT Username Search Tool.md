---
title: Maigret – OSINT Username Search Tool
url: https://www.darknet.org.uk/2026/10/maigret-osint-username-search-tool/
source: Over Security
date: 2026-10-26
fetch_date: 2026-10-27T07:05:37.133687
---

# Maigret – OSINT Username Search Tool

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet.org.uk is a cybersecurity site online since 2000. It covers security tools, technical research and hacking news, alongside an archive of earlier posts.

You are here: [Home](https://www.darknet.org.uk/) / [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) / Maigret – OSINT Username Search Tool

# Maigret – OSINT Username Search Tool

Published October 26, 2026 |

Views: 190

Give Maigret a username and it finds the sites with an account by that name, reads the profiles it finds for names, locations and links to other accounts, then searches for the usernames those links give up. The README puts the reach at 5,900 sites. A default run checks 500 of them, and the list it checks can change overnight without you installing anything, which matters as soon as a result has to go into a report.

![Maigret: Which 500 did you search? Heavy graphite chain links joined by one orange enamel link.](https://www.darknet.org.uk/wp-content/uploads/2026/10/maigret-osint-username-search-1024x576.webp)

Maigret checks 500 sites by default, using a site list that updates itself.

## What is Maigret?

Maigret is an open-source OSINT tool that searches for accounts by username, written in Python and released under the MIT licence. For each name you give it, it requests the matching profile URL on each site it checks and reports the accounts it finds, along with whatever it could pull from the page: full name, location, creation date, follower counts and links to other profiles. Release 0.6.6 came out on 18 September 2026, and the project was still committing in October.

Advertisement

Recursive search is what lifts it above a plain username checker, and it is on by default. When a profile links to another account, Maigret takes the username or ID from that link and starts a new search for it. The documentation’s own example finds a Twitter handle on a GitHub profile and goes on to find a Telegram account under that second name.

On one person that is exactly what you want. On a profile that links to a colleague, a former employer or a shared project, Maigret searches those names as well, so check which names in the output you actually gave it. `--no-recursion` turns it off.

## How many sites does Maigret check?

By default, 500. The site database in the 0.6.6 release holds 5,897 entries, but a run without options checks the 500 ranked highest by Majestic Million, plus any mirror sites tied to a platform in that top 500. `-a` (`--all-sites`) lifts the 500 limit, `--top-sites` sets a different number, and `--tags` picks sites by category or country.

I counted the 0.6.6 database. 694 of its 5,897 entries are marked disabled – checks the maintainers have switched off – which leaves 5,203 enabled, and only 854 of those have a rank recorded at all. The enabled 5,203 are the ceiling for `-a`, not quite what it checks: twelve of them are not ordinary web checks – four Tor sites, one I2P site and seven DNS lookups – and run only with `--tor-proxy`, `--i2p-proxy` or `--with-domains`. Another 25 look up other identifiers, such as Steam or VK IDs, rather than usernames. So a plain `-a` search for a username works from 5,166. The disabled entries come back only with `--use-disabled-sites`, which the documentation warns “may cause many false positives”. Of the enabled entries, 2,664 carry the `forum` tag and 1,114 the `ru` tag.

So `-a` does not give you more of the big platforms. It adds thousands of smaller communities – about half the enabled database is forums, and a fifth is tagged Russian – which is valuable when that is where your subject lives and noise when it isn’t.

Tags are the more precise tool. `--tags us,jp` limits a search to sites marked as American or Japanese, `--tags coding` to software development sites, and `--exclude-tags` drops a category, so `--tags forum --exclude-tags ru` searches forums but skips the Russian ones. The documentation warns that the tag markup “is still not stable”, so a tag tells you how a site was classified, not that the classification is complete.

Advertisement

## Which site database did your Maigret search use?

Not necessarily the one that came with the release, and not necessarily the newest either. On startup, at most once every 24 hours, Maigret checks whether a newer site database has been published. If one has, and it is compatible with your version, it downloads it to `~/.maigret/data.json` and uses it in place of the copy bundled with the release. Between checks it uses the copy it cached last time, and if a download fails or the new list does not fit your version, it falls back to the bundled one. Two people on the same version can therefore search different site lists, and so can you, rerunning a search a week later.

That is the right default for someone who wants as many checks working today as possible. For an investigation that may have to be repeated or explained, it means the version number does not tell you what was searched. According to the documentation, every run prints the database it loaded, as `[+] Using sites database: <path> (<N> sites)`. Keep that line with the results, and keep the file it names too: copy that database next to your case notes and record its SHA-256, because the cached copy at `~/.maigret/data.json` is replaced by the next update.

For case work I would hold the list still and update it on purpose. `--no-autoupdate` uses the cached or bundled database as it is, `"no_autoupdate": true` in `~/.maigret/settings.json` makes that permanent, and `--force-update` fetches a new one when you decide to. `--db` loads a database file you name and skips the update check entirely, so pointing it at the copy you kept is how you rerun a search against exactly the list you used before.

The documentation itself recommends turning updates off for Docker containers, CI pipelines and air-gapped machines.

## How to use Maigret

Give it one or more usernames. `maigret username` searches the default 500 sites, `--html` adds an HTML report, and the README’s examples cover the common variations:

maigret username --html
maigret username --tags coding
maigret user1 user2 user3 -a

|  |  |
| --- | --- |
| 1  2  3 | maigret username --html  maigret username --tags coding  maigret user1 user2 user3 -a |

Reports come in most formats you might need: HTML, PDF (an optional extra, installed with `pip install 'maigret[pdf]'`), XMind, CSV, plain text, newline-delimited JSON with `--json ndjson`, an interactive graph with `--graph` and a Neo4j Cypher script with `--neo4j`.

`--parse` takes a profile URL, extracts the IDs and usernames on it and searches for those, and `--permute` turns two or more names into likely variants (`john doe` into `johndoe`, `j.doe` and so on) and searches them all.

Treat every hit as a lead to open, not a finding. The project’s usage page says some sites “may return false positive results”. A missing result needs the same care, because a site can be absent from the output for three reasons: the name is not there, the site was never checked (outside the 500, disabled, or a `.onion` site with no Tor proxy set, which Maigret skips si...