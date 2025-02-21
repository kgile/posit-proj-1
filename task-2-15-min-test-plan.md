
# Posit Cloud Smoke Test Plan

High level functional test of Posit Cloud which can be executed manually in 15 minutes.  This covers click through of almost all links/dialogs, and execution of primary functionality.

A 15 minute test for this scope of functionality focuses on positive test cases with limited or no
- negative cases:  verifying proper handling of invalid input and actions
- edge cases:  input too large, input too small, etc.
- Web GUI specific concerns:  accessibility, internationalization, penetration, etc.

Caviat:  this test plan is written based on observed behavior of functionality rather than on functional requirements or other description of expected behavior.  As such, functionality may be missed or misunderstood.



## Prereq: Log into Posit Cloud


## Landing page format

### Navigation pane

Verify:
1. Navigation pane is anchored on the left side of the page
2. Navigation pane header contains the Posit logo, "posit Cloud" and an x push button.  Only the x button is actionable.
3. "Spaces" section is below the header and has "Your Workspaces" which is highlighted and has a person icon, and "New Space" which has a + icon. Both are links.
4. "Learn" section is below "Spaces" and has "Guide" with a compas icon, "What's New" with an ! icon, "Recipes" with a chefs hat icon and "Cheatsheets" with a hexigon icon.  All 4 are links.
5. "Help" section is below "Learn" and has "Current System Status" with a diamond icon and "Posit Community" with a comment icon.  Both are links.
6. "Info" section is below "Help" and has "Plans & Pricing" with a $ icon and "Terms and Conditions" with a document icon.  Both are links.

Following the links and validation of the pages will be in later test cases in this plan.

### Footer

Verify:
1. Footer is blue with white text, it does not overlap the navigation pane
2. Posit logo and "posit Cloud" are on the left, not actionable
3. "Terms" and "Status" are under the logo, both are links
	- hover over "Terms" and confirm the link is https://posit.co/about/posit-service-terms-of-use/
	- hover over "Status" and confirm the link is https://status.posit.co
4. Facebook, LinkedIn, Instagram and Github icons are on the right, all are links
	- hover over the Facebook icon and confirm the link is https://pos.it/facebook
	- hover over the LinkedIn icon and confirm the link is https://pos.it/linkedin
	- hover over the Instagram icon and confirm the link is https://pos.it/instagram
	- hover over the Github icon and confirm the link is https://pos.it/github

No further verification of the links in the footer will be completed in this test, a longer test plan would follow the links

### Main pane

Verify "Your Workspace" is the main pane, further validation below


## Your Workspace

### Visual verification of pane controls

1. Header contains
	- "Your Workspace" which is a link, with your username in smaller type below
	- Tabs across the header are "Content", "Usage", and "About"
	- Profile link with your username is on the right, clicking on it pops up a dialog with jprofile information and links
2. Left navigation pane contains
	- "Your Content" 
	- "Archive" 
	- "Trash" 
3. Central pane contains
	- "Your Content ()" with the number of content items in the ()
	- "New Project" dropdown with "New Project from Template", "New RStudio Project", "New Jupyter Project", and "New Project from Git Repository"
	- Content list with "Access" and "Sort" dropdown controls and a search box


### Functional verification of "Your Content"

New Project from Template
1. Click "New Project" and click "New Project from Template"
2. Verify template list
3. Select a template
4. Click "OK"
5. Verify project is created and opened
6. Click on "Untitled Project" on the top to rename the project
7. Click on "Your Workspace" at the top
8. Verify the project is in the "Your Content" list with the expected name and that the number of projects has updated in the () next to "Your Content"

New RStudio Project
1. Click "New Project" and click "New RStudio Project"
2. Verify project is created and opened
3. Rename the project
4. Click on "Your Workspace" at the top
5. Verify the project is in the "Your Content" list with the expected name and that the number of projects has updated in the () next to "Your Content"

New Jupyter Project
1. Click "New Project" and click "New Jupyter Project"
2. Verify project is created and opened
3. Rename the project
4. Click on "Your Workspace" at the top
5. Verify the project is in the "Your Content" list with the expected name and that the number of projects has updated in the () next to "Your Content"
Note:  I could not add a Jupyter project in the free plan

