from setuptools import setup,find_packages

setup(
    name="personal_bot_assistant",
    version="1.1.4",
    entry_points={
        "console_scripts":["bot-start=personal_bot_assistant.bot:main"]
    },
    packages=find_packages()
)