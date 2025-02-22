# posit-proj-1

Task 1 is in the file task-2-15-min-test-plan.md

Task 2 instructions:

- have an environment with python 3.13.2 and pip installed and the path to the python executible in your path
- clone this repo into a directory
- change to that directory
- do the following to install selenium:   _pip install -r requirements.txt_
- edit task-2-test.py and enter user email and password values at lines 
- do the following to run the test: _python3 task-t-test.py_
- note, may be _py_ or _python_ instead of _python3_ depending on your environment


Notes:

It has been 7 years since I wrote web GUI automation and I am rustier than I expected in finding ways
to access the controls.  I simply ran out of time because that slowed me down quite a bit and I have a 
hard stop since I'm flying out tomorrow morning.  I hope the code I've written gives you what you need
to evaluate my coding skills.

I decided to break the test into two test cases, create a new space and ad an RStudio project.  In the end
I only made it partially through the first test case.  

If I had successfully created a new space, I would have validated several items in the new space page to 
confirm the space was created successfully.

The second test case would have used the space created by the first test case

There are several things I would normally do differently.
- I would normally use a logger with formatting and log levels
- I would normally have more exception catching and provide good errors
- I would have used one of the more advanced test libraries, like nose2, for more test functionality
