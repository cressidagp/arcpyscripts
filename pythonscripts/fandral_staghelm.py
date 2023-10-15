'''

Engine: APE
Zone: Teldrassil
Creature: Arch Druid Fandral Staghelm
.npc portto 28680

'''

import arcemu
from arcemu import GossipMenu

NPC_ID_FANDRAL_STAGHELM = 3516

def FandralStaghelm_onHello( unit, event, player ):

    menu = GossipMenu( 2285, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.addItem( arcemu.ICON_CHAT, "I'm not a journeyman herbalist -- am I able to still assist you in your work?", 0, 0 )
    
    menu.addQuests( unit, player )

    menu.sendToPlayer( player )

def FandralStaghelm_onSelectOption( unit, player, id, enteredCode ):

    if id == 0:

        menu = GossipMenu( 2320, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

        menu.sendToPlayer( player )

arcemu.RegisterUnitGossipEvent( NPC_ID_FANDRAL_STAGHELM, arcemu.GOSSIP_EVENT_HELLO, FandralStaghelm_onHello )
arcemu.RegisterUnitGossipEvent( NPC_ID_FANDRAL_STAGHELM, arcemu.GOSSIP_EVENT_SELECT, FandralStaghelm_onSelectOption )