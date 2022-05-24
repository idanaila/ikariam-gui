from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# DB configuration

connection = sqlite3.connect('ikariam_db.db')

# create cursor

cu = connection.cursor()

# create  table

cu.execute(""" CREATE TABLE if not exists buildings (
    city text,
    tw integer,
    academy integer,
    warehouse integer,
    tavern integer,
    palace integer,
    gresidence integer,
    museum integer,
    port integer,
    shipyard integer,
    barracks integer,
    townwall integer,
    embassy integer,
    tradingpost integer,
    workshop integer,
    hideout integer,
    forester integer,
    glassblower integer,
    alchemist integer,
    winery integer,
    stonemason integer,
    carpenter integer,
    optician integer,
    firework integer,
    winepress integer,
    architect integer,
    temple integer,
    depot integer,
    pirate integer,
    market integer,
    seachart integer)
    """)

# commit changes

connection.commit()

# close out connection to the DB

connection.close()

def query_db():
    connection = sqlite3.connect('ikariam_db.db')
    cu = connection.cursor()

    cu.execute("SELECT rowid, * FROM buildings")
    records = cu.fetchall()
    # add our data to the screen

    global count
    count = 0

    for record in records:
        tr.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16], record[17], record[18], record[19], record[20], record[21], record[22], record[23], record[24], record[25], record[26], record[27], record[28], record[29], record[30], record[31]))
        count += 1

    connection.commit()
    connection.close()

prog = Tk()
prog.title('Ikariam DB')
prog.geometry("1366x768")
#prog.attributes("-fullscreen", False)

# style

style = ttk.Style()

# select the theme

style.theme_use('default')

# configure colors

style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")

# change selectoed color

style.map('Treemap', background=[('selected', "#798082")])

# create a treeview frame

tree_frame = Frame(prog)
tree_frame.pack(pady=10)

# create the scrollbars; for X and Y axis

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree_scroll1 = Scrollbar(tree_frame, orient='horizontal')
tree_scroll1.pack(side=BOTTOM, fill=X)

# create the treeview

tr = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
tr = ttk.Treeview(tree_frame, xscrollcommand=tree_scroll1.set, selectmode="extended")
tr.pack()


# configure the scrollbar

tree_scroll.config(command=tr.yview)
tree_scroll1.config(command=tr.xview)

# define our colums

tr['columns'] = ("Oid", "City", "Town Hall", "Academy", "Warehouse", "Tavern", "Palace", "G Residence", "Museum", "Trading Port", "Shipyard", "Barracks", "Town Wall", "Embassy", "Trading Post", "Workshop", "Hideout", "Forester", "Glassblower", "Alchemist", "Winery", "Stonemason", "Carpenter", "Optician", "Firework", "Wine Press", "Architect", "Temple", "Depot", "Pirate Fortress", "Black Market", "Sea Chart")

# format our columns

tr.column("#0", width=0, stretch=NO)
tr.column("Oid", anchor=CENTER, width=100)
tr.column("Town Hall", anchor=CENTER, width=100)
tr.column("Academy", anchor=CENTER, width=100)
tr.column("Warehouse", anchor=CENTER, width=100)
tr.column("Tavern", anchor=CENTER, width=100)
tr.column("Palace", anchor=CENTER, width=100)
tr.column("G Residence", anchor=CENTER, width=100)
tr.column("Museum", anchor=CENTER, width=100)
tr.column("Trading Port", anchor=CENTER, width=100)
tr.column("Shipyard", anchor=CENTER, width=100)
tr.column("Barracks", anchor=CENTER, width=100)
tr.column("Town Wall", anchor=CENTER, width=100)
tr.column("Embassy", anchor=CENTER, width=100)
tr.column("Trading Post", anchor=CENTER, width=100)
tr.column("Workshop", anchor=CENTER, width=100)
tr.column("Hideout", anchor=CENTER, width=100)
tr.column("Forester", anchor=CENTER, width=100)
tr.column("Glassblower", anchor=CENTER, width=100)
tr.column("Alchemist", anchor=CENTER, width=100)
tr.column("Winery", anchor=CENTER, width=100)
tr.column("Stonemason", anchor=CENTER, width=100)
tr.column("Carpenter", anchor=CENTER, width=100)
tr.column("Optician", anchor=CENTER, width=100)
tr.column("Firework", anchor=CENTER, width=100)
tr.column("Wine Press", anchor=CENTER, width=100)
tr.column("Architect", anchor=CENTER, width=100)
tr.column("Temple", anchor=CENTER, width=100)
tr.column("Depot", anchor=CENTER, width=100)
tr.column("Pirate Fortress", anchor=CENTER, width=100)
tr.column("Black Market", anchor=CENTER, width=100)
tr.column("Sea Chart", anchor=CENTER, width=100)

