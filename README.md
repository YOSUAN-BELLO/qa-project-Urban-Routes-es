**Urban Routes — QA Automation (Sprint 8)**

Este repositorio contiene las pruebas automatizadas
desarrolladas para la aplicación **Urban Routes**.  
El objetivo de este proyecto es validar, mediante 
Selenium y pytest, el flujo principal de pedir un taxi: 
desde la configuración de la ruta y la selección de
tarifa, hasta el registro del teléfono, la adición de
un método de pago, el envío de mensajes al conductor
y la solicitud de servicios adicionales (manta, 
pañuelos, helados).

Objetivo: 
comprobar de forma fiable y repetible que las funcionalidades 
críticas del proceso de pedido de un viaje funcionan 
correctamente en la instancia de prueba de Urban Routes.
____________________________________________________________________

**Tecnologías y herramientas utilizadas:**

Este proyecto fue desarrollado utilizando un conjunto de 
herramientas y librerías modernas que permiten realizar 
pruebas automatizadas de extremo a extremo:

- Python 3.13 
Lenguaje de programación utilizado para implementar los 
scripts de prueba, gracias a su sintaxis clara y soporte 
de librerías de testing.
- Selenium WebDriver  
Biblioteca que permite la automatización de navegadores 
web. Se utilizó para interactuar con los elementos de la 
aplicación Urban Routes (campos de texto, botones, 
formularios, etc.).
- pytest 
Framework de testing en Python. Se utilizó para estructurar 
los casos de prueba, realizar las aserciones necesarias y 
generar reportes automáticos sobre los resultados.
- webdriver-manager 
Herramienta que gestiona automáticamente la instalación y 
actualización de los drivers de navegador (ChromeDriver en 
este caso), evitando la configuración manual.
- Google Chrome  
Navegador en el que se ejecutaron las pruebas automatizadas.
- PyCharm  
Entorno de desarrollo integrado (IDE) utilizado para 
programar, depurar y ejecutar las pruebas.  
_________________________________________________________________

**Instrucciones para ejecutar las pruebas**

Sigue estos pasos para poner en marcha el proyecto y ejecutar los tests automatizados:

1) Clonar el repositorio

git clone <URL-del-repositorio>
cd qa-project-Urban-Routes-es


2) (Opcional) Crear un entorno virtual

En Windows: python -m venv venv
venv\Scripts\activate

En macOS / Linux: python3 -m venv venv
source venv/bin/activate

3) Instalar dependencias

pip install -r requirements.txt


4) Iniciar el servidor de Urban Routes

Ingresa a tu cuenta de TripleTen y lanza el servidor.

Copia esta URL en el archivo data.py, en la variable urban_routes_url.

5) Ejecutar los tests

- Para ejecutar todos los tests:
pytest -v
- Para ejecutar un test específico:
pytest main.py::TestUrbanRoutes::test_set_route -v

6) (Opcional) Ejecutar pruebas desde PyCharm

- Abre el proyecto en PyCharm.
- Haz clic derecho sobre main.py o sobre una función de test.
- Selecciona Run 'pytest for main.py'.