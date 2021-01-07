from pyral import Rally
import configuration
import scrapping
from datetime import datetime

accepted = ['Accepted', 'Completed', 'Released-to-Production']
iteration = '(Iteration.Name contains %s)' % configuration.iteration

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
    for projectData in configuration.projects :
        project = projectData[0]
        rally = Rally('rally1.rallydev.com', configuration.user, configuration.password, workspace=configuration.workspace,
               project=project)
        usResponse = rally.get('UserStory', query=iteration)
        defectResponse = rally.get('Defect', query=iteration)
        usText = getStatisticsText(usResponse)
        defectText = getStatisticsText(defectResponse)
        cycleTime = scrapping.getCycleTime(projectData[1])

        text = project.ljust(space,' ') + usText.center(space,' ') + defectText.center(space,' ') + cycleTime.center(space, ' ')
        logFileAndPrint(text)
    return text

today=datetime.now()
logFileAndPrint(today.strftime('%d.%m.%Y %H:%M'))
logFileAndPrint(''.ljust(space, ' ') + 'US'.center(space, ' ') + 'Defect'.center(space, ' '))
logFileAndPrint('Team'.ljust(space, ' ') + '  Comitted / Delivered'.center(space, ' ') + '  Comitted / Delivered'.center(space, ' ') + 'Cycle Time'.center(space, ' '))

getAllTeamStat()
scrapping.driver.quit()