# create teh headings

tr.heading("Oid", text="Oid", anchor=W)
tr.heading("City", text="City", anchor=W)
tr.heading("Town Hall", text="Town Hall", anchor=CENTER)
tr.heading("Academy", text="Academy", anchor=CENTER)
tr.heading("Warehouse", text="Warehouse", anchor=CENTER)
tr.heading("Tavern", text="Tavern", anchor=CENTER)
tr.heading("Palace", text="Palace", anchor=CENTER)
tr.heading("G Residence", text="G Residence", anchor=CENTER)
tr.heading("Museum", text="Museum", anchor=CENTER)
tr.heading("Trading Port", text="Trading Port", anchor=CENTER)
tr.heading("Shipyard", text="Shipyard", anchor=CENTER)
tr.heading("Barracks", text="Barracks", anchor=CENTER)
tr.heading("Town Wall", text="Town Wall", anchor=CENTER)
tr.heading("Embassy", text="Embassy", anchor=CENTER)
tr.heading("Trading Post", text="Trading Post", anchor=CENTER)
tr.heading("Workshop", text="Workshop", anchor=CENTER)
tr.heading("Hideout", text="Hideout", anchor=CENTER)
tr.heading("Forester", text="Forester", anchor=CENTER)
tr.heading("Glassblower", text="Glassblower", anchor=CENTER)
tr.heading("Alchemist", text="Alchemist", anchor=CENTER)
tr.heading("Winery", text="Winery", anchor=CENTER) 
tr.heading("Stonemason", text="Stonemason", anchor=CENTER)
tr.heading("Carpenter", text="Carpenter", anchor=CENTER)
tr.heading("Optician", text="Optician", anchor=CENTER)
tr.heading("Firework", text="Firework", anchor=CENTER)
tr.heading("Wine Press", text="Wine Press", anchor=CENTER)
tr.heading("Architect", text="Architect", anchor=CENTER)
tr.heading("Temple", text="Temple", anchor=CENTER)
tr.heading("Depot", text="Depot", anchor=CENTER)
tr.heading("Pirate Fortress", text="Pirate", anchor=CENTER)
tr.heading("Black Market", text="Black Market", anchor=CENTER) 
tr.heading("Sea Chart", text="Sea Chart", anchor=CENTER)


# add record entry boxes

data_frame = LabelFrame(prog)
data_frame.pack(fill="x", expand="yes", padx=10)

oid_label = Label(data_frame, text="Oid")
oid_label.grid(row=0, column=0, padx=10, pady=10)
oid_entry= Entry(data_frame)
oid_entry.grid(row=0, column=1, padx=10, pady=10)

city_label = Label(data_frame, text="City")
city_label.grid(row=0, column=0, padx=10, pady=10)
city_entry= Entry(data_frame)
city_entry.grid(row=0, column=1, padx=10, pady=10)

tw_label = Label(data_frame, text="Town Hall")
tw_label.grid(row=0, column=2, padx=10, pady=10)
tw_entry= Entry(data_frame)
tw_entry.grid(row=0, column=3, padx=10, pady=10)

academy_label = Label(data_frame, text="Academy")
academy_label.grid(row=0, column=4, padx=10, pady=10)
academy_entry= Entry(data_frame)
academy_entry.grid(row=0, column=5, padx=10, pady=10)

warehouse_label = Label(data_frame, text="Warehouse")
warehouse_label.grid(row=0, column=6, padx=10, pady=10)
warehouse_entry= Entry(data_frame)
warehouse_entry.grid(row=0, column=7, padx=10, pady=10)

