const renderItem = ({ name }, count) => (
    `
    <li class="product-item">
      <span class="product-item__title">${name}</span>
      <span class="product-item__count">${count}</span>
    </li>
    `
  );