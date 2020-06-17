import os
import pathlib
import json

'''
 - confirm each package is valid (main and config)
 - confirm each package has atleast one command
 - alter abilities.json

incorrect = \
{
    'Kara-Weather':
    [
        'missing main',
        'missing version',
        'different version'
    ]
}

'''


path = 'Core/Abilities/'

# confirm if changes were made
def quickCheck():
    incorrect = {}

    # get abilities
    abilities = os.listdir(path)

    for ability in abilities:
        # everything incorrect with the ability
        issues = []

        configPath = path + ability + '/config.json'

        # get ability files
        config = pathlib.Path(configPath)
        if config.is_file():
            # parse json
            with open(configPath, 'r') as file:
                configJSON = json.load(file)

                # read correct main file
                main = pathlib.Path(path + ability + '/' + configJSON['main'])
                # main doesn't exists
                if not main.is_file():
                    # issue encounter
                    issues.append('no main')

                    # log incorrect interaction
                    incorrect[ability] = issues
        else:
            # issue encounter
            issues.append('no config')

            # log incorrect interaction
            incorrect[ability] = issues
    return incorrect

def compile():
    changes = quickCheck()
    print(changes)