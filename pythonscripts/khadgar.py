'''

Engine: APE
Zone: Shattrath City
Creature: Khadgar
.npc portto 75998

'''

import arcemu
from arcemu import GossipMenu

KHADGAR_GOSSIPS = [ 9243, 9876, 9877, 9878, 9879, 9880, 9881 ]

KHADGAR_OPTIONS = [
"I've heard your name spoken only in whispers, mage.  Who are you?",
"Go on, please.",
"I see.",
"What did you do then?",
"What happened next?",
"I see.",
"There was something else I wanted to ask you."
]

KHADGAR_ID = 18166

def khadgar_onHello( unit, event, player ):

    menu = GossipMenu( KHADGAR_GOSSIPS[ 0 ], unit, arcemu.GOSSIP_AUTOSEND_FALSE )

    menu.addItem( arcemu.ICON_CHAT, KHADGAR_OPTIONS[ 0 ], 0, 0 )

    menu.sendToPlayer( player )

def khadgar_onSelectOption( unit, player, id, enteredCode ):

    if id == 0:

        menu = GossipMenu( KHADGAR_GOSSIPS[ 1 ], unit, arcemu.GOSSIP_AUTOSEND_FALSE )

        menu.addItem( arcemu.ICON_CHAT, KHADGAR_OPTIONS[ 1 ], 1, 0 )

        menu.sendToPlayer( player )

    if id == 1:

        menu = GossipMenu( KHADGAR_GOSSIPS[ 2 ], unit, arcemu.GOSSIP_AUTOSEND_FALSE )

        menu.addItem( arcemu.ICON_CHAT, KHADGAR_OPTIONS[ 2 ], 2, 0 )

        menu.sendToPlayer( player )

    if id == 2:

        menu = GossipMenu( KHADGAR_GOSSIPS[ 3 ], unit, arcemu.GOSSIP_AUTOSEND_FALSE )

        menu.addItem( arcemu.ICON_CHAT, KHADGAR_OPTIONS[ 3 ], 3, 0 )

        menu.sendToPlayer( player )

    if id == 3:

        menu = GossipMenu( KHADGAR_GOSSIPS[ 4 ], unit, arcemu.GOSSIP_AUTOSEND_FALSE )

        menu.addItem( arcemu.ICON_CHAT, KHADGAR_OPTIONS[ 4 ], 4, 0 )

        menu.sendToPlayer( player )

    if id == 4:

        menu = GossipMenu( KHADGAR_GOSSIPS[ 5 ], unit, arcemu.GOSSIP_AUTOSEND_FALSE )

        menu.addItem( arcemu.ICON_CHAT, KHADGAR_OPTIONS[ 5 ], 5, 0 )

        menu.sendToPlayer( player )

    if id == 5:

        menu = GossipMenu( KHADGAR_GOSSIPS[ 6 ], unit, arcemu.GOSSIP_AUTOSEND_FALSE )

        menu.addItem( arcemu.ICON_CHAT, KHADGAR_OPTIONS[ 6 ], 6, 0 )

        menu.sendToPlayer( player )

    if id == 6:

        menu = GossipMenu( KHADGAR_GOSSIPS[ 0 ], unit, arcemu.GOSSIP_AUTOSEND_FALSE )

        menu.addItem( arcemu.ICON_CHAT, KHADGAR_OPTIONS[ 0 ], 0, 0 )

        menu.sendToPlayer( player )

arcemu.RegisterUnitGossipEvent( KHADGAR_ID, arcemu.GOSSIP_EVENT_HELLO, khadgar_onHello )
arcemu.RegisterUnitGossipEvent( KHADGAR_ID, arcemu.GOSSIP_EVENT_SELECT, khadgar_onSelectOption )