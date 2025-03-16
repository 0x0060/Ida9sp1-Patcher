<div align="center">
  
# IDA Pro 9 SP1 Patcher

![image](https://github.com/user-attachments/assets/5b390f9c-dd00-4d8d-ac7f-0de93f9849ec)


[![](https://img.shields.io/badge/%20-MIT-98a9f6?style=for-the-badge&labelColor=dedefd&logo=github&logoColor=6874a9)](https://raw.githubusercontent.com/0x0060/Ida9sp1-Patcher/refs/heads/main/LICENSE)
![](https://img.shields.io/badge/%20-PYTHON-98a9f6?style=for-the-badge&labelColor=dedefd&logo=python&logoColor=6874a9)
[![](https://img.shields.io/badge/%20-stars-98a9f6?style=for-the-badge&labelColor=dedefd&logo=github&logoColor=6874a9)](https://github.com/Ida9sp1-Patcher/NIDS/stargazers)
[![](https://img.shields.io/badge/%20-issues-98a9f6?style=for-the-badge&labelColor=dedefd&logo=github&logoColor=6874a9)](https://github.com/0x0060/Ida9sp1-Patcher/issues)

</div>

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [License Structure](#license-structure)
- [Supported Decompilers](#supported-decompilers)
- [Disclaimer](#disclaimer)

## Overview

IDA Pro 9 SP1 Patcher is a utility designed to generate license files for IDA Pro 9 Service Pack 1. It creates a JSON-based license file that includes all available decompiler plugins with a validity period of 10 years from the current date.

## Features

- Generates a valid IDA Pro 9 SP1 license file
- Includes all available decompiler plugins
- Sets a 10-year validity period from the current date
- Uses a clean, object-oriented design with dependency injection
- Customizable owner information

## Requirements

- Python 3.6 or higher
- No external dependencies beyond the Python standard library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/0x0060/Ida9sp1-Patcher.git
cd Ida9sp1-Patcher
```

2. No additional installation steps are required as the tool uses only Python standard libraries.

## Usage

Simply run the main script to generate a license file:

```bash
python main.py
```

The tool will generate an `idapro.hexlic` file in the current directory. You can then copy this file to your IDA Pro installation directory or the location specified in your IDA Pro configuration.

## How It Works

The patcher works by generating a properly formatted license file with the following components:

1. **Time Management**: Uses the system clock to set the current date as the start date and calculates an end date 10 years in the future.

2. **License Generation**: Creates a license object with predefined ID, owner information, and a list of addon plugins.

3. **File Output**: Writes the license data as a JSON file with the required structure and signature.

## License Structure

The generated license file follows this structure:

```json
{
  "header": {"version": 1},
  "payload": {
    "name": "0x0060",
    "email": "ren@0x0060.dev",
    "licenses": [
      {
        "id": "48-2437-ACBD-29",
        "license_type": "named",
        "product": "IDA",
        "product_id": "IDAPRO",
        "edition_id": "ida-pro",
        "seats": 1,
        "start_date": "YYYY-MM-DD HH:MM:SS",
        "end_date": "YYYY-MM-DD HH:MM:SS",
        "issued_on": "YYYY-MM-DD HH:MM:SS",
        "owner": "0x0060",
        "add_ons": [...],
        "features": []
      }
    ]
  },
  "signature": "3238353E900849B6547801BBF8AF31E7822CB4B74A6F54DE03F5E9DFF96AC5DA981B50A62EAAF021F2052CC44498107B36C2D3B34C86B7B48084313189274A1D5D1F45C1F512820C508EA22ABA43EC584E6FEFF6BA9969DD428268F40859AFFE8A2E5BB66CA9C71E78FCAC14E3168D26D11952A71C0F330251D9D74FFC67BD24"
}
```

## Supported Decompilers

The generated license includes the following decompiler plugins:

- HEXX86 - x86 Decompiler
- HEXX64 - x86-64 Decompiler
- HEXARM - ARM Decompiler
- HEXARM64 - ARM64 Decompiler
- HEXMIPS - MIPS Decompiler
- HEXMIPS64 - MIPS64 Decompiler
- HEXPPC - PowerPC Decompiler
- HEXPPC64 - PowerPC64 Decompiler
- HEXRV64 - RISC-V 64 Decompiler
- HEXARC - ARC Decompiler
- HEXARC64 - ARC64 Decompiler

## Disclaimer

This tool is provided for educational purposes only. Using this tool to bypass licensing for commercial software may violate the software's terms of service and applicable laws. The author is not responsible for any misuse of this tool or any consequences that may arise from such misuse.

Always purchase legitimate licenses for commercial software you use professionally.
