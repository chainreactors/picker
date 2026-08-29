---
title: ruby-advisory-db
url: https://kitploit.com/en/tools/github/rubysec/ruby-advisory-db
source: Kitploit
date: 2026-08-28
fetch_date: 2026-08-29T08:31:05.357646
---

# ruby-advisory-db

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

ruby-advisory-db — Community-maintained database of security advisories for Ruby gems and runtimes, providing structured CVE/GHSA data with patched versions for vulnerability tracking and audit integration. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/rubysec/ruby-advisory-db

![](https://assets.kitploit.com/production/public/tools/53414/975700aefb4b787c4b27240d3422054ad504a312d6c20efdecfe2c39cdf304cd-display-v1.webp)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Threat Intelligence](/en/categories/threat-intelligence)[Papers & Research](/en/categories/papers-research)[Learning & Education](/en/categories/education)[Curated Resources](/en/categories/curated-resources)

![GitHub](/providers/github.png)rubysec/ruby-advisory-db

# ruby-advisory-db

Community-maintained database of security advisories for Ruby gems and runtimes, providing structured CVE/GHSA data with patched versions for vulnerability tracking and audit integration.

[View Repository](https://github.com/rubysec/ruby-advisory-db)

1.1k248385 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

[Website](https://rubysec.com)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Ruby Advisory Database

The Ruby Advisory Database is a community effort to compile all security
advisories that are relevant to Ruby libraries.
We expect others to create the data, such as getting CVE's, GHSA's,
OSVDB's, cvss', or original vulnerability information.
More details at [HERE](https://github.com/rubysec/ruby-advisory-db/blob/HEAD/docs/external-data-improvements.md).

You can check your own Gemfile.locks against this database by using
[bundler-audit](https://github.com/rubysec/bundler-audit).

## Support Ruby Security!

Do you know about a vulnerability that isn't listed in this database? Open an
issue or submit a PR.

## Directory Structure

The database is a list of directories that match the names of Ruby libraries on
[rubygems.org](https://rubygems.org/). Within each directory are one or more advisory files
for the Ruby library. These advisory files are named using
the advisories' [CVE](https://cve.mitre.org/) or [GHSA](https://help.github.com/en/articles/about-maintainer-security-advisories) or [OSVDB](https://en.wikipedia.org/wiki/Open_Source_Vulnerability_Database) (legacy) identifier number.

root@kitploit:~

```
gems/:
  actionpack/:
    CVE-2014-0130.yml  CVE-2014-7818.yml  CVE-2014-7829.yml  CVE-2015-7576.yml
    CVE-2015-7581.yml  CVE-2016-0751.yml  CVE-2016-0752.yml
rubies/:
  jruby/:
    ...
  mruby/:
    ...
  ruby/:
    ...
```

### `gems/`

The `gems/` directory contains sub-directories that match the names of the Ruby
libraries on [rubygems.org](https://rubygems.org/). Within each directory are one or more advisory
files for the Ruby library. These advisory files are named using the
advisories' [CVE](https://cve.mitre.org/) or [GHSA](https://help.github.com/en/articles/about-maintainer-security-advisories) ID.

### `rubies/`

The `rubies/` directory contains sub-directories for each Ruby implementation.
Within each directory are one or more advisory files for the Ruby
implementation. These advisory files are named using the advisories' [CVE](https://cve.mitre.org/)
or [GHSA](https://help.github.com/en/articles/about-maintainer-security-advisories) ID.

## Examples

Each advisory file contains the advisory information in [YAML](http://www.yaml.org/) format.
Here are some example advisories:

### `gems/actionpack/CVE-2023-22795.yml`

root@kitploit:~

```
---
gem: actionpack
cve: 2023-22795
ghsa: 8xww-x3g3-6jcv
url: https://github.com/rails/rails/releases/tag/v7.0.4.1
title: ReDoS based DoS vulnerability in Action Dispatch
date: 2023-01-18
description: |
  There is a possible regular expression based DoS vulnerability in Action
  Dispatch related to the If-None-Match header. This vulnerability has been
  assigned the CVE identifier CVE-2023-22795.

  Versions Affected: All
  Not affected: None
  Fixed Versions: 6.1.7.1, 7.0.4.1

  # Impact

  A specially crafted HTTP If-None-Match header can cause the regular
  expression engine to enter a state of catastrophic backtracking, when on a
  version of Ruby below 3.2.0. This can cause the process to use large amounts
  of CPU and memory, leading to a possible DoS vulnerability All users running
  an affected release should either upgrade or use one of the workarounds
  immediately.

  # Workarounds

  We recommend that all users upgrade to one of the FIXED versions. In the
  meantime, users can mitigate this vulnerability by using a load balancer or
  other device to filter out malicious If-None-Match headers before they reach
  the application.

  Users on Ruby 3.2.0 or greater are not affected by this vulnerability.
patched_versions:
  - "~> 5.2.8"
  - "~> 6.1.7, >= 6.1.7.1"
  - ">= 7.0.4.1"
```

### `rubies/ruby/CVE-2022-28739.yml`

root@kitploit:~

```
---
engine: ruby
cve: 2022-28739
url: https://www.ruby-lang.org/en/news/2022/04/12/buffer-overrun-in-string-to-float-cve-2022-28739/
title: Buffer overrun in String-to-Float conversion
date: 2022-04-12
description: |
  A buffer-overrun vulnerability is discovered in a conversion algorithm from a
  String to a Float. This vulnerability has been assigned the CVE identifier
  CVE-2022-28739. We strongly recommend upgrading Ruby.

  Due to a bug in an internal function that converts a String to a Float, some
  conversion methods like Kernel#Float and String#to_f could cause buffer
  over-read. A typical consequence is a process termination due to segmentation
  fault, but in a limited circumstances, it may be exploitable for illegal
  memory read.

  Please update Ruby to 2.6.10, 2.7.6, 3.0.4, or 3.1.2.
patched_versions:
  - ~> 2.6.10
  - ~> 2.7.6
  - ~> 3.0.4
  - '>= 3.1.2'
```

## YAML Schema

### `gems`

* `gem` [String] (required): Name of the affected gem.
* `library` [String] (optional): Name of the ruby library which the
  affected gem belongs to.
* `framework` [String] (optional): Name of the framework which the
  affected gem belongs to. (e.g. rails)
* `platform` [String] (optional): If this vulnerability is platform-specific,
  name of platform this vulnerability affects (e.g. jruby)
* `cve` [String] (optional): Common Vulnerabilities and Exposures (CVE) ID.
* `osvdb` [Integer] (optional): Open Sourced Vulnerability Database (OSVDB) ID.
* `ghsa` [String] (optional): GitHub Security Advisory (GHSA) ID.
* `url` [String] (required): The URL to the full advisory.
* `title` [String] (required): The title of the advisory or individual
  vulnerability. It must be a single line sentence.
  + Line wrap `title:` field at 80.
* `date` [Date] (required): The public disclosure date of the advisory.
* `description` [String] (required): One or more paragraphs describing the
  vulnerability. It may contain multiple paragraphs.
  + Used `description: |` if it is more than one sentence/line.
  + Line wrap `descriptions:` field at 80.
  + Do not include "POC", "PoC", or "Proof of Concept" heading sections
    (any casing) in the `description:` field.
  + Not us...