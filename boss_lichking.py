"""
RAID: ICECROWN CITADEL
ENCOUNTER: The Lich King

.npc portto 134324 tirion

"""
import arcemu
import ArcPyMath as Math
from arcemu import Unit

LK_STATE    = {}
LK_PHASE    = {}
#phase 1 timers... how to store all in one?
LK_SummonSH = {}
LK_SummonDG = {}
LK_Infest   = {}
LK_NecroP   = {}
LK_Berserk  = {}
LK_ShadowT  = {}

#change this to enum?
LK_PHASE_INTRO  = 1
LK_PHASE_ONE    = 2
LK_PHASE_TWO    = 3

CREATUREID_LICH_KING = 36597

SOUNDID_MUSIC_FROZEN_THRONE = 17457
SOUNDID_FURY_OF_FROSTMOURNE = 17459

SPELLID_SUMMON_SHAMBLING_HORROR = 70372
SPELLID_SUMMON_DRUDGE_GHOULS    = 70358
SPELLID_INFEST                  = 70541
SPELLID_NECROTIC_PLAGUE         = 70337
SPELLID_SHADOW_TRAP             = 73539 # need a dummy aura
SPELLID_BERSERK2                = 47008

SPELLID_EMOTE_SIT_NO_SHEATH = 73220 # need dummy aura
SPELLID_PLAY_MOVIE          = 73159 # need scripted effect
SPELLID_FURY_OF_FROSTMOURNE = 72350 #need dummy aura

def LichKing_onDied( unit, event, killer ):
    unit.castSpell( SPELLID_PLAY_MOVIE, True )

def LichKing_onCombatStart( unit, event, target ):
    lkguid = unit.getGUID()
    LK_PHASE[ lkguid ] = LK_PHASE_ONE
    LK_SummonSH[ lkguid ] = 20
    LK_SummonDG[ lkguid ] = 10
    LK_Infest[ lkguid ] = 5
    LK_NecroP[ lkguid ] = Math.randomUInt( 30, 33 )
    LK_Berserk[ lkguid ] = 1000 * 15
    LK_ShadowT[ lkguid ] = 15


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
        #unit.LichKing_doAction( 1 )
        unit.ModifyAIUpdateEvent( 100 )

    elif wpid == 2:
        unit.ModifyAIUpdateEvent( 100 )

    elif wpid == 3:
        unit.ModifyAIUpdateEvent( 9000 )

def LichKing_doAction( action, unit ):
    if action == 1:
        unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "So the Light's vaunted justice has finally arrived? Shall I lay down Frostmourne and throw myself at your mercy, Fordring?" )
        unit.playSoundToSet( 17349 )
        #unit.playSoundToSet( SOUNDID_MUSIC_FROZEN_THRONE )

    elif action == 2:
         print(action)

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
    lkguid = unit.getGUID()
    phase = LK_PHASE[ lkguid ]
    state = LK_STATE[ lkguid ]

    if state == 0 and phase == LK_PHASE_INTRO:
        unit.setSheatState( 1 )
        unit.getAuraBySpellId( SPELLID_EMOTE_SIT_NO_SHEATH ).remove()
        creature = unit.toCreature()
        #walk
        creature.moveTo( 432.0851, -2123.673, 864.6582, 0.0 )

    elif state == 1 and phase == LK_PHASE_INTRO:
        creature.moveTo( 457.835, -2123.426, 841.1582, 0.0 )
            
    elif state == 3 and phase == LK_PHASE_INTRO:
        creature.moveTo( 465.0730, -2123.470, 840.8569, 0.0 )

    elif state == 4 and phase == LK_PHASE_INTRO:
        unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "You'll learn of that first hand. When my work is complete, you will beg for mercy -- and I will deny you. Your anguished cries will be testament to my unbridled power..." )
        unit.playSoundToSet( 17350 )
        unit.ModifyAIUpdateEvent( 1000 )

    elif LK_SummonSH[ lkguid ] <= 0 and phase == LK_PHASE_ONE:
        unit.castSpell( SPELLID_SUMMON_SHAMBLING_HORROR, False )
        LK_SummonSH[ lkguid ] = 60

    elif LK_SummonDG[ lkguid ] <= 0 and phase == LK_PHASE_ONE:
        unit.castSpell( SPELLID_SUMMON_DRUDGE_GHOULS, False )
        LK_SummonDG[ lkguid ] = 30
        
    elif LK_Infest[ lkguid ] <= 0 and ( phase == LK_PHASE_ONE or phase == LK_PHASE_TWO ):
        unit.castSpell( SPELLID_INFEST, False )
        LK_Infest[ lkguid ] = 24

    elif LK_NecroP[ lkguid ] <= 0 and phase == LK_PHASE_ONE:
        creature = unit.toCreature()
        tank = creature.getMostHated()
        if tank is not None:
            unit.castSpell( SPELLID_NECROTIC_PLAGUE, True, tank )
            LK_NecroP[ lkguid ] = Math.randomUInt( 30, 33 )

    elif LK_Berserk[ lkguid ] <= 0 and phase == LK_PHASE_ONE:
        unit.castSpell( SPELLID_BERSERK2, True )
        LK_Berserk[ lkguid ] = 1000 * 15

    elif LK_ShadowT[ lkguid ] <= 0 and phase == LK_PHASE_ONE:
        creature = unit.toCreature()
        tank = creature.getMostHated()
        if tank is not None:
            unit.castSpell( SPELLID_SHADOW_TRAP, False, tank )
            LK_ShadowT[ lkguid ] = 15

    lkguid = unit.getGUID()
    LK_SummonSH[ lkguid ] = LK_SummonSH[ lkguid ] - 1
    LK_SummonDG[ lkguid ] = LK_SummonDG[ lkguid ] - 1
    LK_Infest[ lkguid ] = LK_Infest[ lkguid ] - 1
    LK_NecroP[ lkguid ] = LK_NecroP[ lkguid ] - 1
    LK_Berserk[ lkguid ] = LK_Berserk[ lkguid ] - 1
    LK_ShadowT[ lkguid ] = LK_ShadowT[ lkguid ] - 1

    if state == 99:
            state = 0
    else:
            state = state + 1
            print(state)

    LK_STATE[ unit.getGUID() ] = state
   
def LichKing_onLoad( unit, event ):
    LK_PHASE[ unit.getGUID() ] = 1
    LK_STATE[ unit.getGUID() ] = 0
    LK_TIMER[ unit.getGUID() ] = 0
    unit.castSpell( SPELLID_EMOTE_SIT_NO_SHEATH, True )
    unit.RegisterAIUpdateEvent( 1000 )
    creature = unit.toCreature()
    #creature.setMovementType( arcemu.MOVEMENTTYPE_DONTMOVEWP )
    #creature.resetWaypoint()
    #creature.destroyCustomWaypoints()
    #creature.createCustomWaypoint( 432.0851, -2123.673, 864.6582, 0.0, 250, arcemu.WAYPOINT_FLAG_WALK, 0 )
    #creature.createCustomWaypoint( 457.835, -2123.426, 841.1582, 0.0, 250, arcemu.WAYPOINT_FLAG_WALK, 0 )
    #creature.createCustomWaypoint( 465.0730, -2123.470, 840.8569, 0.0, 250, arcemu.WAYPOINT_FLAG_WALK, 0 )
 
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