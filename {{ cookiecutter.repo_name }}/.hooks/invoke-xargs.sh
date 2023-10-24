#!/bin/bash

set -euxo pipefail

COMMAND="poetry run invoke --search-root src ${1}"
PATH_ARGUMENT="--path"

shift 1

for i in "$@"; do
    if [[ "${i}" == "--"* ]]; then
        COMMAND="${COMMAND} ${i}"
    else
        COMMAND="${COMMAND} ${PATH_ARGUMENT}=${i}"
    fi
done

${COMMAND}
