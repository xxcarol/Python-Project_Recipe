Team: DFP C2 Group 6
Team Members: Thara P., Jessica S., Carol X., Zina O.
Company Name: Ricetta


Demo Video Link: https://youtu.be/XtELNqIx3k4


Overview: 
Ricetta has three functionalities: 


Functionality 1: return 10 random recipes when user enters one or multiple ingredients, scraped from AllRecipes website, EatingWell website and Recipe Puppy API. See Function1.jpeg for an example.
Functionality 2: return 10 most popular recipes with the highest ranking on social media when user enters an ingredient, scraped from Food2Fork API. See Function2.jpeg for an example.
Functionality 3: show a bar chart with the number of recipes within each broad category to user. When user searches for a particular category, return a word cloud of a subset of categories. When user picks an ingredient, return 10 recipes ranked by popularity. This functionality utilizes Kaggle Epicurious Recipe Data in JSON format. See Function3.jpeg for an example.


The four .py files (‘Group6_Ricetta.py’, ‘Function1.py’, ‘Function2.py’, ‘Function3.py’) together achieve those three functionalities. 


To Run:
* Install Python packages (web driver, word cloud).
   * Need to install wordcloud - run the following code in command prompt:
pip install wordcloud
   * Need to install chromedriver
      * https://sites.google.com/a/chromium.org/chromedriver/downloads - download chrome driver zip file and run executable file
* Optional:
   * JSON file has been parsed into CSV. Program can run from JSON by passing through False to the cat_char function or run from CSV by passing through True to the cat char function. Default is set to run from CSV
   * Two datasets from websites (AllRecipies.com & EatingWell.com) have been scrapped and saved as .xlsx to the project folder for ease of running the program. However, to scrape the data again, you can run eatingWell.py and allRecipes.py to recreate EatingWellRecipes.xlsx and AllRecipes.xlsx. Fill the chromedriver file path in the head of the program first.
* Run Group6_Ricetta.py: 
   * All the packages and modules at the top will be imported.
   * The user will be asked to choose which functionality they would like to search recipes by:
      * Ingredients
      * Based on social media ranking popularity
      * Based on categories, ingredients and ratings
   * If user chooses 1 (calls a function in Function1.py) or 2 (calls a function in Function3.py), the program will prompt user to enter ingredients and prints the top 10 recipes in the console ordered either randomly with the first feature or by social media rankings with the second option.
   * If the user selects option 3 (calls a function in Function3.py), the program will print bar chart of the 10 most popular recipe categories along with the number of recipes labeled with that category tag
   * The user will be prompted to enter a category.
   * The program will print a word cloud of popular categories within the category that was chosen to give a particular subset and prompts user to choose an ingredient. 
   * When the user provides an ingredient, the top 10 recipes (if there are more than 10) are printed ranked descending based on popularity.


The source code folder contains:
* 6 python code files
* 4 image files
* 2 excel files
* 1 csv file
* 1 txt file (readme)
* 1 video demonstration
