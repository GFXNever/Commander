#!/bin/sh

python3 setup.py clean
python3 setup.py bdist_wheel --universal

python2 -m pip install `ls -t dist/*.whl | head -1` --force
python3 -m pip install `ls -t dist/*.whl | head -1` --force