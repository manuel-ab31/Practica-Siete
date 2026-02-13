# Sistema de Autenticación con PyQt5 - Patrón MVP

## Descripción

Aplicación de escritorio desarrollada en Python con PyQt5 que implementa un sistema de autenticación utilizando el patrón de diseño MVP (Model-View-Presenter). El proyecto demuestra la separación de responsabilidades y la arquitectura de software limpia.

## Características

- Interfaz gráfica de usuario desarrollada con PyQt5
- Implementación del patrón MVP para mejor separación de responsabilidades
- Sistema de autenticación con validación de credenciales
- Interfaz de inicio de sesión con opción de mostrar/ocultar contraseña
- Navegación entre vistas mediante QStackedWidget
- Validación de campos de entrada

## Estructura del Proyecto

```
practica7/
├── app.py                      # Punto de entrada de la aplicación
├── core/
│   └── app_shell.py           # Contenedor principal de vistas
├── presenters/
│   └── login_presenter.py     # Lógica de presentación del login
├── services/
│   └── auth_service.py        # Servicio de autenticación
└── ui/
    ├── login_view.py          # Vista de inicio de sesión
    └── main_view.py           # Vista principal después del login
```

## Patrón MVP

El proyecto sigue el patrón Model-View-Presenter:

- **Model:** `AuthService` - Maneja la lógica de autenticación
- **View:** `LoginView` y `MainView` - Interfaz de usuario sin lógica de negocio
- **Presenter:** `LoginPresenter` - Coordina la comunicación entre Model y View

## Requisitos

- Python 3.7 o superior
- PyQt5

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/manuel-ab31/Practica-Siete.git
cd Practica-Siete
```

2. Instalar las dependencias:
```bash
pip install PyQt5
```

## Uso

Para ejecutar la aplicación:

```bash
python app.py
```

### Credenciales por Defecto

- Usuario: `admin`
- Contraseña: `1234`

## Funcionalidades Implementadas

### Vista de Login
- Campo de usuario
- Campo de contraseña con modo de ocultación
- Botón para mostrar/ocultar contraseña
- Validación de campos vacíos
- Mensajes de error en caso de credenciales incorrectas
- Soporte para tecla Enter para enviar formulario

### Vista Principal
- Mensaje de bienvenida personalizado
- Confirmación de inicio de sesión exitoso

## Arquitectura

### AppShell
Contenedor principal que administra la navegación entre vistas utilizando `QStackedWidget`. Coordina la inicialización de servicios, presentadores y vistas.

### AuthService
Servicio encargado de la validación de credenciales. Actualmente implementa validación estática, pero está diseñado para ser fácilmente extensible a bases de datos o APIs externas.

### LoginPresenter
Actúa como intermediario entre `LoginView` y `AuthService`, manejando la lógica de presentación y coordinando las acciones del usuario.

## Extensibilidad

El diseño modular permite:
- Reemplazar fácilmente el `AuthService` con implementaciones que consulten bases de datos o APIs
- Agregar nuevas vistas y presentadores sin modificar el código existente
- Implementar validaciones adicionales de forma centralizada

## Autor

Manuel Arías
- GitHub: [@manuel-ab31](https://github.com/manuel-ab31)
- Email: l23030839@celaya.tecnm.mx

## Licencia

Proyecto académico desarrollado para la materia de Tópicos Avanzados de Programación.
