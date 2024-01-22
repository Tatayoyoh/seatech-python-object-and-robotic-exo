#!/bin/bash

# Avoir la complétion VS Code
grep -q WEBOTS_HOME ~/.bashrc
if [ "$?" != "0" ] ; then
    echo 'export WEBOTS_HOME=/usr/local/webots' >> ~/.bashrc
    echo 'export WEBOTS_CONTROLLER=${WEBOTS_HOME}/lib/controller/' >> ~/.bashrc
    echo 'export LD_LIBRARY_PATH=${WEBOTS_CONTROLLER}' >> ~/.bashrc
    echo 'export PYTHONPATH=${WEBOTS_CONTROLLER}/python' >> ~/.bashrc
    source ~/.bashrc
else
    echo 'Webots variables are already setup'
fi

echo 'DONE !'