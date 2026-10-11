# models.py

class Proyecto:
    def __init__(self, titulo, descripcion, tecnologia, enlace="#"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.tecnologia = tecnologia
        self.enlace = enlace

def obtener_proyectos():
    return [
        Proyecto(
            titulo="E-Commerce API", 
            descripcion="Una API REST robusta construida para gestionar inventarios y pasarelas de pago de forma segura.", 
            tecnologia="Flask / PostgreSQL"
        ),
        Proyecto(
            titulo="Portafolio Web", 
            descripcion="Mi sitio web personal diseñado bajo arquitectura MVC con estilos modernos y dinámicos.", 
            tecnologia="Python / Tailwind CSS"
        ),
        Proyecto(
            titulo="Análisis de Datos AI", 
            descripcion="Un script automatizado que procesa grandes volúmenes de datos y genera reportes predictivos.", 
            tecnologia="Python / Pandas / SKLearn"
        )
    ]

def obtener_perfil():
    return {
        "nombre_completo": "Jorge Luis Saenz Bracamonte",
        "profesion": "Desarrollador Backend & Full-Stack Python",
        "rut": "287914776",
        "telefono": "9 2382 7819",
        "whatsapp": "+56923827819",
        "correo": "jorgeluissaenzbracamonte@gmail.com",
        "direccion": "La Alameda, Santiago Centro, Región Metropolitana",
        "github": "https://github.com"
    }

def obtener_habilidades():
    return {
        "Análisis y Diseño": ["Análisis de Requerimientos", "Arquitectura MVC", "Diseño de Sistemas Escalables", "Metodologías Ágiles"],
        "Lenguajes de Programación": ["Python", "PHP", "Java", "JavaScript"],
        "Bases de Datos": ["PostgreSQL", "MySQL", "SQLite", "Optimización de Consultas SQL"],
        "Administración y Redes": ["Administración de Servidores Linux (Debian/Ubuntu)", "Configuración de Redes", "Seguridad de Redes", "Despliegue en la Nube (Render/VPS)"]
    }
