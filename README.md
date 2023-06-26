# data_analyzer


To download and run this code, the following software is required:
* Git
* pip
* python3

## Step 1: Installing Git
#### Ubuntu distribution

To install Git on an Ubuntu distribution, you can follow these steps:

1. Open a terminal on your Ubuntu distribution. Update the package lists for upgrades and new package installations by running the following command:
```
sudo apt-get update
```
2. Install Git by running the following command
```
sudo apt-get install git
```

#### macOS system
To install Git on macOS system, you can follow these steps:

1. Install Homebrew (a package manager for macOS) if you haven't already. Open Terminal and execute the following command:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Once Homebrew is installed, you can use it to install Git by running the following command in Terminal:
 
```
brew install git
```

## Step 2: Installing pip and python
#### Ubuntu distribution

To install pip on an Ubuntu distribution, you can follow these steps:

1. Install pip by running the following command:
```
sudo apt-get install python3-pip
```
2. After the installation is complete, you can verify the installation by checking the pip version with the following command:
```
pip3 --version
```
#### macOS system

To install python3.9 and pip on macOS, you can follow these steps:

Open the Terminal application on your macOS system and run the following command.
```
brew install python@3.9
```
This command will install Python 3.9 along with pip.

2. After the installation is complete, you should have pip installed on your macOS system. You can verify the installation by running the following command:
```
pip --version
```
This command will display the version of pip installed on your system.

## Step 3: cloning the repository in your computer

To clone the repository onto your computer, you can follow these steps:

1. Open a terminal or command prompt on your computer.

2. Navigate to the directory where you want to clone the repository. You can use the cd command followed by the directory path to change to the desired directory. In the terminal or command prompt, run the following command:
```
git clone https://github.com/ReyGuadarrama/data_analyzer
```

3. Once the cloning process is complete, you will have a local copy of the repository in the specified directory on your computer.

## Step 4: Creating a virtual enviroment

To create a virtual environment, you can follow these steps:

1. Open a terminal or command prompt on your computer.

2. To create a virtual environment, navigate to the directory of the cloned repository and execute the following command:
```
python3 -m venv env
```
This command creates a new directory named "env" (you can choose a different name if you prefer) that will contain the virtual environment.

3. Activate the virtual environment by running the following command:
```
source venv/bin/activate
```
Once activated, your command prompt or terminal will display the name of the virtual environment.
You have successfully created and activated the virtual environment. Now you can install Python packages and run the project within this isolated environment. Remember to activate the virtual environment whenever you want to work within it and deactivate it when you're finished. This helps keep your project dependencies isolated and avoids conflicts with other projects or system-wide installations.


## Step 5: Installing requirements

To install requirements to run this code, follow these steps:

1.  Open a terminal or command prompt on your computer, activate your virtual enviroment and run the following command:
```
pip install -r requirements.txt
```


