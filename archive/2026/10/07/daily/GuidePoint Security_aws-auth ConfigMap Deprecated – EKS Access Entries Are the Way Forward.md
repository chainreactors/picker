---
title: aws-auth ConfigMap Deprecated – EKS Access Entries Are the Way Forward
url: https://www.guidepointsecurity.com/blog/aws-auth-config-map-deprecated/
source: GuidePoint Security
date: 2026-10-07
fetch_date: 2026-10-08T08:07:51.792076
---

# aws-auth ConfigMap Deprecated – EKS Access Entries Are the Way Forward

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
	<title>aws-auth ConfigMap Deprecated: What EKS Teams Need Now</title>
<link data-rocket-preload as="style" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.34&#038;display=swap" rel="preload">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.34&#038;display=swap" media="print" onload="this.media=&#039;all&#039;" rel="stylesheet">
<noscript data-wpr-hosted-gf-parameters=""><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;700&#038;ver=2.1.34&#038;display=swap"></noscript>
	<meta name="description" content="AWS deprecated the aws-auth ConfigMap for EKS authentication. Learn how to migrate to Access Entries without recreating stale permissions in a new format." />
	<link rel="canonical" href="https://www.guidepointsecurity.com/blog/aws-auth-config-map-deprecated/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="aws-auth ConfigMap Deprecated - EKS Access Entries Are the Way Forward" />
	<meta property="og:description" content="AWS deprecated the aws-auth ConfigMap for EKS authentication. Learn how to migrate to Access Entries without recreating stale permissions in a new format." />
	<meta property="og:url" content="https://www.guidepointsecurity.com/blog/aws-auth-config-map-deprecated/" />
	<meta property="og:site_name" content="GuidePoint Security" />
	<meta property="article:publisher" content="https://www.facebook.com/GuidePointSec" />
	<meta property="article:published_time" content="2026-10-07T09:00:00+00:00" />
	<meta property="article:modified_time" content="2026-10-07T20:06:18+00:00" />
	<meta property="og:image" content="https://www.guidepointsecurity.com/wp-content/uploads/2023/11/iStock-1343499987_2000x675.jpg" />
	<meta property="og:image:width" content="1" />
	<meta property="og:image:height" content="1" />
	<meta property="og:image:type" content="image/jpeg" />
	<meta name="author" content="Keegan Justis" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:creator" content="@GuidePointSec" />
	<meta name="twitter:site" content="@GuidePointSec" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https:\/\/schema.org","@graph":[{"@type":["Article","BlogPosting"],"@id":"https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/#article","isPartOf":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/"},"author":{"name":"Keegan Justis","@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/person\/a87693898ff4d7dc02ead531d72bcef7"},"headline":"aws-auth ConfigMap Deprecated &#8211; EKS Access Entries Are the Way Forward","datePublished":"2026-10-07T09:00:00+00:00","dateModified":"2026-10-07T20:06:18+00:00","mainEntityOfPage":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/"},"wordCount":1996,"publisher":{"@id":"https:\/\/www.guidepointsecurity.com\/#organization"},"image":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/#primaryimage"},"thumbnailUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2023\/11\/iStock-1343499987_2000x675.jpg","articleSection":["Blog","Cloud Security"],"inLanguage":"en-US"},{"@type":"WebPage","@id":"https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/","url":"https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/","name":"aws-auth ConfigMap Deprecated: What EKS Teams Need Now","isPartOf":{"@id":"https:\/\/www.guidepointsecurity.com\/#website"},"primaryImageOfPage":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/#primaryimage"},"image":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/#primaryimage"},"thumbnailUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2023\/11\/iStock-1343499987_2000x675.jpg","datePublished":"2026-10-07T09:00:00+00:00","dateModified":"2026-10-07T20:06:18+00:00","description":"AWS deprecated the aws-auth ConfigMap for EKS authentication. Learn how to migrate to Access Entries without recreating stale permissions in a new format.","breadcrumb":{"@id":"https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/"]}]},{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/#primaryimage","url":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2023\/11\/iStock-1343499987_2000x675.jpg","contentUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2023\/11\/iStock-1343499987_2000x675.jpg"},{"@type":"BreadcrumbList","@id":"https:\/\/www.guidepointsecurity.com\/blog\/aws-auth-config-map-deprecated\/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https:\/\/www.guidepointsecurity.com\/"},{"@type":"ListItem","position":2,"name":"The Guiding Point","item":"https:\/\/www.guidepointsecurity.com\/blog\/"},{"@type":"ListItem","position":3,"name":"aws-auth ConfigMap Deprecated &#8211; EKS Access Entries Are the Way Forward"}]},{"@type":"WebSite","@id":"https:\/\/www.guidepointsecurity.com\/#website","url":"https:\/\/www.guidepointsecurity.com\/","name":"GuidePoint Security","description":"Stronger Together. Protecting What&#039;s Next.","publisher":{"@id":"https:\/\/www.guidepointsecurity.com\/#organization"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https:\/\/www.guidepointsecurity.com\/?s={search_term_string}"},"query-input":{"@type":"PropertyValueSpecification","valueRequired":true,"valueName":"search_term_string"}}],"inLanguage":"en-US"},{"@type":"Organization","@id":"https:\/\/www.guidepointsecurity.com\/#organization","name":"GuidePoint Security, LLC.","url":"https:\/\/www.guidepointsecurity.com\/","logo":{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/logo\/image\/","url":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2021\/06\/cropped-GPS_MARK_RGB.png","contentUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2021\/06\/cropped-GPS_MARK_RGB.png","width":512,"height":512,"caption":"GuidePoint Security, LLC."},"image":{"@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/logo\/image\/"},"sameAs":["https:\/\/www.facebook.com\/GuidePointSec","https:\/\/x.com\/GuidePointSec","https:\/\/www.linkedin.com\/company\/guidepointsec"]},{"@type":"Person","@id":"https:\/\/www.guidepointsecurity.com\/#\/schema\/person\/a87693898ff4d7dc02ead531d72bcef7","name":"Keegan Justis","image":{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2025\/07\/keegan-profile-150x150.jpg","url":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2025\/07\/keegan-profile-150x150.jpg","contentUrl":"https:\/\/www.guidepointsecurity.com\/wp-content\/uploads\/2025\/07\/keegan-profile-150x150.jpg","caption":"Keegan Justis"},"description":"Keegan Justis is a seasoned professional re...