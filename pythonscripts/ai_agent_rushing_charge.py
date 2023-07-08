import arcemu
from arcemu import Unit

def castRushingCharge_onCombatStart( unit, event, target ):
	unit.castSpell( 6268, False )

# Bloodtallon Taillasher:	
arcemu.RegisterUnitEvent( 3122, arcemu.CREATURE_EVENT_ON_ENTER_COMBAT, castRushingCharge_onCombatStart )

# Bloodtalon Scythemaw:
arcemu.RegisterUnitEvent( 3123, arcemu.CREATURE_EVENT_ON_ENTER_COMBAT, castRushingCharge_onCombatStart )

# Corrupted Bloodtalon Scythemaw:
arcemu.RegisterUnitEvent( 3227, arcemu.CREATURE_EVENT_ON_ENTER_COMBAT, castRushingCharge_onCombatStart )