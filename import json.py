import json
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

# Nombre del archivo JSON
archivo_db = 'personajes.json'

# Cargar personajes desde el archivo JSON
def cargar_personajes():
    if os.path.exists(archivo_db):
        with open(archivo_db, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return [
            {"nombre": "Naruto Uzumaki", "es_shinobi": True, "es_uchiha": False, "es_jinchuriki": True, "es_hokage": True, "genero": "Masculino", "pertenece_a_akatsuki": False, "está_muerto": False},
            {"nombre": "Sasuke Uchiha", "es_shinobi": True, "es_uchiha": True, "es_jinchuriki": False, "es_hokage": False, "genero": "Masculino", "pertenece_a_akatsuki": False, "está_muerto": False},
            {"nombre": "Kakashi Hatake", "es_shinobi": True, "es_uchiha": False, "es_jinchuriki": False, "es_hokage": True, "genero": "Masculino", "pertenece_a_akatsuki": False, "está_muerto": False},
            {"nombre": "Sakura Haruno", "es_shinobi": True, "es_uchiha": False, "es_jinchuriki": False, "es_hokage": False, "genero": "Femenino", "pertenece_a_akatsuki": False, "está_muerto": False},
            {"nombre": "Gaara", "es_shinobi": True, "es_uchiha": False, "es_jinchuriki": True, "es_hokage": False, "genero": "Masculino", "pertenece_a_akatsuki": False, "está_muerto": False},
            {"nombre": "Itachi Uchiha", "es_shinobi": True, "es_uchiha": True, "es_jinchuriki": False, "es_hokage": False, "genero": "Masculino", "pertenece_a_akatsuki": True, "está_muerto": True},
            {"nombre": "Hinata Hyuga", "es_shinobi": True, "es_uchiha": False, "es_jinchuriki": False, "es_hokage": False, "genero": "Femenino", "pertenece_a_akatsuki": False, "está_muerto": False},
            {"nombre": "Jiraiya", "es_shinobi": True, "es_uchiha": False, "es_jinchuriki": False, "es_hokage": False, "genero": "Masculino", "pertenece_a_akatsuki": False, "está_muerto": True},
            {"nombre": "Madara Uchiha", "es_shinobi": True, "es_uchiha": True, "es_jinchuriki": False, "es_hokage": False, "genero": "Masculino", "pertenece_a_akatsuki": True, "está_muerto": True},
            {"nombre": "Obito Uchiha", "es_shinobi": True, "es_uchiha": True, "es_jinchuriki": True, "es_hokage": False, "genero": "Masculino", "pertenece_a_akatsuki": True, "está_muerto": True},
        ]

# Guardar personajes en el archivo JSON
def guardar_personajes(personajes):
    with open(archivo_db, 'w', encoding='utf-8') as file:
        json.dump(personajes, file, ensure_ascii=False, indent=4)

# Clase del juego
class AkinatorNaruto:
    def __init__(self, root):
        self.root = root
        self.root.title("Akinator de Naruto")
        self.root.geometry("600x400")  # Tamaño de la ventana
        self.root.config(bg="#E6E6FA")  # Color de fondo lila

        self.personajes = cargar_personajes()
        self.preguntas = [
            ("es_shinobi", "¿Es un shinobi?"),
            ("es_uchiha", "¿Es del clan Uchiha?"),
            ("es_jinchuriki", "¿Es un jinchuriki?"),
            ("es_hokage", "¿Es o fue Hokage?"),
            ("genero", "¿Es Masculino?"),
            ("pertenece_a_akatsuki", "¿Pertenece a los Akatsuki?"),
            ("está_muerto", "¿Está muerto?")
        ]
        self.posibles = self.personajes.copy()
        self.current_question = 0

        self.label = tk.Label(root, text="Bienvenido al Akinator de Naruto!", bg="#E6E6FA", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button_yes = tk.Button(root, text="Iniciar", command=self.iniciar_juego, width=15, height=2, bg="#9370DB", font=("Helvetica", 14))
        self.button_yes.pack(pady=5)

        self.button_no = tk.Button(root, text="Salir", command=root.quit, width=15, height=2, bg="#9370DB", font=("Helvetica", 14))
        self.button_no.pack(pady=5)

    def iniciar_juego(self):
        self.label.config(text="Responde 'si' o 'no' a las preguntas.")
        self.posibles = self.personajes.copy()
        self.current_question = 0
        self.preguntar()

    def preguntar(self):
        if self.current_question < len(self.preguntas):
            atributo, pregunta = self.preguntas[self.current_question]
            respuesta = simpledialog.askstring("Pregunta", pregunta, parent=self.root)
            if respuesta is None:  # Cancel button pressed
                return

            respuesta = respuesta.strip().lower()
            if respuesta in ['salir', 'no']:
                self.posibles = [p for p in self.posibles if not p[atributo]]
            elif respuesta in ['si', 'sí']:
                self.posibles = [p for p in self.posibles if p[atributo]]
            else:
                messagebox.showwarning("Advertencia", "Por favor, responde 'si' o 'no'.", parent=self.root)
                return

            self.current_question += 1
            if len(self.posibles) == 1:
                self.fin_juego(self.posibles[0]["nombre"])
            elif len(self.posibles) == 0:
                self.fin_juego(None)
            else:
                self.preguntar()
        else:
            self.fin_juego(None)

    def fin_juego(self, resultado):
        if resultado:
            self.label.config(text=f"Tu personaje es {resultado}!")
        else:
            nombre = simpledialog.askstring("Nuevo Personaje", "No pude adivinar. ¿Cuál es el nombre del personaje?", parent=self.root)
            if nombre:
                es_shinobi = simpledialog.askstring("Atributo", "¿Es un shinobi? (si/no)", parent=self.root).strip().lower() == 'si'
                es_uchiha = simpledialog.askstring("Atributo", "¿Es del clan Uchiha? (si/no)", parent=self.root).strip().lower() == 'si'
                es_jinchuriki = simpledialog.askstring("Atributo", "¿Es un jinchuriki? (si/no)", parent=self.root).strip().lower() == 'si'
                es_hokage = simpledialog.askstring("Atributo", "¿Es o fue Hokage? (si/no)", parent=self.root).strip().lower() == 'si'
                genero = simpledialog.askstring("Atributo", "¿Cuál es su género?", parent=self.root)
                pertenece_a_akatsuki = simpledialog.askstring("Atributo", "¿Pertenece a los Akatsuki? (si/no)", parent=self.root).strip().lower() == 'si'
                está_muerto = simpledialog.askstring("Atributo", "¿Está muerto? (si/no)", parent=self.root).strip().lower() == 'si'

                self.personajes.append({
                    "nombre": nombre,
                    "es_shinobi": es_shinobi,
                    "es_uchiha": es_uchiha,
                    "es_jinchuriki": es_jinchuriki,
                    "es_hokage": es_hokage,
                    "genero": genero,
                    "pertenece_a_akatsuki": pertenece_a_akatsuki,
                    "está_muerto": está_muerto,
                })
                guardar_personajes(self.personajes)
                self.label.config(text=f"{nombre} agregado a la base de datos!")

        self.button_yes.config(text="Reiniciar", command=self.reiniciar)
    
   
