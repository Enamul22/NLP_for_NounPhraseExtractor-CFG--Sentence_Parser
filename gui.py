import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from parser import preprocess, np_chunk, parser

def parse_and_show_np_chunks():
    sentence = txt_input.get("1.0", tk.END).strip()
    if not sentence:
        messagebox.showinfo('Info', 'Please enter a sentence.')
        return
    try:
        print(f"Parsing sentence: {sentence}")  # Debug print
        words = preprocess(sentence)
        print(f"Preprocessed words: {words}")  # Debug print
        trees = list(parser.parse(words))
        if not trees:
            print("No parse trees were generated.")  # Debug print
            messagebox.showinfo('Info', 'Could not parse the sentence.')
            return

        np_chunks_set = set()
        for tree in trees:
            for np in np_chunk(tree):
                np_chunks_set.add(" ".join(np.flatten()))
        print(f"NP chunks: {np_chunks_set}")  # Debug print

        txt_output.delete("1.0", tk.END)
        for np in sorted(np_chunks_set):
            txt_output.insert(tk.END, np + "\n")

    except Exception as e:
        messagebox.showerror('Error', str(e))
        print(e)  # Debug print

# Set up the GUI window
window = tk.Tk()
window.title("NP Chunk Parser")
window.geometry('600x400')

# Input text widget
lbl_input = tk.Label(window, text="Enter Sentence:")
lbl_input.pack(pady=5)
txt_input = scrolledtext.ScrolledText(window, height=5)
txt_input.pack(pady=5)

# Button to parse the sentence
btn_parse = tk.Button(window, text="Parse Sentence", command=parse_and_show_np_chunks)
btn_parse.pack(pady=5)

# Output text widget
lbl_output = tk.Label(window, text="Noun Phrase Chunks:")
lbl_output.pack(pady=5)
txt_output = scrolledtext.ScrolledText(window, height=10)
txt_output.pack(pady=5)

# Run the GUI application
window.mainloop()