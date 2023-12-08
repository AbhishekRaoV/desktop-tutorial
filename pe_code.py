import jenkins
import time
import os

# Jenkins Authentication URL
JENKINS_URL = os.environ['JENKINS_URL']
JENKINS_USERNAME = os.environ['JENKINS_USERNAME']
JENKINS_PASSWORD = os.environ['JENKINS_PASSWORD']


class DevOpsJenkins:
    def __init__(self):
        self.jenkins_server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
        self.user = self.jenkins_server.get_whoami()
        version = self.jenkins_server.get_version()
        #print ("Jenkins Version: {}".format(version))
        #print ("Jenkins User: {}".format(self.user['id']))

    def build_job(self, name, parameters=None, token=None):
        next_build_number = self.jenkins_server.get_job_info(name)['nextBuildNumber']
        self.jenkins_server.build_job(name, parameters=parameters, token=token)
        print ("Jenkins Job Name -- {} \nTriggered by User: {}".format(name,self.user['id']))
        time.sleep(10)
        build_info = self.jenkins_server.get_build_info(name, next_build_number)
        return build_info

    def delete_build(self, name, number):
        self.jenkins_server.delete_build(name,number)
        return 'Deleted the build'

"""
if __name__ == "__main__":
    NAME_OF_JOB = os.environ['JENKINS_JOB_NAME_ANSIBLE']
    #TOKEN_NAME = os.environ['JENKINS_API_TOKEN']
    TOKEN_NAME = 'oXzu/wHvqZUBKwytEqxyxd3K42AhM/JJOF2/jtYx'
    # Example Parameter

    #PARAMETERS = {'Name': 'marvel-infra-test','storage_size':'10','instance_type':'t2.medium','instance_count':'1'}

    PARAMETERS = {'Instance_IP':'10.0.1.218','Tool':'MySQL'}
    jenkins_obj = DevOpsJenkins()
    output = jenkins_obj.build_job(NAME_OF_JOB, PARAMETERS, TOKEN_NAME)
    #delete_output = jenkins_obj.delete_build(NAME_OF_JOB, 43)
    #(delete_output)
    print ("Jenkins Build URL: {}".format(output['url']))
"""
