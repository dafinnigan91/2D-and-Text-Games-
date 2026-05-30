import sys
import random

################################
# UTILITY

def Dice():
    return random.randint(1, 20)

def get_input():
    return input("EXECUTE COMMAND: ").strip().lower()

################################
# PUZZLES

def Puzzle_1():
    """Unlock all doors puzzle - Fibonacci sequence reversed"""
    Answer1 = "1-1-2-3-5-8-13-21-34"
    print("DECODE MESSAGE: 2-1-5-34-13-1-32-18")
    guess = get_input()
    if guess == Answer1:
        # Unlock every room in the game
        for room in all_rooms:
            room.locked = False
        print("A voice sounds on the interface informing you that all doors are now unlocked.")
    else:
        print("Incorrect code.")

def Puzzle_2():
    """Eject Battle Mech into space puzzle - Pi reversed"""
    Answer2 = "3.1415926"
    print("DECODE MESSAGE: 6.2951413")
    guess = get_input()
    if guess == Answer2:
        if Battel_Mech in Space_Port_loading_deck.boss:
            Space_Port_loading_deck.boss.remove(Battel_Mech)
        Space_Port_loading_deck.locked = True
        print("A voice sounds and informs you the airlock doors are opening.")
        print("The contents of the loading deck have been ejected into space, including the Battle Mech.")
    else:
        print("Incorrect code.")

def Puzzle_3():
    """Kill Dakik Yamamoto with sunlight puzzle"""
    Answer3 = "deus ex machina"  # lowercased to match get_input()
    print("GOD FROM THE MACHINE")
    guess = get_input()
    if guess == Answer3:
        print("You hit enter on the interface. The metal shutters of the observation deck open silently.")
        print("As the image of Earth becomes visible from the space station you are hit with a beam of bright light.")
        if protagonist.room == Observation_deck and Dakik_Yamamoto in Observation_deck.boss:
            Dakik_Yamamoto.hp = 0
            Observation_deck.boss.remove(Dakik_Yamamoto)
            print("Dakik Yamamoto cries in agony as his withered body bursts into flame in the presence of the Sun's light!")
            print("A moment later he falls to the ground, dead, before turning to ash.")
        else:
            print("After a while the shutters close and you turn to go on your way.")
    else:
        print("Incorrect code.")

################################
# BACKPACK

