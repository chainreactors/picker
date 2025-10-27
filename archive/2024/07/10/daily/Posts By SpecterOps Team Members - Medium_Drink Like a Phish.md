---
title: Drink Like a Phish
url: https://posts.specterops.io/drink-like-a-phish-b9e91d0b5677?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-07-10
fetch_date: 2025-10-06T17:51:11.062980
---

# Drink Like a Phish

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb9e91d0b5677&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fdrink-like-a-phish-b9e91d0b5677&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fdrink-like-a-phish-b9e91d0b5677&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-b9e91d0b5677---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-b9e91d0b5677---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

## PHISHING SCHOOL

# Drink Like a Phish

## How to Make Your Phishing Sites Blend In

[![Forrest Kasler](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*twL-x8eyh-Q1_GWn)](https://medium.com/%40fakasler?source=post_page---byline--b9e91d0b5677---------------------------------------)

[Forrest Kasler](https://medium.com/%40fakasler?source=post_page---byline--b9e91d0b5677---------------------------------------)

9 min read

·

Jul 9, 2024

--

Listen

Share

As you read this, bots are coming to find and destroy your phishing sites. You need to protect them before it’s too late! But how?

A phishing page is no good if our targets never get to see it. After bypassing the secure email gateway, convincing a user to click our link, and bypassing any link crawlers, the last “user outbound” control we need to circumvent is the corporate web proxy. Frequently, organizations will choose to route all of their web traffic (HTTP and HTTPS) through a proxy to block known-bad websites, monitor users, and implement data loss prevention (DLP) on web resources. For phishing, our main concern is staying off the known-bad list. That means we need to avoid being crawled by services that might categorize us as malicious and sound the alarm for others before we even send out the phishing campaign. We also need to avoid tell-tails that might trigger a proxy to identify our content as malicious in real time.

## **Do I Know You?**

Have you ever really looked at your logs when you start up a web server? I don’t just mean an Apache access log. I mean full request URLs, queries, headers, and bodies. Within minutes of opening port 80 or 443, you will see traffic from a variety of internet addresses. If you scrutinize the traffic and its intent, you will see that they are generally asking one of two questions:

1. What are you?
2. Can I exploit you?

You didn’t tell anyone that you were starting a website or what domain you just bought, but the traffic shows up right away just the same. How could this be? Well, it turns out that with modern networking speeds, it really isn’t all that expensive or time consuming to scan the whole public IPv4 range for a few common ports like 80 and 443. Open-source tools like Zmap tout the ability to scan the full IPv4 range in just five minutes:

<https://zmap.io/>

Because of this, both researchers and black hat hackers are constantly running their own internet “surveys” looking to identify and fingerprint open web ports. For research projects, like Shodan and Project Sonar, benign HTTP requests are used to interrogate open web servers to catalog each web service. Black hat hackers, on the other hand, will configure their scanners to run exploit checks against each web server, looking for opportunistic wins. Also in the research camp, you will see traffic from security vendors that run internet surveys to identify and block list potential threats based on HTTP response content.

Obviously, if we want our phishing sites to stay off of security vendor block lists, we should be careful not to present “phishy” looking content to just any observer of our websites; especially ones that just discovered our site by scanning our server’s public IP address. Using server name indication (SNI) on our web server, it is easy enough to present a default page when our website is requested using its IP address and only show our phishing page when a request is made for our phishing domain. This will block IP based scanners from seeing our phishing pages. However, this approach is not sufficient on its own. Unfortunately, the moment you register a domain for phishing and set up your phishing site, your domain name will be leaked to the public in two sources:

1. The Internet Corporation for Assigned Names and Numbers (ICANN) Centralized Zone Data Service (CZDS) zone lists: <https://czds.icann.org/home>
2. Google’s Certificate Transparency service: <https://certificate.transparency.dev/>

When you register your domain, your domain is added to ICANN’s zone list for your top-level domain. Security product vendors frequently download the updated lists and scan any domains they have not seen yet. In addition, when you register a TLS cert for your website (assuming you are properly protecting your clients’ data by using TLS while phishing), your certificate details will be published by Certificate Transparency. If you haven’t seen the data set before, take a minute to check out Ryan Sears’s Cert Stream project to view a sample of certificate transparency data in real time from a browser:

<https://certstream.calidog.io/>

You can bet security vendors are also subscribing to the Certificate Transparency feed to identify new domains and subdomains to scan for malicious websites, so configuring SNI is not enough to keep the scanners at bay. Now that we know what we are up against, let’s talk about how to protect our phishing sites.

## Avoiding Pitfalls

First, recognize that any website you put out on the internet is going to be scanned. At a minimum, we want to avoid several common pitfalls that will get your phishing site burned immediately.

![]()

N00b Move!

### N00b Mistake 1: Respond with phishing content to every HTTP request

Instead, you should configure your server to deliver benign content by default. Only deliver malicious content when the URL matches specific attributes that you put in your phishing links; for example, a special “GET” parameter that indicates to the server that this is a legitimate click.

### N00b Mistake 2: Using new domains for phishing

Instead, whenever possible, it is best to let them sit and deliver benign content for at least a few weeks before using them for phishing. We know that bots are going to crawl our sites, so why not just lay low and give them time to make an incorrect assessment of our domain? It’s always nice to have a solid domain ready to go when you need it, so if you don’t have any “seasoned” domains ready to go at this moment, go ahead and buy a few to start the aging process. You’ll thank me later.

### N00b Mistake 3: Listing subdomains in TLS certificate requests

When you list subdomains for your phishing domains in TLS certificate...