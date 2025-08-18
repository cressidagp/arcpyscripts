import arcemu
from arcemu import GameObject
from arcemu import Unit

#GO_BENEDICT_CHEST = 3239
#NPC_KULTIRAS_MARINE = 3129

def BenedictChest_onUse( go, event, plr ):

    mapMgr = plr.getMapMgr()
    if mapMgr is None:
        return

    marine = mapMgr.spawnCreature( 3129, go.getPositionX(), go.getPositionY(), go.getPositionZ() )

    u = arcemu.toUnit( marine )
    m = arcemu.toCreature( u )
    
    if m is not None:

        m.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "Step away from the Lieutenants belongings!" )

arcemu.RegisterGameObjectEvent( 3239, arcemu.GO_EVENT_ON_USE, BenedictChest_onUse )