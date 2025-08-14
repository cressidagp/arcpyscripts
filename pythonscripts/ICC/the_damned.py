import arcemu
from arcemu import CreatureScript

NPCID_THE_DAMNED = 37011
SPELLID_SHATTERED_BONES = 70961
SPELLID_BONE_FLURRY = 70960

class TheDamnedCreatureScript( CreatureScript ):
	def __init__( self, unit ):
		CreatureScript.__init__( self, unit )
		
	def OnDied( self, killer ):
		self.creature.castSpell( SPELLID_SHATTERED_BONES, True )
		
	def OnDamageTaken( self, attacker, amount ):
		if self.getHealth() / self.getMaxHealth() <= 30:
			self.creature.castSpell( SPELLID_BONE_FLURRY )
	
	@staticmethod
	def create( unit ):
		return TheDamnedCreatureScript( unit )
		
#arcemu.RegisterCreatureScript( NPCID_THE_DAMNED, TheDamnedCreatureScript.create )