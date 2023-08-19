'''

Engine: APE
Zone: Tirisfall Glades
Creature: Meven Korgal

'''

import arcemu
from arcemu import Unit

MEVEN_KORGAL_TEXTS = [
"These undead atrocities will be destroyed!",
"We must be vigilant to eradicate this plague!",
"Keep up the good work.  This scourge will be cleansed!",
"The Scarlet Crusade will scour these lands!",
"Let none with the foul taint of plague live!"
]

MEVEN_KORGAL_STATE = {}

NPC_ID_MEVEN_KORGAL = 1667

def MevenKorgal_onAIUpdate( unit, event ):
    guid = unit.getGUID()

    if guid not in MEVEN_KORGAL_STATE:
        MEVEN_KORGAL_STATE[ guid ] = 0

    state = MEVEN_KORGAL_STATE[ guid ]

    unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, MEVEN_KORGAL_TEXTS[ state ] )

    if state == 4:
            state = 0
    else:
            state = state + 1
    
    MEVEN_KORGAL_STATE[ unit.getGUID() ] = state

def MevenKorgal_onLoad( unit, event ):

    unit.RegisterAIUpdateEvent( 120000 )

arcemu.RegisterUnitEvent( NPC_ID_MEVEN_KORGAL, arcemu.CREATURE_EVENT_ON_LOAD, MevenKorgal_onLoad )
arcemu.RegisterUnitEvent( NPC_ID_MEVEN_KORGAL, arcemu.CREATURE_EVENT_ON_AIUPDATE, MevenKorgal_onAIUpdate )