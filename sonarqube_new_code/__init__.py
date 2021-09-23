import argparse
import requests


def sonarqube_new_code():
    parser = argparse.ArgumentParser(
        description='TODO: Add a description'
    )

    parser.add_argument('-t', action="store", dest="token", required=True)
    parser.add_argument('-u', action="store", dest="url", required=True)
    parser.add_argument('-p', action="store", dest="project", required=True)
    parser.add_argument('-v', action="store", dest="version", default="BASELINE")
    parser.add_argument('-b', action="store", dest="branch", default="master")

    parameters = parser.parse_args()

    r = requests.get("{}/api/project_analyses/search?project={}&category=VERSION&ps=500".format(parameters.url, parameters.project), auth=(parameters.token, ''))

    last_analyses = r.json()['analyses']

    last_version_analyses = list(filter(lambda a: (a['projectVersion'] == parameters.version), last_analyses))

    last_version_analysis_key = last_version_analyses[0]['key']

    requests.post("{}/api/new_code_periods/set?project={}&branch={}&type=SPECIFIC_ANALYSIS&value={}".format(parameters.url, parameters.project, parameters.branch, last_version_analysis_key), auth=(parameters.token, ''))


if __name__ == '__main__':
    sonarqube_new_code()
