import webbrowser
import time

# Set the initial condition to True
condition = True

# While loop to keep checking the condition
while condition:
    url = "https://www.eliteprospects.com/player/282612/henry-mckinney"  # Replace with the desired URL
    webbrowser.open(url)
    
    # Optional: wait for a while before the next iteration to avoid opening too many tabs quickly
    time.sleep(1)
    
    # If you want to break the loop at some point, you can add a condition here.
    # For example, to stop after opening the URL once:
    # condition = False  # Remove or adjust this line as needed
