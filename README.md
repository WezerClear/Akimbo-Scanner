# Akimbo Scanner

![Akimbo Scanner](https://github.com/WezerClear/sub-dir/blob/main/logo.jpg)

**Disclaimer**

This tool is intended for educational purposes and ethical hacking practices. The author disclaims any responsibility for any illegal actions performed with this tool.

## Description

Akimbo Scanner is a tool designed to scan subdomains and directories. It is developed by SGB and maintained on GitHub https://github.com/wezerclear

## Installation

To use Akimbo Scanner, make sure you have Python installed on your system. Clone the repository from GitHub:

```bash
git clone https://github.com/WezerClear/Akimbo-Scanner
```

Navigate to the directory and install the required dependencies using pip:

```bash
cd Akimbo-Scanner
pip3 install -r requirements.txt
```

## Usage

Run the scanner using the following command:

```bash
python3 akimbo_scanner.py -u <target_url>
```

### Options

- `-u, --url`: Specify the target URL.
- `-s, --speed`: Choose the speed of the scan (1 to 5, default is 1).
- `-v, --verbose`: Activate verbose mode.

## Example

```bash
python akimbo_scanner.py -u example.com
```

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss the changes.

## License

No licence

## Acknowledgements

- WezerClear for maintaining the project.
