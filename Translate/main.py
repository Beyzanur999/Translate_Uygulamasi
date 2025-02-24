from tkinter import Tk, Label, Entry, Button, Text, END
from tkinter import ttk
from googletrans import Translator, LANGUAGES  

root = Tk()
root.title("Translator")
root.eval('tk::PlaceWindow . center')

Label(root, text="Metin girin lütfen.").pack(pady=5)
input_text = Entry(root, width=30)
input_text.pack(pady=5)

Label(root, text="Hangi dilde çeviri yapmak istersiniz?").pack(pady=5)

# Dil kodlarını isimlerle eşleştirme
lang_dict = {value.title(): key for key, value in LANGUAGES.items()}
lang_list = list(lang_dict.keys())

# Dil seçimi için ComboBox
target_lang_combo = ttk.Combobox(root, values=lang_list, state="readonly")
target_lang_combo.set("Dil Seçiniz")  
target_lang_combo.pack(pady=5)

def translate_text():
    text = input_text.get()
    selected_lang = target_lang_combo.get()
    
    if text and selected_lang in lang_dict:
        lang_code = lang_dict[selected_lang]
        translator = Translator()  
        translation = translator.translate(text, dest=lang_code)  
        
        result_text.config(state='normal')
        result_text.delete(1.0, END)
        result_text.insert(END, translation.text)
        result_text.config(state='disable')

Button(root, text="Çevir", command=translate_text).pack(pady=10)

result_text = Text(root, height=10, width=40, state='disable')
result_text.pack(pady=10)

root.mainloop()