tavern_label = Label(data_frame, text="Tavern")
tavern_label.grid(row=1, column=0, padx=10, pady=10)
tavern_entry= Entry(data_frame)
tavern_entry.grid(row=1, column=1, padx=10, pady=10)

palace_label = Label(data_frame, text="Palace")
palace_label.grid(row=1, column=2, padx=10, pady=10)
palace_entry= Entry(data_frame)
palace_entry.grid(row=1, column=3, padx=10, pady=10)

gresidence_label = Label(data_frame, text="G Residence")
gresidence_label.grid(row=1, column=4, padx=10, pady=10)
gresidence_entry= Entry(data_frame)
gresidence_entry.grid(row=1, column=5, padx=10, pady=10)

museum_label = Label(data_frame, text="Museum")
museum_label.grid(row=1, column=6, padx=10, pady=10)
museum_entry= Entry(data_frame)
museum_entry.grid(row=1, column=7, padx=10, pady=10)

port_label = Label(data_frame, text="Trading Port")
port_label.grid(row=2, column=0, padx=10, pady=10)
port_entry= Entry(data_frame)
port_entry.grid(row=2, column=1, padx=10, pady=10)

shipyard_label = Label(data_frame, text="Shipyard")
shipyard_label.grid(row=2, column=2, padx=10, pady=10)
shipyard_entry= Entry(data_frame)
shipyard_entry.grid(row=2, column=3, padx=10, pady=10)

barracks_label = Label(data_frame, text="Barracks")
barracks_label.grid(row=2, column=4, padx=10, pady=10)
barracks_entry= Entry(data_frame)
barracks_entry.grid(row=2, column=5, padx=10, pady=10)

townwall_label = Label(data_frame, text="Town Wall")
townwall_label.grid(row=2, column=6, padx=10, pady=10)
townwall_entry= Entry(data_frame)
townwall_entry.grid(row=2, column=7, padx=10, pady=10)

embassy_label = Label(data_frame, text="Embassy")
embassy_label.grid(row=3, column=0, padx=10, pady=10)
embassy_entry= Entry(data_frame)
embassy_entry.grid(row=3, column=1, padx=10, pady=10)

tradingpost_label = Label(data_frame, text="Trading Post")
tradingpost_label.grid(row=3, column=2, padx=10, pady=10)
tradingpost_entry= Entry(data_frame)
tradingpost_entry.grid(row=3, column=3, padx=10, pady=10)

workshop_label = Label(data_frame, text="Workshop")
workshop_label.grid(row=3, column=4, padx=10, pady=10)
workshop_entry= Entry(data_frame)
workshop_entry.grid(row=3, column=5, padx=10, pady=10)

hideout_label = Label(data_frame, text="Hideout")
hideout_label.grid(row=3, column=6, padx=10, pady=10)
hideout_entry= Entry(data_frame)
hideout_entry.grid(row=3, column=7, padx=10, pady=10)

forester_label = Label(data_frame, text="Forester")
forester_label.grid(row=4, column=0, padx=10, pady=10)
forester_entry= Entry(data_frame)
forester_entry.grid(row=4, column=1, padx=10, pady=10)

glassblower_label = Label(data_frame, text="Glassblower")
glassblower_label.grid(row=4, column=2, padx=10, pady=10)
glassblower_entry= Entry(data_frame)
glassblower_entry.grid(row=4, column=3, padx=10, pady=10)

alchemist_label = Label(data_frame, text="Alchemist")
alchemist_label.grid(row=4, column=4, padx=10, pady=10)
alchemist_entry= Entry(data_frame)
alchemist_entry.grid(row=4, column=5, padx=10, pady=10)

winery_label = Label(data_frame, text="Winery")
winery_label.grid(row=4, column=6, padx=10, pady=10)
winery_entry= Entry(data_frame)
winery_entry.grid(row=4, column=7, padx=10, pady=10)

stonemason_label = Label(data_frame, text="Stonemason")
stonemason_label.grid(row=5, column=0, padx=10, pady=10)
stonemason_entry= Entry(data_frame)
stonemason_entry.grid(row=5, column=1, padx=10, pady=10)

carpenter_label = Label(data_frame, text="Carpenter")
carpenter_label.grid(row=5, column=2, padx=10, pady=10)
carpenter_entry= Entry(data_frame)
carpenter_entry.grid(row=5, column=3, padx=10, pady=10)

