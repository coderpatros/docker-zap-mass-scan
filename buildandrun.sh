#!/usr/bin/env bash
docker build -t zap-mass-scan .
docker run --volume `pwd`/wiki:/zap/wiki --interactive zap-mass-scan