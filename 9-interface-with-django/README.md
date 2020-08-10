# Interface with Django

## Setup a Development Instance of the Backend

The backend for this project was written using the Django web framework using Django Channels and Django REST Framework. It consists of a single database table that stores text recognized by Pepper.

This backend was intended to be setup using [Docker Compose](https://docs.docker.com/compose/gettingstarted/), so please make sure your computer has the required prerequisites.

The following are the steps to setting up the environmental instance:

1. Clone the repository onto your computer
2. In the `pepper_backend` directory, go to the `pepper_backend/settings.py` file and make sure the `ALLOWED_HOSTS` option is set accordingly; click [here](https://lifehacker.com/how-to-find-your-local-and-external-ip-address-5833108) to see how to find your local and external IP address
3. In the `pepper_choregraphe_project` directory, go to the "Django LAN" Python box and make sure any IP addresses are pointing to your local and external IP address
4. Once all is said and done, use Docker Compose to setup the environmental instance: `docker-compose up` (you can add the `-d` option at the end to run in "detached" mode, which runs the processes in the background)

**Note: The Django backend has been setup only for development... It is not suited for production (i.e., do not expose this webserver to the public nor use it to collect sensitive information).**
