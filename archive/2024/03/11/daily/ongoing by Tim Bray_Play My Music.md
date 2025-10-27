---
title: Play My Music
url: https://www.tbray.org/ongoing/When/202x/2024/03/10/Play-My-Music
source: ongoing by Tim Bray
date: 2024-03-11
fetch_date: 2025-10-04T12:08:00.744898
---

# Play My Music

# Play My Music

Search

When I’m away from home, I still want to listen to the music we have at home (well, I can live without the
LPs). We had well over a thousand CDs so that’s a lot of music, 12,286 tracks ripped into Apple Lossless.
Except for a few MP3s from, well, never mind.
This instalment of the
[De-Google Project](/ongoing/What/The%20World/Life%20Online/De-Google/) is about ways to do that with less
Big-Tech involvement.

The former Google Play Music, now YouTube Music, allowed
you to load your tunes into the cloud and play them back wherever your phone or computer happened to be. Except for it used to
be easy to upload — just point the uploader at your iTunes library — and
now it’s hard, and then Google removed YouTube Music’s shuffle-your-uploads feature from Android Auto. Also they fired a bunch
of YouTube Music contractors who were trying to unionize. So screw ’em.

I discovered three plausible ways to do this. First and most simply, dump the tunes onto a USB drive; wherever you are in the
world, you can usually plug one in and play tunes from it.

Second, there’s
[Plex](https://www.plex.tv); you run a Plex server on one of your computers at home (in our case a recent Mac Mini)
which you point at music and video directories, and it’ll serve them to clients on the Web or on phones or on platforms like
WebOS and Roku.

Also, it’ll serve your media to anywhere in the world, using
[UPnP](https://en.wikipedia.org/wiki/Universal_Plug_and_Play) to drill an outgoing hole through your firewall.
Obviously, this could make a security-sensitive person nervous and does bother me a bit, because UPnP’s history has featured
some nasty vulnerabilities. I have a to-do to check whether the version on my dumbass telco ISP router is reasonably safe.
I believe that Tailscale would offer a better security posture, but don’t want one more thing to manage.

Finally, Apple Music can apparently do what YouTube Music does; let you upload your tunes into the cloud and play them
anywhere. But moving from one Big-Tech provider to another doesn’t feel like progress.

Does it work? ·
Setting it up on Plex was a Just-Works experience. The process even reached out through our modern Eero mesh to the
old telco router and convinced it to set up the appropriate UPnP voodoo. If you open the Plex server admin interface it
occasionally complains about a double-NAT situation but works anyhow.

Getting the USB working was kind of hilarious. First of all, I bought a 512G USB stick. (My Mac says it only has 460GB, but
what’s 50G between friends?) USB-A because that’s what the car has. It took a couple of hours to copy all the music onto it.

Then I plugged the USB stick into the car and it showed up instantly in the “Sources” tab of the media player, but
greyed out. I snickered when I noticed that *all* the car infotainment menus were crawling and stuttering. Asking the
car’s mighty electronic brain to index that mountain of music was making it sweat.
Anyhow, after a few minutes, I could access the USB and now it works fine, mostly.

By “mostly”, I mean that when I tell it to play music off the USB, it takes a few seconds for the music to start, then a
minute or more to get its shit together and present a coherent picture of what it’s playing. And on one occasion, the music
player just randomly switched over to the radio. So I suspect my inventory is pushing the poor little toy computer in the car
pretty hard. But once it’s going, the presentation is nice:

[![Jaguar infotainment showing current music and weather](PXL_20240309_193242839.png "Jaguar infotainment showing current music and weather")](-big/PXL_20240309_193242839.jpg.html)

A few items to note here:

1. “Musick” is the name I gave the USB key.
2. That recording is
   [Jesus’ Blood Never Failed Me Yet](https://en.wikipedia.org/wiki/Jesus%27_Blood_Never_Failed_Me_Yet), a truly unique
   piece of work by British composer Gavin Bryars. Opinions vary; I think it’s magical but it’s one of the few pieces of music
   that I am absolutely forbidden to play anywhere my wife can hear it.
3. The car software is way more flexible than Android Auto; this is just one of the car’s three screens and there are a lot of
   options for distributing your music and weather and maps and climate control across them.

Which is better? ·
It’s complicated. Obviously, the USB option doesn’t require any network bandwidth. And I think the album-art presentation is
nicer than Plex’s. (You can see that
[here](/ongoing/When/202x/2024/03/09/DeGoogling#p-7)).

The audio quality is pretty well a wash. Plex is a little louder, I suspect them of
[Loudness-War](https://en.wikipedia.org/wiki/Loudness_war) tactics, which is probably OK in a car with its inevitable
background noise. Plex also crossfades the song transitions, clever and pleasing but really not essential.

Plex is really nice software and I feel a little guilty that I’m not sending them any money. They do have a “Pro” level of
service; must check it out.

Then of course Plex needs Android Auto. Which on the one hand I’m probably going to be running a lot if I’m driving around
town to appointments. But… Android Auto is already a little shaky some days, not sure whether it’s crashing or the car software
is creaking or it’s just yet another lousy USB-C connection (I am developing a real hate for that form factor).

Realistically, given that our
car (a Jaguar I-Pace EV) wasn’t a big seller and is five years old, can I really count on Google and Jaguar to do what it takes
to keep Android Auto running?

At this point I need to say a big “Thanks!” to everyone on Fedi/Mastodon who gave me good advice on how to approach this
problem.

Anyhow, as of now, we have two alternatives that work well. The De-Googling march continues forward.

---

**Updated: 2024/03/10**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing/Feed.png)](/ongoing/comments.atom)

From: [Ivan Sagalaev](https://softwaremaniacs.org/) (Mar 10 2024, at 19:40)

You mention carrying a USB with you, but another simple option is to dump it all into your phone and use it to play it. You car works as a Bluetooth headset.

Also, Plex is quickly becoming another content-pushing enterprise. Have a look at Jellyfin instead.

*[[link](#c1710124812.272328)]*

From: [Tom Atkins](https://www.keybits.net) (Mar 11 2024, at 02:12)

In case you're not aware, Plex have a dedicated music app, Plexamp, which I can recommend: <https://www.plex.tv/plexamp/>

*[[link](#c1710148344.163638)]*

From: [Matt](http://) (Mar 12 2024, at 15:09)

I've been an avid Plex user for many years, I've even dabbled in their undocumented API to export playlists for the car or move track ratings from one instance to another. The Plex Pass has definitely been worth it for the remote access (via plex.tv), hardware transcoding, etc.

Plexamp has also been my goto music player since it came out. I can put it on my personal, work laptop, phone, etc and it all "just works." The wife also has a playlist and uses it for her runs. Okay, I've always wished they had a more powerful song rating and management system, but that's partially where the python scripting against their API comes in to play.

Putting it in a Docker container also makes management, backups, and moving it a snap. One hint, if you're doing any transcoding, mount the transcode directory on a ramdisk to save your SSD from premature wear and tear.

*[[link](#c1710281397.330896)]*

From: [Dan](http://dantasse.com) (Mar 13 2024, at 08:00)

Thank you for posting this! I'm in the exact same spot: Google Play Music was pretty good at this, Youtube Music has been worse, I'd love a non-google alternative. Plex sounds like it'd be great for me. Thank you and all your Mastodon friends for doing the research!

*[[link](#c1710342006.253157)]*

From: [Doug K](https://dkretzmann.blogspot.com) (Mar 13 2024, at 11:02)

It's astonishing to me there are no better solutions.. guess we're all supposed to be streaming...