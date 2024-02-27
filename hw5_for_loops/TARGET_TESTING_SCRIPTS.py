from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


BENEFIT_BOXES = (By.XPATH, "//img[contains(@class,'styles__BenefitCardImage')]")
LINK_BOXES = (By.XPATH, "//div[@class='grid_6']")
LINK_INFO_BOXES = (By.CSS_SELECTOR, "[class*=grid_4]")
BROWSE_TEXT = (By.XPATH, "//h2[text()='Browse all Help pages']")
CLICK_CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
CLICK_SIGN_IN = (By.XPATH, "//span[contains(@class,'styles__LinkText')]")
CLICK_ACCOUNT = (By.XPATH, "//span[text()='Sign in' and contains(@class,'styles__ListItemText')]")
SIGN_IN_AGREE_MSG = (By.XPATH, "//p[text()='By signing in, you agree to the following:']")
T_SHIRT_COLORS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
COLOR_VALUE = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")
SEARCH_ICON = (By.XPATH, "//button[contains(@class,'styles__SearchButton')]")
ADD_TO_CART = (By.XPATH, "//button[@id='addToCartButtonOrTextIdFor89130241']")
CANDLE_TEXT = (By.XPATH, "//div[text()='22oz Vanilla Cupcake Original Large Jar Candle - Yankee Candle']")
PRODUCT_EASTER_MUG = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
MUG_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
MUG_IMAGE = (By.XPATH, "//div[contains(@class,'ProductCardImage')]")


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(*CLICK_CART_ICON).click()
    context.wait.until(EC.element_to_be_clickable(CLICK_CART_ICON), message='cart icon not clicked')


@then("Verify {cart_empty_message} text displays")
def verify_cart_icon(context, cart_empty_message):
    assert context.driver.find_element(By.XPATH, "//h1[contains(@class,'styles__StyledHeading')]").is_displayed()


#--------------------------------------------------------
@when('Click on sign in icon')
def click_on_sign_in(context):
    context.wait.until(EC.element_to_be_clickable(CLICK_SIGN_IN), message='Sign in icon not clicked')
    context.driver.find_element(*CLICK_SIGN_IN).click()


@when('Click on Account sign in icon')
def click_on_account_sign_in(context):
    context.wait.until(EC.element_to_be_clickable(CLICK_ACCOUNT), message='Account sign 6 in icon not clicked')
    context.driver.find_element(*CLICK_ACCOUNT).click()
    #sleep(6)


@then('Verify {expected_sign_in_form} message displays accurately')
def verify_by_sign_in(context, expected_sign_in_form):
    context.wait.until(EC.presence_of_element_located(SIGN_IN_AGREE_MSG), message="Sign-in agreement message did not appear")
    actual_sign_in_form = context.driver.find_element(*SIGN_IN_AGREE_MSG).text
    assert expected_sign_in_form == actual_sign_in_form, f'Expected message {expected_sign_in_form} not in {actual_sign_in_form}'

#--------------------------------------------------------
@when("Type search word {product} into textbox")
def click_on_search_words(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    sleep(6) #leave in


@when("Click the search icon")#broken
def click_the_search_icon(context):
    context.wait.until(EC.element_to_be_clickable(SEARCH_ICON), message='search icon not clicked')
    context.driver.find_element(*SEARCH_ICON).click()
    #sleep(6)#wait needed here or test fails


#Doing how shown in class for this particular script, was getting
#    selenium.common.exceptions.ElementClickInterceptedException
#Found solution here:  https://testingbot.com/resources/articles/selenium-elementclickinterceptedexception
@when("Click Add to cart button")
def click_on_cart_button(context):
    add_to_cart_button = context.wait.until(EC.element_to_be_clickable(ADD_TO_CART), message='add to cart not clicked')
    context.driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
    context.driver.find_element(*ADD_TO_CART).click()


@when("Click on Pick Up button")
def click_on_pick_up_button(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label,'pickup')]")), message='Pick-up button not clicked')
    context.driver.find_element(By.XPATH, "//button[contains(@aria-label,'pickup')]").click()
    #sleep(6)


