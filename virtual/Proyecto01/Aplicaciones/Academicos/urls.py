from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.sign_in),
    
    #url para cursos
    path('cursos',views.home,name='cursos'),
    path('registrarCursos',views.registrarCursos),
    path('edicionCurso/<codigo>/', views.edicionCurso),
    path('editarCurso', views.editarCurso),
    path('eliminarCursos/<codigo>',views.eliminarCursos),
    path('buscarCurso', views.buscarCurso, name= 'buscarCurso'),

    #url para docentes
    path('docentes',views.docente, name='docentes'),
    path('registrarDocentes',views.registrarDocentes),
    path('edicionDocente/<codigo>', views.edicionDocente),
    path('editarDocente', views.editarDocente),
    path('eliminarDocente/<codigo>',views.eliminarDocente),
    path('buscarDocentes', views.buscarDocentes, name= 'buscarDocentes'),

    #url para especialidad
    path('especialidad',views.especialidad, name='especialidad'),
    path('registrarEspecialidad',views.registrarEspecialidad),
    path('edicionEspecialidad/<codigo>/', views.edicionEspecialidad),
    path('editarespecialidad', views.editarEspecialidad),
    path('eliminarEspecialidad/<codigo>',views.eliminarEspecialidad),
    path('buscarEspecialidad', views.buscarEspecialidad, name= 'buscarEspecialidad'),

    #url para matricula
    path('matricula',views.matricula, name='matriculas'),
    path('registrarMatricula',views.registrarMatricula),
    path('edicionMatricula/<codigo>/', views.edicionMatricula),
    path('editarMatricula', views.editarMatricula),
    path('eliminarMatricula/<codigo>',views.eliminarMatricula),
    path('buscarMatricula', views.buscarMatricula, name= 'buscarMatricula'),

]