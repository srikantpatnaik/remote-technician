List of pending jobs
--------------------

- Need to write *client.py* to load binary/hex to Arduino device as soon as
  it receives the file from server. The file will be received and overwritten
  each time when user press the execute button on HTML form.
  So need to monitor constantly for any updation in file. 

- Possibly use Django to create web app. This app will have to login fields,
  viz. client login and technician login. Client will fill essentially a form
  stating his problem and availability.
  The technician will attend to the task in the time slot provided by the client.

- The client will be given a file *client.py* to execute on his local machine.
  This file should run during the entire session of debug for technician to 
  access client's hardware.

- The technician can ask client for webcam access to get live feed. The live feed
  images are sent to server by *server.py* . Those images are to be sent to the
  web app to make it appear live {2 fps} (need to figure out a way).
