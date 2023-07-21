'''

Engine: APE
Zone: Teldrassil
Creature: Jenal

'''

import arcemu
from arcemu import GossipMenu

NPC_ID_JENAL = 9047

def Jenal_onHello( unit, event, player ):

    menu = GossipMenu( 2313, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.addItem( arcemu.ICON_CHAT, "What are you doing out here?", 1, 0 )
    menu.addQuests( unit, player )

    menu.sendToPlayer( player )

def Jenal_onSelectOption( unit, player, id, enteredCode ):

    menu = GossipMenu( 2314, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.sendToPlayer( player )

arcemu.RegisterUnitGossipEvent( NPC_ID_JENAL, arcemu.GOSSIP_EVENT_HELLO, Jenal_onHello )
arcemu.RegisterUnitGossipEvent( NPC_ID_JENAL, arcemu.GOSSIP_EVENT_SELECT, Jenal_onSelectOption )