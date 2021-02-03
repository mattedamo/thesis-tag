#!/bin/bash

rel=$(git branch -r --list '*features/*')
if [[ $rel != *"features"* ]]; then
#if [ "$rel" = "" ]; then
  echo "develop"
else
  echo $rel
  echo "pel"
  echo "dell'uovo"
fi
