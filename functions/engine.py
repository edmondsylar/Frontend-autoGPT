# Main functions management.
import os
import uuid
from rich.console import Console

console = Console()

class Engine:
    def __init__(self, workspace):
        # this is a local directory path
        self.workspace = workspace # local parent directory for the worspace
        # print(self.workspace)

        # default project 
        self.default_project = {
            "id": uuid.uuid4(),
            "project_name": "Default Project",
            "project_size": 0,
            "location": self.workspace
        }


    def build_project(self, project):
        project = {
            "id": uuid.uuid4(),
            "project_name": os.path.basename(project),
            "project_size": 0,
            "location": project
        }
        return project

    def defaults(self):
        defaults = []

        # add default ptoject 
        defaults.append(self.default_project)
        
        return defaults
    

    def projects(self):
        projects = [] # projects final list
        _temp_projects = [] # temporary projects list

        # check through the workspace directory for all folders there and add them to projects.
        for root, dir, files in os.walk(self.workspace):
            for file in files:
                project_folder = os.path.join(root)
                if project_folder in _temp_projects:
                    pass
                else:
                    _temp_projects.append(project_folder)
                    _project = self.build_project(project_folder)

                    # now let's add this to the projects list as the final project.
                    projects.append(_project)

        projects.append(self.default_project)
        return projects

    def _project_data(self, project_location):

        # join the workspace and project location
        project_location = os.path.join(self.workspace, project_location)

        data = []
        # check through the workspace directory for all folders there and add them to projects.
        for root, dir, files in os.walk(project_location):
            for file in files:
                data.append(os.path.join(root, file))

        return data
    


player = Engine("D:\\ptyped\\Stable\\Auto-GPT\\autogpt\\auto_gpt_workspace")
console.log(player.projects())