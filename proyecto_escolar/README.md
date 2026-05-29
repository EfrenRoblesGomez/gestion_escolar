# Sistema Web Escolar - Gestión Académica

## Descripción General

Sistema web desarrollado con Flask para la administración académica de una institución educativa. El proyecto permite gestionar alumnos, grupos, materias, docentes, planeaciones y calificaciones desde una interfaz web estructurada y modular.

El sistema implementa:

* Autenticación de usuarios.
* Gestión académica completa.
* Panel administrativo con estadísticas.
* CRUDs para entidades principales.
* Relación entre alumnos, docentes, materias y grupos.
* Registro de calificaciones.
* Organización modular mediante Blueprints.
* ORM con SQLAlchemy.
* Plantillas HTML usando Jinja2.
* Configuración mediante variables de entorno.

---

# Tecnologías Utilizadas

## Backend

* Python 3.8+
* Flask 3.x
* Flask-SQLAlchemy
* SQLAlchemy 2.x
* Werkzeug
* PyMySQL
* python-dotenv

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

## Base de Datos

* MySQL 8+
* SQLite (instancia local incluida para pruebas)

---

# Arquitectura del Proyecto

```text
proyecto_escolar/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── __init__.py
│
├── database/
├── diagramas/
├── instance/
├── sql/
├── config.py
├── run.py
├── requirements.txt
├── README.md
└── .env.example
```

---

# Estructura Completa del Proyecto

## Carpeta `app/`

Contiene toda la lógica principal de la aplicación.

### `app/models/`

Define las entidades y tablas de la base de datos mediante SQLAlchemy.

Archivos:

* `usuario.py`
* `turno.py`
* `grupo.py`
* `materia.py`
* `docente.py`
* `alumno.py`
* `planeacion.py`
* `calificacion.py`

### `app/routes/`

Contiene las rutas HTTP organizadas mediante Blueprints.

Archivos:

* `auth.py`
* `dashboard.py`
* `alumnos.py`
* `grupos.py`
* `materias.py`
* `docentes.py`
* `planeacion.py`
* `calificaciones.py`

### `app/templates/`

Plantillas HTML renderizadas por Flask.

Subdirectorios:

* `auth/`
* `dashboard/`
* `alumnos/`
* `grupos/`
* `materias/`
* `docentes/`
* `planeacion/`
* `calificaciones/`

### `app/static/`

Archivos estáticos.

Contiene:

* CSS
* JavaScript
* estilos globales
* scripts de interacción

---

# Archivo `run.py`

Punto de entrada principal del sistema.

## Funcionalidad

* Inicializa la aplicación Flask.
* Obtiene variables de entorno.
* Configura host, puerto y modo debug.
* Ejecuta el servidor web.

## Código Principal

```python
from app import create_app
import os

if __name__ == '__main__':
    app = create_app()

    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '127.0.0.1')
    debug = os.environ.get('FLASK_DEBUG', True)

    app.run(host=host, port=port, debug=debug)
```

## Variables Utilizadas

| Variable    | Descripción                 |
| ----------- | --------------------------- |
| PORT        | Puerto del servidor         |
| HOST        | Dirección IP del servidor   |
| FLASK_DEBUG | Activa/desactiva modo debug |

---

# Archivo `config.py`

Contiene la configuración global del sistema.

## Funcionalidades

* Carga variables de entorno.
* Configura la base de datos.
* Configura cookies de sesión.
* Define SECRET_KEY.

## Clase Principal

```python
class Configuracion:
```

## Variables Configuradas

| Variable                       | Descripción                        |
| ------------------------------ | ---------------------------------- |
| SECRET_KEY                     | Clave de seguridad de Flask        |
| SQLALCHEMY_DATABASE_URI        | URL de conexión a la base de datos |
| SQLALCHEMY_TRACK_MODIFICATIONS | Desactiva seguimiento innecesario  |
| SESSION_COOKIE_HTTPONLY        | Protege cookies                    |
| SESSION_COOKIE_SAMESITE        | Política SameSite                  |

---

# Archivo `app/__init__.py`

Inicializa la aplicación Flask.

## Responsabilidades

* Crear instancia Flask.
* Inicializar SQLAlchemy.
* Cargar configuración.
* Registrar Blueprints.
* Importar modelos.
* Crear tablas automáticamente.

## Blueprints Registrados

| Blueprint      | Función                  |
| -------------- | ------------------------ |
| auth           | Autenticación            |
| dashboard      | Panel principal          |
| alumnos        | CRUD alumnos             |
| grupos         | CRUD grupos              |
| materias       | CRUD materias            |
| docentes       | CRUD docentes            |
| planeacion     | Planeaciones académicas  |
| calificaciones | Registro de evaluaciones |

---

# Modelos de Base de Datos

## Modelo `Usuario`

Archivo:

```text
app/models/usuario.py
```

## Campos

