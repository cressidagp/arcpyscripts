import arcemu
from arcemu import Unit

def castBoarCharge_onCombatStart( unit, event, target ):
	unit.castSpell( 3385, False )

# Dire Mottled Boar:	
arcemu.RegisterUnitEvent( 3099, arcemu.CREATURE_EVENT_ON_ENTER_COMBAT, castBoarCharge_onCombatStart )

# Elder Mottled Boar:
arcemu.RegisterUnitEvent( 3100, arcemu.CREATURE_EVENT_ON_ENTER_COMBAT, castBoarCharge_onCombatStart )

# Corrupted Mottled Boar:
arcemu.RegisterUnitEvent( 3225, arcemu.CREATURE_EVENT_ON_ENTER_COMBAT, castBoarCharge_onCombatStart )