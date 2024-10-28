import tkinter as tk
import random

# Datos del juego
historias = [
    {
        'descripcion': "El profesor fue encontrado muerto en la escuela enccuntra a su asesino.",
        'personas': ['Ana', 'Carlos', 'Elena', 'Jorge', 'Lucía'],
        'objetos': ['Cuchillo', 'Pistola', 'Veneno', 'Cuerda', 'Llave Inglesa'],
        'lugares': ['Biblioteca', 'Laboratorio', 'Cafetería', 'Aula', 'Jardín'],
        'asesino': 'Elena',
        'objeto_asesino': 'Cuerda',
        'lugar_asesinato': 'Laboratorio',
        'pistas': {
            'Ana': 'Ana estaba con un grupo grande en la biblioteca.',
            'Carlos': 'Carlos fue visto en la cafetería a la hora del asesinato.',
            'Elena': 'Elena fue vista cerca del laboratorio poco antes del asesinato.',
            'Jorge': 'Jorge estaba dando una clase en el aula.',
            'Lucía': 'Lucía estaba en el jardín hablando con un estudiante.',
            'Cuchillo': 'El arma parece ser algo que no corta.',
            'Pistola': 'No se oyeron disparos.',
            'Veneno': 'El profesor no muestra signos de envenenamiento.',
            'Cuerda': 'Parece que algo fue usado para estrangular a la víctima.',
            'Llave Inglesa': 'La llave inglesa está limpia, no fue usada.',
            'Biblioteca': 'En la biblioteca no se oyó ningún ruido extraño.',
            'Laboratorio': 'Se encontraron rastros de lucha en el laboratorio.',
            'Cafetería': 'La cafetería estaba llena, el asesino no podría haber pasado desapercibido.',
            'Aula': 'El aula estaba cerrada en el momento del asesinato.',
            'Jardín': 'El jardín está lejos de la escena del crimen.'
        }
    },
    {
        'descripcion': "El profesor fue encontrado muerto en la escuela enccuntra a su asesino.",
        'personas': ['Daniel', 'Marta', 'Tomás', 'Luis', 'Rosa'],
        'objetos': ['Bate', 'Cuchillo', 'Tijeras', 'Pistola', 'Cadena'],
        'lugares': ['Gimnasio', 'Aula de ciencias', 'Pasillo', 'Sala de profesores', 'Estacionamiento'],
        'asesino': 'Luis',
        'objeto_asesino': 'Cuchillo',
        'lugar_asesinato': 'Aula de ciencias',
        'pistas': {
            'Daniel': 'Daniel estaba en el gimnasio levantando pesas.',
            'Marta': 'Marta fue vista en el estacionamiento moviendo su coche.',
            'Tomás': 'Tomás estaba en la sala de profesores descansando.',
            'Luis': 'Luis fue visto corriendo por el pasillo, muy nervioso.',
            'Rosa': 'Rosa estaba hablando con un grupo de estudiantes en el gimnasio.',
            'Bate': 'No se usó un objeto tan contundente.',
            'Cuchillo': 'El cuchillo parece ser el arma del crimen.',
            'Tijeras': 'Las tijeras están intactas, no fueron usadas.',
            'Pistola': 'No se oyeron disparos.',
            'Cadena': 'La cadena parece estar en su lugar y no tiene sangre.',
            'Gimnasio': 'El gimnasio estaba lleno de gente haciendo ejercicio.',
            'Aula de ciencias': 'El aula de ciencias muestra claros signos de una pelea.',
            'Pasillo': 'El pasillo estaba vacío en el momento del crimen.',
            'Sala de profesores': 'La sala de profesores estaba tranquila, sin ruidos ni peleas.',
            'Estacionamiento': 'El estacionamiento estaba lleno de coches, no hay indicios de un crimen allí.'
        }
    },
    {
        'descripcion': "El profesor fue encontrado muerto en la escuela enccuntra a su asesino.",
        'personas': ['Pablo', 'Ana', 'Roberto', 'Silvia', 'Mario'],
        'objetos': ['Piedra', 'Cuerda', 'Cuchillo', 'Veneno', 'Tijeras'],
        'lugares': ['Jardín', 'Biblioteca', 'Aula de matemáticas', 'Cafetería', 'Auditorio'],
        'asesino': 'Silvia',
        'objeto_asesino': 'Cuchillo',
        'lugar_asesinato': 'Jardín',
        'pistas': {
            'Pablo': 'Pablo fue visto en la biblioteca estudiando.',
            'Ana': 'Ana estaba en la cafetería con sus amigos.',
            'Roberto': 'Roberto estaba hablando por teléfono en el auditorio.',
            'Silvia': 'Silvia fue vista caminando hacia el jardín antes del crimen.',
            'Mario': 'Mario estaba dando clases en el aula de matemáticas.',
            'Piedra': 'No parece que se haya usado una piedra para el asesinato.',
            'Cuerda': 'No hay marcas que sugieran que fue estrangulado.',
            'Cuchillo': 'Se encontraron heridas de cuchillo en el cuerpo del profesor.',
            'Veneno': 'El profesor no muestra signos de envenenamiento.',
            'Tijeras': 'Las tijeras no tienen huellas dactilares ni sangre.',
            'Jardín': 'El jardín es un lugar apartado, el crimen pudo haber ocurrido sin testigos.',
            'Biblioteca': 'La biblioteca estaba tranquila y no hay indicios de un crimen allí.',
            'Aula de matemáticas': 'La clase de matemáticas estaba en progreso durante el crimen.',
            'Cafetería': 'La cafetería estaba llena, no se reportó nada extraño.',
            'Auditorio': 'El auditorio estaba vacío salvo por Roberto que hablaba por teléfono.'
        }
    },
    {
        'descripcion': "El profesor fue encontrado muerto en la escuela enccuntra a su asesino.",
        'personas': ['Laura', 'Carlos', 'Javier', 'Sofía', 'Miguel'],
        'objetos': ['Llave inglesa', 'Veneno', 'Bate', 'Pistola', 'Navaja'],
        'lugares': ['Estacionamiento', 'Biblioteca', 'Gimnasio', 'Sala de reuniones', 'Aula de química'],
        'asesino': 'Carlos',
        'objeto_asesino': 'Llave inglesa',
        'lugar_asesinato': 'Estacionamiento',
        'pistas': {
            'Laura': 'Laura estaba en la sala de reuniones discutiendo un proyecto.',
            'Carlos': 'Carlos fue visto cerca del estacionamiento minutos antes del asesinato.',
            'Javier': 'Javier estaba dando clases en el gimnasio.',
            'Sofía': 'Sofía estaba preparando una presentación en la biblioteca.',
            'Miguel': 'Miguel estaba trabajando en un experimento en el aula de química.',
            'Llave inglesa': 'La llave inglesa fue encontrada con rastros de sangre.',
            'Veneno': 'No hay signos de envenenamiento en la víctima.',
            'Bate': 'El bate está intacto, no fue utilizado.',
            'Pistola': 'No se escucharon disparos en el área.',
            'Navaja': 'La navaja no tiene rastros de sangre.',
            'Estacionamiento': 'El estacionamiento estaba parcialmente vacío cuando ocurrió el asesinato.',
            'Biblioteca': 'En la biblioteca no hubo actividad sospechosa.',
            'Gimnasio': 'El gimnasio estaba lleno, pero nadie reportó algo extraño.',
            'Sala de reuniones': 'La sala de reuniones estaba ocupada con un grupo de personas.',
            'Aula de química': 'En el aula de química se estaba llevando a cabo un experimento complejo.'
        }
    },
    {
        'descripcion': "El profesor fue encontrado muerto en la escuela enccuntra a su asesino.",
        'personas': ['Isabel', 'Pedro', 'Luisa', 'Fernando', 'Andrés'],
        'objetos': ['Bastón', 'Cuerda', 'Llave Inglesa', 'Veneno', 'Tijeras'],
        'lugares': ['Sala de música', 'Aula de historia', 'Biblioteca', 'Pasillo principal', 'Gimnasio'],
        'asesino': 'Pedro',
        'objeto_asesino': 'Bastón',
        'lugar_asesinato': 'Sala de música',
        'pistas': {
            'Isabel': 'Isabel estaba en la biblioteca revisando unos libros.',
            'Pedro': 'Pedro fue visto entrando a la sala de música con un bastón.',
            'Luisa': 'Luisa estaba en el aula de historia preparando su clase.',
            'Fernando': 'Fernando estaba corriendo en el gimnasio.',
            'Andrés': 'Andrés fue visto hablando por teléfono en el pasillo principal.',
            'Bastón': 'El bastón tiene signos de haber sido usado para golpear a la víctima.',
            'Cuerda': 'No hay marcas de estrangulamiento en el cuerpo.',
            'Llave Inglesa': 'La llave inglesa está limpia y no fue utilizada.',
            'Veneno': 'No hay indicios de envenenamiento.',
            'Tijeras': 'Las tijeras no muestran señales de haber sido usadas.',
            'Sala de música': 'La sala de música muestra signos de una pelea.',
            'Aula de historia': 'El aula de historia estaba cerrada cuando ocurrió el crimen.',
            'Biblioteca': 'La biblioteca estaba en silencio, sin ninguna alteración.',
            'Pasillo principal': 'El pasillo principal estaba vacío salvo por Andrés que hablaba por teléfono.',
            'Gimnasio': 'El gimnasio estaba lleno, pero Fernando estaba solo corriendo.'
        }
    }
]

