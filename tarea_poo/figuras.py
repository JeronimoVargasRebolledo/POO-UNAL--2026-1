import tkinter as tk
from tkinter import messagebox
import math

# ==========================================
# LÓGICA DE NEGOCIO (Jerarquía de Clases)
# ==========================================

class FiguraGeometrica:
    def __init__(self):
        self._volumen = 0.0
        self._superficie = 0.0

    def set_volumen(self, volumen):
        self._volumen = volumen

    def set_superficie(self, superficie):
        self._superficie = superficie

    def get_volumen(self):
        return self._volumen

    def get_superficie(self):
        return self._superficie


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        volumen = math.pi * (self.radio ** 2) * self.altura
        self.set_volumen(volumen)
        return volumen

    def calcular_superficie(self):
        area_ladoA = 2.0 * math.pi * self.radio * self.altura
        area_ladoB = 2.0 * math.pi * (self.radio ** 2)
        superficie = area_ladoA + area_ladoB
        self.set_superficie(superficie)
        return superficie


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def calcular_volumen(self):
        volumen = (4.0 / 3.0) * math.pi * (self.radio ** 3)
        self.set_volumen(volumen)
        return volumen

    def calcular_superficie(self):
        superficie = 4.0 * math.pi * (self.radio ** 2)
        self.set_superficie(superficie)
        return superficie


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        volumen = (math.pow(self.base, 2.0) * self.altura) / 3.0
        self.set_volumen(volumen)
        return volumen

    def calcular_superficie(self):
        area_base = math.pow(self.base, 2.0)
        area_lados = 2.0 * self.base * self.apotema
        superficie = area_base + area_lados
        self.set_superficie(superficie)
        return superficie


# ==========================================
# INTERFAZ GRÁFICA (Vistas)
# ==========================================

class VentanaCilindro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cilindro")
        self.geometry("280x200")
        self.resizable(False, False)
        
        # Componentes
        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=150)
        
        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=100, y=50, width=150)
        
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.action_performed)
        self.btn_calcular.place(x=100, y=80, width=150)
        
        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):")
        self.lbl_volumen.place(x=20, y=120)
        
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):")
        self.lbl_superficie.place(x=20, y=150)

    def action_performed(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            cilindro = Cilindro(radio, altura)
            self.lbl_volumen.config(text=f"Volumen (cm3): {cilindro.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {cilindro.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")


class VentanaEsfera(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Esfera")
        self.geometry("280x180")
        self.resizable(False, False)
        
        # Componentes
        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=150)
        
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.action_performed)
        self.btn_calcular.place(x=100, y=50, width=150)
        
        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):")
        self.lbl_volumen.place(x=20, y=100)
        
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):")
        self.lbl_superficie.place(x=20, y=130)

    def action_performed(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)
            self.lbl_volumen.config(text=f"Volumen (cm3): {esfera.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {esfera.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")


class VentanaPiramide(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pirámide")
        self.geometry("280x230")
        self.resizable(False, False)
        
        # Componentes
        tk.Label(self, text="Base (cms):").place(x=20, y=20)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=110, y=20, width=140)
        
        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=110, y=50, width=140)
        
        tk.Label(self, text="Apotema (cms):").place(x=20, y=80)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=110, y=80, width=140)
        
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.action_performed)
        self.btn_calcular.place(x=110, y=110, width=140)
        
        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):")
        self.lbl_volumen.place(x=20, y=160)
        
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):")
        self.lbl_superficie.place(x=20, y=190)

    def action_performed(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())
            piramide = Piramide(base, altura, apotema)
            self.lbl_volumen.config(text=f"Volumen (cm3): {piramide.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {piramide.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x100")
        self.resizable(False, False)
        
        # Botones principales
        self.btn_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro)
        self.btn_cilindro.place(x=20, y=30, width=90)
        
        self.btn_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        self.btn_esfera.place(x=130, y=30, width=90)
        
        self.btn_piramide = tk.Button(self, text="Pirámide", command=self.abrir_piramide)
        self.btn_piramide.place(x=240, y=30, width=90)

    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_piramide(self):
        VentanaPiramide(self)

# Punto de entrada
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