| Campo          | Tipo     | Descripción            |
| -------------- | -------- | ---------------------- |
| id             | Integer  | ID principal           |
| nombre         | String   | Nombre del usuario     |
| apellido       | String   | Apellido               |
| email          | String   | Correo único           |
| password       | String   | Contraseña hasheada    |
| rol            | String   | Rol del usuario        |
| activo         | Boolean  | Estado activo/inactivo |
| ultimo_login   | DateTime | Último acceso          |
| creado_en      | DateTime | Fecha creación         |
| actualizado_en | DateTime | Fecha actualización    |

## Métodos

### `set_password(password)`

Genera hash seguro de contraseña.

### `check_password(password)`

Verifica contraseñas.

### `to_dict()`

Serializa el objeto.

---

## Modelo `Alumno`

Archivo:

```text
app/models/alumno.py
```

## Campos

| Campo          | Tipo       |
| -------------- | ---------- |
| id             | Integer    |
| matricula      | String     |
| nombre         | String     |
| apellido       | String     |
| grupo_id       | ForeignKey |
| activo         | Boolean    |
| creado_en      | DateTime   |
| actualizado_en | DateTime   |

## Relaciones

* Relación con `Grupo`.
* Relación con `Calificacion`.

## Métodos

### `nombre_completo()`

Retorna nombre y apellido concatenados.

### `promedio()`

Calcula promedio automático del alumno.

### `to_dict()`

Convierte datos a diccionario serializable.

---

## Modelo `Calificacion`

Archivo:

```text
app/models/calificacion.py
```

## Campos

| Campo          | Tipo       |
| -------------- | ---------- |
| id             | Integer    |
| alumno_id      | ForeignKey |
| planeacion_id  | ForeignKey |
| docente_id     | ForeignKey |
| valor          | Float      |
| tipo           | String     |
| fecha          | Date       |
| comentarios    | Text       |
| creado_en      | DateTime   |
| actualizado_en | DateTime   |

## Tipos de Calificación

* Parcial
* Final
* Tarea
* Participación

## Métodos

### `estado()`

Determina si el alumno aprobó o reprobó.

### `to_dict()`

Serializa datos.

---

## Modelo `Grupo`

Responsable de agrupar alumnos por:

* Semestre
* Turno
* Grupo

Relaciones:

* Uno a muchos con alumnos.
* Relación con planeaciones.

---

## Modelo `Materia`

Gestiona:

* Nombre de materia.
* Créditos.
* Horas.
* Planeaciones.

---

## Modelo `Docente`

Gestiona:

* Información del maestro.
* Especialidad.
* Relaciones con planeaciones.
* Relación con calificaciones.

---

## Modelo `Planeacion`

Relaciona:

* Materias.
* Docentes.
* Grupos.

Permite estructurar actividades académicas.

---

## Modelo `Turno`

Representa:

* Matutino.
* Vespertino.
* Nocturno.

---

# Sistema de Autenticación

Archivo:

```text
app/routes/auth.py
```

## Funcionalidades

* Login.
* Logout.
* Registro de usuarios.
* Manejo de sesiones.
* Validación de credenciales.
* Hash de contraseñas.

## Rutas

| Ruta           | Método   | Función           |
| -------------- | -------- | ----------------- |
| /auth/login    | GET/POST | Inicio de sesión  |
| /auth/logout   | GET      | Cerrar sesión     |
| /auth/register | GET/POST | Registro usuarios |

## Variables de Sesión

| Variable       | Descripción    |
| -------------- | -------------- |
| usuario_id     | ID del usuario |
| usuario_email  | Correo         |
| usuario_rol    | Rol            |
| usuario_nombre | Nombre         |

---

# Dashboard

Archivo:

```text
app/routes/dashboard.py
```

## Funcionalidades

* Estadísticas generales.
* Conteo de entidades.
* Promedio general.
* Detección de bajo rendimiento.
* Protección de rutas.

## Decoradores

### `login_required`

Restringe acceso a usuarios autenticados.

### `admin_required`

Restringe acceso a administradores.

## Estadísticas Generadas

* Total alumnos.
* Total grupos.
* Total materias.
* Total calificaciones.
* Promedio general.
* Alumnos con promedio menor a 7.

---

# CRUDs Implementados

## Gestión de Alumnos

Funciones:

* Crear alumnos.
* Editar alumnos.
* Eliminar alumnos.
* Ver detalles.
* Listar alumnos.
* Calcular promedio.

## Gestión de Grupos

Funciones:

* Crear grupos.
* Modificar grupos.
* Eliminar grupos.
* Ver alumnos asignados.

## Gestión de Materias

Funciones:

* Registrar materias.
* Actualizar información.
* Eliminar materias.
* Asociar planeaciones.

## Gestión de Docentes

Funciones:

* Registro de docentes.
* Especialidades.
* Asignaciones.

## Gestión de Calificaciones

Funciones:

