# models.py

class Proyecto:
    def __init__(self, titulo, descripcion, tecnologia, enlace="#"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.tecnologia = tecnologia
        self.enlace = enlace

def obtener_proyectos():
    # Aquí simulamos una consulta a base de datos
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
