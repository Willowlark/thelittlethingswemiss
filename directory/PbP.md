---
title: Play by Post GM Blog
permalink: /playbypost/
---

{% for post in site.categories.PbP %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}