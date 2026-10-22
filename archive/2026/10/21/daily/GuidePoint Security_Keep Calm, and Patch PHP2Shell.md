---
title: Keep Calm, and Patch PHP2Shell
url: https://www.guidepointsecurity.com/blog/how-to-patch-php2shell/
source: GuidePoint Security
date: 2026-10-21
fetch_date: 2026-10-22T06:45:18.970218
---

# Keep Calm, and Patch PHP2Shell

<!DOCTYPE html>
<html lang="en-US">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />
<link rel="alternate" type="application/rss+xml" title="GuidePoint Security Feed" href="https://www.guidepointsecurity.com/feed/">

	<!-- This site is optimized with the Yoast SEO Premium plugin v28.5 (Yoast SEO v28.5) - https://yoast.com/product/yoast-seo-premium-wordpress/ -->
	<title>How to Patch PHP2Shell: CVE-2026-109618 &amp; CVE-2026-109619</title>
<link data-rocket-prefetch href="https://fonts.googleapis.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://d10lpsik1i8c69.cloudfront.net" rel="dns-prefetch">
<link data-rocket-prefetch href="https://static.oktopost.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://bat.bing.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://script.crazyegg.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://static.ads-twitter.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://snap.licdn.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://www.googletagmanager.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://lltrck.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://www.gstatic.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://truyoproductionuscdn.truyo.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://cdn.bizible.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://a.omappapi.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://munchkin.marketo.net" rel="dns-prefetch">
<link data-rocket-prefetch href="https://acsbapp.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://go.guidepointsecurity.com" rel="dns-prefetch">
<link data-rocket-prefetch href="https://okt.to" rel="dns-prefetch">
<link data-rocket-prefetch href="https://www.google.com" rel="dns-prefetch">
<link data-rocket-preload as="style" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.34&#038;display=swap" rel="preload">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.34&#038;display=swap" media="print" onload="this.media=&#039;all&#039;" rel="stylesheet">
<noscript data-wpr-hosted-gf-parameters=""><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.34&#038;display=swap"></noscript><link rel="preload" data-rocket-preload as="image" href="https://www.guidepointsecurity.com/wp-content/uploads/2024/09/AdobeStock_493881519_2000x675.jpg" fetchpriority="high">
	<meta name="description" content="PHP2Shell (CVE-2026-109618; CVE-2026-109619) enables unauthenticated RCE on PHP servers. Get patching steps, mitigations, and threat hunting guidance." />
	<link rel="canonical" href="https://www.guidepointsecurity.com/blog/how-to-patch-php2shell/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="Keep Calm, and Patch PHP2Shell" />
	<meta property="og:description" content="PHP2Shell (CVE-2026-109618; CVE-2026-109619) enables unauthenticated RCE on PHP servers. Get patching steps, mitigations, and threat hunting guidance." />
	<meta property="og:url" content="https://www.guidepointsecurity.com/blog/how-to-patch-php2shell/" />
	<meta property="og:site_name" content="GuidePoint Security" />
	<meta property="article:publisher" content="https://www.facebook.com/GuidePointSec" />
	<meta property="article:published_time" content="2026-10-21T19:54:28+00:00" />
	<meta property="article:modified_time" content="2026-10-21T20:34:07+00:00" />
	<meta property="og:image" content="https://www.guidepointsecurity.com/wp-content/uploads/2025/10/GRIT_HeaderImage.png" />
	<meta property="og:image:width" content="1600" />
	<meta property="og:image:height" content="400" />
	<meta property="og:image:type" content="image/png" />
	<meta name="author" content="Justin Timothy" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:creator" content="@GuidePointSec" />
	<meta name="twitter:site" content="@GuidePointSec" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https:\/\/schema.org","@graph":[{"@type":["Article","BlogPosting"],"@id":"https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/#article","isPartOf":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/"},"author":{"name":"Justin Timothy","@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/person\/509b017a0d86aa457f6b33198ea2e95c"},"headline":"Keep Calm, and Patch PHP2Shell","datePublished":"2026-10-21T19:54:28+00:00","dateModified":"2026-10-21T20:34:07+00:00","mainEntityOfPage":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/"},"wordCount":2558,"publisher":{"@id":"https:\/\/www.guidepointsecurity.com\/#organization"},"image":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/#primaryimage"},"thumbnailUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2025\/10\/GRIT_HeaderImage.png","articleSection":["GRIT® Blog","Incident Response &amp; Threat Intelligence","Vulnerability Management &amp; Penetration Testing"],"inLanguage":"en-US"},{"@type":"WebPage","@id":"https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/","url":"https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/","name":"How to Patch PHP2Shell: CVE-2026-109618 & CVE-2026-109619","isPartOf":{"@id":"https:\/\/www.guidepointsecurity.com\/#website"},"primaryImageOfPage":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/#primaryimage"},"image":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/#primaryimage"},"thumbnailUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2025\/10\/GRIT_HeaderImage.png","datePublished":"2026-10-21T19:54:28+00:00","dateModified":"2026-10-21T20:34:07+00:00","description":"PHP2Shell (CVE-2026-109618; CVE-2026-109619) enables unauthenticated RCE on PHP servers. Get patching steps, mitigations, and threat hunting guidance.","breadcrumb":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/"]}]},{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/#primaryimage","url":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2025\/10\/GRIT_HeaderImage.png","contentUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2025\/10\/GRIT_HeaderImage.png","width":1600,"height":400},{"@type":"BreadcrumbList","@id":"https:\/\/www.guidepointsecurity.com\/blog\/how-to-patch-php2shell\/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https:\/\/www.guidepointsecurity.com\/"},{"@type":"ListItem","position":2,"name":"The Guiding Point","item":"https:\/\/www.guidepointsecurity.com\/blog\/"},{"@type":"ListItem","position":3,"name":"Keep Calm, and Patch PHP2Shell"}]},{"@type":"WebSite","@id":"https:\/\/www.guidepointsecurity.com\/#website","url":"https:\/\/www.guidepointsecurity.com\/","name":"GuidePoint Security","description":"Stronger Together. Protecting What&#039;s Next.","publisher":{"@id":"https:\/\/www.guidepointsecurity.com\/#organization"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https:\/\/www.guidepointsecurity.com\/?s={search_term_string}"},"query-input":{"@type":"PropertyValueSpecification","valueRe...