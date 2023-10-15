'''

Engine: APE
Zone: Ghostlands
Creature: Arcanist Vandril
.npc portto 64987

'''

import arcemu
from arcemu import GossipMenu

NPC_ID_ARCANIST_VANDRIL = 16197

def ArcanistVandril_onHello( unit, event, player ):

    menu = GossipMenu( 8417, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.addItem( arcemu.ICON_CHAT, "Arcanist Vandril, what are the Forsaken doing here?", 0, 0 )

    menu.addQuests( unit, player )

    menu.sendToPlayer( player )

def ArcanistVandril_onSelectOption( unit, player, id, enteredCode ):
    
    menu = GossipMenu( 8501, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.sendToPlayer( player )

arcemu.RegisterUnitGossipEvent( NPC_ID_ARCANIST_VANDRIL, arcemu.GOSSIP_EVENT_HELLO, ArcanistVandril_onHello )
arcemu.RegisterUnitGossipEvent( NPC_ID_ARCANIST_VANDRIL, arcemu.GOSSIP_EVENT_SELECT, ArcanistVandril_onSelectOption )