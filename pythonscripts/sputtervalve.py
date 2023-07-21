'''

Engine: APE
Zone: Barrens
Creature: Sputtervalve

'''

import arcemu
from arcemu import GossipMenu

NPC_ID_SPUTTERVALVE = 3442

def Sputtervalve_onHello( unit, event, player ):

    menu = GossipMenu( 519, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.addItem( arcemu.ICON_CHAT, "How can I help?", 1, 0 )
    menu.addQuests( unit, player )

    menu.sendToPlayer( player )

def Sputtervalve_onSelectOption( unit, player, id, enteredCode ):

    menu = GossipMenu( 518, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.sendToPlayer( player )


arcemu.RegisterUnitGossipEvent( NPC_ID_SPUTTERVALVE, arcemu.GOSSIP_EVENT_HELLO, Sputtervalve_onHello )
arcemu.RegisterUnitGossipEvent( NPC_ID_SPUTTERVALVE, arcemu.GOSSIP_EVENT_SELECT, Sputtervalve_onSelectOption )