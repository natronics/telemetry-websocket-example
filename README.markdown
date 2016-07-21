PSAS Telemetry Websocket
========================

![Language: Python 3.4](https://img.shields.io/badge/language-python3-green.svg)
[![Build Status](https://travis-ci.org/natronics/telemetry-websocket-example.svg?branch=master)](https://travis-ci.org/natronics/telemetry-websocket-example)

A test PSAS telemetry websocket deployed to heroku.

Live instance: `wss://psas-telemetry-demo.herokuapp.com/` (websocket connection only).


## Develop

The best way to deal with dependencies in python is with [virtualenv][virtualenv]. If you've never used it before, you can read more about how it works here: <https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/>

Once you have `python3`, `pip`, and `virtualenvwrapper` installed, you can build this project.

To install everything you need for this project, create a new environment (you only need to do this once):

    $ mkvirtualenv -p `which python3` telemetry

Now you can install all the requirements:

    $ pip install -r requirements.txt

When you're done working you can close the virtualenv like this

    $ deactivate

And when you want to work on it again do this:

    $ workon telemetry


## Running

Assuming you have the correct libraries installed in your virtualenv, the run a server locally like this:

    $ honcho start

This will run the commands in the `Procfile`, starting a local webserver on port 5000. You can now test the code by making a websocket connection to

`ws://localhost:5000`


[virtualenv]: https://virtualenv.pypa.io/en/stable/
