---
title: Personal Shoots
---

# Solo Shoots

Photoshoots in which I was the lead/only/etc photographer. I get to take my time during these shoots so they showcase well. 

{% for post in site.categories.personal %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
{% assign images = post.content | split:"<img " %}
{% for image in images %}
  {% if image contains 'src=' %}
    {% assign imageMarkup = image | split:">" | first %}
    <img style="max-height: 480px;" {{ imageMarkup }}>
    {% break %}
  {% endif %}
{% endfor %}
{% endfor %}