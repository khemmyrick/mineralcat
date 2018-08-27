# MINERAL CATALOG

#Just Did
1. Started work on basic templates and views.
2. Added 2nd migration to load JSON. (as of 12:20pm August 26).
- Deleted original database to clean out sample minerals and data from unsuccessful migrations.
- Successfully remigrated 2nd migration.
3. Full list from json now displays on mineral_list template with appropriate mineral_detail anchor tags.
4. Added mineral.attributes to mineral_detail view.
5. Added random_mineral view. Relatively easy money, as expected.
6. Basic setup and Django review steps / version update parsing / pre-test debugging.


# To Do:

1. Update mineral_detail template and view.
- The detail view should display the details of the selected mineral.
- The details template should contain the mineral’s name, image, and image caption.
- Other details that are available about the mineral should be displayed below the image caption.
- Use a template filter to display the name of each attribute in title case.

2. Write unit tests to test that each view is displaying the correct information.
- Doublecheck TDD section of Django Basics course.
- Use Slack.  Do not be stuck on this step for more than 2 days.
- Possibly do this step after EC step.

# EXTRA CREDIT

3. EC: Display the most common or important details at the top of the details list. 
- You can decide on what order to display them in.
- The other miscellaneous details can be in any order.

4. EC: In addition to those provided, additional styles are added and used.