"""Read KEY=value setting from a .env file."""


def load_env(path=".env"):
    setting = {}
    with open(path) as handle:
       for line in handle:
           line = line.strip()
           if not linr or line.startswitch("#"):
               continue
           key, _, value = line.partition("=")
           setting[key.strip()] = value.strip()
    return settings
