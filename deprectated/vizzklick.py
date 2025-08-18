import arcemu
import ArcPyMath as Math
from arcemu import GossipMenu
from arcemu import Unit

NPC_VIZZKLICK = 6568

def vizzklick_onHello( unit, event, player ):
    
    creature = unit.toCreature()

    creature.addNpcFlag( arcemu.NPC_FLAG_VENDOR )

    menu = GossipMenu( 1933, unit, arcemu.GOSSIP_AUTOSEND_FALSE )
    menu.addItem( arcemu.ICON_CHAT, "I wish to browse your wares.", 1, 0 )
    
    menu.sendToPlayer( player )

def vizzklick_onSelect( unit, player, selection, enteredCode ):

    creature = unit.toCreature()
    #creature.addNpcFlag( arcemu.NPC_FLAG_VENDOR )
    
    if id == 1:
        creature.addNpcFlag( arcemu.NPC_FLAG_VENDOR )
        session = player.getSession()
        session.sendInventoryList( creature )
        
    #menu = GossipMenu( 1934, unit, arcemu.GOSSIP_AUTOSEND_FALSE )
    #menu.sendToPlayer( player )


arcemu.RegisterUnitGossipEvent( 6568, arcemu.GOSSIP_EVENT_HELLO, vizzklick_onHello )
arcemu.RegisterUnitGossipEvent( 6568, arcemu.GOSSIP_EVENT_SELECT, vizzklick_onSelect )


'''
import arcemu
from arcemu import GossipMenu
from arcemu import GossipScript
from arcemu import Player
from arcemu import Unit

NPC_VIZZKLICK = 6568

class VizzclickGossip( GossipScript ):
    def __init__( self ):
        GossipScript.__init__( self )

    def OnHello( self, object, player ):
        creature = arcemu.toCreature( object )
        menu = GossipMenu( 1933, object, arcemu.GOSSIP_AUTOSEND_FALSE )
        menu.addItem( arcemu.ICON_CHAT, "I wish to browse your wares.", 1, 0 )
        menu.sendToPlayer( player )

    def OnSelectOption( self, object, player, id, enteredCode ):
        if id == 1:
            session = player.getSession()
            session.sendInventoryList( creature )

arcemu.RegisterCreatureGossipScript( NPC_VIZZKLICK, VizzclickGossip() )'''