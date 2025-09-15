from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import helpers
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(driver, 10)

    # ---------------- LOCALIZADORES ----------------
#1 BOTONES DESDE Y HACIA
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
#2 Selecciona el contenedor padre del icono Comfort
    pedir_taxi_button = (By.XPATH, "//button[contains(text(),'Pedir un taxi')]")
    comfort_tariff = (By.XPATH, "//img[@alt='Comfort']/..")
#3 BOTON NUMERO DE TEFEFONO
    phone_option = (By.XPATH, "//div[text()='Número de teléfono']")
    phone_field = (By.ID, "phone")
    next_button = (By.XPATH, "//button[contains(text(), 'Siguiente')]")
    code_field = (By.ID, "code")
#4 NUMERO CARD
    payment_method_button = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]") #coregir
    add_card_button_modal = (By.XPATH, "//div[text()='Agregar tarjeta']")
    card_number_field = (By.ID, "number")
    card_code_field = (By.NAME, "code")
    confirm_add_card_button = (By.XPATH, "//button[@type='submit' and contains(text(), 'Agregar')]")
    confirm_phone_button = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")
#5 mensaje para el controlador
    message_field = (By.ID, "comment")
#6 Extras (manta y pañuelos → mismo switch)
    extras_checkbox = (By.XPATH, "//div[@class='switch']/span[@class='slider round']")
    extras_input = (By.XPATH, "//div[@class='switch']/input[@class='switch-input']")
#7
    ice_cream_plus = (By.CLASS_NAME, "counter-plus")  # botón +
    ice_cream_value = (By.CLASS_NAME, "counter-value")  # valor actual
#8
    modal_search_taxi = (By.XPATH, "/html/body/div/div/div[3]/div[4]/button")

#9
    details_button = (By.CLASS_NAME, "order-button")  # Botón de detalles (hamburguesa)
    #self.order_button = (By.CLASS_NAME, "order-button")


    # ---------------- MÉTODOS ----------------
    def set_route(self, address_from, address_to):
        self.driver.find_element(*self.from_field).send_keys(address_from)
        self.driver.find_element(*self.to_field).send_keys(address_to)
#1
    def click_pedir_taxi(self):
        self.driver.find_element(*self.pedir_taxi_button).click()
#2
    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff).click()
#3
    def fill_phone_number(self, phone):
        # Paso 1: abrir modal de teléfono
        self.driver.find_element(*self.phone_option).click()

        # Paso 2: ingresar número
        self.driver.find_element(*self.phone_field).send_keys(phone)

        # Paso 3: clic en botón "Siguiente"
        self.driver.find_element(*self.next_button).click()

        # Paso 4: obtener código interceptado con helpers
        code = helpers.retrieve_phone_code(self.driver)

        # Paso 5: escribir código si fue capturado
        if code:
            self.driver.find_element(*self.code_field).send_keys(code)
        # Paso 6: clic en "Confirmar"
        self.driver.find_element(*self.confirm_phone_button).click()

#4
    def add_card(self, card_number, card_code):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.payment_method_button)).click()
        # Paso 1: clic en "Metodo de pago"
        #self.driver.find_element(By.XPATH, "//div[text()='MEtodo de pago']").click()

        # Paso 2: clic en "Agregar tarjeta"
        self.driver.find_element(By.XPATH, "//div[text()='Agregar tarjeta']").click()

        # Paso 3: ingresar número de tarjeta
        self.driver.find_element(By.ID, "number").send_keys(card_number)

        # Paso 4: ingresar código de seguridad
        self.driver.find_element(By.NAME, "code").send_keys(card_code)

        # Paso 5: perder el enfoque (necesario para habilitar el botón)
        self.driver.find_element(By.ID, "number").click()  # clic fuera del campo CVV

        # Paso 6: clic en botón "Agregar"
        self.driver.find_element(By.XPATH, "//button[text()='Agregar']").click()

#5
    def write_message(self, message):
        self.driver.find_element(*self.message_field).send_keys(message)

#6
    def request_blanket_and_tissues(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.extras_checkbox))
        element.click()

        # Validar que el input quedó seleccionado
        checkbox = self.driver.find_element(*self.extras_input)
        assert checkbox.is_selected()

#7
    def request_two_ice_creams(self):
        wait = WebDriverWait(self.driver, 10)
        # Paso 1: hacer clic en el botón "+"
        plus_button = wait.until(EC.element_to_be_clickable(self.ice_cream_plus))
        plus_button.click()  # primer clic → de 1 a 2
        plus_button.click()
        # Paso 2: validar que el valor cambió a "2"
        value = wait.until(EC.visibility_of_element_located(self.ice_cream_value))
        return value.text

#8
    def click_modal_search_taxi(self):
        self.wait.until(EC.element_to_be_clickable(self.modal_search_taxi)).click()

#9
    def click_details_button(self):
        """Hace clic en el botón de detalles"""
        try:
            details_btn = self.wait.until(EC.element_to_be_clickable(self.details_button))
            details_btn.click()
            return True
        except Exception as e:
            print(f"Error al hacer clic en el botón de detalles: {e}")
            return False