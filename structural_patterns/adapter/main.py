class Target:
    """
    The standard interface used by the modern system.
    """

    def request(self) -> dict:
        return {"message": "Default Target behavior"}


class LegacySystem:
    """
    The legacy system that returns data in XML format.
    """

    def legacy_request(self) -> str:
        return "<data><message>Legacy System XML data</message></data>"


class Adapter(Target):
    """
    The adapter converts data from the legacy system to expected format (JSON).
    """

    def __init__(self, legacy_system: LegacySystem):
        self.legacy_system = legacy_system

    def request(self) -> dict:
        # Convert XML to JSON
        legacy_data = self.legacy_system.legacy_request()
        # Manually parse the XML (just for simplicity in this example)
        start = legacy_data.find("<message>") + len("<message>")
        end = legacy_data.find("</message>")
        message = legacy_data[start:end]
        return {"message": message}


def client_code(target: "Target") -> None:
    """
    The client code works with any class that follows the Target interface.
    """
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: Working with the modern system:")
    target = Target()
    client_code(target)
    print("\n")

    print("Client: The legacy system has an incompatible interface:")
    legacy_system = LegacySystem()
    print(f"LegacySystem: {legacy_system.legacy_request()}")
    print("\n")

    print("Client: Using the Adapter to integrate the legacy system:")
    adapter = Adapter(legacy_system)
    client_code(adapter)
