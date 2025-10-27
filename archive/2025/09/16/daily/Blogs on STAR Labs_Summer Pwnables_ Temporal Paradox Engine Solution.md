---
title: Summer Pwnables: Temporal Paradox Engine Solution
url: https://starlabs.sg/blog/2025/09-temporal-paradox-engine-solution/
source: Blogs on STAR Labs
date: 2025-09-16
fetch_date: 2025-10-02T20:11:31.176972
---

# Summer Pwnables: Temporal Paradox Engine Solution

[![logo](https://starlabs.sg/logo-white.png)](https://starlabs.sg/ "  (Alt + H)")

* [Home](https://starlabs.sg/ "Home")
* [About](https://starlabs.sg/about/ "About")
* [Advisories](https://starlabs.sg/advisories/ "Advisories")
* [Blog](https://starlabs.sg/blog/ "Blog")
* [Achievements](https://starlabs.sg/achievements/ "Achievements")
* [Publications](https://starlabs.sg/publications/ "Publications")
* [Search](https://starlabs.sg/search/ "Search (Alt + /)")

[Home](https://starlabs.sg/) » [Blogs](https://starlabs.sg/blog/)

# Summer Pwnables: Temporal Paradox Engine Solution

September 15, 2025 · 13 min · Muhammad Alifa Ramdhan

Table of Contents

* [Challenge #002: Walkthrough](#challenge-002-walkthrough)
* [Author Solution](#author-solution)
* [Intended solution #01](#intended-solution-01)
* [Intended solution #02](#intended-solution-02)
* [Close words](#close-words)
* [Writeup by students](#writeup-by-students)
* [References](#references)

Last month, Jacob asked me to create a CTF challenge for the Summer Pwnables event. I went with a kernel pwnable since my goal was to teach students some more advanced Linux kernel exploitation techniques - something that wouldn’t get solved in a day (and hopefully not by AI either).

After building both the challenge and solution, I figured students should be able to crack it within 3-7 days. Turns out I was right about the timeline, but only one person actually solved it. [Jun Rong Lam](https://www.linkedin.com/in/jro-sg/), he is the first solver by solving this challenge in a week. The next week [Lucas Tan Yi Je](https://www.linkedin.com/in/lucas-tan-yi-jie/) solved it. In third week, [Elijah Chia](https://www.linkedin.com/in/elijah-chia) solved this challenge, so 3 weeks in total. I really amaze by these students skills and persistence.

Before I explain the solution, you can get the challenge [here](https://github.com/star-sg/challenges/blob/main/Aug%202025/readme_ramdhan.md).
If you want hints, you can see [this](https://www.linkedin.com/posts/starlabs-sg_challenge-002-feeling-stuck-time-for-activity-7364558318964543488-GcKd) and [this](https://www.linkedin.com/posts/starlabs-sg_challenge-002-hint-3-our-participants-activity-7366050311725092864-xsgc).

## Challenge #002: Walkthrough[#](#challenge-002-walkthrough)

Now let me introduce you the challenge. Like usual kernel pwnables, we give them vulnerable kernel driver.

```
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/refcount.h>
#include <linux/cdev.h>
#include <linux/slab.h>
#include <linux/miscdevice.h>
#include <linux/uaccess.h>
#include <linux/atomic.h>
#include <linux/list.h>
#include <linux/mutex.h>

#define DEVICE_NAME "paradox_engine"

MODULE_LICENSE("GPL");

struct temporal_event {
        u64 event_id;
        refcount_t causal_weight;
        struct temporal_event *causal_dependency;
        char description[64];
        struct list_head timeline_node;
        struct timeline *parent_timeline;
};

struct timeline {
        u64 timeline_id;
        atomic64_t next_event_id;
        struct list_head events_head;
        struct temporal_event *caused_by_event;
        struct list_head session_node;
};

struct paradox_session_data {
        struct mutex lock;
        struct list_head all_timelines;
        atomic64_t next_timeline_id;
};

static struct kmem_cache *temporal_event_cache;

static void event_erase_from_reality(struct temporal_event *event);

static void event_get(struct temporal_event *event) { if (event) refcount_inc(&event->causal_weight); }
static void event_put(struct temporal_event *event) { if (event && refcount_dec_and_test(&event->causal_weight)) event_erase_from_reality(event); }
static void event_erase_from_reality(struct temporal_event *event) {
        //      printk(KERN_INFO "paradox_engine: Erasing event '%s' (Timeline %llu, Event %llu) from reality.\n", event->description, event->parent_timeline->timeline_id, event->event_id);
        kfree(event);
}

static struct temporal_event* find_event_in_timeline(struct timeline *tl, u64 event_id) {
        struct temporal_event *ev;
        if (!tl) return NULL;
        list_for_each_entry(ev, &tl->events_head, timeline_node) {
                if (ev->event_id == event_id) return ev;
        }
        return NULL;
}

#define PARADOX_CREATE_TIMELINE _IOWR('k', 1, struct paradox_timeline_req)
#define PARADOX_CREATE_EVENT _IOWR('k', 2, struct paradox_event_req)

struct paradox_timeline_req {
        u64 cause_timeline_id, cause_event_id;
        u64 new_timeline_id;
};
struct paradox_event_req {
        u64 target_timeline_id;
        u64 cause_event_id;
        char description[64];
        u64 new_event_id;
};

static int paradox_engine_open(struct inode *inode, struct file *filp) {
        struct paradox_session_data *session = kzalloc(sizeof(*session), GFP_KERNEL);
        if (!session) return -ENOMEM;

        mutex_init(&session->lock);

        INIT_LIST_HEAD(&session->all_timelines);
        atomic64_set(&session->next_timeline_id, 0);

        struct timeline *primordial_tl = kzalloc(sizeof(*primordial_tl), GFP_KERNEL);
        if (!primordial_tl) { kfree(session); return -ENOMEM; }
        primordial_tl->timeline_id = atomic64_fetch_add(1, &session->next_timeline_id);
        atomic64_set(&primordial_tl->next_event_id, 0);
        INIT_LIST_HEAD(&primordial_tl->events_head);
        list_add_tail(&primordial_tl->session_node, &session->all_timelines);

        struct temporal_event *first_cause = kmem_cache_alloc(temporal_event_cache, GFP_KERNEL|__GFP_ZERO);
        if (!first_cause) { kfree(primordial_tl); kfree(session); return -ENOMEM; }
        first_cause->event_id = atomic64_fetch_add(1, &primordial_tl->next_event_id);
        refcount_set(&first_cause->causal_weight, 1);
        strcpy(first_cause->description, "The First Cause");
        first_cause->parent_timeline = primordial_tl;
        list_add_tail(&first_cause->timeline_node, &primordial_tl->events_head);

        filp->private_data = session;
        //printk(KERN_INFO "paradox_engine: New private universe created with Local Causality law.\n");
        return 0;
}

static int paradox_engine_release(struct inode *inode, struct file *filp) {
        struct paradox_session_data *session = filp->private_data;
        struct timeline *tl, *tmp_tl;
        struct temporal_event *event, *tmp_event;
        //printk(KERN_INFO "paradox_engine: Collapsing private universe.\n");
        list_for_each_entry(tl, &session->all_timelines, session_node) {
                list_for_each_entry_safe(event, tmp_event, &tl->events_head, timeline_node) {
                        struct temporal_event *cause = event->causal_dependency;
                        list_del(&event->timeline_node);
                        while (cause) {
                                struct temporal_event *next_in_chain = cause->causal_dependency;
                                event_put(cause);
                                cause = next_in_chain;
                        }
                        event->causal_dependency = NULL;
                        event_put(event);
                }
        }
        //printk(KERN_INFO "paradox_engine: Final cleanup of all timelines.\n");
        list_for_each_entry_safe(tl, tmp_tl, &session->all_timelines, session_node) {
                list_del(&tl->session_node);
                if (tl->caused_by_event) event_put(tl->caused_by_event);
                kfree(tl);
        }
        kfree(session);
        return 0;
}

static long paradox_engine_ioctl(struct file *filp, unsigned int cmd, unsigned long arg) {
        struct paradox_session_data *session = filp->private_data;
        struct timeline *target_tl = NULL, *tmp_tl;
        long ret = 0;

        mutex_lock(&session->lock);

        switch (cmd) {
                case PARADOX_CREATE_TIMELINE:
                        {
                                struct paradox_timeline_req req;
                      ...