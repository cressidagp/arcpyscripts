import arcemu
from arcemu import Unit

TM_STATE = {}
TM_TIMER = {}

CREATUREID_TERENAS_MENETHIL = 36823

def TerenasMenethil_DoAction():
    print("todo")   

def TerenasMenethil_onDamageTaken( unit, event, attacker, amount ):
    print("todo")

def TerenasMenethil_onAIUpdate( unit, event ):
    state = TM_STATE[ unit.getGUID() ]
    print("todo")

def TerenasMenethil_onLoad( unit, event ):
    unit.RegisterAIUpdateEvent( 1000 )

arcemu.RegisterUnitEvent( CREATUREID_TERENAS_MENETHIL, arcemu.CREATURE_EVENT_ON_DAMAGE_TAKEN, TerenasMenethil_onDamageTaken )
arcemu.RegisterUnitEvent( CREATUREID_TERENAS_MENETHIL, arcemu.CREATURE_EVENT_ON_AIUPDATE, TerenasMenethil_onAIUpdate )
arcemu.RegisterUnitEvent( CREATUREID_TERENAS_MENETHIL, arcemu.CREATURE_EVENT_ON_LOAD, TerenasMenethil_onLoad )