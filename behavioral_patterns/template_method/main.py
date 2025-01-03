from abc import ABC, abstractmethod
import csv
import json
import xml.etree.ElementTree as ET


class FileProcessor(ABC):
    """
    The AbstractClass defines the skeleton of the algorithm for processing files.
    It delegates specific file format operations to concrete subclasses.
    """

    def process_file(self, file_path: str) -> None:
        """
        The template method defines the skeleton of file processing algorithm.
        """
        self.read_file(file_path)
        self.parse_data()
        self.save_data()
        self.finalize()

    def read_file(self, file_path: str) -> None:
        """
        Reads the file from the provided path.
        This is a base operation for all formats.
        """
        print(f"Reading file: {file_path}")

    def save_data(self) -> None:
        """
        Save the parsed data to a database or file.
        """
        print("Saving data...")

    def finalize(self) -> None:
        """
        Final clean-up or any operations after saving data.
        """
        print("Finalizing processing...")

    @abstractmethod
    def parse_data(self) -> None:
        """
        Each subclass implements this method
        to handle specific file format parsing.
        """
        pass


class CSVFileProcessor(FileProcessor):
    """
    Concrete implementation for processing CSV files.
    """

    def parse_data(self) -> None:
        """
        Parse CSV file and process the data.
        """
        print("Parsing CSV file...")
        with open("data.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Processing row: {row}")


class JSONFileProcessor(FileProcessor):
    """
    Concrete implementation for processing JSON files.
    """

    def parse_data(self) -> None:
        """
        Parse JSON file and process the data.
        """
        print("Parsing JSON file...")
        with open("data.json", "r") as file:
            data = json.load(file)
            for item in data:
                print(f"Processing item: {item}")


class XMLFileProcessor(FileProcessor):
    """
    Concrete implementation for processing XML files.
    """

    def parse_data(self) -> None:
        """
        Parse XML file and process the data.
        """
        print("Parsing XML file...")
        tree = ET.parse("data.xml")
        root = tree.getroot()
        for elem in root:
            print(f"Processing element: {elem.tag}, {elem.text}")


def client_code(processor: FileProcessor, file_path: str) -> None:
    """
    The client code uses the template method to process different file formats.
    It doesn’t need to know the concrete class, just uses the base class interface.
    """
    processor.process_file(file_path)


if __name__ == "__main__":
    # Client code works with different file formats

    print("Processing CSV file:")
    client_code(CSVFileProcessor(), "data.csv")
    print("")

    print("Processing JSON file:")
    client_code(JSONFileProcessor(), "data.json")
    print("")

    print("Processing XML file:")
    client_code(XMLFileProcessor(), "data.xml")
