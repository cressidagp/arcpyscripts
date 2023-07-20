import arcemu
import ArcPyMath as Math
from arcemu import Unit
from arcemu import GossipMenu

TF_STATE = {}
TF_TIMER = {}

CREATUREID_TIRION_FORDRING = 38995

def TirionFordring_DoAction():
    print("todo")
       
def TirionFordring_onAIUpdate( unit, event ):
    state = TF_STATE[ unit.getGUID() ]
    timer = TF_TIMER[ unit.getGUID() ]
    
    if state == 0:
        unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "We'll grant you a swift death, Arthas. More than can be said for the thousands you've tortured and slain." )
        unit.playSoundToSet( 17390 )
        TF_TIMER[ unit.getGUID() ] = 2
        
    elif state == 1 and timer <= 0:
        unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "test2" )
        unit.emote( EMOTE_ONESHOT_POINT_NOSHEATHE, 0 )
        TF_TIMER[ unit.getGUID() ] = 3
        
    elif state == 3 and timer <= 0:
        #walk
        #move to
        unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "test3" )
        TF_TIMER[ unit.getGUID() ] = 20
        
        
    if state == 99:
            state = 0
    else:
            state = state + 1
            
    TF_STATE[ unit.getGUID() ] = state
    
    timer = timer - 1
    
    TF_TIMER[ unit.getGUID() ] = timer
           
def TirionFordring_onHello( unit, event, player ):
	
	creature = unit.toCreature()
	
	menu = GossipMenu( 15290, unit, arcemu.GOSSIP_AUTOSEND_FALSE )
	
	menu.addItem( arcemu.ICON_CHAT, "We are prepared, Highlord. Let us battle for the fate of Azeroth! For the light of dawn!", 1, 0 )
	menu.sendToPlayer( player )
    
def TirionFordring_onSelectOption( unit, player, id, enteredCode ):

    GossipMenu.complete( player )
    unit.RegisterAIUpdateEvent( 1000 )    
    creature = unit.toCreature()
	
    if id == 1:
            creature.removeNpcFlag( arcemu.NPC_FLAG_GOSSIP )
            creature.setMovementType( arcemu.MOVEMENTTYPE_FORWARDTHENSTOP )

def TirionFordring_onLoad( unit, event ):
    TF_STATE[ unit.getGUID() ] = 0
    TF_TIMER[ unit.getGUID() ] = 0
    #unit.RegisterAIUpdateEvent( 1000 )
    creature = unit.toCreature()
    creature.setMovementType( arcemu.MOVEMENTTYPE_DONTMOVEWP )
    creature.resetWaypoint()
    creature.destroyCustomWaypoints()
    creature.createCustomWaypoint( 489.2970, -2124.840, 840.8569, 0.0, 250, arcemu.WAYPOINT_FLAG_WALK, 0 )  

arcemu.RegisterUnitGossipEvent( CREATUREID_TIRION_FORDRING, arcemu.GOSSIP_EVENT_HELLO, TirionFordring_onHello )
arcemu.RegisterUnitGossipEvent( CREATUREID_TIRION_FORDRING, arcemu.GOSSIP_EVENT_SELECT, TirionFordring_onSelectOption )
arcemu.RegisterUnitEvent( CREATUREID_TIRION_FORDRING, arcemu.CREATURE_EVENT_ON_AIUPDATE, TirionFordring_onAIUpdate )
arcemu.RegisterUnitEvent( CREATUREID_TIRION_FORDRING, arcemu.CREATURE_EVENT_ON_LOAD, TirionFordring_onLoad )