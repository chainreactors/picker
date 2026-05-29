---
title: Aggregating Semgrep Results: Top Rules, Files, and Clusters (MVP Demo)
url: https://armoredcode.com/blog/aggregating-semgrep-results-mvp-demo/
source: Over Security
date: 2026-05-28
fetch_date: 2026-05-29T06:06:09.193635
---

# Aggregating Semgrep Results: Top Rules, Files, and Clusters (MVP Demo)

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>Aggregating Semgrep Results: Top Rules, Files, and Clusters (MVP Demo) | Armored Code</title>

    <!-- IBM Plex -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Copse:wght@400;700&family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">

    <link
      rel="stylesheet"
      href="/assets/css/style.css"
    />
  </head>
  <body>
    <header class="site-header">
  <div class="container">
    <a href="/" class="brand">Armored Code</a>

    <nav class="site-nav">
      <a href="/blog/">Blog</a>
      <a
        href="https://mailchi.mp/a61f93445c94/armored-code-newsletter"
        target="_blank"
        rel="noopener noreferrer"
        >Newsletter</a
      >
    </nav>
  </div>
</header>

    <main class="content"><article class="post">
  <h1>Aggregating Semgrep Results: Top Rules, Files, and Clusters (MVP Demo)</h1>

  <p class="post-meta">January 2026</p>

  <div class="post-content"><h2 id="introduction">Introduction</h2>

<p>Turning security tool outputs into actionable insights is one of the biggest
challenges for developers and security engineers. In this post, I’m sharing a
minimal viable product (MVP) that takes Semgrep scan outputs and visualizes: top
rules, the most affected files, and clusters of related findings.</p>

<h2 id="watch-the-demo">Watch the Demo</h2>

<div class="video-container">

  <iframe src="https://www.youtube.com/embed/JEAuJIKdDjs?si=HvEMtSjh_zZxZ44e" frameborder="0" allowfullscreen=""></iframe>
</div>

<h2 id="how-the-mvp-works">How the MVP Works</h2>

<ol>
  <li><strong>Aggregates Semgrep Results</strong>: JSON outputs from multiple scans are
collected into a single dataset, ready for analysis.</li>
  <li><strong>Highlights Top Rules &amp; Top Files</strong>: Quickly identifies the rules triggered
most often and the files with the highest number of findings. This helps
prioritize what to fix first.</li>
  <li><strong>Clusters Related Findings</strong>: Findings are grouped into logical clusters to
reveal patterns and correlations between rules and code contexts.</li>
</ol>

<h2 id="why-this-matters">Why This Matters</h2>

<ul>
  <li>Provides a fast overview of large codebases.</li>
  <li>Reduces noise by focusing on the findings that matter most.</li>
  <li>Serves as the foundation for a Signal Engine: ingest → normalize → rank →
export/report.</li>
</ul>

<h2 id="next-steps">Next Steps</h2>

<p>This MVP is just the start. The ultimate goal is a full tool, I will call it
<em>Signal Engine</em>, that can:</p>

<ul>
  <li>Ingest results from multiple security tools</li>
  <li>Normalize and deduplicate findings</li>
  <li>Rank risks per finding</li>
  <li>Export actionable reports for developers and security engineers</li>
</ul>

<p>The demo shows a minimal but immediately usable implementation of this approach.</p>

<h2 id="try-it-yourself">Try it Yourself</h2>

<p>If you want to explore this workflow with your own Semgrep outputs, this MVP
provides a fast way to see patterns, prioritize rules, and focus on what really
matters in your code security scans.</p>

<p>The code is AGPLv3 licensed and released here:
<a href="https://github.com/thesp0nge/mvp_semgrep">https://github.com/thesp0nge/mvp_semgrep</a></p>
</div>
</article>
</main>

    <footer class="site-footer">
  <div class="container">
    <p>
      &copy; 2012 - 2026 Armored Code. All rights
      reserved.
    </p>
  </div>
</footer>

  </body>
</html>
