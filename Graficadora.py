import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def graficar_3d():
    try:
        expresion = entrada.get().replace("^", "**")
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x, y)
        
        funciones_permitidas = {"X": X, "Y": Y, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                                "sqrt": np.sqrt, "log": np.log, "exp": np.exp, "abs": np.abs,
                                "pi": np.pi, "e": np.e}
        
        Z = eval(expresion, {"__builtins__": None}, funciones_permitidas)
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title(f"Gráfica de Z = {expresion}")
        plt.show()
        
    except Exception as e:
        messagebox.showerror("Error", f"Expresión no válida: {e}")

root = tk.Tk()
root.title("Graficadora 3D")
root.geometry("400x200")

tk.Label(root, text="Ingrese una función en términos de X e Y:").pack(pady=5)
entrada = tk.StringVar()
tk.Entry(root, textvariable=entrada, font=("Arial", 14), width=30).pack(pady=5)

tk.Button(root, text="Graficar", font=("Arial", 14), command=graficar_3d).pack(pady=10)

root.mainloop()
