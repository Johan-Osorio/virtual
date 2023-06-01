from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            CursoListado = Curso.objects.order_by('codigo')
            return render(request, 'gestionCursos.html', {"cursos":CursoListado}) 
        else:
            # El usuario no ha proporcionado credenciales válidas
            pass
    return render(request,'Login.html')

# Create your views here.

'''---------funciones para tabla Cursos----------------'''
def home(request):
    cursosListado = Curso.objects.all()
    return render(request, "gestionCursos.html",{"cursos":cursosListado})

def registrarCursos(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    creditos = request.POST["numcreditos"]

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo = codigo)
    return render(request, "edicionCursos.html",{"curso":curso})

def editarCurso(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    creditos = request.POST["numcreditos"]

    curso = Curso.objects.get(codigo = codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')

def eliminarCursos(request,codigo):
    curso = Curso.objects.get(codigo = codigo)
    curso.delete()
    return redirect('/')

def buscarCurso(request):
    if request.method == "POST":
        buscarnombre = request.POST.get('nombre')
        busqueda=Curso.objects.filter(nombre__icontains=buscarnombre)
        return render(request,'buscarCursos.html',{"curso":busqueda})
    else:
        cursosListado = Curso.objects.all()
        return render(request, "buscarCursos.html",{"curso":cursosListado})

'''---------funciones para tabla Docentes----------------'''
def docente(request):
    docentesListado = Docente.objects.all()
    return render(request, "gestionDocentes.html",{"docentes":docentesListado})

def registrarDocentes(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    fecha_ingreso = request.POST["txtfecha_ingreso"]
    dni = request.POST["numdni"]
    telefono = request.POST["numtelefono"]

    docente = Docente.objects.create(idDocente=codigo, nombre=nombre, apellido=apellido, fecha_ingreso = fecha_ingreso, dni = dni, telefono = telefono)
    return redirect('/docentes')

def edicionDocente(request, codigo):
    docente = Docente.objects.get(idDocente = codigo)
    return render(request, "edicionDocentes.html",{"docente":docente})

def editarDocente(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    apellido = request.POST["txtapellido"]
    fecha_ingreso = request.POST["txtfecha_ingreso"]
    dni = request.POST["numdni"]
    telefono = request.POST["numtelefono"]

    docente = Docente.objects.get(idDocente = codigo)
    docente.nombre = nombre
    docente.apellido = apellido
    docente.fecha_ingreso = fecha_ingreso
    docente.dni = dni
    docente.telefono = telefono
    docente.save()

    return redirect('/docentes')

def eliminarDocente(request,codigo):
    docente = Docente.objects.get(idDocente = codigo)
    docente.delete()
    return redirect('/docentes')

def buscarDocentes(request):
    if request.method == "POST":
        buscarfecha_ingreso = request.POST.get('fecha_ingreso')
        busqueda=Docente.objects.filter(fecha_ingreso__icontains=buscarfecha_ingreso)
        return render(request,'buscarDocentes.html',{"docente":busqueda})
    else:
        docentesListado = Docente.objects.all()
        return render(request, "buscarDocentes.html",{"docente":docentesListado})


'''---------funciones para tabla especialidad----------------'''
def especialidad(request):
    especialidadListado = Especialidad.objects.all()
    return render(request, "gestionEspecialidad.html",{"especialidad":especialidadListado})

def registrarEspecialidad(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]

    especialidad = Especialidad.objects.create(idEspecialidad=codigo, nombre=nombre, descripcion=descripcion)
    return redirect('/especialidad')

def edicionEspecialidad(request, codigo):
    especialidad = Especialidad.objects.get(idEspecialidad = codigo)
    return render(request, "edicionEspecialidad.html",{"especialidad":especialidad})

def editarEspecialidad(request):
    codigo = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]

    especialidad = Especialidad.objects.get(idEspecialidad = codigo)
    especialidad.nombre = nombre
    especialidad.descripcion = descripcion
    especialidad.save()

    return redirect('/especialidad')

def eliminarEspecialidad(request,codigo):
    especialidad = Especialidad.objects.get(idEspecialidad = codigo)
    especialidad.delete()
    return redirect('/especialidad')

def buscarEspecialidad(request):
    if request.method == "POST":
        buscarnombre = request.POST.get('nombre')
        busqueda=Especialidad.objects.filter(nombre__icontains=buscarnombre)
        return render(request,'buscarEspecialidad.html',{"especialidad":busqueda})
    else:
        especialidadListado = Especialidad.objects.all()
        return render(request, "buscarEspecialidad.html",{"especialidad":especialidadListado})

'''---------funciones para tabla matricula----------------'''
def matricula(request):
    matriculaListado = Matricula.objects.all()
    cursosListado = Curso.objects.all()
    context = {
        "matricula": matriculaListado,
        "cursos": cursosListado
    }
    return render(request, "gestionMatricula.html", context)

def registrarMatricula(request):
    IdMatricula=request.POST["txtmatricula"]
    IdCurso=request.POST["txtcurso"]
    Fechamat=request.POST["txtfechamat"]
    Cuotas = request.POST["txtcuotas"]

    matricula=Matricula.objects.create(idMatricula=IdMatricula, cursos_id=IdCurso, fechaMat=Fechamat, cuotas=Cuotas)
    return redirect('/matricula')

def edicionMatricula(request, codigo):
    matricula = Matricula.objects.get(idMatricula = codigo)
    cursosListado=Curso.objects.all()
    ayuda = {
        "matricula": matricula,
        "cursos": cursosListado
    }
    return render(request, "edicionMatricula.html",ayuda)

def editarMatricula(request):
    idMatricula = request.POST["txtmatricula"]
    cursos = request.POST["txtcurso"]
    fechaMat = request.POST["txtfechamat"]
    cuotas = request.POST["txtcuotas"]

    curso = Curso.objects.get(codigo=cursos)
    matricula = Matricula.objects.get(idMatricula = idMatricula)
    matricula.cursos = curso
    matricula.fechaMat = fechaMat
    matricula.cuotas = cuotas
    matricula.save()

    return redirect('/matricula')

def eliminarMatricula(request,codigo):
    matricula = Matricula.objects.get(idMatricula = codigo)
    matricula.delete()
    return redirect('/matricula')

def buscarMatricula(request):
    if request.method == "POST":
        buscarfechamatri = request.POST.get('fechaMat')
        busqueda=Matricula.objects.filter(fechaMat__icontains=buscarfechamatri)
        return render(request,'buscarMatricula.html',{"matricula":busqueda})
    else:
        matriculaListado = Matricula.objects.all()
        return render(request, "buscarMatricula.html",{"matricula":matriculaListado})
