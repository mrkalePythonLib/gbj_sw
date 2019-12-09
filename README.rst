**********************
Purpose of the package
**********************
The package ``gbj_sw`` contains a set of sub-packages each with one Python
module. All of them are aimed for supporting ordinary python console
applications and scripts.

- The module itself does not have any own modules. It servers just as
  a container for sub-packages.

- Sub-packages are utilized as libraries.

- Each sub-package is treated as a git sub-module, so that it is separated
  git repository. It allows versioning of sub-packages and their modules
  individually, but utilize them together in Python scripts.


Sub-packages and their modules
==============================
The sub-package name is composed of the prefix ``gbj_`` and name of involving
module by the scheme ``gbj_<module>``, e. g., ``gbj_utils``.

gbj_utils
---------
  Auxilliary utilities and functions mainly for interaction with operation
  system.

gbj_config
----------
  Processing configuration INI files.

gbj_mqtt
--------
  Processing MQTT messages by MQTT clients.

gbj_iot
-------
  Handling IoT devices and general parameters and functions for them.
