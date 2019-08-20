# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.checkapp -t test_hinweistext.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.checkapp.testing.EDI_CHECKAPP_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/checkapp/tests/robot/test_hinweistext.robot
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

Scenario: As a site administrator I can add a Hinweistext
  Given a logged-in site administrator
    and an add Fragebogen form
   When I type 'My Hinweistext' into the title field
    and I submit the form
   Then a Hinweistext with the title 'My Hinweistext' has been created

Scenario: As a site administrator I can view a Hinweistext
  Given a logged-in site administrator
    and a Hinweistext 'My Hinweistext'
   When I go to the Hinweistext view
   Then I can see the Hinweistext title 'My Hinweistext'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Fragebogen form
  Go To  ${PLONE_URL}/++add++Fragebogen

a Hinweistext 'My Hinweistext'
  Create content  type=Fragebogen  id=my-hinweistext  title=My Hinweistext

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Hinweistext view
  Go To  ${PLONE_URL}/my-hinweistext
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Hinweistext with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Hinweistext title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
