Feature: Product list page functionality

 Background: 
  Given user is on login page

 Scenario: product list page is sorted from A-Z
 When user is click on sort button and selects Name(A to Z)
 Then user adds last product to cart

 Scenario: product list page is sorted from Z-A
 When user is click on sort button and selects Name(Z to A)
 Then user adds first product in the list to cart

 Scenario: product list page is sorted Price (low to high)
 When user is click on sort button and selects Price (low to high)
 Then user adds first product to cart

 Scenario: product list page is sorted Price (high to low)
 When user is click on sort button and selects Price (high to low)
 Then user adds last product in the list to cart
