# courseFeedbackBot
Fills all the sections as "Excellent" and fills the remarks as "Very good class"

Open up the Course Feedback tab in Academia and refresh it to reset all values. 

To run the bot:
1. Type the following command in your terminal/command prompt to install pynput module:

```
pip install pynput
```
2. Download 'filler.py' file from the repository

3. In terminal, go to the directory where filler.py has been saved and enter: 
```
python3 filler.py
```
if python is not detected, enter:
```
python filler.py
```

4. Wait for the prompt,enter number of theory and practical courses according to the website, then select the first empty field under Theory and press shift to start.

 Note : Windows may detect the script as a threat due to KeyLogging. This is because this program checks if the user inputs 'Shift' on keyboard. Click on the notification that pops up and click on 'Allow on Device' under Threat and Security Settings.

5. Wait for a few seconds. The script will fill in the website.

6. Press 'shift' again to stop the bot. Warning: You will have to restart from the first field once script is interrupted.
