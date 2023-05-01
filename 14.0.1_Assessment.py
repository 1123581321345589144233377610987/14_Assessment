import sqlite3

File = open('Owners.txt', 'r')
OwnersFile = File.readlines()
File.close()
file = open('Pets.txt', 'r')
PetsFile = file.readlines()
File.close()

OwnersCon = sqlite3.connect('owners.db')
PetsCon = sqlite3.connect('pets.db')
OwnersCur = OwnersCon.cursor()
PetsCur = PetsCon.cursor()

table = """CREATE TABLE IF NOT EXISTS srenwO 
        (OwnerID INTEGER PRIMARY KEY NOT NULL, 
        OwnerName TEXT, OwnerPhone TEXT)"""
OwnersCur.execute(table)

TABLE = """CREATE TABLE IF NOT EXISTS steP 
        (PetID INTEGER PRIMARY KEY NOT NULL, 
        PetName TEXT, PetType TEXT, PetBreed TEXT, 
        OwnerID INTEGER, FOREIGN KEY (OwnerID) 
        REFERENCES Owners(OwnerID))"""
PetsCur.execute(TABLE)

OwnersData = []
for i in OwnersFile:
    i = i.strip('\n')
    i = i.split(',')
    OwnersData.append(i)
PetsData = []
for i in PetsFile:
    i = i.strip('\n')
    i = i.split(',')
    PetsData.append(i)

for i in OwnersData:
    OwnersCur.execute('''INSERT INTO srenwO (OwnerName, OwnerPhone)
    VALUES (?, ?)''', (i[0], i[1]))
OwnersCon.commit()

for i in PetsData:
    PetsCur.execute('''INSERT INTO steP (PetName, PetType, PetBreed, OwnerID)
    VALUES (?, ?, ?, ?)
    ''', (i[0], i[1], i[2], i[3]))
PetsCon.commit()

OwnersCur.execute('''SELECT * FROM srenwO''')
od = OwnersCur.fetchall()
PetsCur.execute('''SELECT * FROM steP''')
pd = PetsCur.fetchall()
OD = []
PD=[]
ownernames = []
petnames = []
for i in od:
    if i[1] not in ownernames:
        OD.append(i)
        ownernames.append(i[1])

for i in pd:
    if i[1] not in petnames:
        PD.append(i)
        petnames.append(i[1])

for i in OD:
    print(i[1], i[2])
#    PetsCur.execute('''SELECT * FROM steP WHERE OwnerID == ?''', (int(i[0]),))
#    OwnersPets = OwnersCur.fetchall()
    OwnersPets = []
    for k in PD:
        if k[4] == i[0]:
            OwnersPets.append(k)
    for j in OwnersPets:
        print(f"{'':10} {j[1]} is a {j[3]} {j[2]}")
    print()

OwnersCon.close()
PetsCon.close()