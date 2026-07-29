---
title: How an Unpatched N-Day Let Any Anonymous Visitor Rewrite WooCommerce Prices in ND Booking
url: https://infosecwriteups.com/how-an-unpatched-n-day-let-any-anonymous-visitor-rewrite-woocommerce-prices-in-nd-booking-65c69c9a32ef?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-28
fetch_date: 2026-07-29T05:02:49.372182
---

# How an Unpatched N-Day Let Any Anonymous Visitor Rewrite WooCommerce Prices in ND Booking

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-an-unpatched-n-day-let-any-anonymous-visitor-rewrite-woocommerce-prices-in-nd-booking-65c69c9a32ef&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-an-unpatched-n-day-let-any-anonymous-visitor-rewrite-woocommerce-prices-in-nd-booking-65c69c9a32ef&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-65c69c9a32ef---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-65c69c9a32ef---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Press enter or click to view image in full size

![]()

# How an Unpatched N-Day Let Any Anonymous Visitor Rewrite WooCommerce Prices in ND Booking

## Author: [Shikhali Jamalzade](https://medium.com/u/20557ba7487d?source=post_page---user_mention--65c69c9a32ef---------------------------------------) GitHub: [alisalive](https://github.com/alisalive) LinkedIn: [camalzads](https://www.linkedin.com/in/camalzads/) Type: Independent Security Research | WordPress Plugin CVE Research

[![Shikhali Jamalzade](https://miro.medium.com/v2/resize:fill:64:64/1*1y98p7kVR06Fq8997mI2FQ.png)](https://alisalive.medium.com/?source=post_page---byline--65c69c9a32ef---------------------------------------)

[Shikhali Jamalzade](https://alisalive.medium.com/?source=post_page---byline--65c69c9a32ef---------------------------------------)

11 min read

·

2 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D65c69c9a32ef&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-an-unpatched-n-day-let-any-anonymous-visitor-rewrite-woocommerce-prices-in-nd-booking-65c69c9a32ef&source=---header_actions--65c69c9a32ef---------------------post_audio_button------------------)

Share

This is a write-up of a vulnerability I independently discovered in ND Booking, a WordPress hotel/room booking plugin by Nicdark with WooCommerce integration. The vulnerability allows any unauthenticated visitor to permanently overwrite the price of any WooCommerce product linked to a bookable room, with no login, no capability check, and no ownership validation. I built and verified a full working proof-of-concept before submitting it — only to find out during the submission process that the exact same root cause had already been assigned CVE-2025–63001. The catch: that advisory lists the plugin as vulnerable only “up to and including version 3.8.” I tested this against version 7.0.1, the current release on WordPress.org, and it is still fully exploitable. This write-up documents the full process — discovery, exploitation, and what happened when a “new” finding turned out to be an old, never-actually-patched CVE — because the technical detail is still useful to anyone auditing booking/e-commerce plugins, even though I don’t get credit for a fresh CVE here.

Background: Why ND Booking

My WordPress plugin research methodology targets a curated list of plugins across several categories — booking/reservation, access-control, form builders, membership systems — chosen because they tend to implement their own authentication and state-changing logic on top of WordPress, rather than relying purely on WordPress core’s built-in mechanisms. Plugins that integrate with WooCommerce are a particular focus for me, because they combine two attack surfaces: the plugin’s own AJAX/REST layer, and WooCommerce’s product/pricing data model.

ND Booking caught my attention for a simple reason: it registers a WooCommerce-integration AJAX action directly, rather than routing bookings through WooCommerce’s own cart/checkout security model. Any time a plugin builds a custom bridge into WooCommerce’s write path — inserting into the cart, or worse, mutating product data — I want to see exactly how that bridge is authenticated.

Before touching any code, I did the usual passive pass: checked the plugin’s WPScan history, skimmed the changelog, and looked at how many other plugins in the same “room/booking + WooCommerce” family I had already ruled out. Several sibling plugins I had audited in the same session — a GloriaFood connector, a Beds24 connector, Ticket Tailor — all turned out to be pure SaaS-widget wrappers with no server-side logic of their own, and were dead ends. ND Booking was different: it had its own PHP-side AJAX handlers doing real WooCommerce write operations.

Understanding the Architecture

ND Booking exposes its booking search results through a shortcode, `[nd_booking_search_results]`, registered in `inc/shortcodes/nd_booking_search_result.php`. This shortcode is meant to be dropped onto any public-facing page — a hotel's "search availability" page, for example — and it renders a JavaScript-driven search UI.

To support “book this room” functionality when WooCommerce is active, the plugin registers a dedicated AJAX action:

```
add_action( 'wp_ajax_nd_booking_woo_php', 'nd_booking_woo_php' );
add_action( 'wp_ajax_nopriv_nd_booking_woo_php', 'nd_booking_woo_php' );
```

The `nopriv` variant means this action is reachable by anyone — no login required by design. That much is expected: a booking search page has to work for anonymous visitors. The question is what authorization model protects the handler once it's reachable.

Here is the full handler, `nd_booking_woo_php()`:

```
function nd_booking_woo_php() {
```

```
    check_ajax_referer( 'nd_booking_woo_nonce', 'nd_booking_woo_security' );    //get datas
    $nd_booking_trip_price = sanitize_text_field($_GET['nd_booking_trip_price']);
    $nd_booking_rid = sanitize_text_field($_GET['nd_booking_rid']);
    $nd_booking_meta_box_room_woo_product = get_post_meta( $nd_booking_rid, 'nd_booking_meta_box_room_woo_product', true );    //clear cart
    WC()->cart->empty_cart();    //add to cart the product
    WC()->cart->add_to_cart($nd_booking_meta_box_room_woo_product);    //set the price
    $product = wc_get_product($nd_booking_meta_box_room_woo_product);
    $product->set_regular_price($nd_booking_trip_price);
    $product->set_price($nd_booking_trip_price);
    $product->save();    $nd_booking_book_room_woo_id = 'nd_booking_book_room_'.$nd_booking_rid;
    echo esc_attr($nd_booking_book_room_woo_id);    die();}
```

The only gate here is `check_ajax_referer( 'nd_booking_woo_nonce', 'nd_booking_woo_security' )`. There is no `current_user_can()` call, no check that the requester owns or has any relationship to the room being booked, and — critically — no validation that `$nd_booking_trip_price` is a legitimate p...