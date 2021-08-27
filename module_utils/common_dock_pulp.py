import dockpulp
import os.path
import json

homedir = os.path.expanduser('~')
default_pulp_dir = os.path.join(homedir, '.pulp')
config_dir = '/etc'


def import_dock_pulp_config(name):
    config_file = os.path.join(config_dir, '%s.json' % name)
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except:
        raise Exception('Failed to import %s' % config_file)


DOCK_PULP_DISTRIBUTIONS = import_dock_pulp_config('dockpulpdistributions')


class DockPulpClient(object):
    def __init__(self, env='prod', cert_dir=default_pulp_dir):
        self.client = dockpulp.Pulp(env=env)

        try:
            cert = os.path.join(cert_dir, 'pulp-%s.cer' % env)
            key = os.path.join(cert_dir, 'pulp-%s.key' % env)
            self.client.set_certs(cert, key)
        except:
            raise Exception('Failed to set up client')
