import json
import sys


def get_env_arg_cmd():
    args = sys.argv[1:]
    try:
        if(args[0] == "-env"):
            return args[1]
    except:
        return None


def get_config():

    env = get_env_arg_cmd()

    with open('config.json') as config_file:
        env_vars = json.load(config_file)
        
        if(env == None):
            env = env_vars["env"]
        if(env in env_vars["envs"].keys()):
            return env_vars["envs"][env]
        else:
            raise Exception(
                f"No existe un tag de configuracion con el nombre {env} en config.json"
            )

if __name__ == "__main__":
    print(get_config())
