'''

Engine: APE
Zone: Stormwind City, Tirisfall Glades
Creature: Ian Drake, Edward Cain

'''

import arcemu
import ArcPyMath as Math
from arcemu import GossipMenu
from arcemu import Unit

ELDERS_TEXTS = [
"You're secret code is not a valid one...",
"I would like to whisper my secret code to you to receive Tyrael's Hilt."
]

NPC_ID_IAN_DRAKE = 29093
NPC_ID_EDWARD_CAIN = 29095
ITEM_ID_TYRAELS_HILT = 39656

def elders_onHello( unit, event, player ):

    menu = GossipMenu( 13441, unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.addItem( arcemu.ICON_CHAT, ELDERS_TEXTS[ event ], 0, 1 )

    menu.sendToPlayer( player )

def elders_onSelectOption( unit, player, id, enteredCode ):

    if id == 0:

        if enteredCode == '69':

            player.addItem( ITEM_ID_TYRAELS_HILT, 1 )

        else:
             unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, ELDERS_TEXTS[ 0 ] )

        GossipMenu.complete( player )
            
arcemu.RegisterUnitGossipEvent( NPC_ID_IAN_DRAKE, arcemu.GOSSIP_EVENT_HELLO, elders_onHello )
arcemu.RegisterUnitGossipEvent( NPC_ID_IAN_DRAKE, arcemu.GOSSIP_EVENT_SELECT, elders_onSelectOption )
arcemu.RegisterUnitGossipEvent( NPC_ID_EDWARD_CAIN, arcemu.GOSSIP_EVENT_HELLO, elders_onHello )
arcemu.RegisterUnitGossipEvent( NPC_ID_EDWARD_CAIN, arcemu.GOSSIP_EVENT_SELECT, elders_onSelectOption )