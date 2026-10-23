---
title: Inside SiriusQT: A Seriously Skilled RAT
url: https://www.group-ib.com/blog/siriusqt-rat-hvnc-stealer/
source: Over Security
date: 2026-10-22
fetch_date: 2026-10-23T06:46:37.477069
---

# Inside SiriusQT: A Seriously Skilled RAT

<!DOCTYPE html>
<html lang="en-US">

<head><script>(function(w,i,g){w[g]=w[g]||[];if(typeof w[g].push=='function')w[g].push(i)})
(window,'GTM-PW7265','google_tags_first_party');</script><script>(function(w,d,s,l){w[l]=w[l]||[];(function(){w[l].push(arguments);})('set', 'developer_id.dY2E1Nz', true);
		var f=d.getElementsByTagName(s)[0],
		j=d.createElement(s);j.async=true;j.src='/gtm/';
		f.parentNode.insertBefore(j,f);
		})(window,document,'script','dataLayer');</script>

  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="content_type" content="Blog">
        <meta name="product" content="TI">
        <meta name="location" content="GLOBAL">
        <meta name="release_year" content="2026">
    <script>
    // Queues hbspt.forms.create() calls made before HubSpot's async-loaded
    // v2.js has finished loading, then replays them once it's ready
    // (v2.js's own onload="hubcache.letsgo()" call). Lets the forms.net
    // script load with `async` without breaking forms whose inline
    // hbspt.forms.create({...}) call would otherwise run before hbspt exists.
    window.hubcache = window.hubcache || {
      forms: [],
      letsgo: function () {
        while (hubcache.forms.length) {
          hbspt.forms.create(hubcache.forms.shift());
        }
      }
    };
    if (typeof window.hbspt === 'undefined') {
      window.hbspt = {
        forms: {
          create: function (c) { hubcache.forms.push(c); }
        }
      };
    }
  </script>
  <script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
      dataLayer.push(arguments);
    }
    gtag('consent', 'default', {
      analytics_storage: 'denied',
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied',
      wait_for_update: 500
    });
  </script>
    <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f); })(window,document,'script','dataLayer','GTM-PW7265');</script>
  <!-- End Google Tag Manager -->
    <script src="/wp-content/themes/gib-theme/assets/js/swiper-bundle.min.js"></script>
  <!-- OneTrust Cookies Consent Notice start for group-ib.com -->
  <script src="https://cdn-au.onetrust.com/scripttemplates/otSDKStub.js" type="text/javascript" charset="UTF-8" data-domain-script="0191785e-a497-722c-b405-6b94787f2b40"></script>
  <script>
    function OptanonWrapper() {
      var activeGroups = window.OnetrustActiveGroups || '';
      gtag('consent', 'update', {
        analytics_storage: activeGroups.includes('C0002') ? 'granted' : 'denied',
        ad_storage: activeGroups.includes('C0004') ? 'granted' : 'denied',
        ad_user_data: activeGroups.includes('C0004') ? 'granted' : 'denied',
        ad_personalization: activeGroups.includes('C0004') ? 'granted' : 'denied'
      });
    }
  </script>
  <!-- OneTrust Cookies Consent Notice end for group-ib.com -->

  <meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

	<!-- This site is optimized with the Yoast SEO Premium plugin v28.4 (Yoast SEO v28.4) - https://yoast.com/product/yoast-seo-premium-wordpress/ -->
	<title>Inside SiriusQT: A Seriously Skilled RAT | Group-IB Blog</title>
	<meta name="description" content="SiriusQT, a Windows RAT sold on underground forums since 2026, combines HVNC, credential theft and custom encrypted C2. Analysis of its server, client and licensing." />
	<link rel="canonical" href="https://www.group-ib.com/blog/siriusqt-rat-hvnc-stealer/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="Inside SiriusQT: A Seriously Skilled RAT" />
	<meta property="og:description" content="SiriusQT, a Windows RAT sold on underground forums since 2026, combines HVNC, credential theft and custom encrypted C2. Analysis of its server, client and licensing." />
	<meta property="og:url" content="https://www.group-ib.com/blog/siriusqt-rat-hvnc-stealer/" />
	<meta property="og:site_name" content="Group-IB" />
	<meta property="article:publisher" content="https://www.facebook.com/groupibHQ" />
	<meta property="article:modified_time" content="2026-10-22T07:19:36+00:00" />
	<meta property="og:image" content="https://www.group-ib.com/wp-content/uploads/facebook_-1200x630-2026-10-20t123748.675.png" />
	<meta property="og:image:width" content="1800" />
	<meta property="og:image:height" content="945" />
	<meta property="og:image:type" content="image/png" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:description" content="SiriusQT, a Windows RAT sold on underground forums since 2026, combines HVNC, credential theft and custom encrypted C2. Analysis of its server, client and licensing." />
	<meta name="twitter:site" content="@GroupIB" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https:\/\/schema.org","@graph":[{"@type":"Article","@id":"https:\/\/www.group-ib.com\/blog\/siriusqt-rat-hvnc-stealer\/#article","isPartOf":{"@id":"https:\/\/www.group-ib.com\/blog\/siriusqt-rat-hvnc-stealer\/"},"author":{"@type":"Person","name":"Riccardo Di Pietro","url":"https:\/\/www.group-ib.com\/author\/riccardo-di-pietro\/","jobTitle":"Senior Reverse Engineer"},"headline":"Inside SiriusQT: A Seriously Skilled RAT","datePublished":"2026-10-22T07:09:23+00:00","dateModified":"2026-10-22T07:19:36+00:00","mainEntityOfPage":{"@id":"https:\/\/www.group-ib.com\/blog\/siriusqt-rat-hvnc-stealer\/"},"wordCount":6,"publisher":{"@id":"https:\/\/www.group-ib.com\/#organization"},"inLanguage":"en-US","articleBody":""},{"@type":"WebPage","@id":"https:\/\/www.group-ib.com\/blog\/siriusqt-rat-hvnc-stealer\/","url":"https:\/\/www.group-ib.com\/blog\/siriusqt-rat-hvnc-stealer\/","name":"Inside SiriusQT: A Seriously Skilled RAT | Group-IB Blog","isPartOf":{"@id":"https:\/\/www.group-ib.com\/#website"},"datePublished":"2026-10-22T07:09:23+00:00","dateModified":"2026-10-22T07:19:36+00:00","description":"SiriusQT, a Windows RAT sold on underground forums since 2026, combines HVNC, credential theft and custom encrypted C2. Analysis of its server, client and licensing.","breadcrumb":{"@id":"https:\/\/www.group-ib.com\/blog\/siriusqt-rat-hvnc-stealer\/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https:\/\/www.group-ib.com\/blog\/siriusqt-rat-hvnc-stealer\/"]}],"author":{"@type":"Person","name":"Riccardo Di Pietro","url":"https:\/\/www.group-ib.com\/author\/riccardo-di-pietro\/","jobTitle":"Senior Reverse Engineer"}},{"@type":"BreadcrumbList","@id":"https:\/\/www.group-ib.com\/blog\/siriusqt-rat-hvnc-stealer\/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https:\/\/www.group-ib.com\/"},{"@type":"ListItem","position":2,"name":"Inside SiriusQT: A Seriously Skilled RAT"}]},{"@type":"WebSite","@id":"https:\/\/www.group-ib.com\/#website","url":"https:\/\/www.group-ib.com\/","name":"Group-IB Official Website","description":"","publisher":{"@id":"https:\/\/www.group-ib.com\/#organization"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https:\/\/www.group-ib.com\/?s={search_term_string}"},"query-input":{"@type":"PropertyValueSpecification","valueRequired":true,"valueName":"search_term_string"}}],"inLanguage":"en-US"},{"@type":"Organization","@id":"https:\/\/www.group-ib.com\/#organization","name":"Group-IB","url":"https:\/\/www.group-ib.com\/","logo":{"@type":"ImageObject","inLanguage":"en-US","@id":"https:\/\/www.group-ib.com\/#\/schema\/logo\/image\/","url":"https:\/\/www.group-ib.com\/wp-content\/uploads\/black-logo-5...