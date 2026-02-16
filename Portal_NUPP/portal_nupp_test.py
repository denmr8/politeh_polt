from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.fixture(scope="session")
def driver():
    # Створюємо драйвер один раз на всю сесію
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Закриваємо тільки в самому кінці всіх тестів
    driver.quit()

@pytest.fixture(scope="session")
def wait(driver):
    return WebDriverWait(driver, 15)


def test_portal_login(driver: WebDriver, wait):

    import os
    from dotenv import load_dotenv
    load_dotenv()
    user_val1 = os.getenv('LOGIN1')
    pass_val1 = os.getenv('PASSWORD1')
    
    driver.get('https://portal.nupp.edu.ua/')
    
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
    time.sleep(3)
    
# Очікуємо, що в URL з'явиться хоча б частина адреси порталу
    wait.until(EC.url_contains("portal.nupp.edu.ua"))
    assert "portal.nupp.edu.ua" in driver.current_url
    

def test_kabinet(driver: WebDriver, wait):
    
    KAB = (By.XPATH, "//a[contains(., 'Кабінет')]")
    kab = wait.until(EC.element_to_be_clickable(KAB)).click()

    INF=(By.XPATH, "//a[@href='/self/general-info']")
    inf_btn=wait.until(EC.visibility_of_element_located(INF)).click()
# Чекаємо конкретну частину URL
    wait.until(EC.url_contains("general-info"))
# Перевірка (assert)
    assert "general-info" in driver.current_url
    
    ROZKLAD=(By.XPATH, "//a[@href='/self/time-table']")
    inf_btn=wait.until(EC.visibility_of_element_located(ROZKLAD)).click()
    wait.until(EC.url_contains("time-table"))
    assert "time-table" in driver.current_url
    
    PLAN=("xpath", "//a[@href='/self/individual-plan']")
    plan=wait.until(EC.visibility_of_element_located(PLAN)).click()
    wait.until(EC.url_contains("individual-plan"))
    assert "individual-plan" in driver.current_url
    
    MSC=("xpath", "//a[@href='/self/attestations']")
    msc=wait.until(EC.visibility_of_element_located(MSC)).click()
    wait.until(EC.url_contains("attestations"))
    assert "attestations" in driver.current_url
    
    REZS=("xpath", "//a[@href='/self/exam-session']")
    rezs=wait.until(EC.visibility_of_element_located(REZS)).click()
    wait.until(EC.url_contains("exam-session"))
    assert "exam-session" in driver.current_url
    
    PSUCCS=("xpath", "//a[@href='/self/overall-performance']")
    psuccs=wait.until(EC.visibility_of_element_located(PSUCCS)).click()
    wait.until(EC.url_contains("overall-performance"))
    assert "overall-performance" in driver.current_url
    
    
