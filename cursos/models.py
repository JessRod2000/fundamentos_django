from django.db import models

# Create your models here.

                # hereda de la clase modelo
class Categoria(models.Model):
        # models. y se activan todos los campos que puede existir
    # variable (atributo/columna) = models.TipoData(nombre de campo para consultas/humanos, )
    nombre = models.CharField("nombre", max_length=50, unique=True)
    descripcion = models.TextField("descripción", blank=True)

    # solo sirve para el administrador de django
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
    # 
    def __str__(self):
        return self.nombre
    

class Curso(models.Model):
    # relacion 1:N con la tabla Categoria
    categoria = models.ForeignKey(
        Categoria,#se hace referencia de la tabla donde se hace la referencia
        on_delete=models.PROTECT,#protege la integridad de la bd
        related_name='cursos', #nombre de la relacion que se usa en el ORM Te permite hacer consultas limpias desde la categoría hacia sus cursos
        verbose_name='categoría', 
    )
    # Campos
    titulo = models.CharField("titulo", max_length=120)
    descripcion = models.TextField("descripcion", blank=True)
    fecha_inicio = models.DateField("fecha de inicio")
    carga_horaria = models.PositiveSmallIntegerField("carga horaria", default=0) # número entero positivo pequeño (útil para horas, cantidades pequeñas). Con default=0 evitas nulos y defines un valor inicial.
    activo = models.BooleanField("activo", default=True)

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"

    def __str__(self):
        return self.titulo