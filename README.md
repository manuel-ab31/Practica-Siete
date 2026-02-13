# Sistema de Autenticación con PyQt5 - Patrón MVP

## Descripción

Aplicación de escritorio desarrollada en Python con PyQt5 que implementa un sistema de autenticación utilizando el patrón de diseño MVP (Model-View-Presenter). El proyecto demuestra la separación de responsabilidades y la arquitectura de software limpia.

## Características

- Interfaz gráfica de usuario desarrollada con PyQt5
- Implementación del patrón MVP para mejor separación de responsabilidades
- Sistema de autenticación multi-rol con validación de credenciales
- Tres tipos de usuarios con vistas dedicadas: Administrador, Estudiante y Docente
- Interfaz de inicio de sesión con opción de mostrar/ocultar contraseña
- Navegación dinámica entre vistas mediante QStackedWidget según el rol del usuario
- Validación de campos de entrada

## Estructura del Proyecto

```
practica7/
├── app.py                      # Punto de entrada de la aplicación
├── core/
│   └── app_shell.py           # Contenedor principal de vistas con enrutamiento por rol
├── presenters/
│   └── login_presenter.py     # Lógica de presentación del login
├── services/
│   └── auth_service.py        # Servicio de autenticación multi-rol
└── ui/
    ├── login_view.py          # Vista de inicio de sesión
    ├── main_view.py           # Vista principal para administradores
    ├── student_view.py        # Vista dedicada para estudiantes
    └── teacher_view.py        # Vista dedicada para docentes
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

Todos los usuarios comparten la misma contraseña:

- **Contraseña:** `1234`

**Usuarios disponibles:**
- Usuario: `admin` - Accede al panel de administrador
- Usuario: `estudiante` - Accede al portal de estudiantes
- Usuario: `maestro` - Accede al portal de docentes

## Funcionalidades Implementadas

### Vista de Login
- Campo de usuario
- Campo de contraseña con modo de ocultación
- Botón para mostrar/ocultar contraseña
- Validación de campos vacíos
- Mensajes de error en caso de credenciales incorrectas
- Soporte para tecla Enter para enviar formulario

### Panel de Administrador
- Vista dedicada para usuarios tipo administrador
- Mensaje de bienvenida personalizado
- Confirmación de inicio de sesión exitoso

### Panel de Estudiante
- Vista dedicada para usuarios tipo estudiante
- Interfaz personalizada con información relevante para estudiantes
- Mensaje de bienvenida personalizado

### Panel de Docente
- Vista dedicada para usuarios tipo docente
- Interfaz personalizada con información relevante para docentes
- Mensaje de bienvenida personalizado

## Arquitectura

### AppShell
Contenedor principal que administra la navegación entre vistas utilizando `QStackedWidget`. Coordina la inicialización de servicios, presentadores y vistas, enrutando dinámicamente a la vista correspondiente según el tipo de usuario autenticado.

### AuthService
Servicio encargado de la validación de credenciales multi-rol. Valida tres tipos de usuarios (admin, estudiante, maestro) con una contraseña compartida. Está diseñado para ser fácilmente extensible a bases de datos o APIs externas.

### LoginPresenter
Actúa como intermediario entre `LoginView` y `AuthService`, manejando la lógica de presentación y coordinando las acciones del usuario. Procesa el tipo de usuario autenticado y delega el enrutamiento al `AppShell`.

## Extensibilidad

El diseño modular permite:
- Reemplazar fácilmente el `AuthService` con implementaciones que consulten bases de datos o APIs
- Agregar nuevos roles de usuario y sus vistas correspondientes sin modificar el código existente
- Implementar validaciones adicionales de forma centralizada
- Extender las vistas específicas de cada rol con funcionalidades propias

## Autor

Manuel Arías
- GitHub: [@manuel-ab31](https://github.com/manuel-ab31)
- Email: l23030839@celaya.tecnm.mx

## Licencia

Proyecto académico desarrollado para la materia de Tópicos Avanzados de Programación.
