---
title: Privacy Is OK
url: https://www.tbray.org/ongoing/When/202x/2022/12/29/Privacy-is-OK
source: ongoing by Tim Bray
date: 2022-12-30
fetch_date: 2025-10-04T02:43:48.745697
---

# Privacy Is OK

# Privacy Is OK

Search

*[This fragment is available in [an audio version](Privacy-is-OK.mp3).]*

I hate to write a piece just saying Someone Is Wrong On The Internet. But Reid Blackman’s
[The Signal App and the Danger of
Privacy at All Costs](https://www.nytimes.com/2022/12/28/opinion/jack-dorseys-twitter-signal-privacy.html) (in the NYTimes, forsooth) is not just wrong but dangerously misleading. I haven’t
seen a compact explainer on why, so here goes.

Blackman’s description of what Signal does is accurate: Provides an extremely private communication path among
individuals and groups; private to the extent that
[Signal.org](https://www.signal.org) (a nonprofit) doesn’t even know who’s talking to whom, let alone what
they’re saying.

Blackman argues that this is dangerous because bad people could use it to plan nefarious activities and the legal
authorities wouldn’t be able to eavesdrop on them and stop them. Indeed, bad people can and (I’m sure) do use cryptography to
evade surveillance.

So, let’s agree that Signal offers an upside and a downside. Up: Your privacy is protected from snoopers, be
they maleficent governments or ordinary criminals. Down: It’s hard to wiretap the bad guys.

So, can we remove the downside without doing damage? Blackman says little about that, except the phrase “Whether law
enforcement should tap our phones on the condition that a warrant is obtained…”

I’m sorry to be the bearer of of bad news, but it’s simply not possible to address the downside without completely shattering
the upside. Here are three reasons why.

1. When you say “law enforcement”, who exactly do you mean? Employees of the United States? Of Oregon? Of Crow Wing
   County, MN? Of Italy? Of China? How are you going to sort out the jurisdictional disputes, and how are you going to ensure
   that only “good” law-enforcement organizations get to snoop?
2. A Signal eavesdropping capability would become
   the Holy Grail for every global organized-crime syndicate, national-security agency, and teenage hacker from Belarus.
   They’re pretty smart people at Signal, but there aren’t that many of them, and in a
   fight between them and
   a world-wide army of attackers, I know who I’m betting on.
3. Obviously, employees of Signal would have the ability to eavesdrop on anyone, otherwise they wouldn’t be able to
   respond to wiretapping warrants. How much do you think various flavors of enemy and bad guy would be willing to pay for
   access?

   Even assuming every Signal employee is unimpeachably and eternally incorruptible, suppose an employee has a loved one within the
   jurisdiction of a hostile foreign government. How do you think they’d react to video of that loved one being tortured, with the
   price for ending the torture being wiretapping help?

Blackman says “The company’s proposition that if anyone has access to data, then many unauthorized people probably will have
access to that data is false.” What on earth makes him think that?!

Don’t worry, be happy ·
While I acknowledge that in an ideal world we’d be able to eavesdrop on bad people without shattering privacy for good ones,
that’s not the world we live in. And I actually don’t think it’s that big a problem. For example, Blackman notes that in the
course of the law-enforcement investigation of the January 6th insurrection, police got access to the traitors’ Signal
conversations. How?
Obviously, by getting into their computers or phones, where those conversations are stored.

Serious security professionals would rather hide a camera on your office wall or a keylogger in your PC than try to break the
code. Or even better, get a warrant to search your computer with really serious penalties for refusal.

Also, criminal activities tend to have real-world effects, for example video of people in MAGA hats breaking into
the Capitol, or (much more often) money moving around. Good law-enforcement agencies are quite accomplished at following
the trail of dirty money.

So let’s acknowledge that sometimes strong privacy will slow law-enforcement down. But somehow, they seem to be able to
muddle along without it.

Ideology? ·
Blackman makes all sorts of claims about Signal’s “ideology”, which is irrelevant, because the reality is simpler. It’s
like this: Mathematicians have invented a way to communicate with extreme privacy. (It’s irrelevant whether this is good or bad
at this point, the math doesn’t care.)

Privacy is a good thing,
[one of the benefits of being a member of a
civilization](https://medium.com/i-m-h-o/privacy-primer-c7b9caadfc67). People want it and are justified in wanting it. Now they can have it. There have been no credible proposals for
taking privacy away just from the bad people, and I’ll be astonished if there ever are.

Signal ·
It’s not the only end-to-end encrypted way to communicate, especially since they make their technology available to other
organizations, including WhatsApp.

But while I have your attention, I do recommend Signal. I and my family and most of my
friends and quite a few of my colleagues more or less live in Signal. It’s a really great piece of software. And privacy is good.

---

**Updated: 2023/01/05**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing/Feed.png)](/ongoing/comments.atom)

From: [Fnordpiglet](http://) (Dec 29 2022, at 14:09)

An important aspect of mutually authenticated encryption is that while your conversations are private they’re also verifiably yours. When law enforcement gets access to bad guys devices (or good guys and neutral guys, see US customs dragnet cloning of devices at the border) they know for a very high certainty you did in fact have those conversations and can verify cryptographically who you had them with. Layer on pervasive biometric authentication the story of chain of custody for a communication is even tighter. Again as you point out the math doesn’t care if this is good or bad, it just is. It’s a tool that works in your favor, you know with a very high degree of certainty that the other party is in fact who you think it is. But so does everyone who has access to your conversation know for a high degree of certainty you said those things.

I used to work for a company who advised you always apply the Wall Street journal test to what you write down in a communication - as you can never be certain it won’t be on the front page attributed to you. With mutually authenticated E2E encryption that’s doubly true.

*[[link](#c1672351787.252647)]*

From: [Mark](https://markgoodge.com) (Dec 29 2022, at 14:32)

The (very succesful) cracking of EncroChat is a good example of the fact that law enforcement doesn't really need the ability to eavesdrop on encrypted communications in transit. Compromising the ability of ordinary people to send secure messages isn't really about fighting crime.

*[[link](#c1672353155.784818)]*

From: [ok boomer](http://ok.boomer) (Dec 29 2022, at 16:49)

You can just use any modern encrypted messaging program (made in the last 15 years), and it will encrypt in such a way that you can't prove that the other party wrote that message. Warrantless cloning hard drives at the border should also be illegal. But nice try.

*[[link](#c1672361345.751562)]*

From: [Johannes Ernst](https://reb00ted.org/) (Dec 30 2022, at 11:56)

Glad to see the emphasis that it is often much easier to bribe (or blackmail) employees than a technical attack. Every brute can do it, no army of PhDs in discrete math required.

*[[link](#c1672430180.126873)]*

From: [Joe Pallas](http://) (Dec 30 2022, at 13:12)

I’m not disagreeing, but I think your third point is assuming that if every employee can potentially be compromised then it only takes one compromised employee to compromise privacy. Key splitting would allow internal controls where k of n employees must all authorize decrypting a secret.

It doesn’t make the compromise problem go away, but it does make it harder to accomplish.

*[[link](#c1672434766.35536...