class Backpack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_cap = 0
        self.items = []

    def pick_up(self, room, item_name):
        for item in room.items:
            if item.name.lower() == item_name.lower():
                if self.current_cap + item.weight <= self.capacity:
                    self.items.append(item)
                    room.items.remove(item)
                    self.current_cap += item.weight
                    print(f"{item.name} added to backpack.")
                else:
                    print("Backpack is at capacity.")
                return
        print(f"No item named '{item_name}' found in this room.")

    def put_down(self, room, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                room.items.append(item)
                self.current_cap -= item.weight
                print(f"{item.name} placed in {room.name}.")
                return
        print(f"You don't have '{item_name}' in your backpack.")

backpack = Backpack(100)

################################
# PROTAGONIST

class Protagonist:
    def __init__(self, room, name, hp, max_hp=100, strength=5, gold=100):
        self.room = room
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.strength = strength
        self.gold = gold
        self.equipped = []           # list of item objects
        self.backpack = backpack

    def show_room(self):
        print(self.room.description)

    def show_hp(self):
        print(f"HP: {self.hp}/{self.max_hp}")

    def show_backpack(self):
        if not self.backpack.items:
            print("Backpack is empty.")
        else:
            print("Backpack:", [i.name for i in self.backpack.items])

    def show_equipped(self):
        if not self.equipped:
            print("Nothing equipped.")
        else:
            print("Equipped:", [i.name for i in self.equipped])

    def go_to_room(self, new_room_name):
        for door in self.room.doors:
            if door.name.lower() == new_room_name.lower():
                if door.locked:
                    print(f"{door.name} is locked. You need a keycard.")
                    return
                self.room = door
                self.show_room()
                return
        print("That room isn't accessible from here.")

    # ---- COMBAT ----

    def Protag_strike(self, enemy):
        """
        Rolls d20. On > 5, deals roll + strength + any equipped weapon damage_mod.
        Armour damage_reduction on the enemy side is applied in boss_strike.
        """
        roll = Dice()
        weapon_bonus = sum(
            i.damage_mod for i in self.equipped if isinstance(i, Weapons)
        )
        if roll > 5:
            damage = roll + self.strength + weapon_bonus
            enemy.hp -= damage
            print(f"{self.name} hit {enemy.name} for {damage} damage! ({enemy.name} HP: {enemy.hp})")
        else:
            print(f"{enemy.name} dodged your attack!")

    def gain_XP(self):
        self.max_hp += 4
        self.hp = min(self.hp + 4, self.max_hp)   # small heal on level-up
        print(f"XP gained! Max HP increased by 4. Max HP = {self.max_hp}")

    # ---- ITEMS ----

    def equip(self, item_name):
        """Move item from backpack to equipped list."""
        for item in self.backpack.items:
            if item.name.lower() == item_name.lower():
                self.equipped.append(item)
                self.backpack.items.remove(item)
                self.backpack.current_cap -= item.weight
                print(f"{item.name} equipped.")
                return
        print(f"You don't have '{item_name}' in your backpack.")

    def unequip(self, item_name):
        """Move item from equipped back to backpack."""
        for item in self.equipped:
            if item.name.lower() == item_name.lower():
                self.equipped.remove(item)
                self.backpack.items.append(item)
                self.backpack.current_cap += item.weight
                print(f"{item.name} unequipped and returned to backpack.")
                return
        print(f"You don't have '{item_name}' equipped.")

    def use_potion(self, item_name):
        """Use a potion from the backpack by name."""
        for item in self.backpack.items:
            if item.name.lower() == item_name.lower():
                if isinstance(item, Potions):
                    if item.hp_restor:
                        self.hp = min(self.hp + item.hp_restor, self.max_hp)
                        print(f"Used {item.name}. HP restored. HP = {self.hp}/{self.max_hp}")
                    if item.hp_boost:
                        self.max_hp += item.hp_boost
                        self.hp = self.max_hp
                        print(f"Used {item.name}. Max HP increased by {item.hp_boost}. HP = {self.hp}/{self.max_hp}")
                    self.backpack.items.remove(item)
                    self.backpack.current_cap -= item.weight
                    return True   # signal that a turn was used
                else:
                    print(f"{item.name} is not a potion.")
                    return False
        print(f"You don't have '{item_name}' in your backpack.")
        return False

    def use_keycard(self, card_name):
        """
        Use a keycard from the backpack. Checks whether any door
        in the current room matches the keycard's access target.
        """
        for item in self.backpack.items:
            if item.name.lower() == card_name.lower():
                if isinstance(item, KeyCards):
                    # item.acsesses is the Room object the card unlocks
                    target_room = item.acsesses
                    # Check if that room is a door we can reach from here
                    if target_room in self.room.doors or target_room == self.room:
                        target_room.locked = False
                        self.backpack.items.remove(item)
                        self.backpack.current_cap -= item.weight
                        print(f"{item.name} used. {target_room.name} is now unlocked.")
                    else:
                        print(f"{item.name} doesn't unlock anything accessible from here.")
                    return
                else:
                    print(f"{item.name} is not a keycard.")
                    return
        print(f"You don't have '{card_name}' in your backpack.")

    def pick_up_money(self, item_name):
        """Picks up a Money item and adds its value to gold."""
        for item in self.room.items:
            if item.name.lower() == item_name.lower() and isinstance(item, Money):
                self.gold += item.amount
                self.room.items.remove(item)
                print(f"Picked up {item.name}. Gold: {self.gold}")
                return
        # If it wasn't money, fall through to normal pick_up
        self.backpack.pick_up(self.room, item_name)

################################
# BOSS

class Boss:
    def __init__(self, name, hp, strength, room=None):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.room = room

    def boss_strike(self, target):
        """
        Rolls d20. On > 5, deals roll + strength, reduced by target's
        equipped armour damage_reduction total.
        """
        roll = Dice()
        if roll > 5:
            raw_damage = roll + self.strength
            armour_reduction = sum(
                i.damage_reduction for i in target.equipped if isinstance(i, Armor)
            )
            damage = max(1, raw_damage - armour_reduction)  # always at least 1
            target.hp -= damage
            print(f"{self.name} hit {target.name} for {damage} damage! "
                  f"(blocked {armour_reduction}) HP: {target.hp}/{target.max_hp}")
        else:
            print(f"{target.name} dodged {self.name}'s attack!")

Training_Droid   = Boss("Training Bobby",     50,  0)
Sentine_Droid1   = Boss("Sentinal-25",        20,  1)
Sentine_Droid2   = Boss("Sentinal-26",        20,  1)
Sentine_Droid3   = Boss("Sentinal-27",        25,  1)
Sentine_Droid4   = Boss("Sentinal-Z",         30,  3)
Raptor_1         = Boss("Cyber Raptor S-243", 25,  2)
Raptor_2         = Boss("Cyber Raptor S-250", 25,  3)
Raptor_3         = Boss("Cyber Raptor S-278", 30,  3)
Raptor_4         = Boss("Cyber Raptor S-300", 40,  4)
Raptor_X         = Boss("Cyber Raptor X-7000",50,  7)
Turret_1         = Boss("Marshal-Turret",     75,  5)
Turret_2         = Boss("Synthetics-Turret",  75,  5)
CyberToothCat    = Boss("Cyber-toothed Tiger",100, 15)
Battel_Mech      = Boss("Battel-Mech 7000",   150, 20)
Dakik_Yamamoto   = Boss("Dakik Yamamoto",     float('inf'), 18)

################################
# COMPUTER TERMINAL

class Computer:
    def __init__(self, name):
        self.name = name

    def use_interface(self):
        print("\n--- INTERFACE TERMINAL ---")
        print("Options: unlock all doors | open space-port airlock | open observation-deck shutters | exit")
        select = get_input()
        if select == 'unlock all doors':
            Puzzle_1()
        elif select == 'open space-port airlock':
            Puzzle_2()
        elif select == 'open observation-deck shutters':
            Puzzle_3()
        elif select == 'exit':
            print("You step away from the terminal.")
        else:
            print("Unrecognised command.")

################################
# ITEMS

class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Weapons(Item):
    def __init__(self, name, damage_mod, weight, attachment=None):
        super().__init__(name, weight)
        self.damage_mod = damage_mod
        self.attachment = attachment or []

class Potions(Item):
    def __init__(self, name, hp_restor, hp_boost, description, weight):
        super().__init__(name, weight)
        self.hp_restor = hp_restor
        self.hp_boost  = hp_boost
        self.description = description

class KeyCards(Item):
    def __init__(self, name, acsesses, weight):
        super().__init__(name, weight)
        self.acsesses = acsesses   # Room object this card unlocks

class Armor(Item):
    def __init__(self, name, damage_reduction, weight):
        super().__init__(name, weight)
        self.damage_reduction = damage_reduction

class Attachments(Item):
    def __init__(self, name, damage_mod, weight):
        super().__init__(name, weight)
        self.damage_mod = damage_mod

class Money(Item):
    def __init__(self, name, amount, weight):
        super().__init__(name, weight)
        self.amount = amount

# --- Weapon instances ---
Batton         = Weapons("Batton",        5,  3)
Saphire_Batton = Weapons("Saphire Batton",10, 3)
Grenade        = Weapons("Grenade",       100,2)
SmartPistol    = Weapons("Smart Pistol",  30, 4)

# --- Potion instances ---
HP_Elixer = Potions("HP Elixer", 50,  0,  "A vial of crystalline blue liquid",  1)
HP_Max    = Potions("HP Max",    100, 0,  "A vial of glowing green liquid",      1)
HP_Boost  = Potions("HP Boost",  0,   20, "A vial of deep red liquid",           1)

# --- Armour instances ---
chest_plate   = Armor("Chest Plate",   25, 10)
sholder_guard = Armor("Shoulder Guard",15, 7)
gauntlits     = Armor("Gauntlet",      10, 6)
shin_guard    = Armor("Shin Guard",    10, 5)

# --- Attachment instances ---
electrode = Attachments("Electrode", 8, 2)
garlic    = Attachments("Garlic",    3, 1)
Ember     = Attachments("Ember",     16,2)

# --- Money instances ---
Gold_50  = Money("50 Gold",  50,  0)
Gold_100 = Money("100 Gold", 100, 0)
Gold_500 = Money("500 Gold", 500, 0)

################################
# ROOMS

class Room:
    def __init__(self, name, description, doors=None, boss=None, items=None, locked=False):
        self.name        = name
        self.description = description
        self.doors       = doors or []
        self.boss        = boss  or []
        self.items       = items or []
        self.locked      = locked

    def search_room(self):
        if self.items:
            print("You search the room and find:", [i.name for i in self.items])
        else:
            print("You search the room but find nothing.")

    def unlock(self):
        self.locked = False

Reception = Room("Reception",
    "\033[33mYou are in the Reception of Buraddo HQ. Ahead is the Security Clearance.\033[0m",
    boss=[Training_Droid], items=[HP_Elixer], locked=False)

Security_clearance = Room("Security clearance",
    "You are in Security Clearance. Ahead is the Space Elevator, behind you is Reception.",
    items=[Batton, Gold_50], locked=False)

Space_Elivator = Room("Space Elevator",
    "You are in the Space Elevator. Above is the Entrance Hall, below is Security Clearance.",
    locked=True)

Entrance_Hall = Room("Entrance Hall",
    "You are in the Entrance Hall. Ahead is the North Hall, right is East Hall, left is West Hall.",
    boss=[Sentine_Droid1], items=[Gold_100, HP_Elixer], locked=False)

Cafeteria = Room("Cafeteria",
    "You are in the Cafeteria. Right is the Kitchen, left is the North Hall.",
    boss=[Sentine_Droid2], items=[sholder_guard, Gold_100, HP_Elixer], locked=False)

Kitchen = Room("Kitchen",
    "You are in the Kitchen. Left is the Cafeteria.",
    items=[garlic, Gold_50], locked=False)

North_hall = Room("North Hall",
    "You are in the North Hall. Ahead is the Executive Lobby, right is the Cafeteria, behind is the Entrance Hall.",
    boss=[Sentine_Droid4], items=[Gold_50, HP_Elixer], locked=False)

Executive_lobby = Room("Executive Lobby",
    "You are in the Executive Lobby. Ahead is the Executive Elevator, right is East Wing Hallway, left is West Wing Hallway.",
    boss=[Sentine_Droid4], items=[Gold_500, HP_Boost, electrode], locked=True)

Executive_elevator = Room("Executive Elevator",
    "You are in the Executive Elevator. Above is the Executive Office, below is the Executive Lobby.",
    items=[HP_Max], locked=True)

Executive_Office = Room("Executive Office",
    "You are in the Executive Office. Behind you is the Executive Elevator.",
    boss=[Dakik_Yamamoto], items=[Gold_500, SmartPistol, HP_Boost, HP_Max], locked=False)

East_hall = Room("East Hall",
    "You are in the East Hall. Ahead is the Botanical Garden, right are the Bio Labs, left is the Systems Room.",
    locked=False)

Botanical_Garden = Room("Botanical Garden",
    "You are in the Botanical Gardens. Behind you is the East Hall.",
    boss=[Raptor_X], items=[Gold_50, shin_guard], locked=True)

Biological_labs1 = Room("Biological Labs 1", "Behind you is East Hall.", boss=[Raptor_1], locked=False)
Biological_labs2 = Room("Biological Labs 2", "Behind you is East Hall.", boss=[Raptor_1], locked=False)
Biological_labs3 = Room("Biological Labs 3", "Behind you is East Hall.", boss=[Raptor_2], locked=False)
Biological_labs4 = Room("Biological Labs 4", "Behind you is East Hall.", boss=[Raptor_3], locked=False)
Biological_labs5 = Room("Biological Labs 5", "Behind you is East Hall.", boss=[Raptor_4], locked=False)

Systems_room = Room("Systems Room",
    "You are in the Systems Room. Behind you is East Hall.",
    items=[electrode], locked=True)

West_hall = Room("West Hall",
    "You are in the West Hall. Right: Computer Rooms and Office 1. Left: Meeting Rooms and Office 2.",
    locked=False)

Computer_room1 = Room("Computer Room 1", "Behind you is West Hall.", boss=[Sentine_Droid3], items=[Gold_100],          locked=False)
Computer_room2 = Room("Computer Room 2", "Behind you is West Hall.", boss=[Sentine_Droid3], items=[HP_Max, Gold_100],  locked=False)
Office1        = Room("Office 1",        "Behind you is West Hall.", boss=[Sentine_Droid2], items=[HP_Elixer, Gold_50],locked=False)
Office2        = Room("Office 2",        "Behind you is West Hall.", boss=[Sentine_Droid2], items=[HP_Elixer, Gold_50],locked=False)
Meeting_room1  = Room("Meeting Room 1",  "Behind you is West Hall.", boss=[Sentine_Droid1], items=[gauntlits],         locked=False)
Meeting_room2  = Room("Meeting Room 2",  "Behind you is West Hall.", boss=[Sentine_Droid1],                            locked=False)

West_wing_hallway = Room("West Wing Hallway",
    "Ahead is the Marshal Lobby. Behind is the Executive Lobby.",
    locked=True)

Marshal_lobby = Room("Marshal Lobby",
    "Ahead is the Morgue, right is Marshal Hallway 1.",
    boss=[Raptor_X], locked=False)

Morgue = Room("Morgue",
    "Left is the Medical Unit. Behind is the Marshal Lobby.",
    boss=[CyberToothCat], items=[HP_Max], locked=True)

Medical_unit = Room("Medical Unit",
    "Behind you is the Morgue.",
    items=[HP_Max, HP_Boost, HP_Elixer], locked=False)

Marshal_hallway1 = Room("Marshal Hallway 1", "Ahead is Marshal Hallway 2. Behind is the Marshal Lobby.", locked=False)
Marshal_hallway2 = Room("Marshal Hallway 2",
    "Ahead is the Armoury. Left: Security and Weapons Labs. Behind: Marshal Hallway 1.",
    boss=[Turret_1], locked=False)

Armory   = Room("Armoury",   "Behind you is Marshal Hallway 2.", items=[chest_plate, Grenade], locked=True)
Security = Room("Security",  "Cells on both sides. Behind: Marshal Hallway 2.", boss=[Raptor_X], locked=False)
Cell1    = Room("Cell 1",    "Behind you is Security.", locked=False)
Cell2    = Room("Cell 2",    "Behind you is Security.", locked=False)
Cell3    = Room("Cell 3",    "Behind you is Security.", locked=False)
Cell4    = Room("Cell 4",    "Behind you is Security.", locked=False)

Wepons_lab1 = Room("Weapons Lab 1", "Behind you is Marshal Hallway 2.", boss=[Sentine_Droid4], locked=False)
Wepons_lab2 = Room("Weapons Lab 2", "Behind you is Marshal Hallway 2.", boss=[Sentine_Droid4], locked=False)
Wepons_lab3 = Room("Weapons Lab 3", "Behind you is Marshal Hallway 2.", boss=[Sentine_Droid4], locked=False)

East_wing_hallway = Room("East Wing Hallway",
    "Ahead is the Observation Deck. Behind is the Executive Lobby.",
    locked=False)

Observation_deck = Room("Observation Deck",
    "Behind is East Wing Hallway. Left is the Space Port Loading Deck. Ahead is Synthetics Hallway 1.",
    boss=[Raptor_X], items=[HP_Max], locked=True)

Space_Port_loading_deck = Room("Space Port Loading Deck",
    "Ahead is the Airlock. Behind is the Observation Deck.",
    boss=[Battel_Mech], items=[HP_Max], locked=True)

Synthetics_hallway1 = Room("Synthetics Hallway 1",
    "Left is Synthetics Hallway 2. Right is Storage.",
    locked=False)

Storage_unit = Room("Storage Unit",
    "Behind you is Synthetics Hallway 1.",
    items=[Saphire_Batton, Ember], locked=False)

Synthetics_hallway2 = Room("Synthetics Hallway 2",
    "Left: Synthetics Labs. Right: Nanobot Labs. Behind: Synthetics Hallway 1.",
    boss=[Turret_2], items=[HP_Boost], locked=False)

Synthetics_lab1 = Room("Synthetics Lab 1", "Behind: Synthetics Hallway 2.", boss=[Raptor_4], items=[HP_Max], locked=False)
Synthetics_lab2 = Room("Synthetics Lab 2", "Behind: Synthetics Hallway 2.", boss=[Raptor_4], items=[HP_Max], locked=False)
Synthetics_lab3 = Room("Synthetics Lab 3", "Behind: Synthetics Hallway 2.", boss=[Raptor_X], items=[HP_Max], locked=False)
Nanobot_lab1    = Room("Nanobot Lab 1",    "Behind: Synthetics Hallway 2.", boss=[Sentine_Droid4], items=[HP_Max], locked=False)
Nanobot_lab2    = Room("Nanobot Lab 2",    "Behind: Synthetics Hallway 2.", boss=[Sentine_Droid4], items=[HP_Max], locked=False)
Nanobot_lab3    = Room("Nanobot Lab 3",    "Behind: Synthetics Hallway 2.", locked=False)

# Master list of all rooms — used by Puzzle_1 to unlock everything
all_rooms = [
    Reception, Security_clearance, Space_Elivator, Entrance_Hall, Cafeteria,
    Kitchen, North_hall, Executive_lobby, Executive_elevator, Executive_Office,
    East_hall, Botanical_Garden, Biological_labs1, Biological_labs2,
    Biological_labs3, Biological_labs4, Biological_labs5, Systems_room,
    West_hall, Computer_room1, Computer_room2, Office1, Office2,
    Meeting_room1, Meeting_room2, West_wing_hallway, Marshal_lobby,
    Morgue, Medical_unit, Marshal_hallway1, Marshal_hallway2, Armory,
    Security, Cell1, Cell2, Cell3, Cell4, Wepons_lab1, Wepons_lab2,
    Wepons_lab3, East_wing_hallway, Observation_deck,
    Space_Port_loading_deck, Synthetics_hallway1, Storage_unit,
    Synthetics_hallway2, Synthetics_lab1, Synthetics_lab2, Synthetics_lab3,
    Nanobot_lab1, Nanobot_lab2, Nanobot_lab3,
]

################################
# DOOR CONNECTIONS

Reception.doors.append(Security_clearance)
Security_clearance.doors.extend([Reception, Space_Elivator])
Space_Elivator.doors.extend([Security_clearance, Entrance_Hall])
Entrance_Hall.doors.extend([Space_Elivator, North_hall, East_hall, West_hall])
Cafeteria.doors.extend([Kitchen, Entrance_Hall, North_hall])
Kitchen.doors.append(Cafeteria)
North_hall.doors.extend([Cafeteria, Executive_lobby, Entrance_Hall])
Executive_lobby.doors.extend([North_hall, Executive_elevator, West_wing_hallway, East_wing_hallway])
Executive_elevator.doors.extend([Executive_Office, Executive_lobby])
Executive_Office.doors.append(Executive_elevator)
East_hall.doors.extend([Entrance_Hall, Biological_labs1, Biological_labs2,
                         Biological_labs3, Biological_labs4, Biological_labs5,
                         Systems_room, Botanical_Garden])
Botanical_Garden.doors.append(East_hall)
Biological_labs1.doors.append(East_hall)
Biological_labs2.doors.append(East_hall)
Biological_labs3.doors.append(East_hall)
Biological_labs4.doors.append(East_hall)
Biological_labs5.doors.append(East_hall)
Systems_room.doors.append(East_hall)
West_hall.doors.extend([Entrance_Hall, Computer_room1, Computer_room2,
                         Office1, Office2, Meeting_room1, Meeting_room2])
Computer_room1.doors.append(West_hall)
Computer_room2.doors.append(West_hall)
Office1.doors.append(West_hall)
Office2.doors.append(West_hall)
Meeting_room1.doors.append(West_hall)
Meeting_room2.doors.append(West_hall)
West_wing_hallway.doors.extend([Executive_lobby, Marshal_lobby])
Marshal_lobby.doors.extend([West_wing_hallway, Morgue, Marshal_hallway1])
Morgue.doors.extend([Marshal_lobby, Medical_unit])
Medical_unit.doors.append(Morgue)
Marshal_hallway1.doors.extend([Marshal_lobby, Marshal_hallway2])
Marshal_hallway2.doors.extend([Marshal_hallway1, Security, Wepons_lab1,
                                Wepons_lab2, Wepons_lab3, Armory])
Armory.doors.append(Marshal_hallway2)
Security.doors.extend([Cell1, Cell2, Cell3, Cell4, Marshal_hallway2])
Cell1.doors.append(Security)
Cell2.doors.append(Security)
Cell3.doors.append(Security)
Cell4.doors.append(Security)
Wepons_lab1.doors.append(Marshal_hallway2)
Wepons_lab2.doors.append(Marshal_hallway2)
Wepons_lab3.doors.append(Marshal_hallway2)
East_wing_hallway.doors.extend([Observation_deck, Executive_lobby])
Observation_deck.doors.extend([Space_Port_loading_deck, East_wing_hallway, Synthetics_hallway1])
Space_Port_loading_deck.doors.append(Observation_deck)
Synthetics_hallway1.doors.extend([Observation_deck, Synthetics_hallway2, Storage_unit])
Storage_unit.doors.append(Synthetics_hallway1)
Synthetics_hallway2.doors.extend([Synthetics_hallway1, Synthetics_lab1, Synthetics_lab2,
                                   Synthetics_lab3, Nanobot_lab1, Nanobot_lab2, Nanobot_lab3])
Synthetics_lab1.doors.append(Synthetics_hallway2)
Synthetics_lab2.doors.append(Synthetics_hallway2)
Synthetics_lab3.doors.append(Synthetics_hallway2)
Nanobot_lab1.doors.append(Synthetics_hallway2)
Nanobot_lab2.doors.append(Synthetics_hallway2)
Nanobot_lab3.doors.append(Synthetics_hallway2)

################################
# KEYCARDS — placed in rooms after rooms are defined

KeyCard1  = KeyCards("Space Elevator Key-Card",       Space_Elivator,           1)
KeyCard2  = KeyCards("Botanical Gardens Key-Card",    Botanical_Garden,         1)
KeyCard3  = KeyCards("Executive Lobby Key-Card",      Executive_lobby,          1)
KeyCard4  = KeyCards("West Wing Hallway Key-Card",    West_wing_hallway,        1)
KeyCard5  = KeyCards("Executive Elevator Key-Card",   Executive_elevator,       1)
KeyCard6  = KeyCards("Observation Deck Key-Card",     Observation_deck,         1)
KeyCard7  = KeyCards("Storage Key-Card",              Storage_unit,             1)
KeyCard8  = KeyCards("Morgue Key-Card",               Morgue,                   1)
KeyCard9  = KeyCards("Systems Room Key-Card",         Systems_room,             1)
KeyCard10 = KeyCards("Space Port Loading Deck Key-Card", Space_Port_loading_deck, 1)

Security_clearance.items.append(KeyCard1)
Systems_room.items.append(KeyCard2)
Botanical_Garden.items.append(KeyCard3)
Meeting_room2.items.append(KeyCard4)
Morgue.items.append(KeyCard5)
Armory.items.append(KeyCard6)
Nanobot_lab3.items.append(KeyCard7)
Storage_unit.items.append(KeyCard8)
Biological_labs5.items.append(KeyCard9)
Executive_Office.items.append(KeyCard10)

# Computer terminals placed in rooms
Terminal_reception        = Computer("Reception Terminal")
Terminal_exec_lobby       = Computer("Executive Lobby Terminal")
Terminal_observation      = Computer("Observation Deck Terminal")

Reception.terminal        = Terminal_reception
Executive_lobby.terminal  = Terminal_exec_lobby
Observation_deck.terminal = Terminal_observation

################################
# PROTAGONIST — instantiated after all rooms exist

protagonist = Protagonist(
    room     = Reception,
    name     = 'Akiino',
    hp       = 100,
    max_hp   = 100,
    strength = 5,
    gold     = 100,
)

################################
# COMBAT LOOP

def combat_loop(enemy):
    """
    Runs a full combat encounter with one enemy.
    Returns True if player survived, False if defeated.
    """
    print(f"\n--- COMBAT: {enemy.name} (HP: {enemy.hp}) ---")
    while enemy.hp > 0 and protagonist.hp > 0:
        print(f"\nYour HP: {protagonist.hp}/{protagonist.max_hp}")
        print("Actions: attack | use <potion name> | dash (skip enemy turn) | flee")
        sub_action = get_input()

        if sub_action == 'attack':
            protagonist.Protag_strike(enemy)
            if enemy.hp > 0:
                
                enemy.boss_strike(protagonist)

        elif sub_action.startswith('use '):
            item_name = sub_action[len('use '):].strip()
            used = protagonist.use_potion(item_name)
            if used and enemy.hp > 0:
                enemy.boss_strike(protagonist)  # potion use costs a turn

        elif sub_action == 'dash':
            print("You dash, avoiding the enemy's next attack!")
            # Dash skips the enemy's counterattack this turn

        elif sub_action == 'flee':
            print("You flee from the battle!")
            return True  # player escapes, stays alive

        else:
            print("Unknown combat action.")

        if protagonist.hp <= 0:
            return False

    if enemy.hp <= 0:
        print(f"\n{enemy.name} has been defeated!")
        protagonist.gain_XP()

    return protagonist.hp > 0

################################
# MAIN LOOP

def show_status():
    equipped_names = [i.name for i in protagonist.equipped] if protagonist.equipped else ["none"]
    backpack_names = [i.name for i in protagonist.backpack.items] if protagonist.backpack.items else ["empty"]
    boss_names     = [b.name for b in protagonist.room.boss if b.hp > 0] if protagonist.room.boss else ["none"]
    door_names     = [d.name for d in protagonist.room.doors]
    print(
        f"\n{'='*50}\n"
        f"Location : {protagonist.room.name}\n"
        f"{protagonist.room.description}\n"
        f"{'='*50}\n"
        f"HP       : {protagonist.hp}/{protagonist.max_hp}   Gold: {protagonist.gold}\n"
        f"Equipped : {equipped_names}\n"
        f"Backpack : {backpack_names}\n"
        f"Enemies  : {boss_names}\n"
        f"Doors    : {door_names}\n"
    )

def show_help():
    print("""
COMMANDS:
  move to <room name>     — move to an adjacent room
  search room             — look for items in the room
  pick up <item name>     — add item to backpack (money goes to gold)
  put down <item name>    — drop item from backpack
  equip <item name>       — equip weapon/armour from backpack
  unequip <item name>     — return equipped item to backpack
  use <item name>         — use a potion from backpack
  use keycard <card name> — use a keycard to unlock a door
  use terminal            — interact with computer terminal (if present)
  engage enemy            — start combat with enemies in this room
  show hp                 — display current HP
  show backpack           — list backpack contents
  show equipped           — list equipped items
  describe room           — re-read room description
  help                    — show this list
  quit                    — exit game
""")

def main_loop():
    print("\nWelcome to Buraddo HQ. Type 'help' for commands.\n")
    show_status()

    while True:
        player_action = get_input()

        # --- QUIT ---
        if player_action == 'quit':
            print("Goodbye.")
            sys.exit()

        # --- HELP ---
        elif player_action == 'help':
            show_help()

        # --- MOVEMENT ---
        elif player_action.startswith("move to "):
            new_room_name = player_action[len("move to "):].strip()
            protagonist.go_to_room(new_room_name)
            show_status()

        # --- SEARCH ---
        elif player_action == 'search room':
            protagonist.room.search_room()

        # --- PICK UP ---
        elif player_action.startswith("pick up "):
            item_name = player_action[len("pick up "):].strip()
            protagonist.pick_up_money(item_name)   # handles both money and normal items

        # --- PUT DOWN ---
        elif player_action.startswith("put down "):
            item_name = player_action[len("put down "):].strip()
            protagonist.backpack.put_down(protagonist.room, item_name)

        # --- EQUIP ---
        elif player_action.startswith("equip "):
            item_name = player_action[len("equip "):].strip()
            protagonist.equip(item_name)

        # --- UNEQUIP ---
        elif player_action.startswith("unequip "):
            item_name = player_action[len("unequip "):].strip()
            protagonist.unequip(item_name)

        # --- USE POTION ---
        elif player_action.startswith("use keycard "):
            card_name = player_action[len("use keycard "):].strip()
            protagonist.use_keycard(card_name)

        elif player_action.startswith("use "):
            item_name = player_action[len("use "):].strip()
            protagonist.use_potion(item_name)

        # --- TERMINAL ---
        elif player_action == 'use terminal':
            terminal = getattr(protagonist.room, 'terminal', None)
            if terminal:
                terminal.use_interface()
            else:
                print("There is no terminal in this room.")

        # --- COMBAT ---
        elif player_action == 'engage enemy':
            living_enemies = [b for b in protagonist.room.boss if b.hp > 0]
            if not living_enemies:
                print("There are no enemies here.")
            else:
                for enemy in living_enemies:
                    survived = combat_loop(enemy)
                    if not survived:
                        break
                if protagonist.hp <= 0:
                    print("\nYou have been defeated. Game over.")
                    sys.exit()

        # --- INFO COMMANDS ---
        elif player_action == 'show hp':
            protagonist.show_hp()

        elif player_action == 'show backpack':
            protagonist.show_backpack()

        elif player_action == 'show equipped':
            protagonist.show_equipped()

        elif player_action == 'describe room':
            protagonist.show_room()

        else:
            print("Unknown command. Type 'help' for a list of commands.")

        # --- PASSIVE ENEMY ATTACKS ---
        # Some enemies attack on sight regardless of whether you engaged them
        ambush_rooms = {
            Morgue:                  "Cyber-toothed Tiger",
            Space_Port_loading_deck: "Battel-Mech 7000",
            Executive_Office:        "Dakik Yamamoto",
        }
        if protagonist.room in ambush_rooms:
            enemy_name = ambush_rooms[protagonist.room]
            for b in protagonist.room.boss:
                if b.name == enemy_name and b.hp > 0:
                    print(f"\n{b.name} attacks you!")
                    b.boss_strike(protagonist)

        # --- DEATH CHECK ---
        if protagonist.hp <= 0:
            print("\nYou have been defeated. Game over.")
            sys.exit()

        # --- WIN CHECK ---
        if Dakik_Yamamoto.hp <= 0:
            print("\n" + "="*50)
            print("Dakik Yamamoto has been destroyed.")
            print("Buraddo HQ falls silent. You have won.")
            print("="*50)
            sys.exit()

main_loop()