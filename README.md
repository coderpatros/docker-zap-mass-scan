# Zed Attack Proxy Mass Scan Docker Container

Shamelessly copied and tweaked from the mass baseline script in the
[zaproxy/community-scripts repo](https://github.com/zaproxy/community-scripts/tree/master/api/mass-baseline)

## Intended Use Case

I have over 200 Azure Web Apps I have to worry about. And I need visibility
across them all without the overhead of adding scans to each CD pipeline.

This container will generate a
[dashboard](https://github.com/zaproxy/community-scripts/wiki/Baseline-Summary)
similar to the mass baseline scripts it is based on.

If you want to add a scan to your CD pipeline I recommend my
[zap-scanner container](https://github.com/patros/docker-zap-scanner). It
will generate a JUnit format test result file for a single target.

## Usage

To use this you will need to mount a volume that contains a file
`targets.list`. The file needs to contain a list of target hostnames to scan
followed by a new line character. The scan will be performed over https.

Please note, the script requires each target hostname to be followed by a new
line. i.e. the last line should be empty.

The volume needs to be mounted to `/zap/wiki`. You can use the
`buildandrun.sh` script to try it out locally.

A summary markdown file will be generated as well as a history of scans for
each target host.
