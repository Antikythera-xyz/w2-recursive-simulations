# Python program to convert
# CSV to HTML Table

import csv
from tinyhtml import h, raw
import html

types = {
    'text',
    'quote',
    'img',
}

categories = {
    'Semio-mimetics',
    'Hypognostic Synthesis',
    'Phantomatics',
    'Simutation',
    'Hypercasting',
}

person = {
"Stephanie Sherman":"ssherman",
"N. Katherine Hayles":"nkhayles",
"Bogna Konior":"bkonior",
"Bernard Geoghegan":"bgeoghegan",
"Mindy Seu":"mseu",
"Ranjodh Singh Dhaliwal":"rdhaliwal",
"Jussi Parikka":"jparikka",
"M. Beatrice Fazi":"mbfazi",
"Jimena Canales":"jcanales",
"Patricia Reed":"preed",
"AA Cavia":"acavia",
"Paul Feigelfeld":"pfeigelfeld",
"Geoff Manaugh":"gmanaugh",
"Alexander Jones":"ajones",
}

class Tile:
    # init method or constructor
    def __init__(self, category, person, type, row):
        self.category = category
        self.person = person
        self.type = type
        self.row = row

    # Returns string.
    def toHTML(self):
        if self.type == 'text':
            return self.textHTML()
        if self.type == 'quote':
            return self.quoteHTML()
        if self.type == 'img':
            return self.imgHTML()

    def textHTML(self):
        # <div class="rdhaliwal tile"><span>addressability - series of mechanism to stabilize virtual to physical to find its subjects </span></div>
        klass = person[self.person] + " tile"
        text = raw(self.row["Text"].replace('“','"').replace('”','"'))
        return str(h("div", klass=klass)(h("span")(text)))

    def quoteHTML(self):
        # <div class="ssherman tile quote"><span>“Man thought he was building the world for man but actually built the world for machines”</span></div>
        klass = person[self.person] + " tile quote"
        text = raw(self.row["Text"])
        return str(h("div", klass=klass)(h("span")(text)))

    def imgHTML(self):
        # <div class="jcanales tile image">
        # <img src="img/facial-rec.gif"><br /><span>Photo-recognition and machine vision can be seen as models of 'what matters' to different AIs</span>
        # </div>
        klass = person[self.person] + " tile image"
        src = "img/" + self.row["imageName"]
        text = raw(self.row["Text"].replace('“','"').replace('”','"'))
        return str(h("div", klass=klass)(h("img", src=src),h("br"),h("span")(text)))

# Read csv in.
def main():
    tilesPerCategory = {
        'Semio-mimetics':[],
        'Hypognostic Synthesis':[],
        'Phantomatics':[],
        'Simutation':[],
        'Hypercasting':[],
    }

    with open('copy4.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if row['Type'] == "":
                continue

            t = Tile(row['Tags'], row['Quote author'], row['Type'], row)
            tilesPerCategory[t.category].append(t.toHTML())

    # Ouput tile HTML to file.
    with open('output.html', 'w') as out_file:
        for category in tilesPerCategory:
            print(category)
            out_file.write(category+'\n')
            print(len((tilesPerCategory[category])))
            for tile in tilesPerCategory[category]:
                if tile is None:
                    continue
                out_file.write(tile+'\n')
            out_file.write('\n\n')


main()
