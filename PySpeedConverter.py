import os              # Open files for Windows
import subprocess, sys # Open files for Linux

# Unfortunately the code I wrote for this program has a lot of if elif else statments. Hopefully once I get more proficient with programming in Python
# I can clean up, and reorganize the code to look more proper to industry standards

# Display the program name
print("Python Speed Conversion \n Written by Ryan Cannon")
input("Press enter to continue")

# Clear Screen
os.system('cls')


# Just a few goodies I added to this program just for kicks
def easterEggs(option):

    # Joseph Garrity, Norman J. Grossfeld, and Russell Velázquez - Sonic X Theme
    if (option == "gotta go fast") or (option == "sonic the hedgehog"):
        print("♪ Gotta go fast ♪")
        speed = 186000  # Set the speed to 186,000 Miles per hour 
        unitSymbol = "MPH"
        print("The Speed in Miles Per Hour is:", speed, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\gottagofast.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/gottagofast.ogg'])
        input("Press enter to continue")
        os.system('cls')
        main()

    # Sammy Hagger - I Can't Drive 55
    elif (option == "i can't drive 55") or (option == "go on and write me up for 125"):
        print("♪ Go on and write me up for 125 ♪\n♪ Post my face wanted dead or alive ♪")
        speed = 125 # Set the speed to 125 Miles per hour
        unitSymbol = "MPH"
        print("The Speed in Miles Per Hour is:", speed, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\icantdrive55.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/icantdrive55.ogg'])
        input("Press enter to continue")
        os.system('cls')
        main()

    # Road Runner from Wile E. Coyote and the Road Runner
    elif (option == "road runner") or (option == "meep meep"):
        print("Meep Meep")
        speed = 276  # Set the speed to 276 Miles per hour
        unitSymbol = "MPH"
        print("The Speed in Miles Per Hour is:", speed, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\Roadrunner.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/Roadrunner.ogg'])
        input("Press enter to continue")
        os.system('cls')
        main()

    # Max Coveri - Running In The 90's
    elif (option == "running in the 90s") or (option == "eurobeat intensifies"):
        print("♪ It is a new way I like to be ♪\n♪ I'm just running in the nineties ♪")
        speed = 121 # Set the speed to 121 Miles per hour
        unitSymbol = "MPH"
        print("The speed in Miles per hour is:", speed, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\Runninginthe90s.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/Runninginthe90s.ogg'])
        input("Press enter to continue")
        os.system('cls')
        main()

    # Foghat - Slow Ride
    elif (option == "slow ride") or (option == "take it easy"):
        print("♪ Slow ride ♪ \n♪ Take it easy ♪")
        speed = 1 # Set the speed to 1 Mile per hour
        unitSymbol = "MPH"
        print("The speed in Miles per hour is:", speed, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\slowride.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/slowride.ogg'])
        input("Press enter to continue")
        os.system('cls')
        main()


    # Michael Jackson - Speed Demon
    elif (option == "speed demon") or (option == "michael jackson"):
        print("♪ Speed Demon ♪ \n♪ Mind is like a compass, I'm stopping at nothing ♪")
        speed = 100 # Set the speed to 100
        unitSymbol = "MPH"
        print("The speed in Miles per hour is:", speed, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\speeddemon.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/speeddemon.ogg'])
        input("Press enter to continue")
        os.system('cls')
        main()

    # Nobuyoshi Koshibe - Speed Racer Theme
    elif (option == "speed racer") or (option == "sociopathic racer"):
        print("♪ He's a demon and he's gonna be chasin' after someone ♪ \n♪ Go Speed Racer! Go Speed Racer go! Go Speed Racer goooo!♪")
        speed = 300 # Set the speed to 300 Miles per hour
        unitSymbol = "MPH"
        print("The speed in Miles per hour is:", speed, unitSymbol)

        # Check if the user is running the program on Windows or Linux
        if sys.platform.startswith('win32'):
            os.startfile('EasterEggs\speedracer.ogg')
        else:
            subprocess.Popen(["open", 'EasterEggs/speedracer.ogg'])
        input("Press enter to continue")
        os.system('cls')
        main()

    # If no "special" inputs where typed in, resume normal operations
    else:
        pass


# Make sure the user enters a number when asked for the speed
def ExitorContinue():
    print("Do you want to convert again?")
    # Added the .lower() function so that if the user types the letter in uppercase, the program will accept it
    choice = input("Enter y to continue \nEnter n to exit: ").lower()
    if (choice == "y") or (choice == "yes"):
        # Clear Screen
        os.system('cls')
        main()
    elif (choice == "n") or (choice == "no"):
        quit()
    else:
        # If the user enters something else other than what was asked of them to enter,
        # give them this error message then go back to the start of the prompt.
        os.system('cls')
        print("Invalid option")
        ExitorContinue()


def convertSpeed(option):
                                                # FROM MILES PER HOUR

    # Convert from Miles per hour to Kilometers per hour
    if (option == "1"):
        try:
            userSpeed = float(input("Enter speed in Miles per hour: "))
            speed = (userSpeed * 1.609)
            speedUnit = "Kilometer per hour"
            unitSymbol = "KM/H"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Miles per hour to Feet per second
    elif (option == "2"):
        try:
            userSpeed = float(input("Enter speed in Miles per hour: "))
            speed = (userSpeed * 1.467)
            speedUnit = "Feet per second"  # Dan Schneiders favorite speed unit
            unitSymbol = "FT/S"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Miles per hour to Meters per second
    elif (option == "3"):
        try:
            userSpeed = float(input("Enter speed in Miles per hour: "))
            speed = (userSpeed / 2.237)
            speedUnit = "Meter per seoncd"
            unitSymbol = "M/S"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Miles per hour to Knots
    elif (option == "4"):
        try:
            userSpeed = float(input("Enter speed in Miles per hour: "))
            speed = (userSpeed / 1.151)
            speedUnit = "Knots"
            unitSymbol = "KT"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

                                        # FROM KILOMETERS

    # Convert from Kilometers to Miles per hour
    elif (option == "5"):
        try:
            userSpeed = float(input("Enter speed in Kilometers per hour: "))
            speed = (userSpeed / 1.609)
            speedUnit = "Miles per hour"
            unitSymbol = "MPH"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Kilometers per hour to Feet per second
    elif (option == "6"):
        try:
            userSpeed = float(input("Enter speed in Kilometers per hour: "))
            speed = (userSpeed / 1.097)
            speedUnit = "Feet per second"
            unitSymbol = "FT/S"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Kilometers per hour to Meters per second
    elif (option == "7"):
        try:
            userSpeed = float(input("Enter speed in Kilometers per hour: "))
            speed = (userSpeed / 3.6)
            speedUnit = "Meters Per second"
            unitSymbol = "M/S"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Kilometers per hour to Knots
    elif (option == "8"):
        try:
            userSpeed = float(input("Enter speed in Kilometers per hour: "))
            speed = (userSpeed / 1.852)
            speedUnit = "Knots"
            unitSymbol = "KT"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

                                        # FROM FEET PER SECOND

    # Convert from Feet per second to Miles per hour
    elif (option == "9"):
        try:
            userSpeed = float(input("Enter speed in Feet per second: "))
            speed = (userSpeed / 1.467)
            speedUnit = "Miles per hour"
            unitSymbol = "MPH"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Feet per second to Meters per second
    elif (option == "10"):
        try:
            userSpeed = float(input("Enter speed in Feet per second: "))
            speed = (userSpeed / 3.281)
            speedUnit = "Meters per second"
            unitSymbol = "M/S"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Feet per second to Kilometers per hour per hour
    elif (option == "11"):
        try:
            userSpeed = float(input("Enter speed in Feet per second: "))
            speed = (userSpeed * 1.097)
            speedUnit = "Kilometers per hour"
            unitSymbol = "KM/H"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Feet per second to Knots
    elif (option == "12"):
        try:
            userSpeed = float(input("Enter speed in Feet per second: "))
            speed = (userSpeed / 1.688)
            speedUnit = "Knots"
            unitSymbol = "KT"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

                                    # FROM METERS PER SECOND

    # Convert from Meters per second to Miles per hour
    elif (option == "13"):
        try:
            userSpeed = float(input("Enter speed in Meters per second: "))
            speed = (userSpeed * 2.237)
            speedUnit = "Miles per hour"
            unitSymbol = "MPH"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Meters per second to Feet per second
    elif (option == "14"):
        try:
            userSpeed = float(input("Enter speed in Meters per second: "))
            speed = (userSpeed * 3.281)
            speedUnit = "Feet per second"
            unitSymbol = "FT/S"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Meters per second to Kilometers per hour
    elif (option == "15"):
        try:
            userSpeed = float(input("Enter speed in Meters per second: "))
            speed = (userSpeed * 3.6)
            speedUnit = "Kilometers per hour"
            unitSymbol = "KM/H"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()


    # Convert from Meters per second to Knots
    elif (option == "16"):
        try:
            userSpeed = float(input("Enter speed in Meters per second: "))
            speed = (userSpeed * 1.944)
            speedUnit = "Knots"
            unitSymbol = "KT"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

                                                # FROM KNOTS

    # Convert from Knots to Miles per hour
    elif (option == "17"):
        try:
            userSpeed = float(input("Enter speed in Knots per second: "))
            speed = (userSpeed * 1.151)
            speedUnit = "Miles per hour"
            unitSymbol = "MPH"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Knots to Feet per second
    elif (option == "18"):
        try:
            userSpeed = float(input("Enter speed in Knots per second: "))
            speed = (userSpeed * 1.688)
            speedUnit = "Feet per second"
            unitSymbol = "FT/S"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Knots to Meter per second
    elif (option == "19"):
        try:
            userSpeed = float(input("Enter speed in Knots per second: "))
            speed = (userSpeed / 1.944)
            speedUnit = "Meters per second"
            unitSymbol = "M/S"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()

    # Convert from Knots to Kilometers per hour
    elif (option == "20"):
        try:
            userSpeed = float(input("Enter speed in Knots per second: "))
            speed = (userSpeed * 1.852)
            speedUnit = "Kilometers per hour"
            unitSymbol = "KM/H"
            return speed, speedUnit, unitSymbol
        except:
            os.system('cls')
            print("Error: Please enter a number")
            main()
            

    # Exit the program
    elif (option == "exit") or (option == "quit"):
        exit()

    # Display Error if user enters a non-valid option
    else:
        
        os.system('cls') # Clear Screen
        print("Invalid option")
        main()



def main():
    option = input("1. Convert from Miles per hour to Kilometers per hour \n2. Convert from Miles per hour to Feet per second"
                   "\n3. Convert from Miles per hour to Meters per second\n4. Convert from Miles per hour to Knots"
                   "\n5. Convert from Kilometers per hour to Miles per hour\n6. Convert from Kilometers per hour to Feet per second"
                   "\n7. Convert from Kilometers per hour to Meters per second\n8. Convert from Kilometers per hour to Knots"
                   "\n9. Convert from Feet per second to Miles per hour\n10. Convert from Feet per second to Meters per second"
                   "\n11. Convert from Feet per second to Kilometers per hour\n12. Convert from Feet per second to Knots"
                   "\n13. Convert from Meters per second to Miles per hour\n14. Convert from Meters per seoncd to Feet per second"
                   "\n15. Convert from Meters per second to Kilometers per hour\n16. Convert from Meters per second to Knots"
                   "\n17. Convert from Knots to Miles per hour\n18. Convert from Knots to Feet per second"
                   "\n19. Convert from Knots to Meters per second\n20. Convert from Knots to Kilometers per hour: ").lower()
    easterEggs(option)
    speed, speedUnit, unitSymbol = convertSpeed(option)
    print(f"The speed in {speedUnit} is:", speed, unitSymbol)
    ExitorContinue()


main()
