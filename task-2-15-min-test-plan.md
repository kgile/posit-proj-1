
### Posit Cloud Smoke Test Plan

High level functional test of Posit Cloud which can be executed manually in 15 minutes

A 15 minute test for this scope of functionality focuses on positive test cases with limited or no
- negative cases:  verifying proper handling of invalid input and actions
- edge cases:  input too large, input too small, etc.
- Web GUI specific concerns:  accessibility, internationalization, penetration, etc.

Caviat:  this test plan is written based on observed behavior of functionality rather than on functional requirements or other description of expected behavior.  As such, functionality may be missed or misunderstood.


Prereq: Log into Posit Cloud


## Landing page format

# Navigation pane

Verify:
1. Navigation pane is anchored on the left side of the page
2. Navigation pane header contains the Posit logo, "posit Cloud" and an x push button.  Only the x button is actionable.
3. "Spaces" section is below the header and has "Your Workspaces" which is highlighted and has a person icon, and "New Space" which has a + icon. Both are links.
4. "Learn" section is below "Spaces" and has "Guide" with a compas icon, "What's New" with an ! icon, "Recipes" with a chefs hat icon and "Cheatsheets" with a hexigon icon.  All 4 are links.
5. "Help" section is below "Learn" and has "Current System Status" with a diamond icon and "Posit Community" with a comment icon.  Both are links.
6. "Info" section is below "Help" and has "Plans & Pricing" with a $ icon and "Terms and Conditions" with a document icon.  Both are links.

Following the links and validation of the pages will be in later test cases in this plan.

# Footer

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

# Main pane



## Your Workspace main pane

1. 