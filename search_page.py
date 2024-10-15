from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.imdb.com/search/name/"
        window_height = self.driver.execute_script("return window.innerHeight;")
        self.driver.execute_script(f"window.scrollBy(0, {window_height / 2});")
    
    def load(self):
        self.driver.get(self.url)
    
    def fill_name_field(self, name):
        name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sc-6addea7c-0 jfSEAR")))
        name_input.click()
        name_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,'text-input__25123')))
        name_box.send_keys(name)
    def select_gender(self):
        gender_dropdown = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[7]/div[1]/label/span[1]/div")))
        gender_dropdown.click()

        gender_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[7]/div[2]/div/section/button[1]")))
        gender_btn.click()
        self.driver.execute_script("window.scrollBy(0, -1000);") 

    """
    def select_birth_month(self, month_value):
        birth_month_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "birth_month"))
        )
        birth_month_dropdown.send_keys(month_value)  # Provide month value like "1" for January

    def select_birth_day(self, day_value):
        birth_day_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "birth_day"))
        )
        birth_day_dropdown.send_keys(day_value)  # Provide day value like "1", "2", etc.

    def select_birth_year(self, year_value):
        birth_year_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "birth_year"))
        )
        birth_year_dropdown.send_keys(year_value)
    """

    def submit_search(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        submit_button.click()
