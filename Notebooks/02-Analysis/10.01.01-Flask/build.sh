#!/bin/sh

docker build -t git.services.tdt/ui-college-of-business/bais-6040-0exp .
# docker push git.services.tdt/ui-college-of-business/bais-6040-0exp
docker build -t docker.pkg.github.com/thedarktrumpet/bais-6040-0exp-spr2021/flaskdemo .
docker push docker.pkg.github.com/thedarktrumpet/bais-6040-0exp-spr2021/flaskdemo
