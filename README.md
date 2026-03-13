# perlmutter-spack-config
spack setup for perlmutter

This setup uses the perlmutter managed install of spack. See
https://docs.nersc.gov/development/build-tools/spack/ for more info.

## setup and install packages

```
module load spack
spack env create -d scorecSpackEnv
# copy the yaml and package repo from this repo to the env
cp -r scorecSpackRepo spack.yaml $_
spack env activate scorecSpackEnv
# edit the hardcoded paths in the yaml file
spack concretize
spack install
```

## install more packages

```
module load spack
spack env activate # /path/to/scorecSpackEnv 
spack add # or edit /path/to/scorecSpackEnv/spack.yaml
spack concretize
spack install
```

## give users access to packages

```
module use /global/cfs/cdirs/m499/cws/scorecSpackEnv/spack110/lmod/linux-sles15-x86_64/Core/
module load gcc/12.3.0-jn3n7je cray-mpich/8.1.30-akhkxty
module load pumi/develop-simmodsuite-2025.0-250108dev-int64-shared-mdsIdLong-osixgus
which render
```
