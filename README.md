# DNS Enumeration and Subdomain Scanning Tool

This tool helps you perform DNS enumeration for a given domain and discover valid subdomains from a list provided in a file named `subdomains.txt`.

![DNS Enumeration and Subdomain Scanning Tool](https://i.imgur.com/FmSAfeS.png)

## Features

- DNS record enumeration for multiple types, including A, AAAA, MX, NS, TXT, and others.
- Subdomain discovery using a list from a user-provided text file.
- ASCII art and colorful CLI output for an enhanced user experience.
- Enumeration progress animation.

## Prerequisites

To run this script, you will need Python 3.x installed on your system.

It's recommended to use a virtual environment to manage the Python package dependencies and isolate them from your system's global Python environment.

To create and activate a virtual environment, follow these steps:

On macOS and Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

After activating the virtual environment, install the required Python packages using the provided requirements.txt file with the following command:

```bash
pip install -r requirements.txt
```

This command will automatically install all the packages listed in `requirements.txt`, which should contain:

```
dnspython
colorama
pyfiglet
```

## Usage

Run the script by passing the target domain as a command-line argument:

```bash
python3 dns_enum.py example.com
```

Make sure you have a file named `subdomains.txt` in the same directory as the script, with one subdomain per line. The script will attempt to resolve each subdomain for the A record and print the valid ones to the console, as well as save them to an output file named `<domain>_valid_subdomains.txt`.

### Options

- `<domain>`: The domain for which you want to perform DNS enumeration and subdomain scanning. It should be a valid domain formatted as `example.com`.

## Output

The script generates two types of output:

1. Console output with the DNS enumeration results and valid subdomains highlighted in green.
2. A file named `<domain>_valid_subdomains.txt` containing all valid subdomains discovered during the scan.

## Interruption

If you need to stop the script, use `Ctrl+C`. The script will handle the interrupt and exit gracefully.

## Disclaimer

This tool is for educational and ethical testing purposes only. Users are responsible for abiding by applicable laws and regulations. The creator is not liable for misuse or any illegal activities performed with the tool.

## License

[MIT License](LICENSE.md)

## Author

Trident09