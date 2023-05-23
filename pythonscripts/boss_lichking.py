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
#phase 2
LK_SummonV  = {}
LK_Defile   = {}
LK_SoulR    = {}

CREATUREID_LICH_KING = 36597

#change this to enum?
LK_PHASE_INTRO  = 1
LK_PHASE_ONE    = 2
LK_PHASE_TWO    = 3
LK_PHASE_THREE  = 4

SPELLID_SUMMON_SHAMBLING_HORROR = 70372
SPELLID_SUMMON_DRUDGE_GHOULS    = 70358
SPELLID_INFEST                  = 70541
SPELLID_NECROTIC_PLAGUE         = 70337
SPELLID_SHADOW_TRAP             = 73539 # need a dummy aura
SPELLID_BERSERK2                = 47008

SPELLID_SUMMON_VALKYR           = 69037 # need vehicle fix?
SPELLID_DEFILE                  = 72762
SPELLID_SOUL_REAPER             = 69409

SPELLID_EMOTE_SIT_NO_SHEATH = 73220 # need dummy aura
SPELLID_PLAY_MOVIE          = 73159 # need scripted effect
SPELLID_FURY_OF_FROSTMOURNE = 72350 #need dummy aura

SOUNDID_LK_BERSERK          = 17365
SOUNDID_LK_SUMMON_VALKYR    = 17373
SOUNDID_MUSIC_FROZEN_THRONE = 17457
SOUNDID_MUSIC_SPECIAL       = 17458
SOUNDID_FURY_OF_FROSTMOURNE = 17459

CHAT_MSG_RAID_WARNING_WIDESCREEN    = 41
CHAT_MSG_RAID_BOSS_EMOTE            = 42

def LichKing_onDied( unit, event, killer ):
    unit.castSpell( SPELLID_PLAY_MOVIE, True )

