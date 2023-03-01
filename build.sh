#!/bin/bash
DIR="$HOME/.bashrc"
DIR2="$HOME/.zshrc"
driver_path="export PATH=$PWD:\$PATH"

pip install -r requirements.txt
if test -f "$DIR"; then
  echo "bash shell detected"
  if grep -q "$driver_path" $DIR; then
    echo "PATH is already set up"
    else echo "$driver_path"  >> $DIR
    source $DIR
  fi
else
if test -f "$DIR2"; then
  echo "$DIR2 exists"
    if grep -q "$driver_path" $DIR2; then
        echo "PATH is already set up"
        else echo "$driver_path"  >> $DIR2
        source $DIR2
    fi
fi
fi

echo "building complete"