New Project from Git Repository
1. Click "New Project from Git Repository"
2. Verify pop up dialog
Note: a longer test would create a project from a Git Repo

Click through the "Access" drop down entries and verify project list updates

Click through the "Sort" drop down entries and verify project list updates

Search the list
1. Enter a value in the search box which matches only one of the projects in the list and hit enter
2. Verify the project list updates with only the matching project
3. Click the x icon on the right of the search box
4. Verify the project list updates to show all of the projects

Copy a project
1. Click the copy button next to one of the projects in the list
2. Click OK in the pop-up dialog to copy the project
3. Veirfy project is created and opened
4. Click on "Your Workspace" at the top
5. Verify the project is in the "Your Content" list with the expected name and that the number of projects has updated in the () next to "Your Content"

Delete a project
1. Click the delete button next to one of the projects in the list
2. Verify the pop-up message that states the project has been deleted
3. Verify the project is no longer in the list

Export a project
1. Click the export button next to one of the projects on the list
2. Verify the "Project Export Complete" pop-up and click the "Download" button 
3. Verify the project zip file downloaded
4. Verify the project is still in the project list

Archive a project
1. Click the "..." icon next to one of the projects on the list and click "Move to Archive"
2. Verify the pop-up message that states the project has been archived
3. Verify the project is no longer on the project list

Click the "..." icon next to one of the projects on the list and click "Share Link", verify the pop-up

Click the "..." icon next to one of the projects on the list and click "Settings", verify the settings pop-up
Note: normally I would put information on what to verify.


### Functional verification of Your Workspace navigation pane, Archive and Trash

1. Navigate to "Archive" 
2. Verify the archive page opens and has at least one entry.  Note: this must be executed after the "Archive a project" test above
3. Click "Move to Trash" next to a project
4. Verify the project is removed from the list
5. Navigate to "Trash"
6. Verify the trash page opens and has at least two entries.  Note: this must be executed in order also.
7. Click "Restore" on one of the projects and "Move to Archive" on the other
8. Verify the two projects are no longer on the list
9. Navigate to "Archive" and verify the project moved is there
10. Click "Restore" on a project in the list
11. Navigate to "Your Content" and verify both restored projects are in the list.
12. Click "Delete" on one of the projects
13. Navigate to "Trash"
14. Click "Empty Trash"
15. Click "OK" to confirm emptying the trash
16. Verify the trash list is empty
17. Navigate to "Your Content" and verify none of the projects which were in the trash are on the project list
 
### Functional verification of header

Usage
1. Click on "Usage" in the header
2. Verify "Compute Hours", "Active Content", and "Compute Hours" contain content which reflects at least the usage during this test
3. Verify "Content" contains entries for at least the projects completed in this test
4. Click another date in the date list across the top and verify the page content changes
5. Click the drop down menu to switch from "Usage Period" to "Calendar Month" and verify the page content changes
6. Click another month in the month list across the top and verify the page content changes

About
1. Click About, verify information is provided


## Functional verification of Posit Cloud navigation pane

### New Space

1. Click "New Space"
2. Enter a space name in the pop-up dialog and click "Create"
3. Verify a new space is in the navigation pane with the name provided in the previous step
4. Verify the main pane now shows the new space, and that there are "Data" and "Members" links on the top of the page
5. Click "Data" and verify the page opens
6. Click "Members" and verify the page opens with you as a member
7. Dismiss the information pane on the right
8. Click "Leave Space" on the top right, chose either of the radio buttons, and click OK
9. Verify the center pane goes back to "Your Workspace" and that the new space is no longer on the navigation pane

Click "Guide" and verify a new tab opens with documentation

Click "What's New" and verify a new tab opens with the new information

Click "Recipies" and verify the main pane updates with "Posit Recipies"

Click "Cheatsheets" and verify a new tab opens with cheatsheet information

Click "Current System Status" and verify a new tab opens with system status

Click "Posit Community" and verify a new tab with a bulletin board opens

Click "Plans & Pricing" and verify the main pane updates with pricing information

Click "Terms and Conditions" and verify a new tab opens with terms of use
