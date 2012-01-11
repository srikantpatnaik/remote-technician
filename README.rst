Introduction
============
This program enables the IT-technician to program/debug/monitor the embedded device located at remote location.

Where it can be used
--------------------
- Think of a situation where your product(embedded device connected to client's machine) is located at a far remote location and your client needs a quick updation to his firmware. There are two possible ways to resolve this, either client can bring/send the product back to you or you have to visit the location.

  But there is a *third* possibility too, you can debug/program and simultaneously view the product using a webcam at the client side using this web app.

- It can be used to update firmwares of multiple devices in one go, provided that the devices are registered and have same public key.

- Can be used to troubleshoot software issues of cellphones/tablets.
 
- More crazy implementation could be adding a robotic arm at client side to do the hardware debugging too.

- And lot more.


How it Works
------------
- Client login to his account and fill a form(details paths,ports,packages etc) on web interface(a webapp running at server) stating his problem and availability. 

- Client will be asked to download & execute *client.py* (this file will scan first all the dependencies such as Motion,python modules etc)file during the technician's visit to his problem.

- Technician will be notified and he will attend client's problem during the time slot.

- Technician will not have any access to client's data what so ever.


Pre-Requisite
-------------
- LAMP server (here 'P' is Python/Django) 

- Arduino tool chain on server (in place arduino we can use any embedded device)

- Python support on client's machine

- Motion(ffserver) package on clinet's machine (for webcam streaming)


Installation
------------
Coming soon.


License
-------
GNU GPLV3



