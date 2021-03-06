import csv
from random import shuffle

def writeClassifiedMovesCSV(entries):
  with open('data/classified-moves.csv', 'w') as fh:
    writer = csv.writer(fh, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['engine', 'moveNumber', 'rank', 'loss', 'advantage', 'ambiguity', 'timeConsistent', 'emt', 'rOnAmb', 'onlyMove'])
    shuffle(entries)
    [writer.writerow(entry) for entry in entries]     

def writeClassifiedChunksCSV(entries):
  with open('data/classified-chunks.csv', 'w') as fh:
    writer = csv.writer(fh, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['engine', 'moveNo',
      'rank1', 'loss1', 'advantage1', 'ambiguity1', 'timeConsistent1', 'emt1', 'rOnAmb1', 'onlyMove1',
      'rank2', 'loss2', 'advantage2', 'ambiguity2', 'timeConsistent2', 'emt2', 'rOnAmb2', 'onlyMove2',
      'rank3', 'loss3', 'advantage3', 'ambiguity3', 'timeConsistent3', 'emt3', 'rOnAmb3', 'onlyMove3',
      'rank4', 'loss4', 'advantage4', 'ambiguity4', 'timeConsistent4', 'emt4', 'rOnAmb4', 'onlyMove4',
      'rank5', 'loss5', 'advantage5', 'ambiguity5', 'timeConsistent5', 'emt5', 'rOnAmb5', 'onlyMove5',
      'rank6', 'loss6', 'advantage6', 'ambiguity6', 'timeConsistent6', 'emt6', 'rOnAmb6', 'onlyMove6',
      'rank7', 'loss7', 'advantage7', 'ambiguity7', 'timeConsistent7', 'emt7', 'rOnAmb7', 'onlyMove7',
      'rank8', 'loss8', 'advantage8', 'ambiguity8', 'timeConsistent8', 'emt8', 'rOnAmb8', 'onlyMove8',
      'rank9', 'loss9', 'advantage9', 'ambiguity9', 'timeConsistent9', 'emt9', 'rOnAmb9', 'onlyMove9',
      'rank10', 'loss10', 'advantage10', 'ambiguity10', 'timeConsistent10', 'emt10','rOnAmb10', 'onlyMove10'
    ])
    shuffle(entries)
    [writer.writerow(entry) for entry in entries]

def writeClassifiedMoveChunksCSV(entries):
  with open('data/classified-move-chunks.csv', 'w') as fh:
    writer = csv.writer(fh, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['engine', 'move1', 'move2', 'move3', 'move4',
      'chunk1', 'chunk2', 'chunk3', 'chunk4', 'pmove1', 'pmove2', 'pmove3', 'pvmove4',
      'pchunk1', 'pchunk2', 'pchunk3', 'pchunk4', 'streak1', 'streak2', 'streak3', 'streak4',
      'pstreak1', 'pstreak2', 'pstreak3', 'pstreak4', 'winningIndex'])
    shuffle(entries)
    [writer.writerow(entry) for entry in entries]

def writeClassifiedGamesCSV(entries):
  with open('data/classified-games.csv', 'w') as fh:
    writer = csv.writer(fh, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['engine', 'gb1', 'gb2', 'gb3', 'gb4', 'gp1', 'gp2', 'gp3', 'gp4', 's1', 's2', 's3', 's4', 'sp1', 'sp2', 'sp3', 'sp4'])
    shuffle(entries)
    [writer.writerow(entry) for entry in entries]