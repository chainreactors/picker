---
title: Two ongoing Decades
url: https://www.tbray.org/ongoing/When/202x/2023/02/27/Twenty-ongoing-Years
source: ongoing by Tim Bray
date: 2023-02-28
fetch_date: 2025-10-04T08:13:44.887065
---

# Two ongoing Decades

# Two ongoing Decades

Search

*[This fragment is available in [an audio version](Twenty-ongoing-Years.mp3).]*

Today is the 20th anniversary of
[the first-ever public post](/ongoing/When/200x/2003/02/27/Hello) on this blog (Spoiler: Not that interesting).
Some posts mark milestones:
[Is This Thing On?](/ongoing/When/200x/2003/02/28/Watching) (one day), [One ongoing Year](/ongoing/When/200x/2004/02/26/OngoingYear1),
[730 ongoing Days](/ongoing/When/200x/2005/02/27/OngoingYear2),
[Thirty-six ongoing Months](/ongoing/When/200x/2006/02/27/Three-ongoing-Years), and for the ten-year mark,
[Birthday!](/ongoing/When/201x/2013/02/27/Blog-birthday)

I just re-read that last ten-years note and I think it’s good. If you care about this subject at all, do me a favor and go
read it. I’ll wait. Then, a few more words about doing this in 2023 and into the future.

