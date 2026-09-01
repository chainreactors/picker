---
title: invisible_playwright v0.7.2
url: https://kitploit.com/en/posts/github-feder-cr-invisible_playwright-v072
source: Kitploit
date: 2026-08-31
fetch_date: 2026-09-01T06:59:38.407514
---

# invisible_playwright v0.7.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/7462/e23d5b9ad68fbaf1e80c3e7f70118a4e135514dc069f0b6d27076f6af3e23051.gif)

New releaseAug 31, 2026

# invisible\_playwright v0.7.2

Free antidetect browser stealth for Playwright: undetected headless Firefox fingerprint. Python scraping, recaptcha and bot detection bypass. Open source

Share

![invisible_playwright](https://raw.githubusercontent.com/feder-cr/invisible_playwright/main/docs/banner-light.png)

### Free antidetect browser stealth for Playwright: undetected Firefox fingerprint, headless or headed. Python web scraping and captcha bypass. Open source, and it passes every bot detection test.

![invisible_playwright - 5/5 detection suites passed](https://assets.kitploit.com/production/public/readmes/7462/e23d5b9ad68fbaf1e80c3e7f70118a4e135514dc069f0b6d27076f6af3e23051.gif)

## How it works

Anti-bots ask two questions, and reCAPTCHA, hCaptcha and Cloudflare Turnstile score the answers. invisible\_playwright answers yes to both.

**1. Is this a real browser?** Yes. It is Firefox, patched at the C++ source level.

* The browser fingerprint is set inside the engine, not injected into the page: navigator, screen, GPU/WebGL, canvas, fonts, audio, WebRTC, timezone, network. Headless or headed, the same values either way.
* No JS shim, no override, no seam to read.

**2. Is a real person using it?** Yes. The actions are humanized in the driver.

* Every click, hover and drag follows a natural mouse path with human timing, no teleporting cursor.
* Each input is byte-identical to a real mouse: real input source, pressure, trusted events.

Driven by the standard Playwright API. Full breakdown: [feder-cr/firefox\_antidetect\_patch](https://github.com/feder-cr/firefox_antidetect_patch).

---

## Still seeing captchas or anti-bot? It's the proxy.

Once the browser is handled it stops being the variable. If you are still getting challenged, the tell is no longer the browser, it is the IP you come from. Around 90% of proxies are public: anyone can rent the same address, so it is already known and sits on the blocked-IP lists sites check. A perfect browser on a known IP still loses.

---

## Install

root@kitploit:~

```
pip install invisible-playwright
python -m invisible_playwright fetch      # one-time ~238 MB download (~544 MB unpacked), sha256-verified
```

Supported platforms: **Windows x86\_64**, **Linux x86\_64 / arm64**. macOS is no longer supported (releases stopped at firefox-20); on a Mac the package refuses at launch with a clear message rather than downloading a binary that no longer exists.

---

## Usage

### Random fingerprint per session

**100% Playwright-compatible** - sync and async, all methods, zero API changes. If you already use Playwright, switching is two lines:

root@kitploit:~

```
- from playwright.sync_api import sync_playwright
- with sync_playwright() as p:
-     browser = p.firefox.launch()
+ from invisible_playwright import InvisiblePlaywright
+ with InvisiblePlaywright() as browser:
```

Every session gets a distinct fingerprint (GPU, audio, fonts, screen, ~200 fields) and Bezier-curve mouse motion.

**Sync**

root@kitploit:~

```
from invisible_playwright import InvisiblePlaywright

with InvisiblePlaywright(proxy={"server": "socks5://...", "username": "u", "password": "p"}) as browser:
    page = browser.new_page()
    page.goto("https://example.com")
    page.click("#submit")   # mouse arcs to the button on a Bezier curve
```

**Async**

root@kitploit:~

```
from invisible_playwright.async_api import InvisiblePlaywright

async with InvisiblePlaywright(proxy={"server": "socks5://...", "username": "u", "password": "p"}) as browser:
    page = await browser.new_page()
    await page.goto("https://example.com")
    await page.click("#submit")
```

The `browser` object is a `playwright.sync_api.Browser` / `playwright.async_api.Browser` - every Playwright method works as-is.

Log the seed to replay a run:

root@kitploit:~

```
sf = InvisiblePlaywright()
with sf as browser:
    print("seed =", sf.seed)
    # ...
```

### Reproducible fingerprint

root@kitploit:~

```
with InvisiblePlaywright(seed=42) as browser:
    ...   # same GPU, same canvas hash, same audio context, every run
```

### Proxies

root@kitploit:~

```
proxy = {
    "server": "socks5://gate.example.com:1080",
    "username": "user",
    "password": "pass",
}
with InvisiblePlaywright(proxy=proxy) as browser:
    ...
```

Schemes supported: `socks5`, `socks4`, `http`, `https`. DNS is routed through the proxy by default, no local leak.

### Timezone

The browser timezone follows `timezone=`:

root@kitploit:~

```
# default: timezone is auto-derived from the egress IP (proxy egress if a
# proxy is set, otherwise the host's own public IP)
with InvisiblePlaywright(proxy=proxy) as browser:
    ...

# explicit IANA zone always wins, the only way to force a specific zone
with InvisiblePlaywright(proxy=proxy, timezone="America/New_York") as browser:
    ...
```

### Pinning specific fingerprint fields

By default everything comes from `seed`. To force specific values while the rest stays seed-derived:

root@kitploit:~

```
with InvisiblePlaywright(
    seed=42,
    pin={
        "gpu.renderer": "ANGLE (NVIDIA, NVIDIA GeForce RTX 4090 Direct3D11)",
        "gpu.vendor":   "Google Inc. (NVIDIA)",
        "screen.width":  2560,
        "screen.height": 1440,
        "hardware.concurrency": 16,
    },
) as browser:
    ...
```

Full list of pinnable keys, how pinning interacts with the Bayesian sampler, and common patterns are in **[docs/pinning.md](https://github.com/feder-cr/invisible_playwright/blob/HEAD/docs/pinning.md)**.

---

## CLI

The installed command is `invisible-playwright`, with a hyphen. `python -m invisible_playwright` works identically and needs nothing on PATH.

root@kitploit:~

```
invisible-playwright fetch    # download the engine if missing, check every cached
                              # one against the seal, print the path
invisible-playwright version  # wrapper, core and engine versions, and where the
                              # engine is cached
```

## Documentation, guides and comparisons

All of it reads better, and is searchable, in
**[the wiki](https://github.com/feder-cr/invisible_playwright/wiki)**,
organised into four sections instead of one flat list:

* **[Documentation](https://github.com/feder-cr/invisible_playwright/blob/HEAD/docs/documentation.md)** -
  installation, the two-line switch from plain Playwright, proxy/timezone
  configuration, pinning specific fields, the CLI.
* **[Guides](https://github.com/feder-cr/invisible_playwright/blob/HEAD/docs/guides.md)** - how
  detection actually works, in seven groups: browser identity, canvas/WebGL/fonts/
  audio, network and WebRTC, the automation layer, AI agents, the detectors themselves
  explained from source, and testing.
* **[Comparisons](https://github.com/feder-cr/invisible_playwright/blob/HEAD/docs/comparisons.md)** -
  against Camoufox, Patchright, nodriver and playwright-stealth, and the case for
  Firefox over Chromium generally.
* **[Integrations](https://github.com/feder-cr/invisible_playwright/blob/HEAD/docs/integrations/)** -
  Scrapy, Crawlee, Robot Framework, CodeceptJS, test runners, Playwright MCP, and the
  frameworks it does not fit, by name.

If you don't know where to start: [Three ways to make Playwright undetected](https://github.com/feder-cr/invisible_playwright/blob/HEAD/docs/playwright-stealth-levels.md)
is the map most other pages link back to, [Playwright detected as a bot on one site](https://github.com/feder-cr/invisible_playwright/blob/HEAD/docs/playwri...