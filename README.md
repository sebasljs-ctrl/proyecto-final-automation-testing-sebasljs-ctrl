# Proyecto final de Automation Testing

Proyecto final del curso de QA Automation.

Este proyecto es un conjunto de pruebas automatizadas hecho en Python. Incluye pruebas de interfaz con Selenium, pruebas de API con Requests, Page Object Model, datos externos, reportes, registros y ejecución automática con GitHub Actions.

## Repositorio público

```text
https://github.com/sebasljs-ctrl/proyecto-final-automation-testing-sebasljs-ctrl
```

## Sitios utilizados

Interfaz web: https://www.saucedemo.com/

API: https://jsonplaceholder.typicode.com/

## Tecnologías utilizadas

1. Python
2. Pytest
3. Selenium
4. Requests
5. Pytest HTML
6. Git
7. GitHub
8. GitHub Actions

## Estructura del proyecto

```text
pages/              Page Object Model de las pantallas web
tests/ui/           Pruebas de interfaz
tests/api/          Pruebas de API
utils/              Configuración, datos, navegador y registros
data/               Datos externos en formato JSON
reports/            Reportes HTML generados por Pytest
screenshots/        Capturas automáticas ante fallos
logs/               Registros de ejecución
scripts/            Atajos simples para ejecutar pruebas
.github/workflows/  Flujo automático de GitHub Actions
```

## Page Object Model

Las pruebas de interfaz están organizadas con Page Object Model. La idea es separar lo que hace la página de lo que valida cada prueba.

La carpeta `pages/` contiene los localizadores y las acciones de cada pantalla. La carpeta `tests/ui/` contiene los casos de prueba de interfaz. El archivo `pages/base_page.py` centraliza esperas, clicks, escritura de texto y lectura de elementos.

Clases principales:

1. `LoginPage` abre el sitio, realiza el inicio de sesión y valida mensajes de error.
2. `InventoryPage` valida inventario, productos, filtro y carrito.
3. `CartPage` valida el producto agregado y permite acceder al checkout.
4. `CheckoutPage` carga los datos de compra, finaliza el flujo y valida la confirmación.

## Instalación

Crear y activar el entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

También se pueden usar los atajos de `scripts/` para ejecutar las pruebas sin escribir comandos largos.

## Ejecución rápida

Desde PowerShell, ubicado en la carpeta del proyecto, se puede ejecutar todo con:

```powershell
.\scripts\ejecutar_todo.ps1
```

Para ejecutar solo las pruebas de interfaz:

```powershell
.\scripts\ejecutar_ui.ps1
```

Para ejecutar solo las pruebas de API:

```powershell
.\scripts\ejecutar_api.ps1
```

Para abrir el reporte:

```powershell
.\scripts\abrir_reporte.ps1
```

## Ejecución manual

La suite incluye 5 casos de prueba de interfaz con Selenium y 3 casos de prueba de API con Requests. También incluye escenarios positivos, escenarios negativos y datos de prueba leídos desde archivos externos.

Ejecutar todas las pruebas:

```powershell
python -m pytest
```

Ejecutar solo las pruebas de interfaz:

```powershell
python -m pytest -m ui
```

Ejecutar solo las pruebas de API:

```powershell
python -m pytest -m api
```

## Qué se prueba

La idea de la suite es simple: revisar un flujo real de compra en SauceDemo y probar tres operaciones básicas contra una API pública. No se agregaron casos de más; la suite queda chica, clara y fácil de ejecutar.

En `test_inicio_valido` se abre SauceDemo, se ingresan usuario y clave válidos desde `data/users.json`, y se revisa que el sitio llegue al inventario. También se valida que el título visible de la pantalla sea `Products`, porque ese texto confirma que el ingreso funcionó.

En `test_inicio_invalido` se prueban usuarios incorrectos desde `data/users.json`. La prueba revisa que SauceDemo muestre un mensaje de error. Este caso cubre el escenario negativo que pide la entrega.

En `test_productos` se inicia sesión y se revisa que el inventario esté disponible. La prueba valida que haya al menos un producto y que el filtro de ordenamiento esté visible.

En `test_carrito` se inicia sesión, se agrega el primer producto al carrito y se revisa que el contador marque `1`. Después se abre el carrito y se confirma que el producto agregado sea el mismo que aparece listado.

En `test_compra` se inicia sesión, se agrega un producto, se entra al carrito y se completa la compra con los datos de `data/checkout_data.json`. Al final se valida el mensaje real de SauceDemo: `Thank you for your order!`.

En `test_obtener_publicacion` se consulta un recurso existente en JSONPlaceholder y se revisa que responda `200`. También se consulta uno inexistente y se valida que responda `404`.

En `test_crear_publicacion` se envían los datos de `data/api_payloads.json` y se revisa que la API responda `201`. También se valida que el título, el contenido y el usuario vuelvan en la respuesta.

En `test_eliminar_publicacion` se elimina un recurso de prueba y se revisa que la API responda `200`.

## Pruebas de interfaz

Las pruebas de interfaz trabajan sobre SauceDemo y cubren inicio de sesión válido, inicio de sesión inválido, validación del inventario, agregado de producto al carrito y compra completa.

## Pruebas de API

Las pruebas de API trabajan sobre JSONPlaceholder. Validan respuestas, códigos HTTP y contenido JSON.

## Reportes

El reporte HTML se genera automáticamente en:

```text
reports/report.html
```

El reporte permite revisar las pruebas ejecutadas, su estado, duración y evidencia de fallos cuando corresponde.

## Evidencias

Las evidencias principales quedan en estas carpetas:

```text
screenshots/
logs/
reports/
```

Archivos principales:

```text
screenshots/           Capturas automáticas ante fallos de interfaz
logs/test_execution.log
reports/report.html
```

Las capturas se generan desde `conftest.py` cuando falla una prueba de interfaz. El nombre del archivo incluye el nombre del test y fecha/hora, por ejemplo `test_compra_20260706_183000.png`.

## Datos de prueba

Los datos se leen desde archivos JSON ubicados en `data/`.

```text
users.json             Usuarios válidos e inválidos para SauceDemo
checkout_data.json     Datos usados en la compra
api_payloads.json      Datos usados en las pruebas de API
```

## GitHub Actions

El flujo automático se encuentra en:

```text
.github/workflows/tests.yml
```

Se ejecuta en cada `push` o `pull_request` y guarda reportes, registros y capturas como evidencias.

## Control de versiones

El proyecto usa `main` como rama principal. Las mejoras se preparan en ramas cortas, se revisan localmente y luego se integran a `main` con commits simples.

## Autor

Usuario de GitHub: `sebasljs-ctrl`
