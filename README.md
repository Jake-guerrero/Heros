# Heros
<br/>

This project delves into heros and villians, addressing a handful of questions:
1. How much does the character weigh?
2. How tall is the character?
3. Is the character a hero, villian, or does not fit the category?
4. Which race does a character fall into?
5. Which publisher has the most characters?


## **Getting the Project to Run**


1. Install Python3: Ensure you have Python3 insalled on your computer. Use '<strong>pip install --upgrade pip</strong>' to update pip if neccessary in the terminal.
* If you are running on Windows, the command would be '<strong>py -m pip instsall --upgrade pip</strong>'. Or use '<strong>pip3 -m pip install --upgrade pip</strong>' if you are using macOS.
2. Clone the Respository: Download or clone the repository from Github to a directory of your choice.
* Find and click on the green "<strong>Code</strong>" button at the top of the repository page, copy the URL, and run the following command in your terminal: "<strong>git clone [URL]</strong>. Replace '<strong>[URL]</strong> with the URL you copied.
3. Set Up a Virtual Environment:
* Navigate to the cloned repository folder using your file explore.
* Open a command terminal by typing 'cmd' into the file path line. On macOS, type the command '<strong>cd</strong>'
* Create a virtual enviroment by running: '<strong>py -m venv env</strong>'. This creates a folder named 'env' within your repository to house the virtual environment.
* Activate the virtual environment by running: '<strong>.\env\Scripts\activate</strong>' (on Windows) or '<strong>source env/bin/activate</strong>' (on macOS/Linux). You will see '<strong>(env)</strong>' preceding your directory path, indicating that the virtual environment is active.
4. Install Project Dependencies: Ensure you are in the project directory and install the required packages by running: '<strong>pip install -r requirements.txt</strong>'. This will install the neccessary libraries for the project, which includes:
* '<strong>numpy</strong>'
* '<strong>pandas</strong>'
* '<strong>matplotlib</strong>'
5. Run the Program: Execute the program by typing: '<strong>python superheros.py</strong>' in the command terminal. If you are using Python3, execute the program by typing: '<strong>python3 superheros.py</strong>'.
* If you are not in the Heros directory, use the '<strong>cd</strong>' command to go into the Heros directory.
* When the code is run through powershell, execute the program by typing: <strong>python .\superheros.py</strong>'.
6. Deactivate the Virtual Environment: After you are finished with the program, deactivate the virutal environemnt by running: '<strong>deactivate</strong>' in the command terminal.

After running the code, three visualizations will appear:
1. <strong>Alignment for Comic Book Character</strong>: This visual displays the alignments of the characters from the csv.
2. <strong>Top Five Races by Count</strong>: This visual shows the top five races (other, human, mutant, god, and human/radiation) will fall into.
3. <strong>Top 5 Publishers by Numbers of Heros</strong>: This visual illustrates the number of characters of the top 5 publishers.

To navigate through the visuals, close each window using the X button in the top-left or top-right corner of each visuals.


<br/>

This project was developed with a more fluid approach compared to the Video Game Sales project on my GitHub page. It was designed to demonstrate working with a single CSV DataFrame rather than two.

| Height | Weight | Race |
|:--------:|:--------:|:--------:|
|  How tall the characters are in cm   |  How much the character weighs  |  Where the character falls into what they were born into |

| Alignment | Publisher |
|:--------:|:--------:|
|  If the character is good, evil, or in between  |  The entity responsible for creating the character  |