def LichKing_onCombatStart( unit, event, target ):
    lkguid = unit.getGUID()
    LK_PHASE[ lkguid ] = LK_PHASE_ONE
    LK_SummonSH[ lkguid ] = 20
    LK_SummonDG[ lkguid ] = 10
    LK_Infest[ lkguid ] = 5
    LK_NecroP[ lkguid ] = 33 #Math.randomUInt( 30, 33 )
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
    #summonsh = LK_SummonSH[ lkguid ]
    #summondg = LK_SummonDG[ lkguid ]
    #infest = LK_Infest[ lkguid ]
    #necrop = LK_NecroP[ lkguid ]
    #berserk = LK_Berserk[ lkguid ]
    #shadowt = LK_ShadowT[ lkguid ]

    if phase == LK_PHASE_INTRO and state == 0:
        unit.setSheatState( 1 )
        #aura = unit.getAuraBySpellId( SPELLID_EMOTE_SIT_NO_SHEATH )
        #aura.remove()
        creature = unit.toCreature()
        #walk
        creature.moveTo( 432.0851, -2123.673, 1063.45, 0.0 )

    elif phase == LK_PHASE_INTRO and state == 1:
        creature = unit.toCreature()
        creature.moveTo( 457.835, -2123.426, 1040.88, 0.0 )
            
    elif phase == LK_PHASE_INTRO and state == 2:
        creature = unit.toCreature()
        creature.moveTo( 465.0730, -2123.470, 1040.85, 0.0 )
        unit.ModifyAIUpdateEvent( 9000 )

    elif phase == LK_PHASE_INTRO and state == 3:
        unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_UNIVERSAL, "You'll learn of that first hand. When my work is complete, you will beg for mercy -- and I will deny you. Your anguished cries will be testament to my unbridled power..." )
        unit.playSoundToSet( 17350 )
        unit.ModifyAIUpdateEvent( 1000 )

    elif phase == LK_PHASE_ONE and LK_SummonSH[ lkguid ] <= 0:
        unit.playSoundToSet( SOUNDID_MUSIC_SPECIAL )
        unit.castSpell( SPELLID_SUMMON_SHAMBLING_HORROR, False )
        LK_SummonSH[ lkguid ] = 60

    elif phase == LK_PHASE_ONE and LK_SummonDG[ lkguid ] <= 0:
        unit.castSpell( SPELLID_SUMMON_DRUDGE_GHOULS, False )
        LK_SummonDG[ lkguid ] = 30
        
    elif ( phase == LK_PHASE_ONE or phase == LK_PHASE_TWO ) and LK_Infest[ lkguid ] <= 0:
        unit.castSpell( SPELLID_INFEST, False )
        LK_Infest[ lkguid ] = 24

    elif phase == LK_PHASE_ONE and LK_NecroP[ lkguid ] <= 0:
        #unit.sendChatMessage( CHAT_MSG_RAID_BOSS_EMOTE, arcemu.LANG_UNIVERSAL, "|TInterface\Icons\ability_creature_disease_02.blp:16|t You have been infected by |cFFBC05FFNecrotic Plague|r! |TInterface\Icons\ability_creature_disease_02.blp:16|t" )
        creature = unit.toCreature()
        tank = creature.getMostHated()
        if tank is not None:
            unit.castSpell( SPELLID_NECROTIC_PLAGUE, True, tank )
            LK_NecroP[ lkguid ] = 33 #Math.randomUInt( 30, 33 )

    elif phase == LK_PHASE_ONE and LK_Berserk[ lkguid ] <= 0:
        unit.playSoundToSet( SOUNDID_LK_BERSERK )
        unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, "Face now your tragic end." )
        unit.castSpell( SPELLID_BERSERK2, True )
        LK_Berserk[ lkguid ] = 1000 * 15

    elif phase == LK_PHASE_ONE and LK_ShadowT[ lkguid ] <= 0:
        creature = unit.toCreature()
        tank = creature.getMostHated()
        if tank is not None:
            unit.castSpell( SPELLID_SHADOW_TRAP, False, tank )
            LK_ShadowT[ lkguid ] = 15

    elif phase == LK_PHASE_TWO and LK_SummonV[ lkguid ] <= 0:
        unit.playSoundToSet( SOUNDID_MUSIC_SPECIAL )
        unit.sendChatMessage( arcemu.CHAT_MSG_MONSTER_YELL, arcemu.LANG_UNIVERSAL, "Val'kyr, your master calls!" )
        unit.playSoundToSet( SOUNDID_LK_SUMMON_VALKYR )
        unit.castSpell( SPELLID_SUMMON_VALKYR, True )
        LK_SummonV[ lkguid ] = 50 #Math.randomUInt( 48, 50 )

    elif ( phase == LK_PHASE_TWO or phase == LK_PHASE_THREE ) and LK_Defile[ lkguid ] <= 0:
        unit.sendChatMessage( CHAT_MSG_RAID_WARNING_WIDESCREEN, arcemu.LANG_UNIVERSAL, "%s begins to cast Defile!" )
        creature = unit.toCreature()
        tank = creature.getMostHated()
        if tank is not None:
            unit.castSpell( SPELLID_DEFILE, False, tank )
            LK_Defile[ lkguid ] = 35# Math.randomUInt( 32, 35 )

    elif ( phase == LK_PHASE_TWO or phase == LK_PHASE_THREE ) and LK_SoulR[ lkguid ] <= 0:
        creature = unit.toCreature()
        tank = creature.getMostHated()
        if tank is not None:
            unit.castSpell( SPELLID_SOUL_REAPER, True, tank )
            LK_SoulR[ lkguid ] = 35# Math.randomUInt( 33, 35 )

    lkguid = unit.getGUID()

    if LK_SummonSH[ lkguid ] != None:
        LK_SummonSH[ lkguid ] = LK_SummonSH[ lkguid ] - 1
    
    if LK_SummonDG[ lkguid ] != None:
        LK_SummonDG[ lkguid ] = LK_SummonDG[ lkguid ] - 1

    if LK_Infest[ lkguid ] != None:
        LK_Infest[ lkguid ] = LK_Infest[ lkguid ] - 1

    if LK_NecroP[ lkguid ] != None:
        LK_NecroP[ lkguid ] = LK_NecroP[ lkguid ] - 1
    
    if LK_Berserk[ lkguid ] != None:
        LK_Berserk[ lkguid ] = LK_Berserk[ lkguid ] - 1

    if LK_ShadowT[ lkguid ] != None:    
        LK_ShadowT[ lkguid ] = LK_ShadowT[ lkguid ] - 1

    if LK_SummonV[ lkguid ] != None:
        LK_SummonV[ lkguid ] = LK_SummonV[ lkguid ] - 1

    if LK_Defile[ lkguid ] != None:
        LK_Defile[ lkguid ] = LK_Defile[ lkguid ] - 1

    if LK_SoulR[ lkguid ] != None:
        LK_SoulR[ lkguid ] = LK_SoulR[ lkguid ] - 1

    if state == 99:
            state = 0
    else:
            state = state + 1
            print(state)

    LK_STATE[ unit.getGUID() ] = state
   
def LichKing_onLoad( unit, event ):
    lkguid = unit.getGUID()
    LK_PHASE[ lkguid ] = 1
    LK_STATE[ lkguid ] = 0
    #initialize phase 1 timers:
    LK_SummonSH[ lkguid ] = None
    LK_SummonDG[ lkguid ] = None
    LK_Infest[ lkguid ] = None
    LK_NecroP[ lkguid ] = None
    LK_Berserk[ lkguid ] = None
    LK_ShadowT[ lkguid ] = None
    #initialize phase 2 timers:
    LK_SummonV[ lkguid ] = None
    LK_Defile[ lkguid ] = None
    LK_SoulR[ lkguid ] = None
    unit.castSpell( SPELLID_EMOTE_SIT_NO_SHEATH, True )
    unit.RegisterAIUpdateEvent( 1000 )
    #creature = unit.toCreature()
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