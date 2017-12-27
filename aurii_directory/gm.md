---
title: Aurii Game Master Blog
permalink: /aurii_gm/
---

{% for post in site.categories.aurii %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}