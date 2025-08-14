import arcemu
from arcemu import Unit

SPELLID_STONEFORM = 70733

#EMOTE_STATE_CUSTOM_SPELL_02 = 417

#OBJECT_END = 0x0006
#UNIT_FIELD_FLAGS = 0x0035
#UNIT_FLAG_NOT_ATTACKABLE_9 = 0x00000100
#UNIT_FLAG_NOT_SELECTABLE = 0x02000000

def ICC_Stoneform_handleAura( i, aura, apply ):
	target = aura.getTarget()
	
	if apply:
		target.setEmoteState( 417 )
		target.setUInt32Value( 0x0006 + 0x0035, 0x00000100 + 0x02000000 )

	else:
		target.setEmoteState( arcemu.EMOTE_ONESHOT_NONE )
		target.setUInt32Value( 0x0006 + 0x0035, 0 )
		
arcemu.RegisterDummyAuraHandler( SPELLID_STONEFORM, ICC_Stoneform_handleAura )