# 📘 **README_DJANGO.md — Documentación Técnica del Proyecto**

# 🌐 Proyecto Web con Django – Evolución del Portafolio

Este documento registra la **implementación técnica**, la **investigación sobre Django** y la **evolución del portafolio** desde HTML/CSS/JS hacia una aplicación web completa desarrollada con **Django**, siguiendo los requerimientos del módulo de Desarrollo Web Backend.

---

# 📖 1. Investigación sobre Django

## 💡 ¿Qué es Django?

Django es un **framework web de alto nivel para Python**, diseñado para crear aplicaciones seguras, mantenibles y escalables de forma rápida.
Se basa en el patrón arquitectónico **MTV (Model–Template–View)**.

---

## 🔧 Características principales del framework

* **ORM integrado** para trabajar con bases de datos sin escribir SQL directo.
* **Sistema MTV** claro y mantenible.
* **Admin automático**, completo y personalizable.
* **Autenticación y permisos incorporados**.
* **Gestión de sesiones, formularios y validaciones**.
* **Sistema de templates** flexible y seguro.
* **Enrutamiento sencillo** basado en URLconfs.
* **Alto nivel de seguridad** (protección contra XSS, CSRF, SQL Injection).
* **Escalabilidad utilizada en grandes empresas**.

---

## 🏢 Ventajas para el desarrollo de aplicaciones empresariales

* **Rápido desarrollo**: genera estructura y herramientas listas para usar.
* **Integración completa del backend**: ORM, autenticación, admin, formularios.
* **Reducción de errores** gracias a validaciones internas.
* **Escalable** para aplicaciones grandes.
* **Estabilidad a largo plazo** debido a su comunidad sólida.
* **Ideal para APIs** con Django REST Framework.

---

## ⚔️ Comparativa con otros frameworks

### **Django vs Flask**

| Tema                     | Django                                | Flask                               |
|--------------------------|-----------------------------------------|--------------------------------------|
| Filosofía                | Framework completo ("batteries included") | Microframework minimalista           |
| Estructura               | Guiada y con componentes integrados    | Flexible, tú decides qué agregar     |
| Admin automático         | Sí                                     | No                                   |
| ORM incluido             | Sí                                     | Opcional (por extensión)             |
| Seguridad integrada      | Alta y por defecto                     | Depende de extensiones y configuración|
| Ideal para               | Apps grandes, complejas y empresariales| APIs pequeñas o proyectos simples     |


---

### **Django vs FastAPI**

| Tema                 | Django                          | FastAPI                        |
| -------------------- | ------------------------------- | ------------------------------ |
| Tipo                 | Framework completo              | Enfoque en APIs                |
| Velocidad            | Muy buena                       | Excelente (ASGI)               |
| Curva de aprendizaje | Media                           | Media-alta                     |
| Uso ideal            | Sitios web con backend completo | Microservicios y APIs modernas |

---

### **Django vs Laravel (PHP)**

* Django usa Python; Laravel, PHP.
* Ambos son potentes y escalables.
* Django es preferido en entornos científicos, tecnológicos y de análisis de datos.
* Laravel es común en aplicaciones comerciales tradicionales.

---

# 🛠️ 2. Configuración del Proyecto Django

## 📂 Estructura creada dentro del repositorio del portafolio

```
mi-portafolio/
│── index.html                 ← Frontend original
│── css/
│── js/
│── img/
│── README.md                  ← Portafolio visual
│── README_DJANGO.md           ← Documentación técnica (este archivo)
│── django_portfolio/
      │── config/              ← Proyecto Django
      │── portfolio/           ← Aplicación principal
      │── manage.py
```

---

## 🔹 Comandos utilizados

### Crear carpeta para el proyecto

```bash
mkdir django_portfolio
cd django_portfolio
```

### Crear proyecto base

```bash
django-admin startproject config .
```

### Crear aplicación principal

```bash
python manage.py startapp portfolio
```

### Registrar la app en `settings.py`

```python
INSTALLED_APPS = [
   ...
   'portfolio',
]
```

---

# 🎨 3. Templates y Archivos Estáticos

Se migrará el diseño original del portafolio a Django:

* `index.html` → `portfolio/templates/portfolio/index.html`
* `css/` → `portfolio/static/css/`
* `js/` → `portfolio/static/js/`
* `img/` → `portfolio/static/img/`

Se usa:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/estilos.css' %}">
```

---

# 🗄️ 4. Modelos de Base de Datos

Ejemplo del modelo para proyectos:

```python
class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=200)
    enlace = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
```

Los proyectos se mostrarán dinámicamente en la página.

---

# 📝 5. Formularios Web

Se implementarán formularios para:

* Contacto
* Registro de proyectos
* Autenticación de usuarios

Ejemplo:

```python
from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
```

---

# 🔐 6. Autenticación y Autorización

Se habilitarán:

* Registro e inicio de sesión
* Control de accesos
* Restricción de vistas para usuarios autenticados
* Permisos en el admin

---

# 🛡️ 7. Personalización del Admin

En `admin.py`:

```python
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tecnologia')
    search_fields = ('titulo',)
```

También se configurará la administración de usuarios y permisos.

---

# 🚀 8. Cómo ejecutar el proyecto

## 1. Crear entorno virtual

```bash
python -m venv venv
```

## 2. Activarlo

```bash
venv\Scripts\activate   # Windows
```

## 3. Instalar Django

```bash
pip install django
```

## 4. Migraciones

```bash
python manage.py migrate
```

## 5. Ejecutar servidor

```bash
python manage.py runserver
```

Acceder en:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

# 📌 9. Estado del Proyecto

### ✔ Etapa 1: Investigación

### ✔ Etapa 2: Creación del proyecto Django

### ⬜ Etapa 3: Migración completa del frontend

### ⬜ Etapa 4: Modelos y base de datos

### ⬜ Etapa 5: Formularios

### ⬜ Etapa 6: Autenticación

### ⬜ Etapa 7: Admin personalizado

### ⬜ Etapa 8: Documentación final

---

# 🧾 Licencia

Proyecto académico para fines formativos.

---

