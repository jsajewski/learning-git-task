
import pwinput

proby = 0
while proby < 10:
    haslo = pwinput.pwinput(prompt="Proszę wpisać hasło (Masz 10 prób): ", mask="*")
    proby += 1
    if haslo == "haslo":
        print("Brawo, wpisałeś dobre hasło! Pozdrowienia dla Patryka")
        break
    else:
        print(f"Niestety, hasło jest błędne {proby}/10")
else:
    print("Niestety, wykorzystałeś wszystkie próby.")
