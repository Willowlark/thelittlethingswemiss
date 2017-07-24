---
title: Best of Posts
---

# Best of Posts on the blog. (Pinned things)

{% for post in site.tags.pinned %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}