optician_label = Label(data_frame, text="Optician")
optician_label.grid(row=5, column=4, padx=10, pady=10)
optician_entry= Entry(data_frame)
optician_entry.grid(row=5, column=5, padx=10, pady=10)

firework_label = Label(data_frame, text="Firework")
firework_label.grid(row=5, column=6, padx=10, pady=10)
firework_entry= Entry(data_frame)
firework_entry.grid(row=5, column=7, padx=10, pady=10)

winepress_label = Label(data_frame, text="Wine Press")
winepress_label.grid(row=6, column=0, padx=10, pady=10)
winepress_entry= Entry(data_frame)
winepress_entry.grid(row=6, column=1, padx=10, pady=10)

architect_label = Label(data_frame, text="Architect")
architect_label.grid(row=6, column=2, padx=10, pady=10)
architect_entry= Entry(data_frame)
architect_entry.grid(row=6, column=3, padx=10, pady=10)

temple_label = Label(data_frame, text="Temple")
temple_label.grid(row=6, column=4, padx=10, pady=10)
temple_entry= Entry(data_frame)
temple_entry.grid(row=6, column=5, padx=10, pady=10)

depot_label = Label(data_frame, text="Depot")
depot_label.grid(row=6, column=6, padx=10, pady=10)
depot_entry= Entry(data_frame)
depot_entry.grid(row=6, column=7, padx=10, pady=10)

pirate_label = Label(data_frame, text="Pirate Fortress")
pirate_label.grid(row=7, column=0, padx=10, pady=10)
pirate_entry= Entry(data_frame)
pirate_entry.grid(row=7, column=1, padx=10, pady=10)

market_label = Label(data_frame, text="Black Market")
market_label.grid(row=7, column=2, padx=10, pady=10)
market_entry= Entry(data_frame)
market_entry.grid(row=7, column=3, padx=10, pady=10)

seachart_label = Label(data_frame, text="Sea Chart")
seachart_label.grid(row=7, column=4, padx=10, pady=10)
seachart_entry= Entry(data_frame)
seachart_entry.grid(row=7, column=5, padx=10, pady=10)

def remove():

    # add box asking for deletion confirmation

    res = messagebox.askyesno('Confirmation', 'Do you want to remove the record?')
    if res == True:
        x = tr.selection()[0]
        tr.delete(x)
        connection = sqlite3.connect('ikariam_db.db')
        cu = connection.cursor()
        cu.execute("DELETE from buildings WHERE oid=" + oid_entry.get())
        connection.commit()
        connection.close()
        clear_entries()
    elif res == False:
        pass
    else:
        messagebox.showerror('error', 'Somenthing went wrong! Try again.')


