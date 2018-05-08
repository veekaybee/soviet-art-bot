#!/usr/bin/env bash


FILE=".env"

if [[ $TRAVIS_BRANCH == 'dev' ]]; then
cat <<EOM >$FILE
aws ssm get-parameters-by-path --path "/Dev" |jq -r '.Parameters[]|"\(.Name)=\(.Value)"'|sed -e 's|/Dev/||g'
EOM
    echo "=========== $TRAVIS_BRANCH ENV ==========="
    cat $FILE
elif [[ $TRAVIS_BRANCH == 'master' ]]; then
cat <<EOM >$FILE
aws ssm get-parameters-by-path --path "/Prod" |jq -r '.Parameters[]|"\(.Name)=\(.Value)"'|sed -e 's|/Prod/||g'
EOM
    echo "=========== $TRAVIS_BRANCH ENV ==========="
    cat $FILE
else
    exit 0
fi