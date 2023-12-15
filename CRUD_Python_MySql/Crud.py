import tkinter as tk
from tkinter import *

from tkinter import ttk, messagebox
from clientes import *
from conexion import *

class FormularioClientes:

    def actualizarRegistros():
        try:
            tree.delete(*tree.get_children())
            for row in CClientes.MostrarClientes():
                tree.insert("", 'end', values=row) 
        except ValueError as error:
            print("Error al actualizar registros error: {}".format(error))

    def seleccionarRegistro(evento):
        try:
            itemSeleccionado = tree.focus()
            if itemSeleccionado:
                values = tree.item(itemSeleccionado)['values']
                entradaId.delete(0, END)
                entradaId.insert(0, values[0])
                entradaNombres.delete(0, END)
                entradaNombres.insert(0, values[1])
                entradaApellidos.delete(0, END)
                entradaApellidos.insert(0, values[2])
                combo.set(values[3])
        except ValueError as error:
            print("Error al seleccionar el registro, error: {}".format(error))

    def ModificarRegistros():
        try:
            if entradaId is None or entradaNombres is None or entradaApellidos is None or combo is None:
                messagebox.showinfo("Error", "Debe completar todos los datos")
                return

            nombres = entradaNombres.get()
            apellidos = entradaApellidos.get()
            sexo = combo.get()
            UsuarioId = entradaId.get()

            CClientes.ModificarClientes(UsuarioId, nombres, apellidos, sexo)
            FormularioClientes.actualizarRegistros()

            messagebox.showinfo("Exito", "Modificacion exitosa")

            entradaId.delete(0, END)
            entradaNombres.delete(0, END)
            entradaApellidos.delete(0, END)

        except ValueError as error:
            print("Error al ingresar los datos, error: {}".format(error))

    def EliminarRegistros():
        try:
            if entradaId is None or entradaNombres is None or entradaApellidos is None or combo is None:
                messagebox.showinfo("Error", "Debe completar todos los datos")
                return

            UsuarioId = entradaId.get()

            CClientes.EliminarClientes(UsuarioId)
            FormularioClientes.actualizarRegistros()

            messagebox.showinfo("Exito", "Eliminacion exitosa")

            entradaId.delete(0, END)
            entradaNombres.delete(0, END)
            entradaApellidos.delete(0, END)

        except ValueError as error:
            print("Error al eliminar los datos, error: {}".format(error))

    @staticmethod   
    def formulario():
        global entradaId, entradaNombres, entradaApellidos, combo, tree
        global groupBox, base, groupBox_right

        try:
            base = Tk()
            base.geometry("1220x300")
            base.title("Formulario Python")

            groupBox = LabelFrame(base, text='Datos del Personal', padx=5, pady=5)
            groupBox.grid(row=0, column=0, padx=10, pady=10)

            label = Label(groupBox, text="Id:", width=13, font=("arial", 12)).grid(row=0, column=0)
            entradaId = Entry(groupBox)
            entradaId.grid(row=0, column=1)

            label = Label(groupBox, text="Nombres:", width=13, font=("arial", 12)).grid(row=1, column=0)
            entradaNombres = Entry(groupBox)
            entradaNombres.grid(row=1, column=1)

            label = Label(groupBox, text="Apellidos:", width=13, font=("arial", 12)).grid(row=2, column=0)
            entradaApellidos = Entry(groupBox)
            entradaApellidos.grid(row=2, column=1)

            labelsexo = Label(groupBox, text="Sexo:", width=13, font=("arial", 12)).grid(row=3, column=0)
            seleccionSexo = tk.StringVar(value="Masculino")
            combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino"], textvariable=seleccionSexo)
            combo.grid(row=3, column=1)

            boton1 = Button(groupBox, text="Guardar", width=10, command=FormularioClientes.guardarRegistros).grid(row=4, column=0)
            boton2 = Button(groupBox, text="Modificar", width=10, command=FormularioClientes.ModificarRegistros).grid(row=4, column=1)
            boton3 = Button(groupBox, text="Eliminar", width=10, command=FormularioClientes.EliminarRegistros).grid(row=4, column=2)

            groupBox_right = LabelFrame(base, text='Lista del Personal', padx=5, pady=5)
            groupBox_right.grid(row=0, column=1, padx=5, pady=5)

            tree = ttk.Treeview(groupBox_right, columns=("Id", "Nombres", "Apellidos", "Sexo"), show='headings', height=5)
            tree.column("Id", anchor=CENTER)
            tree.heading("Id", text="Id")
            tree.column("Nombres", anchor=CENTER)
            tree.heading("Nombres", text="Nombres")
            tree.column("Apellidos", anchor=CENTER)
            tree.heading("Apellidos", text="Apellidos")
            tree.column("Sexo", anchor=CENTER)
            tree.heading("Sexo", text="Sexo")

            for row in CClientes.MostrarClientes():
                tree.insert("", 'end', values=row)

            tree.bind("<<TreeviewSelect>>", FormularioClientes.seleccionarRegistro)

            tree.pack()

            base.mainloop()

        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))

    def guardarRegistros():
        try:
            if entradaNombres is None or entradaApellidos is None or combo is None:
                messagebox.showinfo("Error", "Debe completar todos los datos")
                return

            nombres = entradaNombres.get()
            apellidos = entradaApellidos.get()
            sexo = combo.get()

            CClientes.IngresarClientes(nombres, apellidos, sexo)
            FormularioClientes.actualizarRegistros()

            messagebox.showinfo("Exito", "Registro exitoso")

            entradaNombres.delete(0, END)
            entradaApellidos.delete(0, END)

        except ValueError as error:
            print("Error al ingresar los datos, error: {}".format(error))

# Crea una instancia de la clase FormularioClientes
formulario_clientes = FormularioClientes()
formulario_clientes.formulario()
