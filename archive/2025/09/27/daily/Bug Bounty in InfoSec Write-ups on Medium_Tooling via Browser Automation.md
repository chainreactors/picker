---
title: Tooling via Browser Automation
url: https://infosecwriteups.com/tooling-via-browser-automation-5336b17c5497?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-27
fetch_date: 2025-10-02T20:46:35.288272
---

# Tooling via Browser Automation

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5336b17c5497&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftooling-via-browser-automation-5336b17c5497&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ftooling-via-browser-automation-5336b17c5497&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5336b17c5497---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5336b17c5497---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Tooling via Browser Automation

[![Chetan Chinchulkar](https://miro.medium.com/v2/resize:fill:64:64/1*b3FG33fV4gKML4sEy1Zd7A.jpeg)](https://medium.com/%40omnipresent_?source=post_page---byline--5336b17c5497---------------------------------------)

[Chetan Chinchulkar](https://medium.com/%40omnipresent_?source=post_page---byline--5336b17c5497---------------------------------------)

5 min read

·

6 days ago

--

Listen

Share

I’m Chetan Chinchulkar (aka omnipresent), a passionate cybersecurity enthusiast and Software Development Engineer (SDE) by day, CTF addict by night! Currently ranked in the **top 1%** of TryHackMe ([check out my profile here](https://tryhackme.com/r/p/omnipresent)), I spend my free time diving into CTFs, hackthebox, solving cyber mysteries, and obsessively learning new ways to fix (and break) systems.

## Why Use Browser Automation?

When you automate the browser, you no longer have to manually break through the layers of encryption. Instead, you let the browser do the heavy lifting, just as it would for a legitimate user. The JavaScript running in the application performs all its logic client-side, including custom encryption and DOM manipulations.

By using browser automation tools, you interact with the application exactly as a real user would. This means that the browser does all the processing for you. Your automation can simply extract the final payloads or responses once they are rendered or transformed.

This makes browser automation tools incredibly useful for:

* Bypassing CAPTCHAs and client-side restrictions — Since you are simulating real interactions, many bot detection mechanisms become less effective. Certain browser automation tools even allow you to inject your browser context, which means the browser used by the automation software will have established trust to bypass bot detection mechanisms.
* Triggering multi-step workflows — Some exploits require interacting with the application across several screens or user actions. Browser automation allows you to chain these steps together fluidly.
* Lifting rendered or dynamically generated values — Often, the data or tokens you want only appear after JavaScript executes. Browser automation gives you direct access to the live DOM and rendered values.

In short, browser automation tools allow you to embrace the application’s logic rather than fight it. By navigating the app as a user would, you can bypass client-side controls, extract dynamic data, and build more resilient and realistic exploits.

we’ll use Selenium due to its ease of use, Python support, and broad browser compatibility. Selenium is a powerful browser automation tool often used for testing, web scraping, or even simulating user behaviour for penetration testing.

Before we analyse the script, let’s understand some essential concepts related to automating web interactions using Selenium:

* **WebDriver**: Selenium’s WebDriver controls the browser and allows us to navigate to pages, interact with elements, and extract data.
* **Element Identification**: Selenium provides various methods to locate and interact with elements using attributes like ID, Name, or XPath.
* **Headless Mode**: A way to run browsers without a graphical interface, making automation faster and more efficient.
* **CSRF Protection**: Web applications often use Cross-Site Request Forgery (CSRF) tokens to prevent malicious requests. With Selenium, since we are using a browser, the CSRF token is always dynamically generated and submitted with each request.
* **Stealth Techniques**: Selenium Stealth prevents detection by mimicking human behaviour and masking automated fingerprints.

The web application hosted at `http://SECOND_VM_IP/labs/lab1/` validates every login request using a CSRF token. The goal is to perform a brute-force attack using a Selenium-based script to determine the correct password.

Press enter or click to view image in full size

![]()

**Script Overview**

The provided Python script in the VNC VM uses Selenium to attempt login attempts using a wordlist of passwords. Below is the breakdown:

```
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
```

```
import time
import logging
from fake_useragent import UserAgent
```

* **Selenium WebDriver** controls the Chrome browser for automation.
* **selenium\_stealth** is used to prevent bot detection.
* **fake\_useragent** generates realistic browser fingerprints to avoid detection.

**Step 2 — Configuring the Browser**

The browser is configured using various Chrome options for optimal performance and stealth:

```
options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument(f'user-agent={userAgent}')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-cache')
options.add_argument('--disable-gpu')
```

* `--no-sandbox`: Prevents Chrome from using the sandbox mode, which is often necessary when running in Docker or as a root.
* `--headless`: Runs Chrome without a graphical user interface, making it faster and more efficient.
* `start-maximized`: Ensures the browser is fully maximised, preventing issues with responsive layouts.
* `f'user-agent={userAgent}'`: Generates a random browser user agent, helping the script evade detection.
* `--disable-dev-shm-usage`: Prevents memory limitations in Docker containers.
* `--disable-cache`: Ensures the browser fetches fresh data for each attempt.

**Step 3 — Implementing Stealth Techniques**

To prevent detection, the script uses `selenium-stealth`, which modifies browser behaviour to mimic a legitimate user:

```
stealth(chrome,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    rendere...