---
# ThreatMingle

ThreatMingle is a comprehensive cybersecurity platform designed to provide real-time threat insights, personalized risk assessments, community forums, and interactive learning modules.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Assessment](#assessment)
  - [Hub](#hub)
  - [Learn](#learn)
  - [Home](#home)
- [Contributing](#contributing)

## Overview

ThreatMingle is divided into several components, each serving a distinct purpose:

- **Assessment**: Personalized risk assessments and threat queries for URLs, files and IP addresses.
- **Hub**: Real-time communication/chat and community forums.
- **Learn**: Interactive learning modules on various cybersecurity topics.
- **Home**: Landing page and core application settings.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/ThreatMingle.git
cd ThreatMingle
```

2. Install dependencies:
Create a virtual environment for the project

```bash
python3 -m venv venv
pip install -r requirements.txt
```

- Database setup and environment variables required:
The project uses MariaDB for the Database, which you can setup or use
MySQL.

create a database named `threatmingle` in your Database console,
```SQL
CREATE DATABASE IF NOT EXISTS threatmingle;
```

or directly from the terminal:
```bash
echo "CREATE DATABASE IF NOT EXISTS threatmingle" | mysql -uroot -p{your_password}
```


- Get a VirusTotal API key for free: [Sign up for a free API Key](https://www.virustotal.com/gui/join-us)

- Export your variables or use a dotenv file to store them securely
```bash
export VIRUSTOTAL_API_KEY={your_key} DB_USER={your_db_username}
DB_PWD={your_db_password} DB_NAME=threatmingle DB_HOST=localhost DB_PORT=3306
```


3. Run migrations:

```bash
python3 manage.py migrate
```

4. Run server
```bash
python3 manage.py runserver
```


## Usage

### Home
You can access the application served on your localhost address, usually `127.0.0.1:8000`

The Home app manages the landing page and core settings of the application.

- Visit the home page at `/`.

On this interface, the project presents a simple interface, with a chart representation of popular threat categories, ranked by rate of attacks.

The page also contains links to various other aspects of the projects:

### Assessment

The Assessment app handles personalized risk assessments and threat queries.

- Navigate to `/assessment/` for risk assessments.

The assessment page offers a form to collect information on the type of scan you want.


### Hub

The Hub app facilitates real-time communication and community forums.

The `hub` platform uses websockets to facilitate real-time chat functionality.

- Visit `/hub/` for the main hub.
- Create or join predefined rooms from this interface.

### Learn

The Learn app contains interactive learning modules.

- Explore learning modules at `/learn/`.

## Contributing
Contributions to ThreatMingle are not just welcome; they are celebrated!
If you're passionate about cybersecurity and want to contribute to a
project with a purpose, feel free to open an issue or submit a pull
request. Your ideas, expertise, and collaboration are integral to the
growth of ThreatMingle.