def test_rozklad(driver: WebDriver, wait):
    RZKK = (By.XPATH, "//a[.//span[text()='Розклад']]")
    wait.until(EC.element_to_be_clickable(RZKK)).click()
    
    TEACHER=("xpath", "//a[@href='/time-table/teacher']")
    teacher=wait.until(EC.visibility_of_element_located(TEACHER)).click()
    wait.until(EC.url_contains("teacher"))
    assert "teacher" in driver.current_url
    
    ENTR=(By.XPATH, "//input[@id='searchteachersform-search']")
    entr=wait.until(EC.visibility_of_element_located(ENTR)).click()

    
    entr=driver.find_element("xpath","//input[@id='searchteachersform-search']")
    entr.click()
    entr.send_keys("Мирний")
    BTN=(By.XPATH, "//button[@type='submit']")
    btn=wait.until(EC.visibility_of_element_located(BTN)).click()
    
    BTN2=(By.XPATH, "//a[@href='/time-table/teacher?id=819']")
    btn2=wait.until(EC.visibility_of_element_located(BTN2)).click()
    
    wait.until(EC.url_contains("teacher?id=819"))
    assert "teacher?id=819" in driver.current_url
    
    
    ANNOUNCE = (By.XPATH, "//a[.//span[text()='Повідомлення']]")
    wait.until(EC.element_to_be_clickable(ANNOUNCE)).click()
    ANNOUNCE2=(By.XPATH, "//a[@href='/alert/informator' and @class='collapse-item']")
    informator_btn = wait.until(EC.presence_of_element_located(ANNOUNCE2))
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------
    driver.execute_script("arguments[0].click();", informator_btn)
    # wait.until(EC.element_to_be_clickable(ANNOUNCE2)).click()--------------------------------------------------------------------------------------------------------
    wait.until(EC.url_contains("informator"))
    assert "informator" in driver.current_url
    
    WORK_PLAN = (By.XPATH, "//a[.//span[text()='Робочий план']]")
    wait.until(EC.element_to_be_clickable(WORK_PLAN)).click()
    SPECI=(By.XPATH, "//a[@href='/workplan/speciality']")
    wait.until(EC.element_to_be_clickable(SPECI)).click()
    wait.until(EC.url_contains("speciality"))
    assert "speciality" in driver.current_url
    
    FACULTY=(By.XPATH, "//span[@id='select2-workplanform-facultyid-container']")
    wait.until(EC.element_to_be_clickable(FACULTY)).click()
    
    LIN=(By.XPATH, "//li[@id='select2-workplanform-facultyid-result-8epl-1']")
    LIN=(By.XPATH, "//li[contains(@class, 'select2-results__option') and contains(text(), 'Навчально-науковий інститут інформаційних технологій та робототехніки')]")
    lin=wait.until(EC.element_to_be_clickable(LIN)).click()

    KURS=(By.XPATH, "//span[@id='select2-workplanform-course-container']")
    wait.until(EC.element_to_be_clickable(KURS)).click()
    
    LIN2 = (By.XPATH, "//li[contains(@class, 'select2-results__option') and text()='2']")
    wait.until(EC.element_to_be_clickable(LIN2)).click()

    
    POTOK=(By.XPATH, "//span[@id='select2-workplanform-streamid-container']")
    wait.until(EC.element_to_be_clickable(POTOK)).click()
    
    LIN3 = (By.XPATH, "//li[contains(@class, 'select2-results__option') and text()='201-КБ, 202-КБ, 203-КБ']")
    wait.until(EC.element_to_be_clickable(LIN3)).click()    
    

    QUESTION = (By.XPATH, "//a[.//span[text()='Опитування']]")
    wait.until(EC.element_to_be_clickable(QUESTION)).click()
    QUES1=(By.XPATH, "//a[@href='/quiz-new/index']")
    wait.until(EC.element_to_be_clickable(QUES1)).click()
    wait.until(EC.url_contains("quiz-new/index"))
    assert "quiz-new/index" in driver.current_url

    
    DIST = (By.XPATH, "//a[.//span[text()='Дистанційна освіта']]")
    wait.until(EC.element_to_be_clickable(DIST)).click()
    DIST1=(By.XPATH, "//a[@href='https://dist.nupp.edu.ua/']")
    wait.until(EC.element_to_be_clickable(DIST1)).click()

    driver.switch_to.window(driver.window_handles[-1])
    
    wait.until(EC.url_contains("login/index.php"))
    assert "login/index.php" in driver.current_url
    
    driver.switch_to.window(driver.window_handles[-1])
    driver.switch_to.window(driver.window_handles[0])

    HMBTN=(By.XPATH, "//a[@class='nav-link' and @href='/']")
    hmbtn=wait.until(EC.visibility_of_element_located(HMBTN)).click()
    wait.until(EC.url_to_be("https://portal.nupp.edu.ua/"))
    assert driver.current_url == "https://portal.nupp.edu.ua/"
    time.sleep(3)
    
    EXIT1=(By.XPATH, "//a[@class='nav-link dropdown-toggle']")
    exit1=wait.until(EC.element_to_be_clickable(EXIT1)).click()
    EXIT=(By.XPATH, "//a[@href='/logout']")
    exit=wait.until(EC.element_to_be_clickable(EXIT)).click()
    wait.until(EC.url_to_be("https://portal.nupp.edu.ua/"))
    assert driver.current_url == "https://portal.nupp.edu.ua/"
    time.sleep(2)


















    
