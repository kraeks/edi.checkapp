# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.checkapp -t test_fragebogen.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.checkapp.testing.EDI_CHECKAPP_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/checkapp/tests/robot/test_fragebogen.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Fragebogen
  Given a logged-in site administrator
    and an add Fragebogen form
   When I type 'My Fragebogen' into the title field
    and I submit the form
   Then a Fragebogen with the title 'My Fragebogen' has been created

Scenario: As a site administrator I can view a Fragebogen
  Given a logged-in site administrator
    and a Fragebogen 'My Fragebogen'
   When I go to the Fragebogen view
   Then I can see the Fragebogen title 'My Fragebogen'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Fragebogen form
  Go To  ${PLONE_URL}/++add++Fragebogen

a Fragebogen 'My Fragebogen'
  Create content  type=Fragebogen  id=my-fragebogen  title=My Fragebogen

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Fragebogen view
  Go To  ${PLONE_URL}/my-fragebogen
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Fragebogen with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Fragebogen title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
