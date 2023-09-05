# Sagrada generator

This script generates cards for your PnP (Print and Play) projects. The original inspiration for this project stemmed from a BoardGameGeek post available at this link (https://boardgamegeek.com/filepage/219948/sagrada-card-generator). Subsequently, an individual (accessible here: https://gitlab.com/jirsis/sagrada-generator) took the initiative to migrate the original PowerShell script to Python. In my efforts, I've cloned and made some enhancements to the script.

## Execution

```
git clone https://gitlab.com/jirsis/sagrada-generator.git
cd sagrada-generator
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python sagrada_generator.py
```

## Modification

You can modify ```card.txt``` with these format, and you can generate your own cards.

