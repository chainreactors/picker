---
title: A researcher bought noreply.net. Companies started sending him secrets.
url: https://www.wired.com/story/sensitive-info-goes-into-no-reply-emails-constantly-this-guy-sees-it-all/
source: Instapaper: Unread
date: 2026-08-10
fetch_date: 2026-08-11T03:31:58.292094
---

# A researcher bought noreply.net. Companies started sending him secrets.

[Skip to main content](#main-content)

Menu

[WIRED](/)

[SECURITY](/category/security/)

[POLITICS](/category/politics/)

[THE BIG STORY](/category/big-story/)

[BUSINESS](/category/business/)

[SCIENCE](/category/science/)

[CULTURE](/category/culture/)

[REVIEWS](/category/gear/)

Menu

[WIRED](/)

Account

Account

[Newsletters](/newsletter?sourceCode=hamburgernav)

[Security](/category/security/)

[Politics](/category/politics/)

[The Big Story](/category/big-story/)

[Business](/category/business/)

[Science](/category/science/)

[Culture](/category/culture/)

[ReviewsChevron](/category/gear/)

MoreExpand

[The Big Interview](/the-big-interview/)[Magazine](/magazine/)[Events](/tag/wired-events/)[WIRED Insider](/collection/wiredinsider/)[WIRED Consulting](/tag/wired-consulting/)

[Newsletters](/newsletter?sourceCode=hamburgernav)

[Podcasts](/podcasts/)

[Video](/video/)

[Livestreams](https://www.wired.com/livestreams)

[Merch](https://shop.wired.com/)

[SearchSearch](/search/)

[Matt Burgess](/author/matt-burgess/)

[Security](/category/security)

Aug 8, 2026 6:00 AM

# Sensitive Info Goes Into ‘No Reply’ Emails Constantly. This Guy Sees It All

Two security researchers bought cheap domains—including noreply.net and deleteduser.com—and set up email listening services. Hundreds of companies are sending them corporate secrets.

![Sensitive Info Goes Into ‘No Reply Emails Constantly. This Guy Sees It All](https://media.wired.com/photos/6a760fe8a02e6ace8c74de98/master/w_2560%2Cc_limit/Security_CompaniesAreLeakingSensitiveData.gif)

Photo-Illustration: Jobanny Cabrera; Getty Images

Comment

Loader

Save StorySave this story

Comment

Loader

Save StorySave this story

Cory Solovewicz receives more unwanted emails than you. Seriously—it’s a lot more. Since December 2024, one of the domains at which the security researcher receives email has registered 401,796 messages—by his calculations that’s an average of 699.99 pings per day.

This deluge isn’t the regular flood of spam, newsletters, and unwanted deals that fill many people’s inboxes. Instead, companies and other organizations are inadvertently sending Solovewicz other people’s private information and company secrets. Over the last few years, he’s received injury reports from a city government, confirmation of people’s pizza orders, and account setup emails from a school platform. “I get service orders for people that need repairs. I get lots of test platform credentials,” says [Solovewicz](https://cory.so/about), a security researcher and consultant.

Solovewicz is receiving the avalanche of messages as he’s the owner of the domains [noreply.us](http://noreply.us) and [noreply.net](http://noreply.net), which he purchased in 2020 and 2024, respectively. After originally planning to use the noreply.us domain as a catch-all email—which receives mail sent to any @ address on that domain—to filter messages and enhance his privacy, the researcher quickly noticed that other systems were sending mail to @[noreply.us](http://noreply.us) addresses. “I created an accidental honeypot,” Solovewicz tells WIRED. “I had no idea it was going to turn into this.”

Companies may send emails to [companyname]@noreply.net or similar variations believing they aren’t going anywhere, or could not be monitored in any way. Broadly it’s also possible that they may transform a person’s individual email address to send to one of these placeholder style domains if someone leaves a company or deletes their account.

What started out as a personal email project has become a large-scale effort to warn businesses and other groups that they have misconfigured their internal systems and are accidentally sharing sensitive information. Solovewicz, who presented his work at the Defcon security conference yesterday, says ultimately he is relieved that he ended up with the domains rather than criminal hackers or nation states who could use the data maliciously.

“I did not realize that this was going to be as big of a problem as it is,” says Solovewicz, who is not publicly naming impacted entities. The researcher has been alerting affected companies of their problems, encouraging them to fix the errors and misconfigurations. “I just want companies and organizations to do the right thing and to be auditing their systems and fixing their stuff.”

Solovewicz says that the [noreply.net](http://noreply.net) domain is the largest he owns and has received 400,000 messages over the year and a half that he’s owned it, with 28,365 of those containing attachments. The [noreply.us](http://noreply.us) domain has been sent 37,255 messages over 2,345 days since he purchased it in 2020. Over the month before his conference talk, combined, they’ve received more than 11,000 messages. Overall, emails have been sent from more than 14,000 “from” addresses, from 6,200 root domains. The messages are automated by company systems, not written by humans, the researcher says.

While the issue is not a new one—almost 20 years ago, independent security journalist Brian Krebs, then working at the *Washington Post*, wrote how companies were sending [millions of messages to @donotreply.com emails](http://donotreply.com)—it is inherently avoidable. For instance, companies could use internal domains or the [.invalid](https://datatracker.ietf.org/doc/html/rfc6761) domain that is guaranteed not to exist.

Solovewicz is not alone in this voluntary endeavor, which is helping protect the data of companies—often large ones. Earlier this year, Mike Sheward, the head of security at EV charging company Xeal, spent around $15 to buy the domain [deleteduser.com](http://deleteduser.com). “Within the first hour, there were three different organizations that had emailed stuff to @[deleteduser.com](http://deleteduser.com),” Sheward tells WIRED, pointing out that companies appear to be simply changing email addresses rather than entirely deleting accounts from their systems.

Like Solovewicz, Sheward has seen thousands of unintended emails coming his way—from at least 100 different organizations—across multiple domains he now owns. He’s had emails detailing people’s Viagra orders, messages asking him to approve people’s work vacations or leaves of absence, hotel bookings including people’s full names, and invitations to Zoom meetings from a UK government agency. “There’s a lot of cybersecurity companies and a few Microsoft partner companies as well,” Sheward says. A couple of weeks ago he got an invitation to one San Francisco company’s summer BBQ, addressed to “Dear Deleted User.”

One of the most frequent sources of email, Sheward says without naming the firm, is an AI company that uses object recognition technology to detect workers at industrial sites in the Middle East who may not be following safety protocols. The researcher has received [thousands of CCTV stills](https://infosec.exchange/%40SecureOwl/116633004972665833) from the firm, he says. “I am being a good guardian of the internet dumpster—but if I had been a bad one, it’s not hard to see how this information that is willingly thrown at my face could be misused,” wrote in a Medium [post](https://mike-sheward.medium.com/deleteduser-com-a-15-pii-magnet-c4396eb21061) in April.

As both Solovewicz and Sheward realized the potential scale of the misplaced emails—and what a goldmine the data would be for hackers and extortionists—they, working independently, have purchased more than 30 domains to try and limit the potential for malicious actors to copy the approach.

As part of his Defcon talk, Solovewicz explained he has been building a probe to test if other possible placeholder domains may be configured to receive email. “I’ve scanned 7,136 domains, and 328 of them were identified as having catch-all inboxes configured,” Solovewicz says. “I’m not sure I can say how large of a problem this is, but my concern is that what I ‘accidentally’ found when I registered my domain is just the tip of the iceberg.”

Both researchers sa...