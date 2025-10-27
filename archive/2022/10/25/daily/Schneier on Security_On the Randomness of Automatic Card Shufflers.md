---
title: On the Randomness of Automatic Card Shufflers
url: https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html
source: Schneier on Security
date: 2022-10-25
fetch_date: 2025-10-03T20:49:17.603887
---

# On the Randomness of Automatic Card Shufflers

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

## On the Randomness of Automatic Card Shufflers

Many years ago, Matt Blaze and I talked about getting our hands on a casino-grade automatic shuffler and looking for vulnerabilities. We never did it—I remember that we didn’t even try very hard—but [this article](https://www.bbc.com/future/article/20221019-how-a-magician-mathematician-revealed-a-casino-loophole) shows that we probably would have found non-random properties:

> …the executives had recently discovered that one of their machines had been hacked by a gang of hustlers. The gang used a hidden video camera to record the workings of the card shuffler through a glass window. The images, transmitted to an accomplice outside in the casino parking lot, were played back in slow motion to figure out the sequence of cards in the deck, which was then communicated back to the gamblers inside. The casino lost millions of dollars before the gang were finally caught.

Stanford mathematician Persi Diaconis found other flaws:

> With his collaborator Susan Holmes, a statistician at Stanford, Diaconis travelled to the company’s Las Vegas showroom to examine a prototype of their new machine. The pair soon discovered a flaw. Although the mechanical shuffling action appeared random, the mathematicians noticed that the resulting deck still had rising and falling sequences, which meant that they could make predictions about the card order.

*New Scientist* [article](https://www.newscientist.com/article/mg17523525-500-coming-up-trumps/) behind a paywall. Slashdot [thread](https://games.slashdot.org/story/22/10/22/2237234/how-a-mathematician-magician-revealed-a-casino-loophole).

Tags: [gambling](https://www.schneier.com/tag/gambling/), [loopholes](https://www.schneier.com/tag/loopholes/), [random numbers](https://www.schneier.com/tag/random-numbers/)

[Posted on October 24, 2022 at 6:37 AM](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html) •
[17 Comments](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html#comments)

### Comments

[William Entriken](https://phor.net) •
[October 24, 2022 10:00 AM](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html/#comment-411480)

For people seriously studying this topic, I have also worked on studying manual shuffling. I worked with dealers to watch exactly what they are doing and how those rules could be used to predict the next card to be dealt. With an emphasis on blackjack.

Here is a visualization <https://github.com/fulldecent/blackjack-simulator/blob/master/Unshuffle/Unshuffle%20visualization.pdf>

Internally, calling this project Hit on 18. Since it can come up with uncommon recommendations.

Sofakinbd •
[October 24, 2022 10:47 AM](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html/#comment-411481)

Another good link from the BBC:

Sofa

SpaceLifeForm •
[October 24, 2022 2:23 PM](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html/#comment-411484)

@ sofa

From-the-Department-of-Redundancy-Department:

You are hired!

You did not check what Bruce posted.

Read.

SpaceLifeForm •
[October 24, 2022 3:45 PM](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html/#comment-411486)

re: seven shuffles

Find it on the slashdot thread, and see what I wrote yesterday. I have described seven shuffles here previously.

Note that an AC troll popped up quickly, and see the responses.

The slashdot trolls always attack users with lower id numbers. Always.

SpaceLifeForm •
[October 24, 2022 4:32 PM](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html/#comment-411487)

It may have happened at Treasure Island.

But what do I know?

Ted •
[October 24, 2022 5:17 PM](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html/#comment-411488)

@SpaceLifeForm, Lol! Can you do a perfect shuffle? It seems like a rare ability.

Jeff •
[October 24, 2022 5:30 PM](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html/#comment-411489)

@Ted: Perfect shuffles are not rare or very hard. There’s an entire literature in magic about what’s known as the “Faro Shuffle” (referring to the game, not the ruler). Some practitioners have the ability to make a Faro shuffle look like a normal riffle shuffle. It really doesn’t have much use for gamblers, though.

David Leppik •
[October 24, 2022 5:30 PM](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html/#comment-411490)

Shuffling a deck of cards is anything but random. In fact, a perfect shuffle—which magicians learn—causes the deck to be back to the beginning after 8 shuffles. Even a novice can make sure the top and bottom cards stay in place with only a little practice.

What’s more interesting to me is how card games have been designed to minimize the effects of the non-randomness. I’m not talking professional casinos, I’m thinking of how poker has been played by amateurs for over a century. The middle of the deck is the most random, so another player cuts the deck to put the middle on top. Cards are dealt round-robin, so an off-by-one error causes a crooked dealer to give a different player their desired hand. Relatively few cards are dealt per round, and a different player deals every round, so a single crooked shuffle has limited effect.

Here’s a [visualization of a perfect shuffle](https://leppik.net/shuffle/) I did with CSS animations (and a little JavaScript) a while ago.

lurker •
[October 24, 2022 7:00 PM](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html/#comment-411492)

@David Leppik

The article seems to say that although the deck returns to zero state after the 8th shuffle, it has a special feature that after the 7th “perfect” shuffle, even though deterministic, it is sufficiently mixed for many practical purposes. Using a “riffle” shuffle it’s no longer deterministic.

Clive Robinson •
[October 25, 2022 12:05 AM](https://www.schneier.com/blog/archives/2022/10/on-the-randomness-of-automatic-card-shufflers.html/#comment-411496)

@ Bruce,

As I’ve mentioned in the past I have an interest in “Card Shuffling Algorithms”(CSA) for security applications including as “entropy spreaders” on “True Random Number Generators”(TRNGs).

The problem is that all machine based CSA’s are bound and thus without an actual TRNG input are by definition not just determanistic but predictably so. Worse due to just how small the mechanical bounds are they are generally not that hard to reverse the sequences.

For those with a little more than curiosity consider the machines as being in several parts

1, Feed input / stor...