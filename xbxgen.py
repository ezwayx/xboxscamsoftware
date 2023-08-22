import random
import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_xbox_gift_card():
    code = ''.join(str(random.randint(1, 9)) for _ in range(16))
    balance = random.randint(20, 100)
    generated_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Xbox Gift Card Code: {code}\nBalance: ${balance}\nGenerated: {generated_time}"

def generate_xbox_gamepass():
    code = ''.join(str(random.randint(1, 9)) for _ in range(16))
    durations = ["1 month", "3 months", "1 year"]
    duration = random.choice(durations)
    generated_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Xbox GamePass/Gold Code: {code}\nDuration: {duration}\nGenerated: {generated_time}"

def main():
    title = """

 ██████╗ ██████╗ ███╗   ██╗███████╗ ██████╗ ██╗     ███████╗             
██╔════╝██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██║     ██╔════╝             
██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     █████╗               
██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██╔══╝               
╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗███████╗             
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝             
                                                                         
 ██████╗ ██╗███████╗████████╗     ██████╗ ██████╗ ██████╗ ███████╗       
██╔════╝ ██║██╔════╝╚══██╔══╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝       
██║  ███╗██║█████╗     ██║       ██║     ██║   ██║██║  ██║█████╗         
██║   ██║██║██╔══╝     ██║       ██║     ██║   ██║██║  ██║██╔══╝         
╚██████╔╝██║██║        ██║       ╚██████╗╚██████╔╝██████╔╝███████╗       
 ╚═════╝ ╚═╝╚═╝        ╚═╝        ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝       
                                                                         
███████╗ ██████╗ █████╗ ███╗   ███╗██╗    ██╗ █████╗ ██████╗ ███████╗    
██╔════╝██╔════╝██╔══██╗████╗ ████║██║    ██║██╔══██╗██╔══██╗██╔════╝    
███████╗██║     ███████║██╔████╔██║██║ █╗ ██║███████║██████╔╝█████╗      
╚════██║██║     ██╔══██║██║╚██╔╝██║██║███╗██║██╔══██║██╔══██╗██╔══╝      
███████║╚██████╗██║  ██║██║ ╚═╝ ██║╚███╔███╔╝██║  ██║██║  ██║███████╗    
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    
                                                                         
                                                            
                                                                                                                                  
"""
    while True:
        clear_screen()
        print(title)
        print("Main Menu")
        print("(1) Enter Generator")
        print("(2) Current Update")
        
        choice = input("Select 1 or 2: ")
        
        if choice == "1":
            while True:
                clear_screen()
                print(title)
                print("\n(1) Xbox Codes")
                print("(2) PS4 Codes")
                print("(3) Back")
                
                generator_choice = input("Select an option: ")
                
                if generator_choice == "1":
                    while True:
                        clear_screen()
                        print(title)
                        print("\n(1) Xbox Gift Card Code")
                        print("(2) Xbox GamePass/Gold")
                        print("(3) Back")
                        
                        xbox_choice = input("Select an option: ")
                        
                        if xbox_choice == "1":
                            xbox_gift_card = generate_xbox_gift_card()
                            clear_screen()
                            print(title)
                            print("\n" + xbox_gift_card)
                            input("Press Enter to continue...")
                        elif xbox_choice == "2":
                            xbox_gamepass = generate_xbox_gamepass()
                            clear_screen()
                            print(title)
                            print("\n" + xbox_gamepass)
                            input("Press Enter to continue...")
                        elif xbox_choice == "3":
                            break
                elif generator_choice == "2":
                    clear_screen()
                    print(title)
                    print("\nComing soon")
                    input("Press Enter to continue...")
                elif generator_choice == "3":
                    break
        elif choice == "2":
            clear_screen()
            print(title)
            print("\nComing soon")
            input("Press Enter to continue...")
        else:
            clear_screen()
            print(title)
            print("\nInvalid choice. Please select 1 or 2.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
