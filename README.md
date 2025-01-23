# Zodiac and Season Game

![imagezodiac png](https://github.com/user-attachments/assets/fc0b4f03-2599-455d-9245-c8008dd3d817)

Welcome to the zodiac and Season Game! This interactive application allows users to discover their 
zodiac sign and the corresponding season based on their birth date.The app is built using Python's 
Tkinter library for the graphical user interface (GUI) AND UTILIZES JSON data for zodiac sign 
information.

## FEATURES 
- **Zodiac Sign Calculation**: Enter your day and month of birth to find your zodiac sign along with a custom message.
- **Season Calculation**: Enter your birth month to find out the season of the year you were born in.
- **User-Friendly GUI**: Built using Tkinter for a simple and interactive experience.
- **Background Image**: The window is styled with a visually appealing background image.

## REQUIREMENTS 
Before running the project, make sure you have the following Python libraries installed:
- `Tkinter` (usually comes with Python)
- `Pillow` (for handling images)
- `json` (for loading and parsing JSON files)

You can install Pillow with the following command:

```bash
pip install pillow

```
## SETUP AND INSTALLATION
   
   1. Clone this repository to your local machine:
bash
git clone https://github.com/yourusername/zodiac-and-season-game.git
cd zodiac-and-season-game

   2. Prepare the necessary JSON file:

  Ensure that you have a Zodiacsigns.json file that contains the zodiac sign data.
  This file is required to fetch the zodiac messages. The file should have a structure that 
  contains zodiac signs and their descriptions.
  
  3. Run the application: To run the application, simply execute the following command:
```bash
python main.py
```
## HOW TO RUN  
1.Enter the day of your birth (between 1-31) and the month (between 1-12) in the provided fields.
2.Click "See your zodiac sign" to calculate and display your zodiac sign along with a brief message.
3.Click "See your season of the year" to find out which season you were born in based on your birth month.
4.Click "Exit" to close the application.

## EXAMPLE SCREENSHOTS

![Screenshot 2025-01-23 201939](https://github.com/user-attachments/assets/1100bf0c-088f-4479-9b81-7b28159e9ae8)


## CONTRIBUTING 
If you would like to contribute to this project, feel free to fork the repository, 
make your changes, and submit a pull request.
Steps for contribution:
1. Fork the repository.
2. Create a feature branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new pull request.


## ACKNOLEDGMENTS
Thanks to the contributors who helped improve the code.
The app uses the Pillow library for image handling.
Tkinter for creating the graphical user interface.






