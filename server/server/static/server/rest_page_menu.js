const Product_Category = ({url, name, description, my_absolute_url}) => (
    `<li>
        <a
            class="submenu-link products-menu-item" href="${my_absolute_url}">
            ${name}
        </a>
    </li>`
)

const renderData = res => {
    menuHtml = res.data.results.map(Product_Category)
        .join('')
    menu = document.getElementById('rest_page_menu')
    menu.innerHTML += menuHtml
}