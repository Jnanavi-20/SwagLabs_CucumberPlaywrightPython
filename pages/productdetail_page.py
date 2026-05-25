from playwright.sync_api import expect

class ProductdetailsPage():

#     def __init__(self, page):
#         self.page =page 
#         self.url="https://www.saucedemo.com/inventory-item.html?id=4"
        
#     def open(self):
#         self.page.goto(self.url)

#     def select_product_to_productdesc(self, productN):
#        items = self.page.locator(".inventory_item")
#        for i in range(items.count()):
#          item = items.nth(i)
#          name = item.locator(".inventory_item_name").inner_text()
#          if name == productN:
#            price = item.locator(".inventory_item_price").inner_text()
#            print(f"Product: {name}, Price: {price}")
#                 # ✅ Click Add to Cart
#         #    item.locator(".btn_inventory").click()
#            item.locator(".inventory_item_name").click()
#            return

#            raise Exception(f"Product not found: {productN}")

#     def  verify_and_addproducttocart(self, productName, expectedPrice=None):
#         itemdesc= self.page.locator(".inventory_details_container")
#         name = itemdesc.locator("[data-test='inventory-item-name']").inner_text()

#         if productName == name:
               
#               price = itemdesc.locator("[data-test='inventory-item-price']").inner_text()  

#         if expectedPrice:  
#              assert price == expectedPrice, f"Price mismatch: {price} != {expectedPrice}"
                  
#              print(f"Product: {name}, Price: {price}")
#              itemdesc.locator("#add-to-cart").click()
#              return

#         raise Exception(f"Product not found: {productName}")
#         # cart = self.page.locator("#shopping_cart_container")
#         # cart.click()
    
# #remove
#     def verify_and_removeproductfromcart(self, productName, expectedPrice=None):
#         itemdesc= self.page.locator(".inventory_details_container")

#         name = itemdesc.locator("[data-test='inventory-item-name']").inner_text()

#         if productName == name:
               
#               price = itemdesc.locator("[data-test='inventory-item-price']").inner_text()  

#               if expectedPrice:  
#                   assert price == expectedPrice, f"Price mismatch: {price} != {expectedPrice}"
                  
#               print(f"Product: {name}, Price: {price}")
#              # Use text-based locator instead of ID (more stable)
#               add_btn = itemdesc.locator("#add-to-cart")
              
#               remove_btn = itemdesc.locator("#remove")

# # Click Add to Cart
#               expect(add_btn).to_be_visible()
#               add_btn.click()

# # Wait until Remove appears
#               expect(remove_btn).to_be_visible()

# # Click Remove
#               remove_btn.click()

# # ✅ IMPORTANT: wait until it goes back to Add to Cart
#               expect(add_btn).to_be_visible()

#               return

#         raise Exception(f"Product not found: {productName}")

#     def cart_icon_click(self):
#       self.page.wait_for_selector()
#     # header= self.page.locator(".header_label")
#       cart = self.page.locator("a.shopping_cart_link")
#       cart.click()
  

#     def cart_page_verify(self):
#       self.page.wait_for_selector()
#       cartTable= self.page.locator(".cart_list")
#       product=cartTable.locator(".inventory_item_name")
#       print(product.inner_text())
#       Quantity = cartTable.cartTablelocator(".cart_quantity")
#       print(Quantity.inner_text())

#       checkout = self.page.locator("#checkout")
#       checkout.click()

#     def checkoutpage(self, firstname, lastname, zipcode):
#       self.page.wait_for_selector()
#       self.page.locator("#first-name").fill(firstname)
#       self.page.locator("#last-name").fill(lastname)
#       self.page.locator("#postal-code").fill(zipcode)
#       self.page.locator("#continue").click()

#     def checkout_overview(self, product, amount):
#       self.page.wait_for_selector()
#       cart_list = self.page.locator(".cart_list")
#       productN = cart_list.locator(".inventory_item_name")
#       title =productN.inner_text()
#       price = cart_list.locator(".inventory_item_price")
#       AMT = price.inner_text()
#       if product ==title:
#         if AMT:
#            assert AMT == amount, f"Price mismatch: {AMT} != {amount}" 
#       print(f"Product: {title}, Price: {AMT}")

