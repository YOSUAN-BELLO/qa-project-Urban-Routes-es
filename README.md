# 🚖 QA Project - Urban Routes  

## 📌 Descripción del Proyecto  
Este proyecto contiene **pruebas automatizadas** para la aplicación **Urban Routes**,  
una plataforma de solicitud de transporte.  

Las pruebas validan el **flujo completo de pedir un taxi**, incluyendo:  
✅ Selección de tarifas  
✅ Ingreso de información de contacto  
✅ Método de pago  
✅ Opciones adicionales del viaje  
✅ Confirmación y asignación de conductor  

## 🛠️ Tecnologías y Herramientas  

- 🐍 **Python 3.8+** → Lenguaje principal  
- 🌐 **Selenium WebDriver** → Automatización del navegador  
- 🧪 **Pytest** → Framework de testing  
- 🖥️ **ChromeDriver** → Driver para Chrome  

### 🧩 Técnicas de Testing  
- **Page Object Model (POM)** → Separación entre pruebas y UI  
- **Localizadores** → XPath, ID, Class Name  
- **Esperas (implícitas y explícitas)** → Manejo de carga de elementos  
- **Manejo de modales** → Interacción con ventanas dinámicas  
- **Validaciones** → Estados, clases CSS y contenidos en pantalla

## 📂 Estructura del Proyecto  

``bash
qa-project-Urban-Routes-es/
├── main.py          # Casos de prueba
├── pages.py         # Page Object Model
├── helpers.py       # Funciones auxiliares (ej: interceptar SMS)
├── data.py          # Datos de prueba
├── README.md        # Documentación del proyecto
└── requirements.txt # Dependencias

___

## ✅ Casos de Prueba Implementados

1 Configurar la dirección → Establecer origen y destino
2 Seleccionar tarifa Comfort
3 Rellenar el número de teléfono
4 Agregar tarjeta de crédito
5 Escribir mensaje al conductor
6 Solicitar manta y pañuelos
7 Pedir 2 helados
8 Confirmar búsqueda de taxi
9 Esperar información del conductor (con temporizador)

## ⚙️ Requisitos Previos

Python 3.8 o superior
Google Chrome
ChromeDriver (compatible con la versión de Chrome instalada)

## ▶️ Ejecución de Pruebas

🔹 Ejecutar todas las pruebas: pytest main.py 

## 🧪 Datos de Prueba

Definidos en data.py: 🌍 URL de la aplicación 🏠 Direcciones de origen y destino 
📞 Número de teléfono de prueba 💳 Datos de tarjeta de crédito 📝 Mensaje al conductor
⚠️ Notas Importantes 🔄 Las pruebas están diseñadas para ejecutarse en orden secuencial.
⏳ La prueba #9 incluye una espera de 45 segundos para simular la asignación real de conductor.
📲 El proyecto intercepta automáticamente los códigos de verificación SMS.
🌐 Requiere conexión estable a Internet.
🐞 Solución de Problemas

## Si encuentras errores:

Verifica que ChromeDriver esté instalado y sea compatible.
Confirma que las dependencias estén instaladas: pip install -r requirements.txt
Revisa que la aplicación esté accesible en la URL configurada.