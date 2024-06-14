import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
import subprocess
import sys

class DeveloperModeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Developer Mode")
        self.root.geometry("600x700")
        
        # Setup style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12))
        
        # Title Label
        self.label = ttk.Label(self.root, text="Developer Mode", font=('Helvetica', 16))
        self.label.pack(pady=10)
        
        # Button to show system info
        self.info_button = ttk.Button(self.root, text="Show System Info", command=self.show_system_info)
        self.info_button.pack(pady=5)
        
        # Button to create a directory
        self.create_dir_button = ttk.Button(self.root, text="Create Directory", command=self.create_directory)
        self.create_dir_button.pack(pady=5)

        # Button to enable registry developer mode
        self.reg_dev_mode_button = ttk.Button(self.root, text="Enable Developer Mode in Registry", command=self.on_button_click)
        self.reg_dev_mode_button.pack(pady=5)

        # ComboBox for important system developer options
        self.impsystemdevopt = ttk.Combobox(self.root, values=["Enable core developer tools", "Enable Linux subsystem"])
        self.impsystemdevopt.pack(pady=5)

        # Button to handle the developer options
        self.devopt_button = ttk.Button(self.root, text="Apply Developer Option", command=self.devopt_button_click)
        self.devopt_button.pack(pady=5)

        # Button to initialize Git repository
        self.git_init_button = ttk.Button(self.root, text="Initialize Git Repository", command=self.git_init)
        self.git_init_button.pack(pady=5)

        # Button to create Python virtual environment
        self.venv_button = ttk.Button(self.root, text="Create Python Virtual Environment", command=self.create_venv)
        self.venv_button.pack(pady=5)

        # Button to install VS Code
        self.vscode_button = ttk.Button(self.root, text="Install Visual Studio Code", command=self.install_vscode)
        self.vscode_button.pack(pady=5)

        # Button to install Docker
        self.docker_button = ttk.Button(self.root, text="Install Docker", command=self.install_docker)
        self.docker_button.pack(pady=5)

        # Button to install Node.js
        self.node_button = ttk.Button(self.root, text="Install Node.js", command=self.install_node)
        self.node_button.pack(pady=5)

        # Button to connect to development home
        self.dev_home_button = ttk.Button(self.root, text="Connect to Dev Home", command=self.connect_to_dev_home)
        self.dev_home_button.pack(pady=5)

        # Entry for custom commands
        self.command_entry = ttk.Entry(self.root, width=50)
        self.command_entry.pack(pady=5)

        # Button to execute custom command
        self.execute_button = ttk.Button(self.root, text="Execute Command", command=self.execute_command)
        self.execute_button.pack(pady=5)

        # Button to install packages
        self.package_install_button = ttk.Button(self.root, text="Install Package", command=self.install_package)
        self.package_install_button.pack(pady=5)

        # Button to uninstall packages
        self.package_uninstall_button = ttk.Button(self.root, text="Uninstall Package", command=self.uninstall_package)
        self.package_uninstall_button.pack(pady=5)

        # Button to create a conda environment
        self.create_env_button = ttk.Button(self.root, text="Create Environment", command=self.create_conda_env)
        self.create_env_button.pack(pady=5)

        # Button to activate a conda environment
        self.activate_env_button = ttk.Button(self.root, text="Activate Environment", command=self.activate_conda_env)
        self.activate_env_button.pack(pady=5)

    def show_system_info(self):
        # Displaying system information
        system_info = f"Platform: {os.name}\nCurrent Working Directory: {os.getcwd()}"
        messagebox.showinfo("System Info", system_info)
    
    def create_directory(self):
        # Creating a new directory with user input for the directory name
        dir_name = simpledialog.askstring("Input", "Enter the custom directory name:", parent=self.root)
        if dir_name:
            new_dir = os.path.join(os.getcwd(), dir_name)
            try:
                os.makedirs(new_dir, exist_ok=True)
                messagebox.showinfo("Directory Creation", f"Directory '{new_dir}' created successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create directory: {str(e)}")
        else:
            messagebox.showwarning("Input Error", "No directory name provided.")

    def on_button_click(self):
        # Enable developer mode in registry
        try:
            os.system('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1"')
            messagebox.showinfo("Registry Update", "Developer Mode enabled in registry successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to enable Developer Mode in registry: {str(e)}")
    
    def devopt_button_click(self):
        # Handle developer options from the ComboBox
        s_opt = self.impsystemdevopt.get()
        try:
            if s_opt == "Enable core developer tools":
                os.system("DISM /Online /Add-Capability /CapabilityName:Tools.DeveloperMode.Core~~~~0.0.1.0")
                messagebox.showinfo("Developer Option", "Core developer tools enabled successfully!")
            elif s_opt == "Enable Linux subsystem":
                os.system('DISM /Online /Enable-Feature /FeatureName:Microsoft-Windows-Subsystem-Linux')
                messagebox.showinfo("Developer Option", "Linux subsystem enabled successfully!")
            else:
                messagebox.showwarning("Developer Option", "Please select a valid developer option.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply developer option: {str(e)}")

    def git_init(self):
        # Initialize a Git repository
        try:
            os.system('git init')
            messagebox.showinfo("Git", "Initialized a new Git repository successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize Git repository: {str(e)}")

    def create_venv(self):
        # Create a Python virtual environment
        env_name = simpledialog.askstring("Input", "Enter the virtual environment name:", parent=self.root)
        if env_name:
            try:
                os.system(f'python -m venv {env_name}')
                messagebox.showinfo("Virtual Environment", f"Virtual environment '{env_name}' created successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create virtual environment: {str(e)}")
        else:
            messagebox.showwarning("Input Error", "No virtual environment name provided.")
    
    def install_vscode(self):
        # Install Visual Studio Code
        try:
            os.system('winget install -e --id Microsoft.VisualStudioCode')
            messagebox.showinfo("Visual Studio Code", "Visual Studio Code installed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install Visual Studio Code: {str(e)}")

    def install_docker(self):
        # Install Docker
        try:
            os.system('winget install -e --id Docker.DockerDesktop')
            messagebox.showinfo("Docker", "Docker installed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install Docker: {str(e)}")

    def install_node(self):
        # Install Node.js
        try:
            os.system('winget install -e --id OpenJS.NodeJS')
            messagebox.showinfo("Node.js", "Node.js installed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install Node.js: {str(e)}")

    def connect_to_dev_home(self):
        # Connect to development home directory
        dev_home = os.path.expanduser("~")  # Get user's home directory
        os.chdir(dev_home)
        messagebox.showinfo("Connect to Dev Home", f"Connected to development home directory: {dev_home}")

    def execute_command(self):
        # Execute a custom command
        command = self.command_entry.get()
        if command:
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
                messagebox.showinfo("Command Output", output)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Command failed: {e.output}")
        else:
            messagebox.showwarning("Input Error", "No command provided.")
    
    def install_package(self):
        # Install a package using pip
        package_name = simpledialog.askstring("Input", "Enter the package name to install:", parent=self.root)
        if package_name:
            try:
                output = subprocess.check_output(f'{sys.executable} -m pip install {package_name}', shell=True, stderr=subprocess.STDOUT, text=True)
                messagebox.showinfo("Package Installation", f"Package '{package_name}' installed successfully!\n{output}")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to install package: {e.output}")
        else:
            messagebox.showwarning("Input Error", "No package name provided.")
    
    def uninstall_package(self):
        # Uninstall a package using pip
        package_name = simpledialog.askstring("Input", "Enter the package name to uninstall:", parent=self.root)
        if package_name:
            try:
                output = subprocess.check_output(f'{sys.executable} -m pip uninstall -y {package_name}', shell=True, stderr=subprocess.STDOUT, text=True)
                messagebox.showinfo("Package Uninstallation", f"Package '{package_name}' uninstalled successfully!\n{output}")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to uninstall package: {e.output}")
        else:
            messagebox.showwarning("Input Error", "No package name provided.")

    def create_conda_env(self):
        # Create a conda environment
        env_name = simpledialog.askstring("Input", "Enter the conda environment name:", parent=self.root)
        if env_name:
            try:
                output = subprocess.check_output(f'conda create -n {env_name} -y', shell=True, stderr=subprocess.STDOUT, text=True)
                messagebox.showinfo("Conda Environment", f"Conda environment '{env_name}' created successfully!\n{output}")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to create conda environment: {e.output}")
        else:
            messagebox.showwarning("Input Error", "No conda environment name provided.")

    def activate_conda_env(self):
        # Activate a conda environment
        env_name = simpledialog.askstring("Input", "Enter the conda environment name to activate:", parent=self.root)
        if env_name:
            try:
                subprocess.check_call(f'conda activate {env_name}', shell=True)
                messagebox.showinfo("Conda Environment", f"Conda environment '{env_name}' activated successfully!")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to activate conda environment: {str(e)}")
        else:
            messagebox.showwarning("Input Error", "No conda environment name provided.")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = DeveloperModeApp(root)
    root.mainloop()
