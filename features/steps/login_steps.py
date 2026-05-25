from behave import given, when, then
from pages.login_page import LoginPage
from utils.Excel_Util import read_login_data

# @given(u'user is on Login Page')
# def step_launch_browser(context):
#     context.page = context.browser.new_page()
#     context.login = LoginPage(context.page)
#     context.login.open()

# @when(u'user enters valid username and valid password and click on Login button')
# def step_enter_credentials(context):
#     context.login.login("standard_user", "secret_sauce")

# @then(u'user should see HomePage')
# def step_verify_dashboard(context):
#     assert context.login.is_dashboard_visible()

# @given(u'user is on Login Page')
# def step_launch_browser(context):
#     context.page = context.browser.new_page()
#     context.login = LoginPage(context.page)
#     context.login.open()

# @when('user enters "{username}" and "{password}" and Click on Login button')
# def step_enter_credentials(context, username, password):
#     context.login.login(username, password)
#     print(username, password)

# @then('user should see "{result}"')
# def step_validate_result(context, result):
#    if result =="success":
#        assert context.login.is_dashboard_visible(), "Dashboard is not visible"
#    else:
#       error_message = context.login.get_error_message()
#       assert result in error_message, f"Expected '{result}' but got '{error_message}'"

@given("user is on Login Page")
def step_imple(context):
    context.page = context.browser.new_page()
    context.login = LoginPage(context.page)
    context.login.open()
    context.testdata =  read_login_data("testdata/SwagLabsData.xlsx", "Sheet1")

@when("user executes login tests from excel")
def step_enter_credentials(context):

   for data in context.testdata:

      context.login.open()

      context.login.login(data["username"], data["password"])

      if data["result"]== "success":
       
       print("Current URL:", context.page.url)
       assert context.login.is_dashboard_visible()
       print ("on success : " , data )
      else:

       error = context.login.get_error_message()
       assert data["result"] in error
       print ("On Error :" , data )