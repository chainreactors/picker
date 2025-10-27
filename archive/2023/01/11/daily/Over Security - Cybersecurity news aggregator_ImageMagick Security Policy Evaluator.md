---
title: ImageMagick Security Policy Evaluator
url: https://blog.doyensec.com//2023/01/10/imagemagick-security-policy-evaluator.html
source: Over Security - Cybersecurity news aggregator
date: 2023-01-11
fetch_date: 2025-10-04T03:34:20.298003
---

# ImageMagick Security Policy Evaluator

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# ImageMagick Security Policy Evaluator

10 Jan 2023 - Posted by Lorenzo Stella

During our audits we occasionally stumble across [ImageMagick](https://imagemagick.org/) security policy configuration files (`policy.xml`), useful for limiting the default behavior and the resources consumed by the library. In the wild, these files often contain a plethora of recommendations cargo cultured from around the internet. This normally happens for two reasons:

* Its options are only generally described on the online documentation page of the library, with no clear breakdown of what each security directive allowed by the policy is regulating. While the architectural complexity and the granularity of options definable by the policy are the major obstacles for a newbie, the corresponding knowledge base could be more welcoming. By default, ImageMagick comes with an unrestricted policy that must be tuned by the developers depending on their use. According to the docs, *âthis affords maximum utility for ImageMagick installations that run in a sandboxed environment, perhaps in a Docker instance, or behind a firewall where security risks are greatly diminished as compared to a public website.â* A secure strict policy is also made available, however [as noted in the past](https://www.synacktiv.com/en/publications/playing-with-imagetragick-like-its-2016.html) not always is well configured.
* ImageMagick [supports over 100 major file formats](https://imagemagick.org/script/formats.php#supported) (not including sub-formats) types of image formats. The infamous vulnerabilities affecting the library over the years produced a number of urgent security fixes and workarounds involving the addition of policy items excluding the affected formats and features (ImageTragick in [2016](https://imagetragick.com/), [@taviso](https://twitter.com/taviso)âs RCE via GhostScript in [2018](https://seclists.org/oss-sec/2018/q3/142), [@insertScript](https://twitter.com/insertScript)âs shell injection via PDF password in [2020](https://insert-script.blogspot.com/2020/11/imagemagick-shell-injection-via-pdf.html), [@alexisdanizan](https://twitter.com/alexisdanizan)âs in [2021](https://www.synacktiv.com/en/publications/playing-with-imagetragick-like-its-2016.html)).

## Towards safer policies

With this in mind, we decided to study the effects of all the options accepted by ImageMagickâs security policy parser and write a [tool to assist both the developers and the security teams in designing and auditing these files](https://imagemagick-secevaluator.doyensec.com/). Because of the number of available options and the need to explicitly deny all insecure settings, this is usually a manual task, which may not identify subtle bypasses which undermine the strength of a policy. Itâs also easy to set policies that appear to work, but offer no real security benefit. The toolâs checks are based on our research aimed at helping developers to harden their policies and improve the security of their applications, to make sure policies provide a meaningful security benefit and cannot be subverted by attackers.

**The tool can be found at [imagemagick-secevaluator.doyensec.com/](https://imagemagick-secevaluator.doyensec.com/).**

[![](../../../public/images/imagemagick-policy-scanner-poster.png)](../../../public/images/sample-imagemagick-eval-scan.mp4)

## Allowlist vs Denylist approach

A number of seemingly secure policies can be found online, specifying a list of insecure coders similar to:

```
  ...
  <policy domain="coder" rights="none" pattern="EPHEMERAL" />
  <policy domain="coder" rights="none" pattern="EPI" />
  <policy domain="coder" rights="none" pattern="EPS" />
  <policy domain="coder" rights="none" pattern="MSL" />
  <policy domain="coder" rights="none" pattern="MVG" />
  <policy domain="coder" rights="none" pattern="PDF" />
  <policy domain="coder" rights="none" pattern="PLT" />
  <policy domain="coder" rights="none" pattern="PS" />
  <policy domain="coder" rights="none" pattern="PS2" />
  <policy domain="coder" rights="none" pattern="PS3" />
  <policy domain="coder" rights="none" pattern="SHOW" />
  <policy domain="coder" rights="none" pattern="TEXT" />
  <policy domain="coder" rights="none" pattern="WIN" />
  <policy domain="coder" rights="none" pattern="XPS" />
  ...
```

In ImageMagick 6.9.7-7, an [unlisted change](https://blog.awm.jp/2017/02/09/imagemagick-en/) was pushed. The policy parser changed behavior from disallowing the use of a coder if there was at least one `none`-permission rule in the policy to respecting the last matching rule in the policy for the coder. This means that it is possible to adopt an allowlist approach in modern policies, first denying all coders `rights` and enabling the vetted ones. A more secure policy would specify:

```
  ...
  <policy domain="delegate" rights="none" pattern="*" />
  <policy domain="coder" rights="none" pattern="*" />
  <policy domain="coder" rights="read | write" pattern="{GIF,JPEG,PNG,WEBP}" />
  ...
```

## Case sensitivity

Consider the following directive:

```
  ...
  <policy domain="coder" rights="none" pattern="ephemeral,epi,eps,msl,mvg,pdf,plt,ps,ps2,ps3,show,text,win,xps" />
  ...
```

With this, conversions will still be allowed, since policy patterns are case sensitive. Coders and modules must always be upper-case in the policy (e.g. âEPSâ not âepsâ).

## Resource limits

Denial of service in ImageMagick is quite easy to achieve. To get a fresh set of payloads itâs convenient to search [âoomâ](https://github.com/ImageMagick/ImageMagick/issues?q=oom) or similar keywords in the recently opened issues reported on the Github repository of the library. This is an issue since an ImageMagick instance accepting potentially malicious inputs (which is often the case) will always be prone to be exploited. Because of this, the tool also reports if reasonable limits are not explicitly set by the policy.

## Policy fragmentation

Once a policy is defined, itâs important to make sure that the policy file is taking effect. ImageMagick packages bundled with the distribution or installed as dependencies through multiple package managers may specify different policies that interfere with each other. A quick `find` on your local machine will identify multiple occurrences of `policy.xml` files:

```
$ find / -iname policy.xml

# Example output on macOS
/usr/local/etc/ImageMagick-7/policy.xml
/usr/local/Cellar/imagemagick@6/6.9.12-60/etc/ImageMagick-6/policy.xml
/usr/local/Cellar/imagemagick@6/6.9.12-60/share/doc/ImageMagick-6/www/source/policy.xml
/usr/local/Cellar/imagemagick/7.1.0-45/etc/ImageMagick-7/policy.xml
/usr/local/Cellar/imagemagick/7.1.0-45/share/doc/ImageMagick-7/www/source/policy.xml

# Example output on Ubuntu
/usr/local/etc/ImageMagick-7/policy.xml
/usr/local/share/doc/ImageMagick-7/www/source/policy.xml
/opt/ImageMagick-7.0.11-5/config/policy.xml
/opt/ImageMagick-7.0.11-5/www/source/policy.xml
```

Policies can also be configured using the [-limit](https://imagemagick.org/script/command-line-options.php#limit) CLI argument, [MagickCore API](https://imagemagick.org/api/resource.php#SetMagickResourceLimit) methods, or with environment variables.

## A starter, restrictive policy

Starting from the most restrictive policy described in the official documentation, we designed a restrictive policy gathering all our observations:

```
<policymap xmlns="">
  <polic...