---
title: cornucopia v3.5.2
url: https://kitploit.com/en/posts/github-owasp-cornucopia-v352
source: Kitploit
date: 2026-09-11
fetch_date: 2026-09-12T06:48:09.186460
---

# cornucopia v3.5.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/39476/d7ea5ba32bc704e67b7f77b27e6bd0c701aa47a4e64fa667cb186124b9bcc164.png)

New releaseSep 11, 2026

# cornucopia v3.5.2

Card game for software teams to identify security requirements in Agile, conventional, and formal development processes. Language, platform, and technology agnostic.

Share

![](https://raw.githubusercontent.com/owasp/cornucopia/HEAD/resources/logos/cornucopia_logo.svg?raw=true)

[![OWASP Production Project](https://img.shields.io/badge/owasp-production%20project-brightgreen)](https://owasp.org/projects/)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7125/badge)](https://bestpractices.coreinfrastructure.org/projects/7125)
[![Maintainability](https://qlty.sh/gh/OWASP/projects/cornucopia/maintainability.svg)](https://qlty.sh/gh/OWASP/projects/cornucopia)
[![Code Coverage](https://qlty.sh/gh/OWASP/projects/cornucopia/coverage.svg)](https://qlty.sh/gh/OWASP/projects/cornucopia)

# OWASP Cornucopia project

OWASP Cornucopia is a mechanism in the form of a card game to assist software development teams
Identify security requirements in Agile, conventional, and formal development processes.
It is language, platform, and technology agnostic. Visit: <https://cornucopia.owasp.org/>

## The cross-references on the Web App Edition deck relate to the following versions of other OWASP and external resources:

### Standards

* [OWASP Artificial Intelligence Security Verification Standard v1.0 (AISVS)](https://owasp.org/www-project-artificial-intelligence-security-verification-standard-aisvs-docs/)
* [OWASP Application Security Verification Standard (ASVS) v4 (2019) and v5 (2025)](https://owasp.org/www-project-application-security-verification-standard/)
* [OWASP Mobile Application Security Verification Standard (MASVS) v2.1](https://mas.owasp.org/MASVS/)

### Maturity Models

* [OWASP DSOMM](https://dsomm.owasp.org/mapping)
* [OWASP SAMM](https://github.com/owaspsamm/core/tree/develop/model/activities)

### Top 10:

* [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
* [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10)
* [OWASP Top 10](https://owasp.org/Top10/2025/)
* [OWASP Top 10 Client-Side Security Risks](https://owasp.org/www-project-top-10-client-side-security-risks/)

### Guides

* [OWASP Automated Threats to Web Applications](https://github.com/OWASP/www-project-automated-threats-to-web-applications/tree/master/assets/oats/EN)
* [OWASP AI Testing Guide](https://owasp.org/www-project-ai-testing-guide/)
* [OWASP Mobile Application Security Testing Guide (MASTG) v1.7](https://mas.owasp.org/MASTG/)

### Other sources:

* [Mitre ATT&CK](https://attack.mitre.org/)
* [Mitre Atlas™](https://atlas.mitre.org/)
* [Mitre CAPEC™ v3.9](https://capec.mitre.org/data/definitions/2000.html)
* [OWASP Dev Guide Web Application Checklist](https://devguide.owasp.org/en/04-design/02-web-app-checklist/)
* [SAFECode Practical Security Stories and Security Tasks for Agile Development Environments (SAFECode) July 2012](https://safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf)
* [STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)
* [PHANTOM-B](https://shostack.org/blog/why-phantom-b/)

## Contributing to Development

### Large binary files

Please install git-lfs to ensure you can download the output files.

Install from <https://git-lfs.com/>

Then pull the binaries from git lfs.

root@kitploit:~

```
git lfs pull
```

### Using Scripts to develop and build Cornucopia

#### Scripts to build the Cornucopia Card Decks

Please read [README.md](https://github.com/owasp/cornucopia/blob/master/scripts/README.md)

#### Additional Utility Scripts

Please read [README.md](https://github.com/owasp/cornucopia/blob/master/scripts/README.md)

### Security Scanning

First time setup:

root@kitploit:~

```
pip install pre-commit
pre-commit install
```

A Bandit pre-commit hook scans Python scripts for security issues on commit.
It runs automatically via pre-commit (medium severity, high confidence).

To run manually:

root@kitploit:~

```
pre-commit run bandit --all-files
```

### Building and Deploying the Cornucopia website

<https://cornucopia.owasp.org> contains the card browser for each of the cards in the cornucopia suits together with the taxonomy and in depth explaination for each of the cards in the suits.

please read [README.md](https://github.com/owasp/cornucopia/blob/master/cornucopia.owasp.org/README.md)

### Building and Deploying the Cornucopia Game Engine: Copi

Copi (<https://copi.owasp.org>) is an online game engine where you can play Cornucopia and Elevation of Privilege. You can play all the editions of Cornucopia (website and mobile) as well as the Elevation of Privileges game.

please read [README.md](https://github.com/owasp/cornucopia/blob/master/copi.owasp.org/README.md)

## Printing

The latest printable files are released under the [pre-release](https://github.com/OWASP/cornucopia/releases/tag/pre-release). Please download final printable files from there.
The docx/pdf files can be easily printed by any desktop printer, but for the best quality use the idml InDesign files. When sending the files to a printing facility you may have to supply the fonts that has been used in order to create the work.
In case the printing facility doesn't have the fonts at hand you'll find the installable fonts under `resources/templates/Fonts` in this repository. They are both open source and free for commercial use.
The fonts can also be downloaded from the web.
Fivo Sans: <https://www.fontsc.com/font/fivo-sans>
Atkinson Hyperlegible: <https://brailleinstitute.org/freefont>

The following fonts are used:

* Leaflet: Noto Sans (Light/Regular/Italic/Medium (Italic)/SemiBoldItalic/Extra Bold)
* Leaflet: Noto Sans (Thin/Light (Italic)/Italic/Medium//Extra Bold)
* case
  + Noto Sans Condensed Bold
  + Noto Sans Condensed Extra Bold
  + Noto Sans Condensed Medium
  + Noto Sans ExtraCondensed Extra Bold
  + Noto Sans ExtraCondensed Extra Medium
* Logos:
  + Noto Sans Condensed Bold
  + Noto Sans Condensed Extra Bold
  + Noto Sans Extra Condensed Extra Bold

### Dimensions

#### Card decks:

The "bridge" files are (2.25 x 3.5" or 56mm x 87mm) standard playing cards.
The "tarot" files are (2.75 x 4.75" or 70mm x 121 mm) standard playing cards.

#### Cases:

The "bridge" is 60 x 89.25 mm x 27.15 mm
The "tarot" is 122.2 x 73.1 x 29.1 mm

the "tarot" box has standard dimensions used by Agile Stationary to print their Cyber Security Cornucopia Edition.

#### Leaflets:

The "bridge" files are 56mm x 87mm
The "tarot" files are (2.75 x 4.75")

The "bridge" and "tarot" version is 16-20 page spread depending on in which language you print.

Please be aware, that the table of content for the indesign leaflet has to be adjusted for all language versions before printing except for the english version!!
This is because indesign does not support auto adjusting the TOC.
You may need to adjust the font size to fit either a 16 or a 20 page leaflet spread.
DO NOT PRINT an 18 Page leaflet! It won't look good.

### Bleed:

A standard bleed set to 3mm for all 4 sides.

### Paper

Use 300gsm for both the bridge cards and the tarot cards.
For the case, we would recommend folding box board with anti-scuff lamination and 100gsm uncoated stock for the leaflet. The leaflets could also be laminated, but it might make them springy.

## Release process

This repository follows [semver](https://semver.org/) approach. Release a new
version means to tag commit in `master` branch. Please do not use same tag
tw...