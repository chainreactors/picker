---
title: How to find and download phishing kits - phish.report
url: https://phish.report/blog/harvesting-phishing-kits
source: Over Security - Cybersecurity news aggregator
date: 2024-11-16
fetch_date: 2025-10-06T19:20:04.720278
---

# How to find and download phishing kits - phish.report

[![Phish Report Logo](/static/logo-CVCRUOYQ.svg)](/)

How it works

[Phishing site analysis](/features/phishing-site-analysis)
[Rapid attack detection](/features/phishing-site-detection)

Resources

[Documentation](/docs)
[Blog](/blog)

[Pricing](/pricing)

[Log in](/user/login)

![Cover image](/static/phishkit-opendir-V4YVGLGX.png)

# How to find and download phishing kits

[![Bradley's author profile picture](/static/bradley-H5Z3ZQS2.jpg)](https://www.linkedin.com/in/bradleyjkemp/)
[Bradley Kemp](https://www.linkedin.com/in/bradleyjkemp/) on June 26, 2023

Phishing kits are generally sold on underground forums and can be tricky (at least ethically!) for defenders to acquire.
But when you're tackling a phishing campaign, having a copy of the threat actor's phishing kit is immensely useful.

With access to the phishing kit source code, you're no longer beholden to the hosting providers to take the site down, you can perform some countermeasures yourself.
Whether it's an unprotected log file (telling you exactly which of your users have been compromised), or the password for the admin panel (letting you take the site offline), there's often [vulnerabilities in these kits](/blog/top-phishing-kit-vulnerabilities) which are useful to defenders.

Luckily, through a combination of luck and threat actor incompetence, phishing kits can reliably be acquired from the phishing sites themselves.

## Techniques for finding phishing kits

There's two main ways to find phishing kits: be early, or be lucky.

### Get there before the kit is deployed

The first and most reliable way to acquire phishing kits is to grab them while the phishing site is being set up.

Phishing kits are overwhelmingly distributed as ZIP files and deployed to a webserver like this:

1. `kit.zip` is uploaded to the webserver (often using a web UI like [cPanel's File Manager](https://docs.cpanel.net/cpanel/files/file-manager/#working-with-files-and-folders))
2. The phishing kit files are extracted
3. Any setup or installation steps are completed (only for more advanced phishing sites)
4. `kit.zip` is deleted. The phishing site is now fully active.

To download the phishing kit, you'll need to strike in the short window between the kit being uploaded and it being deleted again.
This is usually only a matter of minutes!

But actually, downloading the kit is often the easy part.
The tricky part is finding a phishing domain before it's been set up.

> *Why don't phishers extract the kit before uploading?*
>
> Partly tradition (phishers are generally very low skilled so these sorts of habits proliferate), but also technical limitations.
> Luckily for us, cPanel (one of the most common web hosting control panels) only supports uploading single files, not folders!

#### Finding a phishing site before it's active

Essentially the only way to find a phishing domain before it's been set up is using Certificate Transparency logs.
These contain every HTTPS certificate issued (which, importantly, contain the domains they're valid for) and are far more real-time than other sources like newly-registered domain feeds (which are only updated daily).

Many hosting providers automatically issue an HTTPS certificate for you when creating a website so there's good chance phishing domains end up in these logs before the phisher has had time to finish setting them up.

Wading through the millions of certificates is a challenge, but our guide on [how to detect phishing websites in real-time using open source](/blog/phishing-catcher) is a good introduction.

You'll know you've got a good candidate when you see a default directory listing page like this:

![A future phishing site with directory listing enabled](/static/phishkit-opendir-V4YVGLGX.png)

A future phishing site with directory listing enabled

#### Waiting for the kit to be uploaded

Once you've found a future phishing site, you just need to keep checking it, waiting for that ZIP file to be uploaded.

Rather than sitting manually refreshing the page, you can use a basic script like this:

```
$ watch -g `# Run repeatedly until the output changes` \
  curl --silent phishing-domain.com; `# Fetch the phishing domain and print out the HTML`
  echo -ne '\007' # beep! Alert the user that the contents have changed
```

Once the contents of the directory listing changes, you need to act fast to download the kit (or ideally have your script do this automatically too).

### Guess the filename

While phishers are supposed to delete the phishing kit ZIP file after setting up the site, many forget to do so.
This gives us another opportunity for retrieving kits.

#### Easy mode: directory traversal

Sometimes phishing pages aren't hosted at the root of a domain, but at a sub-path like `account-login.com/brandName/secure`.

While we can't see a list of files within the `brandName/secure` folder, there's a good chance directory listing is still enabled in the parent folders.
So you should try fetching:

* `account-login.com/brandName/` (directory listing may be enabled)
* `account-login.com/brandName/secure.zip` (a ZIP file of this name would extract to a folder named `secure/`)
* `account-login.com/` (directory listing may be enabled)
* `account-login.com/brandName.zip` (a ZIP file of this name would extract to a folder named `brandName/`)

Similarly, if a phishing site is hosted on a subdomain like `secure.brandName.account-login.com`, you should try repeatedly removing the subdomain.

If any of these URLs are a ZIP file, or contain a link to one, you've probably found the kit!

#### Hard mode: guessing the filename

Even if directory traversal isn't an option, you can sometimes still get a copy of the kit.

Although you can't see the list of files on the phishing site, the phishing kit might still be there.
If you can guess the filename, the webserver will happily give you the contents.

This is very hard to pull off, but here are some filenames to try:

* Simply `brandName.zip`. Most phishers include their name/handle in the kit filename so this is unlikely to work, but not impossible!
* A filename you've seen before in a directory listing, but not managed to download in time before it was deleted.
* Variations on previous kit filenames. For example, some more advanced phishing kits have version numbers in the name: increment the version number and you might find the latest release!

### See if someone else has already collected it

While you might be the only ones specifically on the hunt for phishing kits targeting your users, there are multiple projects out there attempting to collect as many kits as possible.
If you're lucky, they may already have a copy of phishing kits you're interested in.

Some places to try are:

* [github.com/0xDanielLopez/phishing\_kits](https://github.com/0xDanielLopez/phishing_kits)
* [github.com/marcoramilli/PhishingKitTracker](https://github.com/marcoramilli/PhishingKitTracker)
* [urlscan.io submissions tagged `phishkit`](https://urlscan.io/search/#task.tags:%22phishkit%22) (though this requires a subscription to download the files)

## Tools for finding phishing kits

The techniques for finding phishing kits aren't themselves difficult, but can become tricky when applying them to a large number of domains.
Rather than implementing these scripts yourself, there's a few pre-built options.

### Phish Report

Phish Report runs through the techniques described here on every site we analyse (whether that's URLs users submit manually or URLs which trigger our automated detections).

On top of phishing kit collection, we also offer [reverse engineering and analysis of phishing kits](/blog/top-phishing-kit-vulnerabilities) where we produce:

* High fidelity detection rule(s) to detect all parts of the phishing site infrastructure.
* A vulnerability assessment of the kit source code (where available) including options to directly disrupt the site.

### StalkPhish

[StalkPhish](https://github.com/t4d/StalkPhish) is a tool which fetches databases...