'''

Engine: APE
Zone: Azuremyst Isle
Creature: Draenei Mourner
.npc portto 69282

'''
import arcemu
from arcemu import Unit

DRAENEI_MOURNER_STATE = {}

#type, lang, text, emote
DRAENEI_MOURNER_DATA = [
	[ 12, 0, "<Sobbing> I hate graveyards.  So many dead.  And my sweet Luhanaa....", 1 ],
	[ 12, 7, "It should have been me!", 6 ],
	[ 12, 7, "Be at peace, my sweet, sweet, Luhanaa.", 6 ],
	[ 12, 7, "I'll never forget you, my love.", 1 ],
	[ 12, 7, "If I ever find the ones responsible for the crash...!", 1 ],
    [ 12, 7, "We should never have come along.", 1 ],
    [ 12, 7, "Why, Luhanaa?  Why?!", 6 ],
    [ 12, 7, "I miss you so much!", 1 ],
    [ 12, 7, "You'll always be here, with me.", 1 ],
    [ 16, 0, "%s weeps softly.", 18 ],
    [ 16, 0, "%s bows his head and sighs, clearly exhausted.", 2 ],
    [ 16, 0, "%s breaks down into huge, wracking sobs.", 18 ],
	[ 16, 0, "%s stares in silence at the grave marker before him.", 0 ]
]

NPCID_DRAENEI_MOURNER = 17073

def DraeneiMourner_onLoad( unit, event ):

    unit.RegisterAIUpdateEvent( 25000 )

def DraeneiMourner_onAIUpdate( unit, event ):
    guid = unit.getGUID()

    if guid not in DRAENEI_MOURNER_STATE:
        DRAENEI_MOURNER_STATE[ guid ] = 0

    state = DRAENEI_MOURNER_STATE[ guid ]

    unit.sendChatMessage( DRAENEI_MOURNER_DATA[ state ][ 0 ], DRAENEI_MOURNER_DATA[ state ][ 1 ], DRAENEI_MOURNER_DATA[ state ][ 2 ] )
    unit.emote( DRAENEI_MOURNER_DATA[ state ][ 3 ] )

    if state == 12:
            state = 0
    else:
            state = state + 1
    
    DRAENEI_MOURNER_STATE[ guid ] = state

arcemu.RegisterUnitEvent( NPCID_DRAENEI_MOURNER, arcemu.CREATURE_EVENT_ON_LOAD, DraeneiMourner_onLoad )
arcemu.RegisterUnitEvent( NPCID_DRAENEI_MOURNER, arcemu.CREATURE_EVENT_ON_AIUPDATE, DraeneiMourner_onAIUpdate )