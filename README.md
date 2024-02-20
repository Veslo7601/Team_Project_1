Quick Description:
The "Address Book" application is designed to help organize personal contact information efficiently. 
Users can easily add and manage contact names and phone numbers. 
Additionally, the application allows for the inclusion of various additional details 
for each contact, such as address, birthday, and email. 
Users can edit or delete existing contact information as needed. 
The program also features a notes section where users can add any supplementary information. 
Other functionalities include viewing the entire contacts list, searching contacts by name or phone number, 
filtering contacts by notes, and displaying contacts with upcoming birthdays. The application seamlessly 
loads data from a data file and stores any changes made to the contacts in a binary data file.

The "Address Book" application adheres to the PEP8 standard and has been developed using both object-oriented programming (OOP) 
and functional approaches. This design choice ensures flexibility and allows for the easy addition of new features in the future.

Quick Instruction:
Users can operate the "Address Book" application using the following commands:

hello: Prints a greeting message.
add <contact name> <phone number>: Adds a new contact or updates the phone number if the contact name already exists.
update <contact name> <old phone> <new phone>: Updates the phone number for a specific contact.
delete <contact name>: Deletes the specified contact.
remove <contact name> <phone>: Deletes a specific phone number associated with a contact.
show all: Displays the entire Address Book.
find <name or phone>: Filters contacts by name letters or phone number.
exit, goodbye, close: Saves any changes to the database and exits the application.
add-address <name, address>: Adds an address for the specified contact.
add-email <name, email>: Adds an email address for the specified contact.
add-birthday <name, birthday>: Adds a birthday for the specified contact.
write <name, note>: Adds a note for the specified contact.
delete-note <name, note>: Removes a note associated with the specified contact.
edit-note <name, note>: Edits an existing note.
find-note <note>: Finds contacts with a specific note.
show-birthdate <number of days>: Displays all contacts with birthdays occurring within the specified number of days.
