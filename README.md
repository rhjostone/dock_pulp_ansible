# Ansible Collection - rhjostone.dock_pulp_ansible

Ansible module for managing dock-pulp repos.

## Installation

```bash
$ pip install ansible
$ ansible-galaxy collection install git@github.com:rhjostone/dock_pulp_ansible.git
```

## Examples:

```yaml
- name: rhacm2/acm-grafana-rhel8
  description: Grafana
  product_line: rhacm2
  image_type: layered
  base_rhel_version: rhel8
  release_categories: ga
  download: true
```
