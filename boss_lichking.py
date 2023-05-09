"""
RAID: ICECROWN CITADEL
ENCOUNTER: The Lich King

.npc portto 134324 tirion

"""

import arcemu
import ArcPyMath as Math
from arcemu import Unit

LK_STATE = {}
LK_TIMER = {}

CREATUREID_LICH_KING = 36597

SOUNDID_MUSIC_FROZEN_THRONE = 17457
SOUNDID_FURY_OF_FROSTMOURNE = 17459

SPELLID_EMOTE_SIT_NO_SHEATH = 73220 # need dummy aura
SPELLID_PLAY_MOVIE = 73159 # need scripted effect
SPELLID_FURY_OF_FROSTMOURNE = 72350 #need dummy aura

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

def LichKing_onReachWP( unit, event, wpid, foward ):
    if wpid == 1:
        unit.doAction( 1 )

def LichKing_doAction( action, unit ):
    if action == 1:
         unit.playSoundToSet( SOUNDID_MUSIC_FROZEN_THRONE )

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
arcemu.RegisterUnitEvent( CREATUREID_LICH_KING, arcemu.CREATURE_EVENT_ON_REACH_WP, LichKing_onReachWP )
arcemu.RegisterUnitEvent( CREATUREID_LICH_KING, arcemu.CREATURE_EVENT_ON_DAMAGE_TAKEN, LichKing_onDamageTaken )
arcemu.RegisterUnitEvent( CREATUREID_LICH_KING, arcemu.CREATURE_EVENT_ON_AIUPDATE, LichKing_onAIUpdate )
arcemu.RegisterUnitEvent( CREATUREID_LICH_KING, arcemu.CREATURE_EVENT_ON_LOAD, LichKing_onLoad )

# Spells:
#arcemu.RegisterDummyAuraHandler( SPELLID_EMOTE_SIT_NO_SHEATH, emoteSeatNoSheat_handleDummyAura )
#arcemu.RegisterDummyAuraHandler( SPELLID_FURY_OF_FROSTMOURNE, furyOfFrostmourne_handleDummyAura )
arcemu.RegisterScriptedEffectHandler( SPELLID_PLAY_MOVIE, playMovie_handleScriptedEffect )