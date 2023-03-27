# COVID-Tracker
Comp-sci project on an embedded system that can track COVID over time.

The system works by having a set of Microbits that are able to communicate between each other via a P2P type of network.
This allows them to determine their distance from each other and whether each of them have COVID-19 as determined by the individuals carrying them. 
If an individual has COVID-19, they can press the A button to flag themselves as being Infected and any individuals near them will be flagged as a Close Contact.
The B button on the Microbit allows the user to start a 20 second timer for washing hands as well to allow for better etiquette in times of disease.

Each Microbit is constantly sending signals, which are picked up by a central Server Microbit. 
This Microbit packages all incoming data and allows the computer it is connected to to read off the data from the serial interface. 
The computer further processes the data to be displayed in both the Json and CSV formats, allowing for access to the information from a remote location. 
This also allows individuals who were near a person before that person got infected, to now be sure to isolate as they are now a Close Contact.
