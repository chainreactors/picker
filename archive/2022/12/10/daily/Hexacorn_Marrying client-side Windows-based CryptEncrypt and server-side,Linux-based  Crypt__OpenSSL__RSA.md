---
title: Marrying client-side Windows-based CryptEncrypt and server-side,Linux-based  Crypt::OpenSSL::RSA
url: https://www.hexacorn.com/blog/2022/12/09/marrying-client-side-windows-based-cryptencrypt-and-server-sidelinux-based-cryptopensslrsa/
source: Hexacorn
date: 2022-12-10
fetch_date: 2025-10-04T01:06:10.898162
---

# Marrying client-side Windows-based CryptEncrypt and server-side,Linux-based  Crypt::OpenSSL::RSA

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2022/12/08/the-future-of-soc/)
[Next →](https://www.hexacorn.com/blog/2022/12/15/how-to-be-a-good-quitter/)

# Marrying client-side Windows-based CryptEncrypt and server-side,Linux-based Crypt::OpenSSL::RSA

Posted on [2022-12-09](https://www.hexacorn.com/blog/2022/12/09/marrying-client-side-windows-based-cryptencrypt-and-server-sidelinux-based-cryptopensslrsa/ "10:51 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Time flies and it does so very quickly. The story I am about to tell you is 8 years old, but it does feel like I wrote it yesterday.

In 2014 a client asked me to develop a never-seen-before prototype of a new type of an endpoint agent that would be code-minimal, position-independent, 32- and 64- architecture-aware and talk to a backend using strong encryption. Yes, kinda EDR or C2-like agent and we had discussions about using it for both blue and red team engagements, if it worked.

Anyone who tried to make Windows crypto primitives talk to (typically Linux-based) server-side crypto primitives knows that it is an awful coding experience. After googling around, and trying different things I eventually developed the prototype. I can’t share the code for obvious reasons, but I can at least describe what it did.

On a client side, I had a routine that would talk to the socket (not proxy aware at that time) and follow a basic data protocol exchanging encrypted data blobs with my server. The data was encrypted with a public key that only server could decrypt. Nothing really ground breaking.

What was annoyingly, frustratingly hard to develop was the actual decryption part. The server part was using Crypt::OpenSSL::RSA (yes, perl!) primitive, and I couldn’t force it to decrypt the CryptEncrypted message I was sending.

After many hours of debugging and googling around I eventually figured it out. After I used CryptEncrypt I just had to reverse the data blob delivered by the function: byte, by byte. Yup, it was that simple.

This entry was posted in [C2](https://www.hexacorn.com/blog/category/c2/), [Random ideas](https://www.hexacorn.com/blog/category/random-ideas/), [RSA](https://www.hexacorn.com/blog/category/rsa/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2022/12/09/marrying-client-side-windows-based-cryptencrypt-and-server-sidelinux-based-cryptopensslrsa/ "Permalink to Marrying client-side Windows-based CryptEncrypt and server-side,Linux-based  Crypt::OpenSSL::RSA").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")