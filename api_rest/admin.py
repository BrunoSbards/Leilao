from django.contrib import admin

from .models import leiloeiro, matricula, Estado, Anexo

admin.site.register(leiloeiro)
admin.site.register(matricula)
admin.site.register(Estado)
admin.site.register(Anexo)
