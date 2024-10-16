﻿# Gas Utility Customer Service Application

## Project Description
A gas utility company is experiencing a high volume of customer service requests, leading to long wait times and poor service. This Django application aims to improve customer service by allowing customers to submit service requests online, track their status, and view their account information. It also provides customer support representatives with a tool to manage requests and support customers effectively.

### Key Features:
- **Service Requests**: Customers can submit service requests online by selecting the type of request, providing details, and attaching files.
- **Request Tracking**: Customers can track the status of their service requests, including the submission date, time, and resolution time.
- **Customer Support Management**: Support representatives can manage customer requests, improving response times and service quality.

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Virtualenv package

### Setup and Installation

1. **Create a Virtual Environment**:
   Create a virtual environment named `env` in the project directory:
   ```bash
   python -m venv env
2. ### Activate the Virtual Environment:
   - On **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```
3. **Install Django**:  
   After activating the virtual environment, install Django:
   ```bash
   pip install django

4. ** Navigate into the `gas_utility` directory**:

   ```bash
   cd gas_utility

5. **Make Migrations**:  
   Create new migrations based on the changes in your models:
   ```bash
   python manage.py makemigrations

6. **Migrate the Database**:
   ```bash
   python manage.py migrate
7. **Run the Application**:
   ```bash
   python manage.py runserver
