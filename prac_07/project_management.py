"""
time estimate: 50min
actual time: 57min
"""

import os
import datetime
from project import Project


class ProjectManagement:
    def __init__(self):
        """Initialize the Project Management system."""
        self.projects = []
        self.filename = "projects.txt"  # 默认的文件名

    def load_projects(self, filename=None):
        """Load projects from the specified file."""
        if filename is None:
            filename = self.filename

        if not os.path.exists(filename):
            print(f"Error: {filename} does not exist.")
            return

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()[1:]  # Skip header line

            for line in lines:
                name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
                project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
                self.projects.append(project)

        print(f"Loaded {len(self.projects)} projects from {filename}")

    def save_projects(self, filename=None):
        """Save the projects to the specified file."""
        if filename is None:
            filename = self.filename

        with open(filename, 'w', encoding='utf-8') as file:
            # Write the header
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in self.projects:
                file.write(
                    f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate:.2f}\t{project.completion_percentage}\n")

        print(f"Projects saved to {filename}")

    def display_projects(self):
        """Display all projects, categorized by completion status."""
        incomplete = [p for p in self.projects if p.is_incomplete()]
        completed = [p for p in self.projects if p.is_completed()]

        # Sort by priority
        incomplete.sort(key=lambda x: x.priority)
        completed.sort(key=lambda x: x.priority)

        print("Incomplete projects:")
        for project in incomplete:
            print(f"  {project}")

        print("\nCompleted projects:")
        for project in completed:
            print(f"  {project}")

    def filter_projects_by_date(self, date_string):
        """Filter and display projects that start after a given date."""
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = sorted([p for p in self.projects if p.start_date > filter_date], key=lambda x: x.start_date)

        for project in filtered_projects:
            print(f"  {project}")

    def add_new_project(self):
        """Prompt the user to add a new project."""
        print("Let's add a new project")
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yy): ")
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion_percentage = int(input("Percent complete: "))

        new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        self.projects.append(new_project)
        print(f"Project '{name}' added.")

    def update_project(self):
        """Allow the user to update a project."""
        print("Update project:")
        for idx, project in enumerate(self.projects):
            print(f"{idx} {project}")

        project_choice = int(input("Project choice: "))
        selected_project = self.projects[project_choice]

        new_percentage = input(f"New Percentage ({selected_project.completion_percentage}): ")
        if new_percentage:
            selected_project.completion_percentage = int(new_percentage)

        new_priority = input(f"New Priority ({selected_project.priority}): ")
        if new_priority:
            selected_project.priority = int(new_priority)

    def main_menu(self):
        """Display the main menu and execute user commands."""
        while True:
            print("\n- (L)oad projects")
            print("- (S)ave projects")
            print("- (D)isplay projects")
            print("- (F)ilter projects by date")
            print("- (A)dd new project")
            print("- (U)pdate project")
            print("- (Q)uit")
            choice = input(">>> ").lower()

            if choice == "l":
                filename = input("Enter filename to load: ")
                self.load_projects(filename)
            elif choice == "s":
                filename = input("Enter filename to save: ")
                self.save_projects(filename)
            elif choice == "d":
                self.display_projects()
            elif choice == "f":
                date_string = input("Show projects that start after date (dd/mm/yy): ")
                self.filter_projects_by_date(date_string)
            elif choice == "a":
                self.add_new_project()
            elif choice == "u":
                self.update_project()
            elif choice == "q":
                save_choice = input("Would you like to save to projects.txt? (y/n): ")
                if save_choice.lower() == "y":
                    self.save_projects()
                print("Thank you for using the project management software.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    project_management = ProjectManagement()
    project_management.main_menu()
