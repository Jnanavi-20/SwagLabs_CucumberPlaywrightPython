from behave import given, when, then
from pages.productList_page import productList_page
from pages.login_page import LoginPage
    
@given(u'user is on login page')
def step_launch_browser(context):
     context.page = context.browser.new_page()
     context.login = LoginPage(context.page)
     context.login.open()
     context.login.login("standard_user", "secret_sauce")
     context.productlist = productList_page(context.page)
    #  context.productlist.open()

@when(u'user is click on sort button and selects Name(A to Z)')
def step_impl(context):
   # context.productlist.open()
    context.productlist.select_sorting_AZ()
   
@then(u'user adds last product to cart')
def step_impl(context):
   context.productlist.verify_and_add_product("Test.allTheThings() T-Shirt (Red)", "$15.99")
    

@when(u'user is click on sort button and selects Name(Z to A)')
def step_impl(context):
   # context.productlist.open()
    context.productlist.select_sorting_ZA()  

@then(u'user adds first product in the list to cart')
def step_impl(context):
    context.productlist.verify_and_add_product("Test.allTheThings() T-Shirt (Red)", "$15.99")

@when(u'user is click on sort button and selects Price (low to high)')
def step_impl(context):
    context.productlist.select_sorting_LTH()

@then(u'user adds first product to cart')
def step_impl(context):
     context.productlist.verify_and_add_product("Sauce Labs Onesie", "$7.99")


@when(u'user is click on sort button and selects Price (high to low)')
def step_impl(context):
     context.productlist.select_sorting_HTL()

@then(u'user adds last product in the list to cart')
def step_impl(context):
   context.productlist.verify_and_add_product("Sauce Labs Onesie", "$7.99")
