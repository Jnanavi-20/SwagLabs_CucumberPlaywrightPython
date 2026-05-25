from behave import given, when, then
from pages.productList_page import productList_page
from pages.productdetail_page import ProductdetailsPage
from pages.login_page import LoginPage

@given(u'user is logged in')
def step_impl(context):
    context.page = context.browser.new_page()
    context.login = LoginPage(context.page)
    context.login.open()
    context.login.login("standard_user", "secret_sauce")
    context.productlist= productList_page(context.page)
    context.productlist.open()
    context.productdetails = ProductdetailsPage(context.page)

@when(u'user click on add to cart button')
def step_impl(context):
    context.productlist.select_sorting_AZ()
    context.productdetails.select_product_to_productdesc("Sauce Labs Backpack")
   

@then(u'user see product cart flag as 1')
def step_impl(context):
     context.productdetails.verify_and_addproducttocart("Sauce Labs Backpack", "$29.99")


@when(u'user click on add to cart button and click on remove button')
def step_impl(context):
    context.productlist.select_sorting_AZ()
    context.productdetails.select_product_to_productdesc("Sauce Labs Backpack")


@then(u'user should complete order process')
def step_impl(context):
 #   context.page.goto("https://www.saucedemo.com/inventory-item.html?id=4")
    
    # context.productdetails.verify_and_addproducttocart("Sauce Labs Backpack", "$29.99")
    print("iam inside remove product")
    context.productdetails.verify_and_removeproductfromcart("Sauce Labs Backpack", "$29.99")
    # context.productdetails.open()
    # context.productdetails.cart_icon_click()
    # context.productdetails.cart_page_verify()
    # context.productdetails.checkoutpage("secret", "sauce", 890456)
    # context.productdetails.checkout_complete()