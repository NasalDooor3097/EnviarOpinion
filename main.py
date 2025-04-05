import tkinter as tk
from tkinter import messagebox
import webbrowser
import urllib.parse


TU_NUMERO = "3330368577"  
TU_NOMBRE = "Alberto"  

def enviar_whatsapp():
    opinion = texto_opinion.get("1.0", tk.END).strip()
    
    if not opinion:
        messagebox.showwarning("Oops", "Por favor escribe tu opinión antes de enviar")
        return
    
    
    mensaje = f"*Nueva opinión sobre alimentación saludable para {TU_NOMBRE}:*\n\n{opinion}"
    
    mensaje_codificado = urllib.parse.quote(mensaje)
    
    
    numero_formateado = TU_NUMERO.lstrip('0')  
    if not numero_formateado.startswith('52'):
        numero_formateado = f"52{numero_formateado}"  
    
    
    url_whatsapp = f"https://wa.me/{numero_formateado}?text={mensaje_codificado}"
    
    
    webbrowser.open_new(url_whatsapp)
    
   
    texto_opinion.delete("1.0", tk.END)
    messagebox.showinfo("Listo", f"Se abrirá WhatsApp para enviar tu opinión")











ventana = tk.Tk()
ventana.title("alimentación saludable")
ventana.geometry("500x400")
ventana.configure(bg="#f0f8ff")


color_whatsapp = "#25D366"
color_fondo = "#f0f8ff"


tk.Label(ventana, text=f"💬 Escribe una opinion de alimentación saludable", 
         font=("Arial", 16, "bold"), bg=color_fondo, fg=color_whatsapp).pack(pady=15)


tk.Label(ventana, text="🍎🥦🍗🥛🍞", font=("Arial", 30), bg=color_fondo).pack()


tk.Label(ventana, text="Comparte tus comentarios sobre alimentación saludable:", 
         font=("Arial", 10), bg=color_fondo).pack(pady=10)


texto_opinion = tk.Text(ventana, height=10, width=50, font=("Arial", 11), wrap=tk.WORD)
texto_opinion.pack(padx=20, pady=10)


tk.Button(ventana, text=f"ENVIAR  q(≧▽≦q)", command=enviar_whatsapp,
          bg=color_whatsapp, fg="white", font=("Arial", 12, "bold"),
          padx=20, pady=8, bd=0).pack()


tk.Label(ventana, text="Se abrirá WhatsApp para que completes el envío", 
         font=("Arial", 8), bg=color_fondo, fg="gray").pack(pady=10)

ventana.mainloop()