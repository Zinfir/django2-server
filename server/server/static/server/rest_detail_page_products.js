const Product = ({url, name, description, my_absolute_url, image, product_category}) => (
    `<div class="block product-hover">
        <img src="${image}" alt="">

        <div class="product-text">
            <a href="${my_absolute_url}">&gt;</a>
            <h3>${name}</h3>
            <p>${product_category}</p>
        </div>
    </div>
    `
)

const renderPageData = res => {
    menuHtml = res.data.results.map(Product)
        .join('')
    menu = document.getElementById('detail_page_extra_products')
    menu.innerHTML += menuHtml
}