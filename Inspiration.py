import requests
import json
from tkinter import *
from tkinter import messagebox
import sqlite3

stoic_quotes = Tk()
stoic_quotes.title("Stoic Wisdom")
#stoic_quotes.iconbitmap("iconfile.ico")


con = sqlite3.connect("StoicWisdomGUIProject/SavedQuotes.db")
cObj = con.cursor()
con.commit()


cObj.execute(" CREATE TABLE IF NOT EXISTS Saved(id INTEGER PRIMARY KEY AUTOINCREMENT, Writer TEXT, Quote TEXT)" )                           
con.commit()

#cObj.execute("DELETE FROM Saved WHERE id=8")
#con.commit()                                




'''
def stoic_quotes():
stoic_writers = [

           {
               'author': 'Marcus Aurelius'
           }
        ,

           {
               'author': 'TheStoicEmperor'
           }
]
'''
def stoic_wisdom():
        

    
    
        api_request = requests.get('https://api.themotivate365.com/stoic-quote')
        api = json.loads(api_request.content)

        x = api['data']['author']
        y = api['data']['quote']

        def store_db():
            cObj.execute("INSERT INTO SAVED(Writer, Quote) VALUES(?, ?)" , (x,y ) )
            messagebox.showinfo("Notification", "Quote has been saved!")
            con.commit()
            
            
    
        wisdom_from = Label(stoic_quotes, text = "Wisdom From:",bg= "Light Pink" , fg = "Black" , font="Ariel 18", borderwidth=1, relief="groove", padx="4", pady="4"  )
        wisdom_from.grid(row=1, column=0, sticky= N+S+W+E)

        fetch_writer = Label(stoic_quotes, text = api['data']['author'] ,bg= "Light Blue" , fg = "Black", font="Ariel 18", borderwidth=1, relief="groove", padx="4", pady="4")
        fetch_writer.grid(row=1, column=1, sticky= N+S+W+E)


        quote_label = Label(stoic_quotes, text = "Quote:",bg= "Light Pink" , fg = "Black", font="Ariel 18", borderwidth=1, relief="groove", padx="4", pady="4" )
        quote_label.grid(row=2, column=0, sticky= N+S+W+E)    
    
        fetch_quote = Message(stoic_quotes, text = api['data']['quote'] ,bg= "Light Blue" , fg = "Black", font="Ariel 18", borderwidth=1, relief="groove", padx="4", pady="4"  )
        fetch_quote.grid(row= 2, column=1, sticky= N+S+W+E)
        
        next_quote = Button(stoic_quotes, text = "Next", bg= "Green", command = stoic_wisdom,  fg = "Blue", font="Ariel 18", borderwidth=1, relief="groove", padx="4", pady="4" )
        next_quote.grid(row= 3, column=1, sticky= N+S+W+E)    

        save_quote = Button(stoic_quotes, text = "Save", bg= "Green", command = store_db,  fg = "Blue", font="Ariel 18", borderwidth=1, relief="groove", padx="4", pady="4" )
        save_quote.grid(row= 3, column=0, sticky= N+S+W+E)  
        
        api = ''
        
        

        
        

stoic_wisdom()
stoic_quotes.mainloop()

cObj.close()
con.close()
