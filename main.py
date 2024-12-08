import pyttsx3
import customtkinter
from tkinter import messagebox,ttk

root = customtkinter.CTk()
root.title("Receptionist")
root.geometry("400x350")
root.resizable(False, False)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

engine = pyttsx3.init()

def details():
    query = chkbox_1.get()
    prb = str(query)
    if prb.lower() == "admission":
        engine.say("Please meet Ms. Amardeep")
        engine.runAndWait()
    if query != "":
        engine.say("Please meet Ms. Amardip")
        engine.runAndWait()
    elif prb.lower() == "class incharges":
        messagebox.showinfo("Reception", """VI A	Munirka Ahuja
VI B	Avneet Kaur
VI C	Simranjot Kaur
VI D	Renu Bala
VII A	Rupinder Kaur
VII B	Sharandeep Kaur
VII C	Geetanjali Verma
VII D	Chandni Duggal
VIII A	Isha Arora
VIII B	Harpreet Kaur Gugnani
VIII C	Deepa Singh
VIII D	Yogita Sood
VIII E	Gurdish Kaur
IX A	Rajbrinder Kaur
IX B	Meena Khanna
IX C	Punam Sahi
IX D	Isha Kapoor
X A	Yogesh Kumar
X B	Shweta Kumari
X C	Tarannum Goyal
X D	Upasna Pathak
XI A	Himanshu Sharma
XI B	Simran Narang
XI C	Mandeep Kaur
XI D	Meenakshi Arora
XI E	Nikhar Chopra
XII A	Kamal Jyoti
XII B	Jyoti Berry
XII C	Monika Sehgal
XII D	Ashwinder Kaur""")
    elif prb.lower() == "transport":
        messagebox.showinfo("Reception","""Route-1	Madhuban Enclave (near virdi kitchen, Eknaam real estate). More Store Barewal Road. Block- C (main road near Venus Saloon) Rajguru nagar. Royal Resort Rajguru nagar. Railway Crossing Rajguru nagar. Main road Block- CD (near Park) Rajguru nagar. Bhagat Naamdev chowk Rajguru nagar. HJBlock B.R.S.Nagar. Opp. Gurudwara. Makkar Stationary Block- I.BRS nagar. Gurudwara Singh Sabha Kutia Sahib Block- I. BRS nagar. Shitla Mata Mandir I-Block. BRS nagar. Gate no. 6 Block - G BRS nagar. Swami Vivekanand Flats opposite Laxmi Narayan Mandir Block- C. Main Gate Block- E ( Ranbir Fancy Dress towards Telephone exchange)\n.
Route-2	Field Ganj. Div no.-3. Baba Than Singh Chowk. Chhavi patshahi Gurudwara. CMC Hospital. Mini Rose Garden. Suffian chowk. Janakpuri. Cheema chowk. Vishkarma chowk. Cycle Market (Near Pannu pakoda). Overlock road. Main road dugri (Rajeshwari Apartments). Sant Fateh Singh Ngr Main gate.\n
Route-3	Bharat Nagar Chowk ( Jagraon Brigde to Sham nagar bus stand). LIC building sham nagar (bus stand to midda chowk). Midda chowk towards new model town. New model town (gurudwara or mandir). Kochar market chowk. Pink flats. Bhai wala chowk (b/s Ansal plaza road). Durga mata mandir. Sarabha nagar. Wok Singh Sarabha nagar. Hero bakery Pakhowal road.\n
Route-4	  Mall road. Fountain chowk. Kailash chowk. Dandi swami chowk. Haibowal aarey wala chowk. Ram Sharnam. Dr. Bassi Clinic (Kitchlu ngr. chowk). Rose garden. Police lines back road Avasthi Bone & Joint clinic. Gurudwara Guru Nanak Dev Ji (Saroj Khan Dance Academy /Aastha Hospital road.). Main Ferozeupr road opp. Maharaj ngr PAU gate. Aggar Nagar Block A-B Main gate.\n
Route-5	Gate no.5 Block – F SBS nagar. Prem Vihar. Main railway crossing road Block –H SBS nagar. Main gate. Block- G SBS nagar. New B.R.S. nagar near railway crossing. Gate no. 6, Housefed Complex, Block- E. SBS nagar, Main gate. Housefed Complex, Block- D ( Housefed Complex road), Rajeev enclave, Block –D. SBS nagar. Vikas nagar Extn., (Indoor Stadium road.). Punjab mata nagar chowk (Fauji Karayana). Pal milk dairy, U-turn from canal. Vishal nagar main road. Pink flats main gate (sua
road). Sua road. Jawaddi Gurudwara. Phullawal Road. Phase-III Flats. Phase III. Army Flats.\n
Route-6	Palam Vihar Main gate. Omaxe main gate.\n
Route-7	Gill chowk, Sangeet Cinema, Basant park (Janta ngr road), Kot Mangal Singh chowk, Janata ngr chowk, ATI road (Itta wala chowk), D.S.Lotey dharamkanda. I.T.I, Sabzi Mandi nr. Dussehra ground Isher ngr bridge. Canal road toward Dugri.\n
Route-8	Gill Village Main chowk, nr. Harry petrol pump, Ranjit Avenue(Mc.Donald chowk), Ranjit Avenue Phase 2 (Main gate), Delta city main gate, Gold dust colony main gate, Alamgir enclave main gate J.K Resort, Star enclave, Chopra real estate (mkt) Canal View Bulara. Main gate canal view nr water tank. Bikhu Agro Ind. (Isher ngr) Stamina Gym road. A-one dhaba (Bachittar ngr road)\n
Route-9	Janta Enclave Gate main road. Janta enclave water tank near Rama properties. Prabhu Ji Road Joginder Pandit. Basant Avenue (post office road towards Pal Estate). Jassal house. Makkar colony road. Paradise mansion-I, II adj, Basant Avenue. Sahiba traders double road Basant Avenue. SBI ATM road. Shiv Durga Mandir DAV school road. Babbu Karyana road Rock Look salon. DAV School road. Bamba Farms Basant avenue near DAV school. Lotia dreamlane road (Shant Gupta
hardware store.). Green park basant avenue ext. 9 Kali Mata Mandir. Shikha Tutorials yoga par. Supreme property consultant. Guru Nanak Dairy near flower chowk.\n
Route-10	Under Bridge near Sewa kender (Dabbu). Chintpurni Mandir. Park (transformer, backside Reliance fresh). Pandit ji fruit & juice. Baba Deep Singh chowk gate no. 8. Hotel Silver Stone mkt. Gurudwara Santokhsar Singh Sabha. Oster Safrina Outlet road. Chowk b/s Harkrishan Public School(Baba Shaheed Gilan wale). Kehar Gas Service mkt. Ram Park gate. Bharat Petrol Pump Dugri.\n
Route-11	B/S Johar Kothi road. Central Model School B/s Chevron Hotel. Sethi Study Circle road. Chaupati road opp. Shah Nursing home. Harnam nagar road to GTB Hospital road. Ishmeet Singh chowk. Krishna Mandir. Jagdev woodwork market. Gurudwara Singh Sabha (Dugri, Green Avenue gate), Anna Green park to Smile playway school board. Urban Estate welfare society gate, Shamshan ghat
(Dugri village). Durga mandir. Cherubs Playway school road.\n
Route-12	Kiran vihar main road, Kiran vihar lane 4 main road, kiran vihar xtn. main road, Dev chowk, Threeke main road, Basant city main gate main road, Raja diary, T-point near park, Basant city main road, Le Palm Flats main road, Nirmal enclave Basant city, Basant city main chowk, Centra Greens main gate, Amrit sagar chowk, Phullanwal, Ambey Medicos Phullanwal, Phullanwal.\n
Route-13	 Bhai Himmat singh nagar (Sua road), Nitesh Vihar (Main Gate), 200 ft. road, Bhagat Singh Nagar, Dhandra road. G. K. Vihar Gate no. 2 , Ekta Vihar(Main gate), Glada Flats. Gate no.1 Green Valley welfare society. Gate no.4 Green Valley welfare society. Gate no.3 Golden line (opp. Greenland School). Gate no.1 Golden line. Main gate Sukhmani welfare society.\n
Route-15	Fauji dhaba opp. Merryland palace. Laal kothi road. Dhaka colony to Dr. Vibhu Narad …road. Tirkona park to Noor medical road. Noor Medical road to Grace Beauty salon road. Verka Booth Gulati chowk road. Gulati chowk. Bikaner sweets to Timmy Bakery road. More store, Model town. Tirkona park to Baba Deep Singh Gurudwara road. Swami Vivekanand meditation Pyramid road to Dugri signal (canal road).""")
    elif prb.lower() == "fee structure":
        engine.say("Please meet Ms. Aamardeep")
        engine.runAndWait()



#LABEL
label_1 = customtkinter.CTkLabel(root, text="Receptionist",font=("Helvetica",30,"bold"))
label_1.pack(padx=10,pady=10)
#CHECKBOX
chkbox_1 = customtkinter.CTkComboBox(root, values=["Admission","Class Incharges","Transport","Fee Structure"],width=300)
chkbox_1.set("Choose your query")
chkbox_1.pack(padx=20,pady=30)
#ENTRY1
entry_1 = customtkinter.CTkEntry(root, placeholder_text="Query: ", height=45, width=800)
entry_1.pack(padx=20,pady=30)

button_2 = customtkinter.CTkButton(root, text="Enter", height=30, width=155, command = details)
button_2.pack(padx=20,pady=30)

root.mainloop()
