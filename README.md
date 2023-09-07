# Sagrada generator

This script generates cards for your PnP (Print and Play) projects. The original inspiration for this project stemmed from a BoardGameGeek post available at this [link](https://boardgamegeek.com/filepage/219948/sagrada-card-generator). Subsequently, an individual (accessible [here](https://gitlab.com/jirsis/sagrada-generator)) took the initiative to migrate the original PowerShell script to Python. In my efforts, I've cloned and made some enhancements to the script.

I included the full list of sagrada promos and packs listed [here](https://boardgamegeek.com/thread/2737742/list-all-sagrada-promos-and-packs)

## Format of card.txt file
If you want to include more custom cards, you could add lines to the card.txt file following the next format for a new card:

### This is an example of a card
`Vitraux

5

3wrw2

wg6pw

yw1wb

w5w4w

Promo1A`

### Description

Line 1 (Vitraux)    = Name of the card. This name would be filled in the bottom of the card.

Line 2 (5)         = Difficulty of the card.

Line 3 (3wrw2)      = From line 3 to line 6 you need to put the content of the card.

Line 4 (wg6pw)

Line 5 (yw1wb)

Line 6 (w5w4w)

Line 7 (Promo1A)    = Name of the generated file.

For Lines 3 to 6 you must use this convention:
- 1 or 2 or 3 or 4 or 5 or 6 for a die 
- w for a White space
- r for a Red space
- g for a Green space
- b for a Blue space
- p for a Purple space
- y for a Yellow space

