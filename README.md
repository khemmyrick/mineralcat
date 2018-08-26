# MINERAL CATALOG

#Just Did
1. Started work on basic templates and views.
2. Added 2nd migration to load JSON. (as of 12:20pm August 26).
3. Generic sample minerals plus full list from json now display on mineral_list template.
4. Basic setup and Django review steps / version update parsing / pre-test debugging.

# To Do:

1. Get basic Django views/templates up and running.
- Get working index page mineral detail/mineral list pages.
- Get this step done before worrying about JSON. 

2. Find pattern for applying JSON fixture to minerals app.
- ???????
- Attempt applying with manual migration.
- Deserialization?

3. Update mineral_list.html template (and mineral_list view) to show names of all minerals.
- This view should display the name of each mineral in the database.
- Each name in the list is a link to the detail view of the mineral.

4. Update mineral_detail template and view.
- The detail view should display the details of the selected mineral.
- The details template should contain the mineral’s name, image, and image caption.
- Other details that are available about the mineral should be displayed below the image caption.
- Use a template filter to display the name of each attribute in title case.

5. Write unit tests to test that each view is displaying the correct information.
- Doublecheck TDD section of Django Basics course.
- Use Slack.  Do not be stuck on this step for more than 2 days.
- Possibly do this step after EC step.

# EXTRA CREDIT

6. EC: Display the most common or important details at the top of the details list. 
- You can decide on what order to display them in.
- The other miscellaneous details can be in any order.

7. EC: Add a link that goes to a random mineral details page.
- import random as easy_money
- if easy_money: self.high_five(self)
- write more noob coding jokes.

8. EC: In addition to those provided, additional styles are added and used.