Stats & tech ·
As I write this, there are 5,263 entries here containing 5,098 pictures and 2,249,991 words.
At which point, the following picture applies, stolen from Rakhim’s
[Honestly Undefined](https://rakhim.org/honestly-undefined/), “A webcomic about computers and uncertainty”:

[![Cartoon by Rakhim: Blogging vs blog setups](Rakhim-graph.png "Cartoon by Rakhim: Blogging vs blog setups")](-big/Rakhim-graph.jpg.html)

Heh… I’m the “Weird dude who writes raw HTML” (in Emacs, no less) but then I’m also an “Author of custom static site
generators”.

But, unlike most such
authors, I never write about the generator (nor will I ever open-source it) because it’s kind of gross: 3,000 lines of Perl
written in a brief 2002 hyperfocus episode. It’s all in one file, with no concessions to modularity nor modernity. OK, if you
must, here’s [More on Baking](/ongoing/When/201x/2011/03/18/Baking-ongoing), about something that I think this site does
right.

You know what does make me feel a little smug? My writing environment. Yeah, I author in what’s more or less XHTML, but I
basically never type an angle-bracket. Emacs is simply the world’s best tool for high-powered text editing and on this hill I
will die. For the members of the Emacs tribe, a couple of snippets that may cause smiles and nods.

[![Emacs voodoo to help publish this blog](ongoing-mode.png "Emacs voodoo to help publish this blog")](-big/ongoing-mode.jpg.html)

So when you press `'`, below are the things you can follow it with.
This works because nobody with good taste would ever use a dumb
naked non-typographical single quote, so I repurpose it as a blogging-command-initiator.

[![Emacs voodoo to help publish this blog](ong-insert-special.png "Emacs voodoo to help publish this blog")](-big/ong-insert-special.jpg.html)

Sidebar: How many words? ·
Above, I mentioned the number of words so far. It was actually kind of
hard to measure since a lot of the text is XML junk. So I got Lauren to write me a two-line XSLT and then I had a pure-text version of
all the entries. Unfortunately, `wc -w` and Emacs disagreed on the word count, by a lot. So I opened up the 14-Mb
`.txt` file in Microsoft Word; say what you will, that program does know how to count ’em. Mind you, it burned 14
minutes of CPU time to figure out that the text (in the default 10.5pt Courier New monospace) would occupy 7,028 pages.

(Of course, that word count doesn’t include the contents of this section.)

POSSE ·
That’s the word for what this blog is, as defined
[over at indieweb.org](https://indieweb.org/POSSE): “POSSE is an abbreviation for Publish (on your) Own Site,
Syndicate Elsewhere, the practice of posting content on your own site first, then publishing copies or sharing links to third
parties (like social media silos) with original post links to provide viewers a path to directly interacting with your
content.”

Cory Doctorow recently published
[Pluralistic is three](https://pluralistic.net/2023/02/19/drei-drei-drei/), from which: “POSSE stands for ‘Post Own
Site, Share Everywhere’, and it's an idea that comes out of the Indieweb movement. Under POSSE, you post your work to a site you
control, but syndicate to all the platforms and silos, with a link back to the original.”

Which seems like self-evidently a good approach. It allows me to not care very much that the quips and links I post to Twitter or
Mastodon or whatever the social flavor-of-the-month is might go away. If I really care about it, it gets published here.

Impact? ·
As in, I put a lot of work into this space and it’s reasonable to ask: Has it mattered, and if so, to whom?

The biggest impact is obvious, that would be the impact on my life. The blog has got me jobs, helped me hire, found me
friends, taught me
to write better, taught me about running a production application, and been a ticket to join conversations I care about. Without it, my
life would be immensely poorer along multiple dimensions. I have not regretted launching this thing for even a second over all
the years.

How about impact on other people? Well, I don’t track readership, very much. I couldn’t if I wanted to, because I publish a
full-text RSS/Atom feed, and it’s being fetched all the time by loads of different aggregators and other random software. Some
of the feed fetchers say (in the User-agent) how many subscribers they’re fetching on behalf of. Last time I added those up it
came to twenty thousand or so, but on the one hand, lots of those people will have stopped following feeds a decade ago,
and on the other, some of them come from Slack or Teams, and some from IP addresses inside governments and big companies. So,
who knows? I sure don’t.

I do have a script that plows through recent website logs and pretty reliably counts actual human reads through a browser
(from the site, not the feed). I don’t run it that often, but let’s go do that right now:

[![Recent ongoing viewership statistics](stats.png "Recent ongoing viewership statistics")](-big/stats.jpg.html)

Human reads of ongoing articles for the last two weeks.
Some of these, from years previous, retain a pleasing residual readership.

I guess one thing is worth saying: These numbers are up quite a bit since I started posting links on Mastodon.

Also, year after year,
[/2005/12/23/UPI](/ongoing/When/200x/2005/12/23/UPI) keeps getting fetched for no reason I can discern, except
perhaps that it includes the phrase “cat semantics”.

In this space, I’ve had the privilege of arguing against the horrors of `WS-*`, against Single Page Applications
(especially about the time when Twitter became one, for a while), and against cryptocurrencies. Not always contra: I’ve inveighed
in favor of REST, of Android as a viable platform, of
Unicode (and especially UTF-8), of Ruby, of Go, and of functional-programming idioms.

Most of those arguments came out the way I wanted, and while I would never claim to have moved any
needles myself, my rhetoric probably didn’t hurt. And then there’s the important thing — the privilege of being part of the
conversation.

These days I’m advocating against what Twitter has become and in favor of the Fediverse. Let’s see how this one turns out.

Thinking tool ·
When I’m thinking about something complicated and not sure what to make of it, it’s really super-helpful to start writing an
ongoing piece about it. Sometimes I find a path to a coherent argument that I believe in; and then
sometimes I discover that I didn’t actually think what I thought I thought; still a useful outcome. I recommend this practice.

Greatest hits ·
I still have plenty of writing energy but am getting kind of
old — ongoing’s past is doubtless bigger than its future.

I’ve always thought that when a musician starts doing re-releases and “Greatest Hits” packages, it’s a signal they’ve lost
their mojo, and not much new goodness is to be expected. But over the past twenty years there’ve been pieces that I
suspect might find a second readership if dropped into social media and the feed. So I’m going to try the occasional “Twenty
Years Ago Today” and see if I find it rewarding.

Thanks! ·
For reading, now...