#!/bin/sh

export VIRTUAL_ENV="__VIRTUAL_ENV__"
export PATH="$VIRTUAL_ENV/__BIN_NAME__:$PATH"

if [ "x__VIRTUAL_PROMPT__" != x ] ; then
    VIRTUAL_ENV_PROMPT="__VIRTUAL_PROMPT__"
else
    VIRTUAL_ENV_PROMPT=$(basename "$VIRTUAL_ENV")
fi
export VIRTUAL_ENV_PROMPT

unset PYTHON_HOME
exec "${@:-$SHELL}"
