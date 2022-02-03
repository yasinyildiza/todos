#!/usr/bin/env bash

PACKAGE_NAME=todos

pip3 uninstall -y $PACKAGE_NAME

pip3 install -e .

uvicorn todos:app --reload
