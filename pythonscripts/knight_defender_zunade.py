'''

Engine: APE
Zone: Bloodmyst Isle
Creature: Knight Defender Zunade
.npc portto 74750

'''

import arcemu
from arcemu import GossipMenu

NPC_ID_K_D_ZUNADE = 18030

def KnightDefenderZunade_onHello( unit, event, player ):

    menu = GossipMenu( 9172, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.addItem( arcemu.ICON_CHAT, "Tell me about the Defenders.", 0, 0 )

    menu.sendToPlayer( player )

def KnightDefenderZunade_onSelectOption( unit, player, id, enteredCode ):

    menu = GossipMenu( 9206, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.sendToPlayer( player )

arcemu.RegisterUnitGossipEvent( NPC_ID_K_D_ZUNADE, arcemu.GOSSIP_EVENT_HELLO, KnightDefenderZunade_onHello )
arcemu.RegisterUnitGossipEvent( NPC_ID_K_D_ZUNADE, arcemu.GOSSIP_EVENT_SELECT, KnightDefenderZunade_onSelectOption )