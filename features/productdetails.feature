Feature: Product details page functionality
 Background: 
   Given user is logged in

 Scenario: add product from product details page
 When user click on add to cart button
 Then user see product cart flag as 1

 Scenario: proceed to checkout
 When user click on add to cart button and click on remove button
 Then user should complete order process 