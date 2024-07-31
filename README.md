# Discord Discount Bot

## Contents

- [Discord Discount Bot](#discord-discount-bot)
  - [Contents](#contents)
  - [How it works (simplified)](#how-it-works-simplified)
  - [Preview (fast)](#preview-fast)
    - [Help command](#help-command)
    - [Add\_item command](#add_item-command)
    - [Start\_loop command](#start_loop-command)
  - [How it works (technically)](#how-it-works-technically)
  - [How rules works](#how-rules-works)
    - [Database rules](#database-rules)
      - [To add a new table](#to-add-a-new-table)
    - [Default values rules](#default-values-rules)
      - [To add a new default value](#to-add-a-new-default-value)
  - [Usage](#usage)
    - [Copy and paste this in bash:](#copy-and-paste-this-in-bash)
    - [Next steps](#next-steps)
  - [Contact-me](#contact-me)

## How it works (simplified)
The bot employs an in-store search system (currently operational only on <a href="https://www.kabum.com.br" target="_blank">KaBuM!</a>) to identify the most pertinent products. The product categories are pre-defined; however, additional product categories may be incorporated through the use of the $add_item "item" command. The bot randomly selects specific products and disseminates them at regular 10-minute intervals.

## Preview (fast)

### Help command
![help](https://raw.githubusercontent.com/Rafaelszc/discord-discount-bot/main/resources/midia/help.gif)

### Add_item command
![add_item](https://raw.githubusercontent.com/Rafaelszc/discord-discount-bot/main/resources/midia/add_item.gif)

### Start_loop command
![start_loop](https://raw.githubusercontent.com/Rafaelszc/discord-discount-bot/main/resources/midia/start_loop.gif)

## How it works (technically)

The bot starts by webscraping the stores (initially KaBuM!) and storing the url of each product in a database. These searches are based on product types/names, which are pre-defined in a JSON file (read the rules), but new product names/types can also be implemented in the database by using the $add_item command. The webscraping action is carried out regardless of whether the user has activated it or not (using the $start_loop command), while the sending of embeds and the random selection of products depend on being activated.

## How rules works

### Database rules
In `resources/rules/database_rules.json`, this json will set the default database tables and columns.

#### To add a new table
Add on json
```json
{
    "id": 1,
    "table_name": "the table name",
    "columns": {"column1": "column1 type",
                "column2": "column2 type"}
}
```

### Default values rules
In `resources/rules/default_values.json`, this json will set the default values in database.

#### To add a new default value
Add on json
```json
{
    "id": 1,
    "table_name": "table name for this value",
    "values": ["value1", "value2"]
}
```

## Usage

### Copy and paste this in bash:
```bash
# Clone this repository
$ git clone https://github.com/Rafaelszc/discord-discount-bot

# Go to main path
$ cd discord-discount-bot/

# Install the dependencies
$ pip install -r requirements.txt

# Create a .env file
$ mkdir resources/env
$ touch resources/env/token.env
```

### Next steps
1. Add your bot's token and your discord ID to the `token.env` file, naming it TOKEN and AUTHOR_ID respectively
2. Run `app.py`

## Contact-me

<div class="contact-images" align=center>
    <a href="https://github.com/Rafaelszc"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white%22" style="border-radius: 10px; height: 35px; padding-right: 2px;"></a>
    <a href="mailto:rafaelbjj84@gmail.com"><img src="https://img.shields.io/badge/GMAIL-100000?style=for-the-badge&logo=gmail&logoColor=red" style="border-radius: 10px; height: 35px"></a>
    <a href="https://www.linkedin.com/in/rafael-souza-5461762b8"><img src="https://img.shields.io/badge/LINKEDIN-100000?style=for-the-badge&logo=linkedin&logoColor=blue" style="border-radius: 10px; height: 35px; padding-left: 2px;"></a>
</div>