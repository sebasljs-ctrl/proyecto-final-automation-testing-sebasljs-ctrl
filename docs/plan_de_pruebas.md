# Plan de pruebas

Este documento resume qué se prueba, cómo se prueba y qué evidencia queda en el proyecto. No agrega más automatizaciones; solo ordena la información para que la entrega sea clara.

## Alcance

El proyecto valida los flujos principales de SauceDemo y algunos endpoints públicos de JSONPlaceholder.

## Objetivos

El objetivo principal es comprobar que los flujos de interfaz funcionen correctamente con Selenium y que las pruebas de API respondan como se espera. También se busca dejar evidencia con reportes HTML, registros y capturas automáticas cuando una prueba de interfaz falle.

El proyecto usa Page Object Model para separar la lógica de interacción con la página de las validaciones de la prueba. Esto hace que los casos sean más fáciles de leer y mantener.

## Estrategia Page Object Model

La lógica de Selenium queda dentro de `pages/`. Cada clase representa una pantalla del flujo automatizado.

| Clase | Responsabilidad |
| --- | --- |
| LoginPage | Abre SauceDemo, inicia sesión y obtiene errores de ingreso |
| InventoryPage | Valida inventario, productos, filtro y carrito |
| CartPage | Valida el producto agregado y avanza a la compra |
| CheckoutPage | Completa datos, finaliza la compra y valida la confirmación |

Las pruebas de `tests/ui/` usan los métodos de esas páginas. Así muestran el flujo del usuario y no quedan llenas de selectores.

## Gestión de capturas

Las capturas automáticas se gestionan desde `conftest.py` con el hook `pytest_runtest_makereport`.

Se generan solo cuando falla una prueba de interfaz. Se guardan en `screenshots/`. El nombre incluye el test y fecha/hora, por ejemplo `test_compra_20260706_183000.png`. Cuando `pytest-html` está disponible, la captura también se adjunta al reporte HTML.

## Casos de interfaz

| ID | Caso | Tipo |
| --- | --- | --- |
| UI-001 | Inicio de sesión válido redirige a inventario | Positivo |
| UI-002 | Inicio de sesión inválido muestra error | Negativo |
| UI-003 | Inventario muestra productos y filtro | Positivo |
| UI-004 | Agregar producto al carrito | Positivo |
| UI-005 | Compra completa | Positivo |

## Casos de API

| ID | Método | Caso |
| --- | --- | --- |
| API-001 | GET | Obtener publicación existente |
| API-002 | POST | Crear publicación |
| API-003 | DELETE | Eliminar publicación |

El caso API-001 valida una respuesta exitosa y también una respuesta de error. Con eso se cubren ambos escenarios sin agregar casos innecesarios.

## Criterios de aceptación

Para considerar correcta la entrega, todas las pruebas deben poder ejecutarse de forma independiente. El reporte debe mostrar estado y duración de las pruebas. Los registros deben guardar pasos clave de ejecución. Si falla una prueba de interfaz, debe generarse una captura en `screenshots/`.
