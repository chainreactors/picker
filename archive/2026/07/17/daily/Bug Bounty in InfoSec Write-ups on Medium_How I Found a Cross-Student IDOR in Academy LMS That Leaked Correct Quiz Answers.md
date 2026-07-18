---
title: How I Found a Cross-Student IDOR in Academy LMS That Leaked Correct Quiz Answers
url: https://infosecwriteups.com/how-i-found-a-cross-student-idor-in-academy-lms-that-leaked-correct-quiz-answers-c68bfe06f3a0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-17
fetch_date: 2026-07-18T04:45:03.560669
---

# How I Found a Cross-Student IDOR in Academy LMS That Leaked Correct Quiz Answers

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-cross-student-idor-in-academy-lms-that-leaked-correct-quiz-answers-c68bfe06f3a0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-cross-student-idor-in-academy-lms-that-leaked-correct-quiz-answers-c68bfe06f3a0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c68bfe06f3a0---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c68bfe06f3a0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Press enter or click to view image in full size

![]()

Cybersecurity

Technology

Bug Bounty

Walkthrough

WordPress

# How I Found a Cross-Student IDOR in Academy LMS That Leaked Correct Quiz Answers

## Author: [Shikhali Jamalzade](https://medium.com/u/20557ba7487d?source=post_page---user_mention--c68bfe06f3a0---------------------------------------) GitHub: [alisalive](http://github.com/alisalive) LinkedIn: [camalzads](http://linkedin.com/in/camalzads) Type: Independent Security Research | WordPress Plugin CVE Research

[![Shikhali Jamalzade](https://miro.medium.com/v2/resize:fill:64:64/1*1y98p7kVR06Fq8997mI2FQ.png)](https://alisalive.medium.com/?source=post_page---byline--c68bfe06f3a0---------------------------------------)

[Shikhali Jamalzade](https://alisalive.medium.com/?source=post_page---byline--c68bfe06f3a0---------------------------------------)

8 min read

·

3 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dc68bfe06f3a0&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-cross-student-idor-in-academy-lms-that-leaked-correct-quiz-answers-c68bfe06f3a0&source=---header_actions--c68bfe06f3a0---------------------post_audio_button------------------)

Share

This is a write-up of a vulnerability I independently discovered in Academy LMS, a WordPress LMS plugin with 2,000+ active installations. The vulnerability allowed any enrolled student to read another student’s private quiz results and extract the correct answers to quiz questions — before or during an attempt. It was independently confirmed by another researcher, has since been patched, and this write-up is being published after the fix was released.

Background: Why Academy LMS

My WordPress plugin research methodology targets plugins in the 500–9,000 active installations range — a zone that tends to receive less security scrutiny than larger plugins while still having enough real-world deployment to matter. For each candidate, I start with passive analysis: reading the changelog for security-related keywords, reviewing the readme, and checking WPScan’s vulnerability history before touching any code.

Academy LMS caught my attention because its 3.8.1 changelog contained a specific entry: “Fixed — AJAX API vulnerability in the Notes feature.” This is one of the strongest signals I look for. A developer who has already fixed a security issue in one part of a codebase often used the same patterns elsewhere — and those other places sometimes didn’t get fixed at the same time. My hypothesis was simple: if the Notes controller was fixed, what about the Quiz controller?

This turned out to be exactly the right question.

Understanding the Architecture

Academy LMS uses two parallel systems for handling API requests.

The first is a centralized AJAX handler defined in `includes/classes/abstract-ajax-handler.php`. Every AJAX action registered through this base class passes through `handle_ajax_request()`, which enforces nonce validation and capability checks before dispatching to the actual callback. This is a solid design pattern.

The second system is a collection of REST controllers under `includes/api/` and `addons/quizzes/api/`. Each controller registers its own routes via `register_rest_route()` and defines its own `permission_callback` per endpoint. This is where consistency breaks down.

When I grepped for `permission_callback` across the entire plugin, the Notes controller showed the correct pattern: every route used `array($this, 'permissions_check')`, and that function derived the user via `get_current_user_id()`, never accepting a user identifier from the request. The Notes fix had made this air-tight.

The Quiz attempts controller told a different story.

Two routes in `addons/quizzes/api/quiz-questions.php` used `'permission_callback' => '__return_true'` — meaning no authentication required at all for those endpoints. That was worth noting. But the more serious issue was in `addons/quizzes/api/quiz-attempts.php`, specifically in the `get_student_quiz_attempt_details` endpoint.

The Vulnerability: Two Separate Failure Points

The `get_student_quiz_attempt_details` handler had two independent authorization failures that together created a working IDOR.

Failure point one: the target user was read from the request, not the session.

```
// addons/quizzes/api/quiz-attempts.php, line ~305
$student_id = $request->get_param( 'user_id' );
if ( ! $student_id ) {
    $student_id = get_current_user_id();
}
```

The handler falls back to the session user only if `user_id` is absent from the request. Any caller who supplies a `user_id` parameter gets that value used as the target identity. This is the classic IDOR setup: the object being accessed is determined by a client-controlled key.

Failure point two: the access gate was evaluated against the victim’s context, not the caller’s.

```
// lines ~308-315
$is_administrator = current_user_can( 'administrator' );
$is_instructor    = \Academy\Helper::is_instructor_of_this_course( $student_id, $course_id );
$enrolled         = \Academy\Helper::is_enrolled( $course_id, $student_id );
$is_public        = \Academy\Helper::is_public_course( $course_id );
```

```
if ( $is_administrator || $is_instructor || $enrolled || $is_public ) {
    // returns attempt details
}
```

Notice that `is_instructor_of_this_course` and `is_enrolled` both receive `$student_id` — the attacker-controlled value — not `get_current_user_id()`. So when an attacker supplies a victim's `user_id`, the gate asks "is the victim enrolled in this course?" rather than "is the caller enrolled in this course?" If the victim is enrolled (which they must be to have a quiz attempt), the gate returns true, and the handler proceeds to fetch and return that victim's data.

The database query confirmed the full impact:

```
// classes/query.php, get_quiz_attempt_details()
"SELECT
    attempt_answers.attempt_id,
    attempt_answers.user_...