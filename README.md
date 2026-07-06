# Proyecto final de Automation Testing

Proyecto final del curso de QA Automation.

El trabajo consiste en un framework de pruebas automatizadas desarrollado en Python. Incluye pruebas de interfaz con Selenium WebDriver, pruebas de API con Requests, uso de Page Object Model, datos externos, reportes, logs y ejecucion automatica con GitHub Actions.

## Repositorio publico

```text
https://github.com/sebasljs-ctrl/proyecto-final-automation-testing-sebasljs-ctrl
```

## Sitios utilizados

- UI: https://www.saucedemo.com/
- API: https://jsonplaceholder.typicode.com/

## Tecnologias utilizadas

- Python
- Pytest
- Selenium WebDriver
- Requests
- Pytest HTML
- Git
- GitHub
- GitHub Actions

## Estructura del proyecto

```text
pages/              Page Object Model de las pantallas web
tests/ui/           Pruebas de interfaz
tests/api/          Pruebas de API
utils/              Configuracion, datos, driver y logging
data/               Datos externos en formato JSON
reports/            Reportes HTML generados por Pytest
screenshots/        Capturas automaticas ante fallos
logs/               Logs de ejecucion
scripts/            Comandos simples para ejecutar pruebas
.github/workflows/  Workflow de GitHub Actions
```

## Page Object Model

Las pruebas de interfaz estan organizadas con Page Object Model para separar la interaccion con la pagina de las validaciones de cada test.

- `pages/` contiene los localizadores y acciones de cada pantalla
- `tests/ui/` contiene los casos de prueba de interfaz
- `pages/base_page.py` centraliza esperas explicitas, clicks, escritura de texto y lectura de elementos

Clases principales

- `LoginPage` abre el sitio, realiza el login y valida mensajes de error
- `InventoryPage` valida inventario, productos, filtro y carrito
- `CartPage` valida el producto agregado y permite acceder al checkout
- `CheckoutPage` carga los datos de compra, finaliza el flujo y valida la confirmacion

## Instalacion

Crear y activar el entorno virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

En esta PC el entorno ya esta creado en la carpeta anterior del proyecto. Por eso tambien se pueden usar los scripts de `scripts/` sin activar nada manualmente.

## Ejecucion rapida

Desde PowerShell, ubicado en la carpeta del proyecto:

```powershell
.\scripts\ejecutar_todo.ps1
```

Ejecutar solo pruebas UI

```powershell
.\scripts\ejecutar_ui.ps1
```

Ejecutar solo pruebas API

```powershell
.\scripts\ejecutar_api.ps1
```

Abrir el reporte

```powershell
.\scripts\abrir_reporte.ps1
```

## Ejecucion manual

La suite incluye

- 5 casos de prueba UI con Selenium
- 3 casos de prueba API con Requests
- Escenarios positivos y negativos
- Datos de prueba leidos desde archivos externos

Ejecutar todas las pruebas

```powershell
python -m pytest
```

Ejecutar solo las pruebas UI

```powershell
python -m pytest -m ui
```

Ejecutar solo las pruebas API

```powershell
python -m pytest -m api
```

## Pruebas UI

Las pruebas de interfaz trabajan sobre SauceDemo y cubren estos flujos

- Login valido
- Login invalido
- Validacion del inventario
- Agregado de producto al carrito
- Checkout completo

## Pruebas API

Las pruebas de API trabajan sobre JSONPlaceholder e incluyen validaciones de respuesta, codigos HTTP y contenido JSON.

## Reportes

El reporte HTML se genera automaticamente en

```text
reports/report.html
```

El reporte permite revisar los tests ejecutados, su estado, duracion y evidencia de fallos cuando corresponde.

## Evidencias

Las evidencias se guardan en estas carpetas

```text
screenshots/
logs/
reports/
```

Archivos principales

```text
screenshots/           Capturas automaticas ante fallos UI
logs/test_execution.log
reports/report.html
```

Las capturas se generan desde `conftest.py` cuando falla una prueba de interfaz. El nombre del archivo usa una etiqueta corta del test, por ejemplo `checkout.png` o `carrito.png`.

## Datos de prueba

Los datos se leen desde archivos JSON ubicados en `data/`.

```text
users.json             Usuarios validos e invalidos para SauceDemo
checkout_data.json     Datos usados en el checkout
api_payloads.json      Datos usados en las pruebas API
```

## GitHub Actions

El workflow se encuentra en

```text
.github/workflows/tests.yml
```

Se ejecuta en cada `push` o `pull_request` y guarda reportes, logs y capturas como artefactos.

## Control de versiones

El proyecto usa `main` como rama principal. Las mejoras se preparan en ramas cortas, se revisan localmente y luego se integran a `main` con commits simples.

## Autor

Usuario de GitHub: `sebasljs-ctrl`
