---
title: js-yaml-source-map
url: https://buaq.net/go-155147.html
source: unSafe.sh - 不安全
date: 2023-03-25
fetch_date: 2025-10-04T10:36:11.901780
---

# js-yaml-source-map

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

js-yaml-source-map

A library for finding YAML source locations after parsing by js-yaml.Installationnpm
*2023-3-24 22:11:0
Author: [github.com(查看原文)](/jump-155147.htm)
阅读量:31
收藏*

---

A library for finding YAML source locations after parsing by [js-yaml](https://github.com/nodeca/js-yaml).

## Installation

```
npm install js-yaml-source-map js-yaml
```

## Usage

```
---
# file: example.yaml
fruits:
  - apple
  - banana
  - orange
people:
  - name: Eric
    age: 26
  - name: Lily
    age: 22
states:
  CA: California
  NY: New York
    capital: Albany
  TX: Texas
```

```
import fs from "fs";
import yaml from "js-yaml";
import SourceMap from "js-yaml-source-map";

const data = fs.readFileSync("./example.yaml", "utf8");

const map = new SourceMap();
// pass map.listen() to the listener option
const loaded = yaml.load(data, { listener: map.listen() });

console.log(loaded); // { fruits: [ 'apple', 'banana', 'orange' ], ... }

// different syntaxes supported
console.log(map.lookup("fruits")); // { line: 4, column: 10, position: 42 }
console.log(map.lookup("people.0.age")); // { line: 9, column: 8, position: 95 }
console.log(map.lookup(".people[1].name")); // { line: 10, column: 9, position: 108}
console.log(map.lookup(["states", "NY", "capital"])); // { line: 16, column: 12, position: 188 }
```

If you're using CommonJS, you'll need to access the `default` key:

```
const SourceMap = require("js-yaml-source-map").default;

const map = new SourceMap();

//...
```

## API Reference

### `SourceMap`

**Constructor:** `new SourceMap()`

**Properties:**

* `SourceMap().map`: `PathMap`

**Methods:**

* `SourceMap().listen(): (event: "open" | "close", state: State) => void`
* `SourceMap().lookup(path: string | string[]): SourceLocation | undefined`

### Types

```
interface PathMap {
  [path: string]: {
    line: number;
    position: number;
    lineStart: number;
  };
}

interface SourceLocation {
  line: number;
  column: number;
  position: number;
}
```

## Limitations

* This library does not work with multi-document sources and `yaml.loadAll()`. Using it with `yaml.loadAll()` will result in undefined behavior.
* Using arrays or objects as keys will not work properly, and will result in undefined behavior.

文章来源: https://github.com/projectdiscovery/js-yaml-source-map
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)