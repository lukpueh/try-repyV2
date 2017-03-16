# Try RepyV2!

Try Repy was implemented as a web-based software development and execution environment for Repy in the course of a bachelor seminar at the research group of Future Communication, University of Vienna, 2011.

This repository contains a port of Try Repy to run on RepyV2 powered [Seattle](https://github.com/SeattleTestbed/docs) and [Sensibility](https://github.com/SensibilityTestbed/instructions) Testbed nodes.


## Getting Started
```shell
git clone https://github.com/lukpueh/try-repyV2
```

### Deploy locally
Make sure to have a local Seattle/Sensibility installation. If you don't have one, you can obtain it from [Sensibility Custom Installer Builder](https://sensibilityclearinghouse.poly.edu/custominstallerbuilder/). Then, build and run `Try RepyV2!` using the following commands:

```shell
# In try-repyV2
./tr_build.sh
./tr_run.sh </path/to/local/seattle/seattle_repy> <connport listed in restrictions.tryrepy>

# You should see something like:
Webinterface available on:
http://<your local IP>:<the port you specified above>
```

### Deploy remotely (using `seash`)
Make sure to have downloaded and unzipped [`seash`, the experiment manager](https://sensibilityclearinghouse.poly.edu/demokit/sensibility-testbed-demokit.zip) and placed your [experimenter keys](https://github.com/SensibilityTestbed/instructions/blob/master/Setup.md) inside. You will need it to build `Try RepyV2!` and to deploy it on a remote vessel.

```shell
# In try-repyV2
./tr_build.sh <path/to/sensibility-testbed-demokit>
```
Follow the [seash instructions](https://github.com/SensibilityTestbed/instructions/blob/master/seash_intro.md) to start the seash console, load your cryptographic keys, find available vessels and set an active target. Once you've done all of that, you just have to upload the `Try RepyV2!` files and start the web controller using the following `seash` commands:

```shell
# In the seash console
user@%all !> uploaddir <path/to/try-repyV2/build>
user@%all !> start dylink.r2py tr_webcontroller.r2py <connport as shown by the seash command `show resources`>
user@%all !> show log

# You should see something like:
Log from '<remote node IP>:1224:v1':
========================================
Running program: dylink.r2py
Arguments: ['tr_webcontroller.r2py', '<the port specified above>']
========================================
Webinterface available on:
http://<remote note IP>:<the port specified above>
```

## Links
- [Try Repy! (old repository)](https://github.com/SeattleTestbed/attic/tree/master/trunk/repy/apps/tryrepy)
- [Try Repy! (Bachelor's thesis)](https://seattle.poly.edu/static/try_repy_thesis.pdf)