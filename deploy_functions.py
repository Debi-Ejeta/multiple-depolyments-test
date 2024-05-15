import sys
import subprocess
import json

def deploy_function(config):
    project_id = config['project_id']
    function_dir = config['function_dir']
    entry_point = config['entry_point']
    trigger_type = config['trigger_type']
    source_path = f'./{function_dir}'

    command = [
        'gcloud', 'functions', 'deploy', function_dir,
        '--runtime', 'nodejs16',  # Ensure runtime version matches your function's requirements
        '--entry-point', entry_point,
        '--source', source_path,
        '--region', 'us-east1',  # Adjust the region as necessary
        '--project', project_id,
        '--allow-unauthenticated'
    ]

    if trigger_type == 'http':
        command.extend(['--trigger-http'])
    else:
        command.extend([
            '--trigger-event', config['trigger_event'],
            '--trigger-resource', config['trigger_resource']
        ])

    subprocess.run(command, check=True)

if __name__ == "__main__":
    config = json.loads(sys.argv[1])
    deploy_function(config)
