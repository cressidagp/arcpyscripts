import arcemu
import ArcPyMath as Math
from arcemu import Unit
from arcemu import ObjectLocator

RAELEN_TEXTS = [
"We have yet to meet our quota for the wood demand. Now back to work with you.",
"Daylight is still upon us so let's see that axe of yours chopping some more wood.",
"We need to get this wagon filled by the end of the day. So back to work with you. Chop, chop!"
]

RAELEN_EMOTES = [ 25, 1, 5 ]

NPC_ID_SUPERVISOR_RAELEN = 10616
NPC_ID_EASTVALE_PEASANT = 11328

def SupervisorRaelen_onLoad( unit, event ):

    unit.RegisterAIUpdateEvent( 1 * 1000 )

def SupervisorRaelen_onAIUpdate( unit, event ):

    objects = unit.getObjectsInRange()
    for o in objects:
        u = arcemu.toUnit( o )
        if u is not None:
            entry = u.getUInt32Value( arcemu.OBJECT_FIELD_ENTRY )

            if entry == NPC_ID_EASTVALE_PEASANT:
                distance = unit.calcDistance( u )
                print(distance)
                
                if distance < 10:
                    i = Math.randomUInt( 2 )
                    unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_COMMON, RAELEN_TEXTS[ Math.randomUInt( i ) ] )
                    unit.emote( RAELEN_EMOTES[ Math.randomUInt( i ) ], 0 )
                    unit.ModifyAIUpdateEvent( 20 * 1000 )

arcemu.RegisterUnitEvent( NPC_ID_SUPERVISOR_RAELEN, arcemu.CREATURE_EVENT_ON_LOAD, SupervisorRaelen_onLoad )
arcemu.RegisterUnitEvent( NPC_ID_SUPERVISOR_RAELEN, arcemu.CREATURE_EVENT_ON_AIUPDATE, SupervisorRaelen_onAIUpdate )