#       totalamount = self.page.locator(".summary_total_label").innert_text()
#       print(totalamount)
#       self.page.locator("#finish").click()

#     def checkout_complete(self):
#       self.page.wait_for_selector()
#       checkout = self.page.locator("#checkout_complete_container")
#       checkout.locator(".complete-header").inner_text()
#       checkout.locator("#back-to-products").click()

    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/inventory-item.html?id=4"

    def open(self):
        self.page.goto(self.url)

    def select_product_to_productdesc(self, productN):
        items = self.page.locator(".inventory_item")

        for i in range(items.count()):
            item = items.nth(i)
            name = item.locator(".inventory_item_name").inner_text()

            if name == productN:
                item.locator(".inventory_item_name").click()
                return

        raise Exception(f"Product not found: {productN}")

    def verify_and_addproducttocart(self, productName, expectedPrice=None):
        itemdesc = self.page.locator(".inventory_details_container")

        name = itemdesc.locator("[data-test='inventory-item-name']").inner_text()

        if productName != name:
            raise Exception(f"Product mismatch: {name}")

        price = itemdesc.locator("[data-test='inventory-item-price']").inner_text()

        if expectedPrice:
            assert price == expectedPrice, f"{price} != {expectedPrice}"

        print(f"Product: {name}, Price: {price}")

        add_btn = self.page.locator("button:has-text('Add to cart')")
        add_btn.click()

    def verify_and_removeproductfromcart(self, productName, expectedPrice=None):
        itemdesc = self.page.locator(".inventory_details_container")

        name = itemdesc.locator("[data-test='inventory-item-name']").inner_text()

        if productName != name:
            raise Exception(f"Product mismatch: {name}")

        price = itemdesc.locator("[data-test='inventory-item-price']").inner_text()

        if expectedPrice:
            assert price == expectedPrice

        add_btn = self.page.locator("button:has-text('Add to cart')")
        remove_btn = self.page.locator("button:has-text('Remove')")

        add_btn.click()
        expect(remove_btn).to_be_visible()

        remove_btn.click()
        expect(add_btn).to_be_visible()

    def cart_icon_click(self):
        self.page.locator(".shopping_cart_link").click()

    def cart_page_verify(self):
        cartTable = self.page.locator(".cart_list")

        product = cartTable.locator(".inventory_item_name").inner_text()
        quantity = cartTable.locator(".cart_quantity").inner_text()

        print(product, quantity)

        self.page.locator("#checkout").click()

    def checkoutpage(self, firstname, lastname, zipcode):
        self.page.locator("#first-name").fill(firstname)
        self.page.locator("#last-name").fill(lastname)
        self.page.locator("#postal-code").fill(str(zipcode))
        self.page.locator("#continue").click()


    def checkout_overview(self, product, amount):
      cart_list = self.page.locator(".cart_list")

      title = cart_list.locator(".inventory_item_name").first
      price = cart_list.locator("[data-test='inventory-item-price']").first

      expect(title).to_contain_text(product)
      expect(price).to_contain_text(amount)

      total_price = self.page.locator("[data-test='total-label']")
      expect(total_price).to_contain_text("Total: $32.39")

      finish_btn = self.page.locator("[data-test='finish']")

    # ✅ IMPORTANT: wait + click + navigation
      expect(finish_btn).to_be_visible()

      with self.page.expect_navigation():
        finish_btn.click()

    # ✅ Verify order completed
      expect(self.page.locator(".complete-header")).to_have_text("Thank you for your order!")

# def checkout_complete(self):
#     pageheader=self.page.locator("#checkout_complete_container")
#     msg = pageheader.locator(".complete-header").inner_text()
#     print(msg)
#     BackBTN= pageheader.locator("#back-to-products")
#     expect(BackBTN).to_be_visible()
#     expect(BackBTN).to_be_enabled()
#     BackBTN.click(timeout=5000)
