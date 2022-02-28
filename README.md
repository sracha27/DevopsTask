# DevopsTask: 

**Application:**
> Language used for this application is python.
> libriries used Flask, Scipy, Math, Numpy.

**HOW TO RUN APPLICATION:**
> To install application dependencies, 
> Need to redirect to DevopsTask/python-virtual-environments/dev/bin and run **source activate** to get the runtime dependencies on application server
> From the root folder run **python3 task.py** to start the application

**HOW TO PERFORM CRUD OPERATION RESTAPI:**
> To list all the students data "curl -X GET http://$APPLICATION_IP:$APPLICATION_PORT/students" on any terminal and from the browser "http://$APPLICATION_IP:$APPLICATION_PORT/students".

> To add students data " curl -i -X PUT -H 'Content-Type: application/json' -d '{"InputNumericalValue": "84.2", "InputUnitofMeasure": "Fahrenheit","TargetUnitofMeasure": "Rankine", "StudentResponse": "543.94"}' http://$APPLICATION_IP:$APPLICATION_PORT/students/student_id "

> To get the results of the student " curl -X GET http://$APPLICATION_IP:$APPLICATION_PORT/students/student_id "

**CICD-SETUP:**
> I have created the free-style jenkins job for deploying the application.

**Five tasks that I wolud like to perform for more productive solution: **

> Dockerize the application.

> Create a terraform template to provison the instance on the fly.

> Create the pipeline job for creation of infrastructure, continuous integration and continuous deployment.

> Deploying Jenkins on EKS.

> Update the code to provide the user input at runtime. 
