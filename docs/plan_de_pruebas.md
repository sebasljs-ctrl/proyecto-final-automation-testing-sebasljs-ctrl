# Plan de pruebas

## Alcance

El framework valida flujos principales del sitio Saucedemo y endpoints publicos de JSONPlaceholder.

## Objetivos

- Verificar flujos UI completos con Selenium.
- Validar escenarios positivos y negativos.
- Ejecutar pruebas API con distintos metodos HTTP.
- Generar reportes HTML, logs y capturas ante fallos.
- Evidenciar el uso de Page Object Model para separar tests e interacciones web.

## Estrategia Page Object Model

La logica de Selenium queda encapsulada en `pages/`. Cada clase representa una pantalla del flujo automatizado:

| Clase | Responsabilidad |
| --- | --- |
| LoginPage | Abrir Saucedemo, iniciar sesion y obtener errores de login |
| InventoryPage | Validar inventario, productos, filtro y carrito |
| CartPage | Validar producto agregado y avanzar a checkout |
| CheckoutPage | Completar datos, finalizar compra y validar confirmacion |

Los tests de `tests/ui/` usan estos metodos de pagina y mantienen solo el flujo de negocio y las assertions.

## Gestion de capturas

Las capturas automaticas se gestionan desde `conftest.py` con el hook `pytest_runtest_makereport`.

- Se generan solo ante fallos.
- Se guardan en `screenshots/`.
- El nombre incluye test, fecha y hora.
- Se adjuntan al reporte HTML cuando `pytest-html` esta disponible.

## Casos UI

| ID | Caso | Tipo |
| --- | --- | --- |
| UI-001 | Login valido redirige a inventario | Positivo |
| UI-002 | Login invalido muestra error | Negativo |
| UI-003 | Inventario muestra productos y filtro | Positivo |
| UI-004 | Agregar producto al carrito | Positivo |
| UI-005 | Checkout completo | Positivo |

## Casos API

| ID | Metodo | Caso |
| --- | --- | --- |
| API-001 | GET | Obtener post existente |
| API-002 | POST | Crear post |
| API-003 | DELETE | Eliminar post |

El caso API-001 valida tanto respuesta exitosa como respuesta de error para cubrir ambos escenarios sin agregar casos innecesarios.

## Criterios de aceptacion

- Todas las pruebas deben ejecutarse de forma independiente.
- Los reportes deben mostrar estado y duracion.
- Los logs deben registrar pasos clave.
- Ante fallos UI debe generarse una captura en `screenshots/`.
