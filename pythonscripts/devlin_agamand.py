'''

Engine: APE
Zone: Tirisfall Glades
Creature: Devlin Agamand

'''

import arcemu
from arcemu import Unit

DEVLIN_AGAMAND_TEXTS = [
"Mother, oh mother.  You should have listened to me...",
"They thought I was weak.  Haha!!",
"I am the head of the family.  Me.  ME!!!",
"I'm cold, lord.  When will you keep your promise?",
"My family hates me.  Frightened idiots, all of them!",
"Father?  Are you proud of me now? HAHAH!",
"Thurman my brother, who's laughing now?  Hah!"
]

DEVLIN_AGAMAND_STATE = {}

NPC_ID_DEVLIN_AGAMAND = 1657

def DevlinAgamand_onAIUpdate( unit, event ):
    guid = unit.getGUID()

    if guid not in DEVLIN_AGAMAND_STATE:
        DEVLIN_AGAMAND_STATE[ guid ] = 0

    state = DEVLIN_AGAMAND_STATE[ guid ]

    unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, DEVLIN_AGAMAND_TEXTS[ state ] )

    if state == 6:
            state = 0
    else:
            state = state + 1
    
    DEVLIN_AGAMAND_STATE[ unit.getGUID() ] = state

def DevlinAgamand_onLoad( unit, event ):

    unit.RegisterAIUpdateEvent( 25000 )

arcemu.RegisterUnitEvent( NPC_ID_DEVLIN_AGAMAND, arcemu.CREATURE_EVENT_ON_LOAD, DevlinAgamand_onLoad )
arcemu.RegisterUnitEvent( NPC_ID_DEVLIN_AGAMAND, arcemu.CREATURE_EVENT_ON_AIUPDATE, DevlinAgamand_onAIUpdate )