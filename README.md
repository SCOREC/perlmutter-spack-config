# perlmutter-spack-config
spack setup for perlmutter


## install packages

```
module load spack
spack env create -d scorecSpackEnv
cp spack.yaml $_ # copy the yaml from this repo to the env
spack env activate scorecSpackEnv
# edit the hardcoded paths in the yaml file as needed
spack concretize
spack install
```

## use packages

```
module use /global/cfs/cdirs/m499/cws/scorecSpackEnv/spack110/lmod/linux-sles15-x86_64/Core/
module load gcc/12.3.0-jn3n7je cray-mpich/8.1.30-akhkxty
module load pumi/develop-simmodsuite-2025.0-250108dev-int64-shared-mdsIdLong-osixgus
which render
```
