from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()

    task_link = 'https://stepik.org/lesson/181384/step/8?unit=156009'
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # говорим Selenium проверять в течение 13 секунд, пока число не станет равным 100
    button = WebDriverWait(browser, 13).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), "100"))

    # жмем бук
    book_button = browser.find_element_by_css_selector('button#book').click()

    # решаем задачу и жмем сабмит
    x_elem = browser.find_element_by_css_selector('span#input_value').text
    y = calc(x_elem)
    input_field = browser.find_element_by_css_selector('input.form-control').send_keys(y)
    submit_btn = browser.find_element_by_css_selector('#solve').click()

# !!!Дополнительно для Копирования ответа!!!
    # принимаем алерт и выделяем текст ответа
    alert = browser.switch_to.alert
    alert_text = alert.text
    answer_text = alert_text.split(':')[-1]

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # жмем ok
    alert.accept()

    # переходим на страницу задания
    browser.get(task_link)
    time.sleep(5)
    enter_btn = browser.find_element_by_css_selector('a#ember56').click()
    time.sleep(1)

    # вводим данные
    browser.find_element_by_css_selector("input[name='login']").send_keys('smittersan@gmail.com')
    browser.find_element_by_css_selector("input[name='password']").send_keys('ytzvbifvyt19')
    time.sleep(2)
    browser.find_element_by_css_selector(".sign-form__btn").click()
    time.sleep(1)

    #снова открываем таску и вводим полученные ранее данные
    browser.get(task_link)
    time.sleep(5)
    answer_input = browser.find_element_by_css_selector('textarea[autocorrect="off"]').send_keys(answer_text)
    send_btn = browser.find_element_by_css_selector('button.submit-submission').click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()