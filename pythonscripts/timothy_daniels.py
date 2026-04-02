import arcemu
from arcemu import GossipMenu

NPCID_TIMOTHY_DANIELS = 18019

def TimothyDaniels_onHello( unit, event, player ):

    menu = GossipMenu( 9238, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.addItem( arcemu.ICON_VENDOR, "I wish to browse your wares.", 0, 0 )
    menu.addItem( arcemu.ICON_CHAT, "Specialist, eh? Just what kind of specialist are you, anyway?", 1, 0 )

    session = player.getSession()
    menu.sendToPlayer( player )

def TimothyDaniels_onSelect( unit, player, id, enteredCode ):

    creature = unit.toCreature()

    if id == 0:

        session = player.getSession()
        session.sendInventoryList( creature )

    else:
        menu = GossipMenu( 9239, unit, arcemu.GOSSIP_AUTOSEND_FALSE )
        menu.sendToPlayer( player )

arcemu.RegisterUnitGossipEvent( NPCID_TIMOTHY_DANIELS, arcemu.GOSSIP_EVENT_HELLO, TimothyDaniels_onHello )
arcemu.RegisterUnitGossipEvent( NPCID_TIMOTHY_DANIELS, arcemu.GOSSIP_EVENT_SELECT, TimothyDaniels_onSelect )