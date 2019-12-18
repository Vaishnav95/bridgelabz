'''
Customize Message Demonstration using String Function and RegEx
a. Desc -> Read in the following message: Hello <<name>>, We have your full
name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx.
Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016.
Use Regex to replace name, full name, Mobile#, and Date with proper value.
b. I/P -> read in the Message
c. Logic -> Use Regex to do the following
Replace <<name>> by first name of the user ( assume you are the user)
replace <<full name>> by user full name.
replace any occurance of mobile number that should be in format
91-xxxxxxxxxx by your contact number.
replace any date in the format XX/XX/XXXX by current date.
d. O/P -> Print the Modified Message.
'''

from utils import Util

regex_object = Util()
regex_string = regex_object.regex_string()