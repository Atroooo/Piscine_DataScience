from DiamondTrap import King


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

Joffrey = King("JoffreyT")
try:
    Joffrey.set_eyes(1)
except Exception as e:
    print(e)

try:
    Joffrey.set_hairs(1)
except Exception as e:
    print(e)
