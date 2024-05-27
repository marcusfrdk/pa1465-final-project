# PA1465 - Final Project

This is our _(group 11)_ final project for the course PA1465 at [BTH](https://bth.se).

## Assignment

Read more about the assignment [here](./ASSIGNMENT.md).

## Requirements

- [Docker](https://docs.docker.com/engine/install/)
- [Python >= 3.11.1](https://www.python.org/)

## Installation

In order to set up the project and keep a consistent environment across different operating systems and developer environments, follow the steps below:

### 1. Install requirements

Make sure you have installed the [requirements](./README.md#requirements).

### 2. Set up the virtual environment

In order to get consistent executions and results, a virtual environment must be used. You can set up a virtual environment with the following command.

#### Linux/MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```ps
python -m venv venv
venv\bin\Activate.ps1
```

_Note: To leave the virtual environment, run the command `deactivate`_

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run

### All tests

```bash
python run.py
```

### Only test different versions

```bash
python run.py --versions
```

### Only test different operating systems

```bash
python run.py --operating-systems
```

_Note: You can use any combination of flags_

