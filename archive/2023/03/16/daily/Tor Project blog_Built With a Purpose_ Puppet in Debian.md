---
title: Built With a Purpose: Puppet in Debian
url: https://blog.torproject.org/built-with-purpose-puppet-debian/
source: Tor Project blog
date: 2023-03-16
fetch_date: 2025-10-04T09:47:56.655835
---

# Built With a Purpose: Puppet in Debian

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Built With a Purpose: Puppet in Debian

by [lavamind](/author/lavamind)
| March 15, 2023

![](/static/images/lead.png)

At the Tor Project, we're always on the lookout for opportunities to contribute
back to the communities around the platforms and tools we depend on to keep the
lights on. [Puppet](https://www.puppet.com/community/open-source) and [Debian](https://www.debian.org/) are two such projects, so we're happy to
announce that the upcoming Debian stable release, codename [bookworm](https://www.debian.org/releases/bookworm/), will
deliver an up-to-date suite of Puppet software thanks to the efforts of the Tor
Project!

A year ago, [TPA](https://gitlab.torproject.org/tpo/tpa/team) (AKA Tor Project sysadmin Team) started [planning an
upgrade](https://gitlab.torproject.org/tpo/tpa/team/-/issues/40662) of our fleet of nearly 100 Debian machines to the latest stable
release, `bullseye`. One item of concern was that not only were the Puppet
packages in Debian `bullseye` already nearly end-of-life (version 5.5), but the
PuppetDB package was also now [missing](https://tracker.debian.org/news/1115427/puppetdb-removed-from-testing/) entirely from the distribution. At
this point it seemed the only feasible option would be to migrate our entire
Puppet infrastructure to the [vendor-supplied packages](https://apt.puppet.com/).

## Advantages of distribution packages

So why not switch over to the [upstream Puppetlabs packages](https://www.puppet.com/docs/puppet/7/install_puppet.html#enable_the_puppet_platform_apt) and call it a
day? Essentially, because deploying software directly from vendors is not a
decision we take lightly, and because Puppet is such a core component of our
infrastructure, this called for careful consideration.

There are several reasons to prefer software shipped through distribution
packages.

### Improved security and reliability

Reports of [increasing numbers](https://drewdevault.com/2022/05/12/Supply-chain-when-will-we-learn.html) of [software supply-chain attacks](https://en.wikipedia.org/wiki/Supply_chain_attack) in
recent years have shed light on the difficult problem of shipping software
securely. Many popular solutions, like npm or PyPI suffer from vulnerabilities
which are not easily fixed, such as [typosquatting](https://blog.sonatype.com/ransomware-in-a-pypi-sonatype-spots-requests-typosquat) and [developper
sabotage](https://arstechnica.com/information-technology/2022/03/sabotage-code-added-to-popular-npm-package-wiped-files-in-russia-and-belarus/), at least not without breaking what makes them popular.

Puppetlabs doesn't rely on third-party package managers, and instead maintains
its own APT repository to ship packages to end-users. Although this is an
improvement, configuring an additional APT repository on a Debian-based system
effectively grants whoever controls the repository the ability to deploy
software and execute code with *maximum* privileges. This is a significant
potential attack surface.

We understand the challenge of [running an APT repository](https://support.torproject.org/apt/#apt_tor-deb-repo), and we trust in
the ability of the Debian project to maintain their own repositories reliably
and securely.

Even assuming the delivery channel is secure, concerns still remain about the
process used to build the binary packages. Not only does Puppetlabs employ a
somewhat exotic in-house build system, [EZBake](https://github.com/puppetlabs/ezbake), but we have no means to
evaluate the integrity of the build process itself.

On the other hand, Debian package are built from source (as opposed to
redistributing upstream binaries) on purpose-built infrastructure, and logs
generated during this process are made available for examination.

The Debian project, in collaboration with [reproducible-builds.org](https://reproducible-builds.org) even
provides automated reproducibility tests for packages and encourages maintainers
to fix issues hampering the ability for anyone to compile a given package and
obtain a byte-for-byte identical binary. Both the [puppet-agent](https://tests.reproducible-builds.org/debian/rb-pkg/bookworm/amd64/puppet-agent.html) and
[puppetserver](https://tests.reproducible-builds.org/debian/rb-pkg/bookworm/amd64/puppetserver.html) package we uploaded to Debian are currently reproducible.

### User-centric policies

Another concern is that the Puppetlabs packages ship with [analytics](https://github.com/puppetlabs/dropsonde),
enabled by default. Although an opt-out configuration parameter exists,
features like this are necessarily in conflict with users' right to privacy.

This is one area where Debian also shines: the project's [social contract](https://www.debian.org/social_contract)
guarantees the interests of users are always placed first and foremost. This
guides Debian the [established practice](https://lintian.debian.org/tags/privacy-breach-generic) of adressing privacy leaks in
package resources and runtime code.

As such, Debian's `puppetserver` package doesn't implement telemetry, and the
update check that "phones home" at regular intervals is disabled by default.

### Greater system integration

The Puppetlabs packages deploys its runtime libraries and code under the
`/opt/puppetlabs` directory. In addition to the Puppet applications, this
includes copies of the Ruby, JRuby and Clojure interpreters, as well as dozens
of third-party Clojure and Java libraries.

This duplication of code is a burden that is ultimately carried by system
administrators because they're the ones responsible for ensuring their
infrastructure is running code that is up to date and free from security
issues. Debian has a solid track record on this front, and we're confident that
security issues in, for example, the Ruby intrepreter, are adressed swiftly.

In addition, security updates to the Debian stable distribution are crafted in
a way that minimizes as much as possible the upgrade footprint. Puppetlabs
offers no such guarantees for their packages, so it's not unlikely that at some
point, addressing a security issue might require a disruptive upgrade.

# A sustained effort

Work on packaging new PuppetDB and Puppet Server [Clojure](https://clojure.org/) dependencies in
Debian had already progressed, [thanks to funding](https://veronneau.org/puppetserver-6-a-debian-packaging-post-mortem.html) from the [Wikimedia
Foundation](https://wikimediafoundation.org/). So it felt completing the work was within reach.

Thus, over the past 6 months, in addition to our regular TPA duties we have
been working to get Puppet in Debian ready for `bookworm`, the upcoming Debian
12 stable release. We started with the Puppet agent package, before moving on
to PuppetDB and finally Puppet Server, upgrading or adding dozens of dependency
packages along the way including many Clojure and Ruby libraries, [JRuby](https://www.jruby.org/) and
other Puppet components such as [Facter](https://github.com/puppetlabs/facter), [Hiera](https://github.com/puppetlabs/hiera) and [Trocla](https://github.com/duritong/trocla).

In collaboration with the [Debian Puppet Team](https://wiki.debian.org/Teams/Puppet), we worked to triage and fix
bugs reported in the Debian bug tracker, as well as implementing new or
improved build and integration tests for [Debian CI](https://ci.debian.net/). We also collaborated
with Puppetlabs to merge several patches upstream, including one patch to
[improve the reproducibility](https://github.com/puppetlabs/puppet/pull/8916) of Puppet agent builds.

## Looking ahead

With this work now behind us, we can look forward to [bringing our Puppet
infrastructure into a more modern age](https://gitlab.torproject.org/groups/tpo/tpa/-/milestones/8#tab-i...