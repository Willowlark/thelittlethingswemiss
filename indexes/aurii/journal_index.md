---
title: Aurii Library
permalink: /aurii_library/index.html
---

Listed below are in character collections of character journals and world writings. Each player has leeway with their character's journal beyond that it must remain **canon only**, and **in character**. The details of how these journals are made technically can be found [here]({% link _posts/aurii/posts/2017-12-27-journaling.md  %}). The index page for each character is also an in character section.

---


{% for item in site.aurii_library %}
# [{{ item.title }}]({{site.baseurl}}{{item.url}})
> {{ item.excerpt }}
{% endfor %}