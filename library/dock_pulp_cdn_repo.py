from ansible.module_utils import common_dock_pulp

def run_module():
    module_args = dict(
        name=dict(required=True),
        description=dict(required=True),
        product_line=dict(required=True),
        image_type=dict(required=True),
        base_rhel_version=dict(required=True),
        release_categories=dict(required=True),
        download=dict(type='bool', required=True)
    )

    client = common_dock_pulp.DockPulpClient()

    
def main():
    run_module()


if __name__ == '__main__':
    main()
