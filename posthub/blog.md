---
title: Cosplaying blog
---

# Blogging about Cosplay photography and maybe even cosplaying

{% for post in site.categories.cosplay %}
* [{{ post.title }}]({{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}