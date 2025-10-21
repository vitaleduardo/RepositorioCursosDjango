from django.http import HttpResponse


menu = """
    <a href="/">Inicio</a> |
    <a href="/cursos/">Cursos</a> |
    <a href="/contacto/">Contacto</a>
    <hr>
"""


def principal(request):
    contenido = """
    <h1>Bienvenido al portal CursosDjango</h1>
    <p>Este portal tiene como objetivo ofrecer información sobre distintos cursos
    en las áreas de tecnología, bases de datos y programación. </p>
    """
    return HttpResponse(menu + contenido)


def cursos(request):
    contenido = """
    <h2>Lista de Cursos Disponibles</h2>
    <ul>
        <li>Base de Datos</li>
        <li>Programación</li>
        <li>Desarrollo Web</li>
        <li>Inteligencia Artificial</li>
        <li>Redes</li>
    </ul>
    """
    return HttpResponse(menu + contenido)


def contacto(request):
    contenido = """
    <h2>Formulario de Contacto</h2>
    <form>
        <p>Nombre: <input type="text" name="nombre"></p>
        <p>Correo electrónico: <input type="email" name="correo"></p>
        <p>Curso de interés: 
            <select name="curso">
                <option>Base de Datos</option>
                <option>Programación</option>
                <option>Desarrollo Web</option>
                <option>Inteligencia Artificial</option>
                <option>Redes</option>
            </select>
        </p>
        <p>Comentarios:</p>
        <p><textarea name="comentarios" cols="50" rows="5"></textarea></p>
        <p><input type="button" value="Enviar"></p>
    </form>
    """
    return HttpResponse(menu + contenido)
