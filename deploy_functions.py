import sys
import subprocess
import json

def deploy_function(config):
    function_dir = config['function_dir']
    entry_point = config['entry_point']
    trigger_type = config['trigger_type']
    source_path = f'./functions/{function_dir}'

    command = [
        'gcloud', 'functions', 'deploy', function_dir,
        '--runtime', 'nodejs16',
        '--entry-point', entry_point,
        '--source', source_path,
        '--region', 'us-east1',
        '--project', 'new-project-422101',
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