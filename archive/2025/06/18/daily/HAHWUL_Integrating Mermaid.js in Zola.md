---
title: Integrating Mermaid.js in Zola
url: https://www.hahwul.com/dev/zola/mermaid-in-zola/
source: HAHWUL
date: 2025-06-18
fetch_date: 2025-10-06T22:53:37.854362
---

# Integrating Mermaid.js in Zola

[ ]

[![HAHWUL Logo](/images/logo.png)](/)

[ ]

- [WHO](/about/)
- [BLOG](/blog/)
- [SEC](/sec/)
- [DEV](/dev/)
- [PROJECTS](/projects/)

* ENGLISH
* [한국어](https://www.hahwul.com/ko/dev/zola/mermaid-in-zola/)

`⌘``K`

[ENGLISH](https://www.hahwul.com/dev/zola/mermaid-in-zola/)

[한국어](https://www.hahwul.com/ko/dev/zola/mermaid-in-zola/)

JULY 06, 2025

# Integrating Mermaid.js in Zola

Applying and optimizing Mermaid.js in Zola, a Rust-based static site generator

[Mermaid.js](https://mermaid.js.org) is a powerful library that lets you create various diagrams using Markdown-like syntax. In this post, I'll walk you through the steps to integrate Mermaid.js into a Zola static site generator and how to optimize its performance.

```
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    Campaign A: [0.3, 0.6]
    Campaign B: [0.45, 0.23]
    Campaign C: [0.57, 0.69]
    Campaign D: [0.78, 0.34]
    Campaign E: [0.40, 0.34]
    Campaign F: [0.35, 0.78]
```

```
 quadrantChart
      title Reach and engagement of campaigns
      x-axis Low Reach --> High Reach
      y-axis Low Engagement --> High Engagement
      quadrant-1 We should expand
      quadrant-2 Need to promote
      quadrant-3 Re-evaluate
      quadrant-4 May be improved
      Campaign A: [0.3, 0.6]
      Campaign B: [0.45, 0.23]
      Campaign C: [0.57, 0.69]
      Campaign D: [0.78, 0.34]
      Campaign E: [0.40, 0.34]
      Campaign F: [0.35, 0.78]
```

## 1. Creating a Shortcode

The first step to using Mermaid.js in Zola is to create a shortcode. I created mermaid.html in the templates/shortcodes directory.

```
<pre class="mermaid">
 {{ body }}
</pre>
```

This shortcode is very simple; it just generates a `<pre>` tag with the mermaid class. However, Mermaid.js identifies this mermaid class to convert the content into a graph, making it incredibly easy to create diagrams.

You can use it like this code in markdown.

```
{% mermaid() %}
sequenceDiagram
    Alice->>+John: Hello John, how are you?
    Alice->>+John: John, can you hear me?
    John-->>-Alice: Hi Alice, I can hear you!
    John-->>-Alice: I feel great!
{% end %}
```

## 2. Adding the Mermaid.js Library

### CDN Approach (Initial Method)

Initially, I used a CDN to load Mermaid.js. I added the code to load mermaid.js in my overall layout, `base.html`:

```
<!-- mermaid -->
<script type="module">
   import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
   mermaid.initialize({ startOnLoad: true, theme: 'dark' });
</script>
```

This method was simple to implement but came with the downsides of external dependency and potential network latency.

### Internalizing with Local Files (Optimization)

To improve performance and remove external dependencies, I internalized Mermaid.js by saving it as a local file.

First, I found that .mjs files were difficult to handle as they often load multiple chunks. So, I opted to download the `.js` file instead.

```
curl -s https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js -o static/js/mermaid.min.js
```

Afterward, I loaded it in base.html by referencing the local path:

```
<!-- mermaid -->
<script src="/js/mermaid.min.js"></script>
<script>
  mermaid.initialize({ startOnLoad: false, theme: 'dark' });
</script>
```

## 3. Optimizing the Rendering Method

### startOnLoad Method (Initial Method)

Initially, I used Mermaid.js's default rendering method, `startOnLoad: true`.

```
mermaid.initialize({ startOnLoad: true, theme: 'dark' });
```

While this method automatically rendered all diagrams upon page load, it caused a delay in rendering because it waited for all other elements, like images, to fully load on the page.

### Manual Rendering Method (Optimization)

I realized it would be better to proceed immediately once the Mermaid code was fully loaded. So, I switched to manually specifying the rendering time. I set `startOnLoad: false` to prevent automatic rendering and then changed it to manually render only the necessary elements after the DOM was loaded.

```
mermaid.initialize({ startOnLoad: false, theme: 'dark' });
document.addEventListener('DOMContentLoaded', async () => {
  const mermaidElements = document.querySelectorAll('.mermaid');

  if (mermaidElements.length > 0) {
      await mermaid.run({
          nodes: mermaidElements
      });
  }
});
```

As a result, as soon as objects with the mermaid class are identified, rendering starts almost simultaneously with page access.

## Conclusion

Let's test with a simple example to see if it works well

```
 mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectiveness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid
```

It works perfectly!

[#mermaidjs](https://www.hahwul.com/tags/mermaidjs/)
[#zola](https://www.hahwul.com/tags/zola/)

[ ]

[ ]

### Table of Contents

[1. Creating a Shortcode](https://www.hahwul.com/dev/zola/mermaid-in-zola/#1-creating-a-shortcode)

[2. Adding the Mermaid.js Library](https://www.hahwul.com/dev/zola/mermaid-in-zola/#2-adding-the-mermaid-js-library)

[CDN Approach (Initial Method)](https://www.hahwul.com/dev/zola/mermaid-in-zola/#cdn-approach-initial-method)
[Internalizing with Local Files (Optimization)](https://www.hahwul.com/dev/zola/mermaid-in-zola/#internalizing-with-local-files-optimization)

[3. Optimizing the Rendering Method](https://www.hahwul.com/dev/zola/mermaid-in-zola/#3-optimizing-the-rendering-method)

[startOnLoad Method (Initial Method)](https://www.hahwul.com/dev/zola/mermaid-in-zola/#startonload-method-initial-method)
[Manual Rendering Method (Optimization)](https://www.hahwul.com/dev/zola/mermaid-in-zola/#manual-rendering-method-optimization)

[Conclusion](https://www.hahwul.com/dev/zola/mermaid-in-zola/#conclusion)

[Previous

Search in Zola: Fuse.js vs. Elasticlunr.js](https://www.hahwul.com/dev/zola/search-in-zola/)

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
  + [ENGLISH](https://www.hahwul.com/dev/zola/mermaid-in-zola/)
  + [한국어](https://www.hahwul.com/ko/dev/zola/mermaid-in-zola/)