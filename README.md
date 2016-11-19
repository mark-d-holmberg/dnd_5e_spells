
# D&D 5e Spell JSON Generator
## Author: austen0

### Summary
This project is intended to generate JSON files compatible with the RPG Card generator at https://crobi.github.io/rpg-cards/. The spell source file contains all (maybe?) from the PHB and EE.

### Instructions

**Create a new spell list:**

Generate a list of all available spells by running:

```
Syntax:  $ python spell_cards.py --new_spell_list ${/path/to/spell_list.csv}
Example: $ python spell_cards.py --new_spell_list druid.csv
```

You can also choose to generate only spells useable by one or more classes with the following flag:

```
Syntax:  --classes ${classes}
Example: --classes S,W

Class abbreviations:
B - Bard
C - Cleric
D - Druid
M - Monk
P - Paladin
R - Ranger
S - Sorcerer
W - Warlock
Z - Wizard
```


**Pick Spells:**

Open the new spell list and use `ctrl+f` to find the spells you'd like and un-comment them.

**Generate JSON file:**

To generate the JSON file from your spell list, run:

```
Syntax:  $ python spell_cards.py --gen_spell_json ${/path/to/spell_list.csv}
Example: $ python spell_cards.py --gen_spell_json druid.csv
```

You can also use the following optional flags:

```
Syntax:  --color ${color}
Example: --color darkgreen

Syntax:  --icon_back ${icon}
Example: --icon_back heavy-thorny-triskelion
```
