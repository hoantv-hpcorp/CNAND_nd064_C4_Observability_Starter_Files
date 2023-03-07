#!/bin/sh

for i in {1..100000}
do
    curl 10.43.52.109:8000
    if [ $(($i % 10)) == 0 ]
    then
        curl 10.43.52.109:8000/notfound
    fi
    
    if [ $(($i % 100)) == 0 ]
    then
        curl 10.43.52.109:8000/simulate_system_error
    fi

    sleep 0.05
done
