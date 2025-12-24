---
layout: default
title: Code Diff Example
---

```diff
+ This is an addition
- This is a deletion
```



{% for commit in site.commits %}
{{ commit.message }}

{{ commit.description }}


View Patch
{% endfor %}