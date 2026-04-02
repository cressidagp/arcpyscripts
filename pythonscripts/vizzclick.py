import arcemu
from arcemu import GossipMenu

NPCID_VIZZCLICK = 6568

def Vizzclick_onHello( unit, event, player ):

    menu = GossipMenu( 1933, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.addItem( arcemu.ICON_CHAT, "I wish to browse your wares.", 0, 0 )

    menu.sendToPlayer( player )

def Vizzclick_onSelect( unit, player, id, enteredCode ):

    creature = unit.toCreature()

    if id == 0:

        session = player.getSession()
        session.sendInventoryList( creature )


arcemu.RegisterUnitGossipEvent( NPCID_VIZZCLICK, arcemu.GOSSIP_EVENT_HELLO, Vizzclick_onHello )
arcemu.RegisterUnitGossipEvent( NPCID_VIZZCLICK, arcemu.GOSSIP_EVENT_SELECT, Vizzclick_onSelect )