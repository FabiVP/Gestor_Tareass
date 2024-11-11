import tkinter as tk
from tkinter import ttk, messagebox
from src.logica.Gestor_Tareass import GestorTareas


class GestorTareasGUI:
    def __init__(self, root, gestor):
        self.gestor = gestor
        self.root = root
        self.root.title("Gestor de Tareas")

        # Personalización de la ventana principal
        self.root.configure(bg='#f0f4f7')
        self.root.geometry("600x400")  # Tamaño de la ventana

        # Marco principal
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Estilo de los widgets
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 10, 'bold'), background='#2e6f9e', foreground='#000000')
        style.configure('TLabel', font=('Helvetica', 10), background='#f0f4f7', foreground='#000000')
        style.configure('TEntry', font=('Helvetica', 10), foreground='#000000')
        style.configure('TListbox', font=('Helvetica', 10), foreground='#000000')

        # Título
        ttk.Label(self.frame, text="Título:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.titulo_entry = ttk.Entry(self.frame, width=30)
        self.titulo_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Descripción
        ttk.Label(self.frame, text="Descripción:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.descripcion_entry = ttk.Entry(self.frame, width=50)
        self.descripcion_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Botón de agregar tarea
        self.agregar_btn = ttk.Button(self.frame, text="Agregar Tarea", command=self.agregar_tarea)
        self.agregar_btn.grid(row=2, column=1, sticky=tk.W, pady=5)

        # Listbox de tareas
        self.tareas_listbox = tk.Listbox(self.frame, height=10, width=80, font=('Helvetica', 10), bg='#e8f0fe',
                                         selectbackground='#d0e1f9', fg='#000000')
        self.tareas_listbox.grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.W)

        # Botones adicionales
        self.completar_btn = ttk.Button(self.frame, text="Marcar como Completada", command=self.marcar_completada)
        self.completar_btn.grid(row=4, column=0, pady=5, sticky=tk.W)

        self.eliminar_btn = ttk.Button(self.frame, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.eliminar_btn.grid(row=4, column=1, pady=5, sticky=tk.W)

        self.actualizar_lista()

    def agregar_tarea(self):
        titulo = self.titulo_entry.get()
        descripcion = self.descripcion_entry.get()
        try:
            self.gestor.agregar_tarea(titulo, descripcion)
            self.actualizar_lista()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_lista(self):
        self.tareas_listbox.delete(0, tk.END)
        for indice, tarea in enumerate(self.gestor.obtener_tareas()):
            estado = "Completada" if tarea.completada else "Pendiente"
            self.tareas_listbox.insert(tk.END,
                                       f"{indice + 1}. {tarea.titulo} - {estado}\n  - Descripción: {tarea.descripcion}")

    def marcar_completada(self):
        seleccion = self.tareas_listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            self.gestor.marcar_completada(indice)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

    def eliminar_tarea(self):
        seleccion = self.tareas_listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            self.gestor.eliminar_tarea(indice)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")


def run():
    root = tk.Tk()
    gestor = GestorTareas()
    app = GestorTareasGUI(root, gestor)
    root.mainloop()


if __name__ == "__main__":
    run()