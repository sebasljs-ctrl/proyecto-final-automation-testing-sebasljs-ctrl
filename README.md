# proyecto-final-automation-testing-sebasljs-ctrl

Framework de automatizacion de pruebas desarrollado por `sebasljs-ctrl` para la entrega final del curso de QA Automation.

Repositorio publico:

```text
https://github.com/sebasljs-ctrl/proyecto-final-automation-testing-sebasljs-ctrl
```

## Sitios utilizados

- UI: https://www.saucedemo.com/
- API: https://jsonplaceholder.typicode.com/

## Tecnologias

- Python
- Pytest
- Selenium WebDriver
- Requests
- Pytest HTML
- Git y GitHub
- GitHub Actions

## Estructura del proyecto

```text
pages/              Page Object Model para las pantallas web
tests/ui/           Casos de prueba de interfaz
tests/api/          Casos de prueba de API
utils/              Configuracion, lectura de datos, driver y logging
data/               Datos externos JSON
reports/            Reportes HTML generados por pytest
screenshots/        Capturas automaticas ante fallos
logs/               Logs de ejecucion
.github/workflows/  Integracion continua con GitHub Actions
```

## Page Object Model

La automatizacion UI separa la logica de interaccion de la logica de validacion:

- `pages/`: contiene localizadores y acciones de cada pantalla.
- `tests/ui/`: contiene los flujos de prueba y assertions.
- `pages/base_page.py`: centraliza esperas explicitas, clicks, escritura de texto y lectura de elementos.

Clases principales:

- `LoginPage`: apertura del sitio, login y lectura de mensajes de error.
- `InventoryPage`: validacion de inventario, productos, filtro y carrito.
- `CartPage`: validacion del producto agregado y acceso a checkout.
- `CheckoutPage`: carga de datos de compra, finalizacion y mensaje de confirmacion.

## Instalacion

Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```powershell
python -m pip install -r requirements.txt
```

## Ejecucion de pruebas

La suite final se mantiene ajustada a lo necesario para la consigna:

- 5 casos UI con Selenium.
- 3 casos API con Requests.

Ejecutar todas las pruebas:

```powershell
python -m pytest
```

Ejecutar solo pruebas UI:

```powershell
python -m pytest -m ui
```

Ejecutar solo pruebas API:

```powershell
python -m pytest -m api
```

## Reportes

El reporte HTML se genera automaticamente en:

```text
reports/report.html
```

El reporte muestra tests ejecutados, estado, duracion y evidencia de fallos cuando corresponda.

## Evidencias

- Capturas ante fallos: `screenshots/`
- Logs de ejecucion: `logs/test_execution.log`
- Reporte HTML: `reports/report.html`

Las capturas se generan automaticamente desde `conftest.py` cuando falla una prueba UI. El nombre usa una etiqueta corta del test y fecha/hora compacta, como `checkout_20260706_173000.png`.

## Datos de prueba

Los datos se leen desde archivos JSON ubicados en `data/`.

- `users.json`: usuarios validos e invalidos para Saucedemo
- `checkout_data.json`: informacion para el checkout
- `api_payloads.json`: datos para pruebas API

## GitHub Actions

El workflow ubicado en `.github/workflows/tests.yml` ejecuta las pruebas en cada `push` o `pull_request` y guarda reportes, logs y capturas como artefactos.

## Control de versiones

El proyecto usa `main` como rama principal. Las mejoras se preparan en ramas cortas, se revisan localmente y luego se integran a `main` con commits simples y descriptivos.

## Autor

Usuario GitHub: `sebasljs-ctrl`
