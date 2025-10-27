---
title: SQL Injection Attack on Airport Security
url: https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html
source: Schneier on Security
date: 2024-09-03
fetch_date: 2025-10-06T18:28:22.878332
---

# SQL Injection Attack on Airport Security

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## SQL Injection Attack on Airport Security

Interesting [vulnerability](https://ian.sh/tsa):

> …a special lane at airport security called Known Crewmember (KCM). KCM is a TSA program that allows pilots and flight attendants to bypass security screening, even when flying on domestic personal trips.
>
> The KCM process is fairly simple: the employee uses the dedicated lane and presents their KCM barcode or provides the TSA agent their employee number and airline. [Various forms of ID](https://www.apfa.org/wp-content/uploads/2019/10/KCM-Program-Changes_OCT19.pdf) need to be presented while the TSA agent’s laptop verifies the employment status with the airline. If successful, the employee can access the sterile area without any screening at all.
>
> A similar system also exists for cockpit access, called the Cockpit Access Security System (CASS). Most aircraft have at least one jumpseat inside the cockpit sitting behind the flying pilots. When pilots need to commute or travel, it is not always possible for them to occupy a revenue seat, so a jumpseat can be used instead. CASS allows the gate agent of a flight to verify that the jumpseater is an authorized pilot. The gate agent can then inform the crew of the flight that the jumpseater was authenticated by CASS.
>
> [attack details omitted]
>
> At this point, we realized we had discovered a very serious problem. Anyone with basic knowledge of SQL injection could login to this site and add anyone they wanted to KCM and CASS, allowing themselves to both skip security screening and then access the cockpits of commercial airliners.
>
> We ended up finding several more serious issues but began the disclosure process immediately after finding the first issue.

Tags: [air travel](https://www.schneier.com/tag/air-travel/), [SQL injection](https://www.schneier.com/tag/sql-injection/), [TSA](https://www.schneier.com/tag/tsa/)

[Posted on September 2, 2024 at 7:07 AM](https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html) •
[8 Comments](https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html#comments)

### Comments

Matthias Urlichs •
[September 2, 2024 7:29 AM](https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html/#comment-440312)

As usual, the government idjits (stronger expletives elided) do all they can to discourage further attempts to responsibly disclose vulnerabilities.

If I were to discover something like this I’d put up a public web site with a detailed exploit (anonymously of course), distribute the URL widely, and watch them scramble.

Bcs •
[September 2, 2024 10:37 AM](https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html/#comment-440314)

Shocked. Appalled. Not surprised.

If anything, I’m more surprised this wasn’t found after some 16 year old used it to get free flights.

Matthias Urlichs •
[September 2, 2024 11:44 AM](https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html/#comment-440316)

Most 16 year olds are too obviously too young.

Anyway. Check out “Catch me if you can” if you want to know to do that sort of thing convincingly.

Wayne •
[September 2, 2024 1:19 PM](https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html/#comment-440319)

Sounds like Frank Abagnale is back in business!

lurker •
[September 2, 2024 8:54 PM](https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html/#comment-440322)

The old SQL injection trick, eh? SQL, the DB engine used by pros, and abused by amateurs. Drills through bulletproof cockpit doors. The TSA and DHS’ post facto CYA fudging puts them squarely in the amateur camp. 23 years of security theatre for what progress?

C U Anon •
[September 3, 2024 9:06 AM](https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html/#comment-440331)

Lurker:

“23 years of security theatre for what progress?”

About -30 years, call it “crawl back”…

Some remember

‘Brown shirts and double your pay day’

As they became federales on the Government pay-pension&healthcare, better than some pilots were getting…

Morley •
[September 3, 2024 10:00 AM](https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html/#comment-440332)

Sigh… Still using strings as an API. Could at least make the string API a compiler error and require a flag to turn into a warning.

Winter •
[September 4, 2024 1:04 AM](https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html/#comment-440338)

@lurker

> 23 years of security theatre for what progress?

Maybe *security theatre* has always been the wrong word as it suggests a real story with actual content?

But, denying toddlers access to planes because they were deemed terrorists? Come on, no theatre play would include that.

I suggest *security operetta* instead for the DHS, as it always was about the song and dance, not the theatre.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2024/09/sql-injection-attack-on-airport-security.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2024/09/sql-injection-attack-on-airport-security.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2024%2F09%2Fsql-injection-attack-on-airport-security.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required):

Comments:
![](https://www.schneier.com/wp-content/themes/schneier/assets/images/loader.gif)

**Allowed HTML**
<a href="URL"> • <em> <cite> <i> • <strong> <b> • <sub> <sup> • <ul> <ol> <li> • <blockquote> <pre>
**Markdown Extra** syntax via <https://michelf.ca/projects/php-markdown/extra/>

Δ

[← Friday Squid Blogging: Economic Fallout from Falklands Halting Squid Fishing](https://www.schneier.com/blog/archives/2024/08/friday-squid-blogging-economic-fallout-from-falklands-halting-squid-fishing.html) [List of Old NSA Training Videos →](https://www.schneier.com/blog/archives/2024/09/list-of-old-nsa-training-videos.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019...