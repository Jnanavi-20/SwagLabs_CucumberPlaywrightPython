# from behave import given, when, then
# from pages.login_page import LoginPage

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
       