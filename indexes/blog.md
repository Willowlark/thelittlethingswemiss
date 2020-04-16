---
title: Photography Blog
permalink: /indexes/blog/
---

{% for post in site.tags.main-blog %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}