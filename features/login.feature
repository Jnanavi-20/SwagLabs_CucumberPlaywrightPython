Feature: Login functionality 
 Scenario: Login with excel data
  Given user is on Login Page 
  When user executes login tests from excel
  

 # Examples:
#   | username | password | result |
 #   | standard_user | secret_sauce | success |
 #   | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out. |
 #   | standard_user | wrong123 | Epic sadface: Username and password do not match any user in this service |
# When user enters "<username>" and "<password>" and Click on Login button
# Scenario: Valid Login
# Given User is on LoginPage
# When user enters valid username and valid password and click on Login button
# Then user should see Homepage