# SMT4A save editor in the terminal that is probably near-absurdly scuffed, but it functions.
# Other save editors do exist, but this was meant to serve the specific function of 
# switching demons in specific slots. I a bit ahead of myself.
# A lot of the data regarding hex addresses I got from waynelimt's Save Editor at:
# https://github.com/waynelimt/SMT_IV_Apocalypse_Save_Editor
# The skill data for the above editor was incomplete, so I got the skill data from
# The Black X's cheat table at: https://fearlessrevolution.com/viewtopic.php?t=16219



import os
from stat import FILE_ATTRIBUTE_SPARSE_FILE
from pointers import *


class Editor:
    # A basic editor class for interactions with an SMT4A save.
    def __init__(self, savefile):
        self._promptCont = lambda: input("Press Enter to Continue.")
        self._promptInvalid = lambda: print("Invalid Input")
        # I'm like, 99.9% VSC is giving a false positive here, I don't see how someone can inject commands through this.
        self._cls = lambda: os.system("cls" if os.name == "nt" else "clear")

        self._save = savefile

    def confirm(self):
        choice = input("Are you sure? (y/N)")
        if choice == "y":
            return True
        else:
            return False


    def menu(self):
        # Basic terminal menu for the editor.
        loop = True
        while loop:
            self._cls()

            while not self._save.loaded():
                print("Save Not Detected!")
                filename = input("Filename of save?: ")
                self._save.loadSave(filename)
                self._cls()

            print("1. Read Data --- 2. Write Data --- 3. Save/Load Files --- 0. Exit")
            choice = input()
            self._cls()
            if choice == "1":
                self.reader()
            elif choice == "2":
                self.writer()
            elif choice == "3":
                self.manager()
            elif choice == "0":
                if self.confirm():
                    loop = False
            else:
                self._promptInvalid()
                self._promptCont()

    def reader(self):
        # Basic Terminal Menu for reading data in the save file loaded into the editor.
        loop = True
        while loop:
            self._cls()
            print("1. MC --- 2. Demons --- 3. Etc --- 0. Exit")
            choice = input()
            if choice == "1":
                print(self._save.mcStr())
                self._promptCont()
            elif choice == "2":
                self.readDemon()
            elif choice == "3":
                print(self._save.etcStr())
                self._promptCont()
            elif choice == "0":
                loop = False
            else:
                self._promptInvalid()
                self._promptCont()
    
    def readDemon(self):
        # Displays a list of demons, then prompts user to read a given demon's data.
        loop = True
        while loop:
            slot = self.selectDemon("Which Demon? (0 to exit.): ")
            if slot > 0:
                print(self._save.deStr(slot))
                self._promptCont()
            elif slot == 0:
                loop = False
            else:
                self._promptInvalid()
                self._promptCont()
            

    def writer(self):
        # Basic Terminal Menu for writing data in the 
        loop = True
        while loop:
            self._cls()
            if not self._save.loaded():
                print("*WARNING: NO SAVE IS LOADED*")
            print("1. MC --- 2. Demons --- 3. Etc --- 0. Exit")
            choice = input()
            if choice == "1":
                print(self.writeMc())
            elif choice == "2":
                self.writeDe()
            elif choice == "3":
                print(self.writeEtc())
            elif choice == "0":
                loop = False
            else:
                self._promptInvalid()
                self._promptCont()

    def writeMc(self):
        loop = True
        while loop:
            self._cls()
            msg = self._save.mcStr().splitlines()
            i = 1
            while i < len(msg):
                print(f"{i}. " + msg[i])
                i += 1

            choice = input("Edit which row? (0 to exit): ")
            if choice == "1":
                self.writeMcHpMp()
            elif choice == "2":
                self.writeMcStats()
            elif choice == "3":
                self.writeMcSkills()
            elif choice == "0":
                return
            else:
                self._promptInvalid()
                self._promptCont()

    def writeMcSkills(self):
        loop = True
        while loop:
            self._cls()
            msg = self._save.mcStr().splitlines()[3]
            print(msg)
            try:
                choice = int(input("Which Skill Slot? (9 to swap, 0 to exit): "))
            except KeyboardInterrupt:
                raise KeyboardInterrupt()
            except:
                choice = -1
        
            if 1 <= choice <= 8:
                value = self.hexInput()
                if value != -1:
                    self._save.writeMcSkill(value, choice)
            elif choice == 9:
                self.swapMcSkill()
            elif choice == 0:
                loop = False
            else:
                self._promptInvalid()
                self._promptCont()

        return
        
    def swapMcSkill(self):
        loop = True
        while loop:
            self._cls()
            msg = self._save.mcStr().splitlines()[3]
            print(msg)
            try:
                i = int(input("First Skill? ( 0 to exit): "))
            except KeyboardInterrupt:
                raise KeyboardInterrupt()
            except:
                i = -1
            
            if i == 0:
                loop = False
            elif i not in range(1, 9):
                self._promptInvalid()
                self._promptCont()
            else:
                try:
                    j = int(input("Second Skill?: "))
                except KeyboardInterrupt:
                    raise KeyboardInterrupt()
                except:
                    j = -1
                if j in range(1, 9):
                    self._save.swapMcSkill(i, j)
                else:
                    self._promptInvalid()
                    self._promptCont()
            


    def writeMcStats(self):
        loop = True
        while loop:
            self._cls()
            msg = self._save.mcStr().splitlines()[2]
            print(msg)
            print("1. Strength - 2. Dexterity - 3. Magic - 4. Agility - 5. Luck - 0. Exit")
            try:
                choice = int(input())
            except KeyboardInterrupt:
                raise KeyboardInterrupt()
            except:
                choice = -1

            if 1 <= choice <= 5:
                value = self.intInput()
                if value != -1:
                    self._save.writeMcStat(value, choice)
            elif choice == 0:
                loop = False
            else:
                self._promptInvalid()
                self._promptCont()

        return
        

    def writeMcHpMp(self):
        # Menu for editting the 2nd row (level, hp, mp) of demon information.
        loop = True
        while loop:
            self._cls()
            msg = self._save.mcStr().splitlines()[1]
            print(msg)
            print("1. Level --- 2. HP --- 3. MP --- 0. Exit")
            choice = input()
            
            if choice == "1":
                value = self.intInput()
                if value != -1:
                    self._save.writeMcLvl(value)
            elif choice == "2":
                value = self.intInput()
                if value != -1:
                    self._save.writeMcHp(value)
            elif choice == "3":
                value = self.intInput()
                if value != -1:
                    self._save.writeMcMp(value)
            elif choice == "0":
                return
            else:
                self._promptInvalid()
                self._promptCont()



    def writeDe(self):
        #Selects a demon to edit in the editDe function
        loop = True
        while loop:
            slot = self.selectDemon("Edit which Demon? (25 to swap slots, 0 to exit): ")
            if slot == 0:
                loop = False
            elif slot in range(0, 26):
                self.editDe(slot)
            elif slot == -2: # Special case of swapping
                self.swapDe()
            else:
                self._promptInvalid()
                self._promptCont()

    def swapDe(self):
        loop = True
        while loop: 
            i = self.selectDemon("First Demon? (0 to exit): ")
            
            if i == 0:
                loop = False
            elif i < 0:
                self._promptInvalid()
                self._promptCont()
            else:
                j = self.selectDemon("Second Demon?: ")
                if i < 0:
                    self._promptInvalid()
                    self._promptCont()
                else:
                    self._save.swapDeSlot(i, j)

    def editDe(self, slot):
        # Menu to edit the demon specified in slot

        loop = True
        while loop:
            self._cls()
            msg = self._save.deStr(slot).splitlines()
            i = 0
            while i < len(msg):
                print(f"{i+1}. " + msg[i])
                i += 1

            choice = input("Edit which row? (0 to exit): ")
            if choice == "1":
                self.writeDeId(slot)
            elif choice == "2":
                self.writeDeHpMp(slot)
            elif choice == "3":
                self.writeDeStats(slot)
            elif choice == "4":
                self.writeDeSkills(slot)
            elif choice == "0":
                return
            else:
                self._promptInvalid()
                self._promptCont()

    def writeDeSkills(self, slot):
        loop = True
        while loop:
            self._cls()
            msg = self._save.deStr(slot).splitlines()[3]
            print(msg)
            try:
                choice = int(input("Which Skill Slot? (9 to swap, 0 to exit): "))
            except KeyboardInterrupt:
                raise KeyboardInterrupt()
            except:
                choice = -1
        
            if 1 <= choice <= 8:
                value = self.hexInput()
                if value != -1:
                    self._save.writeDeSkill(slot, value, choice)
            elif choice == 9:
                self.swapDeSkill(slot)
            elif choice == 0:
                loop = False
            else:
                self._promptInvalid()
                self._promptCont()

        return
        
    def swapDeSkill(self, slot):
        loop = True
        while loop:
            self._cls()
            msg = self._save.deStr(slot).splitlines()[3]
            print(msg)
            try:
                i = int(input("First Skill? ( 0 to exit): "))
            except KeyboardInterrupt:
                raise KeyboardInterrupt()
            except:
                i = -1
            
            if i == 0:
                loop = False
            elif i not in range(1, 9):
                self._promptInvalid()
                self._promptCont()
            else:
                try:
                    j = int(input("Second Skill?: "))
                except KeyboardInterrupt:
                    raise KeyboardInterrupt()
                except:
                    j = -1
                if j in range(1, 9):
                    self._save.swapDeSkill(slot, i, j)
                else:
                    self._promptInvalid()
                    self._promptCont()
            


    def writeDeStats(self, slot):
        loop = True
        while loop:
            self._cls()
            msg = self._save.deStr(slot).splitlines()[2]
            print(msg)
            print("1. Strength - 2. Dexterity - 3. Magic - 4. Agility - 5. Luck - 0. Exit")
            try:
                choice = int(input())
            except KeyboardInterrupt:
                raise KeyboardInterrupt()
            except:
                choice = -1

            if 1 <= choice <= 5:
                value = self.intInput()
                if value != -1:
                    self._save.writeDeStat(slot, value, choice)
            elif choice == 0:
                loop = False
            else:
                self._promptInvalid()
                self._promptCont()

        return
        

    def writeDeHpMp(self, slot):
        # Menu for editting the 2nd row (level, hp, mp) of demon information.
        loop = True
        while loop:
            self._cls()
            msg = self._save.deStr(slot).splitlines()[1]
            print(msg)
            print("1. Level --- 2. HP --- 3. MP --- 0. Exit")
            choice = input()
            
            if choice == "1":
                value = self.intInput()
                if value != -1:
                    self._save.writeDeLvl(slot, value)
            elif choice == "2":
                value = self.intInput()
                if value != -1:
                    self._save.writeDeHp(slot, value)
            elif choice == "3":
                value = self.intInput()
                if value != -1:
                    self._save.writeDeMp(slot, value)
            elif choice == "0":
                return
            else:
                self._promptInvalid()
                self._promptCont()

    def writeDeId(self, slot):
        id = self.hexInput()
        if id != -1:
            self._save.writeDeId(slot, id)

    def writeEtc(self):
        loop = True
        while loop:
            self._cls()
            print(self._save.etcStr())
            print("1. Macca --- 2. App Points --- 0. Exit")
            choice = input()

            if choice == "1":
                value = self.intInput()
                if value != -1:
                    self._save.writeMacca(value)

            elif choice == "2":
                value = self.intInput()
                if value != -1:
                    self._save.writeApp(value)

            elif choice == "0":
                loop = False

            else:
                self._promptInvalid()
                self._promptCont()

    def manager(self):
        loop = True
        while loop:
            self._cls()
            print("1. Save Updated File --- 2. Load Another Save --- 3. Save Demon --- 4. Load Demon --- 0. Exit")
            choice = input()

            if choice == "1":
                choice = input("File Name? (0 to cancel): ")
                if choice != "0":
                    self._save.uploadFile(choice)

            elif choice == "2":
                choice = input("File to load? (0 to cancel): ")
                if choice != "0":
                    self._save.loadSave(choice)

            elif choice == "3":
                slot = self.selectDemon("Which Demon? (0 to exit): ")
                if slot > 0:
                    choice = input("File Name? (0 to cancel): ")
                    if choice != "0":
                        self._save.saveDe(choice, slot)

            elif choice == "4":
                choice = input("File Name? (0 to cancel): ")
                try:
                    fh = open(choice, "rb")
                    fh.close()
                except:
                    print("File Not Found!")
                    self._promptCont()
                    choice = "0"

                if choice != "0":
                    slot = self.selectDemon("Which Demon to Replace? (0 to cancel): ")
                    if slot > 0:
                        self._save.loadDe(choice, slot)
                    elif slot < 0:
                        self._promptInvalid()
                        self._promptCont()

            elif choice == "0":
                loop = False
            else:
                self._promptInvalid()
                self._promptCont()



    def selectDemon(self, msg=""):
        # Returns a user-selected demon's slot from the stock.
        # Returns -1 if the reponse is invalid.
        # Returns -2 if the response is 25, a special case of demons being swapped in some calls.
        self._cls()
        print(self._save.deListStr())
        try:
            choice = int(input(msg))
        except KeyboardInterrupt:
            raise KeyboardInterrupt()
        except:
            choice = -1
        else:
            if choice not in range(0, 25):
                if choice == 25:
                    choice = -2
                else:
                    choice = -1
            
        return choice

    def hexInput(self):
        n = input("Hexcode: ")
        try:
            int("0x"+n, 16)
        except KeyboardInterrupt:
            raise KeyboardInterrupt()
        except:
            print("Not a valid Hex Code!")
            n = -1
            
        return n 

    def intInput(self):
        # Returns a user-given integer, or prints an error message
        try:
            choice = int(input("Value?: "))
        except KeyboardInterrupt:
            raise KeyboardInterrupt()
        except:
            self._promptInvalid()
            self._promptCont()
            choice = -1
        return choice


def main():

    save = Save(None)
    editor = Editor(save)
    editor.menu()

    return

if __name__ == '__main__':
    main()