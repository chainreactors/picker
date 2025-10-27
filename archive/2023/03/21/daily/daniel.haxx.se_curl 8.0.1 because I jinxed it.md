---
title: curl 8.0.1 because I jinxed it
url: https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/
source: daniel.haxx.se
date: 2023-03-21
fetch_date: 2025-10-04T10:08:53.970013
---

# curl 8.0.1 because I jinxed it

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# curl 8.0.1 because I jinxed it

[March 20, 2023](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [44 Comments](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comments)

Right. I said in the [8.0.0 blog post](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-0-is-here/) that it might be a good release. It was. Apart form the little bug that caused it to crash in several test cases.

So now we shipped curl 8.0.1, which is almost identical apart from a single commit that was reverted.

Exactly why this was not discovered in our tests and CI jobs before the release we have yet to figure out, but it is certainly more than just a little disturbing.

My deepest apologies for this.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[release](https://daniel.haxx.se/blog/tag/release/)

# Post navigation

[Previous Postcurl 8.0.0 is here](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-0-is-here/)[Next Postcurl code coverage](https://daniel.haxx.se/blog/2023/03/28/curl-code-coverage/)

## 44 thoughts on “curl 8.0.1 because I jinxed it”

1. ![](https://secure.gravatar.com/avatar/769643d022c187d3fbcf06c38b0c61686b0548618e37826c9566d52124994874?s=34&d=monsterid&r=g) **Taran** says:

   [March 21, 2023 at 09:44](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26620)

   No one gives a fuck!

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [March 21, 2023 at 11:03](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26621)

      @Taran: thanks for your very useful feedback!

      1. ![](https://secure.gravatar.com/avatar/b0a0da7670399f7c5c7e8a3ce7fb9a873fb450580413c37c4feb4a09d84879e2?s=34&d=monsterid&r=g) **Charlie Boyle** says:

         [March 21, 2023 at 12:15](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26632)

         I give a fuck Mr Stenberg!
      2. ![](https://secure.gravatar.com/avatar/f914465a9fe966dc74d52c0b1ee3a09ad2693804f54140ec7d09fa7d365df3d1?s=34&d=monsterid&r=g) **Daniele C** says:

         [March 21, 2023 at 12:32](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26634)

         Ignore them… Thanks for the fix, great example of transparency, and looking forward for a post about the CI issue!
      3. ![](https://secure.gravatar.com/avatar/af0a78ca4be64f241d2ef30805ef208090d478e87c0d18504854478ae89e4997?s=34&d=monsterid&r=g) **Maniac** says:

         [March 21, 2023 at 13:02](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26638)

         to add a more positive meaning to Taran’s comment:
         No one gives a fuck, that the 8.0.0 version was not perfect, and thanks for the effort to make it perfect.
   2. ![](https://secure.gravatar.com/avatar/bb2253fdb53ef36d447201a6c68351760125b675f9dc30085b495b17a7ba2c90?s=34&d=monsterid&r=g) **Frublet** says:

      [March 21, 2023 at 11:43](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26623)

      I do!

      1. ![](https://secure.gravatar.com/avatar/b334cdf08b498d2dee2ed198751f1885b7dc8bccdacd2658ad220495c747de2f?s=34&d=monsterid&r=g) **Ozone** says:

         [March 21, 2023 at 23:22](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26665)

         Thanks for your awesome contribution to the open source community. You’re obviously doing very important/difficult work, and mishaps happen.

         We appreciate the fix and transparency. 🙂
   3. ![](https://secure.gravatar.com/avatar/bd23fb7871e3398569d12f1b5a09c5fb44e70cc9284fe32a7d691f317d39d99d?s=34&d=monsterid&r=g) **Taran’s mom** says:

      [March 21, 2023 at 12:09](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26630)

      I give a fuck about you, Taran. I’ll get you a pizza on my way home.
   4. ![](https://secure.gravatar.com/avatar/09dd00779e6467ec54f49a840fe38635098afdc03c0cf8bc65aea849bb90455c?s=34&d=monsterid&r=g) **Taran = Squidward** says:

      [March 21, 2023 at 12:36](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26635)

      Actually I do, thanks for the update, Daniel
   5. ![](https://secure.gravatar.com/avatar/dc39755cab9fd2e179453207b819012bbd5b3aefb20f4a5da0969dddff74f5cd?s=34&d=monsterid&r=g) **[Gerg? Móricz](https://mogery.me)** says:

      [March 21, 2023 at 12:39](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26636)

      i give a fuck 🙂
   6. ![](https://secure.gravatar.com/avatar/6d67151d34a908396f92568da7b6ef13de32b643b08add8b328c9f3619422ecb?s=34&d=monsterid&r=g) **mrjay42** says:

      [March 21, 2023 at 12:51](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26637)

      Well I do give a f\*ck!

      I use Curl at my job, in my scripts at home, on my personal servers, etc.

      Thanks to the people who maintain this kind of lib/program -> I don’t have the ability to do it, so Thanks <3
   7. ![](https://secure.gravatar.com/avatar/67519691b910919fe9fcb2617ff551db39fc9031a80257906da54ef2f30a3526?s=34&d=monsterid&r=g) **Taran's imaginary girlfriend** says:

      [March 21, 2023 at 13:33](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26642)

      @Taran ur bad n ur mom stinks, stfu
   8. ![](https://secure.gravatar.com/avatar/7f946e4972ae0efa58628fcba82e8491c8d11c54263797152c4153d903740758?s=34&d=monsterid&r=g) **[RobIII](https://robiii.me)** says:

      [March 21, 2023 at 14:13](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26645)

      Ungrateful jerk
   9. ![](https://secure.gravatar.com/avatar/d043899d31cd1e6162179462f3d99ccc79d63f29b7b821573104d6c42adb6f8d?s=34&d=monsterid&r=g) **TaranDestroyed** says:

      [March 21, 2023 at 14:42](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26653)

      – Be @Taran
      – Sad basement nerd
      – Randomly find blog post about curl 8.0.1
      – “Hehe, this is going to be so funny”
      – Post “No one gives a fuck!”
      – Chug another bottle of coke
      – Devour an entire bag of cheetos
      – Sit back and marvel at my creation

      You’re sad.
   10. ![](https://secure.gravatar.com/avatar/a46f0ccadbb6a2bfbc12a1419476ae0a1db14dbb93d05f6a4173c4744cb0ad27?s=34&d=monsterid&r=g) **[Be Kind Buddy](https://bekindbuddy.com)** says:

       [March 21, 2023 at 15:52](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26662)

       Perhaps instead of saying that “No one cares” about Daniel’s update, you could consider sharing how you feel and taking some time to relax on the beach, get a tan, and enjoy some time to yourself. ??

       Also, you can say mean things to me at:
       BeKindBuddy.com
       I’m quite therapeutic.
   11. ![](https://secure.gravatar.com/avatar/a46f0ccadbb6a2bfbc12a1419476ae0a1db14dbb93d05f6a4173c4744cb0ad27?s=34&d=monsterid&r=g) **[Be Kind Buddy](https://bekindbuddy.com)** says:

       [March 21, 2023 at 15:53](https://daniel.haxx.se/blog/2023/03/20/curl-8-0-1-because-i-jinxed-it/#comment-26663)

       Perhaps instead of saying that “No one cares” about Daniel’s update, you could consider sharing how you feel, unsubscribing, or taking some time...