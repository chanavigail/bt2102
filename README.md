# A Library System

<p> A standalone app created to mimic a library system. The system supports the following functions: </p>
<ul>
  <li> Library membership creation, deletion, and updating of details </li>
  <li> Book borrowing and returning </li>
  <li> Book reservation and cancellation </li>
  <li> Fine payment, if any, for overdue book returns </li>
  <li> Book details search </li>
  <li> Displaying all books on loan and on reservation </li>
  <li> Displaying members who have outstanding fine payments </li>
  <li> Displaying books on loan to a member given their membership ID </li>
</ul>

<p> App GUI was developed using tkinter, functions in python were integrated with a local MySQL database. </p>

### User guide
<ol>
  <li> Download all files. LibBooks.txt and LibMems.txt are not required for the app to be functional, but are provided to give the user sample data. </li>
  <li> App was created to be run locally, thus a local instance has to be created using MySQL Workbench. In the constructor method for the database in lib/sql_database.py, replace the host, port, user, and passwd arguments in mysql.connector.connect() with the details of the user's local database. </li>
  <li> Run the queries found in bt2102db.sql in MySQL Workbench in the local instance created. Sample data and queries are provided to populate the tables, but is not required for the app to be functional. </li>
  <li> Run main.py in the terminal. </li>
</ol>
