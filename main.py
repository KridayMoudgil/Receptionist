from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import customtkinter
import tkinter as tk
import pyttsx3

root = customtkinter.CTk()
root.geometry("900x600")
root.resizable(False, False)
root.title("BBPS Office Manager")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

engine = pyttsx3.init()

template = """
Answer the question below.
You are a receptionist for Bal Bharati Public School, Ludhiana. You don't have a name.
The principal of the school is Mr. Ashish Sawhney.
The head mistress of the school is Ms. Amardeep. 
Your job is to handle all the admission related processes.
You have to ask the parents of the student to ask them to forward all the details on bbps123@gmail.com. For any other queries, you have to ask the parents to organize a meeting with Ms. Amardeep.
Here is the list of class incharges:
VI A	Munirka Ahuja.
VI B	Avneet Kaur.
VI C	Simranjot Kaur.
VI D	Renu Bala.
VII A	Rupinder Kaur.
VII B	Sharandeep Kaur.
VII C	Geetanjali Verma.
VII D	Chandni Duggal.
VIII A	Isha Arora.
VIII B	Harpreet Kaur Gugnani.
VIII C	Deepa Singh.
VIII D	Anchal Sharma.
VIII E	Gurdish Kaur.
IX A	Rajbrinder Kaur.
IX B	Meena Khanna.
IX C	Punam Sahi.
IX D	Isha Kapoor.
IX E	Yogita Sood.
X A	Yogesh Kumar.
X B	Shweta Kumari.
X C	Tarannum Goyal.
X D	Upasna Pathak.
XI A	Himanshu Sharma.
XI B	Simran Narang.
XI C	Mandeep Kaur.
XI D	Meenakshi Arora.
XI E	Nikhar Chopra.
XII A	Kamal Jyoti.
XII B	Jyoti Berry.
XII C	Monika Sehgal.
XII D	Ashwinder Kaur.

Here is the conversation history: {context}
Question : {question}
Answer : """

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

context = ""
def handle_conversation():
    global context

    user_input = entry_1.get()
    response_label.configure(state="normal")
    response_label.insert(tk.END, "Generating...\n\n")
    response_label.yview(tk.END)
    root.update()
    result = chain.invoke({"context": context, "question": user_input})
    response = str(result)
    response_label.configure(state="normal")
    response_label.insert(tk.END, f"Reception: \n\n{response}\n\n")
    response_label.configure(state="disabled")
    response_label.yview(tk.END)
    context += f"\nUser: {user_input}\nAI: {result}"


def say_response():
    context = ""
    user_input = entry_1.get()
    result = chain.invoke({"context": context, "question": user_input})
    response = str(result)
    engine.say(response)
    engine.runAndWait()


label_1 = customtkinter.CTkLabel(root, text="Office Manager", font=("Roboto", 40, "bold"))
label_1.pack(padx=5, pady=10)

entry_1 = customtkinter.CTkEntry(root, placeholder_text="Prompt: ", height=45, width=800)
entry_1.pack(padx=50, pady=10)

button_1 = customtkinter.CTkButton(root, text="Generate Response", height=30, width=155, command=handle_conversation,fg_color='dark green')
button_1.pack(padx=60, pady=10)

button_2 = customtkinter.CTkButton(root, text="Say Response", height=30, width=155, command=say_response,fg_color='dark green')
button_2.pack(padx=70, pady=10)

# Scrollable frame for responses
frame = customtkinter.CTkFrame(root, bg_color="#000")
frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

scrollbar = customtkinter.CTkScrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

response_label = customtkinter.CTkTextbox(frame, wrap=tk.WORD, height=20, font=("Helvetica", 15), state="normal",
                                          yscrollcommand=scrollbar.set)
response_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.configure(command=response_label.yview)




root.mainloop()
