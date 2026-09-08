---
title: puppet-os-hardening
url: https://kitploit.com/en/tools/github/dev-sec/puppet-os-hardening
source: Kitploit
date: 2026-09-07
fetch_date: 2026-09-08T06:41:01.627379
---

# puppet-os-hardening

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

puppet-os-hardening — This puppet module provides numerous security-related configurations, providing all-round base protection. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/dev-sec/puppet-os-hardening

![](https://assets.kitploit.com/production/public/tools/54390/457593d9801fd7dd96f2c19d2c4ec1e4042450f24b33799f43f5dc1c7354878b-display-v1.webp)

[Cloud Infrastructure Security](/en/categories/cloud-infrastructure-security)[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Configuration Auditing](/en/categories/configuration-auditing)[Network Security](/en/categories/network-security)[DevSecOps](/en/categories/devsecops)[Authentication](/en/categories/authentication)

![GitHub](/providers/github.png)dev-sec/puppet-os-hardening

# puppet-os-hardening

This puppet module provides numerous security-related configurations, providing all-round base protection.

[View Repository](https://github.com/dev-sec/puppet-os-hardening)

291100391 month ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

[Website](http://dev-sec.io/)

Share

# Puppet OS hardening

[![Puppet Forge Version](https://img.shields.io/puppetforge/v/hardening/os_hardening.svg)](https://forge.puppet.com/hardening/os_hardening)
[![Puppet Forge Downloads](https://img.shields.io/puppetforge/dt/hardening/os_hardening.svg)](https://forge.puppet.com/hardening/os_hardening)
[![Puppet Forge Endorsement](https://img.shields.io/puppetforge/e/hardening/os_hardening.svg)](https://forge.puppet.com/hardening/os_hardening)
[![Build Status](https://github.com/dev-sec/puppet-os-hardening/workflows/tests/badge.svg)](https://github.com/dev-sec/puppet-os-hardening/workflows/tests)

#### Table of Contents

1. [Module Description - What the module does and why it is useful](#module-description)
2. [Setup - The basics of getting started with os\_hardening](#setup)
   * [Setup Requirements](#setup-requirements)
   * [Beginning with os\_hardening](#beginning-with-os_hardening)
3. [Usage - Configuration options and additional functionality](#usage)
   * [Important for Puppet Enterprise](#important-for-puppet-enterprise)
   * [Parameters](#parameters)
   * [Hiera usage](#hiera-usage)
   * [Note about wanted/unwanted packages and disabled services](#note-about-wantedunwanted-packages-and-disabled-services)

- [Limitations - OS compatibility, etc.](#limitations)

- [Development - Guide for contributing to the module](#development)

- [Testing - Quality gates for your changes in the code](#testing)
  * [Local Testing](#local-testing)
  * [PDK Tests](#pdk-tests)
  * [Integration Tests (Docker)](#integration-tests-docker)
  * [Integration Tests (DigitalOcean)](#integration-tests-digitalocean)
  * [CI testing of PRs & forks](#ci-testing-of-prs--forks)

- [Get in touch](#get-in-touch)

- [Contributors + Kudos](#contributors--kudos)

- [License and Author](#license-and-author)

## Module Description

This Puppet module provides secure configuration of your base OS with hardening and is part of the [DevSec Hardening Framework](https://dev-sec.io).

## Setup

### Setup Requirements

* Puppet OpenSource or Enterprise
* [Module stdlib](https://forge.puppet.com/puppetlabs/stdlib)
* [Module sysctl](https://forge.puppet.com/herculesteam/augeasproviders_sysctl)

### Beginning with os\_hardening

After adding this module, you can use the class:

root@kitploit:~

```
class { 'os_hardening': }
```

All parameters are contained within the main `os_hardening` class, so you just have to pass them like this:

root@kitploit:~

```
class { 'os_hardening':
  enable_ipv4_forwarding => true,
}
```

## Usage

### IMPORTANT for Puppet Enterprise

**If you are using this module in a PE environment, you have to set** `pe_environment = true`
Otherwise puppet will drop an error (duplicate resource)!

### Parameters

* `system_environment = 'default'`
  define the context in which the system runs. Some options don't work for `docker`/`lxc`
* `pe_environment = false`
  set this to true if you are using Puppet Enterprise **IMPORTANT - see above**
* `extra_user_paths = []`
  add additional paths to the user's `PATH` variable (default is empty).
* `umask = undef`
  umask used for the creation of new home directories by useradd / newusers (e.g. '027')
* `maildir = undef`
  path for maildir (e.g. '/var/mail')
* `usergroups = true`
  true if you want separate groups for each user, false otherwise
* `sys_uid_min = undef` and `sys_gid_min = undef`
  override the default setting for `login.defs`
* `password_max_age = 60`
  maximum password age
* `password_min_age = 7`
  minimum password age (before allowing any other password change)
* `password_warn_age = 7`
  Days warning before password change is due
* `login_retries = 5`
  the maximum number of login retries if password is bad (normally overridden by PAM / auth\_retries)
* `login_timeout = 60`
  authentication timeout in seconds, so login will exit if this time passes
* `chfn_restrict = ''`
  which fields may be changed by regular users using chfn
* `allow_login_without_home = false`
  true if to allow users without home to login
* `allow_change_user = false`
  if a user may use `su` to change his login
* `ignore_users = []`
  array of system user accounts that should *not be* hardened (password disabled and shell set to `/usr/sbin/nologin`)
* `folders_to_restrict = ['/usr/local/games','/usr/local/sbin','/usr/local/bin','/usr/bin','/usr/sbin','/sbin','/bin']`
  folders to make sure of that group and world do not have write access to it or any of the contents
* `ignore_max_files_warnings = false`
  true if you do not want puppet to log max\_files and performance warnings on the recursion of folders with > 1000 files eg /bin /usr/bin
* `recurselimit = 5`
  directory depth for recursive permission check
* `passwdqc_enabled = true`
  true if you want to use strong password checking in PAM using passwdqc
* `auth_retries = 5`
  the maximum number of authentication attempts, before the account is locked for some time
* `auth_lockout_time = 600`
  time in seconds that needs to pass, if the account was locked due to too many failed authentication attempts
* `passwdqc_options = 'min=disabled,disabled,16,12,8'`
  set to any option line (as a string) that you want to pass to passwdqc
* `manage_pam_unix = false`
  true if you want pam\_unix managed by this module
* `enable_pw_history = true`
  true if you want pam\_unix to remember password history to prevent reuse of passwords (requires `manage_pam_unix = true`)
* `pw_remember_last = 5`
  the number of last passwords (e.g. 5 will prevent user to reuse any of her last 5 passwords)
* `only_root_may_su = false`
  true when only root and member of the group wheel may use su, required to be true for CIS Benchmark compliance
* `root_ttys = ['console','tty1','tty2','tty3','tty4','tty5','tty6']`
  registered TTYs for root
* `whitelist = []`
  all files which should keep their SUID/SGID bits if set (will be combined with pre-defined whiteliste of files)
* `blacklist = []`
  all files which should have th...