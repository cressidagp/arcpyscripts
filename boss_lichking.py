"""
RAID: ICECROWN CITADEL
ENCOUNTER: The Lich King

.npc portto 134324 tirion

"""

import arcemu
import ArcPyMath as Math
from arcemu import Unit
from arcemu import GossipMenu

LK_STATE = {}
LK_TIMER = {}
TF_STATE = {}
TF_TIMER = {}
TM_STATE = {}

CREATUREID_LICH_KING = 36597
CREATUREID_TIRION_FORDRING = 38995
CREATUREID_TERENAS_MENETHIL = 36823

EMOTE_ONESHOT_POINT_NOSHEATHE = 397

SOUNDID_FURY_OF_FROSTMOURNE = 17459

SPELLID_EMOTE_SIT_NO_SHEATH = 73220 # need dummy aura
SPELLID_PLAY_MOVIE = 73159 # need scripted effect
SPELLID_FURY_OF_FROSTMOURNE = 72350 #need dummy aura

#
#
# The Lich King
#
#
def LichKing_onDied( unit, event, killer ):
    unit.castSpell( SPELLID_PLAY_MOVIE, True )

def LichKing_onCombatStart( unit, event, target ):
    print("todo")

def LichKing_onTargetDied( unit, event, target ):
    chance = Math.randomUInt( 1 )
    if chance == 0:
        unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "Hope wanes..." )
        unit.playSoundToSet( 17363 )
        
    else:
       unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "The end has come!" )
       unit.playSoundToSet( 17364 )

def LichKing_DoAction():
    print("todo")

def LichKing_onDamageTaken( unit, event, attacker, amount ):
    health = unit.getHealth()
    maxhealth = unit.getMaxHealth()
    if not ((health - amount) / maxhealth > 70):
        print("todo")

    if not ((health - amount) / maxhealth > 40):
        print("todo")
        
    if not ((health - amount) / maxhealth > 10):
        #reactpassive
        #attackstop
        unit.playSoundToSet( SOUNDID_FURY_OF_FROSTMOURNE )
        unit.castSpell( SPELLID_FURY_OF_FROSTMOURNE, False )
        #setwalk
        
def LichKing_onAIUpdate( unit, event ):
    state = LK_STATE[ unit.getGUID() ]
    timer = LK_TIMER[ unit.getGUID() ]

    if state == 0:
            unit.setSheatState( 1 )
            unit.getAuraBySpellId( SPELLID_EMOTE_SIT_NO_SHEATH ).remove()
            #walk
            #moveto

    elif state == 1:
            print("todo")
    
    elif state == 3:
            print("todo")

    elif state == 4:
            unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "You'll learn of that first hand. When my work is complete, you will beg for mercy -- and I will deny you. Your anguished cries will be testament to my unbridled power..." )
            unit.playSoundToSet( 17350 )

    if state == 99:
            state = 0
    else:
            state = state + 1

    LK_STATE[ unit.getGUID() ] = state

    timer = timer - 1

    LK_TIMER[ unit.getGUID() ] = timer


    
def LichKing_onLoad( unit, event ):
    LK_STATE[ unit.getGUID() ] = 0
    LK_TIMER[ unit.getGUID() ] = 0
    #unit.castSpell(SPELLID_EMOTE_SIT_NO_SHEATH, True)

#
#
# TIRION FORDRING
#
#
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

#
#
# King Terenas Menethil
#
#
def TerenasMenethil_DoAction():
    print("todo")   

def TerenasMenethil_onDamageTaken( unit, event, attacker, amount ):
    print("todo")

def TerenasMenethil_onAIUpdate( unit, event ):
    state = TM_STATE[ unit.getGUID() ]
    print("todo")

def TerenasMenethil_onLoad( unit, event ):
    unit.RegisterAIUpdateEvent( 1000 ) 
#
# Spell: Emote - Seat (No Sheat)
#
def emoteSeatNoSheat_handleDummyAura():
    print("research me")

#
# Spell: Fury of Frostmourne
#
def furyOfFrostmourne_handleDummyAura():
    print("research me")
    
#
# Spell: Play Movie
#
def playMovie_handleScriptedEffect( effectIndex, spell ):
    print("research me")
    
# The Lich King:
arcemu.RegisterUnitEvent( CREATUREID_LICH_KING, arcemu.CREATURE_EVENT_ON_DIED, LichKing_onDied )
arcemu.RegisterUnitEvent( CREATUREID_LICH_KING, arcemu.CREATURE_EVENT_ON_ENTER_COMBAT, LichKing_onCombatStart )
arcemu.RegisterUnitEvent( CREATUREID_LICH_KING, arcemu.CREATURE_EVENT_ON_TARGET_DIED, LichKing_onTargetDied )
arcemu.RegisterUnitEvent( CREATUREID_LICH_KING, arcemu.CREATURE_EVENT_ON_DAMAGE_TAKEN, LichKing_onDamageTaken )
arcemu.RegisterUnitEvent( CREATUREID_LICH_KING, arcemu.CREATURE_EVENT_ON_AIUPDATE, LichKing_onAIUpdate )
arcemu.RegisterUnitEvent( CREATUREID_LICH_KING, arcemu.CREATURE_EVENT_ON_LOAD, LichKing_onLoad )

# Tirion Fordring:
arcemu.RegisterUnitGossipEvent( CREATUREID_TIRION_FORDRING, arcemu.GOSSIP_EVENT_HELLO, TirionFordring_onHello )
arcemu.RegisterUnitGossipEvent( CREATUREID_TIRION_FORDRING, arcemu.GOSSIP_EVENT_SELECT, TirionFordring_onSelectOption )
arcemu.RegisterUnitEvent( CREATUREID_TIRION_FORDRING, arcemu.CREATURE_EVENT_ON_AIUPDATE, TirionFordring_onAIUpdate )
arcemu.RegisterUnitEvent( CREATUREID_TIRION_FORDRING, arcemu.CREATURE_EVENT_ON_LOAD, TirionFordring_onLoad )

# King Terenas Menethil:
arcemu.RegisterUnitEvent( CREATUREID_TERENAS_MENETHIL, arcemu.CREATURE_EVENT_ON_DAMAGE_TAKEN, TerenasMenethil_onDamageTaken )
arcemu.RegisterUnitEvent( CREATUREID_TERENAS_MENETHIL, arcemu.CREATURE_EVENT_ON_AIUPDATE, TerenasMenethil_onAIUpdate )
arcemu.RegisterUnitEvent( CREATUREID_TERENAS_MENETHIL, arcemu.CREATURE_EVENT_ON_LOAD, TerenasMenethil_onLoad )

# Spells:
#arcemu.RegisterDummyAuraHandler( SPELLID_EMOTE_SIT_NO_SHEATH, emoteSeatNoSheat_handleDummyAura )
#arcemu.RegisterDummyAuraHandler( SPELLID_FURY_OF_FROSTMOURNE, furyOfFrostmourne_handleDummyAura )
arcemu.RegisterScriptedEffectHandler( SPELLID_PLAY_MOVIE, playMovie_handleScriptedEffect )