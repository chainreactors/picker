---
title: Self-Replicating Worm Hits 180+ npm Packages to Steal Credentials in Latest Supply Chain Attack
url: https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html
source: The Hacker News
date: 2025-09-17
fetch_date: 2025-10-02T20:16:23.705965
---

# Self-Replicating Worm Hits 180+ npm Packages to Steal Credentials in Latest Supply Chain Attack

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

# [Self-Replicating Worm Hits 180+ npm Packages to Steal Credentials in Latest Supply Chain Attack](https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html)

**Sep 16, 2025**Ravie LakshmananMalware / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjS_YOeydLAlQ9uG63pTINB3QdaSSEhATMNZfCUGatfAgVrEJImME3VxV7EVSABpR4mVnb4wDSo3_4sITiXidfobQvJENPJyUbTjkgkpgbBcr_dvM4LInO2dUsAvsmzJ-ND9s1F4jL1gv8i1t4n3CQT0sohCV8MJnrGKZVzNoLLV8j7ASliIr_c_V9QdNck/s790-rw-e365/npm.jpg)

Cybersecurity researchers have flagged a fresh software supply chain attack targeting the npm registry that has affected more than 40 packages that belong to multiple maintainers.

"The compromised versions include a function (NpmModule.updatePackage) that downloads a package tarball, modifies package.json, injects a local script (bundle.js), repacks the archive, and republishes it, enabling automatic trojanization of downstream packages," supply chain security company Socket [said](https://socket.dev/blog/tinycolor-supply-chain-attack-affects-40-packages).

The end goal of the campaign is to search developer machines for secrets using TruffleHog's [credential scanner](https://github.com/trufflesecurity/trufflehog) and transmit them to an external server under the attacker's control. The attack is capable of targeting both Windows and Linux systems.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The following packages have been identified as impacted by the incident -

* angulartics2@14.1.2
* @ctrl/deluge@7.2.2
* @ctrl/golang-template@1.4.3
* @ctrl/magnet-link@4.0.4
* @ctrl/ngx-codemirror@7.0.2
* @ctrl/ngx-csv@6.0.2
* @ctrl/ngx-emoji-mart@9.2.2
* @ctrl/ngx-rightclick@4.0.2
* @ctrl/qbittorrent@9.7.2
* @ctrl/react-adsense@2.0.2
* @ctrl/shared-torrent@6.3.2
* @ctrl/tinycolor@4.1.1, @4.1.2
* @ctrl/torrent-file@4.1.2
* @ctrl/transmission@7.3.1
* @ctrl/ts-base32@4.0.2
* encounter-playground@0.0.5
* json-rules-engine-simplified@0.2.4, 0.2.1
* koa2-swagger-ui@5.11.2, 5.11.1
* @nativescript-community/gesturehandler@2.0.35
* @nativescript-community/sentry 4.6.43
* @nativescript-community/text@1.6.13
* @nativescript-community/ui-collectionview@6.0.6
* @nativescript-community/ui-drawer@0.1.30
* @nativescript-community/ui-image@4.5.6
* @nativescript-community/ui-material-bottomsheet@7.2.72
* @nativescript-community/ui-material-core@7.2.76
* @nativescript-community/ui-material-core-tabs@7.2.76
* ngx-color@10.0.2
* ngx-toastr@19.0.2
* ngx-trend@8.0.1
* react-complaint-image@0.0.35
* react-jsonschema-form-conditionals@0.3.21
* react-jsonschema-form-extras@1.0.4
* rxnt-authentication@0.0.6
* rxnt-healthchecks-nestjs@1.0.5
* rxnt-kue@1.0.7
* swc-plugin-component-annotate@1.9.2
* ts-gaussian@3.0.6

The malicious JavaScript code ("bundle.js") injected into each of the trojanized package is designed to download and run TruffleHog, a legitimate secret scanning tool, using it to scan the host for tokens and cloud credentials, such as GITHUB\_TOKEN, NPM\_TOKEN, AWS\_ACCESS\_KEY\_ID, and AWS\_SECRET\_ACCESS\_KEY.

"It validates npm tokens with the whoami endpoint, and it interacts with GitHub APIs when a token is available," Socket said. "It also attempts cloud metadata discovery that can leak short-lived credentials inside cloud build agents."

The script then abuses the developer's credentials (i.e., the GitHub personal access tokens) to create a GitHub Actions workflow in .github/workflows, and exfiltrates the collected data to a webhook[.]site endpoint.

Developers are advised to audit their environments and rotate npm tokens and other exposed secrets if the aforementioned packages are present with publishing credentials.

"The workflow that it writes to repositories persists beyond the initial host," the company noted. "Once committed, any future CI run can trigger the exfiltration step from within the pipeline where sensitive secrets and artifacts are available by design."

StepSecurity, which also [shared details](https://www.stepsecurity.io/blog/ctrl-tinycolor-and-40-npm-packages-compromised) of the campaign, said the attack demonstrates a concerning evolution in supply chain threats, given that the malware includes a self-propagating mechanism enabling automatic infection of downstream packages. This behavior creates a "cascading compromise across the ecosystem."

### More Than 500 Packages Impacted

The ongoing npm supply chain incident, codenamed [Shai-Hulud attack](https://www.ox.security/blog/npm-2-0-hack-40-npm-packages-hit-in-major-supply-chain-attack/), has also leveraged the "[crowdstrike-publisher](https://www.npmjs.com/~crowdstrike-publisher)" npm account to [publish](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages) several trojanized packages. In all, no less than 500 npm packages have been impacted. -

* @crowdstrike/commitlint@8.1.1, 8.1.2
* @crowdstrike/falcon-shoelace@0.4.2
* @crowdstrike/foundry-js@0.19.2
* @crowdstrike/glide-core@0.34.2, 0.34.3
* @crowdstrike/logscale-dashboard@1.205.2
* @crowdstrike/logscale-file-editor@1.205.2
* @crowdstrike/logscale-parser-edit@1.205.1, 1.205.2
* @crowdstrike/logscale-search@1.205.2
* @crowdstrike/tailwind-toucan-base@5.0.2
* browser-webdriver-downloader@3.0.8
* ember-browser-services@5.0.3
* ember-headless-form-yup@1.0.1
* ember-headless-form@1.1.3
* ember-headless-table@2.1.6
* ember-url-hash-polyfill@1.0.13
* ember-velcro@2.2.2
* eslint-config-crowdstrike-node@4.0.4
* eslint-config-crowdstrike@11.0.3
* monorepo-next@13.0.2
* remark-preset-lint-crowdstrike@4.0.2
* verror-extra@6.0.1
* yargs-help-output@5.0.3

"After detecting several malicious Node Package Manager (npm) packages in the public npm registry, a third-party open source repository, we swiftly removed them and proactively rotated our keys in public registries," a CrowdStrike spokesperson told The Hacker News.

"These packages are not used in the Falcon sensor, the platform is not impacted and customers remain p...