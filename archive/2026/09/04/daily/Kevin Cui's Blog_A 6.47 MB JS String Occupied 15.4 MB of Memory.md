---
title: A 6.47 MB JS String Occupied 15.4 MB of Memory
url: https://bugs.cc/posts/one-character-doubles-js-string-memory/
source: Kevin Cui's Blog
date: 2026-09-04
fetch_date: 2026-09-05T06:29:10.288364
---

# A 6.47 MB JS String Occupied 15.4 MB of Memory

[Skip to content](#main)[![](/_astro/avatar.DxjqQTYP_dapbY.webp)Kevin Cui's Blog](/)

* [Home](/)
* [Posts](/posts/)
* [Projects](/projects/)
* [Search](/search/)
* [RSS](/index.xml)
* [中文 (Chinese)](/zh/posts/one-character-doubles-js-string-memory/ "Switch language")

# A 6.47 MB JS String Occupied 15.4 MB of Memory

Posted on 2026-09-0415 min read[#javascript](/tags/javascript/)[#bun](/tags/bun/)[#cloudflare workers](/tags/cloudflare-workers/)

Table of contents

1. [The symptom](#the-symptom)
2. [Why two bytes](#why-two-bytes)
3. [The fix](#the-fix)
4. [Script source on Cloudflare Workers](#script-source-on-cloudflare-workers)
5. [How to check](#how-to-check)
6. [Closing](#closing)

[open-connector (opens in a new tab)](https://github.com/oomol-lab/open-connector) is an open-source project we work on. It wraps 1,464 third-party APIs (Slack, GitHub, Feishu, and others) behind a single action interface. Each third party is a provider. Which actions it has, and the JSON Schema for each action’s input and output, live in a JSON file. Those files are the catalog. The service loads them into memory at startup.

We were recently cutting resident memory on its Bun single-file binary, taking RSS after startup from 378 MiB down to 293 MiB ([open-connector#490 (opens in a new tab)](https://github.com/oomol-lab/open-connector/pull/490)). The heap’s largest single object turned out to be a JSON string: 6,471,221 characters, 6.47 MB as UTF-8, but 15.4 MB in JavaScriptCore’s heap. The reason was that 49 of those 6.47 million characters sit outside Latin-1.

I then looked at the Cloudflare Workers heap. Same cause: two characters made a 14.5 MB script occupy 27.6 MiB. Writing it down.

**Environment:**

* macOS arm64
* Bun 1.4.0 (JavaScriptCore)
* Node 26.7.0 (V8)
* esbuild 0.28.x, wrangler 4.127.1

## The symptom

At startup the service `JSON.stringify`s a summary of every provider in the catalog (name, description, the list of actions, no schemas) and caches that string as the `/api/providers` response body. Every later request sends it as-is. That string is `providerSummariesJson`, 6,471,221 characters.

While looking at memory I used `heapStats()` from `bun:jsc` to compare the heap before and after loading the catalog, then nulled this string on its own. That confirmed it accounted for 15.4 MB by itself.

The catalog can be loaded two ways. By default, every provider’s JSON Schema is read into memory at startup. It can also keep only names, descriptions, and action lists, and read a schema from its file the first time some action actually needs it. In that second mode the whole JS heap is 26.4 MiB, and this one string is more than half of it.

6.47 MB of text occupying 15.4 MB is roughly 2x. Scan the string for code points above U+00FF:

```
const tally = new Map();

for (const ch of text) {

if (ch.codePointAt(0) > 0xff) tally.set(ch, (tally.get(ch) ?? 0) + 1);

}
```

```
chars: 6471221, non-Latin-1 code points: 49

U+2014 "—" x13

U+2022 "•" x12

U+2192 "→" x3

U+8868 "表" x2

U+5E7F "广" x2

...
```

49 characters: 13 em dashes, 12 bullets, 3 arrows, and 21 CJK characters from a few providers whose descriptions are in Chinese. Those 49 come from 17 provider files. The other 1,447 files are pure ASCII. Those 49 characters made every character in the string occupy two bytes.

## Why two bytes

The ECMAScript spec says a string is a sequence of 16-bit code units. Engines do not actually store two bytes per character. V8 has `SeqOneByteString` and `SeqTwoByteString`. JavaScriptCore’s `StringImpl` has an `is8Bit()` 8-bit form and a 16-bit form. The rule is the same: if every character in the string is at most U+00FF, store one byte per character. If any character is above that, store the whole string two bytes per character. In V8’s source that ceiling is `kMaxOneByteCharCode = 0xFF`.

The ceiling is Latin-1, not ASCII. `é` (U+00E9) is not ASCII, but its code point is still at most U+00FF, so it stays one byte. What actually forces the whole string to two bytes is anything above U+00FF: an em dash (U+2014), a bullet (U+2022), an arrow (U+2192), CJK, emoji. Mix one CJK character into 6.47 million others and the whole string doubles.

A script to check. Eight million ASCII characters, then one `é` or one `中` on the end, and see how much the heap grows:

demo.mjs

```
import v8 from "node:v8";

function heap() {

globalThis.gc();

globalThis.gc();

return v8.getHeapStatistics().used_heap_size;

}

function build(extra) {

const s = "abcdefgh".repeat(1_000_000) + extra;

s.charCodeAt(s.length - 1); // flatten the rope, see below

return s;

}

const base = heap();

const ascii = build("");

const h1 = heap();

const latin = build("é");

const h2 = heap();

const cjk = build("中");

const h3 = heap();

console.log(`8,000,000 x ASCII        : heap +${((h1 - base) / 1048576).toFixed(1)} MiB`);

console.log(`same + one "é" (U+00E9)  : heap +${((h2 - h1) / 1048576).toFixed(1)} MiB`);

console.log(`same + one "中" (U+4E2D) : heap +${((h3 - h2) / 1048576).toFixed(1)} MiB`);

globalThis.keep = [ascii, latin, cjk];
```

```
$ node --expose-gc demo.mjs

8,000,000 x ASCII        : heap +7.6 MiB

same + one "é" (U+00E9)  : heap +7.6 MiB

same + one "中" (U+4E2D) : heap +15.3 MiB
```

Swap `heap()` for `Bun.gc(true)` plus `process.memoryUsage().heapUsed` and Bun 1.4.0 prints the same three numbers: 7.6, 7.6, 15.3. Both engines agree.

TextStatus: [✓] Blocking enabled
Gravity: [✗] Update overdue

[ ] Write every character above Latin-1 as \uXXXX

```
Status: [✓] Blocking enabled
Gravity: [✗] Update overdue
```

UTF-16 code units
:   56

UTF-8
:   60 B

Above Latin-1
:   2: ✓ U+2713, ✗ U+2717

Engine representation
:   2 bytes per unit (UTF-16)

Heap (payload only)
:   112 B = 56 × 2

```
Status: [\u2713] Blocking enabled
Gravity: [\u2717] Update overdue
```

UTF-16 code units
:   66

UTF-8
:   66 B

Above Latin-1
:   none

Engine representation
:   1 byte per unit (Latin-1)

Heap (payload only)
:   66 B = 66 × 1

Edit the text, or paste some JSON of your own.

Characters above Latin-1 are marked in red.

V8 can also print the type:

```
$ node --allow-natives-syntax -e '%DebugPrint("abc" + "é"); %DebugPrint("abc" + "中")'

DebugPrint: 0xd0faee56981: [String] in OldSpace: "abc\xe9"

- type: SEQ_ONE_BYTE_STRING_TYPE

DebugPrint: 0xd0faee56999: [String] in OldSpace: u"abc\u4e2d"

- type: SEQ_TWO_BYTE_STRING_TYPE
```

That `charCodeAt` in the script is required. `a + b` does not copy immediately in either engine. It builds a rope (V8 calls it `ConsString`, JSC calls it `JSRopeString`), and each half keeps its original representation. The eight million ASCII characters are still one-byte at that point. Index it, run a regexp, call `indexOf`, or write it as an HTTP response body, and the engine flattens the rope into a contiguous buffer. That is when the widest character decides the width of the whole thing. Without that line, all three numbers are 7.6.

`%DebugPrint` can show the rope itself:

```
$ node --allow-natives-syntax -e 'const s = "abcdefgh".repeat(4) + "中"; %DebugPrint(s)'

DebugPrint: 0x1be004ae841: [String]: uc"abcdefghabcdefghabcdefghabcdefgh\u4e2d"

- type: CONS_TWO_BYTE_STRING_TYPE
```

The `c` in the prefix means cons. The moment of concatenation, V8 already tags this rope as two-byte, because the right half is two-byte. The ASCII characters on the left still sit in their original one-byte buffer. The actual recopy at two bytes happens when the rope is flattened.

Both engines’ rules are in the source. V8’s `String` class comments restate the spec, then give the one-byte ceiling and the two sequential character types ([string.h (opens in a new tab)](https://github.com/v8/v8/blob/main/src/objects/string.h), [unicode.h (opens in a new tab)](https://github.com/v8/v8/blob/main/src/strings/unicode.h)):

v8/src/objects/string.hv8/src/strings/unicode.h

v8/src/objects/string.h

```
// The String abstract class captures JavaScript string values:

//

// Ecma-262:

//  4.3.16 St...