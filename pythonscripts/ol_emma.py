'''

Engine: APE
Zone: Stormwind City
Creature: Ol Emma

'''

import arcemu
import ArcPyMath as Math
from arcemu import Unit

OL_EMMA_TEXTS = [
"Seems like a hundred times a day I walk all the way to the well to get more water. No respect for their elders I tell ya.",
"Jack and Jill my wrinkled patoot! I do all the water luggin' 'round here.",
"Think I'm starting to wear a rut in the paving stones.",
"One of these days I'm gonna drown him in that blue robe. And all his brooms too.",
"O'course I'm talkin to myself. Only way to get decent conversation in this city.",
"As if I don't have better things to do in my old age than carry buckets of water.",
"Where's the water, Emma? Get the water, Emma? If'n it weren't fer me, that lot wouldn't know what water looks like.",
"Deja vu.  For a moment, I thought I was back home... before the plague..."
]

OL_EMMA_STATE = {}

NPC_ID_OL_EMMA = 3520

def OlEmma_onReachWP( unit, event, waypointId, forward ):

	chance = Math.randomUInt( 99 )

	if chance < 10:

		guid = unit.getGUID()

		if guid not in OL_EMMA_STATE:
			OL_EMMA_STATE[ guid ] = 0

		state = OL_EMMA_STATE[ guid ]

		if forward:
			unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_COMMON, OL_EMMA_TEXTS[ state ] )

		else:
			unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_COMMON, OL_EMMA_TEXTS[ state + 4 ] )

		if state == 3:
				state = 0
		
		else:
				state = state + 1

		OL_EMMA_STATE[ unit.getGUID() ] = state

arcemu.RegisterUnitEvent( NPC_ID_OL_EMMA, arcemu.CREATURE_EVENT_ON_REACH_WP, OlEmma_onReachWP )