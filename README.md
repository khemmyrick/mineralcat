# MINERAL CATALOG

#Just Did
1. Started work on basic templates and views.
2. Added 2nd migration to load JSON. (as of 12:20pm August 26).
3. Generic sample minerals plus full list from json now display on mineral_list template.
4. Added mineral.attributes to mineral_detail view.
5. Basic setup and Django review steps / version update parsing / pre-test debugging.

# To Do:

1. Update mineral_list.html template (and mineral_list view) to show names of all minerals.
- Each name in the list is a link to the detail view of the mineral.

2. Update mineral_detail template and view.
- The detail view should display the details of the selected mineral.
- The details template should contain the mineral’s name, image, and image caption.
- Other details that are available about the mineral should be displayed below the image caption.
- Use a template filter to display the name of each attribute in title case.

3. Write unit tests to test that each view is displaying the correct information.
- Doublecheck TDD section of Django Basics course.
- Use Slack.  Do not be stuck on this step for more than 2 days.
- Possibly do this step after EC step.

# EXTRA CREDIT

4. EC: Display the most common or important details at the top of the details list. 
- You can decide on what order to display them in.
- The other miscellaneous details can be in any order.

5. EC: Add a link that goes to a random mineral details page.
- import random as easy_money
- if easy_money: self.high_five(self)
- write more noob coding jokes.

6. EC: In addition to those provided, additional styles are added and used.