# Funciones del juego
def iniciar_juego():
    global caso
    caso = random.choice(historias)
    texto_descripcion.set(caso['descripcion'])
    # Actualizamos los menús desplegables con las nuevas opciones del caso
    menu_personas.set(caso['personas'][0])
    menu_objetos.set(caso['objetos'][0])
    menu_lugares.set(caso['lugares'][0])
    opciones_personas['menu'].delete(0, 'end')
    opciones_objetos['menu'].delete(0, 'end')
    opciones_lugares['menu'].delete(0, 'end')

    for persona in caso['personas']:
        opciones_personas['menu'].add_command(label=persona, command=tk._setit(menu_personas, persona))
    for objeto in caso['objetos']:
        opciones_objetos['menu'].add_command(label=objeto, command=tk._setit(menu_objetos, objeto))
    for lugar in caso['lugares']:
        opciones_lugares['menu'].add_command(label=lugar, command=tk._setit(menu_lugares, lugar))
    
    boton_iniciar.pack_forget()
    frame_juego.pack()

def elegir_opcion():
    eleccion_persona = menu_personas.get()
    eleccion_objeto = menu_objetos.get()
    eleccion_lugar = menu_lugares.get()

    pista_persona = caso['pistas'].get(eleccion_persona, "Sin pistas.")
    pista_objeto = caso['pistas'].get(eleccion_objeto, "Sin pistas.")
    pista_lugar = caso['pistas'].get(eleccion_lugar, "Sin pistas.")

    resultado.set(f"Pista sobre la persona: {pista_persona}\n"
                  f"Pista sobre el objeto: {pista_objeto}\n"
                  f"Pista sobre el lugar: {pista_lugar}")

