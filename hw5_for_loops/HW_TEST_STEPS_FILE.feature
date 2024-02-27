# TracyArispe at 2/4/2024

Feature: Target.com user features


  Scenario: Verify user cart is empty on Target.com
    Given Open Target main page
    When Click on cart icon
    Then Verify Your cart is empty text displays


  Scenario: User can open the sign-in form on Target.com
    Given Open Target main page
    When Click on sign in icon
    When Click on Account sign in icon
    Then Verify By signing in, you agree to the following: message displays accurately


  Scenario: Verify item added to cart on Target.com
    Given Open Target main page
    When Type search word yankee candles into textbox
    When Click the search icon
    When Click Add to cart button
    When Click on Pick Up button
    When Click Side Panel Add to Cart button
    When click on View cart & check out
    Then Verify 22oz Vanilla Cupcake Original Large Jar Candle - Yankee Candle message is shown


  Scenario: Verify 5 benefit boxes are shown on Target.com circle page
    Given Open Target circle page
    Then Verify 5 benefit boxes are shown

  Scenario: Verify Target.com help UI
    Given Open Target help UI page
    Then Verify Target Help text is shown
      Then Verify 7 link boxes are shown
      Then Verify 2 information boxes are shown
      Then Verify Browse all Help pages text is visible

  Scenario: Verify user can click through colors
    Given Open Target product A-87800442 page
    Then Verify colors are clickable

  Scenario: Verify all product name, image show up in search result
    Given Open Target main page
    When Type search word easter bunny coffee mug into textbox
    When Click the search icon
    Then Verify product title and images shown


