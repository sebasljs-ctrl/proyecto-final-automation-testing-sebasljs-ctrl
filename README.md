# Proyecto Final - Automation Testing

Framework de automatizacion de pruebas desarrollado para la entrega final del curso de QA Automation.

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

El reporte muestra los tests ejecutados, estado, duracion y evidencia de fallos cuando corresponda.

## Evidencias

- Capturas de pantalla ante fallos: `screenshots/`
- Logs de ejecucion: `logs/test_execution.log`
- Reporte HTML: `reports/report.html`

## Datos de prueba

Los datos se leen desde archivos JSON ubicados en `data/`.

- `users.json`: usuarios validos e invalidos para Saucedemo
- `checkout_data.json`: informacion para el checkout
- `api_payloads.json`: datos para pruebas API

## GitHub Actions

El workflow ubicado en `.github/workflows/tests.yml` ejecuta las pruebas en cada `push` o `pull_request` y guarda reportes, logs y capturas como artefactos.

## Autor

GitHub: sebasljs-ctrl
