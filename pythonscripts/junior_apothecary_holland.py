'''

Engine: APE
Zone: Tirisfall Glades
Creature: Junior Apothecary Holland

'''

import arcemu
import ArcPyMath as Math
from arcemu import Unit

APOTHECARY_HOLLAND_TEXTS = [
"What could be taking so long?",
"How long can it take to pick a handful of weeds?",
"At this rate I could have gathered them myself!",
"If you want something done right, do it yourself!",
"As if I had all eternity.",
"Ah, this must be him now... no?  Bah!",
"Maybe I should have just bought some off of Faruza?",
"I had to go and requisition an Abomination... an Abomination!"
]

APOTHECARY_HOLLAND_STATE = {}

NPC_ID_APOTHECARY_HOLLAND = 10665

def ApothecaryHolland_onReachWP( unit, event, waypointId, forward ):

    chance = Math.randomUInt( 99 )

    if chance < 10:

        guid = unit.getGUID()

        if guid not in APOTHECARY_HOLLAND_STATE:
              APOTHECARY_HOLLAND_STATE[ guid ] = 0
              
        state = APOTHECARY_HOLLAND_STATE[ guid ]

        unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_ORCISH, APOTHECARY_HOLLAND_TEXTS[ state ] )
          
        if state == 7:
                state = 0
        else:
                state = state + 1

        APOTHECARY_HOLLAND_STATE[ unit.getGUID() ] = state

arcemu.RegisterUnitEvent( NPC_ID_APOTHECARY_HOLLAND, arcemu.CREATURE_EVENT_ON_REACH_WP, ApothecaryHolland_onReachWP )