# ---------- Strings ----------

strSplashScreen = """
-----------------------------------------------------
|       JHUB Coding Scheme - Module 3: Python       |
|               Drone Guidance System               |
|                                                   |
|           Author: Alex Huetson (30299165)         |
-----------------------------------------------------
Available Commands:
"""

strExplainScreen = "The drone knows where it is at all times. It knows this because it knows where it isn't. By subtracting where it is from where it isn't, or where it isn’t from where it is, it obtains a difference or deviation. The guidance subsystem uses deviations to generate corrective commands to drive the drone from a position where it is to a position where it isn't and arriving at a position that it wasn't, it now is. Consequently, the position where it is is now the position that it wasn't, and it follows that the position that it was is now the position that it isn't. In the event that the position that it is in is not the position that it wasn't, the system has acquired a variation. The variation being the difference between where the drone is and where it wasn't. If variation is considered to be a significant factor, it too may be corrected by the GEA. However, the drone must also know where it was. The drone guidance computer scenario works as follows: Because a variation has modified some of the information that the drone has obtained, it is not sure just where it is. However, it is sure where it isn't, within reason, and it knows where it was. It now subtracts where it should be from where it wasn't, or vice-versa. And by differentiating this from the algebraic sum of where it shouldn't be and where it was, it is able to obtain the deviation and its variation, which is called error."

# ---------- Data ----------

tupGridSize = (12, 12) # Although lists start at 0, we want it to be 1 size larger because we want to add numbering later on. This is also easier for users heads.

dctCommands = {
    "STOP": ["Stops the program.", "CMD: Stopping program.", quit],
    "EXPLAIN": ["Explains how drones work", ("CMD: Explaining how drones work.\n" + strExplainScreen), lambda *args: None],
}

dctDirections = {
    "N": (0, 1),
    "S": (0, -1),
    "W": (-1, 0),
    "E": (1, 0),
}