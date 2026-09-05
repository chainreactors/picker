---
title: Attacking and Defending SCOM: Management Server Relay and Obtaining Run As Credentials
url: https://www.guidepointsecurity.com/blog/attacking-and-defending-scom/
source: GuidePoint Security
date: 2026-09-04
fetch_date: 2026-09-05T06:29:01.190231
---

# Attacking and Defending SCOM: Management Server Relay and Obtaining Run As Credentials

<!DOCTYPE html>
<html lang="en-US">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />
<link rel="alternate" type="application/rss+xml" title="GuidePoint Security Feed" href="https://www.guidepointsecurity.com/feed/">

	<!-- This site is optimized with the Yoast SEO Premium plugin v28.2 (Yoast SEO v28.2) - https://yoast.com/product/yoast-seo-premium-wordpress/ -->
	<title>Attacking and Defending SCOM: Management Server Relay and Obtaining Run As Credentials</title>
<link data-rocket-preload as="style" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.29&#038;display=swap" rel="preload">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.29&#038;display=swap" media="print" onload="this.media=&#039;all&#039;" rel="stylesheet">
<noscript data-wpr-hosted-gf-parameters=""><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.29&#038;display=swap"></noscript>
	<meta name="description" content="Learn how attackers exploit SCOM so that you can preserve its operational capabilities without expanding your attack surface." />
	<link rel="canonical" href="https://www.guidepointsecurity.com/blog/attacking-and-defending-scom/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="Attacking and Defending SCOM: Management Server Relay and Obtaining Run As Credentials" />
	<meta property="og:description" content="Learn how attackers exploit SCOM so that you can preserve its operational capabilities without expanding your attack surface." />
	<meta property="og:url" content="https://www.guidepointsecurity.com/blog/attacking-and-defending-scom/" />
	<meta property="og:site_name" content="GuidePoint Security" />
	<meta property="article:publisher" content="https://www.facebook.com/GuidePointSec" />
	<meta property="article:published_time" content="2026-09-04T09:00:00+00:00" />
	<meta property="og:image" content="https://www.guidepointsecurity.com/wp-content/uploads/2026/03/BLOG_Image_8.png" />
	<meta property="og:image:width" content="2000" />
	<meta property="og:image:height" content="675" />
	<meta property="og:image:type" content="image/png" />
	<meta name="author" content="Ryan Voit" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:creator" content="@GuidePointSec" />
	<meta name="twitter:site" content="@GuidePointSec" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https:\/\/schema.org","@graph":[{"@type":["Article","BlogPosting"],"@id":"https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/#article","isPartOf":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/"},"author":{"name":"Ryan Voit","@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/person\/d978cb8a1649b224e274c29306eeb0c0"},"headline":"Attacking and Defending SCOM: Management Server Relay and Obtaining Run As Credentials","datePublished":"2026-09-04T09:00:00+00:00","mainEntityOfPage":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/"},"wordCount":3992,"publisher":{"@id":"https:\/\/www.guidepointsecurity.com\/#organization"},"image":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/#primaryimage"},"thumbnailUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2026\/03\/BLOG_Image_8.png","articleSection":["Blog","Threat &amp; Attack Simulation"],"inLanguage":"en-US"},{"@type":"WebPage","@id":"https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/","url":"https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/","name":"Attacking and Defending SCOM: Management Server Relay and Obtaining Run As Credentials","isPartOf":{"@id":"https:\/\/www.guidepointsecurity.com\/#website"},"primaryImageOfPage":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/#primaryimage"},"image":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/#primaryimage"},"thumbnailUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2026\/03\/BLOG_Image_8.png","datePublished":"2026-09-04T09:00:00+00:00","description":"Learn how attackers exploit SCOM so that you can preserve its operational capabilities without expanding your attack surface.","breadcrumb":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/"]}]},{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/#primaryimage","url":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2026\/03\/BLOG_Image_8.png","contentUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2026\/03\/BLOG_Image_8.png","width":2000,"height":675,"caption":"Identity Security in hybrid cloud environments requires AD and Entra ID"},{"@type":"BreadcrumbList","@id":"https:\/\/www.guidepointsecurity.com\/blog\/attacking-and-defending-scom\/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https:\/\/www.guidepointsecurity.com\/"},{"@type":"ListItem","position":2,"name":"The Guiding Point","item":"https:\/\/www.guidepointsecurity.com\/blog\/"},{"@type":"ListItem","position":3,"name":"Attacking and Defending SCOM: Management Server Relay and Obtaining Run As Credentials"}]},{"@type":"WebSite","@id":"https:\/\/www.guidepointsecurity.com\/#website","url":"https:\/\/www.guidepointsecurity.com\/","name":"GuidePoint Security","description":"","publisher":{"@id":"https:\/\/www.guidepointsecurity.com\/#organization"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https:\/\/www.guidepointsecurity.com\/?s={search_term_string}"},"query-input":{"@type":"PropertyValueSpecification","valueRequired":true,"valueName":"search_term_string"}}],"inLanguage":"en-US"},{"@type":"Organization","@id":"https:\/\/www.guidepointsecurity.com\/#organization","name":"GuidePoint Security, LLC.","url":"https:\/\/www.guidepointsecurity.com\/","logo":{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/logo\/image\/","url":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2021\/06\/cropped-GPS_MARK_RGB.png","contentUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2021\/06\/cropped-GPS_MARK_RGB.png","width":512,"height":512,"caption":"GuidePoint Security, LLC."},"image":{"@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/logo\/image\/"},"sameAs":["https:\/\/www.facebook.com\/GuidePointSec","https:\/\/x.com\/GuidePointSec","https:\/\/www.linkedin.com\/company\/guidepointsec"]},{"@type":"Person","@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/person\/d978cb8a1649b224e274c29306eeb0c0","name":"Ryan Voit","image":{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/secure.gravatar.com\/avatar\/b446079d28a750945e59e0f93461d288f9f5a275861927f90918a2e93e3030f9?s=96&d=mm&r=g","url":"https:\/\/secure.gravatar.com\/avatar\/b446079d28a750945e59e0f93461d288f9f5a275861927f90918a2e93e3030f9?s=96&d=mm&r=g","contentUrl":"https:\/\/secure.gravatar.com\/avatar\/b446079d28a750945e59e0f93461d288f9f5a275861927f90918a2e93e3030f9?s=96&d=mm&r=g","caption":"Ryan Voit"},"url":"https:\/\/www.guidepointsecurity.com\/blog\/author\/ryan-voitguidepointsecurity-com\/"}]}</script>
	<!-- / Yoast SEO Premium plugin. -->

<link rel='dns-prefetch' href=...