---
title: Thomas Fitzsimmons: Excorporate and OAuth 2.0
url: https://www.fitzsim.org/blog/?p=596
source: Planet Classpath
date: 2023-05-24
fetch_date: 2025-10-04T11:38:06.058575
---

# Thomas Fitzsimmons: Excorporate and OAuth 2.0

[Skip to content](#content)

[fitzsim's development log](https://www.fitzsim.org/blog/)

# Excorporate and OAuth 2.0

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1) [May 23, 2023May 23, 2023](https://www.fitzsim.org/blog/?p=596)
[6 Comments on Excorporate and OAuth 2.0](https://www.fitzsim.org/blog/?p=596#comments)

I recently released [Excorporate 1.1.0](https://elpa.gnu.org/packages/excorporate.html) to GNU ELPA.  Excorporate allows Emacs users to retrieve calendar entries directly from an Exchange server such as Office 365, without the need for external programs.

The latest release adds experimental OAuth 2.0 support, via a new library I wrote and published to GNU ELPA, called [url-http-oauth](https://elpa.gnu.org/packages/url-http-oauth.html). With Excorporate 1.1.0, I can access Office 365 again.  A while ago, the server to which I connect had disabled password-based authentication — including application-specific passwords.

I haven’t heard any success reports from users yet, so I wanted to mention the update on my blog. Soon I’ll write a followup post about my thoughts on OAuth 2.0 from a client implementer perspective.

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1)[May 23, 2023May 23, 2023](https://www.fitzsim.org/blog/?p=596)Posted in[Emacs](https://www.fitzsim.org/blog/?cat=3)

## Post navigation

[Previous Post Previous post:
Pixel phones are sold with bootloader unlocking disabled](https://www.fitzsim.org/blog/?p=545)

[Next Post Next post:
firefox-javascript-repl](https://www.fitzsim.org/blog/?p=669)

## Join the Conversation

1. ![](https://secure.gravatar.com/avatar/36709cfff435baf6bcecb09819e06fdd1385f76be372d7be28918c23d643306b?s=60&d=mm&r=g)
2. ![](https://secure.gravatar.com/avatar/d35a78f80fb4c9d6c457e988c467cce1c51965169cc68dc70414e8b57eac0a22?s=60&d=mm&r=g)
3. ![](https://secure.gravatar.com/avatar/6d4a80dee3a081cb5334debbe1f71fc5788db27b1f0189b05934d93883ebf442?s=60&d=mm&r=g)
4. ![](https://secure.gravatar.com/avatar/ed61083db432ab4941e728e0ccf7c6688f2bbb6880091686a58a7436c8d478c8?s=60&d=mm&r=g)
5. ![](https://secure.gravatar.com/avatar/?s=60&d=mm&r=g)

6 Comments

1. ![](https://secure.gravatar.com/avatar/36709cfff435baf6bcecb09819e06fdd1385f76be372d7be28918c23d643306b?s=60&d=mm&r=g)**Dustin Farris** says:

   [July 11, 2023 at 4:15 pm](https://www.fitzsim.org/blog/?p=596#comment-46285)

   This is working for me.

   [Reply](https://www.fitzsim.org/blog/?p=596&replytocom=46285#respond)

   1. ![](https://secure.gravatar.com/avatar/d35a78f80fb4c9d6c457e988c467cce1c51965169cc68dc70414e8b57eac0a22?s=60&d=mm&r=g)**Thomas Fitzsimmons** says:

      [July 12, 2023 at 10:08 am](https://www.fitzsim.org/blog/?p=596#comment-46292)

      Great! Thanks for following up to let me know.

      [Reply](https://www.fitzsim.org/blog/?p=596&replytocom=46292#respond)

      1. ![](https://secure.gravatar.com/avatar/?s=60&d=mm&r=g)**Anonymous** says:

         [August 28, 2024 at 9:11 am](https://www.fitzsim.org/blog/?p=596#comment-47640)

         Not working

         [Reply](https://www.fitzsim.org/blog/?p=596&replytocom=47640#respond)
   2. ![](https://secure.gravatar.com/avatar/6d4a80dee3a081cb5334debbe1f71fc5788db27b1f0189b05934d93883ebf442?s=60&d=mm&r=g)**dmf** says:

      [December 26, 2023 at 2:38 pm](https://www.fitzsim.org/blog/?p=596#comment-46717)

      Sorry to ask, but I relatively new to Emacs.
      I am just trying to understand what is “login\_hint” and “client\_identifier”. Can you share sample configuration, and process about how and where can I find it?

      [Reply](https://www.fitzsim.org/blog/?p=596&replytocom=46717#respond)
2. ![](https://secure.gravatar.com/avatar/ed61083db432ab4941e728e0ccf7c6688f2bbb6880091686a58a7436c8d478c8?s=60&d=mm&r=g)**Benjamin Leis** says:

   [January 10, 2024 at 4:45 pm](https://www.fitzsim.org/blog/?p=596#comment-46753)

   Is there a doc on how to configure this?

   [Reply](https://www.fitzsim.org/blog/?p=596&replytocom=46753#respond)

   1. ![](https://secure.gravatar.com/avatar/d35a78f80fb4c9d6c457e988c467cce1c51965169cc68dc70414e8b57eac0a22?s=60&d=mm&r=g)**Thomas Fitzsimmons** says:

      [April 17, 2025 at 6:24 pm](https://www.fitzsim.org/blog/?p=596#comment-49534)

      It is basically impossible to write general documentation for OAuth 2.0 configurations, unfortunately, because every installation will have different restrictions, subject to vendor defaults, administrator preferences and organizational policies.

      Did you see the Excorporate Info manual? You can find the vague OAuth 2.0 blurb at C-h R excorporate RET m configuration RET.

      You can also look at the url-http-oauth-demo.el file that ships alongside url-http-oauth.el. It has a fully-worked OAuth 2.0 configuration example albeit against a well-understood user-respecting Free Software OAuth 2.0 implementation (Sourcehut’s). That may give you some hints as to how to configure url-http-oauth.el against your organization’s server.

      [Reply](https://www.fitzsim.org/blog/?p=596&replytocom=49534#respond)

## Leave a comment

### [Cancel reply](/blog/?p=596#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name

Email

Website

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

[About www.fitzsim.org](/about)

## Meta

* [Log in](https://www.fitzsim.org/blog/wp-login.php)
* [Entries feed](https://www.fitzsim.org/blog/?feed=rss2)
* [Comments feed](https://www.fitzsim.org/blog/?feed=comments-rss2)
* [WordPress.org](https://wordpress.org/)

[fitzsim's development log](https://www.fitzsim.org/blog/),
[Proudly powered by WordPress.](https://wordpress.org/)