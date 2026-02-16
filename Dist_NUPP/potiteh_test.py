from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

def test_dist_portal():
    
    driver=webdriver.Chrome()
    driver.maximize_window()
    wait=WebDriverWait(driver ,10)
    import os
    from dotenv import load_dotenv

    load_dotenv()
    
    driver.get('https://nupp.edu.ua/page/studentovi.html')

    user_val = os.getenv('LOGIN')
    pass_val = os.getenv('PASSWORD')
    
    BOX2 = (By.XPATH, "//a[@href='http://dist.nupp.edu.ua/']")
    element = wait.until(EC.presence_of_element_located(BOX2))
    driver.execute_script("arguments[0].click();", element)
    
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    
    name_login=(By.ID,"username")
    user=wait.until(EC.element_to_be_clickable(name_login))
    user.send_keys(user_val)
    
    pass_login=(By.ID,'password')
    pasword=wait.until(EC.element_to_be_clickable(pass_login))
    pasword.send_keys(pass_val)
    
    log_btn=(By.ID,'loginbtn')
    btn_login=wait.until(EC.element_to_be_clickable(log_btn))
    btn_login.click()
    
    # driver.quit()
    
    
    ICON=(By.XPATH, "//a[@id='user-menu-toggle']")
    icon=wait.until(EC.element_to_be_clickable(ICON)).click()
    
    USER_PROFILE=(By.XPATH, "//a[@href='https://dist.nupp.edu.ua/user/profile.php']")
    user_profile=wait.until(EC.visibility_of_element_located(USER_PROFILE)).click()
    wait.until(EC.url_contains("profile.php"))
    assert "profile.php" in driver.current_url
    # time.sleep(3)
    
    icon=wait.until(EC.element_to_be_clickable(ICON)).click()
    
    MARKS=(By.XPATH, "//a[@href='https://dist.nupp.edu.ua/grade/report/overview/index.php']")
    marks=wait.until(EC.visibility_of_element_located(MARKS)).click()
    wait.until(EC.url_contains("grade/report/overview/index.php"))
    assert "grade/report/overview/index.php" in driver.current_url
    
    icon=wait.until(EC.element_to_be_clickable(ICON)).click()
    
    KALENDAR=(By.XPATH, "//a[@href='https://dist.nupp.edu.ua/calendar/view.php?view=month']")
    kalendar=wait.until(EC.visibility_of_element_located(KALENDAR)).click()
    wait.until(EC.url_contains("view.php?view=month"))
    assert "view.php?view=month" in driver.current_url
    
    icon=wait.until(EC.element_to_be_clickable(ICON)).click()
    
    MESSAGE=(By.XPATH, "//a[@href='https://dist.nupp.edu.ua/message/index.php']")
    message=wait.until(EC.visibility_of_element_located(MESSAGE)).click()
    wait.until(EC.url_contains("message/index.php"))
    assert "message/index.php" in driver.current_url
    
    icon=wait.until(EC.element_to_be_clickable(ICON)).click()
    
    OWN_FILES=(By.XPATH, "//a[@href='https://dist.nupp.edu.ua/user/files.php']")
    own_files=wait.until(EC.visibility_of_element_located(OWN_FILES)).click()
    wait.until(EC.url_contains("files.php"))
    assert "files.php" in driver.current_url
    
    icon=wait.until(EC.element_to_be_clickable(ICON)).click()
    
    REPORTS=(By.XPATH, "//a[@href='https://dist.nupp.edu.ua/reportbuilder/index.php']")
    reports=wait.until(EC.visibility_of_element_located(REPORTS)).click()
    wait.until(EC.url_contains("reportbuilder/index.php"))
    assert "reportbuilder/index.php" in driver.current_url
    
    icon=wait.until(EC.element_to_be_clickable(ICON)).click()
    
    LIKES=(By.XPATH, "//a[@href='https://dist.nupp.edu.ua/user/preferences.php']")
    likes=wait.until(EC.visibility_of_element_located(LIKES)).click()
    wait.until(EC.url_contains("user/preferences.php"))
    assert "user/preferences.php" in driver.current_url
    
    icon=wait.until(EC.element_to_be_clickable(ICON)).click()
    
    LANGUAGE=(By.XPATH, "//a[@class='carousel-navigation-link dropdown-item']")
    language=wait.until(EC.visibility_of_element_located(LANGUAGE)).click()
    RU_LANGUAGE=(By.XPATH, "//a[@href='https://dist.nupp.edu.ua/user/preferences.php?userid=30811&lang=ru']")
    ru_language=wait.until(EC.visibility_of_element_located(RU_LANGUAGE)).click()
    wait.until(EC.url_contains("lang=ru"))
    assert "lang=ru" in driver.current_url
    
    icon=wait.until(EC.element_to_be_clickable(ICON)).click()
    
    language=wait.until(EC.visibility_of_element_located(LANGUAGE)).click()
    UA_LANGUAGE=(By.XPATH, "//a[@href='https://dist.nupp.edu.ua/user/preferences.php?userid=30811&lang=uk']")
    ua_language=wait.until(EC.visibility_of_element_located(UA_LANGUAGE)).click()
    wait.until(EC.url_contains("lang=uk"))
    assert "lang=uk" in driver.current_url
    
    icon=wait.until(EC.element_to_be_clickable(ICON)).click()
    
    EXIT=(By.XPATH, "//a[contains(text(),  'Вийти')]")
    exit=wait.until(EC.visibility_of_element_located(EXIT)).click()
    wait.until(EC.url_contains("login/index.php"))
    assert "login/index.php" in driver.current_url
    
    
def test_portal_login():
    driver=webdriver.Chrome()
    driver.maximize_window()
    wait=WebDriverWait(driver ,10)
    
    import os
    from dotenv import load_dotenv

    load_dotenv()
    
    driver.get('https://nupp.edu.ua/page/studentovi.html')
     
    user_val1 = os.getenv('LOGIN1')
    pass_val1 = os.getenv('PASSWORD1') 
     
    # time.sleep(2)
    BOX2=(By.XPATH,"//a[@href='/page/rozklad.html']")
    box2=wait.until(EC.visibility_of_element_located(BOX2))
    driver.execute_script("arguments[0].click();", box2)
    # time.sleep(2)
    BOX3 = (By.XPATH, "//a[@href='https://portal.nupp.edu.ua/']")
    box3_el = wait.until(EC.presence_of_element_located(BOX3))
    driver.execute_script("arguments[0].click();", box3_el)
    # time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    AUTHORIZATION=(By.XPATH,"//a[contains(text(), 'Авторизація')]")
    autorization=wait.until(EC.visibility_of_element_located(AUTHORIZATION)).click()
    
    AUT2=("xpath","//a[contains(text(), 'Увійти')]")
    autorization2=wait.until(EC.visibility_of_element_located(AUT2)).click()
    
    login=driver.find_element("xpath","//input[@id='loginform-username']")
    login.click()
    login.send_keys(user_val1)
    
    passw=driver.find_element("xpath","//input[@id='loginform-password']")
    passw.click()
    passw.send_keys(pass_val1) 
    
    BTN= ("xpath", "//button[contains(text(),  'Увійти')]")
    btn=wait.until(EC.visibility_of_element_located(BTN)).click()
    
    time.sleep(1)
    driver.quit()
    
    
# def test_positive_login():
    
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     wait=WebDriverWait(driver ,10)

#     driver.get('https://portal.nupp.edu.ua/self/general-info')
#     print(driver.current_url)
    
    