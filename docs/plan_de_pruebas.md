# Plan de pruebas

## Alcance

El framework valida flujos principales del sitio Saucedemo y endpoints publicos de JSONPlaceholder.

## Objetivos

- Verificar flujos UI completos con Selenium.
- Validar escenarios positivos y negativos.
- Ejecutar pruebas API con distintos metodos HTTP.
- Generar reportes HTML, logs y capturas ante fallos.

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
| API-002 | GET | Validar post inexistente |
| API-003 | POST | Crear post |
| API-004 | DELETE | Eliminar post |

## Criterios de aceptacion

- Todas las pruebas deben ejecutarse de forma independiente.
- Los reportes deben mostrar estado y duracion.
- Los logs deben registrar pasos clave.
- Ante fallos UI debe generarse una captura en `screenshots/`.

