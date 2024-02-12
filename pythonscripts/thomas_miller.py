import arcemu
import ArcPyMath as Math
from arcemu import Unit

THOMAS_MILLER_TEXTS = [
"Fresh bread for sale!",
"Freshly baked bread for sale!",
"Rolls, buns and bread. Baked fresh!",
"Warm, wholesome bread!"
]

NPC_ID_THOMAS_MILLER = 3518

def ThomasMiller_onReachWP( unit, event, waypointId, forward ):

    if waypointId == 2 or waypointId == 23:

        for x in range( 2 ):

            unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_COMMON, THOMAS_MILLER_TEXTS[ Math.randomUInt( 3 ) ], x * 3 * 1000 )
        
arcemu.RegisterUnitEvent( NPC_ID_THOMAS_MILLER, arcemu.CREATURE_EVENT_ON_REACH_WP, ThomasMiller_onReachWP )