# Interfaz gráfica
root = tk.Tk()
root.title("Asesinato del Profesor")

# Pantalla de inicio
frame_inicio = tk.Frame(root)
frame_inicio.pack()

label_bienvenida = tk.Label(frame_inicio, text="¡Bienvenido al juego del asesinato del profesor!")
label_bienvenida.pack()

boton_iniciar = tk.Button(frame_inicio, text="Iniciar Juego", command=iniciar_juego)
boton_iniciar.pack()

# Pantalla del juego
frame_juego = tk.Frame(root)

texto_descripcion = tk.StringVar()
label_descripcion = tk.Label(frame_juego, textvariable=texto_descripcion)
label_descripcion.pack()

label_persona = tk.Label(frame_juego, text="Selecciona una persona:")
label_persona.pack()

menu_personas = tk.StringVar(root)
menu_personas.set("Elige una persona")
opciones_personas = tk.OptionMenu(frame_juego, menu_personas, "")
opciones_personas.pack()

label_objeto = tk.Label(frame_juego, text="Selecciona un objeto:")
label_objeto.pack()

menu_objetos = tk.StringVar(root)
menu_objetos.set("Elige un objeto")
opciones_objetos = tk.OptionMenu(frame_juego, menu_objetos, "")
opciones_objetos.pack()

label_lugar = tk.Label(frame_juego, text="Selecciona un lugar:")
label_lugar.pack()

menu_lugares = tk.StringVar(root)
menu_lugares.set("Elige un lugar")
opciones_lugares = tk.OptionMenu(frame_juego, menu_lugares, "")
opciones_lugares.pack()

boton_elegir = tk.Button(frame_juego, text="Elegir", command=elegir_opcion)
boton_elegir.pack()

resultado = tk.StringVar()
label_resultado = tk.Label(frame_juego, textvariable=resultado)
label_resultado.pack()

# Ejecutar el programa
root.mainloop()

