---
title: Shoot Scratchpads
permalink: /pad/
---

# Directory of Photoshoot idea/scratch/shoot/fsuk pads. 

{% for post in site.categories.shootpad %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }})
{% endfor %}