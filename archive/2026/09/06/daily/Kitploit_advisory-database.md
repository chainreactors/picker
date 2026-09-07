---
title: advisory-database
url: https://kitploit.com/en/tools/github/pypa/advisory-database
source: Kitploit
date: 2026-09-06
fetch_date: 2026-09-07T06:48:36.251711
---

# advisory-database

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

advisory-database — Community-owned database of security advisories for Python packages on PyPI, providing structured vulnerability data in OSV format for integration with tools like pip-audit and OSV. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/pypa/advisory-database

![](https://assets.kitploit.com/production/public/tools/54273/578c03b2936983e49340afa1300fa2b4c4def635067b23238967f954aa3d0d2e-display-v1.webp)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[DevSecOps](/en/categories/devsecops)[Threat Intelligence](/en/categories/threat-intelligence)[Supply Chain Security](/en/categories/supply-chain-security)[Curated Resources](/en/categories/curated-resources)

![GitHub](/providers/github.png)pypa/advisory-database

# advisory-database

Community-owned database of security advisories for Python packages on PyPI, providing structured vulnerability data in OSV format for integration with tools like pip-audit and OSV.

[View Repository](https://github.com/pypa/advisory-database)

368109273 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Python Packaging Advisory Database

This is a community owned repository of advisories for packages published on
<https://pypi.org>.

Advisories live in the [vulns](https://github.com/pypa/advisory-database/blob/main/vulns) directory and use a YAML encoding of
a [simple format](https://ossf.github.io/osv-schema/).

## Contributing advisories

### Making a pull request

Existing entries can be edited by simply creating a pull request.

To introduce a new entry, create a pull request with a new file that has a name
matching `PYSEC-0000-<anything>.yaml`. This will be later picked up by
automation to allocate a proper ID once merged.

You can validate the structure of your YAML file by running:

root@kitploit:~

```
pipx run check-jsonschema --schemafile https://raw.githubusercontent.com/ossf/osv-schema/main/validation/schema.json <PATH TO YAML FILE>
```

### Triage process

Much of the existing set of vulnerabilities are collected from the
 feed.

[NVD CVE](https://nvd.nist.gov/vuln/data-feeds)

We use [this tool](https://github.com/google/osv/tree/master/vulnfeeds), which
performs a lot of heuristics to match CVEs with exact Python packages and
versions (which is a difficult problem!) and a small amount of human triage to
generate the `.yaml` entries here.

## Using this data

### Marking specific attributes as vulnerable

To help with reducing false positive matches, entries in this database can include details on specific code elements of a package that are vulnerable.
OSV entries in this database have the following [`ecosystem_specific`](https://ossf.github.io/osv-schema/#affectedecosystem_specific-field) definition to encode this:

root@kitploit:~

```
"ecosystem_specific": {
  "imports": [
    {
       "attribute": string,
       "modules": [ string ],
    }
  ]
}
```

"imports" is a JSON array containing the modules and attributes affected by the vulnerability...
For example, a vulnerability that affects PIL::ImageFont can be represented as...

root@kitploit:~

```
"imports": [
  {
    "attribute": "ImageFont",
    "modules": ["PIL"]
  }
]
```

which is equivalent to `PIL:ImageFont`. If a second attribute `ImageFont2` is also affected, then a second import entry needs to be added to the `imports` array.

root@kitploit:~

```
"imports": [
  { "attribute": "ImageFont", "modules": ["PIL"] },
  { "attribute": "ImageFont2", "modules": ["PIL"] }
]
```

Attributes which are accessible via multiple paths may be represented in a condensed form. Consider the attribute `django.db.models:JSONField` from the [django project](https://github.com/django/django/blob/0ee2b8c326d47387bacb713a3ab369fa9a7a22ee/django/db/models/__init__.py#L99).
The attribute `django.db.models:JSONField` is a re-export of `django.db.models.fields.json:JSONField` and both are valid paths.
These can be condensed to a more compact OSV representation as:

root@kitploit:~

```
{
  "attribute": "JSONField",
  "modules": ["django.db.models", "django.db.models.fields.json"]
}
```

### Tooling

This data is exposed by [`pip-audit`](https://github.com/pypa/pip-audit),
which provides a CLI for resolving Python dependencies in an environment
or project and identifying known vulnerabilities:

root@kitploit:~

```
python -m pip install pip-audit
python -m pip-audit -r requirements.txt
```

You can also use [`pypa/gh-action-pip-audit`](https://github.com/pypa/gh-action-pip-audit)
on GitHub Actions:

root@kitploit:~

```
jobs:
  pip-audit:
    steps:
      - uses: pypa/[email protected]
        with:
          inputs: requirements.txt
```

### APIs

Vulnerabilities are integrated into the
[Open Source Vulnerabilities](https://osv.dev) project, which provides an API to
query for vulnerabilities like so:

root@kitploit:~

```
$ curl -X POST -d \
          '{"version": "2.4.1", "package": {"name": "jinja2", "ecosystem": "PyPI"}}' \
          "https://api.osv.dev/v1/query"
```

This data has also been integrated into the
[PyPI JSON API](https://docs.pypi.org/api/json/#known-vulnerabilities).

## Code of Conduct

Everyone interacting with this project is expected to follow the
[PSF Code of Conduct](https://github.com/pypa/.github/blob/main/CODE_OF_CONDUCT.md).

[Download Tool](https://github.com/pypa/advisory-database)