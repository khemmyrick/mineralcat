# MINERAL CATALOG

#Just Did
1. Started work on basic templates and views.
2. Attempted to add 2nd migration to load JSON.
- When load_rocks was in migrations dir (as 0002_load_rocks)
it raised a NodeNotFound error, which seems to think that either
the initial migration never happened, or that load_rocks
can't be dependent on 0001_initial forsome other reason.
3. Basic setup and Django review steps / version update parsing / pre-test debugging.

# To Do:

4. Get basic Django views/templates up and running.
- Get working index page mineral detail/mineral list pages.
- Get this step done before worrying about JSON. 

5. Find pattern for applying JSON fixture to minerals app.
- ???????
- Attempt applying with manual migration.
- Deserialization?

6. Update mineral_list.html template (and mineral_list view) to show names of all minerals.
- This view should display the name of each mineral in the database.
- Each name in the list is a link to the detail view of the mineral.

7. Update mineral_detail template and view.
- The detail view should display the details of the selected mineral.
- The details template should contain the mineral’s name, image, and image caption.
- Other details that are available about the mineral should be displayed below the image caption.
- Use a template filter to display the name of each attribute in title case.

8. Write unit tests to test that each view is displaying the correct information.
- Doublecheck TDD section of Django Basics course.
- Use Slack.  Do not be stuck on this step for more than 2 days.
- Possibly do this step after EC step.

# EXTRA CREDIT

9. EC: Display the most common or important details at the top of the details list. 
- You can decide on what order to display them in.
- The other miscellaneous details can be in any order.

10. EC: Add a link that goes to a random mineral details page.
- import random as easy_money
- if easy_money: self.high_five(self)
- write more noob coding jokes.

11. EC: In addition to those provided, additional styles are added and used.