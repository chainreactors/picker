---
title: Focal Router Orb - A 2 MB WordPress Implant With a Guessable Token and a Service Worker
url: https://lukeleal.com/research/posts/focal-router-orb-wordpress-implant/
source: Over Security
date: 2026-11-14
fetch_date: 2026-11-15T08:37:38.582667
---

# Focal Router Orb - A 2 MB WordPress Implant With a Guessable Token and a Service Worker

[# Cybersecurity Research 🚀](/research/posts/)

* Menu ▾
* + [Backdoors](https://lukeleal.com/research/tags/backdoor/)
  + [Phishing](https://lukeleal.com/research/tags/phishing/)
  + [Skimmers](https://lukeleal.com/research/tags/skimmer/)
  + [Past Research](https://blog.sucuri.net/author/luke)
  + [PGP Key](https://lukeleal.com/research/pages/pgp/)
  + [RSS](https://lukeleal.com/research/posts/index.xml)

* [Backdoors](https://lukeleal.com/research/tags/backdoor/)
* [Phishing](https://lukeleal.com/research/tags/phishing/)
* [Skimmers](https://lukeleal.com/research/tags/skimmer/)
* + ▾
  + - [Past Research](https://blog.sucuri.net/author/luke)
    - [PGP Key](https://lukeleal.com/research/pages/pgp/)
    - [RSS](https://lukeleal.com/research/posts/index.xml)

# [Focal Router Orb - A 2 MB WordPress Implant With a Guessable Token and a Service Worker](https://lukeleal.com/research/posts/focal-router-orb-wordpress-implant/)

2026-11-05Luke

#[Focal Router Orb](https://lukeleal.com/research/tags/focal-router-orb/)
#[service worker](https://lukeleal.com/research/tags/service-worker/)
#[EtherHiding](https://lukeleal.com/research/tags/etherhiding/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[implant](https://lukeleal.com/research/tags/implant/)
#[mu-plugin](https://lukeleal.com/research/tags/mu-plugin/)
#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![Focal Router Orb - A 2 MB WordPress Implant With a Guessable Token and a Service Worker](https://lukeleal.com/research/focal-router-orb-cover-q90.jpg "Cover Image")

## Table of Contents

* [The Disguise](#the-disguise)
* [Obfuscation and Padding](#obfuscation-and-padding)
* [A Control Endpoint With a Guessable Key](#a-control-endpoint-with-a-guessable-key)
* [The Hidden Administrator](#the-hidden-administrator)
* [Passwords, Cookies and the Implant’s Storage](#passwords-cookies-and-the-implants-storage)
* [Persistence and Spreading](#persistence-and-spreading)
* [The Browser Side: Visitors and a Service Worker](#the-browser-side-visitors-and-a-service-worker)
* [What This Build Can’t Do](#what-this-build-cant-do)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Samples](#samples)

The file is called `focal-orb_sample.php` and is **2,211,731 bytes**. The first lines look like any plugin from the WordPress directory: a name (*Focal Router Orb*), the description *“Intelligent widget rendering assistant”*, a GPL license line and a plugin URI that points at wordpress.org.

> Behind that header is a persistence framework of **341 functions**. It creates a hidden administrator, keeps every admin password it sees, forges 14 day login cookies, copies itself to other WordPress sites on the same server, and registers a service worker in the administrator’s browser.

Most of the 2.2 MB is padding. About 582 KB is code, and the other 1.6 MB is 407 comments of random hex.

I analysed it statically and never ran it. I folded the string concatenations with a script, read the result, and inflated the one embedded blob (the service worker) in Python. One thing to know before the details: **this build has its network layer removed.** The two HTTP helpers, `yq_http()` and `yq_http_get()`, return `false` with the reason `no_egress`, and the C2 resolver has no seeds. I can’t tell if the actor ships a no-egress variant or if the file was changed before it reached me. The sample is still fully functional as a **push-controlled** implant, and that is what this post covers.

## The Disguise[#](#the-disguise)

```
/**
 * Plugin Name:       Focal Router Orb
 * Plugin URI:        https://wordpress[.]org/plugins/focal-router-orb/
 * Description:       Intelligent widget rendering assistant
 * Version:           1.2.1
 * Author:            Leo Edwards
 * Author URI:        https://leoedwards[.]dev
 ...
 */
/* YQV:5.1.7 */
```

The header is complete (text domain, `Requires PHP`, `Tested up to: 6.5`), which makes it pass a quick look in the plugin list. I didn’t check whether the slug exists on wordpress.org or whether “Leo Edwards” is a real person or an invented persona, so I’m not attributing anything to the name.

The line that matters is the second one, `/* YQV:5.1.7 */`. It is an internal version marker, and the implant uses it as a gate: a pushed update is only accepted if its first 4 KB contain a marker of the form `/* XXV:n.n.n */` that is newer than the running one. It is also a very good thing to search for (see Detection).

Almost every function starts with `yq_`, with names like `yq_ep_serve`, `yq_ensure_admin`, `yq_spread` and `yq_drop_sw`. A few small helpers have short random names instead (`zupu` and `wevi` wrap `add_action` and `add_filter`, `gumi` makes random hex). The class at the top, `hopig`, is a decoy with one method that returns its argument.

## Obfuscation and Padding[#](#obfuscation-and-padding)

Strings are built from pieces, and function names are hidden behind concatenation, so that no sensitive name appears whole:

```
if (!("\x66\x75\x6ecti\x6fn" . "_exists")("\x79q_ep" . '_alp' . "ha")) {
```

That is `function_exists('yq_ep_alpha')`. Numbers are arithmetic too: `(2 | 8)` is 10, `(8 >> 3)` is 1. A string-folding pass makes the file readable, and nothing in it is encrypted. Only one real blob exists: 3,180 characters of base64 that inflate to the service worker.

**The padding is the interesting part.** `yq_pad()` appends random-hex comments of about 4 KB each until the file reaches 1.8 to 2.5 MB:

```
while (strlen($c) < $t - 4100) {
    $r = bin2hex(random_bytes(2000));
    $c .= "\n/*" . $r . '*/';
}
```

It only does this if the host has at least 150 MB of free disk and a PHP memory limit of 64 MB or more. Two effects follow. Every copy has a different hash, so a hash blocklist never matches twice. And many scanners and upload filters skip or truncate files of this size, which hides the code from them. `yq_unpad()` removes the comments again with `(\r?\n/\*[0-9a-f]{1000,}\*/)+$` when the implant needs to read its own source.

## A Control Endpoint With a Guessable Key[#](#a-control-endpoint-with-a-guessable-key)

Instead of calling out to a C2, the implant listens. Every request is checked by `yq_ep_match()`. A request is the operator’s if it carries a **token** either as a bare query-string key or in a header:

```
GET /?NEGdOssGqFDmB HTTP/1.1
X-SC-EP: NEGdOssGqFDmB            (alternative)
```

The token is not a secret. It is derived from today’s date and the site’s hostname:

```
function yq_ep_token($day, $host) {
    $b = hash('sha256', $day . $host, true);       // raw 32 bytes
    $n = (ord($b[0]) % 10) + 6;                    // 6 to 15 letters
    $o = '';
    for ($i = 0; $i < $n; $i++) $o .= $alphabet[ord($b[$i + 1]) % 52];   // a-zA-Z
    return $o;
}
```

`$day` is the UTC date as `Y-m-d`. The accepted window is **2 days** by default (today and yesterday, changeable up to 7 with `SC_EP_WINDOW`). The hosts are `HTTP_HOST`, `SERVER_NAME` and the hosts of `home_url()` and `site_url()`, each with and without `www.`. For `example.com` on `2026-11-05` the token is `NEGdOssGqFDmB` (and `JJOaJeADPJplux` for `www.example.com`). I ported this to Python and checked it against my own PHP implementation of the same algorithm.

The operator doesn’t need to know anything about the site except the hostname. That also means **anyone** who reads this algorithm can compute the same token and reach the endpoint, and can decrypt captured traffic, because the token is also the XOR key for requests and responses.

What the endpoint does:

* **`GET` or `HEAD`**: returns a JSON object with the implant version, PHP version, whether it is “waiting for an installer”, and an info block (server IP, domain, root path, active plugins, mu-plugins, login URL, recorded errors). The reply is XOR-encrypted with the token and has the headers `X-SC-V: 5.1.7`, `X-S...