def update():
    selected = tr.focus()
    tr.item(selected, text="", values=(oid_entry.get(), city_entry.get(), tw_entry.get(), academy_entry.get(), warehouse_entry.get(), tavern_entry.get(), palace_entry.get(), gresidence_entry.get(), museum_entry.get(), port_entry.get(), shipyard_entry.get(), barracks_entry.get(), townwall_entry.get(), embassy_entry.get(), tradingpost_entry.get(), workshop_entry.get(), hideout_entry.get(), forester_entry.get(), glassblower_entry.get(), alchemist_entry.get(), winery_entry.get(), stonemason_entry.get(), carpenter_entry.get(), optician_entry.get(), firework_entry.get(), winepress_entry.get(), architect_entry.get(), temple_entry.get(), depot_entry.get(), pirate_entry.get(), market_entry.get(), seachart_entry.get(),))

    # update the DB

    connection = sqlite3.connect('ikariam_db.db')
    cu = connection.cursor()

    cu.execute("""UPDATE buildings SET
        oid = :oid,
        city = :city,
        tw = :tw,
        academy = :academy,
        warehouse = :warehouse,
        tavern = :tavern,
        palace = :palace,
        gresidence = :gresidence,
        museum = :museum,
        port = :port,
        shipyard = :shipyard,
        barracks = :barracks,
        townwall = :townwall,
        embassy = :embassy,
        tradingpost = :tradingpost,
        workshop = :workshop,
        hideout = :hideout,
        forester = :forester,
        glassblower = :glassblower,
        alchemist = :alchemist,
        winery = :winery,
        stonemason = :stonemason,
        carpenter = :carpenter,
        optician = :optician,
        firework = :firework,
        winepress = :winepress,
        architect = :architect,
        temple = :temple,
        depot = :depot,
        pirate = :pirate,
        market = :market,
        seachart = :seachart
        
        WHERE oid = :oid""",
        
        {
            'oid': oid_entry.get(),
            'city': city_entry.get(),
            'tw': tw_entry.get(),
            'academy': academy_entry.get(),
            'warehouse': warehouse_entry.get(),
            'tavern': tavern_entry.get(),
            'palace': palace_entry.get(),
            'gresidence': gresidence_entry.get(),
            'museum': museum_entry.get(),
            'port': port_entry.get(),
            'shipyard': shipyard_entry.get(),
            'barracks': barracks_entry.get(),
            'townwall': townwall_entry.get(),
            'embassy': embassy_entry.get(),
            'tradingpost': tradingpost_entry.get(),
            'workshop': workshop_entry.get(),
            'hideout': hideout_entry.get(),
            'forester': forester_entry.get(),
            'glassblower': glassblower_entry.get(),
            'alchemist': alchemist_entry.get(),
            'winery': winery_entry.get(),
            'stonemason': stonemason_entry.get(),
            'carpenter': carpenter_entry.get(),
            'optician': optician_entry.get(),
            'firework': firework_entry.get(),
            'winepress': winepress_entry.get(),
            'architect': architect_entry.get(),
            'temple': temple_entry.get(),
            'depot': depot_entry.get(),
            'pirate': pirate_entry.get(),
            'market': market_entry.get(),
            'seachart': seachart_entry.get()
        
        })

    connection.commit()
    connection.close()
    clear_entries()

def clear_entries():

    # clear boxes from the gui view

    oid_entry.delete(0, END)
    city_entry.delete(0, END)
    tw_entry.delete(0, END)
    academy_entry.delete(0, END)
    warehouse_entry.delete(0, END)
    tavern_entry.delete(0, END)
    palace_entry.delete(0, END)
    gresidence_entry.delete(0, END)
    museum_entry.delete(0, END)
    port_entry.delete(0, END)
    shipyard_entry.delete(0, END)
    barracks_entry.delete(0, END)
    townwall_entry.delete(0, END)
    embassy_entry.delete(0, END)
    tradingpost_entry.delete(0, END)
    workshop_entry.delete(0, END)
    hideout_entry.delete(0, END)
    forester_entry.delete(0, END)
    glassblower_entry.delete(0, END)
    alchemist_entry.delete(0, END)
    winery_entry.delete(0, END)
    stonemason_entry.delete(0, END)
    carpenter_entry.delete(0, END)
    optician_entry.delete(0, END)
    firework_entry.delete(0, END)
    winepress_entry.delete(0, END)
    architect_entry.delete(0, END)
    temple_entry.delete(0, END)
    depot_entry.delete(0, END)
    pirate_entry.delete(0, END)
    market_entry.delete(0, END)
    seachart_entry.delete(0, END)


def select_record(e):
    # clear boxes

    clear_entries()

    # grab record number

    selected = tr.focus()

    # grab record values

    values = tr.item(selected, 'values')

    # output to entry boxes

    oid_entry.insert(0, values[0])
    city_entry.insert(0, values[1])
    tw_entry.insert(0, values[2])
    academy_entry.insert(0, values[3])
    warehouse_entry.insert(0, values[4])
    tavern_entry.insert(0, values[5])
    palace_entry.insert(0, values[6])
    gresidence_entry.insert(0, values[7])
    museum_entry.insert(0, values[8])
    port_entry.insert(0, values[9])
    shipyard_entry.insert(0, values[10])
    barracks_entry.insert(0, values[11])
    townwall_entry.insert(0, values[12])
    embassy_entry.insert(0, values[13])
    tradingpost_entry.insert(0, values[14])
    workshop_entry.insert(0, values[15])
    hideout_entry.insert(0, values[16])
    forester_entry.insert(0, values[17])
    glassblower_entry.insert(0, values[18])
    alchemist_entry.insert(0, values[19])
    winery_entry.insert(0, values[20])
    stonemason_entry.insert(0, values[21])
    carpenter_entry.insert(0, values[22])
    optician_entry.insert(0, values[23])
    firework_entry.insert(0, values[24])
    winepress_entry.insert(0, values[25])
    architect_entry.insert(0, values[26])
    temple_entry.insert(0, values[27])
    depot_entry.insert(0, values[28])
    pirate_entry.insert(0, values[29])
    market_entry.insert(0, values[30])
    seachart_entry.insert(0, values[31])


