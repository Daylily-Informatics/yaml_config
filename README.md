# yaml_config


## Pre-requisites
* For MAC/Linux systems (though should be straightforward to port to Windows).
* [conda/mamba](https://anaconda.org/conda-forge/mamba)

## Create Environment

Using conda/mamba.

```bash
mamba env create -n DYAML -f DYAML.yaml
```


## Usage

* Be sure to have a `project` `~/.config/` subdirectory which contains a `project.yaml` file.

```bash
project='myproj';
mkdir -p ~/.config/$project
touch ~/.config/$project/$project.yaml
```

* Use in an ipython shell
```python

import yaml_config.config_manager as YCM
yconfig = YCM.ProjectConfigManager('jem')
yconfig.get_config()

# Out: {'access_key': 'aaa', 'secret_access_key': 'bbbb', 'username': 'jmmmem'}
```

