import arcemu
import ArcPyMath as Math
from arcemu import Unit

#NPC_SUNSTRIDER_GUARDIAN = 15371

SUNSTRIDER_GUARDIAN_TEXTS = [
"Move along, $C!",
"Off with you, $n!",
"Do not push it citizen!"
]

def SunstriderGuardian_onEmote( unit, event, player, emoteId ):
    
    chance = Math.randomUInt( 100 )

    if chance <= 30:

        #EMOTE_ONESHOT_SALUTE
        if emoteId == 14:
            unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, SUNSTRIDER_GUARDIAN_TEXTS[ 2 ] )
            unit.emote( arcemu.EMOTE_ONESHOT_TALK, 1000 )

        #EMOTE_ONESHOT_SALUTE
        elif emoteId == 66:
            random = Math.randomUInt( 1 )
            unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, SUNSTRIDER_GUARDIAN_TEXTS[ random ] )
            unit.emote( 66, 1000 )

arcemu.RegisterUnitEvent( 15371, arcemu.CREATURE_EVENT_ON_EMOTE, SunstriderGuardian_onEmote )