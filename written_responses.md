1. What is a regular expression and how does it work?

   > A regular expression is a special type of text string that allows you to describe a particular search pattern.
   > You can write simple characters and wildcard notations in a text file to search for a phone number or a email address
   > Like pattern = r"[0-9]{3}[-][0-9]{3}[-][0-9]{4}|[0-9]{10}|[(][0-9]{3}[)]\s[0-9]{3}[-][0-9]{4}|[0-9]{3}\s[0-9]{3}\s[0-9]{4}"

2. What is an array and how does it work?

   > Array is a data structure at its simplest form. We where told that "An array is a sequence of elements of the same type
   > stored in a contiguous block of memory"
   > Arrays are storage containers that contain a fixed number of values.
   > How does it work? or How do we declare the array. Arrays work by being declared.
   > 1 Determine how big you array needs to be
   > 2 Request a block of memory that will fit that array
   > 3 Receive the address of memory of the reserved block
   > 4 Write your values in that block to form the array

3. What is a hash table and how does it work?
   > Has tables are another type of data structure.
   > They are called Dictionaries in Python and are know by many other names. Like Associative Arrays
   > It is a Key/Value data storage and retrieval.
   > They way it works is array is declared. Then a Hash table will take a key and run it through a Hash function
   > this will then change that key into an integer then it wil take the new hash key and vert that to an array index via a modulo function.
