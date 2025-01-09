from abc import ABC, abstractmethod
from typing import List


class FileSystemComponent(ABC):
    """Common interface for files and folders."""

    @abstractmethod
    def show(self, depth: int = 0) -> str:
        pass


class File(FileSystemComponent):
    """Individual file."""

    def __init__(self, name: str) -> None:
        self.name = name

    def show(self, depth: int = 0) -> str:
        return f"{' ' * depth}- {self.name}"


class Folder(FileSystemComponent):
    """Folder that can contain files and other folders."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> None:
        self._children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        self._children.remove(component)

    def show(self, depth: int = 0) -> str:
        result = f"{' ' * depth}+ {self.name}\n"
        for child in self._children:
            result += child.show(depth + 2) + "\n"
        return result.strip()


# Client
if __name__ == "__main__":
    # Create individual files
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    # Create folders
    folder1 = Folder("Documents")
    folder2 = Folder("Images")
    folder3 = Folder("Projects")

    # Compose the hierarchy
    folder1.add(file1)
    folder1.add(file2)
    folder2.add(file3)
    folder3.add(folder1)
    folder3.add(folder2)

    # Display the file system structure
    print(folder3.show())
