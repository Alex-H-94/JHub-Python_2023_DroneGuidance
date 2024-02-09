from data import strSplashScreen, tupGridSize, dctCommands, dctDirections

class ExpCommandInput (Exception): pass
class ExpRouteInvalid (Exception): pass

def main():
    # ===== Decorate the landing screen. This could be put inside the while loop with a command to clean up the interface, but that might interfere with the automatic code checker.
    print(strSplashScreen)
    for key in dctCommands:
        print(f"> {key} : {dctCommands[key][0]}")
    
    # ===== Begin.
    while True:
        try:
            lstPlottedRoute = [[
                    [] for x in range(-1, tupGridSize[0]) # start at -1 to make grid +1 longer for space for numbering down the side.
                ] for y in range(0, tupGridSize[1])
            ]
            
            strFileName = input("\nEnter the next route instructions file: ")
            
            # ===== Check if what is entered matches any given commands. Execute if so.
            if strFileName.upper() in dctCommands: # .upper() used to accept variations like 'Stop' 'stop' or 'StOp'.
                print(dctCommands[strFileName.upper()][1])
                dctCommands[strFileName.upper()][2]()
                raise ExpCommandInput # User did not enter a file name, so skip the rest of the functionality.
            
            # ===== Adjust the user input if they wrote 'routexxx' instead of 'routexxx.txt'
            if strFileName[-4:] != ".txt":
                strFileName += ".txt"
                
            # ===== Attempt to open the file.
            f = open(strFileName, 'r')
            lstRoute = f.readlines()
            f.close()
            
            # ===== Get the starting point. -1 accounts for computers starting lists at '0' vs humans entering values from '1'.
            tupStartPos = (int(lstRoute[0]) - 1, int(lstRoute[1]) - 1)
            
            # ===== Begin calculating the plotted route and saving it.
            tupCurrentPos = tupStartPos
            lstPlottedRoute[tupCurrentPos[1]][tupCurrentPos[0] + 1] = " S " # Mark the start. +1 accounts for the grid being +1 longer to accomodate numbering.
            
            for i in range(len(lstRoute[2:])): # Begin :2 steps in, to account for the first two values being the starting coords.
                dir = lstRoute[i + 2].strip() # Clean the value of any formatting. +2 accounts for the first two values being the starting coords.
                
                if dir in dctDirections:
                    tupCurrentPos = ((tupCurrentPos[0] + dctDirections[dir][0]), 
                                        (tupCurrentPos[1] + dctDirections[dir][1]))
                                                            
                    if (tupCurrentPos[0] > tupGridSize[0] # Check if its within grid bounds.
                        or tupCurrentPos[0] < 0 
                        or tupCurrentPos[1] > tupGridSize[1] 
                        or tupCurrentPos[1] < 0):
                        raise ExpRouteInvalid
                    else:
                        lstPlottedRoute[tupCurrentPos[1]][tupCurrentPos[0] + 1] = " x " 
                else:
                    raise ExpRouteInvalid # If there is an unknown direction, force a failure.
            
            # ===== Print grid and numbering.
            for lstLine in reversed(lstPlottedRoute): # Reverse the rows, otherwise it'll print upside down.                                
                for i in range(len(lstLine)):
                    if i == 0: lstLine[i]= f" {(lstPlottedRoute.index(lstLine) + 1):02d} " # Add numbering on the first line. +1 accounts for numbering starting at 0. ':02d' converts single digits to double digits for formatting.
                    if not lstLine[i]: lstLine[i]= " - " # If there is no value (" x ") then insert an 'empty' value instead.
                
                print(*lstLine)

            strNumbering = ""            
            for i in range(tupGridSize[0]+1): # Finally, print all the numbers on the bottom.
                strNumbering += f" {i:02d} "
                
            print(strNumbering)
            
            # ===== Complete.
               
        except ExpCommandInput:
            continue
        
        except FileNotFoundError as fnf:
            print(f"File not found: {fnf.filename}. Ensure the .txt is in the same directory as the script.") # Always helpful for the user.
            continue
        
        except ExpRouteInvalid:
            print("Error: The route is outside of the grid.")
            continue

if __name__ == "__main__":
    main()