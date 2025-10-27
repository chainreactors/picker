---
title: Search in Zola: Fuse.js vs. Elasticlunr.js
url: https://www.hahwul.com/dev/zola/search-in-zola/
source: HAHWUL
date: 2025-07-27
fetch_date: 2025-10-06T23:17:47.257160
---

# Search in Zola: Fuse.js vs. Elasticlunr.js

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/dev/zola/search-in-zola/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/dev/zola/search-in-zola/)

[한국어](https://www.hahwul.com/ko/dev/zola/search-in-zola/)

JULY 26, 2025

# Search in Zola: Fuse.js vs. Elasticlunr.js

Comparing Fuse.js and Elasticlunr.js for Zola’s client-side search. Learn which library suits your static site’s needs.

Zola is a fast and lightweight static site generator. To implement client-side search functionality without a server, you need a suitable JavaScript library. Zola supports generating index formats based on Fuse and Elasticlunr for search, making it easy to implement search features.

Both are lightweight and operate without dependencies, but they differ in Korean language support and ease of use. In this article, I'll discuss the features, performance, Korean support of these two libraries, and why I chose Fuse.js.

## What is Fuse.js and Elasticlunr.js?

To add search functionality in Zola, you need a client-side JavaScript library. Fuse.js and Elasticlunr.js are popular options, each strong in fuzzy search and full-text search, respectively.

| Library | Features | Pros/Cons |
| --- | --- | --- |
| Fuse.js | Library specialized in fuzzy search | Pros: Strong in handling typos or partial matches, simple setup for quick implementation Cons: Does not support complex search features |
| Elasticlunr.js | Supports full-text search | Pros: Provides advanced features like Boolean queries, TF/IDF ranking Cons: Requires additional setup for Korean search |

## Why Compare These Two?

Search functionality for blogs or documents should be simple yet support multiple languages well. Both libraries are appealing because they work without dependencies and can be easily integrated with Zola's Tera templates and JavaScript. However, for me, the key factors in choosing were Korean search performance, ease of setup, and how well it aligns with Zola's simple philosophy.

### Fuse.js: Simple and Powerful Fuzzy Search

* Features: Easily indexes arrays or object lists by specifying keys like `title`, `content`. Flexible query adjustments are possible with search threshold or weights.
* Korean Support: Naturally handles Korean fuzzy search without separate plugins. For example, searching for "한글" will find results like "한글 검색", "한글서치".
* Performance: Operates quickly and lightly on small to medium-sized datasets (hundreds to thousands of documents).

e.g.

```
const fuse = new Fuse(list, { keys: ['title', 'content'], threshold: 0.4 });
const results = fuse.search('한글');
```

### Elasticlunr.js: Advanced Search Option

* Features: Supports field-specific indexing, stop word customization, Boolean queries, TF/IDF ranking. Precise search is possible with field-specific boosting (e.g., `title:검색`).
* Korean Support: Default settings are English-centric, so Korean search performance is poor. You need to add the `lunr-languages` plugin for proper Korean tokenization.
* Performance: Fast even on large datasets, but limited by browser memory, and setup is relatively complex.

e.g.

```
const index = elasticlunr();
index.addField('title');
index.addDoc(doc);
const results = index.search('한글', { fields: { title: { boost: 2 } } });
```

## How to Integrate with Zola?

Zola allows easy configuration of search UI with Tera templates and JavaScript. Depending on the `config.toml` settings, a JSON format index file is generated during build, which can be loaded in JavaScript to add search functionality.

### Fuse

Set `index_format` to `fuse_javascript` or `fuse_json`, and during build, an index file in a format usable by Fuse.js, like `search_index.en.json`, will be generated.

```
# config.toml
[search]
index_format = "fuse_javascript" # or "fuse_json"
```

### Elasticlunr

Similarly, set it to `elasticlunr_javascript` or `elasticlunr_json` to generate an index file in Elasticlunr format.

```
# config.toml
[search]
index_format = "elasticlunr_javascript" # or "elasticlunr_json"
```

### My Case

I added more weight to `title` and included `body` and `tags` in the search targets as follows. You can adjust the `threshold` value to set search sensitivity.

```
var options = {
  keys: [
    { name: "title", weight: 2 },
    { name: "body", weight: 1 },
    { name: "tags", weight: 1 },
  ],
  includeScore: true,
  ignoreLocation: true,
  threshold: 0.4, // Adjust as needed for search sensitivity
};
var currentTerm = "";
var documents = Object.values(window.searchIndex.documentStore.docs);
var fuse = new Fuse(documents, options);

// https://github.com/hahwul/goyo/blob/main/static/goyo.js
```

## Why I Chose Fuse.js

Initially, since Zola didn't directly support Korean indexes, I was using Elasticlunr, which only worked for English searches. However, in May of this year (2025.05), the [PR](https://github.com/getzola/zola/pull/2881) I submitted was merged, officially enabling Korean index support, and it was included in a recent release.

This led me to reconsider search libraries, and ultimately, I leaned towards Fuse.js because it aligns well with Zola's simple philosophy. The fact that the Fuse.js community is much more active was also appealing. Additionally, while `lunr-language` supports Korean, integrating it with Elasticlunr.js requires a lot of effort, whereas Fuse.js can be used immediately without separate setup, making it convenient.

## Conclusion

If you're implementing search functionality in Zola, I recommend Fuse.js as a simple and fast solution. It's especially optimal for small to medium-sized sites, providing flexible fuzzy search for Korean without additional setup. Elasticlunr.js is useful where advanced search features are needed, but in most cases, I think Fuse offers better value for the investment.

Both libraries are excellent, but in my experience, Fuse.js fits better with Zola's conciseness. If you're running a blog or documentation page, I hope you'll compare various search features and create an even better search experience.

[#fuse.js](https://www.hahwul.com/tags/fuse-js/)
[#elasticlunr.js](https://www.hahwul.com/tags/elasticlunr-js/)
[#zola](https://www.hahwul.com/tags/zola/)

[ ]

[ ]

### Table of Contents

[What is Fuse.js and Elasticlunr.js?](https://www.hahwul.com/dev/zola/search-in-zola/#what-is-fuse-js-and-elasticlunr-js)

[Why Compare These Two?](https://www.hahwul.com/dev/zola/search-in-zola/#why-compare-these-two)

[Fuse.js: Simple and Powerful Fuzzy Search](https://www.hahwul.com/dev/zola/search-in-zola/#fuse-js-simple-and-powerful-fuzzy-search)
[Elasticlunr.js: Advanced Search Option](https://www.hahwul.com/dev/zola/search-in-zola/#elasticlunr-js-advanced-search-option)

[How to Integrate with Zola?](https://www.hahwul.com/dev/zola/search-in-zola/#how-to-integrate-with-zola)

[Fuse](https://www.hahwul.com/dev/zola/search-in-zola/#fuse)
[Elasticlunr](https://www.hahwul.com/dev/zola/search-in-zola/#elasticlunr)
[My Case](https://www.hahwul.com/dev/zola/search-in-zola/#my-case)

[Why I Chose Fuse.js](https://www.hahwul.com/dev/zola/search-in-zola/#why-i-chose-fuse-js)

[Conclusion](https://www.hahwul.com/dev/zola/search-in-zola/#conclusion)

[Next

Integrating Mermaid.js in Zola](https://www.hahwul.com/dev/zola/mermaid-in-zola/)

[Contact](/contact)
[Thanks](/thanks)
[Sitemap](/sitemap.xml)
Random
[Feeds](/feeds)

© 2025 HAHWUL
Developed and Designed by Me

* [WHO](/about/)
* [BLOG](/blog/)
* [SEC](/sec/)
* [DEV](/dev/)
* [PROJECTS](/projects/)

---

* Language
  + [ENGLISH](https://www.hahwul.com/dev/zola/search-in-zola/)
  + [한국어](https://www.hahwul.com/ko/dev/zola/search-in-zola/)