def add():

    connection = sqlite3.connect('ikariam_db.db')
    cu = connection.cursor()

    cu.execute("INSERT INTO buildings VALUES (:city, :tw, :academy, :warehouse, :tavern, :palace, :gresidence, :museum, :port, :shipyard, :barracks, :townwall, :embassy, :tradingpost, :workshop, :hideout, :forester, :glassblower, :alchemist, :winery, :stonemason, :carpenter, :optician, :firework, :winepress, :architect, :temple, :depot, :pirate, :market, :seachart)",
        {
            #'oid': oid_entry.get(),
            'city': city_entry.get(),
            'tw': tw_entry.get(),
            'academy': academy_entry.get(),
            'warehouse': warehouse_entry.get(),
            'tavern': tavern_entry.get(),
            'palace': palace_entry.get(),
            'gresidence': gresidence_entry.get(),
            'museum': museum_entry.get(),
            'port': port_entry.get(),
            'shipyard': shipyard_entry.get(),
            'barracks': barracks_entry.get(),
            'townwall': townwall_entry.get(),
            'embassy': embassy_entry.get(),
            'tradingpost': tradingpost_entry.get(),
            'workshop': workshop_entry.get(),
            'hideout': hideout_entry.get(),
            'forester': forester_entry.get(),
            'glassblower': glassblower_entry.get(),
            'alchemist': alchemist_entry.get(),
            'winery': winery_entry.get(),
            'stonemason': stonemason_entry.get(),
            'carpenter': carpenter_entry.get(),
            'optician': optician_entry.get(),
            'firework': firework_entry.get(),
            'winepress': winepress_entry.get(),
            'architect': architect_entry.get(),
            'temple': temple_entry.get(),
            'depot': depot_entry.get(),
            'pirate': pirate_entry.get(),
            'market': market_entry.get(),
            'seachart': seachart_entry.get()
        })
    connection.commit()
    connection.close()
    clear_entries()

    # update the program table as we added an entry; get the rows and delete them

    tr.delete(*tr.get_children())
    query_db()

def blevels():
    connection = sqlite3.connect('ikariam_db.db')
    cu = connection.cursor()

    bulev = cu.execute("SELECT SUM(tw + academy + warehouse + tavern + palace + gresidence + museum + port + shipyard + barracks + townwall + embassy + tradingpost + workshop + hideout + forester + glassblower + alchemist + winery + stonemason + carpenter + optician + firework + winepress + architect + temple + depot + pirate + market + seachart) as sum_score FROM buildings")
    bulev2 = bulev.fetchone()
    # bulev2 is a tuple; use join and str go get rid of () and ''
    bulev3 = " ".join(str(x) for x in bulev2)
    messagebox.showinfo('Building Levels', 'Building Levels: ' + str(bulev3))

    connection.commit()
    connection.close()
    clear_entries()

# add buttons

button_frame = LabelFrame(prog)
button_frame.pack(fill="x", expand="yes", padx=10)

select_button = Button(button_frame, text="Clear Entries", command=clear_entries)
select_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(button_frame, text="Update Record", command=update)
update_button.grid(row=0, column=1, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record", command=add)
add_button.grid(row=0, column=2, padx=10, pady=10)

remove_button = Button(button_frame, text="Remove Record", command=remove)
remove_button.grid(row=0, column=3, padx=10, pady=10)

blevels_button = Button(button_frame, text="Building Levels", command=blevels)
blevels_button.grid(row=0, column=6, padx=10, pady=10)

# bind the treeview

tr.bind("<ButtonRelease-1>", select_record)

# pull data from database upon start

query_db()

prog.mainloop()

