{% extends "base.html" %}

{% block title %}Product page{% endblock %}

{% block content %}
<main class="product-details">
  <h1 class="my-4">{{ product.title }}</h1>
  <div class="row">
    <div class="col-4">
      <img src="{{ product.image.url }}" alt="{{ product.title }}" class="w-100">
    </div>
    <div class="col-8">
      <h3 class="mb-3">Cost: {{ product.cost }}</h3>
      <h3 class="mb-3">Status: {{ product.get_status_display }}</h3>
      <div class="mb-3">
        <h3 class="mb-3">Description:</h3>
        {{ product.description }}
      </div>

      <form method="post">
        {% csrf_token %}
        <h3 class="mb-3">Purchase this product</h3>
        <div class="row">
          <div class="col-6">
            <div class="input-group mb-3">
              <input name="count" type="text" class="form-control" placeholder="Count" aria-label="Cost"
                     aria-describedby="product-count">
              <span class="input-group-text" id="product-count">
                <button type="submit" class="btn">Purchase</button>
              </span>
            </div>
            </div>
          </div>
      </form>

      {% if product.purchases.exists %}
        <div>
          <h3 class="my-3">Users previously purchased this product:</h3>
          <ul>
            {% for purchase in product.purchases.all %}
              <li>{{ purchase.count }} item(s) by {{ purchase.user.username }} at {{ purchase.created_at }}</li>
            {% endfor %}
          </ul>
        </div>
      {% endif %}
    </div>
  </div>
</main>
{% endblock %}