* Registrar calificaciones.
* Actualizar evaluaciones.
* Historial académico.
* Estados aprobado/reprobado.

---

# Sistema de Plantillas

El proyecto utiliza Jinja2.

## Archivo Base

```text
app/templates/base.html
```

Sirve como plantilla principal.

## Beneficios

* Reutilización de componentes.
* Menús compartidos.
* Estructura uniforme.
* Reducción de código duplicado.

---

# Base de Datos

## Scripts SQL

Ubicación:

```text
/database/schema.sql
/sql/schema.sql
```

## Contenido

* Creación de tablas.
* Relaciones.
* Llaves foráneas.
* Restricciones.
* Datos iniciales.

---

# Diagramas

La carpeta `diagramas/` contiene:

| Archivo          | Descripción              |
| ---------------- | ------------------------ |
| arquitectura.png | Arquitectura del sistema |
| casos_uso.png    | Casos de uso             |
| modelo_er.png    | Modelo entidad-relación  |

---

# Instalación Completa

## 1. Clonar proyecto

```bash
git clone <repositorio>
cd proyecto_escolar
```

---

## 2. Crear entorno virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Dependencias Principales

| Dependencia      | Uso                 |
| ---------------- | ------------------- |
| Flask            | Framework web       |
| Flask-SQLAlchemy | Integración ORM     |
| SQLAlchemy       | Manejo BD           |
| PyMySQL          | Driver MySQL        |
| Werkzeug         | Seguridad y hashing |
| python-dotenv    | Variables entorno   |

---

# Configuración del Entorno

## Archivo `.env`

Ejemplo:

```env
DATABASE_URL=mysql+pymysql://usuario:password@localhost:3306/control_escolar
SECRET_KEY=clave_super_secreta
FLASK_ENV=development
FLASK_DEBUG=True
HOST=127.0.0.1
PORT=5000
```

---

# Crear Base de Datos

## MySQL

```bash
mysql -u root -p < database/schema.sql
```

---

# Ejecutar Aplicación

```bash
python run.py
```

Servidor disponible en:

```text
http://127.0.0.1:5000
```

---

# Seguridad Implementada

## Contraseñas

* Hash mediante Werkzeug.
* Verificación segura.
* Contraseñas no almacenadas en texto plano.

## Sesiones

* Cookies HttpOnly.
* SameSite configurado.
* Variables protegidas.

## Acceso

* Protección mediante decoradores.
* Validación de usuarios activos.
* Restricción por roles.

---

# Roles del Sistema

## Administrador

Permisos:

* Acceso completo.
* Registro de usuarios.
* Administración total.

## Docente

Permisos:

* Gestión académica.
* Registro de calificaciones.
* Consulta de grupos.

## Control Escolar

Permisos:

* Gestión de alumnos.
* Administración de grupos.
* Control académico.

---

# Relaciones Principales

## Alumno

* Pertenece a un grupo.
* Tiene muchas calificaciones.

## Grupo

* Tiene muchos alumnos.
* Tiene planeaciones.

## Planeación

Relaciona:

* Grupo.
* Materia.
* Docente.

## Calificación

Pertenece a:

* Alumno.
* Planeación.
* Docente.

---

# Funciones Importantes

## Promedio Automático

Implementado en:

```python
Alumno.promedio()
```

Calcula promedio dinámicamente.

---

## Estado de Calificación

Implementado en:

```python
Calificacion.estado()
```

Retorna:

* Aprobado.
* Reprobado.

---

# Ventajas del Proyecto

* Arquitectura modular.
* Separación clara de responsabilidades.
* Escalable.
* Fácil mantenimiento.
* ORM robusto.
* Integración sencilla con MySQL.
* Seguridad básica implementada.
* CRUDs completos.
* Uso de Blueprints.

---

# Posibles Mejoras Futuras

* API REST.
* JWT.
* Roles avanzados.
* Exportación PDF/Excel.
* Reportes gráficos.
* Notificaciones.
* Recuperación de contraseña.
* Auditoría de cambios.
* Logs del sistema.
* Dockerización.
* Tests automatizados.
* CI/CD.

---

# Recomendaciones Técnicas

## Producción

No usar:

```python
debug=True
```

en producción.

## Seguridad

Cambiar:

* SECRET_KEY.
* Credenciales de base de datos.
* Usuario administrador inicial.

## Base de Datos

* Implementar migraciones.
* Respaldos automáticos.
* Índices optimizados.

---

# Flujo General del Sistema

```text
Usuario → Login → Dashboard → CRUDs → Base de Datos
```

---

# Estado del Proyecto

El sistema ya cuenta con:

* Arquitectura funcional.
* Persistencia de datos.
* Gestión académica.
* Sistema de autenticación.
* CRUDs operativos.
* Dashboard funcional.
* Plantillas HTML.
* ORM configurado.
* Conexión MySQL.

---

# Autor

Proyecto desarrollado para gestión escolar académica usando Flask y SQLAlchemy.
