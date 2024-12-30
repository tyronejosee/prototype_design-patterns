from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class DocumentBuilder(ABC):
    """
    The Builder interface specifies the methods for creating the different parts
    of the Document objects.
    """

    @property
    @abstractmethod
    def document(self) -> None:
        pass

    @abstractmethod
    def build_header(self) -> None:
        pass

    @abstractmethod
    def build_content(self) -> None:
        pass

    @abstractmethod
    def build_footer(self) -> None:
        pass


class SimpleDocumentBuilder(DocumentBuilder):
    """
    Concrete builder for a simple report.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._document = Document()

    @property
    def document(self) -> Document:
        document = self._document
        self.reset()
        return document

    def build_header(self) -> None:
        self._document.add("Simple Header")

    def build_content(self) -> None:
        self._document.add("Simple Content")

    def build_footer(self) -> None:
        self._document.add("Simple Footer")


class DetailedDocumentBuilder(DocumentBuilder):
    """
    Concrete builder for a detailed report.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._document = Document()

    @property
    def document(self) -> Document:
        document = self._document
        self.reset()
        return document

    def build_header(self) -> None:
        self._document.add("Detailed Header with Table of Contents")

    def build_content(self) -> None:
        self._document.add("Detailed Content with Analysis and Data")

    def build_footer(self) -> None:
        self._document.add("Detailed Footer with References")


class Document:
    """
    The Product we are building (the report).
    """

    def __init__(self) -> None:
        self.parts: List[str] = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Document Parts: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is responsible for executing the building steps in a
    specific sequence.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> DocumentBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: DocumentBuilder) -> None:
        self._builder = builder

    def build_simple_document(self) -> None:
        self.builder.build_header()
        self.builder.build_content()
        self.builder.build_footer()

    def build_detailed_document(self) -> None:
        self.builder.build_header()
        self.builder.build_content()
        self.builder.build_footer()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director, and then
    starts the document building process.
    """

    director = Director()

    # Create a simple report
    simple_builder = SimpleDocumentBuilder()
    director.builder = simple_builder
    print("Simple Document: ")
    director.build_simple_document()
    simple_builder.document.list_parts()

    print("\n")

    # Create a detailed report
    detailed_builder = DetailedDocumentBuilder()
    director.builder = detailed_builder
    print("Detailed Document: ")
    director.build_detailed_document()
    detailed_builder.document.list_parts()

    print("\n")

    # Create a custom document
    print("Custom Document: ")
    simple_builder.build_header()
    simple_builder.build_footer()
    simple_builder.document.list_parts()
