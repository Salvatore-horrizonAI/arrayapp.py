#Questo è il mio progetto per il calcolo degli array.
#Salvatore Naro
import numpy as np
import customtkinter
import tkinter
from tkinter import messagebox
import ast
import csv
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
window = customtkinter.CTk()
window.geometry("1000x700") 
window.title("Salvatore per Meta")

main_frame = customtkinter.CTkScrollableFrame(window, width=900, height=650)
main_frame.pack(pady=10, padx=10, fill="both", expand=True)
input_frame = customtkinter.CTkFrame(master=main_frame)
input_frame.pack(pady=10, padx=10, fill="x")

label = customtkinter.CTkLabel(master=input_frame, text="Inserisci un array")
label.pack(pady=5)

entry = customtkinter.CTkEntry(master=input_frame, placeholder_text="Inserisci un array", width=400)
entry.pack(pady=5)


results_frame = customtkinter.CTkFrame(master=main_frame)
results_frame.pack(pady=10, padx=10, fill="both", expand=True)


buttons_frame = customtkinter.CTkFrame(master=main_frame)
buttons_frame.pack(pady=10)
def save():
    if 'results' not in globals():
        messagebox.showerror("Errore", "Prima esegui un calcolo con l'array")
        return
    
    save_file = filedialog.asksaveasfilename(defaultextension=".csv",
                                           filetypes=[("CSV files", "*.csv")],
                                           title="Salva file csv")
    if not save_file: 
        return
    
    try:
        with open(save_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Operazione", "Risultato"])  
            for key, value in results.items():
                
                if isinstance(value, np.ndarray):
                    value_str = np.array2string(value, separator=', ')
                else:
                    value_str = str(value)
                writer.writerow([key, value_str])
        messagebox.showinfo("Successo", "File salvato correttamente")
    except Exception as e:
        messagebox.showerror("Errore", f"Impossibile salvare il file: {str(e)}")
def array():
    arr_str = entry.get()
    if not arr_str:
        messagebox.showerror("Errore", "Inserisci un array valido")
        return
    
    try:
        global results
        arr = np.array(ast.literal_eval(arr_str))
        results = {
            "Somma": np.sum(arr),
            "Prodotto": np.prod(arr),
            "Divisione per 2": arr / 2,
            "Sottrazione di 2": arr - 2,
            "Media": np.mean(arr),
            "Minimo": np.min(arr),
            "Massimo": np.max(arr),
            "Ordinato crescente": np.sort(arr),
            "Ordinato decrescente": np.sort(arr)[::-1],
            "Mediana": np.median(arr),
            "Varianza": np.var(arr),
            "Numero casuale": np.random.choice(arr),
            "Indice minimo": np.argmin(arr),
            "Indice massimo": np.argmax(arr)
        }
        
       
        for widget in results_frame.winfo_children():
            widget.destroy()
        
        
        for i, (key, value) in enumerate(results.items()):
            row = i // 2
            col = i % 2
            label = customtkinter.CTkLabel(
                master=results_frame, 
                text=f"{key}: {str(value)}",
                wraplength=400
            )
            label.grid(row=row, column=col, padx=5, pady=2, sticky="w")
        
        
        if arr.ndim == 1:
            fig, ax = plt.subplots(figsize=(6, 3))
            ax.plot(arr, 'o-')
            ax.set_title("Grafico dell'array")
            ax.set_ylabel("valore",color="white")
            ax.set_xlabel("indice",color="white")
            ax.grid(color='gray', linestyle='--', alpha=0.3)
            ax.set_facecolor('#2b2b2b')
            
            canvas = FigureCanvasTkAgg(fig, master=results_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=len(results)//2+1, column=0, columnspan=2, pady=10)
        
    except Exception as e:
        messagebox.showerror("Errore", f"Input non valido: {str(e)}")

def mode():
    luce = customtkinter.get_appearance_mode()
    if luce == "Dark":
        customtkinter.set_appearance_mode("light")
    else:
        customtkinter.set_appearance_mode("dark")


button_calc = customtkinter.CTkButton(
    master=buttons_frame,
    text="Calcola",
    command=array
)
button_calc.pack(side="left", padx=5)
button_save=customtkinter.CTkButton(master=buttons_frame,
                                    text="Salva",
                                    command = save)
button_save.pack(side="left", padx=7)

color = customtkinter.CTkSwitch(
    master=buttons_frame,
    width=10,
    height=10,
    text="",
    command=mode
)
color.pack(side="left", padx=5)
window.mainloop()