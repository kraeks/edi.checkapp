# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.checkapp -t test_antwortoption.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.checkapp.testing.EDI_CHECKAPP_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/checkapp/tests/robot/test_antwortoption.robot
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

Scenario: As a site administrator I can add a Antwortoption
  Given a logged-in site administrator
    and an add Fragestellung form
   When I type 'My Antwortoption' into the title field
    and I submit the form
   Then a Antwortoption with the title 'My Antwortoption' has been created

Scenario: As a site administrator I can view a Antwortoption
  Given a logged-in site administrator
    and a Antwortoption 'My Antwortoption'
   When I go to the Antwortoption view
   Then I can see the Antwortoption title 'My Antwortoption'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Fragestellung form
  Go To  ${PLONE_URL}/++add++Fragestellung

a Antwortoption 'My Antwortoption'
  Create content  type=Fragestellung  id=my-antwortoption  title=My Antwortoption

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Antwortoption view
  Go To  ${PLONE_URL}/my-antwortoption
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Antwortoption with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Antwortoption title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
