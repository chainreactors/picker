---
title: Managing Agentic AI: Why the Control Plane Problem Is an AI Problem
url: https://www.guidepointsecurity.com/blog/managing_agentic_ai/
source: GuidePoint Security
date: 2026-09-29
fetch_date: 2026-09-30T07:42:10.027909
---

# Managing Agentic AI: Why the Control Plane Problem Is an AI Problem

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
	<title>Managing Agentic AI: Why the Control Plane Problem Is an AI Problem | GuidePoint Security</title>
<link data-rocket-preload as="style" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.34&#038;display=swap" rel="preload">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.34&#038;display=swap" media="print" onload="this.media=&#039;all&#039;" rel="stylesheet">
<noscript data-wpr-hosted-gf-parameters=""><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.34&#038;display=swap"></noscript>
	<meta name="description" content="AI agents aren’t waiting for updated policies and strategies. Often, they&#039;re operating without scoped identities, human sponsors, or governance. Fix that before it becomes an incident." />
	<link rel="canonical" href="https://www.guidepointsecurity.com/blog/managing_agentic_ai/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="Managing Agentic AI: Why the Control Plane Problem Is an AI Problem" />
	<meta property="og:description" content="AI agents aren’t waiting for updated policies and strategies. Often, they&#039;re operating without scoped identities, human sponsors, or governance. Fix that before it becomes an incident." />
	<meta property="og:url" content="https://www.guidepointsecurity.com/blog/managing_agentic_ai/" />
	<meta property="og:site_name" content="GuidePoint Security" />
	<meta property="article:publisher" content="https://www.facebook.com/GuidePointSec" />
	<meta property="article:published_time" content="2026-09-29T10:00:00+00:00" />
	<meta property="og:image" content="https://www.guidepointsecurity.com/wp-content/uploads/2018/03/AI-iStock-scaled.jpg" />
	<meta property="og:image:width" content="2560" />
	<meta property="og:image:height" content="1737" />
	<meta property="og:image:type" content="image/jpeg" />
	<meta name="author" content="Ingrid Kambe" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:creator" content="@GuidePointSec" />
	<meta name="twitter:site" content="@GuidePointSec" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https:\/\/schema.org","@graph":[{"@type":["Article","BlogPosting"],"@id":"https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/#article","isPartOf":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/"},"author":{"name":"Ingrid Kambe","@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/person\/f9f60eae51fb5592914a492df66a81c7"},"headline":"Managing Agentic AI: Why the Control Plane Problem Is an AI Problem","datePublished":"2026-09-29T10:00:00+00:00","mainEntityOfPage":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/"},"wordCount":1708,"publisher":{"@id":"https:\/\/www.guidepointsecurity.com\/#organization"},"image":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/#primaryimage"},"thumbnailUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2018\/03\/AI-iStock-scaled.jpg","keywords":["Agentic AI","AI","IAM","IDC","Identity and Access Management"],"articleSection":["AI Security","Blog","Identity &amp; Access Management"],"inLanguage":"en-US"},{"@type":"WebPage","@id":"https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/","url":"https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/","name":"Managing Agentic AI: Why the Control Plane Problem Is an AI Problem | GuidePoint Security","isPartOf":{"@id":"https:\/\/www.guidepointsecurity.com\/#website"},"primaryImageOfPage":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/#primaryimage"},"image":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/#primaryimage"},"thumbnailUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2018\/03\/AI-iStock-scaled.jpg","datePublished":"2026-09-29T10:00:00+00:00","description":"AI agents aren’t waiting for updated policies and strategies. Often, they're operating without scoped identities, human sponsors, or governance. Fix that before it becomes an incident.","breadcrumb":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/"]}]},{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/#primaryimage","url":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2018\/03\/AI-iStock-scaled.jpg","contentUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2018\/03\/AI-iStock-scaled.jpg","width":2560,"height":1737},{"@type":"BreadcrumbList","@id":"https:\/\/www.guidepointsecurity.com\/blog\/managing_agentic_ai\/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https:\/\/www.guidepointsecurity.com\/"},{"@type":"ListItem","position":2,"name":"The Guiding Point","item":"https:\/\/www.guidepointsecurity.com\/blog\/"},{"@type":"ListItem","position":3,"name":"Managing Agentic AI: Why the Control Plane Problem Is an AI Problem"}]},{"@type":"WebSite","@id":"https:\/\/www.guidepointsecurity.com\/#website","url":"https:\/\/www.guidepointsecurity.com\/","name":"GuidePoint Security","description":"Stronger Together. Protecting What&#039;s Next.","publisher":{"@id":"https:\/\/www.guidepointsecurity.com\/#organization"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https:\/\/www.guidepointsecurity.com\/?s={search_term_string}"},"query-input":{"@type":"PropertyValueSpecification","valueRequired":true,"valueName":"search_term_string"}}],"inLanguage":"en-US"},{"@type":"Organization","@id":"https:\/\/www.guidepointsecurity.com\/#organization","name":"GuidePoint Security, LLC.","url":"https:\/\/www.guidepointsecurity.com\/","logo":{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/logo\/image\/","url":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2021\/06\/cropped-GPS_MARK_RGB.png","contentUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2021\/06\/cropped-GPS_MARK_RGB.png","width":512,"height":512,"caption":"GuidePoint Security, LLC."},"image":{"@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/logo\/image\/"},"sameAs":["https:\/\/www.facebook.com\/GuidePointSec","https:\/\/x.com\/GuidePointSec","https:\/\/www.linkedin.com\/company\/guidepointsec"]},{"@type":"Person","@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/person\/f9f60eae51fb5592914a492df66a81c7","name":"Ingrid Kambe","image":{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2025\/05\/Ingrid_Kambe-150x150.jpeg","url":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2025\/05\/Ingrid_Kambe-150x150.jpeg","contentUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2025\/05\/Ingrid_Kambe-150x150.jpeg","caption":"Ingrid Kambe"},"description":"Ingrid helps bring cybersecurity services and products to market in a way that is meaningful to customers. Ingrid is a strategic ...