@when("Click Side Panel Add to Cart button")
def click_side_panel_add(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and contains(@aria-label,'Add to cart for 22oz')]")), message='Side Panel Add to Cart button not clicked')
    context.driver.find_element(By.XPATH, "//button[@type='button' and contains(@aria-label,'Add to cart for 22oz')]").click()
    #sleep(6)


@when("click on View cart & check out")
def click_on_view_cart_and_check_out(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='View cart & check out']")), message='View cart & check out button not clicked')
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    #sleep(6)


@then("Verify {expected_text} message is shown")
def verify_cart_and_check_out(context, expected_text):
    context.wait.until(EC.presence_of_element_located(CANDLE_TEXT), message='Message not shown')
    actual_text = context.driver.find_element(*CANDLE_TEXT).text
    assert expected_text == actual_text, f'Expected message {expected_text} not in {actual_text}'
    #sleep(6)

#========================================================================================
@given('Open Target circle page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify {box_amount} benefit boxes are shown')
def verify_5_benefit_boxes(context, box_amount):
    box_amount = int(box_amount)
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(benefit_boxes) == box_amount, f'Expected {box_amount} links, but got {len(benefit_boxes)}'

#---------------------------------------------------------------------------------------------
@given('Open Target help UI page')
def open_target_help_ui(context):
    context.driver.get('https://help.target.com/help')


@then('Verify {target_help} text is shown')
def verify_cart_and_check_out(context, target_help):
    actual_target_help = context.driver.find_element(By.XPATH, "//h2[@class='custom-h2']").text
    assert target_help == actual_target_help, f'Expected message {target_help} not in {actual_target_help}'


@then('Verify {link_help_boxes} link boxes are shown')
def verify_6_buttons(context, link_help_boxes):
    link_help_boxes = int(link_help_boxes)
    link_boxes = context.driver.find_elements(*LINK_BOXES)
    assert len(link_boxes) == link_help_boxes, f'Expected {link_help_boxes} links, but got {len(link_boxes)}'


@then('Verify {info_box} information boxes are shown')
def verify_info_buttons(context, info_box):
    info_box = int(info_box)
    link_info_boxes = context.driver.find_elements(*LINK_INFO_BOXES)
    assert len(link_info_boxes) == info_box, f'Expected {info_box} links, but got {len(link_info_boxes)}'


@then('Verify {expected_help_page_text} text is visible')
def verify_info_buttons(context, expected_help_page_text):
    actual_help_page_text = context.driver.find_element(*BROWSE_TEXT).text
    assert actual_help_page_text == expected_help_page_text, f'Expected {expected_help_page_text} not displayed'

#-------------------------------------------------------------------------
@given('Open Target product {t_shirt_id} page')
def open_product_page(context, t_shirt_id):
    context.driver.get('https://www.target.com/p/A-87800442')
    #sleep(6)


@then('Verify colors are clickable')
def verify_colors(context):
    expected_colors = ['Black', 'Blue', 'Dark Green', 'Light Pink', 'White']
    actual_colors = []

    colors = context.driver.find_elements(*T_SHIRT_COLORS)
    for color in colors:
        color.click()
        current_color = context.driver.find_element(*COLOR_VALUE).text
        current_color = current_color.split('\n')[1] #This will split 'Color\nBlue'] and take whats in position [1]
        if current_color in expected_colors:
            actual_colors.append(current_color)

    assert expected_colors == actual_colors, f'Expected {expected_colors} does not match {actual_colors}'


@then("Verify product title and images shown")
def verify_title_and_images(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(6)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    mug_info_array = context.driver.find_elements(*PRODUCT_EASTER_MUG)

    for mug in mug_info_array:
        mug_title = mug.find_element(*MUG_TITLE).text

        print('Title: ', mug_title)
        assert mug_title, 'Mug title not shown'
        #mug.find_element(*MUG_IMAGE)
        #print(mug_image)





