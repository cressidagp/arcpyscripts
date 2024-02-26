'''
 
Engine: APE
Zone: EF
Creature: Supervisor Raelen
.npc portto 53868
 
'''

import arcemu
import ArcPyMath as Math
#from arcemu import ObjectLocator
from arcemu import CreatureScript


RAELEN_TEXTS = [
"We have yet to meet our quota for the wood demand. Now back to work with you.",
"Daylight is still upon us so let's see that axe of yours chopping some more wood.",
"We need to get this wagon filled by the end of the day. So back to work with you. Chop, chop!"
]

RAELEN_EMOTES = [ 25, 1, 5 ]

NPC_ID_SUPERVISOR_RAELEN = 10616
NPC_ID_EASTVALE_PEASANT = 11328

RAELEN_STATE = {}

class SupervisorRaelenCreatureScript( CreatureScript ):

     isEnabled = True
     timerToEnable = 20

     def __init__( self, unit ):
          CreatureScript.__init__( self, unit )

     def OnLoad( self ):
          npc = self.creature
          npc.RegisterAIUpdateEvent( 1000 )
          self.isEnabled = True

     def AIUpdate( self ):
          
          if self.isEnabled == False:
               self.timerToEnable = self.timerToEnable - 1
               if self.timerToEnable <= 0:
                    self.isEnabled = True
               return
          
          npc = self.creature
          objects = npc.getObjectsInRange() 
          for o in objects:
               c = arcemu.toCreature( o )
               if c is not None:
                    entry = c.getUInt32Value( arcemu.OBJECT_FIELD_ENTRY )
                    if entry == NPC_ID_EASTVALE_PEASANT:
                         distance = npc.calcDistance( c )
                         if distance < 4:
                              i = Math.randomUInt( 2 )
                              npc.sendChatMessage( arcemu.CHAT_MSG_MONSTER_SAY, arcemu.LANG_COMMON, RAELEN_TEXTS[ Math.randomUInt( i ) ] )
                              npc.emote( RAELEN_EMOTES[ Math.randomUInt( i ) ], 0 )
                              self.isEnabled = False
                              self.timerToEnable = 20

     @staticmethod
     def create( unit ):
          return SupervisorRaelenCreatureScript( unit )

arcemu.RegisterCreatureScript( NPC_ID_SUPERVISOR_RAELEN, SupervisorRaelenCreatureScript.create )