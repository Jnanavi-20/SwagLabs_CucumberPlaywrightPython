class productList_page():

    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/inventory.html"

    def open(self):
        self.page.goto(self.url)

#-------

    def verify_and_add_product(self, product_name, expected_price=None):
        items = self.page.locator(".inventory_item")

        for i in range(items.count()):
            item = items.nth(i)

            name = item.locator(".inventory_item_name").inner_text()
            if name == product_name:

                price = item.locator(".inventory_item_price").inner_text()

                # ✅ Validate price (only if provided)
                if expected_price:
                    assert price == expected_price, f"Price mismatch: {price} != {expected_price}"

                print(f"Product: {name}, Price: {price}")

                # ✅ Click Add to Cart
                item.locator(".btn_inventory").click()
                return

        raise Exception(f"Product not found: {product_name}")
    
    def select_sorting_AZ(self):
        self.page.locator(".product_sort_container").select_option("az")
    
    def select_sorting_ZA(self):
        self.page.locator(".product_sort_container").select_option("za")
    
    def select_sorting_LTH(self):
        self.page.locator(".product_sort_container").select_option("lohi")

    def select_sorting_HTL(self):
        self.page.locator(".product_sort_container").select_option("hilo")