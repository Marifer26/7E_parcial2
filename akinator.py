import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Nombre del archivo JSON
archivo_db = 'personajes.json'

# Cargar personajes desde el archivo JSON
def cargar_personajes():
    if os.path.exists(archivo_db):
        with open(archivo_db, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return [
            {"nombre": "Naruto Uzumaki", "es_shinobi": True, "es_uchiha": False, "es_jinchuriki": True, "es_hokage": True, "es_hombre": True, "pertenece_a_akatsuki": False, "esta_muerto": False},
            {"nombre": "Sasuke Uchiha", "es_shinobi": True, "es_uchiha": True, "es_jinchuriki": False, "es_hokage": False, "es_hombre": True, "pertenece_a_akatsuki": False, "esta_muerto": False},
            {"nombre": "Kakashi Hatake", "es_shinobi": True, "es_uchiha": False, "es_jinchuriki": False, "es_hokage": True, "es_hombre": True, "pertenece_a_akatsuki": False, "esta_muerto": False},
            {"nombre": "Sakura Haruno", "es_shinobi": True, "es_uchiha": False, "es_jinchuriki": False, "es_hokage": False, "es_hombre": False, "pertenece_a_akatsuki": False, "esta_muerto": False},
            {"nombre": "Gaara", "es_shinobi": True, "es_uchiha": False, "es_jinchuriki": True, "es_hokage": False, "es_hombre": True, "pertenece_a_akatsuki": False, "esta_muerto": False},
            {"nombre": "Itachi Uchiha", "es_shinobi": True, "es_uchiha": True, "es_jinchuriki": False, "es_hokage": False, "es_hombre": True, "pertenece_a_akatsuki": True, "esta_muerto": True},
            {"nombre": "Jiraiya", "es_shinobi": True, "es_uchiha": False, "es_jinchuriki": False, "es_hokage": False, "es_hombre": True, "pertenece_a_akatsuki": False, "esta_muerto": True},
            {"nombre": "Obito Uchiha", "es_shinobi": True, "es_uchiha": True, "es_jinchuriki": True, "es_hokage": False, "es_hombre": True, "pertenece_a_akatsuki": True, "esta_muerto": True},
        ]

# Guardar personajes en el archivo JSON
def guardar_personajes(personajes):
    with open(archivo_db, 'w', encoding='utf-8') as file:
        json.dump(personajes, file, ensure_ascii=False, indent=4)

# Clase del juego
class AkinatorNaruto:
    def __init__(self, root):
        self.root = root
        self.root.title("adivina el personaje de Naruto")
        self.root.geometry("600x400")  # Tamaño de la ventana
        self.root.config(bg="#E6E6FA")  # Color de fondo lila

        self.personajes = cargar_personajes()
        self.preguntas = [
            ("es_shinobi", "¿Es un shinobi?"),
            ("es_uchiha", "¿Es del clan Uchiha?"),
            ("es_jinchuriki", "¿Es un jinchuriki?"),
            ("es_hokage", "¿Es o fue Hokage?"),
            ("es_hombre", "¿Es hombre?"),
            ("pertenece_a_akatsuki", "¿Pertenece a los Akatsuki?"),
            ("esta_muerto", "¿Está muerto?")
        ]
        self.posibles = self.personajes.copy()
        self.current_question = 0

        self.label = tk.Label(root, text="Bienvenido a adivina el personaje de Naruto!", bg="#E6E6FA", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button_yes = tk.Button(root, text="Iniciar", command=self.iniciar_juego, width=15, height=2, bg="#9370DB", font=("Helvetica", 14))
        self.button_yes.pack(pady=5)

        self.button_no = tk.Button(root, text="Salir", command=root.quit, width=15, height=2, bg="#9370DB", font=("Helvetica", 14))
        self.button_no.pack(pady=5)

        self.frame_respuestas = tk.Frame(root, bg="#E6E6FA")
        self.frame_respuestas.pack(pady=20)

    def iniciar_juego(self):
        self.label.config(text="Responde a las preguntas usando los botones.")
        self.posibles = self.personajes.copy()
        self.current_question = 0
        self.mostrar_respuestas(False)
        self.preguntar()

    def mostrar_respuestas(self, mostrar):
        for widget in self.frame_respuestas.winfo_children():
            widget.destroy()

        if mostrar:
            self.button_yes.pack_forget()
            self.button_no.pack_forget()

            tk.Button(self.frame_respuestas, text="Sí", command=lambda: self.responder("sí"), bg="#98FB98").pack(side=tk.LEFT, padx=5)
            tk.Button(self.frame_respuestas, text="No", command=lambda: self.responder("no"), bg="#FF7F7F").pack(side=tk.LEFT, padx=5)
            tk.Button(self.frame_respuestas, text="Salir", command=self.root.quit, bg="#FFB6C1").pack(side=tk.LEFT, padx=5)

    def preguntar(self):
        if self.current_question < len(self.preguntas):
            atributo, pregunta = self.preguntas[self.current_question]
            self.label.config(text=pregunta)
            self.mostrar_respuestas(True)
        else:
            self.fin_juego(None)

    def responder(self, respuesta):
        atributo, pregunta = self.preguntas[self.current_question]
        
        if respuesta == "no":
            self.posibles = [p for p in self.posibles if not p[atributo]]
        else:
            self.posibles = [p for p in self.posibles if p[atributo]]

        self.current_question += 1
        if len(self.posibles) == 1:
            self.fin_juego(self.posibles[0]["nombre"])
        elif len(self.posibles) == 0:
            self.fin_juego(None)
        else:
            self.preguntar()

    def fin_juego(self, resultado):
        self.mostrar_respuestas(False)
        if resultado:
            # Preguntar al usuario si es el personaje que pensaba
            confirmacion = messagebox.askyesno("Confirmación", f"¿Tu personaje es {resultado}?", parent=self.root)
            if confirmacion:
                self.label.config(text=f"¡Adiviné! Tu personaje es {resultado}!")
                # Reiniciar el juego inmediatamente
                self.root.after(2000, self.iniciar_juego)  # Espera 2 segundos antes de reiniciar
            else:
                self.label.config(text="No pude adivinar. ¿Quieres añadir un nuevo personaje?")
                tk.Button(self.frame_respuestas, text="Sí", command=self.agregar_personaje, bg="#98FB98").pack(side=tk.LEFT, padx=5)
                tk.Button(self.frame_respuestas, text="No", command=self.iniciar_juego, bg="#FF7F7F").pack(side=tk.LEFT, padx=5)
        else:
            self.label.config(text="No pude adivinar. ¿Quieres añadir un nuevo personaje?")
            tk.Button(self.frame_respuestas, text="Sí", command=self.agregar_personaje, bg="#98FB98").pack(side=tk.LEFT, padx=5)
            tk.Button(self.frame_respuestas, text="No", command=self.iniciar_juego, bg="#FF7F7F").pack(side=tk.LEFT, padx=5)

    def agregar_personaje(self):
        nombre = simpledialog.askstring("Nombre del personaje", "¿Cuál es el nombre del personaje?", parent=self.root)
        if nombre:
            es_shinobi = simpledialog.askstring("Atributo", "¿Es un shinobi? (si/no)", parent=self.root).strip().lower() == 'si'
            es_uchiha = simpledialog.askstring("Atributo", "¿Es del clan Uchiha? (si/no)", parent=self.root).strip().lower() == 'si'
            es_jinchuriki = simpledialog.askstring("Atributo", "¿Es un jinchuriki? (si/no)", parent=self.root).strip().lower() == 'si'
            es_hokage = simpledialog.askstring("Atributo", "¿Es o fue Hokage? (si/no)", parent=self.root).strip().lower() == 'si'
            es_hombre = simpledialog.askstring("Atributo", "¿Es hombre? (si/no)", parent=self.root).strip().lower() == 'si'
            pertenece_a_akatsuki = simpledialog.askstring("Atributo", "¿Pertenece a los Akatsuki? (si/no)", parent=self.root).strip().lower() == 'si'
            esta_muerto = simpledialog.askstring("Atributo", "¿Está muerto? (si/no)", parent=self.root).strip().lower() == 'si'

            self.personajes.append({
                "nombre": nombre,
                "es_shinobi": es_shinobi,
                "es_uchiha": es_uchiha,
                "es_jinchuriki": es_jinchuriki,
                "es_hokage": es_hokage,
                "es_hombre": es_hombre,
                "pertenece_a_akatsuki": pertenece_a_akatsuki,
                "esta_muerto": esta_muerto,
            })
            guardar_personajes(self.personajes)
            self.label.config(text=f"{nombre} agregado a la base de datos!")
            self.root.after(2000, self.iniciar_juego)  # Reiniciar el juego automáticamente

if __name__ == "__main__":
    root = tk.Tk()
    juego = AkinatorNaruto(root)
    root.mainloop()
