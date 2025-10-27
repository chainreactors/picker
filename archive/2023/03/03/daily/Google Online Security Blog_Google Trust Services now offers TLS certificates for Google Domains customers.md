---
title: Google Trust Services now offers TLS certificates for Google Domains customers
url: http://security.googleblog.com/2023/03/google-trust-services-now-offers-tls.html
source: Google Online Security Blog
date: 2023-03-03
fetch_date: 2025-10-04T08:30:36.344078
---

# Google Trust Services now offers TLS certificates for Google Domains customers

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Google Trust Services now offers TLS certificates for Google Domains customers](https://security.googleblog.com/2023/03/google-trust-services-now-offers-tls.html "Google Trust Services now offers TLS certificates for Google Domains customers")

March 2, 2023

Andy Warner, Google Trust Services, and Carl Krauss, Product Manager, Google Domains

We’re excited to announce changes that make getting [Google Trust Services](https://pki.goog/) TLS certificates easier for Google Domains customers. With this integration, all Google Domains customers will be able to acquire public certificates for their websites at no additional cost, whether the site runs on a Google service or uses another provider. Additionally, Google Domains is now making [an API available](https://domains.google/learn/gts-acme) to allow for DNS-01 challenges with Google Domains DNS servers to issue and renew certificates automatically.

Like the existing [Google Cloud](https://cloud.google.com/blog/products/identity-security/introducing-general-availability-of-google-cloud-certificate-manager) integration, Automatic Certificate Management Environment ([ACME](https://datatracker.ietf.org/doc/html/rfc8555)) protocol is used to enable seamless automatic lifecycle management of TLS certificates.

These certificates are issued by the same Certificate Authority (CA) Google uses for its own sites, so they are widely supported across the entire spectrum of devices used to access your services.

### How do I use it?

Using ACME ensures your certificates are renewed automatically and many hosting services already support ACME. If you're running your own web servers / services, there are ACME clients that integrate easily with common servers. To use this feature, you will need an API key called an [External Account Binding](https://tools.ietf.org/html/rfc8555#section-7.3.4) key. This enables your certificate requests to be associated with your Google Domains account. You can get an API key by visiting [Google Domains](https://domains.google.com/) and navigating to the Security page for your domain. There you’ll see a section for Google Trust Services where you can get your EAB Key.

![](https://lh5.googleusercontent.com/E55DsekQeTDNVTgv3LIUUv_WS1xnp6PsjDI4qDruYRt3xCBqKL157NZVNDU2ZVdGwCZ0SmBZZXFeO-XLKqAxS9E0ijBysV52zGIUI8jw4uNAsV1JgK0-3upl7vY6Wn7FmQ8GQahyFh0EmUJrQj70GwQ)

*Example of EAB Credentials in Google Domains*

As an example, with the popular Certbot ACME client, the configuration to register an account looks like:

certbot register --email <CONTACT\_EMAIL> --no-eff-email --server "https://dv.acme-v02.api.pki.goog/directory"  --eab-kid "<EAB\_KEY\_ID>" --eab-hmac-key "<EAB\_HMAC\_KEY>"

The EAB\_KEY\_ID and EAB\_HMAC\_KEY are both provided on your Google Domains security page.

After the account is created, you may issue certificates by running:

certbot certonly -d <domain.com> --server "https://dv.acme-v02.api.pki.goog/directory" --standalone

Then follow the prompts to complete validation and download your certificate. If you need additional information please visit the [Google Domains help center](https://support.google.com/domains/answer/7630973).

###

###

### Google Domains and ACME DNS-01

ACME uses challenges to validate domain control before issuing certificates. The [ACME DNS-01](https://www.rfc-editor.org/rfc/rfc8555.html#section-8.4) challenge can be an efficient way for users to automate the validation process and integrate with existing websites and web hosting services.

Google Domains now provides an API for ACME DNS-01 challenges that helps streamline the process for users to authenticate domain control quickly and securely. This is now offered in some popular ACME clients like [Certbot](https://certbot.eff.org/) via [this plugin](https://github.com/aaomidi/certbot-dns-google-domains), [Caddy](https://caddyserver.com/), [Certify The Web](https://certifytheweb.com/), [Posh-ACME](https://poshac.me/). You can find additional information on the [Google Domains site](https://domains.google/learn/gts-acme).

![](https://lh4.googleusercontent.com/yyVw4GcbfKacG3XstiUF7g2QhgqKRfiiWVrfuho9jkUxdmjrbdUPCeOuFPEN03ixzioBhif5F0rPs4qTVd8bFUD8e6vl7irm1_VZFrABLImO-cRDzRK36aqPe5DVi4g2iGoUtz6SD9OYoNGBPT7Ljhc)

*Example of DNS API Access Token in Google Domains*

To set up automatic certificate provisioning with ACME and DNS-01, follow these steps:

1. Sign in to [Google Domains](https://domains.google.com/registrar).
2. Select the domain that you want to use.
3. At the top left, click “Menu” and select “Security”.
4. Under section “ACME DNS API”, click “Create token”.
5. A dialog box will appear with an “API Token”. This is the API Token you will need to enter into your ACME client. You will need to copy this value and can do so by clicking the copy button next to the API Token.

* **NOTE:** This value is only shown **once**. After the dialog box is closed you  will not be able to see this API Token again. Store this token in a safe place, since anyone that has it gains the ability to modify some DNS TXT records for your Domain.
* If you did not save this value before closing the dialog box, you can easily delete and create a new API token.
* A limit of 10 API tokens per domain can exist at a time.

6. Once the dialog box is closed you will be able to see in the list that the token has been created. You can delete this token at any time to revoke its access.
7. The API token can now be used in an ACME client that supports the Google Domains ACME DNS API. Each ACME client differs slightly on how to specify this API Token so you will need to read the documentation on your desired ACME client.

Regardless of which ACME client you use, Google Domains and Google Trust Services are excited to offer a reliable option for no-cost TLS certificates. This continues the mission of helping build a safer internet by providing a transparent, trusted, and reliable Certificate Authority.

![Share on Twitter](https://www.gstatic.com/images/icons/material/system/2x/post_twitter_black_24dp.png)

![Share on Facebook](https://www.gstatic.com/images/icons/material/system/2x/post_facebook_black_24dp.png)

[Google](https://plus.google.com/112374322230920073195)

#### No comments :

[Post a Comment](https://www.blogger.com/comment/fullpage/post/1176949257541686127/4025163291752105758)

[**](https://security.googleblog.com/)

[**](https://security.googleblog.com/2023/03/thank-you-and-goodbye-to-chrome-cleanup.html "Newer Post")

[**](https://security.googleblog.com/2023/03/8-ways-to-secure-chrome-browser-for.html "Older Post")

![](data:image/png;base64...)

## Labels

**

* [#sharethemicincyber](https://security.googleblog.com/search/label/%23sharethemicincyber)
* [#supplychain #security #opensource](https://security.googleblog.com/search/label/%23supplychain%20%23security%20%23opensource)
* [AI Security](https://security.googleblog.com/search/label/AI%20Security)
* [android](https://security.googleblog.com/search/label/android)
* [android security](https://security.googleblog.com/search/label/android%20security)
* [android tr](https://security.googleblog.com/search/label/android%20tr)
* [app security](https://security.googleblog.com/search/label/app%20security)
* [big data](https://security.googleblog.com/search/label/big%20data)
* [biometrics](https://security.googleblog.com/search/label/biometrics)
* [blackhat](https://security.googleblog.com/search/label/blackhat)
* [C++](https://security.googleblog.com/search/label/C%2B%2B)
* [chrome](https://security.googleblog.com/search/label/chrome)
* [chrome enterprise](https://security.googleblog.com/search/label/chrome%20enterprise)
* [chrome security]...