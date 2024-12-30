from threading import Lock


class SingletonMeta(type):
    """
    Thread-safe Singleton implementation.
    """

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class ConfigurationManager(metaclass=SingletonMeta):
    """
    A Singleton class for managing application configuration.
    """

    def __init__(self, config_file: str) -> None:
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """
        Simulates loading configuration from a file.
        """
        print(f"Loading configuration from {self.config_file}...")
        # Simulate file loading.
        return {
            "app_name": "MyApp",
            "version": "1.0",
            "debug": True,
            "database": {
                "host": "localhost",
                "port": 5432,
                "user": "admin",
                "password": "secret",
            },
        }

    def get(self, key: str):
        """
        Get a configuration value by key.
        """
        return self.config.get(key)

    def update(self, key: str, value):
        """
        Update a configuration value.
        """
        self.config[key] = value


# Test the ConfigurationManager singleton
def test_configuration_manager():
    manager1 = ConfigurationManager("config.yaml")
    print(f"Manager1 Config: {manager1.get('app_name')}")

    manager2 = ConfigurationManager("config.json")
    print(f"Manager2 Config: {manager2.get('app_name')}")

    # Update configuration in one instance
    manager1.update("app_name", "UpdatedApp")
    print(f"Manager1 Updated Config: {manager1.get('app_name')}")
    print(
        f"Manager2 Updated Config: {manager2.get('app_name')}"
    )  # Should reflect the same change


if __name__ == "__main__":
    print("Testing ConfigurationManager Singleton...\n")
    test_configuration_manager()
