from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import json
import sys


class TimeProvider(ABC):
    """
    Abstract base class for time-related operations.
    """
    @abstractmethod
    def current_time(self) -> str:
        """
        Get the current time formatted as a string.
        
        Returns:
            str: Formatted current time string
        """
        pass
    
    @abstractmethod
    def future_time(self, years: int) -> str:
        """
        Get a future time formatted as a string.
        
        Args:
            years: Number of years to add to current time
            
        Returns:
            str: Formatted future time string
        """
        pass


class DefaultTimeProvider(TimeProvider):
    """
    Default implementation of TimeProvider that uses the system clock.
    """
    def current_time(self) -> str:
        """
        Get the current time formatted as a string.
        
        Returns:
            str: Current time formatted as 'YYYY-MM-DD HH:MM:SS'
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def future_time(self, years: int = 999999) -> str:
        """
        Get a future time formatted as a string.
        
        Args:
            years: Number of years to add to current time (default: 10)
            
        Returns:
            str: Future time formatted as 'YYYY-MM-DD HH:MM:SS'
        """
        future = datetime.now() + timedelta(days=365 * years)
        return future.strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class AddonPlugin:
    """
    Represents an addon plugin for the IDA Pro license.
    """
    id: str
    code: str
    owner: str
    start_date: str
    end_date: str
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the addon plugin to a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the addon plugin
        """
        return {
            "id": self.id,
            "code": self.code,
            "owner": self.owner,
            "start_date": self.start_date,
            "end_date": self.end_date
        }


@dataclass
class LicenseId:
    """
    Represents the license ID section of the IDA Pro license.
    """
    id: str = "48-2437-ACBD-29"
    license_type: str = "named"
    product: str = "IDA"
    product_id: str = "IDAPRO"
    edition_id: str = "ida-pro"
    seats: int = 1
    start_date: str = ""
    end_date: str = ""
    issued_on: str = ""
    owner: str = "0x0060"
    add_ons: List[AddonPlugin] = field(default_factory=list)
    features: List[Any] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the license ID to a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the license ID
        """
        return {
            "id": self.id,
            "license_type": self.license_type,
            "product": self.product,
            "product_id": self.product_id,
            "edition_id": self.edition_id,
            "seats": self.seats,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "issued_on": self.issued_on,
            "owner": self.owner,
            "add_ons": [addon.to_dict() for addon in self.add_ons],
            "features": self.features
        }


@dataclass
class LicensePayload:
    """
    Represents the payload section of the IDA Pro license.
    """
    name: str = "0x0060"
    email: str = "ren@0x0060.dev"
    licenses: List[LicenseId] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the license payload to a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the license payload
        """
        return {
            "name": self.name,
            "email": self.email,
            "licenses": [license_id.to_dict() for license_id in self.licenses]
        }


@dataclass
class License:
    """
    Represents the complete IDA Pro license.
    """
    header: Dict[str, Any] = field(default_factory=lambda: {"version": 1})
    payload: LicensePayload = field(default_factory=LicensePayload)
    signature: str = "3238353E900849B6547801BBF8AF31E7822CB4B74A6F54DE03F5E9DFF96AC5DA981B50A62EAAF021F2052CC44498107B36C2D3B34C86B7B48084313189274A1D5D1F45C1F512820C508EA22ABA43EC584E6FEFF6BA9969DD428268F40859AFFE8A2E5BB66CA9C71E78FCAC14E3168D26D11952A71C0F330251D9D74FFC67BD24"
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the license to a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the license
        """
        return {
            "header": self.header,
            "payload": self.payload.to_dict(),
            "signature": self.signature
        }


class LicenseGenerator:
    """
    Generator for IDA Pro licenses.
    """
    def __init__(self, time_provider: Optional[TimeProvider] = None):
        """
        Initialize the license generator.
        
        Args:
            time_provider: Provider for time-related operations (default: DefaultTimeProvider)
        """
        self.time_provider = time_provider or DefaultTimeProvider()
    
    def generate_license(self) -> License:
        """
        Generate an IDA Pro license.
        
        Returns:
            License: Generated license object
        """
        start_date = self.time_provider.current_time()
        end_date = self.time_provider.future_time(10)
        
        license_id = LicenseId(
            start_date=start_date,
            end_date=end_date,
            issued_on=start_date
        )
        
        addon_plugins = [
            "HEXX86", "HEXX64", "HEXARM", "HEXARM64",
            "HEXMIPS", "HEXMIPS64", "HEXPPC", "HEXPPC64",
            "HEXRV64", "HEXARC", "HEXARC64"
        ]
        
        for i, plugin in enumerate(addon_plugins):
            addon = AddonPlugin(
                id=f"48-1337-DEAD-{i}",
                code=plugin,
                owner=license_id.id,
                start_date=start_date,
                end_date=end_date
            )
            license_id.add_ons.append(addon)
        
        payload = LicensePayload()
        payload.licenses.append(license_id)
        
        license = License(payload=payload)
        
        return license


class FileWriter:
    """
    Writer for license files.
    """
    @staticmethod
    def write_json(data: Dict[str, Any], filename: str) -> bool:
        """
        Write JSON data to a file.
        
        Args:
            data: JSON data to write
            filename: Name of the file to write to
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, separators=(',', ':'))
            return True
        except IOError as e:
            print(f"Failed to open file :( -> {filename}\n{str(e)}", file=sys.stderr)
            return False


def main() -> int:
    """
    Main function.
    
    Returns:
        int: Exit code
    """
    generator = LicenseGenerator()
    
    license = generator.generate_license()
    
    writer = FileWriter()
    success = writer.write_json(license.to_dict(), "idapro.hexlic")
    
    if success:
        print("License file generated: idapro.hexlic :D")
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
