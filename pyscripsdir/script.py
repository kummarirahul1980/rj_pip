from pathlib import Path

packages = {
    "rj_home": {
        "name": "rj-home",
        "dependencies": ["rj-core"],
        "script": 'chaduvukofirst = "core.cli:chaduvukofirst"',
    },
    "rj_core": {
        "name": "rj-core",
        "dependencies": ["bcrypt"],
    },
    "rj_mails": {
        "name": "rj-mails",
    },
    "rj_api": {
        "name": "rj-api",
    },
    "rj_serialisers": {
        "name": "rj-serialisers",
    },
    "rj_apps": {
        "name": "rj-apps",
    },
}

for directory, config in packages.items():
    content = f"""[project]
name = "{config["name"]}"
version = "0.1.1"
authors = [
    {{ name = "rahul" }}
]
dependencies = {config.get("dependencies", [])}
"""

    if "script" in config:
        content += f"""
[project.scripts]
{config["script"]}
"""

    Path(directory, "pyproject.toml").write_text(content)
