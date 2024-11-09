# Please refrain from using this version and download the codeberg version! This version has terrible design, obfuscated code and not the best license
Codeberg version here: https://codeberg.org/hikeri/Ripify
Ripify💀 An add-on to the OrpheusDL library that adds a web interface | Ripify github mirror repo

## Overview

Ripify-GithubEdition is an add-on for the OrpheusDL library that provides a user-friendly web interface for managing and archiving music from various services. OrpheusDL is a powerful modular music archival tool written in Python, designed to facilitate the archiving process from multiple sources. With Ripify-GithubEdition, users can easily interact with OrpheusDL through a sleek web interface, making music archiving more accessible and efficient.

## Features

- **Web Interface**: A clean and intuitive web interface for managing your music archives.
- **Integration with OrpheusDL**: Seamlessly integrates with the OrpheusDL library to leverage its powerful archiving capabilities.
- **Multi-Service Support**: Archive music from various services with ease.
- **Modular Design**: Built on the modular architecture of OrpheusDL, allowing for easy updates and enhancements.
- **Protection from bots**: Simple protection against bots and downloads without using a website.

## Installation

To install Ripify-GithubEdition, follow these steps:

1. Ensure you have Python 3.6 or higher installed on your system.
2. Clone the repository:

   ```bash
   git clone https://github.com/hikeri/Ripify.git
   cd Ripify
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   rm requirements.txt
   ```

4. Ensure you have OrpheusDL installed, and move all the contents of the Rip-ify repository to the root folder of your OrpheusDL installation:

   ```bash
   mv Ripify/* /path/to/orpheusdl/
   ```

5. Go to the folder with orpheus and run the web interface:

   ```bash
   cd /path/to/orpheusdl/
   python webui.py
   ```

6. Open your web browser and navigate to `http://localhost:5000` to access the Ripify-GithubEdition interface.

7. If you want to use this not only on localhost, then use an https certificate. (Without it, the download will most likely not work.)

## Usage

Once the web interface is running, you can:

- Download music using a beautiful web interface
- Modify the source code according to the current license

## License

This project is licensed under the [Github Restrictive License v1.2](https://github.com/hikeri/Ripify/blob/main/LICENSE.md). 

Which means you cannot use this software for any purpose other than personal and non-commercial
