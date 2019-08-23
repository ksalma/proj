from jenkinsapi import jenkins
from jenkinsapi.jenkins import Jenkins

jnk = Jenkins('http://localhost:8080', username='kacem', password='salma11')
server = jenkins.Jenkins('http://localhost:8080', username='kacem', password='salma11')

job_name='first'
server.build_job(job_name,params=None)
