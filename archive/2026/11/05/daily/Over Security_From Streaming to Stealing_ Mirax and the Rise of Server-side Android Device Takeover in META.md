---
title: From Streaming to Stealing: Mirax and the Rise of Server-side Android Device Takeover in META
url: https://www.group-ib.com/blog/mirax-android-device-takeover-rat/
source: Over Security
date: 2026-11-05
fetch_date: 2026-11-06T08:41:35.730741
---

# From Streaming to Stealing: Mirax and the Rise of Server-side Android Device Takeover in META

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
        <meta name="product" content="FP">
        <meta name="location" content="META">
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
	<title>From Streaming to Stealing: Mirax and the Rise of Server-side Android Device Takeover in META | Group-IB Blog</title>
	<meta name="description" content="Discover how the Mirax Android malware campaign uses streaming app lures, server-side C2, and Accessibility Service abuse for device takeover targeting financial institutions in the META region." />
	<link rel="canonical" href="https://www.group-ib.com/blog/mirax-android-device-takeover-rat/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="From Streaming to Stealing: Mirax and the Rise of Server-side Android Device Takeover in META" />
	<meta property="og:description" content="Discover how the Mirax Android malware campaign uses streaming app lures, server-side C2, and Accessibility Service abuse for device takeover targeting financial institutions in the META region." />
	<meta property="og:url" content="https://www.group-ib.com/blog/mirax-android-device-takeover-rat/" />
	<meta property="og:site_name" content="Group-IB" />
	<meta property="article:publisher" content="https://www.facebook.com/groupibHQ" />
	<meta property="article:modified_time" content="2026-11-05T07:30:14+00:00" />
	<meta property="og:image" content="https://www.group-ib.com/wp-content/uploads/facebook_-1200x630-2026-11-03t103837.711.png" />
	<meta property="og:image:width" content="1800" />
	<meta property="og:image:height" content="945" />
	<meta property="og:image:type" content="image/png" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:description" content="Discover how the Mirax Android malware campaign uses streaming app lures, server-side C2, and Accessibility Service abuse for device takeover targeting financial institutions in the META region." />
	<meta name="twitter:site" content="@GroupIB" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https:\/\/schema.org","@graph":[{"@type":"Article","@id":"https:\/\/www.group-ib.com\/blog\/mirax-android-device-takeover-rat\/#article","isPartOf":{"@id":"https:\/\/www.group-ib.com\/blog\/mirax-android-device-takeover-rat\/"},"author":[{"@type":"Person","name":"Daria Storozheva","url":"https:\/\/www.group-ib.com\/author\/daria-storozheva\/","jobTitle":"Fraud Analyst"},{"@type":"Person","name":"Andrei Loshchev","url":"https:\/\/www.group-ib.com\/author\/andrei-loshchev\/","jobTitle":"Team Lead, Fraud Consulting Analyst","sameAs":["https:\/\/www.linkedin.com\/in\/andreilosh\/"]},{"@type":"Person","name":"Bruno Bijelić","url":"https:\/\/www.group-ib.com\/author\/bruno-bijelic\/","jobTitle":"Reverse Engineer","sameAs":["https:\/\/www.linkedin.com\/in\/bruno-bijeli%C4%87-14476b20a\/"]}],"headline":"From Streaming to Stealing: Mirax and the Rise of Server-side Android Device Takeover in META","datePublished":"2026-11-05T07:18:04+00:00","dateModified":"2026-11-05T07:30:14+00:00","mainEntityOfPage":{"@id":"https:\/\/www.group-ib.com\/blog\/mirax-android-device-takeover-rat\/"},"wordCount":15,"publisher":{"@id":"https:\/\/www.group-ib.com\/#organization"},"inLanguage":"en-US","articleBody":""},{"@type":"WebPage","@id":"https:\/\/www.group-ib.com\/blog\/mirax-android-device-takeover-rat\/","url":"https:\/\/www.group-ib.com\/blog\/mirax-android-device-takeover-rat\/","name":"From Streaming to Stealing: Mirax and the Rise of Server-side Android Device Takeover in META | Group-IB Blog","isPartOf":{"@id":"https:\/\/www.group-ib.com\/#website"},"datePublished":"2026-11-05T07:18:04+00:00","dateModified":"2026-11-05T07:30:14+00:00","description":"Discover how the Mirax Android malware campaign uses streaming app lures, server-side C2, and Accessibility Service abuse for device takeover targeting financial institutions in the META region.","breadcrumb":{"@id":"https:\/\/www.group-ib.com\/blog\/mirax-android-device-takeover-rat\/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https:\/\/www.group-ib.com\/blog\/mirax-android-device-takeover-rat\/"]}],"author":[{"@type":"Person","name":"Daria Storozheva","url":"https:\/\/www.group-ib.com\/author\/daria-storozheva\/","jobTitle":"Fraud Analyst"},{"@type":"Person","name":"Andrei Loshchev","url":"https:\/\/www.group-ib.com\/author\/andrei-loshchev\/","jobTitle":"Team Lead, Fraud Consulting Analyst","sameAs":["https:\/\/www.linkedin.com\/in\/andreilosh\/"]},{"@type":"Person","name":"Bruno Bijelić","url":"https:\/\/www.group-ib.com\/author\/bruno-b...