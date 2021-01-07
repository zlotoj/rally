import sys

from pyral import Rally, rallyWorkset
import configuration
import scrapping
from datetime import datetime

accepted = ['Accepted', 'Completed', 'Released-to-Production']
# projects = ['OrderSvc-KRK-TEAM2-IFS-45387011', 'OrderSvc-KRK-TEAM3-IFS-45387011',
#             'OrderSvc-KRK-TEAM7-IFS-46336952', 'OrderSvc-KRK-TEAM8-IFS-46336952'
projects = [
['OrderSvc-KRK-TEAM1-IFS-45387011'         , '112919413276d'],
['OrderSvc-KRK-TEAM2-IFS-45387011'         , '60188493954d'],
['OrderSvc-KRK-TEAM3-IFS-45387011'         , '42853899240d'],
['OrderSvc-KRK-TEAM4-IFS-46336961'         , '28264785372d'],
['OrderSvc-KRK-TEAM5-IFS-46336961'         , '46636368178d'],
['OrderSvc-KRK-TEAM6-IFS-46336961'         , '40622865014d'],
['OrderSvc-KRK-TEAM7-IFS-46336952'         , '146706645212d'],
['OrderSvc-KRK-TEAM8-IFS-46336952'         , '33531548540d'],
['OrderSvc-KRK-TEAM9-IFS-47149932'         , '40107009780d'],
['OrderSvc-KRK-TEAM10-IFS-47149932'        , '201000371296d'],
['OrderSvc-KRK-TEAM11-IFS-47149932'        , '180080401892d'],
['OrderSvc-KRK-TEAM12-IFS-47802415'        , '49311460719d'],
['OrderSvc-KRK-TEAM13-IFS-48159329'        , '32868951837d'],
# ['OrderSvc - BLR - TEAM14 - IFS - 200833177', '140580272260d'],
['SYSSERVICES-KRK-LibertyTG-IFS-46679659',   '38080841894d']]

iteration = '(Iteration.Name contains S01)'

def getStatisticsText(responseItemtype) :
    commitmentCount = 0
    completedPoints = 0
    commitmentPoints = 0
    completedCount = 0
    for item in responseItemtype:
        try:
            if item.ScheduleState in accepted:
                completedPoints+=item.PlanEstimate
                completedCount+=1
            commitmentCount+=1
            commitmentPoints+=item.PlanEstimate
        except:
            pass
    text = (str(commitmentCount) + '/' + str(int(commitmentPoints)) + ' ' + str(completedCount) + '/' + str(int(completedPoints)))
    return text

space=41

def logFileAndPrint(text):
    with open('teamStatistics.txt', 'a+') as the_file:
        the_file.write(text)
        print(text)

def getAllTeamStat():
    for projectData in projects :
        project = projectData[0]
        usText = ' '
        defectText = ' '
        rally = Rally('rally1.rallydev.com', configuration.user, configuration.password, workspace=configuration.workspace,
               project=project)
        usResponse = rally.get('UserStory', query=iteration)
        defectResponse = rally.get('Defect', query=iteration)
        usText = getStatisticsText(usResponse)
        defectText = getStatisticsText(defectResponse)

        cycleTime = ' '
        cycleTime = scrapping.getCycleTime(projectData[1])

        text = project.ljust(space,' ') + usText.center(space,' ') + defectText.center(space,' ') + cycleTime.center(space, ' ')
        logFileAndPrint(text)
        # print(cycleTime)
    return text

today = datetime.now()
logFileAndPrint(today.strftime('%d.%m.%Y %H:%M'))
logFileAndPrint(''.ljust(space, ' ') + 'US'.center(space, ' ') + 'Defect'.center(space, ' '))
logFileAndPrint('Team'.ljust(space, ' ') + '  Comitted / Delivered'.center(space, ' ') + '  Comitted / Delivered'.center(space, ' ') + 'Cycle Time'.center(space, ' '))

getAllTeamStat()
scrapping.driver.quit()
